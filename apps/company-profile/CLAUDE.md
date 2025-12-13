# Claude Code Guide - Company Profile

**Project**: Company Profile & Landing Page
**Tech Stack**: Next.js 16, React 19, TypeScript, Tailwind CSS, next-intl
**Purpose**: Public-facing company website with information, features, pricing, blog, and lead generation

---

## Quick Start

This is a **public marketing website** - no authentication, simpler than other apps.

### Documentation

**Read these:**
- `apps/company-profile/README.md` - Project overview
- `apps/company-profile/docs/dev-guide/01-setup.md` - Complete setup guide
- `apps/store-portal/CLAUDE.md` - Shared Next.js patterns

### Key Features

1. **Static Pages**: Most pages are static or ISR (Incremental Static Regeneration)
2. **Forms**: Contact form, demo request, newsletter signup
3. **SEO**: Heavy focus on metadata, Open Graph, structured data
4. **Performance**: Optimized images, minimal JavaScript
5. **Port**: Runs on `http://localhost:3002`

### Implementation Patterns

**Contact Form:**

```tsx
// app/[locale]/contact/page.tsx
'use client';

import { useState } from 'react';
import { Button, Input } from '@toko/ui-web';

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    if (response.ok) {
      alert('Thank you! We will contact you soon.');
      setFormData({ name: '', email: '', message: '' });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        placeholder="Your Name"
        required
      />
      <Input
        type="email"
        value={formData.email}
        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        placeholder="Your Email"
        required
      />
      <textarea
        value={formData.message}
        onChange={(e) => setFormData({ ...formData, message: e.target.value })}
        placeholder="Your Message"
        required
      />
      <Button type="submit">Send Message</Button>
    </form>
  );
}
```

**API Route for Contact Form:**

```typescript
// app/api/contact/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { db } from '@toko/firebase-client';
import { collection, addDoc } from 'firebase/firestore';

export async function POST(request: NextRequest) {
  try {
    const { name, email, message } = await request.json();

    // Save to Firestore
    await addDoc(collection(db, 'contact_submissions'), {
      name,
      email,
      message,
      submittedAt: new Date().toISOString(),
      status: 'new',
    });

    // TODO: Send email notification

    return NextResponse.json({ success: true }, { status: 200 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to submit' },
      { status: 500 }
    );
  }
}
```

**SEO Metadata:**

```typescript
// app/[locale]/page.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'TOKO ANAK BANGSA - Solusi POS & Marketplace Terbaik',
  description: 'Platform all-in-one untuk UMKM Indonesia. Kelola toko, inventori, dan marketplace dalam satu sistem.',
  keywords: 'POS, kasir, marketplace, UMKM, Indonesia, inventory',
  openGraph: {
    title: 'TOKO ANAK BANGSA',
    description: 'Solusi POS & Marketplace untuk UMKM',
    images: ['/images/og-image.png'],
  },
};
```

### File Organization

```
apps/company-profile/
├── app/[locale]/
│   ├── page.tsx                # Homepage
│   ├── about/page.tsx          # About page
│   ├── features/page.tsx       # Features page
│   ├── pricing/page.tsx        # Pricing page
│   ├── blog/
│   │   ├── page.tsx            # Blog list
│   │   └── [slug]/page.tsx     # Blog post
│   ├── contact/page.tsx        # Contact form
│   └── api/
│       ├── contact/route.ts    # Contact form API
│       └── newsletter/route.ts # Newsletter API
├── components/
│   ├── sections/               # Page sections
│   │   ├── Hero.tsx
│   │   ├── Features.tsx
│   │   ├── Pricing.tsx
│   │   └── CTA.tsx
│   └── forms/
│       ├── ContactForm.tsx
│       └── NewsletterForm.tsx
└── content/
    ├── blog/                   # MDX blog posts
    └── testimonials/           # Testimonial data
```

### Environment Variables

```env
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_CONTACT_EMAIL=info@tokoanak.id
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

### Commands

```bash
pnpm dev:company      # Start on port 3002
```

---

**Focus on SEO, performance, and lead generation forms.**

**Last Updated**: 2024-12-13
