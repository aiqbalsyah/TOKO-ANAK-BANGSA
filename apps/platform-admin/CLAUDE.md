# Claude Code Guide - Platform Admin

**Project**: Platform Admin (System Administration Panel)
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: System-level administration for managing tenants, subscriptions, users, monitoring, and platform operations

---

## Quick Start

This app follows **Store Portal patterns** but with cross-tenant admin features.

### Documentation

**Read these:**
- `apps/platform-admin/README.md` - Project overview
- `apps/platform-admin/docs/dev-guide/01-setup.md` - Complete setup guide
- `docs/features/14-platform-admin.md` - Platform admin specifications
- `apps/store-portal/CLAUDE.md` - Shared Next.js patterns

### Key Differences

1. **Admin-Only Access**: Restricted to `@tokoanak.id` email addresses
2. **Cross-Tenant Data**: Access data across all tenants
3. **User Impersonation**: Ability to impersonate users for support
4. **System Monitoring**: Platform health, analytics, logs
5. **Port**: Runs on `http://localhost:3003`

### Implementation Patterns

**Admin Authentication Check:**

```tsx
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('admin-token')?.value;
  const adminRole = request.cookies.get('admin-role')?.value;
  const path = request.nextUrl.pathname;
  const isPublicPath = path === '/login';

  // Require admin authentication
  if (!isPublicPath && (!token || adminRole !== 'admin')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}
```

**Admin Login (Email Domain Check):**

```tsx
// app/[locale]/(auth)/login/page.tsx
'use client';

import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '@toko/firebase-client';

export default function AdminLoginPage() {
  const handleLogin = async (email: string, password: string) => {
    // Check email domain
    if (!email.endsWith('@tokoanak.id')) {
      alert('Only @tokoanak.id emails can access admin panel');
      return;
    }

    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    const idToken = await userCredential.user.getIdToken();

    // Verify admin role via API
    const response = await fetch('/api/auth/verify-admin', {
      method: 'POST',
      body: JSON.stringify({ idToken }),
    });

    if (!response.ok) {
      throw new Error('Not authorized as admin');
    }

    // Redirect to dashboard
    router.push('/');
  };

  return (
    // Login form
  );
}
```

**Cross-Tenant Data Access:**

```tsx
// app/[locale]/(dashboard)/tenants/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { Tenant } from '@toko/shared-types';

export default function TenantsPage() {
  const [tenants, setTenants] = useState<Tenant[]>([]);

  useEffect(() => {
    fetchAllTenants();
  }, []);

  const fetchAllTenants = async () => {
    // Admin API endpoint - returns all tenants
    const response = await fetch('/api/admin/tenants');
    const data = await response.json();
    setTenants(data.tenants);
  };

  return (
    <div>
      <h1>All Tenants ({tenants.length})</h1>
      {/* Tenant management UI */}
    </div>
  );
}
```

**User Impersonation:**

```tsx
// app/[locale]/(dashboard)/support/impersonate/page.tsx
'use client';

export default function ImpersonatePage() {
  const handleImpersonate = async (userId: string) => {
    // Generate impersonation token
    const response = await fetch('/api/admin/impersonate', {
      method: 'POST',
      body: JSON.stringify({ userId }),
    });

    const { token } = await response.json();

    // Open store-portal with impersonation token
    const url = `http://localhost:3000/impersonate?token=${token}`;
    window.open(url, '_blank');
  };

  return (
    <div>
      <h1>Impersonate User</h1>
      <p>⚠️ All actions are logged. Use for support only.</p>
      {/* User selection UI */}
    </div>
  );
}
```

**Platform Analytics:**

```tsx
// app/[locale]/(dashboard)/page.tsx
'use client';

import { MetricCard } from '@/components/analytics/MetricCard';
import { useAnalytics } from '@/hooks/useAnalytics';

export default function DashboardPage() {
  const { data, loading } = useAnalytics({ dateRange: 'last_30_days' });

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Platform Dashboard</h1>

      <div className="grid grid-cols-4 gap-4">
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
    </div>
  );
}
```

### File Organization

```
apps/platform-admin/
├── app/[locale]/(dashboard)/
│   ├── page.tsx               # Platform dashboard
│   ├── tenants/               # Tenant management
│   ├── users/                 # User management
│   ├── subscriptions/         # Subscription management
│   ├── analytics/             # Platform analytics
│   ├── monitoring/            # System monitoring
│   └── support/               # Support tools
├── components/
│   ├── tenants/               # Tenant components
│   ├── analytics/             # Charts and metrics
│   └── monitoring/            # System health components
└── hooks/
    ├── useTenants.ts          # Tenant data
    ├── useAnalytics.ts        # Analytics data
    └── useMonitoring.ts       # Monitoring data
```

### Security Considerations

1. **Email Domain Check**: Only `@tokoanak.id` can access
2. **Admin Role Verification**: Check Firebase custom claims
3. **Audit Logging**: Log all admin actions
4. **Data Masking**: Mask sensitive data (passwords, payment info)
5. **IP Whitelisting**: Consider restricting to office IPs (production)

### Environment Variables

```env
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_API_URL=http://localhost:8080/api
NEXT_PUBLIC_ADMIN_EMAIL_DOMAIN=@tokoanak.id
```

### Commands

```bash
pnpm dev:admin        # Start on port 3003
```

---

**Handle with care - this app has elevated privileges and cross-tenant access.**

**Last Updated**: 2024-12-13
