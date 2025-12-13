# Modular Architecture - Services & Components

**Goal**: Build maintainable, testable, and reusable features using modular services and component-based design

---

## Architecture Principles

### 1. Separation of Concerns

Each module should have a single, well-defined responsibility:

- **Services**: Business logic, data access, external integrations
- **Components**: UI rendering, user interactions
- **Utilities**: Pure functions, helpers
- **Types**: Data models, interfaces

### 2. Dependency Injection

Services should be injectable and mockable for testing:

```typescript
// ❌ Bad: Direct instantiation
class OrderService {
  private paymentService = new PaymentService();

  async createOrder() {
    await this.paymentService.process();
  }
}

// ✅ Good: Dependency injection
class OrderService {
  constructor(private paymentService: PaymentService) {}

  async createOrder() {
    await this.paymentService.process();
  }
}
```

### 3. Interface-Based Design

Define interfaces for services to enable swapping implementations:

```typescript
// Define interface
interface PaymentGateway {
  processPayment(amount: number): Promise<PaymentResult>;
  refundPayment(transactionId: string): Promise<void>;
}

// Multiple implementations
class MidtransGateway implements PaymentGateway {
  async processPayment(amount: number) { /* ... */ }
  async refundPayment(transactionId: string) { /* ... */ }
}

class StripeGateway implements PaymentGateway {
  async processPayment(amount: number) { /* ... */ }
  async refundPayment(transactionId: string) { /* ... */ }
}

// Service uses interface, not concrete implementation
class CheckoutService {
  constructor(private paymentGateway: PaymentGateway) {}
}
```

---

## Module Structure

### Directory Organization

```
packages/
├── shared-types/              # Shared data models
│   ├── src/
│   │   ├── product.ts        # Product types & schemas
│   │   ├── order.ts          # Order types & schemas
│   │   ├── customer.ts       # Customer types & schemas
│   │   └── index.ts
│   └── package.json
│
├── firebase-client/           # Firebase SDK wrapper
│   ├── src/
│   │   ├── firestore/
│   │   │   ├── products.ts   # Product Firestore operations
│   │   │   ├── orders.ts     # Order Firestore operations
│   │   │   └── index.ts
│   │   ├── auth/
│   │   │   ├── auth-service.ts
│   │   │   └── index.ts
│   │   ├── storage/
│   │   │   ├── upload.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   └── package.json
│
├── business-logic/            # Core business services
│   ├── src/
│   │   ├── services/
│   │   │   ├── product/
│   │   │   │   ├── product.service.ts
│   │   │   │   ├── pricing.service.ts
│   │   │   │   └── unit-conversion.service.ts
│   │   │   ├── order/
│   │   │   │   ├── order.service.ts
│   │   │   │   ├── checkout.service.ts
│   │   │   │   └── pos.service.ts
│   │   │   ├── payment/
│   │   │   │   ├── midtrans.service.ts
│   │   │   │   ├── cash.service.ts
│   │   │   │   └── payment-factory.ts
│   │   │   └── shipping/
│   │   │       ├── rajaongkir.service.ts
│   │   │       └── shipping.service.ts
│   │   ├── interfaces/        # Service interfaces
│   │   │   ├── payment-gateway.interface.ts
│   │   │   ├── shipping-provider.interface.ts
│   │   │   └── notification-service.interface.ts
│   │   └── index.ts
│   └── package.json
│
└── ui-web/                    # Shared UI components
    ├── src/
    │   ├── components/
    │   │   ├── product/
    │   │   │   ├── ProductCard.tsx
    │   │   │   ├── ProductForm.tsx
    │   │   │   └── PricingTierInput.tsx
    │   │   ├── order/
    │   │   │   ├── OrderList.tsx
    │   │   │   ├── OrderCard.tsx
    │   │   │   └── OrderStatusBadge.tsx
    │   │   ├── pos/
    │   │   │   ├── POSCart.tsx
    │   │   │   ├── ProductSearch.tsx
    │   │   │   └── PaymentModal.tsx
    │   │   └── common/
    │   │       ├── Button.tsx
    │   │       ├── Input.tsx
    │   │       └── Modal.tsx
    │   ├── hooks/
    │   │   ├── useProducts.ts
    │   │   ├── useOrders.ts
    │   │   └── usePOSCart.ts
    │   └── index.ts
    └── package.json
```

---

## Service Layer Pattern

### Product Service Example

```typescript
// packages/business-logic/src/services/product/product.service.ts

import { db } from '@pos/firebase-client';
import { Product, ProductSchema } from '@pos/shared-types';
import { PricingService } from './pricing.service';
import { UnitConversionService } from './unit-conversion.service';

export class ProductService {
  constructor(
    private pricingService: PricingService,
    private unitConversionService: UnitConversionService
  ) {}

  /**
   * Create a new product
   */
  async createProduct(
    tenantId: string,
    data: Omit<Product, 'id' | 'createdAt' | 'updatedAt'>
  ): Promise<Product> {
    // Validate input
    const validated = ProductSchema.parse(data);

    // Calculate profit margins for all pricing tiers
    const pricingWithMargins = this.pricingService.calculateMargins({
      cost: validated.cost,
      priceA: validated.priceA,
      priceB: validated.priceB,
      priceC: validated.priceC,
    });

    // Create product document
    const productRef = db
      .collection(`tenants/${tenantId}/products`)
      .doc();

    const product: Product = {
      ...validated,
      id: productRef.id,
      ...pricingWithMargins,
      createdAt: new Date(),
      updatedAt: new Date(),
    };

    await productRef.set(product);

    return product;
  }

  /**
   * Get product price for specific customer type and unit
   */
  async getPrice(
    productId: string,
    tenantId: string,
    unit: 'DUS' | 'PACK' | 'PCS',
    customerType: 'A' | 'B' | 'C'
  ): Promise<number> {
    const product = await this.getProduct(productId, tenantId);

    // Get base price for customer type
    const basePrice = this.pricingService.getPrice(product, customerType);

    // Convert price based on unit
    return this.unitConversionService.convertPrice(
      product,
      basePrice,
      unit
    );
  }

  /**
   * Get product by ID
   */
  async getProduct(
    productId: string,
    tenantId: string
  ): Promise<Product> {
    const doc = await db
      .collection(`tenants/${tenantId}/products`)
      .doc(productId)
      .get();

    if (!doc.exists) {
      throw new Error(`Product ${productId} not found`);
    }

    return doc.data() as Product;
  }

  /**
   * Update product inventory
   */
  async updateInventory(
    productId: string,
    tenantId: string,
    quantity: number,
    unit: 'DUS' | 'PACK' | 'PCS'
  ): Promise<void> {
    // Convert to base unit (PCS)
    const product = await this.getProduct(productId, tenantId);
    const quantityInPCS = this.unitConversionService.toBaseUnit(
      product,
      quantity,
      unit
    );

    // Update inventory
    await db
      .collection(`tenants/${tenantId}/products`)
      .doc(productId)
      .update({
        inventory: admin.firestore.FieldValue.increment(quantityInPCS),
        updatedAt: new Date(),
      });
  }
}
```

### Pricing Service (Supporting Service)

```typescript
// packages/business-logic/src/services/product/pricing.service.ts

import { Product } from '@pos/shared-types';

export class PricingService {
  /**
   * Calculate profit margins for all pricing tiers
   */
  calculateMargins(pricing: {
    cost: number;
    priceA: number;
    priceB: number;
    priceC: number;
  }) {
    return {
      marginA: this.calculateMargin(pricing.cost, pricing.priceA),
      marginB: this.calculateMargin(pricing.cost, pricing.priceB),
      marginC: this.calculateMargin(pricing.cost, pricing.priceC),
    };
  }

  /**
   * Calculate profit margin percentage
   */
  private calculateMargin(cost: number, price: number): number {
    if (cost === 0) return 0;
    return ((price - cost) / cost) * 100;
  }

  /**
   * Get price for specific customer type
   */
  getPrice(product: Product, customerType: 'A' | 'B' | 'C'): number {
    switch (customerType) {
      case 'A':
        return product.priceA;
      case 'B':
        return product.priceB;
      case 'C':
        return product.priceC;
      default:
        return product.priceB; // Default to retail
    }
  }
}
```

### Unit Conversion Service

```typescript
// packages/business-logic/src/services/product/unit-conversion.service.ts

import { Product } from '@pos/shared-types';

export class UnitConversionService {
  /**
   * Convert quantity to base unit (PCS)
   */
  toBaseUnit(
    product: Product,
    quantity: number,
    unit: 'DUS' | 'PACK' | 'PCS'
  ): number {
    switch (unit) {
      case 'DUS':
        return quantity * product.unitConversion.dusToPack * product.unitConversion.packToPcs;
      case 'PACK':
        return quantity * product.unitConversion.packToPcs;
      case 'PCS':
        return quantity;
    }
  }

  /**
   * Convert price based on unit
   */
  convertPrice(
    product: Product,
    basePrice: number,
    unit: 'DUS' | 'PACK' | 'PCS'
  ): number {
    const multiplier = this.toBaseUnit(product, 1, unit);
    return basePrice * multiplier;
  }
}
```

---

## Order Service with Payment Factory Pattern

### Payment Gateway Interface

```typescript
// packages/business-logic/src/interfaces/payment-gateway.interface.ts

export interface PaymentResult {
  success: boolean;
  transactionId: string;
  amount: number;
  method: string;
  details?: any;
}

export interface PaymentGateway {
  /**
   * Process payment
   */
  processPayment(params: {
    amount: number;
    orderId: string;
    customerId?: string;
    metadata?: Record<string, any>;
  }): Promise<PaymentResult>;

  /**
   * Verify payment status
   */
  verifyPayment(transactionId: string): Promise<PaymentResult>;

  /**
   * Refund payment
   */
  refundPayment(transactionId: string, amount?: number): Promise<void>;
}
```

### Payment Implementations

```typescript
// packages/business-logic/src/services/payment/midtrans.service.ts

import { PaymentGateway, PaymentResult } from '../../interfaces/payment-gateway.interface';

export class MidtransService implements PaymentGateway {
  async processPayment(params: {
    amount: number;
    orderId: string;
    customerId?: string;
  }): Promise<PaymentResult> {
    // Call Midtrans API
    const response = await fetch('https://api.midtrans.com/v2/charge', {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${process.env.MIDTRANS_SERVER_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        transaction_details: {
          order_id: params.orderId,
          gross_amount: params.amount,
        },
        customer_details: {
          customer_id: params.customerId,
        },
      }),
    });

    const data = await response.json();

    return {
      success: data.transaction_status === 'settlement',
      transactionId: data.transaction_id,
      amount: params.amount,
      method: 'midtrans',
      details: data,
    };
  }

  async verifyPayment(transactionId: string): Promise<PaymentResult> {
    // Verify with Midtrans
    // ...
  }

  async refundPayment(transactionId: string): Promise<void> {
    // Refund via Midtrans
    // ...
  }
}

// packages/business-logic/src/services/payment/cash.service.ts

export class CashPaymentService implements PaymentGateway {
  async processPayment(params: {
    amount: number;
    orderId: string;
  }): Promise<PaymentResult> {
    // No external API call for cash
    // Just record the payment
    return {
      success: true,
      transactionId: `CASH-${Date.now()}`,
      amount: params.amount,
      method: 'cash',
    };
  }

  async verifyPayment(transactionId: string): Promise<PaymentResult> {
    // Cash payments are always verified (already received)
    return {
      success: true,
      transactionId,
      amount: 0,
      method: 'cash',
    };
  }

  async refundPayment(transactionId: string): Promise<void> {
    // Manual cash refund process
    console.log(`Refund cash payment: ${transactionId}`);
  }
}
```

### Payment Factory

```typescript
// packages/business-logic/src/services/payment/payment-factory.ts

import { PaymentGateway } from '../../interfaces/payment-gateway.interface';
import { MidtransService } from './midtrans.service';
import { CashPaymentService } from './cash.service';

export class PaymentFactory {
  static create(method: 'midtrans' | 'cash' | 'edc' | 'qris'): PaymentGateway {
    switch (method) {
      case 'midtrans':
        return new MidtransService();
      case 'cash':
        return new CashPaymentService();
      // Add more payment methods
      default:
        throw new Error(`Unknown payment method: ${method}`);
    }
  }
}
```

### Order Service Using Payment Factory

```typescript
// packages/business-logic/src/services/order/order.service.ts

import { PaymentFactory } from '../payment/payment-factory';
import { Order } from '@pos/shared-types';

export class OrderService {
  /**
   * Create order with payment
   */
  async createOrder(
    tenantId: string,
    orderData: Omit<Order, 'id'>,
    paymentMethod: 'midtrans' | 'cash' | 'edc'
  ): Promise<Order> {
    // Create payment gateway based on method
    const paymentGateway = PaymentFactory.create(paymentMethod);

    // Process payment
    const paymentResult = await paymentGateway.processPayment({
      amount: orderData.total,
      orderId: orderData.orderNumber,
      customerId: orderData.customer?.id,
    });

    if (!paymentResult.success) {
      throw new Error('Payment failed');
    }

    // Create order in Firestore
    const order: Order = {
      ...orderData,
      payment: {
        method: paymentMethod,
        status: 'paid',
        transactionId: paymentResult.transactionId,
        paidAt: new Date(),
      },
      status: 'completed',
      createdAt: new Date(),
    };

    await db.collection(`tenants/${tenantId}/orders`).add(order);

    return order;
  }
}
```

---

## Component Layer Pattern

### Custom Hooks for Data Fetching

```typescript
// packages/ui-web/src/hooks/useProducts.ts

import { useState, useEffect } from 'react';
import { Product } from '@pos/shared-types';
import { ProductService } from '@pos/business-logic';

export function useProducts(tenantId: string) {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  const productService = new ProductService(
    new PricingService(),
    new UnitConversionService()
  );

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setLoading(true);
        const data = await productService.getProducts(tenantId);
        setProducts(data);
      } catch (err) {
        setError(err as Error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [tenantId]);

  return { products, loading, error };
}
```

### Presentational Component

```typescript
// packages/ui-web/src/components/product/ProductCard.tsx

import { Product } from '@pos/shared-types';

interface ProductCardProps {
  product: Product;
  customerType: 'A' | 'B' | 'C';
  onAddToCart: (productId: string, unit: string) => void;
}

export function ProductCard({
  product,
  customerType,
  onAddToCart,
}: ProductCardProps) {
  const price = customerType === 'A'
    ? product.priceA
    : customerType === 'B'
    ? product.priceB
    : product.priceC;

  return (
    <div className="product-card">
      <img src={product.images[0]} alt={product.name} />
      <h3>{product.name}</h3>
      <p className="price">Rp {price.toLocaleString('id-ID')}</p>

      <div className="unit-selector">
        <button onClick={() => onAddToCart(product.id, 'PCS')}>
          + PCS
        </button>
        <button onClick={() => onAddToCart(product.id, 'PACK')}>
          + PACK
        </button>
        <button onClick={() => onAddToCart(product.id, 'DUS')}>
          + DUS
        </button>
      </div>
    </div>
  );
}
```

### Container Component

```typescript
// apps/marketplace/app/[locale]/products/page.tsx

'use client';

import { useProducts } from '@pos/ui-web/hooks/useProducts';
import { ProductCard } from '@pos/ui-web/components/product/ProductCard';
import { useCart } from '@/hooks/useCart';

export default function ProductsPage() {
  const { products, loading, error } = useProducts('tenant_123');
  const { addToCart } = useCart();

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div className="products-grid">
      {products.map(product => (
        <ProductCard
          key={product.id}
          product={product}
          customerType="B"
          onAddToCart={addToCart}
        />
      ))}
    </div>
  );
}
```

---

## Testing Modular Services

### Unit Testing Services

```typescript
// packages/business-logic/__tests__/services/product/pricing.service.test.ts

import { PricingService } from '../../../src/services/product/pricing.service';

describe('PricingService', () => {
  let pricingService: PricingService;

  beforeEach(() => {
    pricingService = new PricingService();
  });

  describe('calculateMargins', () => {
    it('should calculate correct profit margins', () => {
      const result = pricingService.calculateMargins({
        cost: 1000,
        priceA: 1200,
        priceB: 1300,
        priceC: 1400,
      });

      expect(result.marginA).toBe(20); // (1200-1000)/1000 = 20%
      expect(result.marginB).toBe(30); // (1300-1000)/1000 = 30%
      expect(result.marginC).toBe(40); // (1400-1000)/1000 = 40%
    });

    it('should return 0 margin when cost is 0', () => {
      const result = pricingService.calculateMargins({
        cost: 0,
        priceA: 1000,
        priceB: 1000,
        priceC: 1000,
      });

      expect(result.marginA).toBe(0);
    });
  });
});
```

### Mocking Dependencies

```typescript
// packages/business-logic/__tests__/services/order/order.service.test.ts

import { OrderService } from '../../../src/services/order/order.service';
import { PaymentGateway } from '../../../src/interfaces/payment-gateway.interface';

// Mock payment gateway
class MockPaymentGateway implements PaymentGateway {
  async processPayment() {
    return {
      success: true,
      transactionId: 'TEST-123',
      amount: 100000,
      method: 'mock',
    };
  }

  async verifyPayment() { /* ... */ }
  async refundPayment() { /* ... */ }
}

describe('OrderService', () => {
  it('should create order with successful payment', async () => {
    const mockPayment = new MockPaymentGateway();
    const orderService = new OrderService(mockPayment);

    const order = await orderService.createOrder('tenant_123', {
      orderNumber: 'ORD-001',
      total: 100000,
      // ... other order data
    }, 'mock');

    expect(order.payment.status).toBe('paid');
    expect(order.payment.transactionId).toBe('TEST-123');
  });
});
```

---

## Best Practices

### 1. Single Responsibility Principle

Each service/component should do ONE thing well:

```typescript
// ❌ Bad: Service doing too much
class ProductService {
  createProduct() { /* ... */ }
  uploadImage() { /* ... */ }
  sendEmail() { /* ... */ }
  calculateShipping() { /* ... */ }
}

// ✅ Good: Focused services
class ProductService {
  createProduct() { /* ... */ }
}

class ImageService {
  uploadImage() { /* ... */ }
}

class EmailService {
  sendEmail() { /* ... */ }
}

class ShippingService {
  calculateShipping() { /* ... */ }
}
```

### 2. Dependency Inversion

Depend on abstractions (interfaces), not concretions:

```typescript
// ✅ Good: Depends on interface
class OrderService {
  constructor(
    private paymentGateway: PaymentGateway,  // Interface
    private notificationService: NotificationService  // Interface
  ) {}
}
```

### 3. Avoid God Objects

Break large services into smaller, focused services:

```typescript
// ❌ Bad: God object
class OrderService {
  createOrder() { }
  processPayment() { }
  calculateShipping() { }
  sendNotification() { }
  updateInventory() { }
  generateInvoice() { }
}

// ✅ Good: Composed services
class OrderService {
  constructor(
    private paymentService: PaymentService,
    private shippingService: ShippingService,
    private notificationService: NotificationService,
    private inventoryService: InventoryService,
    private invoiceService: InvoiceService
  ) {}

  async createOrder() {
    await this.paymentService.process();
    await this.shippingService.calculate();
    await this.notificationService.send();
    await this.inventoryService.update();
    await this.invoiceService.generate();
  }
}
```

### 4. Pure Functions Where Possible

```typescript
// ✅ Pure function: Same input = Same output, No side effects
function calculateMargin(cost: number, price: number): number {
  return ((price - cost) / cost) * 100;
}

// ❌ Impure function: Side effects
function calculateMargin(cost: number, price: number): number {
  console.log('Calculating margin');  // Side effect
  globalMarginCache = { cost, price };  // Side effect
  return ((price - cost) / cost) * 100;
}
```

---

## Summary

**Modular Architecture Benefits**:
- ✅ Testable (easy to mock dependencies)
- ✅ Maintainable (single responsibility)
- ✅ Reusable (shared packages)
- ✅ Scalable (add features without modifying existing code)
- ✅ Type-safe (TypeScript interfaces)

**Key Patterns**:
1. Service Layer Pattern
2. Factory Pattern
3. Dependency Injection
4. Interface-Based Design
5. Repository Pattern (Firestore)
6. Container/Presentational Components

---

**Last Updated**: 2024-12-13
