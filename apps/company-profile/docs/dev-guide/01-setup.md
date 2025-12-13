# Company Profile - Development Setup Guide

**Project**: Company Profile & Landing Page
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: Public-facing company website with information about TOKO ANAK BANGSA, product features, pricing, and lead generation

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
- All apps (company-profile, store-portal, marketplace, etc.)
- All packages (firebase-client, shared-types, ui-web)

### 3. Environment Configuration

Create environment file:

```bash
cd apps/company-profile
cp .env.example .env.local
```

Edit `.env.local`:

```env
# Firebase Configuration (for contact forms, newsletter)
NEXT_PUBLIC_FIREBASE_API_KEY=your-api-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project-id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id

# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8080/api

# App Configuration
NEXT_PUBLIC_APP_URL=http://localhost:3002
NODE_ENV=development

# Contact Form
NEXT_PUBLIC_CONTACT_EMAIL=info@tokoanak.id

# Google Analytics (optional)
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

Get Firebase credentials from [Firebase Console](https://console.firebase.google.com/) → Project Settings → General → Your apps → Web app

---

## Running the Application

### Development Server

**Option 1: From project root (recommended)**
```bash
# Start company-profile only
pnpm dev:company

# Or start all apps
pnpm dev
```

**Option 2: From app directory**
```bash
cd apps/company-profile
pnpm dev
```

The app will be available at: **http://localhost:3002**

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
apps/company-profile/
├── app/                        # Next.js 16 App Router
│   ├── [locale]/               # Internationalization routing
│   │   ├── page.tsx            # Homepage (hero, features, CTA)
│   │   ├── about/              # About us page
│   │   ├── features/           # Product features page
│   │   ├── pricing/            # Pricing plans page
│   │   ├── blog/               # Blog/news section
│   │   │   ├── page.tsx        # Blog list
│   │   │   └── [slug]/         # Blog post detail
│   │   ├── contact/            # Contact page
│   │   ├── demo/               # Request demo form
│   │   ├── privacy/            # Privacy policy
│   │   ├── terms/              # Terms of service
│   │   ├── layout.tsx          # Root layout
│   │   └── not-found.tsx       # 404 page
│   └── api/                    # API routes
│       ├── contact/            # Contact form submission
│       └── newsletter/         # Newsletter subscription
├── components/                 # React components
│   ├── ui/                     # Base UI components (from @toko/ui-web)
│   ├── layouts/                # Layout components
│   │   ├── Header.tsx          # Site header with navigation
│   │   ├── Footer.tsx          # Site footer
│   │   └── MobileMenu.tsx      # Mobile navigation
│   ├── sections/               # Page sections
│   │   ├── Hero.tsx            # Homepage hero section
│   │   ├── Features.tsx        # Features showcase
│   │   ├── HowItWorks.tsx      # How it works section
│   │   ├── Pricing.tsx         # Pricing table
│   │   ├── Testimonials.tsx    # Customer testimonials
│   │   ├── CTA.tsx             # Call-to-action sections
│   │   └── Stats.tsx           # Statistics section
│   ├── forms/                  # Form components
│   │   ├── ContactForm.tsx     # Contact form
│   │   ├── DemoRequestForm.tsx # Demo request form
│   │   └── NewsletterForm.tsx  # Newsletter signup
│   └── common/                 # Shared components
│       ├── FeatureCard.tsx     # Feature card
│       ├── PricingCard.tsx     # Pricing plan card
│       └── TestimonialCard.tsx # Testimonial card
├── lib/                        # Utility libraries
│   ├── firebase.ts             # Firebase client initialization
│   ├── api.ts                  # API client
│   ├── analytics.ts            # Google Analytics
│   └── utils.ts                # Helper functions
├── hooks/                      # Custom React hooks
│   ├── useContactForm.ts       # Contact form submission
│   └── useNewsletter.ts        # Newsletter subscription
├── types/                      # TypeScript type definitions
│   └── index.ts                # Local types
├── i18n/                       # Internationalization
│   ├── routing.ts              # i18n routing configuration
│   └── request.ts              # i18n request configuration
├── messages/                   # Translation files
│   ├── en.json                 # English translations
│   └── id.json                 # Indonesian translations
├── content/                    # Content files
│   ├── blog/                   # Blog posts (MDX)
│   └── testimonials/           # Testimonials data
├── public/                     # Static files
│   ├── images/                 # Images
│   │   ├── hero/               # Hero images
│   │   ├── features/           # Feature screenshots
│   │   └── logos/              # Company logos
│   ├── icons/                  # Icons
│   └── videos/                 # Demo videos
├── styles/                     # Global styles
│   └── globals.css             # Tailwind CSS
├── middleware.ts               # Next.js middleware (i18n)
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
pnpm dev:company

# Access at http://localhost:3002
```

### 2. Add New Dependency

**App-specific dependency:**
```bash
cd apps/company-profile
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

### Public Routes
- `/` - Homepage (hero, features, how it works, pricing, testimonials, CTA)
- `/about` - About TOKO ANAK BANGSA (mission, vision, team)
- `/features` - Product features showcase (POS, inventory, marketplace, etc.)
- `/pricing` - Subscription plans and pricing
- `/blog` - Blog/news listing
- `/blog/[slug]` - Individual blog post
- `/contact` - Contact form
- `/demo` - Request demo form
- `/privacy` - Privacy policy
- `/terms` - Terms of service

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
    "getStarted": "Mulai Sekarang",
    "learnMore": "Pelajari Lebih Lanjut",
    "requestDemo": "Minta Demo"
  },
  "hero": {
    "title": "Solusi POS & Marketplace Terbaik untuk UMKM Indonesia",
    "subtitle": "Kelola toko, inventori, dan penjualan online dalam satu platform",
    "cta": "Coba Gratis 14 Hari"
  },
  "features": {
    "pos": "Kasir (POS)",
    "inventory": "Manajemen Inventori",
    "marketplace": "Marketplace Online",
    "reports": "Laporan & Analitik"
  },
  "pricing": {
    "free": "Gratis",
    "basic": "Basic",
    "pro": "Pro",
    "enterprise": "Enterprise"
  }
}
```

### Use in Component

```tsx
'use client';

import { useTranslations } from 'next-intl';

export default function HeroSection() {
  const t = useTranslations('hero');

  return (
    <section>
      <h1>{t('title')}</h1>
      <p>{t('subtitle')}</p>
      <button>{t('cta')}</button>
    </section>
  );
}
```

---

## Contact Form Implementation

### Contact Form Component

```tsx
'use client';

import { useState } from 'react';
import { useTranslations } from 'next-intl';

export default function ContactForm() {
  const t = useTranslations('contact');
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    company: '',
    message: '',
  });
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Failed to submit');

      setSubmitted(true);
      setFormData({ name: '', email: '', phone: '', company: '', message: '' });
    } catch (error) {
      console.error('Contact form error:', error);
      alert('Failed to submit form. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  if (submitted) {
    return (
      <div className="success-message">
        <h3>{t('thankYou')}</h3>
        <p>{t('weWillContact')}</p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder={t('name')}
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        required
      />
      <input
        type="email"
        placeholder={t('email')}
        value={formData.email}
        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        required
      />
      <input
        type="tel"
        placeholder={t('phone')}
        value={formData.phone}
        onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
      />
      <input
        type="text"
        placeholder={t('company')}
        value={formData.company}
        onChange={(e) => setFormData({ ...formData, company: e.target.value })}
      />
      <textarea
        placeholder={t('message')}
        value={formData.message}
        onChange={(e) => setFormData({ ...formData, message: e.target.value })}
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? t('submitting') : t('submit')}
      </button>
    </form>
  );
}
```

### Contact API Route

```typescript
// app/api/contact/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { db } from '@toko/firebase-client';
import { collection, addDoc } from 'firebase/firestore';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { name, email, phone, company, message } = body;

    // Validate input
    if (!name || !email || !message) {
      return NextResponse.json(
        { error: 'Missing required fields' },
        { status: 400 }
      );
    }

    // Save to Firestore
    await addDoc(collection(db, 'contact_submissions'), {
      name,
      email,
      phone: phone || '',
      company: company || '',
      message,
      submittedAt: new Date().toISOString(),
      status: 'new',
    });

    // TODO: Send email notification to sales team

    return NextResponse.json(
      { success: true, message: 'Contact form submitted successfully' },
      { status: 200 }
    );
  } catch (error) {
    console.error('Contact form error:', error);
    return NextResponse.json(
      { error: 'Failed to submit contact form' },
      { status: 500 }
    );
  }
}
```

---

## Newsletter Subscription

### Newsletter Form

```tsx
'use client';

import { useState } from 'react';

export default function NewsletterForm() {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [subscribed, setSubscribed] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('/api/newsletter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });

      if (!response.ok) throw new Error('Failed to subscribe');

      setSubscribed(true);
      setEmail('');
    } catch (error) {
      console.error('Newsletter error:', error);
      alert('Failed to subscribe. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  if (subscribed) {
    return <p>✓ Terima kasih! Anda telah berlangganan newsletter kami.</p>;
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        placeholder="Email Anda"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Berlangganan...' : 'Berlangganan'}
      </button>
    </form>
  );
}
```

---

## Google Analytics Integration

### Analytics Setup

```typescript
// lib/analytics.ts
export const GA_MEASUREMENT_ID = process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID;

export const pageview = (url: string) => {
  if (typeof window.gtag !== 'undefined') {
    window.gtag('config', GA_MEASUREMENT_ID!, {
      page_path: url,
    });
  }
};

export const event = ({ action, category, label, value }: {
  action: string;
  category: string;
  label?: string;
  value?: number;
}) => {
  if (typeof window.gtag !== 'undefined') {
    window.gtag('event', action, {
      event_category: category,
      event_label: label,
      value: value,
    });
  }
};
```

### Track Page Views

```tsx
// app/layout.tsx
'use client';

import { useEffect } from 'react';
import { usePathname } from 'next/navigation';
import { pageview } from '@/lib/analytics';

export default function RootLayout({ children }) {
  const pathname = usePathname();

  useEffect(() => {
    pageview(pathname);
  }, [pathname]);

  return (
    <html>
      <body>{children}</body>
    </html>
  );
}
```

---

## SEO Optimization

### Metadata for Homepage

```typescript
// app/[locale]/page.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'TOKO ANAK BANGSA - Solusi POS & Marketplace Terbaik untuk UMKM Indonesia',
  description: 'Platform all-in-one untuk mengelola toko, inventori, kasir (POS), dan marketplace online. Mudah digunakan, harga terjangkau, support 24/7.',
  keywords: 'POS, kasir, marketplace, UMKM, Indonesia, inventory, toko online',
  openGraph: {
    title: 'TOKO ANAK BANGSA - Solusi POS & Marketplace',
    description: 'Platform all-in-one untuk UMKM Indonesia',
    images: ['/images/og-image.png'],
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'TOKO ANAK BANGSA',
    description: 'Solusi POS & Marketplace untuk UMKM',
    images: ['/images/twitter-image.png'],
  },
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

### Issue: Port 3002 already in use

**Solution:** Kill the process or use a different port:
```bash
# Kill process
lsof -ti:3002 | xargs kill -9

# Or use different port
pnpm dev -- --port 3006
```

### Issue: Firebase initialization error

**Solution:** Check that:
1. `.env.local` exists with correct Firebase credentials
2. All `NEXT_PUBLIC_*` variables are set
3. Restart dev server after changing `.env.local`

### Issue: Contact form not submitting

**Solution:** Check:
1. API route is accessible at `/api/contact`
2. Firestore collection `contact_submissions` exists
3. Network tab for errors

### Issue: Images not loading

**Solution:** Ensure:
1. Images are in `public/images/` directory
2. Image paths start with `/images/` (not `./images/`)
3. Next.js Image component is configured correctly

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
| `NEXT_PUBLIC_APP_URL` | App URL | `http://localhost:3002` | Yes |
| `NEXT_PUBLIC_CONTACT_EMAIL` | Contact email | `info@tokoanak.id` | Yes |
| `NEXT_PUBLIC_GA_MEASUREMENT_ID` | Google Analytics ID | `G-XXXXXXXXXX` | No |
| `NODE_ENV` | Environment | `development` | Yes |

---

## Useful Commands

```bash
# Start development server
pnpm dev:company

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

# Optimize images
pnpm optimize:images
```

---

## Content Management

### Adding Blog Posts

Create a new MDX file in `content/blog/`:

```mdx
---
title: "5 Tips Meningkatkan Penjualan Toko Kelontong"
date: "2024-12-13"
author: "Tim TOKO ANAK BANGSA"
category: "Tips Bisnis"
image: "/images/blog/tips-penjualan.jpg"
excerpt: "Panduan praktis untuk meningkatkan penjualan toko kelontong Anda"
---

# 5 Tips Meningkatkan Penjualan Toko Kelontong

Berikut adalah tips praktis yang bisa langsung Anda terapkan...

## 1. Kelola Stok dengan Baik

Pastikan produk favorit pelanggan selalu tersedia...

## 2. Tawarkan Harga Kompetitif

Bandingkan harga dengan kompetitor...
```

### Adding Testimonials

Edit `content/testimonials/index.json`:

```json
[
  {
    "id": "1",
    "name": "Budi Santoso",
    "company": "Toko Makmur, Jakarta",
    "role": "Pemilik Toko",
    "avatar": "/images/testimonials/budi.jpg",
    "content": "TOKO ANAK BANGSA sangat membantu bisnis saya. Sekarang saya bisa fokus melayani pelanggan, sistem yang urus sisanya!",
    "rating": 5
  }
]
```

---

## Next Steps

1. Read `02-architecture.md` (when available) to understand system design
2. Read `03-coding-standards.md` (when available) for code conventions
3. Review UI component library in `packages/ui-web`
4. Review shared types in `packages/shared-types`
5. Add company branding and content
6. Set up Google Analytics for tracking

---

**Last Updated**: 2024-12-13
