# GitHub Copilot Instructions - TOKO ANAK BANGSA

This file provides context to GitHub Copilot about this project's architecture, conventions, and best practices.

## Project Overview

**TOKO ANAK BANGSA** is a multi-tenant POS & Marketplace platform built with:
- **Monorepo**: Turborepo + pnpm workspaces
- **Frontend**: Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS
- **Backend**: Python 3.12, Flask, Firebase Admin SDK
- **Database**: Firebase Firestore (NoSQL)
- **Authentication**: Firebase Auth

## Architecture

### Monorepo Structure

```
pos_app_v1/
├── apps/
│   ├── api/                    # Flask API (Python 3.12)
│   ├── store-portal/           # Store Portal (Next.js 16) - Port 3000
│   ├── marketplace/            # Marketplace (Next.js 16) - Port 3001
│   ├── company-profile/        # Company Profile (Next.js 16) - Port 3002
│   └── platform-admin/         # Platform Admin (Next.js 16) - Port 3003
├── packages/
│   ├── firebase-client/        # Firebase SDK wrapper
│   ├── shared-types/           # Zod schemas & TypeScript types
│   └── ui-web/                 # shadcn/ui components
```

## Code Generation Guidelines

### Next.js Components

**Always use:**
- Server Components by default (no `'use client'` unless needed)
- Client Components only when using hooks, event handlers, or browser APIs
- App Router file structure: `app/[locale]/(route-group)/page.tsx`
- TypeScript with strict typing
- Tailwind CSS for styling
- Components from `@toko/ui-web` package
- next-intl for internationalization

**Example Page Component:**

```tsx
// app/[locale]/(dashboard)/products/page.tsx
import { getTranslations } from 'next-intl/server';
import { ProductList } from '@/components/products/ProductList';

export default async function ProductsPage() {
  const t = await getTranslations('products');

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">{t('title')}</h1>
      <ProductList />
    </div>
  );
}
```

**Example Client Component:**

```tsx
// components/products/ProductList.tsx
'use client';

import { useState, useEffect } from 'react';
import { useTranslations } from 'next-intl';
import { Button } from '@toko/ui-web';
import { Product } from '@toko/shared-types';

export function ProductList() {
  const t = useTranslations('products');
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    const response = await fetch('/api/products');
    const data = await response.json();
    setProducts(data.products);
  };

  return (
    <div className="grid grid-cols-3 gap-4">
      {products.map((product) => (
        <div key={product.id} className="border rounded-lg p-4">
          <h3 className="font-semibold">{product.name}</h3>
          <p className="text-gray-600">IDR {product.price.toLocaleString('id-ID')}</p>
        </div>
      ))}
    </div>
  );
}
```

### Flask API

**Always use:**
- Blueprint pattern for route organization
- Pydantic for request/response validation
- Firebase Admin SDK for database operations
- Tenant isolation middleware
- Standard error response format

**Example API Route:**

```python
# apps/api/routes/products.py
from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from pydantic import BaseModel, Field

products_bp = Blueprint('products', __name__)
db = firestore.client()

class CreateProductRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

@products_bp.route('/api/products', methods=['POST'])
def create_product():
    try:
        # Get tenant_id from middleware
        tenant_id = request.tenant_id

        # Validate request
        data = CreateProductRequest(**request.json)

        # Create product
        product_ref = db.collection('products').document()
        product_data = {
            **data.dict(),
            'tenant_id': tenant_id,
            'created_at': firestore.SERVER_TIMESTAMP,
        }
        product_ref.set(product_data)

        return jsonify({
            'success': True,
            'data': {'id': product_ref.id, **product_data}
        }), 201

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
```

### TypeScript Types & Validation

**Always use:**
- Zod schemas from `@toko/shared-types` for validation
- Infer TypeScript types from Zod schemas
- Export both schema and type

**Example:**

```typescript
// packages/shared-types/src/product.ts
import { z } from 'zod';

export const ProductSchema = z.object({
  id: z.string(),
  name: z.string().min(1).max(255),
  price: z.number().positive(),
  stock: z.number().int().nonnegative(),
  tenant_id: z.string(),
  created_at: z.string(),
  updated_at: z.string(),
});

export type Product = z.infer<typeof ProductSchema>;

export const CreateProductSchema = ProductSchema.omit({
  id: true,
  tenant_id: true,
  created_at: true,
  updated_at: true,
});

export type CreateProductDTO = z.infer<typeof CreateProductSchema>;
```

## Multi-tenant Isolation

**CRITICAL**: Every database query MUST filter by `tenant_id`.

**Firestore Query (Frontend):**
```typescript
const productsRef = collection(db, 'products');
const q = query(productsRef, where('tenant_id', '==', tenantId));
const snapshot = await getDocs(q);
```

**Firestore Query (Backend):**
```python
products_ref = db.collection('products')
query = products_ref.where('tenant_id', '==', tenant_id)
products = [doc.to_dict() for doc in query.stream()]
```

## Internationalization (i18n)

**Always use next-intl for translations:**

```tsx
// Server Component
import { getTranslations } from 'next-intl/server';

const t = await getTranslations('namespace');
<h1>{t('key')}</h1>

// Client Component
import { useTranslations } from 'next-intl';

const t = useTranslations('namespace');
<h1>{t('key')}</h1>
```

**Translation files:**
- `apps/*/messages/id.json` (Indonesian)
- `apps/*/messages/en.json` (English)

## Styling Guidelines

**Use Tailwind CSS utility classes:**
- Responsive: `md:`, `lg:` prefixes
- Dark mode: `dark:` prefix
- Spacing: `p-4`, `m-6`, `gap-4`
- Layout: `flex`, `grid`, `grid-cols-3`
- Typography: `text-sm`, `font-semibold`, `text-gray-600`

**Use shadcn/ui components from `@toko/ui-web`:**
```tsx
import { Button, Input, Dialog, Card } from '@toko/ui-web';
```

## Error Handling

**Frontend:**
```tsx
try {
  const response = await fetch('/api/products');
  if (!response.ok) {
    throw new Error('Failed to fetch products');
  }
  const data = await response.json();
} catch (error) {
  console.error('Error:', error);
  // Show error toast
}
```

**Backend:**
```python
try:
    # Database operation
    pass
except Exception as e:
    return jsonify({'success': False, 'error': str(e)}), 500
```

## File Naming Conventions

- **Components**: PascalCase (e.g., `ProductCard.tsx`)
- **Hooks**: camelCase with `use` prefix (e.g., `useProducts.ts`)
- **Utils**: camelCase (e.g., `formatCurrency.ts`)
- **Routes**: kebab-case (e.g., `product-management/`)
- **Python**: snake_case (e.g., `products_routes.py`)

## Import Order

```tsx
// 1. React/Next.js
import { useState } from 'react';
import { useRouter } from 'next/navigation';

// 2. Third-party libraries
import { useTranslations } from 'next-intl';

// 3. Internal packages
import { Product } from '@toko/shared-types';
import { Button } from '@toko/ui-web';

// 4. Local imports
import { ProductCard } from '@/components/products/ProductCard';
import { useProducts } from '@/hooks/useProducts';
```

## Documentation References

When generating code, refer to:
- **Feature Specs**: `docs/features/01-14.md` files
- **Dev Guides**: `apps/*/docs/dev-guide/01-setup.md`
- **AI Quick Reference**: `apps/*/CLAUDE.md`

## Common Patterns

### Custom Hook Pattern
```tsx
// hooks/useProducts.ts
export function useProducts(tenantId: string) {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts();
  }, [tenantId]);

  const fetchProducts = async () => {
    setLoading(true);
    const response = await fetch(`/api/products?tenant_id=${tenantId}`);
    const data = await response.json();
    setProducts(data.products);
    setLoading(false);
  };

  return { products, loading, refetch: fetchProducts };
}
```

### Form Validation with Zod
```tsx
import { z } from 'zod';
import { CreateProductSchema } from '@toko/shared-types';

const formSchema = CreateProductSchema;
type FormData = z.infer<typeof formSchema>;

const handleSubmit = (data: FormData) => {
  const result = formSchema.safeParse(data);
  if (!result.success) {
    // Show validation errors
    return;
  }
  // Submit form
};
```

## Testing Considerations

When generating tests:
- Use Jest for unit tests
- Use React Testing Library for component tests
- Use pytest for Python tests
- Mock Firebase operations
- Test tenant isolation

## Environment Variables

Always use environment-specific variables:
- `NEXT_PUBLIC_*` for client-side (Next.js)
- Regular env vars for server-side
- Never commit secrets to git

## Git Commit Messages

**IMPORTANT**: All commit messages must follow the Conventional Commits specification.

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(api): add product search endpoint` |
| `fix` | Bug fix | `fix(store-portal): resolve cart total calculation` |
| `refactor` | Code refactoring (no functional changes) | `refactor(marketplace): simplify checkout flow` |
| `docs` | Documentation only changes | `docs(readme): update installation steps` |
| `style` | Code style changes (formatting, semicolons) | `style(api): apply black formatter` |
| `test` | Adding or updating tests | `test(products): add unit tests for validation` |
| `chore` | Maintenance tasks, dependency updates | `chore: update Next.js to 16.1.0` |
| `perf` | Performance improvements | `perf(api): optimize product queries` |
| `ci` | CI/CD pipeline changes | `ci: add GitHub Actions workflow` |
| `build` | Build system or dependency changes | `build: configure Turborepo caching` |

### Scopes

| Scope | Description |
|-------|-------------|
| `api` | Backend API changes (Flask) |
| `store-portal` | Store Portal app changes |
| `marketplace` | Marketplace app changes |
| `company-profile` | Company Profile app changes |
| `platform-admin` | Platform Admin app changes |
| `firebase-client` | Firebase client package |
| `shared-types` | Shared types package |
| `ui-web` | UI components package |
| `auth` | Authentication related changes |
| `products` | Product management |
| `inventory` | Inventory management |
| `orders` | Order management |
| `payments` | Payment integration |
| `customers` | Customer management |
| `reports` | Reports and analytics |

### Commit Message Examples

```bash
# Features
feat(api): add product management endpoints
feat(store-portal): implement POS cashier interface
feat(marketplace): add shopping cart functionality
feat(payments): integrate Midtrans payment gateway

# Bug Fixes
fix(api): resolve token refresh issue
fix(store-portal): product form validation error
fix(marketplace): cart total calculation for discounts
fix(auth): prevent duplicate session creation

# Refactoring
refactor(api): improve error handling middleware
refactor(marketplace): simplify cart state management
refactor(shared-types): consolidate product schemas

# Documentation
docs(api): update product endpoints documentation
docs(readme): add deployment instructions
docs(features): update authentication specification

# Testing
test(api): add auth unit tests
test(products): add integration tests for CRUD

# Chore/Maintenance
chore: update dependencies to latest versions
chore(deps): upgrade Next.js to 16.1.0
chore: configure ESLint flat config

# Performance
perf(api): optimize Firestore batch queries
perf(store-portal): implement React Server Components caching

# Build/CI
ci: add GitHub Actions workflow for testing
build: optimize Turborepo pipeline configuration
```

### Rules

1. **Subject Line**:
   - Keep under 50 characters
   - Use imperative mood ("add" not "added" or "adds")
   - No period at the end
   - Lowercase after scope

2. **Scope**:
   - Use the predefined scopes above
   - Single scope per commit (use the most relevant one)
   - Can be omitted for global changes (e.g., `chore: update dependencies`)

3. **Description**:
   - Clear and concise explanation of what changed
   - Focus on "what" and "why", not "how"
   - Reference story/issue if applicable: `feat(api): add streaming #STORY-001`

4. **Body** (optional):
   - Use when additional context is needed
   - Wrap at 72 characters
   - Explain motivation for the change

5. **Footer** (optional):
   - Reference issues: `Fixes #123`, `Closes #456`
   - Breaking changes: `BREAKING CHANGE: description`

### Breaking Changes

For breaking changes, add `BREAKING CHANGE:` in the footer:

```
feat(api): change product API response format

BREAKING CHANGE: Product API now returns nested variant data instead of flat structure.
Update all API clients to handle new response format.
```

Or use `!` after the scope:

```
feat(api)!: change product API response format
```

### Multi-scope Changes

If a change affects multiple scopes, use the most relevant one or use multiple commits:

```bash
# Option 1: Use most relevant scope
feat(api): add product and inventory sync endpoints

# Option 2: Separate commits (preferred)
feat(api): add product sync endpoint
feat(api): add inventory sync endpoint
```

---

**Remember**: This is a production-ready, multi-tenant platform. Always prioritize:
1. Security (tenant isolation)
2. Type safety (TypeScript, Pydantic)
3. Performance (Server Components, caching)
4. User experience (i18n, responsive design)
5. Clear commit messages (following conventions above)
