# @toko/ui-web

Shared UI component library for **TOKO ANAK BANGSA** web applications. Built with [shadcn/ui](https://ui.shadcn.com/) and Tailwind CSS.

## Overview

This package provides a comprehensive set of reusable, accessible React components styled with Tailwind CSS. All components are built on top of Radix UI primitives for maximum accessibility and customization.

## Installation

This package is part of the monorepo and is automatically available to all Next.js apps.

```bash
pnpm add @toko/ui-web
```

## Setup in Next.js Apps

### 1. Import Global Styles

Add the following to your `app/globals.css` or `app/layout.tsx`:

```tsx
import '@toko/ui-web/styles';
```

### 2. Configure Tailwind

Extend your Tailwind config to include the UI package:

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/**/*.{ts,tsx}',
    '../../packages/ui-web/src/**/*.{ts,tsx}', // Include ui-web components
  ],
  presets: [require('../../packages/ui-web/tailwind.config')],
  theme: {
    extend: {},
  },
  plugins: [],
};

export default config;
```

### 3. Add Tailwind Plugins

Install required plugins:

```bash
pnpm add -D tailwindcss-animate
```

## Usage

### Button

```tsx
import { Button } from '@toko/ui-web';

export function MyComponent() {
  return (
    <div className="flex gap-2">
      <Button variant="default">Default</Button>
      <Button variant="destructive">Destructive</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="ghost">Ghost</Button>
      <Button variant="link">Link</Button>
      <Button size="sm">Small</Button>
      <Button size="lg">Large</Button>
      <Button size="icon">
        <IconPlus />
      </Button>
    </div>
  );
}
```

### Input & Label

```tsx
import { Input, Label } from '@toko/ui-web';

export function LoginForm() {
  return (
    <div className="space-y-4">
      <div>
        <Label htmlFor="email">Email</Label>
        <Input id="email" type="email" placeholder="nama@example.com" />
      </div>
      <div>
        <Label htmlFor="password">Password</Label>
        <Input id="password" type="password" />
      </div>
    </div>
  );
}
```

### Card

```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter, Button } from '@toko/ui-web';

export function ProductCard() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Laptop Asus ROG</CardTitle>
        <CardDescription>Gaming laptop with RTX 4060</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-2xl font-bold">Rp 15.000.000</p>
      </CardContent>
      <CardFooter>
        <Button className="w-full">Tambah ke Keranjang</Button>
      </CardFooter>
    </Card>
  );
}
```

### Badge

```tsx
import { Badge } from '@toko/ui-web';

export function OrderStatus() {
  return (
    <div className="flex gap-2">
      <Badge variant="default">Pending</Badge>
      <Badge variant="success">Completed</Badge>
      <Badge variant="warning">Processing</Badge>
      <Badge variant="destructive">Cancelled</Badge>
      <Badge variant="outline">Draft</Badge>
    </div>
  );
}
```

### Dialog

```tsx
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger, Button } from '@toko/ui-web';

export function DeleteProductDialog() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="destructive">Hapus Produk</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Hapus Produk?</DialogTitle>
          <DialogDescription>Aksi ini tidak dapat dibatalkan. Produk akan dihapus secara permanen.</DialogDescription>
        </DialogHeader>
        <div className="flex justify-end gap-2">
          <Button variant="outline">Batal</Button>
          <Button variant="destructive">Hapus</Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
```

### Toast Notifications

```tsx
'use client';

import { useToast, Button } from '@toko/ui-web';

export function ToastDemo() {
  const { toast } = useToast();

  return (
    <Button
      onClick={() => {
        toast({
          title: 'Produk berhasil ditambahkan',
          description: 'Laptop Asus ROG telah ditambahkan ke keranjang',
        });
      }}
    >
      Tampilkan Toast
    </Button>
  );
}
```

Don't forget to add the Toaster component to your root layout:

```tsx
// app/layout.tsx
import { ToastProvider, ToastViewport } from '@toko/ui-web';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <ToastProvider>
          {children}
          <ToastViewport />
        </ToastProvider>
      </body>
    </html>
  );
}
```

## Utility Functions

### `cn()` - Class Name Merger

Merge Tailwind CSS classes with proper precedence:

```tsx
import { cn } from '@toko/ui-web';

// Later classes override earlier ones
cn('px-2 py-1', 'px-4'); // Result: 'py-1 px-4'

// Conditional classes
cn('text-lg', isActive && 'font-bold', error && 'text-red-500');
```

### Indonesian Formatting Utilities

#### Format Currency (IDR)

```tsx
import { formatCurrency } from '@toko/ui-web';

formatCurrency(15000000); // "Rp 15.000.000"
formatCurrency(1500.5); // "Rp 1.500"
formatCurrency(999.99, { minimumFractionDigits: 2 }); // "Rp 999,99"
```

#### Format Numbers

```tsx
import { formatNumber } from '@toko/ui-web';

formatNumber(1234567); // "1.234.567"
formatNumber(12.345, { minimumFractionDigits: 2 }); // "12,35"
```

#### Format Dates

```tsx
import { formatDate, formatDateTime } from '@toko/ui-web';

formatDate(new Date()); // "13 Des 2024"
formatDate('2024-12-13'); // "13 Des 2024"

formatDateTime(new Date()); // "13 Des 2024, 14:30"
```

#### Phone Number Utilities

```tsx
import { isValidPhoneNumber, formatPhoneNumber } from '@toko/ui-web';

isValidPhoneNumber('081234567890'); // true
isValidPhoneNumber('+6281234567890'); // true
isValidPhoneNumber('1234'); // false

formatPhoneNumber('081234567890'); // "0812-3456-7890"
formatPhoneNumber('+6281234567890'); // "+62 812-3456-7890"
```

#### Other Utilities

```tsx
import { truncate, slugify } from '@toko/ui-web';

truncate('Very long product name here', 20); // "Very long product n..."

slugify('Laptop Asus ROG Strix'); // "laptop-asus-rog-strix"
slugify('Produk #1 @ Rp 100.000'); // "produk-1-rp-100000"
```

## Customization

### Theme Colors

The UI components use CSS variables for theming. You can customize colors in your app's `globals.css`:

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    /* ... customize other colors */
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    /* ... dark mode colors */
  }
}
```

### Component Customization

All components accept `className` prop for custom styling:

```tsx
<Button className="bg-blue-600 hover:bg-blue-700">Custom Button</Button>

<Card className="border-2 border-blue-500 shadow-xl">Custom Card</Card>
```

### Extending Components

Create your own variants using CVA:

```tsx
import { buttonVariants } from '@toko/ui-web';
import { cva } from 'class-variance-authority';

const myButtonVariants = cva(buttonVariants(), {
  variants: {
    size: {
      xl: 'h-14 px-10 text-lg',
    },
  },
});
```

## Available Components

### Form Components
- `Button` - Button with multiple variants
- `Input` - Text input field
- `Label` - Form label

### Layout Components
- `Card` - Card container with header, content, footer
- `Badge` - Status badge with variants
- `Separator` - Horizontal/vertical divider

### Overlay Components
- `Dialog` - Modal dialog
- `Toast` - Toast notifications
- `Popover` - Popover overlay
- `Tooltip` - Tooltip overlay

## Dark Mode

All components support dark mode out of the box. Enable dark mode using `class` strategy:

```tsx
// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="id" className="dark">
      {/* or use next-themes for toggle */}
      <body>{children}</body>
    </html>
  );
}
```

## Accessibility

All components are built on Radix UI primitives and follow WAI-ARIA guidelines:

- Keyboard navigation
- Screen reader support
- Focus management
- ARIA attributes

## TypeScript Support

All components are fully typed with TypeScript:

```tsx
import type { ButtonProps } from '@toko/ui-web';

const CustomButton: React.FC<ButtonProps> = (props) => {
  return <Button {...props} />;
};
```

## Best Practices

1. **Use semantic variants**: Choose variants that match the action intent (e.g., `destructive` for delete actions)
2. **Maintain consistency**: Use the same components across all apps for consistent UX
3. **Extend, don't override**: Prefer extending components over creating completely new ones
4. **Test accessibility**: Always test keyboard navigation and screen readers
5. **Use Indonesian locale**: All formatting utilities default to Indonesian locale

## Development

### Building

```bash
# Build once
pnpm build

# Watch mode
pnpm dev
```

### Type Checking

```bash
pnpm typecheck
```

### Linting

```bash
pnpm lint
```

## Adding New Components

To add a new shadcn/ui component:

1. Visit [ui.shadcn.com](https://ui.shadcn.com/)
2. Copy the component code
3. Create a new file in `src/components/ui/`
4. Export from `src/index.ts`
5. Update this README

## License

Private - TOKO ANAK BANGSA
