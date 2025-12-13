# @toko/shared-types

Shared TypeScript types and Zod schemas for **TOKO ANAK BANGSA** - Multi-tenant POS & Marketplace Platform.

## Overview

This package provides type-safe data schemas and validation using [Zod](https://zod.dev/). All schemas are validated at runtime and provide TypeScript type inference for compile-time type safety.

## Installation

This package is part of the monorepo and is automatically available to all apps via the workspace.

```bash
pnpm add @toko/shared-types
```

## Usage

### Basic Import

```typescript
import { ProductSchema, CreateProductInput, z } from '@toko/shared-types';

// Validate data
const product = ProductSchema.parse(data);

// Type-safe input
const input: CreateProductInput = {
  name: 'Laptop Asus ROG',
  categoryId: 'uuid-here',
  sellingPrice: 15000000,
  stockQuantity: 10,
};

// Validate with error handling
const result = ProductSchema.safeParse(data);
if (result.success) {
  console.log('Valid product:', result.data);
} else {
  console.error('Validation errors:', result.error.errors);
}
```

### Common Patterns

#### API Response Validation

```typescript
import { ApiResponseSchema, ProductSchema } from '@toko/shared-types';

// Define response schema
const ProductResponseSchema = ApiResponseSchema(ProductSchema);

// Validate API response
const response = await fetch('/api/products/123');
const data = await response.json();
const validated = ProductResponseSchema.parse(data);

if (validated.success) {
  console.log('Product:', validated.data);
} else {
  console.error('Error:', validated.error);
}
```

#### Paginated Lists

```typescript
import { PaginatedResponseSchema, ProductSchema } from '@toko/shared-types';

const ProductListSchema = PaginatedResponseSchema(ProductSchema);

const response = await fetch('/api/products?page=1&limit=20');
const data = await response.json();
const validated = ProductListSchema.parse(data);

console.log('Products:', validated.data);
console.log('Total:', validated.meta.total);
console.log('Has next page:', validated.meta.hasNext);
```

#### Form Validation (React Hook Form)

```typescript
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { CreateProductInputSchema, CreateProductInput } from '@toko/shared-types';

function ProductForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CreateProductInput>({
    resolver: zodResolver(CreateProductInputSchema),
  });

  const onSubmit = (data: CreateProductInput) => {
    // Data is already validated
    console.log('Valid data:', data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('name')} />
      {errors.name && <span>{errors.name.message}</span>}
      {/* ... */}
    </form>
  );
}
```

#### Server-side Validation (Flask API)

```python
# Python equivalent using pydantic (similar to Zod)
from pydantic import BaseModel, validator

class CreateProductInput(BaseModel):
    name: str
    category_id: str
    selling_price: float
    stock_quantity: int

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or len(v) < 1:
            raise ValueError('Product name is required')
        return v
```

## Available Schemas

### Tenant Schemas
- `TenantSchema` - Complete tenant/store data
- `CreateTenantInputSchema` - Input for creating a tenant
- `UpdateTenantInputSchema` - Input for updating a tenant
- `TenantStatusSchema` - Enum: active, suspended, pending, closed
- `SubscriptionPlanSchema` - Enum: free, basic, professional, enterprise
- `BusinessTypeSchema` - Enum: retail, wholesale, restaurant, etc.

### User Schemas
- `UserSchema` - Complete user profile with multi-tenant memberships
- `UserRoleSchema` - Enum: owner, admin, cashier, viewer
- `UserPermissionsSchema` - Granular permission flags
- `TenantMemberSchema` - User's role within a specific tenant
- `CreateUserInputSchema` - Input for user registration
- `InviteUserInputSchema` - Input for inviting users to a tenant
- Helper: `getDefaultPermissionsByRole(role)` - Get default permissions

### Product Schemas
- `ProductSchema` - Complete product data with variants
- `ProductVariantSchema` - Product variant (size, color, etc.)
- `ProductCategorySchema` - Product category/subcategory
- `ProductUnitSchema` - Measurement units (pcs, kg, liter, etc.)
- `CreateProductInputSchema` - Input for creating products
- `UpdateProductInputSchema` - Input for updating products
- `ProductQuerySchema` - Filter/search/pagination parameters
- `ProductStatusSchema` - Enum: active, inactive, out_of_stock, discontinued

### Order Schemas
- `OrderSchema` - Complete order/sale data
- `OrderLineItemSchema` - Individual product in an order
- `PaymentDetailsSchema` - Payment information and breakdown
- `ShippingAddressSchema` - Delivery address
- `CreateOrderInputSchema` - Input for creating orders
- `UpdateOrderStatusInputSchema` - Input for status updates
- `ProcessPaymentInputSchema` - Input for payment processing
- `RefundOrderInputSchema` - Input for refunds
- `OrderQuerySchema` - Filter/search parameters
- `OrderStatusSchema` - Enum: pending, confirmed, processing, ready, completed, cancelled, refunded
- `PaymentMethodSchema` - Enum: cash, debit_card, credit_card, e_wallet, bank_transfer, qris
- `OrderTypeSchema` - Enum: pos, online, marketplace, wholesale

### Customer Schemas
- `CustomerSchema` - Complete customer profile
- `CustomerAddressSchema` - Customer address with coordinates
- `CustomerLoyaltySchema` - Loyalty points and tier
- `CreateCustomerInputSchema` - Input for creating customers
- `UpdateCustomerInputSchema` - Input for updating customers
- `AddCustomerAddressInputSchema` - Input for adding addresses
- `CustomerQuerySchema` - Filter/search parameters
- `CustomerTypeSchema` - Enum: retail, wholesale, regular, vip
- `CustomerStatusSchema` - Enum: active, inactive, blocked

### Common Schemas
- `PaginationMetaSchema` - Pagination metadata
- `PaginatedResponseSchema<T>` - Generic paginated response
- `ApiResponseSchema<T>` - Generic API response wrapper
- `SuccessResponseSchema<T>` - Success response
- `ErrorResponseSchema` - Error response
- `IdParamSchema` - UUID parameter validation
- `SlugParamSchema` - Slug parameter validation
- `DateRangeSchema` - Date range filter
- `SortSchema` - Sort parameters
- `FileUploadSchema` - File upload metadata
- `ImageUploadSchema` - Image upload with dimensions
- `AuditLogSchema` - Audit trail entry
- `NotificationSchema` - User notification
- `ActivityLogSchema` - Activity feed entry
- `SettingsSchema` - Key-value settings

## Type Inference

All schemas automatically generate TypeScript types:

```typescript
import { ProductSchema, Product } from '@toko/shared-types';

// These are equivalent:
type Product1 = z.infer<typeof ProductSchema>;
type Product2 = Product; // Exported type

// Both give you full type safety
const product: Product = {
  id: 'uuid',
  tenantId: 'uuid',
  name: 'Laptop',
  // ... TypeScript will enforce all required fields
};
```

## Validation Helpers

### Safe Parse (No Exceptions)

```typescript
import { ProductSchema } from '@toko/shared-types';

const result = ProductSchema.safeParse(data);

if (result.success) {
  // result.data is fully typed and valid
  console.log(result.data);
} else {
  // result.error contains validation errors
  console.error(result.error.errors);
}
```

### Strict Parse (Throws Exception)

```typescript
import { ProductSchema } from '@toko/shared-types';

try {
  const product = ProductSchema.parse(data);
  // product is fully typed and valid
} catch (error) {
  // Handle validation error
  console.error(error);
}
```

### Partial Validation

```typescript
import { UpdateProductInputSchema } from '@toko/shared-types';

// Only validates fields that are present
const updates = UpdateProductInputSchema.parse({
  name: 'New Name',
  // Other fields are optional
});
```

## Multi-tenant Considerations

All main entities include `tenantId` for data isolation:

```typescript
// Products are scoped to a tenant
const product = {
  tenantId: 'tenant-uuid',
  name: 'Product Name',
  // ...
};

// Users have memberships in multiple tenants
const user = {
  id: 'user-uuid',
  email: 'user@example.com',
  tenants: [
    { tenantId: 'tenant-1', role: 'owner' },
    { tenantId: 'tenant-2', role: 'cashier' },
  ],
};
```

## Indonesian Business Context

The schemas include Indonesian-specific features:

- Default currency: IDR
- Default timezone: Asia/Jakarta
- Default language: id (Indonesian)
- Default tax rate: 11% (PPN)
- NPWP field for business tax ID
- Province-based addressing
- QRIS payment method support

## Development

### Building

```bash
# Build once
pnpm build

# Watch mode
pnpm dev
```

### Type Checking

```bash
pnpm typecheck
```

### Linting

```bash
pnpm lint
```

## Integration with Other Packages

### With @toko/firebase-client

```typescript
import { firebaseDb } from '@toko/firebase-client';
import { ProductSchema } from '@toko/shared-types';
import { collection, addDoc } from 'firebase/firestore';

// Type-safe Firestore operations
const productsRef = collection(firebaseDb, 'products');

// Validate before saving
const productData = ProductSchema.parse(input);
await addDoc(productsRef, productData);
```

### With Flask API

The schemas should be mirrored in your Flask API using Pydantic for server-side validation:

```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateProductInput(BaseModel):
    name: str
    category_id: str
    selling_price: float
    stock_quantity: int = 0
    # ... mirror the Zod schema
```

## Best Practices

1. **Always validate external data** - Never trust user input or API responses
2. **Use TypeScript types** - Let TypeScript enforce types at compile time
3. **Prefer safeParse** - Use `safeParse()` instead of `parse()` to avoid exceptions
4. **Validate early** - Validate at API boundaries (forms, API routes)
5. **Keep schemas DRY** - Reuse base schemas with `.extend()`, `.omit()`, `.partial()`
6. **Document custom validations** - Add comments for business logic validations

## License

Private - TOKO ANAK BANGSA
