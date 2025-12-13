# Internationalization (i18n) - Multi-Language Support

**Category**: SETUP
**Priority**: MUST HAVE (MVP)
**Phase**: 1

---

## Overview

Platform supports **Indonesian (default)** and **English** languages for all user-facing content.

---

## Supported Languages

1. **Indonesian (Bahasa Indonesia)** - Default
   - Language code: `id` or `id-ID`
   - Default for all users
   - All content available in Indonesian

2. **English**
   - Language code: `en` or `en-US`
   - Secondary language
   - All content available in English

---

## User Stories

**As a user (store owner or customer),**
**I want to switch between Indonesian and English,**
**So that I can use the platform in my preferred language.**

**Acceptance Criteria**:
- ✅ Default language is Indonesian
- ✅ Language selector available in UI (header/settings)
- ✅ User can switch to English
- ✅ Language preference persists across sessions
- ✅ All UI text translated (buttons, labels, messages)
- ✅ Error messages translated
- ✅ Email notifications translated
- ✅ Static content translated (terms, privacy, help)

---

## Scope of Translation

### What Gets Translated

**✅ User Interface**:
- Navigation menus
- Buttons and labels
- Form fields and placeholders
- Validation messages
- Error messages
- Success messages
- Tooltips and hints

**✅ Static Content**:
- Landing pages
- Terms of Service
- Privacy Policy
- Help documentation
- FAQ

**✅ Email Templates**:
- Order confirmation
- Payment confirmation
- Shipping updates
- Password reset
- Welcome emails

**✅ Notifications**:
- In-app notifications
- Email notifications
- SMS (if applicable)

### What Does NOT Get Translated

**❌ User-Generated Content**:
- Store names
- Product names
- Product descriptions
- Customer reviews
- Store descriptions

**Note**: Store owners create content in their preferred language. We don't auto-translate user content.

---

## Technical Implementation

### Framework: next-intl (Next.js)

**Library**: `next-intl` (recommended for Next.js 13+ App Router)

```bash
pnpm add next-intl
```

**Directory Structure**:

```
apps/store-portal/
├── messages/
│   ├── id.json          # Indonesian translations
│   └── en.json          # English translations
├── middleware.ts        # Language detection
└── app/
    └── [locale]/        # Locale-based routing
        ├── layout.tsx
        └── page.tsx

apps/marketplace/
├── messages/
│   ├── id.json
│   └── en.json
└── app/
    └── [locale]/
        └── ...
```

---

### Translation Files

**Indonesian (`messages/id.json`)**:

```json
{
  "common": {
    "save": "Simpan",
    "cancel": "Batal",
    "delete": "Hapus",
    "edit": "Edit",
    "search": "Cari",
    "loading": "Memuat...",
    "error": "Terjadi kesalahan",
    "success": "Berhasil"
  },
  "auth": {
    "login": "Masuk",
    "logout": "Keluar",
    "register": "Daftar",
    "email": "Email",
    "password": "Kata Sandi",
    "forgotPassword": "Lupa Kata Sandi?",
    "createAccount": "Buat Akun",
    "signInWithGoogle": "Masuk dengan Google"
  },
  "product": {
    "name": "Nama Produk",
    "description": "Deskripsi",
    "price": "Harga",
    "stock": "Stok",
    "category": "Kategori",
    "images": "Gambar",
    "addProduct": "Tambah Produk",
    "editProduct": "Edit Produk",
    "deleteProduct": "Hapus Produk",
    "units": {
      "dus": "Dus",
      "pack": "Pack",
      "pcs": "Pcs"
    },
    "pricing": {
      "cost": "Harga Modal",
      "priceA": "Harga Grosir (A)",
      "priceB": "Harga Eceran (B)",
      "priceC": "Harga Member (C)",
      "margin": "Margin"
    }
  },
  "order": {
    "title": "Pesanan",
    "newOrder": "Pesanan Baru",
    "orderNumber": "Nomor Pesanan",
    "customer": "Pelanggan",
    "total": "Total",
    "status": "Status",
    "date": "Tanggal",
    "statusValues": {
      "pending": "Menunggu Pembayaran",
      "paid": "Dibayar",
      "processing": "Diproses",
      "shipped": "Dikirim",
      "delivered": "Diterima",
      "cancelled": "Dibatalkan"
    }
  },
  "shipping": {
    "enableShipping": "Aktifkan Pengiriman",
    "pickupOnly": "Ambil di Toko",
    "shippingCost": "Ongkos Kirim",
    "courier": "Kurir",
    "service": "Layanan",
    "weight": "Berat (gram)",
    "dimensions": "Dimensi (cm)",
    "width": "Lebar",
    "length": "Panjang",
    "height": "Tinggi"
  },
  "validation": {
    "required": "{{field}} wajib diisi",
    "email": "Email tidak valid",
    "minLength": "{{field}} minimal {{min}} karakter",
    "maxLength": "{{field}} maksimal {{max}} karakter",
    "number": "{{field}} harus berupa angka",
    "positive": "{{field}} harus lebih dari 0"
  }
}
```

**English (`messages/en.json`)**:

```json
{
  "common": {
    "save": "Save",
    "cancel": "Cancel",
    "delete": "Delete",
    "edit": "Edit",
    "search": "Search",
    "loading": "Loading...",
    "error": "An error occurred",
    "success": "Success"
  },
  "auth": {
    "login": "Login",
    "logout": "Logout",
    "register": "Register",
    "email": "Email",
    "password": "Password",
    "forgotPassword": "Forgot Password?",
    "createAccount": "Create Account",
    "signInWithGoogle": "Sign in with Google"
  },
  "product": {
    "name": "Product Name",
    "description": "Description",
    "price": "Price",
    "stock": "Stock",
    "category": "Category",
    "images": "Images",
    "addProduct": "Add Product",
    "editProduct": "Edit Product",
    "deleteProduct": "Delete Product",
    "units": {
      "dus": "Carton",
      "pack": "Pack",
      "pcs": "Pieces"
    },
    "pricing": {
      "cost": "Cost Price",
      "priceA": "Wholesale Price (A)",
      "priceB": "Retail Price (B)",
      "priceC": "Member Price (C)",
      "margin": "Margin"
    }
  },
  "order": {
    "title": "Orders",
    "newOrder": "New Order",
    "orderNumber": "Order Number",
    "customer": "Customer",
    "total": "Total",
    "status": "Status",
    "date": "Date",
    "statusValues": {
      "pending": "Pending Payment",
      "paid": "Paid",
      "processing": "Processing",
      "shipped": "Shipped",
      "delivered": "Delivered",
      "cancelled": "Cancelled"
    }
  },
  "shipping": {
    "enableShipping": "Enable Shipping",
    "pickupOnly": "Pick-up Only",
    "shippingCost": "Shipping Cost",
    "courier": "Courier",
    "service": "Service",
    "weight": "Weight (grams)",
    "dimensions": "Dimensions (cm)",
    "width": "Width",
    "length": "Length",
    "height": "Height"
  },
  "validation": {
    "required": "{{field}} is required",
    "email": "Invalid email",
    "minLength": "{{field}} must be at least {{min}} characters",
    "maxLength": "{{field}} must be at most {{max}} characters",
    "number": "{{field}} must be a number",
    "positive": "{{field}} must be greater than 0"
  }
}
```

---

### Configuration Files

**next-intl setup (`apps/store-portal/i18n.ts`)**:

```typescript
import { getRequestConfig } from 'next-intl/server';

export default getRequestConfig(async ({ locale }) => ({
  messages: (await import(`./messages/${locale}.json`)).default
}));
```

**Middleware (`apps/store-portal/middleware.ts`)**:

```typescript
import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
  // Supported locales
  locales: ['id', 'en'],

  // Default locale
  defaultLocale: 'id',

  // Locale detection
  localeDetection: true
});

export const config = {
  // Match all pathnames except for
  // - /api (API routes)
  // - /_next (Next.js internals)
  // - /static (static files)
  matcher: ['/((?!api|_next|static|.*\\..*).*)']
};
```

**Root Layout (`apps/store-portal/app/[locale]/layout.tsx`)**:

```typescript
import { NextIntlClientProvider } from 'next-intl';
import { notFound } from 'next/navigation';

const locales = ['id', 'en'];

export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export default async function LocaleLayout({
  children,
  params: { locale }
}: {
  children: React.Node;
  params: { locale: string };
}) {
  // Validate locale
  if (!locales.includes(locale)) notFound();

  let messages;
  try {
    messages = (await import(`@/messages/${locale}.json`)).default;
  } catch (error) {
    notFound();
  }

  return (
    <html lang={locale}>
      <body>
        <NextIntlClientProvider locale={locale} messages={messages}>
          {children}
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
```

---

### Usage in Components

**Using translations**:

```typescript
'use client';

import { useTranslations } from 'next-intl';

export function ProductForm() {
  const t = useTranslations('product');

  return (
    <form>
      <label>{t('name')}</label>
      <input placeholder={t('name')} />

      <label>{t('description')}</label>
      <textarea placeholder={t('description')} />

      <label>{t('pricing.priceA')}</label>
      <input type="number" />

      <button>{t('save', { ns: 'common' })}</button>
    </form>
  );
}
```

**Language Switcher Component**:

```typescript
'use client';

import { useLocale } from 'next-intl';
import { usePathname, useRouter } from 'next/navigation';

export function LanguageSwitcher() {
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();

  const switchLocale = (newLocale: string) => {
    // Replace current locale in pathname
    const newPathname = pathname.replace(`/${locale}`, `/${newLocale}`);
    router.push(newPathname);
  };

  return (
    <select value={locale} onChange={(e) => switchLocale(e.target.value)}>
      <option value="id">🇮🇩 Bahasa Indonesia</option>
      <option value="en">🇺🇸 English</option>
    </select>
  );
}
```

---

### Data Model (User Preference)

**Firestore - User Document**:

```javascript
// Collection: users/{userId}
{
  id: "user_123",
  email: "user@example.com",
  displayName: "John Doe",

  // Preferences
  preferences: {
    language: "id",  // or "en"
    theme: "light",
    notifications: true
  },

  createdAt: timestamp,
  updatedAt: timestamp
}
```

---

### Routing Structure

**URL Structure**:

```
# Indonesian (default)
https://admin.yourmarketplace.com/id/dashboard
https://www.yourmarketplace.com/id/products

# English
https://admin.yourmarketplace.com/en/dashboard
https://www.yourmarketplace.com/en/products

# Auto-redirect if no locale
https://admin.yourmarketplace.com/dashboard
→ https://admin.yourmarketplace.com/id/dashboard (default)
```

---

## Email Templates (i18n)

**Email Template Structure**:

```
functions/email-templates/
├── id/
│   ├── order-confirmation.html
│   ├── payment-confirmation.html
│   └── password-reset.html
└── en/
    ├── order-confirmation.html
    ├── payment-confirmation.html
    └── password-reset.html
```

**Cloud Function - Send Email**:

```javascript
export const sendOrderConfirmation = functions.firestore
  .document('orders/{orderId}')
  .onCreate(async (snap, context) => {
    const order = snap.data();

    // Get user language preference
    const userDoc = await admin.firestore()
      .doc(`users/${order.customerId}`)
      .get();

    const userLanguage = userDoc.data()?.preferences?.language || 'id';

    // Load email template in user's language
    const template = await loadEmailTemplate(`${userLanguage}/order-confirmation.html`);

    // Send email
    await sendEmail({
      to: order.customerEmail,
      subject: userLanguage === 'id' ? 'Konfirmasi Pesanan' : 'Order Confirmation',
      html: template.render({ order })
    });
  });
```

---

## Currency & Number Formatting

**Indonesian Format**:
- Currency: Rp 150,000
- Decimal separator: comma (,)
- Thousands separator: period (.)
- Example: Rp 1.500.000,50

**English/US Format**:
- Currency: IDR 150,000
- Decimal separator: period (.)
- Thousands separator: comma (,)
- Example: IDR 1,500,000.50

**Implementation**:

```typescript
import { useLocale } from 'next-intl';

export function useCurrencyFormat() {
  const locale = useLocale();

  const formatCurrency = (amount: number) => {
    if (locale === 'id') {
      return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR'
      }).format(amount);
    } else {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'IDR'
      }).format(amount);
    }
  };

  return { formatCurrency };
}

// Usage:
// const { formatCurrency } = useCurrencyFormat();
// formatCurrency(150000)
// → "Rp150.000" (id) or "IDR150,000" (en)
```

---

## Date & Time Formatting

**Implementation**:

```typescript
export function useDateFormat() {
  const locale = useLocale();

  const formatDate = (date: Date) => {
    return new Intl.DateTimeFormat(locale === 'id' ? 'id-ID' : 'en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    }).format(date);
  };

  const formatDateTime = (date: Date) => {
    return new Intl.DateTimeFormat(locale === 'id' ? 'id-ID' : 'en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    }).format(date);
  };

  return { formatDate, formatDateTime };
}

// Usage:
// formatDate(new Date())
// → "13 Desember 2024" (id) or "December 13, 2024" (en)
```

---

## Implementation Checklist

### Setup
- [ ] Install `next-intl` package
- [ ] Create translation files (`id.json`, `en.json`)
- [ ] Configure middleware for locale detection
- [ ] Setup locale-based routing (`[locale]` folder)

### Translation
- [ ] Translate all UI text (common, auth, product, order, etc.)
- [ ] Translate validation messages
- [ ] Translate email templates
- [ ] Translate static pages (terms, privacy, help)

### Components
- [ ] Create LanguageSwitcher component
- [ ] Add language selector to header
- [ ] Update all components to use `useTranslations()`
- [ ] Implement currency formatting
- [ ] Implement date/time formatting

### Backend
- [ ] Store user language preference in Firestore
- [ ] Update email functions to use user's language
- [ ] Translate Firebase error messages

### Testing
- [ ] Test all pages in Indonesian
- [ ] Test all pages in English
- [ ] Test language switching
- [ ] Test currency formatting (both locales)
- [ ] Test email templates (both languages)
- [ ] Test language persistence across sessions

---

## References

- [next-intl Documentation](https://next-intl-docs.vercel.app/)
- [Next.js Internationalization](https://nextjs.org/docs/app/building-your-application/routing/internationalization)

---

**Last Updated**: 2024-12-13
