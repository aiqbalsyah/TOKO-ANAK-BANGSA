# Claude Code Guide - Marketplace

**Project**: Marketplace (Customer-Facing E-commerce)
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: Public online storefront where customers can browse products, add to cart, checkout, and track orders

---

## Quick Start

This app follows the **same patterns as Store Portal** but with customer-facing features.

### Documentation

**Read these:**
- `apps/marketplace/README.md` - Project overview
- `apps/marketplace/docs/dev-guide/01-setup.md` - Complete setup guide
- `docs/features/10-marketplace.md` - Marketplace feature specifications
- `apps/store-portal/CLAUDE.md` - Shared Next.js patterns

### Key Differences from Store Portal

1. **Public Access**: Most routes are public (no authentication required)
2. **Customer Authentication**: Login/register for customers (not staff)
3. **Shopping Cart**: Zustand state management for cart
4. **Checkout Flow**: Midtrans payment integration
5. **Port**: Runs on `http://localhost:3001`

### Implementation Patterns

**Shopping Cart (Zustand):**

```tsx
// hooks/useCart.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface CartItem {
  productId: string;
  name: string;
  price: number;
  quantity: number;
}

interface CartState {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (productId: string) => void;
  total: () => number;
}

export const useCart = create<CartState>()(
  persist(
    (set, get) => ({
      items: [],
      addItem: (item) => set((state) => ({ items: [...state.items, item] })),
      removeItem: (id) => set((state) => ({
        items: state.items.filter(i => i.productId !== id)
      })),
      total: () => get().items.reduce((sum, item) =>
        sum + (item.price * item.quantity), 0
      ),
    }),
    { name: 'cart-storage' }
  )
);
```

**Checkout with Midtrans:**

```tsx
// app/[locale]/checkout/page.tsx
'use client';

import { useCart } from '@/hooks/useCart';
import { loadMidtransScript } from '@/lib/payment';

export default function CheckoutPage() {
  const { items, total, clearCart } = useCart();

  const handleCheckout = async () => {
    // Load Midtrans script
    await loadMidtransScript();

    // Create order via API
    const order = await fetch('/api/orders', {
      method: 'POST',
      body: JSON.stringify({ items, total: total() }),
    }).then(r => r.json());

    // Get payment token
    const payment = await fetch('/api/payments/midtrans/token', {
      method: 'POST',
      body: JSON.stringify({ orderId: order.id, amount: total() }),
    }).then(r => r.json());

    // Open Midtrans payment page
    window.snap.pay(payment.token, {
      onSuccess: () => {
        clearCart();
        router.push(`/orders/${order.id}`);
      },
    });
  };

  return (
    <button onClick={handleCheckout}>Place Order</button>
  );
}
```

### File Organization

```
apps/marketplace/
├── app/[locale]/
│   ├── (public)/              # Public routes (no auth)
│   │   ├── page.tsx           # Homepage
│   │   ├── products/          # Product catalog
│   │   ├── cart/              # Shopping cart
│   │   └── checkout/          # Checkout flow
│   ├── (customer)/            # Customer routes (auth required)
│   │   ├── account/           # Account settings
│   │   └── orders/            # Order history
│   └── (auth)/                # Auth routes
│       ├── login/
│       └── register/
├── components/
│   ├── products/              # Product components
│   ├── cart/                  # Cart components
│   └── checkout/              # Checkout components
└── hooks/
    ├── useCart.ts             # Shopping cart state
    └── useProducts.ts         # Product catalog
```

### Environment Variables

```env
# Standard Next.js + Firebase
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_API_URL=http://localhost:8080/api

# Midtrans Payment
NEXT_PUBLIC_MIDTRANS_CLIENT_KEY=SB-Mid-client-...
MIDTRANS_SERVER_KEY=SB-Mid-server-...
MIDTRANS_IS_PRODUCTION=false
```

### Commands

```bash
pnpm dev:marketplace   # Start on port 3001
```

---

**Refer to `apps/store-portal/CLAUDE.md` for complete Next.js patterns and best practices.**

**Last Updated**: 2024-12-13
