# Developer Guide - TOKO ANAK BANGSA

Complete guide for developers working on the TOKO ANAK BANGSA platform.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
3. [Component Architecture](#component-architecture)
4. [Development Workflow](#development-workflow)
5. [Code Style Guide](#code-style-guide)
6. [Testing Guidelines](#testing-guidelines)
7. [Deployment](#deployment)

---

## Project Overview

**TOKO ANAK BANGSA** is a multi-tenant POS & Marketplace platform for Indonesian SMEs.

### Technology Stack

- **Monorepo**: Turborepo + pnpm workspaces
- **Frontend**: Next.js 16 (App Router), React 19, TypeScript
- **Backend**: Python Flask API
- **Database**: Firebase (Firestore, Auth, Storage, RTDB)
- **UI**: shadcn/ui + Tailwind CSS
- **Validation**: Zod schemas
- **Deployment**: Firebase App Hosting

### Applications

1. **Store Portal** (Port 3000) - POS & Store Management
2. **Marketplace** (Port 3001) - Public E-commerce
3. **Company Profile** (Port 3002) - Landing Page
4. **Platform Admin** (Port 3003) - Platform Management
5. **Flask API** (Port 8080) - Backend Services

---

## Getting Started

### Prerequisites

- Node.js >= 20.0.0
- pnpm >= 10.0.0
- Python >= 3.12
- Firebase CLI
- Git

### Initial Setup

```bash
# Clone repository
git clone <repository-url>
cd pos_app_v1

# Install dependencies
pnpm install

# Install Python dependencies for Flask API
cd apps/api
pip install -r requirements.txt
cd ../..

# Copy environment variables
cp .env.example .env.local

# Build packages
pnpm build

# Start all applications
pnpm dev
```

### Available Commands

```bash
# Development
pnpm dev                    # Run all apps
pnpm dev:store-portal       # Run store portal only
pnpm dev:marketplace        # Run marketplace only
pnpm dev:company-profile    # Run company profile only
pnpm dev:platform-admin     # Run platform admin only
pnpm dev:api                # Run Flask API only

# Build
pnpm build                  # Build all apps
pnpm build:store-portal     # Build store portal only

# Type checking
pnpm typecheck              # Check all TypeScript

# Linting
pnpm lint                   # Lint all code

# Firebase
pnpm firebase:emulators     # Start Firebase emulators

# Deployment
pnpm deploy:store-portal    # Deploy store portal
pnpm deploy:marketplace     # Deploy marketplace
pnpm deploy:all             # Deploy everything
```

---

## Component Architecture

### Overview

We use a **modular, feature-based component architecture** that scales from small to large applications.

### Directory Structure

```
apps/[app-name]/
├── app/                        # Next.js App Router
│   ├── page.tsx               # Route entry (thin layer)
│   ├── layout.tsx             # Layout wrapper
│   └── globals.css            # Global styles
├── components/
│   ├── pages/                 # Page-level components
│   │   └── home/             # Home page feature
│   │       ├── index.tsx     # Main component export
│   │       ├── components/   # Sub-components
│   │       └── hooks/        # Custom hooks
│   ├── shared/               # Shared components
│   │   ├── header/
│   │   └── sidebar/
│   ├── layouts/              # Layout components
│   │   └── main-layout/
│   └── ui/                   # Local UI overrides
├── lib/                       # Utilities
│   └── utils.ts
└── public/                    # Static assets
```

### Component Layer Explanation

#### 1. **app/** - Routing Layer
- **Purpose**: Define routes and metadata
- **Responsibility**: Import and render page components
- **Rule**: Keep thin, no business logic

```tsx
// app/page.tsx
import { HomePage } from '@/components/pages/home';

export default function Page() {
  return <HomePage />;
}
```

#### 2. **components/pages/** - Page Components
- **Purpose**: Page-level features
- **Structure**: Feature folders with modular organization

```
components/pages/home/
├── index.tsx              # Main component (composition)
├── components/            # Sub-components (presentation)
│   ├── welcome-card.tsx
│   ├── auth-status.tsx
│   └── stats-grid.tsx
├── hooks/                 # Custom hooks (logic)
│   ├── use-auth-state.ts
│   └── use-stats.ts
├── utils/                 # Helper functions
│   └── format-stats.ts
└── types/                 # Type definitions
    └── stats.types.ts
```

#### 3. **components/shared/** - Shared Components
- **Purpose**: Components used across multiple pages
- **Examples**: Header, Footer, Navigation, Modals

```
components/shared/
├── header/
│   ├── index.tsx
│   ├── components/
│   │   ├── logo.tsx
│   │   ├── nav-menu.tsx
│   │   └── user-menu.tsx
│   └── hooks/
│       └── use-navigation.ts
└── footer/
    └── index.tsx
```

#### 4. **components/layouts/** - Layout Components
- **Purpose**: Page layout wrappers
- **Examples**: MainLayout, AuthLayout, DashboardLayout

```
components/layouts/
└── main-layout/
    ├── index.tsx
    └── components/
        ├── sidebar.tsx
        └── topbar.tsx
```

### Creating a New Page

**Example**: Create a Dashboard page

1. **Create feature folder structure**:
```bash
mkdir -p components/pages/dashboard/{components,hooks,utils}
```

2. **Create index.tsx** (Main component):
```tsx
// components/pages/dashboard/index.tsx
'use client';

import { MainLayout } from '@/components/layouts/main-layout';
import { StatsGrid } from './components/stats-grid';
import { RecentOrders } from './components/recent-orders';
import { useDashboardData } from './hooks/use-dashboard-data';

export function DashboardPage() {
  const { stats, orders, loading } = useDashboardData();

  if (loading) return <div>Loading...</div>;

  return (
    <MainLayout>
      <div className="space-y-6">
        <h1>Dashboard</h1>
        <StatsGrid stats={stats} />
        <RecentOrders orders={orders} />
      </div>
    </MainLayout>
  );
}
```

3. **Create sub-components**:
```tsx
// components/pages/dashboard/components/stats-grid.tsx
import { Card } from '@toko/ui-web';

interface StatsGridProps {
  stats: {
    revenue: number;
    orders: number;
    customers: number;
  };
}

export function StatsGrid({ stats }: StatsGridProps) {
  return (
    <div className="grid grid-cols-3 gap-4">
      <Card>
        <h3>Revenue</h3>
        <p>{stats.revenue}</p>
      </Card>
      {/* ... */}
    </div>
  );
}
```

4. **Create custom hooks**:
```tsx
// components/pages/dashboard/hooks/use-dashboard-data.ts
'use client';

import { useEffect, useState } from 'react';
import { firebaseDb, collection, getDocs } from '@toko/firebase-client';

export function useDashboardData() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      // Fetch dashboard data
      setLoading(false);
    }
    fetchData();
  }, []);

  return { stats, orders: [], loading };
}
```

5. **Add route**:
```tsx
// app/dashboard/page.tsx
import { DashboardPage } from '@/components/pages/dashboard';

export default function Page() {
  return <DashboardPage />;
}
```

### Component Best Practices

#### ✅ DO

```tsx
// ✅ Use named exports for components
export function WelcomeCard() { }

// ✅ Colocate related code
components/pages/home/
  components/
  hooks/
  utils/

// ✅ Keep components focused
function StatsCard({ value, label }: StatsCardProps) {
  return <div>{value} {label}</div>;
}

// ✅ Use TypeScript interfaces
interface StatsCardProps {
  value: number;
  label: string;
}

// ✅ Extract business logic to hooks
const { data, loading } = useStats();
```

#### ❌ DON'T

```tsx
// ❌ Don't use default exports for components
export default function WelcomeCard() { }

// ❌ Don't mix concerns in one file
// (200 lines of mixed UI and logic)

// ❌ Don't create god components
function MegaComponent() {
  // 500 lines of everything
}

// ❌ Don't skip TypeScript types
function StatsCard(props: any) { } // ❌

// ❌ Don't put logic in components
function StatsCard() {
  const [data, setData] = useState();
  useEffect(() => {
    // 50 lines of data fetching ❌
  }, []);
}
```

---

## Development Workflow

### 1. Feature Development

```bash
# 1. Create feature branch
git checkout -b feature/dashboard-page

# 2. Create component structure
mkdir -p components/pages/dashboard/{components,hooks}

# 3. Develop with hot reload
pnpm dev:store-portal

# 4. Type check
pnpm typecheck

# 5. Lint
pnpm lint

# 6. Commit
git add .
git commit -m "feat(store-portal): add dashboard page"

# 7. Push and create PR
git push origin feature/dashboard-page
```

### 2. Using Shared Packages

```tsx
// Import from @toko packages
import { firebaseAuth, firebaseDb } from '@toko/firebase-client';
import { ProductSchema, CreateProductInput } from '@toko/shared-types';
import { Button, Card, Badge } from '@toko/ui-web';

// Validate with Zod
const product = ProductSchema.parse(data);

// Use Firebase
const user = firebaseAuth.currentUser;
```

### 3. Adding New Dependencies

```bash
# Add to specific app
pnpm --filter @toko/store-portal add package-name

# Add to shared package
pnpm --filter @toko/ui-web add package-name

# Add dev dependency to root
pnpm add -D -w package-name
```

---

## Code Style Guide

### File Naming

- **Components**: `kebab-case.tsx` (e.g., `stats-card.tsx`)
- **Hooks**: `use-*.ts` (e.g., `use-auth-state.ts`)
- **Utils**: `kebab-case.ts` (e.g., `format-currency.ts`)
- **Types**: `*.types.ts` (e.g., `product.types.ts`)

### Component Naming

```tsx
// ✅ PascalCase for components
export function StatsCard() { }
export function WelcomeMessage() { }

// ✅ camelCase for hooks
export function useAuthState() { }
export function useProductForm() { }

// ✅ camelCase for utilities
export function formatCurrency() { }
export function slugify() { }
```

### Import Order

```tsx
// 1. React/Next.js
import { useState, useEffect } from 'react';
import Link from 'next/link';

// 2. Third-party libraries
import { zodResolver } from '@hookform/resolvers/zod';

// 3. @toko packages
import { firebaseAuth } from '@toko/firebase-client';
import { ProductSchema } from '@toko/shared-types';
import { Button, Card } from '@toko/ui-web';

// 4. Local imports
import { useAuthState } from './hooks/use-auth-state';
import { WelcomeCard } from './components/welcome-card';
```

### TypeScript Guidelines

```tsx
// ✅ Use interfaces for props
interface ButtonProps {
  variant: 'default' | 'outline';
  onClick: () => void;
  children: React.ReactNode;
}

// ✅ Infer types from Zod schemas
import { ProductSchema } from '@toko/shared-types';
type Product = z.infer<typeof ProductSchema>;

// ✅ Use type for unions/intersections
type Status = 'pending' | 'active' | 'completed';

// ✅ Avoid 'any'
function process(data: unknown) { } // ✅
function process(data: any) { }     // ❌
```

---

## Testing Guidelines

### Unit Testing (Coming Soon)

```tsx
// Example: Testing a component
import { render, screen } from '@testing-library/react';
import { StatsCard } from './stats-card';

describe('StatsCard', () => {
  it('renders value and label', () => {
    render(<StatsCard value={100} label="Orders" />);
    expect(screen.getByText('100')).toBeInTheDocument();
    expect(screen.getByText('Orders')).toBeInTheDocument();
  });
});
```

---

## Deployment

### Development Deployment

```bash
# Deploy to dev environment
firebase use dev
pnpm deploy:store-portal
```

### Staging Deployment

```bash
# Deploy to staging
firebase use staging
pnpm deploy:all
```

### Production Deployment

```bash
# Deploy to production
firebase use prod
pnpm deploy:all
```

See [ENVIRONMENTS.md](./ENVIRONMENTS.md) for detailed environment configuration.

---

## Troubleshooting

### TypeScript Errors

```bash
# Build packages first
pnpm build

# Or run in dev mode (auto-builds)
pnpm dev
```

### Import Resolution Issues

```bash
# Clear Next.js cache
rm -rf .next

# Reinstall dependencies
rm -rf node_modules
pnpm install
```

### Firebase Connection Issues

Check environment variables:
```bash
# Verify .env.local has correct values
cat .env.local
```

---

## Additional Resources

- [ENVIRONMENTS.md](./ENVIRONMENTS.md) - Environment configuration
- [Next.js Documentation](https://nextjs.org/docs)
- [Firebase Documentation](https://firebase.google.com/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com)
- [Zod Documentation](https://zod.dev)

---

## Getting Help

- Check existing documentation
- Search closed issues
- Ask in team chat
- Create GitHub issue with reproduction

---

**Happy Coding! 🚀**
