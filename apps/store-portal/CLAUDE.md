# Claude Code Guide - Store Portal

**Project**: Store Portal (POS & Store Management)
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: Back-office portal for store owners and staff to manage POS, inventory, orders, customers, and business operations

---

## Quick Start for AI Assistants

When working on this project with Claude Code, follow this workflow:

### 1. Understand the Project

**Read these first:**
- `apps/store-portal/README.md` - Project overview
- `apps/store-portal/docs/dev-guide/01-setup.md` - Complete setup guide and patterns

**Documentation structure:**
- Feature specs: `docs/features/01-14.md` - Business requirements and UI specifications
- Dev guide: `apps/store-portal/docs/dev-guide/` - Development patterns and setup
- UI components: `packages/ui-web/` - Shared React components
- Shared types: `packages/shared-types/` - TypeScript types and Zod schemas
- Firebase client: `packages/firebase-client/` - Firebase SDK wrapper

### 2. Working on Stories

**When filling a story** (via `/fill-story` command):

1. **Identify the feature**: Read the relevant feature file from `docs/features/`
   - Example: POS → `docs/features/05-pos-cashier.md`

2. **Check user flows**: Follow UI patterns from "User Flows" section

3. **Use UI components**: Reference `packages/ui-web/docs/dev-guide/01-setup.md` for available components

4. **Follow project structure**: Organize files according to Next.js App Router conventions

### 3. Implementation Patterns

**App Router Structure:**

```
app/[locale]/(dashboard)/
├── products/
│   ├── page.tsx              # Product list page
│   ├── [id]/
│   │   └── page.tsx          # Product detail page
│   └── create/
│       └── page.tsx          # Create product page
```

**Page Component Example:**

```tsx
// app/[locale]/(dashboard)/products/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { useTranslations } from 'next-intl';
import { Button, Input, Dialog } from '@toko/ui-web';
import { Product } from '@toko/shared-types';
import { db } from '@toko/firebase-client';
import { collection, query, where, getDocs } from 'firebase/firestore';

export default function ProductsPage() {
  const t = useTranslations('products');
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      // Get current tenant ID from auth context
      const tenantId = 'tenant-1'; // TODO: Get from auth context

      const q = query(
        collection(db, 'products'),
        where('tenantId', '==', tenantId)
      );

      const snapshot = await getDocs(q);
      const data = snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      })) as Product[];

      setProducts(data);
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">{t('title')}</h1>
        <Button href="/products/create">
          {t('createProduct')}
        </Button>
      </div>

      {loading ? (
        <div>Loading...</div>
      ) : (
        <div className="grid grid-cols-3 gap-4">
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      )}
    </div>
  );
}
```

**Custom Hook Example:**

```tsx
// hooks/useProducts.ts
import { useState, useEffect } from 'react';
import { Product } from '@toko/shared-types';
import { queryDocuments } from '@toko/firebase-client';
import { useAuth } from './useAuth';

export function useProducts() {
  const { tenantId } = useAuth();
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!tenantId) return;

    const fetchProducts = async () => {
      try {
        const data = await queryDocuments<Product>(
          'products',
          'tenantId',
          '==',
          tenantId
        );
        setProducts(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [tenantId]);

  const refetch = () => {
    setLoading(true);
    // Re-fetch logic
  };

  return { products, loading, error, refetch };
}
```

**Form Validation Example:**

```tsx
// app/[locale]/(dashboard)/products/create/page.tsx
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { CreateProductSchema, CreateProductDTO } from '@toko/shared-types';
import { Button, Input, Form } from '@toko/ui-web';
import { createDocument } from '@toko/firebase-client';

export default function CreateProductPage() {
  const form = useForm<CreateProductDTO>({
    resolver: zodResolver(CreateProductSchema),
    defaultValues: {
      name: '',
      price: 0,
      stock: 0,
    },
  });

  const onSubmit = async (data: CreateProductDTO) => {
    try {
      const productId = await createDocument('products', {
        ...data,
        tenantId: 'tenant-1', // Get from auth
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      });

      // Redirect to product list
      router.push('/products');
    } catch (error) {
      console.error('Error creating product:', error);
    }
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        <Input
          {...form.register('name')}
          label="Product Name"
          error={form.formState.errors.name?.message}
        />
        <Input
          {...form.register('price', { valueAsNumber: true })}
          type="number"
          label="Price"
          error={form.formState.errors.price?.message}
        />
        <Button type="submit">Create Product</Button>
      </form>
    </Form>
  );
}
```

### 4. File Organization

```
apps/store-portal/
├── app/[locale]/(dashboard)/
│   ├── products/
│   │   ├── page.tsx                    # List page
│   │   ├── [id]/page.tsx               # Detail page
│   │   └── create/page.tsx             # Create page
│   ├── pos/
│   └── inventory/
├── components/
│   ├── products/
│   │   ├── ProductCard.tsx             # Presentation component
│   │   ├── ProductForm.tsx             # Form component
│   │   └── ProductList.tsx             # List component
├── hooks/
│   ├── useProducts.ts                  # Products data hook
│   ├── useAuth.ts                      # Authentication
│   └── useCart.ts                      # POS cart state
├── lib/
│   ├── firebase.ts                     # Re-export from @toko/firebase-client
│   └── api.ts                          # API client helpers
└── types/
    └── index.ts                        # Local types only
```

### 5. Key Principles

**Always follow these rules:**

1. **Use Shared Packages**:
   - Import from `@toko/ui-web` for all UI components
   - Import from `@toko/shared-types` for types and validation
   - Import from `@toko/firebase-client` for Firebase operations

2. **Internationalization**:
   - All user-facing text must use `useTranslations()` from next-intl
   - Add translations to `messages/id.json` and `messages/en.json`

3. **Type Safety**:
   - Use TypeScript types from `@toko/shared-types`
   - Validate forms with Zod schemas
   - No `any` types

4. **State Management**:
   - Use React hooks for local state
   - Use Context API for shared state (auth, tenant)
   - Use Zustand for complex global state (POS cart)

5. **Tenant Isolation**:
   - Always filter Firestore queries by `tenantId`
   - Get `tenantId` from auth context

### 6. UI Components

**Available from @toko/ui-web:**

```tsx
import {
  Button,
  Input,
  Select,
  Checkbox,
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  Avatar,
  Card,
  Table,
  Toast,
  useToast,
} from '@toko/ui-web';
```

**Example Usage:**

```tsx
function ProductActions() {
  const { toast } = useToast();

  const handleDelete = async () => {
    try {
      await deleteDocument('products', productId);
      toast({
        title: 'Success',
        description: 'Product deleted successfully',
      });
    } catch (error) {
      toast({
        title: 'Error',
        description: 'Failed to delete product',
        variant: 'destructive',
      });
    }
  };

  return <Button onClick={handleDelete}>Delete</Button>;
}
```

### 7. Internationalization

**Adding Translations:**

```json
// messages/id.json
{
  "products": {
    "title": "Produk",
    "createProduct": "Tambah Produk",
    "editProduct": "Edit Produk",
    "deleteConfirm": "Hapus produk ini?"
  }
}
```

**Using Translations:**

```tsx
'use client';

import { useTranslations } from 'next-intl';

export default function ProductsPage() {
  const t = useTranslations('products');

  return (
    <div>
      <h1>{t('title')}</h1>
      <Button>{t('createProduct')}</Button>
    </div>
  );
}
```

### 8. Testing

**Before marking story as complete:**

1. Run type checking: `pnpm typecheck`
2. Run linting: `pnpm lint`
3. Manual testing:
   - Test all user flows from feature documentation
   - Test with different screen sizes (mobile, tablet, desktop)
   - Test form validation (valid and invalid inputs)
   - Test error states (network errors, empty states)

### 9. Common Operations

**Firestore with Firebase Client:**

```tsx
import {
  getDocumentById,
  createDocument,
  updateDocument,
  deleteDocument,
  queryDocuments,
} from '@toko/firebase-client';

// Get one
const product = await getDocumentById<Product>('products', 'product-id');

// Create
const productId = await createDocument('products', {
  name: 'New Product',
  price: 10000,
  tenantId: 'tenant-1',
});

// Update
await updateDocument('products', 'product-id', { price: 15000 });

// Delete
await deleteDocument('products', 'product-id');

// Query
const products = await queryDocuments<Product>(
  'products',
  'tenantId',
  '==',
  'tenant-1'
);
```

---

## Quick Reference

**Documentation:**
- Setup: `apps/store-portal/docs/dev-guide/01-setup.md`
- Features: `docs/features/01-14.md`
- UI Components: `packages/ui-web/docs/dev-guide/01-setup.md`
- Shared Types: `packages/shared-types/docs/dev-guide/01-setup.md`
- Firebase Client: `packages/firebase-client/docs/dev-guide/01-setup.md`

**Commands:**
```bash
# From root
pnpm dev:store        # Start store-portal on port 3000

# From app directory
cd apps/store-portal
pnpm dev             # Start dev server
pnpm build           # Production build
pnpm typecheck       # Type check
pnpm lint            # Lint code
```

**Environment Variables:**
```env
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
NEXT_PUBLIC_API_URL=http://localhost:8080/api
```

---

**Last Updated**: 2024-12-13
