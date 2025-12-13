# Platform Admin - Development Setup Guide

**Project**: Platform Admin (System Administration Panel)
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: System-level administration for managing tenants, subscriptions, users, monitoring, and platform operations

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
- All apps (platform-admin, store-portal, marketplace, etc.)
- All packages (firebase-client, shared-types, ui-web)

### 3. Environment Configuration

Create environment file:

```bash
cd apps/platform-admin
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
NEXT_PUBLIC_APP_URL=http://localhost:3003
NODE_ENV=development

# Admin Configuration
NEXT_PUBLIC_ADMIN_EMAIL_DOMAIN=@tokoanak.id
```

Get Firebase credentials from [Firebase Console](https://console.firebase.google.com/) → Project Settings → General → Your apps → Web app

---

## Running the Application

### Development Server

**Option 1: From project root (recommended)**
```bash
# Start platform-admin only
pnpm dev:admin

# Or start all apps
pnpm dev
```

**Option 2: From app directory**
```bash
cd apps/platform-admin
pnpm dev
```

The app will be available at: **http://localhost:3003**

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
apps/platform-admin/
├── app/                        # Next.js 16 App Router
│   ├── [locale]/               # Internationalization routing
│   │   ├── (auth)/             # Authentication routes
│   │   │   ├── login/          # Admin login
│   │   │   └── forgot-password/ # Password reset
│   │   ├── (dashboard)/        # Admin dashboard (protected)
│   │   │   ├── layout.tsx      # Dashboard layout with sidebar
│   │   │   ├── page.tsx        # Platform overview dashboard
│   │   │   ├── tenants/        # Tenant management
│   │   │   │   ├── page.tsx    # Tenant list
│   │   │   │   ├── [id]/       # Tenant detail
│   │   │   │   └── create/     # Create new tenant
│   │   │   ├── users/          # User management
│   │   │   │   ├── page.tsx    # All users across tenants
│   │   │   │   └── [id]/       # User detail
│   │   │   ├── subscriptions/  # Subscription management
│   │   │   │   ├── page.tsx    # All subscriptions
│   │   │   │   ├── plans/      # Subscription plans
│   │   │   │   └── billing/    # Billing & payments
│   │   │   ├── analytics/      # Platform analytics
│   │   │   │   ├── revenue/    # Revenue analytics
│   │   │   │   ├── growth/     # Growth metrics
│   │   │   │   └── churn/      # Churn analysis
│   │   │   ├── monitoring/     # System monitoring
│   │   │   │   ├── health/     # System health
│   │   │   │   ├── performance/ # Performance metrics
│   │   │   │   ├── errors/     # Error tracking
│   │   │   │   └── logs/       # System logs
│   │   │   ├── support/        # Support tools
│   │   │   │   ├── tickets/    # Support tickets
│   │   │   │   └── impersonate/ # User impersonation
│   │   │   └── settings/       # Platform settings
│   │   │       ├── general/    # General settings
│   │   │       ├── features/   # Feature flags
│   │   │       └── integrations/ # Third-party integrations
│   │   ├── layout.tsx          # Root layout
│   │   └── page.tsx            # Home page
│   └── api/                    # API routes
│       ├── impersonate/        # User impersonation endpoint
│       └── export/             # Data export endpoints
├── components/                 # React components
│   ├── ui/                     # Base UI components (from @toko/ui-web)
│   ├── layouts/                # Layout components
│   │   ├── DashboardLayout.tsx # Admin dashboard layout
│   │   └── Sidebar.tsx         # Admin navigation sidebar
│   ├── tenants/                # Tenant management components
│   │   ├── TenantList.tsx      # Tenant table
│   │   ├── TenantCard.tsx      # Tenant summary card
│   │   ├── TenantForm.tsx      # Create/edit tenant
│   │   └── TenantStats.tsx     # Tenant statistics
│   ├── users/                  # User management components
│   │   ├── UserList.tsx        # User table
│   │   └── UserDetail.tsx      # User profile
│   ├── subscriptions/          # Subscription components
│   │   ├── SubscriptionList.tsx # Subscription table
│   │   ├── PlanCard.tsx        # Subscription plan card
│   │   └── BillingHistory.tsx  # Billing history
│   ├── analytics/              # Analytics components
│   │   ├── RevenueChart.tsx    # Revenue visualization
│   │   ├── GrowthChart.tsx     # Growth metrics
│   │   ├── ChurnChart.tsx      # Churn analysis
│   │   └── MetricCard.tsx      # KPI metric card
│   ├── monitoring/             # Monitoring components
│   │   ├── SystemHealth.tsx    # System health dashboard
│   │   ├── PerformanceChart.tsx # Performance metrics
│   │   ├── ErrorLog.tsx        # Error log viewer
│   │   └── LogViewer.tsx       # System log viewer
│   └── common/                 # Shared components
│       ├── DataTable.tsx       # Generic data table
│       ├── StatCard.tsx        # Statistic card
│       └── DateRangePicker.tsx # Date range selector
├── lib/                        # Utility libraries
│   ├── firebase.ts             # Firebase client initialization
│   ├── api.ts                  # API client
│   ├── auth.ts                 # Admin authentication
│   ├── impersonation.ts        # User impersonation logic
│   └── utils.ts                # Helper functions
├── hooks/                      # Custom React hooks
│   ├── useAuth.ts              # Admin authentication
│   ├── useTenants.ts           # Tenant data management
│   ├── useSubscriptions.ts     # Subscription data
│   ├── useAnalytics.ts         # Analytics data
│   └── useMonitoring.ts        # Monitoring data
├── types/                      # TypeScript type definitions
│   └── index.ts                # Local types (Admin, Metrics, etc.)
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
├── middleware.ts               # Next.js middleware (admin auth, role check)
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
pnpm dev:admin

# Access at http://localhost:3003
```

### 2. Add New Dependency

**App-specific dependency:**
```bash
cd apps/platform-admin
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

### Authentication Routes (Public)
- `/login` - Admin login (restricted to @tokoanak.id emails)
- `/forgot-password` - Password reset

### Dashboard Routes (Protected - Admin Only)
- `/` - Platform overview dashboard (KPIs, system health)

**Tenant Management:**
- `/tenants` - All tenants list and management
- `/tenants/[id]` - Tenant detail and configuration
- `/tenants/create` - Create new tenant

**User Management:**
- `/users` - All users across all tenants
- `/users/[id]` - User detail and management

**Subscription Management:**
- `/subscriptions` - All active subscriptions
- `/subscriptions/plans` - Subscription plan management
- `/subscriptions/billing` - Billing and payment tracking

**Analytics:**
- `/analytics/revenue` - Revenue analytics (MRR, ARR, growth)
- `/analytics/growth` - User and tenant growth metrics
- `/analytics/churn` - Churn analysis and retention

**Monitoring:**
- `/monitoring/health` - System health and uptime
- `/monitoring/performance` - API performance metrics
- `/monitoring/errors` - Error tracking and alerting
- `/monitoring/logs` - System logs viewer

**Support:**
- `/support/tickets` - Support ticket management
- `/support/impersonate` - User impersonation tool

**Settings:**
- `/settings/general` - Platform-wide settings
- `/settings/features` - Feature flags management
- `/settings/integrations` - Third-party integrations

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
  "tenants": {
    "title": "Tenant",
    "createTenant": "Buat Tenant Baru",
    "suspendTenant": "Suspend Tenant"
  },
  "analytics": {
    "mrr": "MRR (Pendapatan Bulanan Berulang)",
    "activeUsers": "Pengguna Aktif",
    "churnRate": "Tingkat Churn"
  }
}
```

### Use in Component

```tsx
'use client';

import { useTranslations } from 'next-intl';

export default function TenantsPage() {
  const t = useTranslations('tenants');

  return (
    <div>
      <h1>{t('title')}</h1>
      <button>{t('createTenant')}</button>
    </div>
  );
}
```

---

## Admin Authentication

### Admin Login (Restricted Access)

```tsx
'use client';

import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '@/lib/firebase';
import { useRouter } from 'next/navigation';

export default function AdminLoginPage() {
  const router = useRouter();

  const handleLogin = async (email: string, password: string) => {
    // Check if email is from allowed domain
    if (!email.endsWith('@tokoanak.id')) {
      alert('Only @tokoanak.id emails can access admin panel');
      return;
    }

    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;

      // Get ID token
      const idToken = await user.getIdToken();

      // Verify admin role via API
      const response = await fetch('/api/auth/verify-admin', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idToken }),
      });

      if (!response.ok) {
        throw new Error('Not authorized as admin');
      }

      // Create admin session
      await fetch('/api/auth/session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idToken, role: 'admin' }),
      });

      // Redirect to dashboard
      router.push('/');
    } catch (error) {
      console.error('Admin login failed:', error);
    }
  };

  return (
    // Admin login form
  );
}
```

### Protected Admin Routes

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;
  const isPublicPath = path === '/login' || path === '/forgot-password';
  const token = request.cookies.get('admin-token')?.value;
  const adminRole = request.cookies.get('admin-role')?.value;

  // Redirect to login if accessing protected route without admin token
  if (!isPublicPath && (!token || adminRole !== 'admin')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Redirect to dashboard if accessing auth pages with admin token
  if (isPublicPath && token && adminRole === 'admin') {
    return NextResponse.redirect(new URL('/', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
};
```

---

## User Impersonation

### Impersonation Feature

Allows admins to impersonate users for support and debugging purposes.

```tsx
'use client';

import { useState } from 'react';
import { apiRequest } from '@/lib/api';

export default function ImpersonationPage() {
  const [userId, setUserId] = useState('');
  const [loading, setLoading] = useState(false);

  const handleImpersonate = async () => {
    if (!userId) return;

    setLoading(true);

    try {
      // Generate impersonation token
      const response = await apiRequest('/admin/impersonate', {
        method: 'POST',
        body: JSON.stringify({ userId }),
      });

      // Open store-portal in new window with impersonation token
      const impersonateUrl = `http://localhost:3000/impersonate?token=${response.token}`;
      window.open(impersonateUrl, '_blank');
    } catch (error) {
      console.error('Impersonation failed:', error);
      alert('Failed to impersonate user');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Impersonate User</h1>
      <input
        type="text"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />
      <button onClick={handleImpersonate} disabled={loading}>
        {loading ? 'Impersonating...' : 'Impersonate'}
      </button>

      <div className="warning">
        <p>⚠️ All actions taken during impersonation are logged</p>
        <p>Use only for legitimate support purposes</p>
      </div>
    </div>
  );
}
```

---

## Analytics Dashboard

### Platform Metrics

```tsx
'use client';

import { useAnalytics } from '@/hooks/useAnalytics';
import { MetricCard } from '@/components/analytics/MetricCard';
import { RevenueChart } from '@/components/analytics/RevenueChart';

export default function DashboardPage() {
  const { data, loading } = useAnalytics({
    dateRange: 'last_30_days',
  });

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Platform Dashboard</h1>

      <div className="metrics-grid">
        <MetricCard
          title="Total Tenants"
          value={data.tenants.total}
          change={data.tenants.growth}
          trend="up"
        />
        <MetricCard
          title="Active Users"
          value={data.users.active}
          change={data.users.growth}
          trend="up"
        />
        <MetricCard
          title="MRR"
          value={`IDR ${data.revenue.mrr.toLocaleString('id-ID')}`}
          change={data.revenue.growth}
          trend="up"
        />
        <MetricCard
          title="Churn Rate"
          value={`${data.churn.rate}%`}
          change={data.churn.change}
          trend="down"
        />
      </div>

      <RevenueChart data={data.revenue.history} />

      <div className="system-health">
        <h2>System Health</h2>
        <p>API Uptime: {data.health.uptime}%</p>
        <p>Avg Response Time: {data.health.responseTime}ms</p>
        <p>Error Rate: {data.health.errorRate}%</p>
      </div>
    </div>
  );
}
```

---

## API Integration

### Admin API Client

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

// Tenant Management
export const getTenants = (params?: {
  status?: string;
  plan?: string;
  search?: string;
  page?: number;
  limit?: number;
}) => {
  const queryString = new URLSearchParams(params as any).toString();
  return apiRequest<{ tenants: Tenant[]; total: number }>(`/admin/tenants?${queryString}`);
};

export const getTenant = (id: string) =>
  apiRequest<Tenant>(`/admin/tenants/${id}`);

export const suspendTenant = (id: string, reason: string) =>
  apiRequest(`/admin/tenants/${id}/suspend`, {
    method: 'POST',
    body: JSON.stringify({ reason }),
  });

// Analytics
export const getAnalytics = (dateRange: string) =>
  apiRequest<PlatformAnalytics>(`/admin/analytics?dateRange=${dateRange}`);

// Monitoring
export const getSystemHealth = () =>
  apiRequest<SystemHealth>('/admin/monitoring/health');

export const getErrorLogs = (params?: {
  level?: string;
  since?: string;
  limit?: number;
}) => {
  const queryString = new URLSearchParams(params as any).toString();
  return apiRequest<ErrorLog[]>(`/admin/monitoring/errors?${queryString}`);
};
```

---

## Common Issues & Troubleshooting

### Issue: `Module not found` errors

**Solution:** Ensure all dependencies are installed:
```bash
# From project root
pnpm install
```

### Issue: Port 3003 already in use

**Solution:** Kill the process or use a different port:
```bash
# Kill process
lsof -ti:3003 | xargs kill -9

# Or use different port
pnpm dev -- --port 3005
```

### Issue: Firebase initialization error

**Solution:** Check that:
1. `.env.local` exists with correct Firebase credentials
2. All `NEXT_PUBLIC_*` variables are set
3. Restart dev server after changing `.env.local`

### Issue: Cannot access admin panel

**Solution:** Ensure:
1. Using an email ending with `@tokoanak.id`
2. User has `admin` role in Firebase custom claims
3. Admin token cookie is set

### Issue: Analytics data not loading

**Solution:** Check:
1. API is running and accessible
2. Admin authentication token is valid
3. CORS is configured for admin panel URL
4. Network tab for API errors

### Issue: Impersonation not working

**Solution:** Verify:
1. User ID is valid and exists
2. Impersonation token is generated correctly
3. store-portal accepts impersonation tokens
4. Impersonation action is logged in audit logs

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
| `NEXT_PUBLIC_APP_URL` | App URL | `http://localhost:3003` | Yes |
| `NEXT_PUBLIC_ADMIN_EMAIL_DOMAIN` | Allowed admin email domain | `@tokoanak.id` | Yes |
| `NODE_ENV` | Environment | `development` | Yes |

---

## Useful Commands

```bash
# Start development server
pnpm dev:admin

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

# Export analytics data
pnpm export:analytics
```

---

## Security Considerations

### Admin Access Control

1. **Email Restriction**: Only `@tokoanak.id` emails can access admin panel
2. **Role Verification**: Verify admin role in Firebase custom claims
3. **Multi-Factor Authentication**: Enable MFA for all admin accounts (recommended)
4. **IP Whitelisting**: Consider restricting admin panel to office IPs (production)

### Audit Logging

All admin actions should be logged:

```typescript
// Log admin action
await apiRequest('/admin/audit-log', {
  method: 'POST',
  body: JSON.stringify({
    action: 'suspend_tenant',
    targetId: tenantId,
    reason: suspensionReason,
    timestamp: new Date().toISOString(),
  }),
});
```

### Data Access

- Admins have cross-tenant access - use responsibly
- All data access should be justified and logged
- Implement data masking for sensitive information (passwords, payment details)
- Regular security audits of admin activities

---

## Next Steps

1. Read `02-architecture.md` (when available) to understand system design
2. Read `03-coding-standards.md` (when available) for code conventions
3. Review feature documentation: `/docs/features/14-platform-admin.md`
4. Check UI component library in `packages/ui-web`
5. Review shared types in `packages/shared-types`
6. Set up admin user with proper permissions

---

**Last Updated**: 2024-12-13
