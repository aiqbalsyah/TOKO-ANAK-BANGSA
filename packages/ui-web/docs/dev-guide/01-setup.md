# UI Web - Development Setup Guide

**Project**: UI Web Component Library
**Tech Stack**: React 19, TypeScript, Tailwind CSS, Radix UI, tsup
**Purpose**: Shared UI component library for all TOKO ANAK BANGSA web applications

---

## Overview

`@toko/ui-web` is a shared package that provides reusable React components for all web applications in the monorepo. It's built on top of Radix UI primitives and styled with Tailwind CSS, ensuring consistency, accessibility, and great developer experience across all apps.

**Why a Shared UI Library?**
- **Consistency**: Uniform look and feel across all applications
- **Reusability**: Write components once, use everywhere
- **Accessibility**: Built on Radix UI primitives (WAI-ARIA compliant)
- **Maintainability**: Update UI in one place, all apps benefit
- **Performance**: Tree-shakeable, only import what you need
- **Type Safety**: Full TypeScript support

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js 22+** - [Download Node.js](https://nodejs.org/)
- **pnpm 9+** - Install: `npm install -g pnpm`
- **TypeScript knowledge** - This is a TypeScript library
- **React 19 knowledge** - For component development
- **Tailwind CSS knowledge** - For styling

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

This will install dependencies for this package and all consuming apps.

### 3. Package Structure

```
packages/ui-web/
├── src/                    # Source code
│   ├── components/         # UI components
│   │   ├── ui/             # Base components (Radix UI wrappers)
│   │   │   ├── button.tsx
│   │   │   ├── input.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── dropdown-menu.tsx
│   │   │   ├── select.tsx
│   │   │   ├── checkbox.tsx
│   │   │   ├── avatar.tsx
│   │   │   ├── toast.tsx
│   │   │   └── ...
│   │   └── composed/       # Composed/complex components
│   │       ├── data-table.tsx
│   │       ├── card.tsx
│   │       ├── form.tsx
│   │       └── ...
│   ├── styles/             # Global styles
│   │   └── globals.css     # Tailwind base + custom styles
│   ├── utils/              # Utility functions
│   │   └── cn.ts           # className utility (clsx + tailwind-merge)
│   ├── hooks/              # Custom React hooks
│   │   └── use-toast.ts    # Toast notifications
│   └── index.ts            # Main export file
├── dist/                   # Build output (generated)
│   ├── index.js            # CommonJS build
│   ├── index.mjs           # ESM build
│   └── index.d.ts          # Type definitions
├── docs/                   # Documentation
│   └── dev-guide/          # Developer guides
├── package.json            # Package configuration
├── tsconfig.json           # TypeScript configuration
├── tailwind.config.ts      # Tailwind configuration
└── README.md               # Package overview
```

---

## Development Workflow

### 1. Build Package

**Development mode (watch):**
```bash
cd packages/ui-web
pnpm dev
```

This will build the package and watch for changes, automatically rebuilding when you edit source files.

**Production build:**
```bash
pnpm build
```

### 2. Add New Component

Create a new component in `src/components/ui/`:

```tsx
// src/components/ui/badge.tsx
import * as React from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '../../utils/cn';

const badgeVariants = cva(
  'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground',
        secondary: 'bg-secondary text-secondary-foreground',
        success: 'bg-green-100 text-green-800',
        warning: 'bg-yellow-100 text-yellow-800',
        danger: 'bg-red-100 text-red-800',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
);

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

export function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  );
}
```

Export it in `src/index.ts`:

```typescript
export * from './components/ui/badge';
```

### 3. Type Checking

```bash
pnpm typecheck
```

### 4. Linting

```bash
pnpm lint
```

### 5. Clean Build Artifacts

```bash
pnpm clean
```

---

## Package Configuration

### Build Setup (tsup)

The package uses `tsup` for building. Configuration in `package.json`:

```json
{
  "scripts": {
    "build": "tsup src/index.ts --format cjs,esm --dts --external react --external react-dom",
    "dev": "tsup src/index.ts --format cjs,esm --dts --external react --external react-dom --watch"
  }
}
```

**Note**: React and React DOM are externalized (peer dependencies).

### Package Exports

```json
{
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    },
    "./styles": "./src/styles/globals.css"
  }
}
```

Apps can import styles:
```typescript
import '@toko/ui-web/styles';
```

---

## Using the Package in Apps

### Installation

Apps in the monorepo reference this package via workspace protocol:

```json
{
  "dependencies": {
    "@toko/ui-web": "workspace:*"
  }
}
```

### Import Styles

In your app's root layout or global CSS file:

```tsx
// app/layout.tsx
import '@toko/ui-web/styles';
import './globals.css';
```

### Import Components

```tsx
import {
  Button,
  Input,
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  Select,
  Checkbox,
  Avatar,
  Toast,
  useToast,
} from '@toko/ui-web';
```

---

## Component Examples

### Example: Button Component

```tsx
// src/components/ui/button.tsx
import * as React from 'react';
import { Slot } from '@radix-ui/react-slot';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '../../utils/cn';

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline: 'border border-input hover:bg-accent hover:text-accent-foreground',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'underline-offset-4 hover:underline text-primary',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : 'button';
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = 'Button';

export { Button, buttonVariants };
```

### Example: Input Component

```tsx
// src/components/ui/input.tsx
import * as React from 'react';
import { cn } from '../../utils/cn';

export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          'flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
          className
        )}
        ref={ref}
        {...props}
      />
    );
  }
);
Input.displayName = 'Input';

export { Input };
```

### Example: Dialog Component (Radix UI Wrapper)

```tsx
// src/components/ui/dialog.tsx
import * as React from 'react';
import * as DialogPrimitive from '@radix-ui/react-dialog';
import { X } from 'lucide-react';
import { cn } from '../../utils/cn';

const Dialog = DialogPrimitive.Root;
const DialogTrigger = DialogPrimitive.Trigger;
const DialogPortal = DialogPrimitive.Portal;
const DialogClose = DialogPrimitive.Close;

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      'fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0',
      className
    )}
    {...props}
  />
));
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName;

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        'fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg',
        className
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
));
DialogContent.displayName = DialogPrimitive.Content.displayName;

const DialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      'flex flex-col space-y-1.5 text-center sm:text-left',
      className
    )}
    {...props}
  />
);
DialogHeader.displayName = 'DialogHeader';

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn(
      'text-lg font-semibold leading-none tracking-tight',
      className
    )}
    {...props}
  />
));
DialogTitle.displayName = DialogPrimitive.Title.displayName;

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogClose,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogTitle,
};
```

### Example: Utility Function (cn)

```typescript
// src/utils/cn.ts
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Merge Tailwind CSS classes with proper precedence
 * Uses clsx for conditional classes and tailwind-merge to handle conflicts
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

### Example: Toast Hook

```typescript
// src/hooks/use-toast.ts
import * as React from 'react';

type ToastProps = {
  id: string;
  title?: string;
  description?: string;
  variant?: 'default' | 'destructive';
};

export function useToast() {
  const [toasts, setToasts] = React.useState<ToastProps[]>([]);

  const toast = React.useCallback(
    ({
      title,
      description,
      variant = 'default',
    }: Omit<ToastProps, 'id'>) => {
      const id = Math.random().toString(36).slice(2, 9);
      setToasts((prev) => [...prev, { id, title, description, variant }]);

      // Auto dismiss after 5 seconds
      setTimeout(() => {
        setToasts((prev) => prev.filter((t) => t.id !== id));
      }, 5000);

      return id;
    },
    []
  );

  const dismiss = React.useCallback((id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  return { toasts, toast, dismiss };
}
```

---

## Usage in Applications

### Example: Using Button in Store Portal

```tsx
// apps/store-portal/app/[locale]/(dashboard)/products/page.tsx
'use client';

import { Button } from '@toko/ui-web';
import { PlusIcon } from 'lucide-react';

export default function ProductsPage() {
  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1>Products</h1>
        <Button>
          <PlusIcon className="mr-2 h-4 w-4" />
          Add Product
        </Button>
      </div>

      <div className="flex gap-2">
        <Button variant="outline">Export</Button>
        <Button variant="secondary">Import</Button>
        <Button variant="destructive">Delete Selected</Button>
      </div>
    </div>
  );
}
```

### Example: Using Dialog

```tsx
'use client';

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  Button,
  Input,
} from '@toko/ui-web';
import { useState } from 'react';

export function CreateProductDialog() {
  const [open, setOpen] = useState(false);

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>Create Product</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Create New Product</DialogTitle>
        </DialogHeader>
        <div className="space-y-4">
          <Input placeholder="Product name" />
          <Input placeholder="Price" type="number" />
          <Input placeholder="Stock" type="number" />
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => setOpen(false)}>
              Cancel
            </Button>
            <Button>Create</Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}
```

### Example: Using Toast

```tsx
'use client';

import { Button, useToast } from '@toko/ui-web';

export function ProductActions() {
  const { toast } = useToast();

  const handleDelete = () => {
    // Perform delete...
    toast({
      title: 'Product deleted',
      description: 'The product has been removed from inventory',
      variant: 'default',
    });
  };

  const handleError = () => {
    toast({
      title: 'Error',
      description: 'Failed to delete product. Please try again.',
      variant: 'destructive',
    });
  };

  return (
    <div>
      <Button onClick={handleDelete}>Delete Product</Button>
    </div>
  );
}
```

---

## Tailwind Configuration

### Base Tailwind Config

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
} satisfies Config;
```

### Global Styles

```css
/* src/styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 212.7 26.8% 83.9%;
  }
}
```

---

## Best Practices

### 1. Component Composition

Build complex components from simpler ones:

```tsx
// ✅ Good: Composed from base components
export function LoginForm() {
  return (
    <div className="space-y-4">
      <Input type="email" placeholder="Email" />
      <Input type="password" placeholder="Password" />
      <Button className="w-full">Login</Button>
    </div>
  );
}
```

### 2. Use Variants for Styling

```tsx
// ✅ Good: Use CVA for variant management
const buttonVariants = cva('base-classes', {
  variants: {
    variant: { ... },
    size: { ... },
  },
});
```

### 3. Forward Refs

Always forward refs for components that wrap HTML elements:

```tsx
const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (props, ref) => <button ref={ref} {...props} />
);
```

### 4. Export Component Props

```tsx
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'outline';
}
```

### 5. Use cn() for Class Merging

```tsx
<Button className={cn('custom-class', props.className)} />
```

---

## Common Issues & Troubleshooting

### Issue: Styles not applying

**Solution:** Ensure global styles are imported:
```tsx
import '@toko/ui-web/styles';
```

### Issue: React version mismatch

**Solution:** Check peer dependencies. All apps must use React 19:
```json
{
  "peerDependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  }
}
```

### Issue: Tailwind classes not working

**Solution:** Configure Tailwind to scan ui-web package:
```typescript
// apps/*/tailwind.config.ts
export default {
  content: [
    './app/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    '../../packages/ui-web/src/**/*.{ts,tsx}', // Add this
  ],
};
```

### Issue: Component not exporting

**Solution:** Ensure component is exported in `src/index.ts`:
```typescript
export * from './components/ui/button';
```

---

## Useful Commands

```bash
# Build package
pnpm build

# Watch mode (development)
pnpm dev

# Type check
pnpm typecheck

# Lint
pnpm lint

# Clean build artifacts
pnpm clean

# Build from project root
pnpm build --filter @toko/ui-web
```

---

## Adding New Components

1. Create component in `src/components/ui/`
2. Export from `src/index.ts`
3. Build package: `pnpm build`
4. Use in apps: `import { NewComponent } from '@toko/ui-web'`

---

## Next Steps

1. Review Radix UI documentation: https://radix-ui.com
2. Review Tailwind CSS documentation: https://tailwindcss.com
3. Add more components as needed
4. Create Storybook for component documentation (optional)
5. Write component tests

---

**Last Updated**: 2024-12-13
