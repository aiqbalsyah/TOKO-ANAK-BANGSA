# Shared Types - Development Setup Guide

**Project**: Shared Types Library
**Tech Stack**: TypeScript, Zod, tsup
**Purpose**: Centralized TypeScript types and Zod validation schemas for all TOKO ANAK BANGSA applications

---

## Overview

`@toko/shared-types` is a shared package that provides TypeScript type definitions and Zod validation schemas used across all applications in the monorepo. It ensures type consistency between frontend apps, backend API, and enforces runtime validation.

**Why a Shared Types Package?**
- **Consistency**: Single source of truth for all data types
- **Type Safety**: Shared types prevent type mismatches between frontend and backend
- **Runtime Validation**: Zod schemas validate data at runtime
- **DRY**: Define types once, use everywhere
- **Refactoring**: Update types in one place, all apps benefit

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js 22+** - [Download Node.js](https://nodejs.org/)
- **pnpm 9+** - Install: `npm install -g pnpm`
- **TypeScript knowledge** - This is a TypeScript library
- **Zod knowledge** - For schema validation

---

## Initial Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd pos_app_v1
```

### 2. Install Dependencies

From the **project root** (monorepo):

```bash
# Install all dependencies for all apps/packages
pnpm install
```

This will install dependencies for this package and all consuming apps.

### 3. Package Structure

```
packages/shared-types/
├── src/                    # Source code
│   ├── index.ts            # Main export file
│   ├── tenant.ts           # Tenant types & schemas
│   ├── user.ts             # User types & schemas
│   ├── product.ts          # Product types & schemas
│   ├── inventory.ts        # Inventory types & schemas
│   ├── order.ts            # Order types & schemas
│   ├── customer.ts         # Customer types & schemas
│   ├── supplier.ts         # Supplier types & schemas
│   ├── payment.ts          # Payment types & schemas
│   ├── financial.ts        # Financial types & schemas
│   ├── notification.ts     # Notification types & schemas
│   ├── common.ts           # Common/shared types
│   └── enums.ts            # Enumerations
├── dist/                   # Build output (generated)
│   ├── index.js            # CommonJS build
│   ├── index.mjs           # ESM build
│   └── index.d.ts          # Type definitions
├── docs/                   # Documentation
│   └── dev-guide/          # Developer guides
├── package.json            # Package configuration
├── tsconfig.json           # TypeScript configuration
└── README.md               # Package overview
```

---

## Development Workflow

### 1. Build Package

**Development mode (watch):**
```bash
cd packages/shared-types
pnpm dev
```

This will build the package and watch for changes, automatically rebuilding when you edit source files.

**Production build:**
```bash
pnpm build
```

### 2. Add New Dependency

```bash
cd packages/shared-types
pnpm add package-name
```

### 3. Type Checking

```bash
pnpm typecheck
```

### 4. Linting

```bash
pnpm lint
```

### 5. Clean Build Artifacts

```bash
pnpm clean
```

---

## Package Configuration

### Build Setup (tsup)

The package uses `tsup` for building. Configuration in `package.json`:

```json
{
  "scripts": {
    "build": "tsup src/index.ts --format cjs,esm --dts",
    "dev": "tsup src/index.ts --format cjs,esm --dts --watch"
  }
}
```

**Output formats:**
- **CommonJS** (`dist/index.js`) - For Node.js/older bundlers
- **ESM** (`dist/index.mjs`) - For modern bundlers
- **TypeScript declarations** (`dist/index.d.ts`) - For type checking

### Package Exports

```json
{
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  }
}
```

---

## Using the Package in Apps

### Installation

Apps in the monorepo reference this package via workspace protocol:

```json
{
  "dependencies": {
    "@toko/shared-types": "workspace:*"
  }
}
```

### Import in Applications

**Frontend (Next.js apps):**
```typescript
import {
  Product,
  ProductSchema,
  Order,
  OrderSchema,
  Customer,
  Tenant
} from '@toko/shared-types';
```

**Backend (Flask API):**
```python
# Python apps can reference TypeScript types for documentation purposes
# But need to define their own Python types/Pydantic models
```

---

## Implementation Examples

### Example: Product Types & Schemas

```typescript
// src/product.ts
import { z } from 'zod';

// Zod schema (runtime validation)
export const ProductSchema = z.object({
  id: z.string(),
  tenantId: z.string(),
  name: z.string().min(1).max(255),
  description: z.string().optional(),
  sku: z.string().optional(),
  barcode: z.string().optional(),
  categoryId: z.string(),
  brandId: z.string().optional(),
  price: z.number().positive(),
  cost: z.number().nonnegative().optional(),
  stock: z.number().int().nonnegative(),
  minStock: z.number().int().nonnegative().default(0),
  maxStock: z.number().int().nonnegative().optional(),
  unit: z.string().default('PCS'),
  images: z.array(z.string()).default([]),
  isActive: z.boolean().default(true),
  createdAt: z.string(),
  updatedAt: z.string(),
});

// TypeScript type (derived from schema)
export type Product = z.infer<typeof ProductSchema>;

// Create/Update DTOs
export const CreateProductSchema = ProductSchema.omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

export type CreateProductDTO = z.infer<typeof CreateProductSchema>;

export const UpdateProductSchema = CreateProductSchema.partial();

export type UpdateProductDTO = z.infer<typeof UpdateProductSchema>;

// Product with variants
export const ProductVariantSchema = z.object({
  id: z.string(),
  productId: z.string(),
  name: z.string(),
  sku: z.string().optional(),
  barcode: z.string().optional(),
  price: z.number().positive(),
  stock: z.number().int().nonnegative(),
  attributes: z.record(z.string()).optional(),
});

export type ProductVariant = z.infer<typeof ProductVariantSchema>;
```

### Example: Order Types & Schemas

```typescript
// src/order.ts
import { z } from 'zod';
import { OrderStatus, PaymentStatus, PaymentMethod } from './enums';

export const OrderItemSchema = z.object({
  productId: z.string(),
  productName: z.string(),
  sku: z.string().optional(),
  quantity: z.number().int().positive(),
  price: z.number().positive(),
  discount: z.number().nonnegative().default(0),
  subtotal: z.number().nonnegative(),
});

export type OrderItem = z.infer<typeof OrderItemSchema>;

export const OrderSchema = z.object({
  id: z.string(),
  tenantId: z.string(),
  orderNumber: z.string(),
  customerId: z.string().optional(),
  customerName: z.string().optional(),
  customerEmail: z.string().email().optional(),
  customerPhone: z.string().optional(),
  items: z.array(OrderItemSchema),
  subtotal: z.number().nonnegative(),
  tax: z.number().nonnegative().default(0),
  discount: z.number().nonnegative().default(0),
  shippingCost: z.number().nonnegative().default(0),
  total: z.number().nonnegative(),
  status: z.nativeEnum(OrderStatus),
  paymentStatus: z.nativeEnum(PaymentStatus),
  paymentMethod: z.nativeEnum(PaymentMethod),
  shippingAddress: z.object({
    street: z.string(),
    city: z.string(),
    province: z.string(),
    postalCode: z.string(),
    country: z.string().default('Indonesia'),
  }).optional(),
  notes: z.string().optional(),
  createdAt: z.string(),
  updatedAt: z.string(),
});

export type Order = z.infer<typeof OrderSchema>;

export const CreateOrderSchema = OrderSchema.omit({
  id: true,
  orderNumber: true,
  createdAt: true,
  updatedAt: true,
});

export type CreateOrderDTO = z.infer<typeof CreateOrderSchema>;
```

### Example: Customer Types & Schemas

```typescript
// src/customer.ts
import { z } from 'zod';
import { CustomerTier, CustomerStatus } from './enums';

export const CustomerSchema = z.object({
  id: z.string(),
  tenantId: z.string(),
  name: z.string().min(1).max(255),
  email: z.string().email().optional(),
  phone: z.string().min(10).max(15),
  address: z.string().optional(),
  city: z.string().optional(),
  province: z.string().optional(),
  tier: z.nativeEnum(CustomerTier).default(CustomerTier.Regular),
  status: z.nativeEnum(CustomerStatus).default(CustomerStatus.Active),
  creditLimit: z.number().nonnegative().default(0),
  currentDebt: z.number().nonnegative().default(0),
  totalPurchases: z.number().nonnegative().default(0),
  lastPurchaseAt: z.string().optional(),
  notes: z.string().optional(),
  createdAt: z.string(),
  updatedAt: z.string(),
});

export type Customer = z.infer<typeof CustomerSchema>;

export const CreateCustomerSchema = CustomerSchema.omit({
  id: true,
  totalPurchases: true,
  currentDebt: true,
  lastPurchaseAt: true,
  createdAt: true,
  updatedAt: true,
});

export type CreateCustomerDTO = z.infer<typeof CreateCustomerSchema>;
```

### Example: Enumerations

```typescript
// src/enums.ts

// Customer enums
export enum CustomerTier {
  Regular = 'REGULAR',
  Wholesaler = 'WHOLESALER',
  Reseller = 'RESELLER',
}

export enum CustomerStatus {
  Active = 'ACTIVE',
  Inactive = 'INACTIVE',
  Blocked = 'BLOCKED',
}

// Order enums
export enum OrderStatus {
  Pending = 'PENDING',
  Processing = 'PROCESSING',
  Shipped = 'SHIPPED',
  Delivered = 'DELIVERED',
  Cancelled = 'CANCELLED',
}

export enum PaymentStatus {
  Pending = 'PENDING',
  Paid = 'PAID',
  PartiallyPaid = 'PARTIALLY_PAID',
  Refunded = 'REFUNDED',
  Failed = 'FAILED',
}

export enum PaymentMethod {
  Cash = 'CASH',
  BankTransfer = 'BANK_TRANSFER',
  Credit = 'CREDIT',
  EWallet = 'E_WALLET',
  QRIS = 'QRIS',
}

// User enums
export enum UserRole {
  Owner = 'OWNER',
  Manager = 'MANAGER',
  Cashier = 'CASHIER',
  Staff = 'STAFF',
}

export enum UserStatus {
  Active = 'ACTIVE',
  Inactive = 'INACTIVE',
  Suspended = 'SUSPENDED',
}

// Subscription enums
export enum SubscriptionPlan {
  Free = 'FREE',
  Basic = 'BASIC',
  Pro = 'PRO',
  Enterprise = 'ENTERPRISE',
}

export enum SubscriptionStatus {
  Active = 'ACTIVE',
  Trial = 'TRIAL',
  Expired = 'EXPIRED',
  Cancelled = 'CANCELLED',
}
```

### Example: Common Types

```typescript
// src/common.ts
import { z } from 'zod';

// Pagination
export const PaginationSchema = z.object({
  page: z.number().int().positive().default(1),
  limit: z.number().int().positive().max(100).default(20),
  total: z.number().int().nonnegative(),
});

export type Pagination = z.infer<typeof PaginationSchema>;

// API Response
export const ApiResponseSchema = z.object({
  success: z.boolean(),
  data: z.any().optional(),
  error: z.string().optional(),
  message: z.string().optional(),
});

export type ApiResponse<T = any> = {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
};

// Timestamps
export interface Timestamps {
  createdAt: string;
  updatedAt: string;
}

// Soft Delete
export interface SoftDelete {
  deletedAt: string | null;
}

// Tenant Isolation
export interface TenantIsolated {
  tenantId: string;
}

// Audit Log
export interface AuditLog {
  userId: string;
  action: string;
  targetType: string;
  targetId: string;
  changes: Record<string, any>;
  timestamp: string;
  ipAddress?: string;
}
```

### Example: Main Export File

```typescript
// src/index.ts

// Product types
export * from './product';

// Order types
export * from './order';

// Customer types
export * from './customer';

// User types
export * from './user';

// Tenant types
export * from './tenant';

// Supplier types
export * from './supplier';

// Inventory types
export * from './inventory';

// Payment types
export * from './payment';

// Financial types
export * from './financial';

// Notification types
export * from './notification';

// Common types
export * from './common';

// Enums
export * from './enums';
```

---

## Usage in Applications

### Example: Validating API Request (Frontend)

```typescript
// apps/store-portal/app/api/products/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { CreateProductSchema } from '@toko/shared-types';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    // Validate request body with Zod schema
    const validatedData = CreateProductSchema.parse(body);

    // Now validatedData is type-safe and validated
    // Proceed with creating product...

    return NextResponse.json({ success: true, data: validatedData });
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { success: false, error: error.errors },
        { status: 400 }
      );
    }

    return NextResponse.json(
      { success: false, error: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

### Example: Using Types in Components

```tsx
// apps/store-portal/components/products/ProductCard.tsx
import { Product } from '@toko/shared-types';

interface ProductCardProps {
  product: Product;
  onEdit: (product: Product) => void;
  onDelete: (productId: string) => void;
}

export function ProductCard({ product, onEdit, onDelete }: ProductCardProps) {
  return (
    <div>
      <h3>{product.name}</h3>
      <p>IDR {product.price.toLocaleString('id-ID')}</p>
      <p>Stock: {product.stock} {product.unit}</p>
      <button onClick={() => onEdit(product)}>Edit</button>
      <button onClick={() => onDelete(product.id)}>Delete</button>
    </div>
  );
}
```

### Example: API Client with Types

```typescript
// apps/store-portal/lib/api.ts
import { Product, CreateProductDTO, UpdateProductDTO } from '@toko/shared-types';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const getProducts = async (): Promise<Product[]> => {
  const response = await fetch(`${API_URL}/products`);
  const data = await response.json();
  return data.products;
};

export const createProduct = async (data: CreateProductDTO): Promise<Product> => {
  const response = await fetch(`${API_URL}/products`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const result = await response.json();
  return result.data;
};

export const updateProduct = async (
  id: string,
  data: UpdateProductDTO
): Promise<Product> => {
  const response = await fetch(`${API_URL}/products/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const result = await response.json();
  return result.data;
};
```

---

## Best Practices

### 1. Schema-First Design

Define Zod schemas first, then derive TypeScript types:

```typescript
// ✅ Good: Schema first, type derived
export const ProductSchema = z.object({ ... });
export type Product = z.infer<typeof ProductSchema>;

// ❌ Bad: Type first, no runtime validation
export type Product = { ... };
```

### 2. Use DTOs for Create/Update

```typescript
// Create DTO (omit auto-generated fields)
export const CreateProductSchema = ProductSchema.omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

// Update DTO (all fields optional)
export const UpdateProductSchema = CreateProductSchema.partial();
```

### 3. Export Both Schema and Type

```typescript
// Always export both
export const ProductSchema = z.object({ ... });
export type Product = z.infer<typeof ProductSchema>;
```

### 4. Use Enums for Constants

```typescript
// ✅ Good: TypeScript enum
export enum OrderStatus {
  Pending = 'PENDING',
  Processing = 'PROCESSING',
}

// ❌ Bad: String literals (no autocomplete)
export type OrderStatus = 'PENDING' | 'PROCESSING';
```

### 5. Document Complex Types

```typescript
/**
 * Product entity representing an item in the inventory
 *
 * @property id - Unique product identifier
 * @property tenantId - Tenant that owns this product
 * @property name - Product name (1-255 characters)
 * @property price - Selling price (must be positive)
 * @property stock - Current stock level
 */
export type Product = z.infer<typeof ProductSchema>;
```

---

## Testing

### Example: Testing Schemas

```typescript
// src/__tests__/product.test.ts
import { describe, it, expect } from 'vitest';
import { ProductSchema, CreateProductSchema } from '../product';

describe('Product schemas', () => {
  it('should validate valid product', () => {
    const validProduct = {
      id: '123',
      tenantId: 'tenant-1',
      name: 'Indomie Goreng',
      categoryId: 'cat-1',
      price: 3000,
      stock: 100,
      unit: 'PCS',
      images: [],
      isActive: true,
      createdAt: '2024-12-13T00:00:00Z',
      updatedAt: '2024-12-13T00:00:00Z',
    };

    const result = ProductSchema.safeParse(validProduct);
    expect(result.success).toBe(true);
  });

  it('should reject invalid price', () => {
    const invalidProduct = {
      // ... other fields
      price: -100, // Invalid: negative price
    };

    const result = ProductSchema.safeParse(invalidProduct);
    expect(result.success).toBe(false);
  });
});
```

---

## Common Issues & Troubleshooting

### Issue: Apps not picking up type changes

**Solution:** Rebuild the package:
```bash
cd packages/shared-types
pnpm build
```

### Issue: Zod validation errors

**Solution:** Check error details:
```typescript
const result = ProductSchema.safeParse(data);
if (!result.success) {
  console.log(result.error.errors);
}
```

### Issue: Circular dependencies

**Solution:** Separate types into smaller modules and import carefully

### Issue: Type inference not working

**Solution:** Explicitly use `z.infer`:
```typescript
export type Product = z.infer<typeof ProductSchema>;
```

---

## Useful Commands

```bash
# Build package
pnpm build

# Watch mode (development)
pnpm dev

# Type check
pnpm typecheck

# Lint
pnpm lint

# Clean build artifacts
pnpm clean

# Run tests
pnpm test

# Build from project root
pnpm build --filter @toko/shared-types
```

---

## Next Steps

1. Review Zod documentation: https://zod.dev
2. Add types for all domain entities
3. Write comprehensive tests for all schemas
4. Document complex types with JSDoc
5. Keep types in sync with backend API and database schema

---

**Last Updated**: 2024-12-13
