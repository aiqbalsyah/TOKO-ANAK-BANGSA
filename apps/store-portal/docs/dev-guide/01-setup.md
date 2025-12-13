# Store Portal - Development Setup Guide

**Project**: Store Portal (POS & Store Management)
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: Back-office portal for store owners and staff to manage POS, inventory, orders, customers, and business operations

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
- All apps (store-portal, marketplace, platform-admin, etc.)
- All packages (firebase-client, shared-types, ui-web)

### 3. Environment Configuration

Create environment file:

```bash
cd apps/store-portal
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
NEXT_PUBLIC_APP_URL=http://localhost:3000
NODE_ENV=development
```

Get Firebase credentials from [Firebase Console](https://console.firebase.google.com/) → Project Settings → General → Your apps → Web app

---

## Running the Application

### Development Server

**Option 1: From project root (recommended)**
```bash
# Start store-portal only
pnpm dev:store

# Or start all apps
pnpm dev
```

**Option 2: From app directory**
```bash
cd apps/store-portal
pnpm dev
```

The app will be available at: **http://localhost:3000**

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
apps/store-portal/
├── app/                        # Next.js 16 App Router
│   ├── [locale]/               # Internationalization routing
│   │   ├── (auth)/             # Authentication routes group
│   │   │   ├── login/          # Login page
│   │   │   └── register/       # Registration page
│   │   ├── (dashboard)/        # Dashboard routes group (protected)
│   │   │   ├── layout.tsx      # Dashboard layout with sidebar
│   │   │   ├── page.tsx        # Dashboard home
│   │   │   ├── products/       # Product management
│   │   │   ├── inventory/      # Inventory management
│   │   │   ├── pos/            # Point of Sale
│   │   │   ├── orders/         # Order management
│   │   │   ├── customers/      # Customer management
│   │   │   ├── suppliers/      # Supplier & purchasing
│   │   │   ├── reports/        # Reports & analytics
│   │   │   └── settings/       # Store settings
│   │   ├── layout.tsx          # Root layout
│   │   └── page.tsx            # Home page
│   └── api/                    # API routes (if any)
├── components/                 # React components
│   ├── ui/                     # Base UI components (from @toko/ui-web)
│   ├── layouts/                # Layout components
│   │   ├── DashboardLayout.tsx # Dashboard layout
│   │   └── Sidebar.tsx         # Navigation sidebar
│   ├── products/               # Product-related components
│   ├── inventory/              # Inventory components
│   ├── pos/                    # POS components
│   └── common/                 # Shared components
├── lib/                        # Utility libraries
│   ├── firebase.ts             # Firebase client initialization
│   ├── api.ts                  # API client
│   └── utils.ts                # Helper functions
├── hooks/                      # Custom React hooks
│   ├── useAuth.ts              # Authentication hook
│   ├── useProducts.ts          # Products data hook
│   └── useOrders.ts            # Orders data hook
├── types/                      # TypeScript type definitions
│   └── index.ts                # Local types
├── i18n/                       # Internationalization
│   ├── routing.ts              # i18n routing configuration
│   └── request.ts              # i18n request configuration
├── messages/                   # Translation files
│   ├── en.json                 # English translations
│   └── id.json                 # Indonesian translations
├── public/                     # Static files
│   ├── images/                 # Images
│   └── icons/                  # Icons
├── styles/                     # Global styles (if any)
│   └── globals.css             # Tailwind CSS
├── middleware.ts               # Next.js middleware (i18n, auth)
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
pnpm dev:store

# Access at http://localhost:3000
```

### 2. Add New Dependency

**App-specific dependency:**
```bash
cd apps/store-portal
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
# Install Prettier (if not already)
pnpm add -D prettier

# Format code
pnpm prettier --write .
```

---

## Key Features & Routes

### Authentication Routes (Public)
- `/login` - Store staff login
- `/register` - New store registration

### Dashboard Routes (Protected)
- `/` - Dashboard home (sales overview, metrics)
- `/pos` - Point of Sale interface
- `/products` - Product management (CRUD, variants, pricing)
- `/inventory` - Inventory tracking (stock levels, adjustments)
- `/orders` - Order management (POS + marketplace orders)
- `/customers` - Customer database (tiers, credit, history)
- `/suppliers` - Supplier management & purchasing
- `/reports` - Reports & analytics
- `/settings` - Store settings (staff, payment, tax, etc.)

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
    "save": "Simpan",
    "cancel": "Batal",
    "delete": "Hapus"
  },
  "products": {
    "title": "Produk",
    "addProduct": "Tambah Produk",
    "editProduct": "Edit Produk"
  }
}
```

### Use in Component

```tsx
'use client';

import { useTranslations } from 'next-intl';

export default function ProductsPage() {
  const t = useTranslations('products');

  return (
    <div>
      <h1>{t('title')}</h1>
      <button>{t('addProduct')}</button>
    </div>
  );
}
```

---

## Authentication Flow

### Using Firebase Auth

```tsx
'use client';

import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '@/lib/firebase';

export default function LoginPage() {
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
        body: JSON.stringify({ idToken })
      });

      // Redirect to dashboard
      router.push('/');
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

Use middleware to protect routes:

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;
  const isPublicPath = path === '/login' || path === '/register';
  const token = request.cookies.get('auth-token')?.value;

  // Redirect to login if accessing protected route without token
  if (!isPublicPath && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Redirect to dashboard if accessing auth pages with token
  if (isPublicPath && token) {
    return NextResponse.redirect(new URL('/', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
};
```

---

## API Integration

### API Client Setup

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

// Usage
export const getProducts = () => apiRequest<Product[]>('/products');
export const createProduct = (data: CreateProductDTO) =>
  apiRequest<Product>('/products', {
    method: 'POST',
    body: JSON.stringify(data),
  });
```

---

## Common Issues & Troubleshooting

### Issue: `Module not found` errors

**Solution:** Ensure all dependencies are installed:
```bash
# From project root
pnpm install
```

### Issue: Port 3000 already in use

**Solution:** Kill the process or use a different port:
```bash
# Kill process
lsof -ti:3000 | xargs kill -9

# Or use different port
pnpm dev -- --port 3002
```

### Issue: Firebase initialization error

**Solution:** Check that:
1. `.env.local` exists with correct Firebase credentials
2. All `NEXT_PUBLIC_*` variables are set
3. Restart dev server after changing `.env.local`

### Issue: Translations not loading

**Solution:** Ensure:
1. Translation files exist in `messages/` directory
2. Locale is configured in `i18n/routing.ts`
3. Using `'use client'` directive when using `useTranslations`

### Issue: Workspace package not found

**Solution:** Rebuild workspace:
```bash
# From project root
pnpm install
```

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
| `NEXT_PUBLIC_APP_URL` | App URL | `http://localhost:3000` | Yes |
| `NODE_ENV` | Environment | `development` | Yes |

---

## Useful Commands

```bash
# Start development server
pnpm dev:store

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

## Next Steps

1. Read `02-architecture.md` (when available) to understand system design
2. Read `03-coding-standards.md` (when available) for code conventions
3. Review feature documentation in `/docs/features/`
4. Check UI component library in `packages/ui-web`
5. Review shared types in `packages/shared-types`

---

**Last Updated**: 2024-12-13
