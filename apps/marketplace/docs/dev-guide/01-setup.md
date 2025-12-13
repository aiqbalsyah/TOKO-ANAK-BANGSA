# Marketplace - Development Setup Guide

**Project**: Marketplace (Public Online Store)
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: Customer-facing e-commerce marketplace where customers can browse products, add to cart, checkout, and track orders

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js 22+** - [Download Node.js](https://nodejs.org/)
- **pnpm 9+** - Install: `npm install -g pnpm`
- **Firebase CLI** - Install: `npm install -g firebase-tools`

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

This will install dependencies for:
- All apps (marketplace, store-portal, platform-admin, etc.)
- All packages (firebase-client, shared-types, ui-web)

### 3. Environment Configuration

Create environment file:

```bash
cd apps/marketplace
cp .env.example .env.local
```

Edit `.env.local`:

```env
# Firebase Configuration
NEXT_PUBLIC_FIREBASE_API_KEY=your-api-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project-id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id

# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8080/api

# App Configuration
NEXT_PUBLIC_APP_URL=http://localhost:3001
NODE_ENV=development

# Midtrans Payment Gateway (for checkout)
NEXT_PUBLIC_MIDTRANS_CLIENT_KEY=your-midtrans-client-key
MIDTRANS_SERVER_KEY=your-midtrans-server-key
MIDTRANS_IS_PRODUCTION=false
```

Get Firebase credentials from [Firebase Console](https://console.firebase.google.com/) → Project Settings → General → Your apps → Web app

Get Midtrans credentials from [Midtrans Dashboard](https://dashboard.midtrans.com/)

---

## Running the Application

### Development Server

**Option 1: From project root (recommended)**
```bash
# Start marketplace only
pnpm dev:marketplace

# Or start all apps
pnpm dev
```

**Option 2: From app directory**
```bash
cd apps/marketplace
pnpm dev
```

The app will be available at: **http://localhost:3001**

### Production Build

```bash
# Build for production
pnpm build

# Start production server
pnpm start
```

---

## Project Structure

```
apps/marketplace/
├── app/                        # Next.js 16 App Router
│   ├── [locale]/               # Internationalization routing
│   │   ├── (public)/           # Public routes (no auth required)
│   │   │   ├── page.tsx        # Homepage (featured products)
│   │   │   ├── products/       # Product listing & search
│   │   │   │   ├── page.tsx    # All products
│   │   │   │   ├── [id]/       # Product detail page
│   │   │   │   └── category/[slug]/  # Category pages
│   │   │   ├── cart/           # Shopping cart
│   │   │   ├── checkout/       # Checkout flow
│   │   │   ├── about/          # About the store
│   │   │   └── contact/        # Contact page
│   │   ├── (customer)/         # Customer account routes (protected)
│   │   │   ├── account/        # Account settings
│   │   │   ├── orders/         # Order history
│   │   │   │   ├── page.tsx    # All orders
│   │   │   │   └── [id]/       # Order detail & tracking
│   │   │   └── wishlist/       # Saved products
│   │   ├── (auth)/             # Authentication routes
│   │   │   ├── login/          # Customer login
│   │   │   ├── register/       # Customer registration
│   │   │   └── forgot-password/ # Password reset
│   │   ├── layout.tsx          # Root layout
│   │   └── page.tsx            # Redirect to homepage
│   └── api/                    # API routes
│       ├── checkout/           # Checkout API
│       └── webhooks/           # Payment webhooks (Midtrans)
├── components/                 # React components
│   ├── ui/                     # Base UI components (from @toko/ui-web)
│   ├── layouts/                # Layout components
│   │   ├── Header.tsx          # Site header with cart
│   │   ├── Footer.tsx          # Site footer
│   │   └── CustomerLayout.tsx  # Customer account layout
│   ├── products/               # Product components
│   │   ├── ProductCard.tsx     # Product grid item
│   │   ├── ProductGrid.tsx     # Product listing grid
│   │   ├── ProductFilter.tsx   # Filter sidebar
│   │   ├── ProductSearch.tsx   # Search bar
│   │   └── ProductDetail.tsx   # Product detail view
│   ├── cart/                   # Shopping cart components
│   │   ├── CartDrawer.tsx      # Cart sidebar
│   │   ├── CartItem.tsx        # Cart item row
│   │   └── CartSummary.tsx     # Cart totals
│   ├── checkout/               # Checkout components
│   │   ├── CheckoutForm.tsx    # Checkout form
│   │   ├── ShippingForm.tsx    # Shipping address
│   │   ├── PaymentMethod.tsx   # Payment selection
│   │   └── OrderSummary.tsx    # Order review
│   └── common/                 # Shared components
│       ├── Breadcrumb.tsx      # Breadcrumb navigation
│       ├── Hero.tsx            # Homepage hero
│       └── CategoryCard.tsx    # Category tiles
├── lib/                        # Utility libraries
│   ├── firebase.ts             # Firebase client initialization
│   ├── api.ts                  # API client
│   ├── cart.ts                 # Shopping cart logic
│   ├── payment.ts              # Payment integration (Midtrans)
│   └── utils.ts                # Helper functions
├── hooks/                      # Custom React hooks
│   ├── useAuth.ts              # Customer authentication
│   ├── useCart.ts              # Shopping cart state
│   ├── useProducts.ts          # Product catalog data
│   └── useOrders.ts            # Customer orders
├── types/                      # TypeScript type definitions
│   └── index.ts                # Local types (Cart, Checkout, etc.)
├── i18n/                       # Internationalization
│   ├── routing.ts              # i18n routing configuration
│   └── request.ts              # i18n request configuration
├── messages/                   # Translation files
│   ├── en.json                 # English translations
│   └── id.json                 # Indonesian translations
├── public/                     # Static files
│   ├── images/                 # Images
│   └── icons/                  # Icons
├── styles/                     # Global styles
│   └── globals.css             # Tailwind CSS
├── middleware.ts               # Next.js middleware (i18n, customer auth)
├── next.config.ts              # Next.js configuration
├── tailwind.config.ts          # Tailwind CSS configuration
├── tsconfig.json               # TypeScript configuration
├── package.json                # Dependencies
└── README.md                   # Project overview
```

---

## Development Workflow

### 1. Start Development

```bash
# From project root
pnpm dev:marketplace

# Access at http://localhost:3001
```

### 2. Add New Dependency

**App-specific dependency:**
```bash
cd apps/marketplace
pnpm add package-name
```

**Workspace dependency** (shared package):
```bash
# Already configured in package.json
"dependencies": {
  "@toko/firebase-client": "workspace:*",
  "@toko/shared-types": "workspace:*",
  "@toko/ui-web": "workspace:*"
}
```

### 3. Run Type Checking

```bash
# From app directory
pnpm typecheck

# Or from root for all apps
pnpm typecheck
```

### 4. Run Linting

```bash
# From app directory
pnpm lint

# Or from root for all apps
pnpm lint
```

### 5. Format Code

```bash
# Format code
pnpm prettier --write .
```

---

## Key Features & Routes

### Public Routes (No Authentication)
- `/` - Homepage (featured products, categories, hero banner)
- `/products` - Product catalog (all products with search and filters)
- `/products/[id]` - Product detail page
- `/products/category/[slug]` - Category-specific products
- `/cart` - Shopping cart
- `/checkout` - Checkout flow (address, shipping, payment)
- `/about` - About the store
- `/contact` - Contact page

### Customer Routes (Protected)
- `/account` - Customer account settings
- `/orders` - Order history
- `/orders/[id]` - Order detail and tracking
- `/wishlist` - Saved products (future)

### Authentication Routes
- `/login` - Customer login
- `/register` - Customer registration
- `/forgot-password` - Password reset

---

## Internationalization (i18n)

The app supports multiple languages using `next-intl`.

### Supported Languages
- English (en)
- Indonesian (id) - Default

### Add Translation

Edit `messages/id.json` or `messages/en.json`:

```json
{
  "common": {
    "addToCart": "Tambah ke Keranjang",
    "buyNow": "Beli Sekarang",
    "viewDetails": "Lihat Detail"
  },
  "products": {
    "allProducts": "Semua Produk",
    "inStock": "Tersedia",
    "outOfStock": "Habis",
    "priceRange": "Rentang Harga"
  },
  "cart": {
    "title": "Keranjang Belanja",
    "empty": "Keranjang Anda kosong",
    "checkout": "Checkout",
    "continueShopping": "Lanjut Belanja"
  }
}
```

### Use in Component

```tsx
'use client';

import { useTranslations } from 'next-intl';

export default function ProductCard({ product }) {
  const t = useTranslations('products');

  return (
    <div>
      <h3>{product.name}</h3>
      <p>{product.inStock ? t('inStock') : t('outOfStock')}</p>
      <button>{t('common.addToCart')}</button>
    </div>
  );
}
```

---

## Shopping Cart Implementation

### Cart State Management

```tsx
'use client';

import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface CartItem {
  productId: string;
  name: string;
  price: number;
  quantity: number;
  image?: string;
}

interface CartState {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (productId: string) => void;
  updateQuantity: (productId: string, quantity: number) => void;
  clearCart: () => void;
  total: () => number;
}

export const useCart = create<CartState>()(
  persist(
    (set, get) => ({
      items: [],

      addItem: (item) =>
        set((state) => {
          const existing = state.items.find((i) => i.productId === item.productId);
          if (existing) {
            return {
              items: state.items.map((i) =>
                i.productId === item.productId
                  ? { ...i, quantity: i.quantity + item.quantity }
                  : i
              ),
            };
          }
          return { items: [...state.items, item] };
        }),

      removeItem: (productId) =>
        set((state) => ({
          items: state.items.filter((i) => i.productId !== productId),
        })),

      updateQuantity: (productId, quantity) =>
        set((state) => ({
          items: state.items.map((i) =>
            i.productId === productId ? { ...i, quantity } : i
          ),
        })),

      clearCart: () => set({ items: [] }),

      total: () => {
        const { items } = get();
        return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
      },
    }),
    {
      name: 'cart-storage',
    }
  )
);
```

### Using Cart in Component

```tsx
'use client';

import { useCart } from '@/hooks/useCart';

export default function ProductDetail({ product }) {
  const { addItem } = useCart();

  const handleAddToCart = () => {
    addItem({
      productId: product.id,
      name: product.name,
      price: product.price,
      quantity: 1,
      image: product.image,
    });
  };

  return (
    <div>
      <h1>{product.name}</h1>
      <p>IDR {product.price.toLocaleString('id-ID')}</p>
      <button onClick={handleAddToCart}>Add to Cart</button>
    </div>
  );
}
```

---

## Checkout Flow

### Checkout Process

```tsx
'use client';

import { useState } from 'usestate';
import { useCart } from '@/hooks/useCart';
import { apiRequest } from '@/lib/api';

export default function CheckoutPage() {
  const { items, total, clearCart } = useCart();
  const [loading, setLoading] = useState(false);
  const [shippingAddress, setShippingAddress] = useState({});
  const [paymentMethod, setPaymentMethod] = useState('');

  const handleCheckout = async () => {
    setLoading(true);

    try {
      // Create order
      const order = await apiRequest('/orders', {
        method: 'POST',
        body: JSON.stringify({
          items,
          shippingAddress,
          paymentMethod,
          total: total(),
        }),
      });

      // Get Midtrans payment token
      const payment = await apiRequest('/payments/midtrans/token', {
        method: 'POST',
        body: JSON.stringify({
          orderId: order.id,
          amount: total(),
        }),
      });

      // Redirect to Midtrans payment page
      window.snap.pay(payment.token, {
        onSuccess: function () {
          clearCart();
          router.push(`/orders/${order.id}`);
        },
        onPending: function () {
          router.push(`/orders/${order.id}`);
        },
        onError: function () {
          alert('Payment failed');
        },
      });
    } catch (error) {
      console.error('Checkout failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Checkout</h1>
      {/* Shipping address form */}
      {/* Payment method selection */}
      <button onClick={handleCheckout} disabled={loading}>
        {loading ? 'Processing...' : 'Place Order'}
      </button>
    </div>
  );
}
```

### Midtrans Integration

```typescript
// lib/payment.ts
export function loadMidtransScript() {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = process.env.NEXT_PUBLIC_MIDTRANS_IS_PRODUCTION === 'true'
      ? 'https://app.midtrans.com/snap/snap.js'
      : 'https://app.sandbox.midtrans.com/snap/snap.js';
    script.setAttribute('data-client-key', process.env.NEXT_PUBLIC_MIDTRANS_CLIENT_KEY!);
    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
  });
}
```

---

## Customer Authentication

### Login Flow

```tsx
'use client';

import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '@/lib/firebase';
import { useRouter } from 'next/navigation';

export default function LoginPage() {
  const router = useRouter();

  const handleLogin = async (email: string, password: string) => {
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;

      // Get ID token
      const idToken = await user.getIdToken();

      // Send to API for session creation
      await fetch('/api/auth/session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idToken }),
      });

      // Redirect to account or cart
      router.push('/account');
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    // Login form
  );
}
```

### Protected Routes

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;

  // Define protected customer routes
  const isProtectedPath = path.startsWith('/account') ||
                         path.startsWith('/orders') ||
                         path.startsWith('/wishlist');

  const token = request.cookies.get('auth-token')?.value;

  // Redirect to login if accessing protected route without token
  if (isProtectedPath && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
};
```

---

## API Integration

### Product Catalog API

```typescript
// lib/api.ts
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8080/api';

export async function apiRequest<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.statusText}`);
  }

  return response.json();
}

// Product API
export const getProducts = (params?: {
  category?: string;
  search?: string;
  minPrice?: number;
  maxPrice?: number;
  page?: number;
  limit?: number;
}) => {
  const queryString = new URLSearchParams(params as any).toString();
  return apiRequest<{ products: Product[]; total: number }>(`/products?${queryString}`);
};

export const getProduct = (id: string) =>
  apiRequest<Product>(`/products/${id}`);

export const getCategories = () =>
  apiRequest<Category[]>('/categories');
```

---

## Common Issues & Troubleshooting

### Issue: `Module not found` errors

**Solution:** Ensure all dependencies are installed:
```bash
# From project root
pnpm install
```

### Issue: Port 3001 already in use

**Solution:** Kill the process or use a different port:
```bash
# Kill process
lsof -ti:3001 | xargs kill -9

# Or use different port
pnpm dev -- --port 3004
```

### Issue: Firebase initialization error

**Solution:** Check that:
1. `.env.local` exists with correct Firebase credentials
2. All `NEXT_PUBLIC_*` variables are set
3. Restart dev server after changing `.env.local`

### Issue: Midtrans payment not working

**Solution:** Ensure:
1. Midtrans client key and server key are set in `.env.local`
2. Using sandbox credentials for development (`MIDTRANS_IS_PRODUCTION=false`)
3. Midtrans script is loaded before calling `window.snap.pay()`

### Issue: Cart not persisting

**Solution:** Check:
1. Browser localStorage is enabled
2. Cart state is using `persist` middleware from zustand
3. Clear browser cache and reload

### Issue: Products not displaying

**Solution:** Check:
1. API is running at `http://localhost:8080`
2. CORS is enabled in API for `http://localhost:3001`
3. Network tab in DevTools for API errors

---

## Environment Variables Reference

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `NEXT_PUBLIC_FIREBASE_API_KEY` | Firebase API key | `AIza...` | Yes |
| `NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN` | Firebase auth domain | `project.firebaseapp.com` | Yes |
| `NEXT_PUBLIC_FIREBASE_PROJECT_ID` | Firebase project ID | `toko-anak-bangsa` | Yes |
| `NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET` | Firebase storage bucket | `project.appspot.com` | Yes |
| `NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID` | FCM sender ID | `123456789` | Yes |
| `NEXT_PUBLIC_FIREBASE_APP_ID` | Firebase app ID | `1:123:web:abc` | Yes |
| `NEXT_PUBLIC_API_URL` | Backend API URL | `http://localhost:8080/api` | Yes |
| `NEXT_PUBLIC_APP_URL` | App URL | `http://localhost:3001` | Yes |
| `NEXT_PUBLIC_MIDTRANS_CLIENT_KEY` | Midtrans client key | `SB-Mid-client-...` | Yes |
| `MIDTRANS_SERVER_KEY` | Midtrans server key (server-side only) | `SB-Mid-server-...` | Yes |
| `MIDTRANS_IS_PRODUCTION` | Production mode flag | `false` | Yes |
| `NODE_ENV` | Environment | `development` | Yes |

---

## Useful Commands

```bash
# Start development server
pnpm dev:marketplace

# Build for production
pnpm build

# Start production server
pnpm start

# Type checking
pnpm typecheck

# Linting
pnpm lint

# Format code
pnpm prettier --write .

# Add dependency
pnpm add package-name

# Add dev dependency
pnpm add -D package-name

# Clean build artifacts
rm -rf .next

# View bundle size
pnpm build && pnpm analyze
```

---

## Testing Payment Integration

### Test Midtrans Sandbox

Use these test cards in sandbox mode:

**Successful Payment:**
- Card Number: `4811 1111 1111 1114`
- Expiry: `01/25`
- CVV: `123`

**Failed Payment:**
- Card Number: `4911 1111 1111 1113`
- Expiry: `01/25`
- CVV: `123`

For more test scenarios, see [Midtrans Testing](https://docs.midtrans.com/en/technical-reference/sandbox-test)

---

## Next Steps

1. Read `02-architecture.md` (when available) to understand system design
2. Read `03-coding-standards.md` (when available) for code conventions
3. Review feature documentation: `/docs/features/10-marketplace.md`
4. Check UI component library in `packages/ui-web`
5. Review shared types in `packages/shared-types`
6. Test payment integration in sandbox mode

---

**Last Updated**: 2024-12-13
