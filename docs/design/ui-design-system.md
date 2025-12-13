# TOKO ANAK BANGSA - UI Design System

**Product**: TOKO ANAK BANGSA
**Design Reference**: `/docs/ui-sample/`
**UI Library**: shadcn/ui + Tailwind CSS
**Last Updated**: 2024-12-13

---

## Design Philosophy

**Clean, Modern, Data-Focused**

The TOKO ANAK BANGSA design system prioritizes:
- **Clarity**: Clear information hierarchy and data visualization
- **Efficiency**: Quick access to important metrics and actions
- **Professionalism**: Business-oriented design suitable for SMEs
- **Accessibility**: High contrast, readable fonts, clear visual cues
- **Indonesian Market**: Familiar patterns for local users

---

## Color Palette

### Primary Colors

**Dark Green (Primary)**
- Main: `#2B5F4C` (RGB: 43, 95, 76)
- Use: Sidebar, primary buttons, headers
- Tailwind: `bg-emerald-800`

**Light Green (Accent)**
- Main: `#7AC29A` (RGB: 122, 194, 154)
- Use: Active states, selected items, success indicators
- Tailwind: `bg-emerald-400`

**Mint Green (Success/Positive)**
- Main: `#D4F1E3` (RGB: 212, 241, 227)
- Use: Metric cards (positive), success messages
- Tailwind: `bg-emerald-100`

### Secondary Colors

**Light Blue (Info)**
- Main: `#D8E9FA` (RGB: 216, 233, 250)
- Use: Metric cards (info), informational messages
- Tailwind: `bg-blue-100`

**Light Purple (Neutral)**
- Main: `#E8E5F2` (RGB: 232, 229, 242)
- Use: Alternative metric cards
- Tailwind: `bg-purple-100`

### Neutral Colors

**White**
- Main: `#FFFFFF`
- Use: Main background, cards

**Light Gray**
- Main: `#F5F7FA` (RGB: 245, 247, 250)
- Use: Page background, subtle borders
- Tailwind: `bg-gray-50`

**Medium Gray**
- Main: `#6B7280` (RGB: 107, 114, 128)
- Use: Secondary text, subtitles
- Tailwind: `text-gray-500`

**Dark Gray**
- Main: `#1F2937` (RGB: 31, 41, 55)
- Use: Primary text, headings
- Tailwind: `text-gray-800`

### Status Colors

**Normal/Optimal**
- Color: `#7AC29A` (Light Green)
- Badge: Rounded, light background

**High/Warning**
- Color: `#FCD34D` (Yellow)
- Use: Warnings, high values
- Tailwind: `bg-yellow-300`

**Error/Critical**
- Color: `#EF4444` (Red)
- Use: Errors, critical alerts
- Tailwind: `bg-red-500`

---

## Typography

### Font Family

**Primary Font**: Inter, system-ui, -apple-system, sans-serif

```css
font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont,
             'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

### Font Sizes

```css
/* Headings */
h1: 2rem (32px) - font-bold
h2: 1.5rem (24px) - font-semibold
h3: 1.25rem (20px) - font-semibold
h4: 1.125rem (18px) - font-medium
h5: 1rem (16px) - font-medium

/* Body */
base: 0.875rem (14px) - font-normal
small: 0.75rem (12px) - font-normal
tiny: 0.625rem (10px) - font-normal

/* Display (Big Numbers) */
display-xl: 3rem (48px) - font-bold
display-lg: 2.5rem (40px) - font-bold
display-md: 2rem (32px) - font-semibold
```

### Font Weights

```css
font-light: 300
font-normal: 400
font-medium: 500
font-semibold: 600
font-bold: 700
```

---

## Layout Structure

### Sidebar Layout

**Desktop (> 1024px)**:
```
┌─────────────────────────────────────────────────┐
│ [Sidebar]  [Main Content Area]                  │
│  200px           Fluid                          │
│                                                 │
│   Logo      Header (Greeting + Filters)        │
│   Nav       ─────────────────────────────      │
│   Items     Metric Cards (Grid 2-4 columns)    │
│   ...       ─────────────────────────────      │
│             Content Sections                    │
│             (Charts, Tables, etc.)              │
│                                                 │
│   Profile   Footer                              │
└─────────────────────────────────────────────────┘
```

**Tablet (768px - 1023px)**:
- Sidebar collapses to icon-only (60px)
- Main content expands

**Mobile (< 768px)**:
- Sidebar becomes bottom navigation or hamburger menu
- Single column layout
- Stack metric cards vertically

### Grid System

**Metric Cards Grid**:
```css
/* Desktop: 4 columns */
grid-cols-4 gap-4

/* Tablet: 2 columns */
md:grid-cols-2 gap-3

/* Mobile: 1 column */
grid-cols-1 gap-2
```

---

## Tailwind Theme Configuration

Before creating components, we setup a proper Tailwind theme with semantic color tokens. This ensures consistency and makes it easy to maintain brand colors.

### Complete `tailwind.config.ts`

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        // TOKO ANAK BANGSA Brand Colors (Semantic Tokens)
        brand: {
          // Primary (Dark Green)
          primary: {
            DEFAULT: '#2B5F4C',      // Main dark green
            foreground: '#D4F1E3',   // Light text on dark green
            hover: '#234C3E',        // Darker on hover
          },

          // Secondary (Medium Green)
          secondary: {
            DEFAULT: '#3D7A5E',      // Medium green
            foreground: '#FFFFFF',   // White text
            hover: '#2B5F4C',        // Darker on hover
          },

          // Accent (Light Green)
          accent: {
            DEFAULT: '#7AC29A',      // Light green
            foreground: '#1F2937',   // Dark text on light background
            hover: '#5DB380',        // Slightly darker
          },

          // Success/Positive (Mint Green)
          success: {
            DEFAULT: '#D4F1E3',      // Mint green background
            foreground: '#2B5F4C',   // Dark green text
            border: '#7AC29A',       // Light green border
          },
        },

        // Status Colors (Semantic)
        status: {
          normal: {
            bg: '#D4F1E3',           // Mint green
            text: '#2B5F4C',         // Dark green
          },
          high: {
            bg: '#FEF3C7',           // Light yellow
            text: '#92400E',         // Dark yellow
          },
          optimal: {
            bg: '#DBEAFE',           // Light blue
            text: '#1E3A8A',         // Dark blue
          },
          active: {
            bg: '#ECFDF5',           // Very light green
            text: '#065F46',         // Medium dark green
          },
          success: {
            bg: '#D1FAE5',           // Light green
            text: '#065F46',         // Dark green
          },
          warning: {
            bg: '#FEF3C7',           // Light yellow
            text: '#92400E',         // Dark yellow
          },
          error: {
            bg: '#FEE2E2',           // Light red
            text: '#991B1B',         // Dark red
          },
        },

        // Neutral Colors
        background: {
          DEFAULT: '#FFFFFF',        // White
          muted: '#F9FAFB',         // Very light gray (page background)
          subtle: '#F3F4F6',        // Light gray
        },

        // Text Colors
        text: {
          primary: '#111827',        // Almost black
          secondary: '#6B7280',      // Medium gray
          muted: '#9CA3AF',         // Light gray
          inverse: '#FFFFFF',       // White
        },

        // Border Colors
        border: {
          DEFAULT: '#E5E7EB',       // Light gray
          muted: '#F3F4F6',         // Very light gray
          focus: '#7AC29A',         // Brand accent
        },

        // Metric Card Colors
        metric: {
          dark: {
            bg: '#2B5F4C',           // Dark green
            text: '#FFFFFF',         // White
            subtitle: '#D4F1E3',     // Light mint
          },
          'dark-blue': {
            bg: '#1E3A8A',           // Dark blue
            text: '#FFFFFF',         // White
            subtitle: '#DBEAFE',     // Light blue
          },
          'dark-purple': {
            bg: '#5B21B6',           // Dark purple
            text: '#FFFFFF',         // White
            subtitle: '#E9D5FF',     // Light purple
          },
          light: {
            bg: '#D4F1E3',           // Mint green
            text: '#2B5F4C',         // Dark green
            subtitle: '#3D7A5E',     // Medium green
          },
          'light-blue': {
            bg: '#DBEAFE',           // Light blue
            text: '#1E3A8A',         // Dark blue
            subtitle: '#3B82F6',     // Medium blue
          },
          'light-purple': {
            bg: '#E9D5FF',           // Light purple
            text: '#5B21B6',         // Dark purple
            subtitle: '#7C3AED',     // Medium purple
          },
          'light-yellow': {
            bg: '#FEF3C7',           // Light yellow
            text: '#92400E',         // Dark yellow
            subtitle: '#D97706',     // Medium yellow
          },
        },

        // Sidebar Colors
        sidebar: {
          bg: '#2B5F4C',             // Dark green
          text: '#FFFFFF',           // White
          'text-muted': '#D4F1E3',   // Light mint
          active: '#7AC29A',         // Light green
          hover: '#3D7A5E',          // Medium green
          border: '#3D7A5E',         // Medium green
        },
      },

      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },

      borderRadius: {
        lg: '0.5rem',   // 8px
        xl: '0.75rem',  // 12px
        '2xl': '1rem',  // 16px
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}

export default config
```

### CSS Variables Setup (Optional - for shadcn/ui compatibility)

```css
/* app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Brand colors */
    --brand-primary: 43 95 76;           /* #2B5F4C */
    --brand-primary-foreground: 212 241 227;  /* #D4F1E3 */
    --brand-accent: 122 194 154;         /* #7AC29A */

    /* Background */
    --background: 255 255 255;           /* #FFFFFF */
    --background-muted: 249 250 251;     /* #F9FAFB */

    /* Text */
    --text-primary: 17 24 39;            /* #111827 */
    --text-secondary: 107 114 128;       /* #6B7280 */

    /* Border */
    --border: 229 231 235;               /* #E5E7EB */
    --border-focus: 122 194 154;         /* #7AC29A */

    /* shadcn/ui variables */
    --primary: 43 95 76;                 /* Brand primary */
    --primary-foreground: 255 255 255;   /* White */
    --ring: 122 194 154;                 /* Brand accent for focus rings */
  }
}
```

### Benefits of Semantic Tokens

✅ **Single Source of Truth**: All colors defined in one place
✅ **Easy Maintenance**: Update brand colors without touching components
✅ **Type Safety**: Autocomplete for color tokens in VSCode
✅ **Consistency**: All components use the same color palette
✅ **Scalability**: Easy to add dark mode or theme switching

### How to Use Semantic Tokens

**Before (Hardcoded)** ❌:
```tsx
<div className="bg-emerald-800 text-white">
  <p className="text-emerald-300">Subtitle</p>
</div>
```

**After (Semantic)** ✅:
```tsx
<div className="bg-brand-primary text-brand-primary-foreground">
  <p className="text-brand-primary-foreground/70">Subtitle</p>
</div>
```

**Metric Cards** ✅:
```tsx
<div className="bg-metric-dark-bg text-metric-dark-text">
  <p className="text-metric-dark-subtitle">Subtitle</p>
</div>
```

**Status Badges** ✅:
```tsx
<div className="bg-status-normal-bg text-status-normal-text">
  Normal
</div>
```

---

## Components

### 1. Sidebar Navigation

**Appearance**:
- Background: Dark Green (#2B5F4C)
- Width: 200px (expanded), 60px (collapsed)
- Icons: White
- Active state: Light Green (#7AC29A) background
- Hover: Slightly lighter green

**Structure** (Using Semantic Tokens):
```tsx
<aside className="w-[200px] bg-sidebar-bg h-screen flex flex-col">
  {/* Logo */}
  <div className="p-4 flex items-center gap-3">
    <div className="w-10 h-10 bg-brand-secondary rounded-lg flex items-center justify-center">
      {/* Icon */}
    </div>
    <div>
      <h3 className="text-sidebar-text font-semibold">TOKO ANAK BANGSA</h3>
      <p className="text-sidebar-text-muted text-xs">Store Management</p>
    </div>
  </div>

  {/* Navigation Items */}
  <nav className="flex-1 px-2 py-4 space-y-1">
    <a href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sidebar-text hover:bg-sidebar-hover">
      <DashboardIcon />
      <span>Dashboard</span>
    </a>
    <a href="/analytics" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-sidebar-active text-brand-accent-foreground">
      <AnalyticsIcon />
      <span>Analytics</span>
    </a>
    {/* More items... */}
  </nav>

  {/* User Profile */}
  <div className="p-4 border-t border-sidebar-border">
    <div className="flex items-center gap-3">
      <div className="w-10 h-10 bg-brand-secondary rounded-full flex items-center justify-center text-sidebar-text">
        LG
      </div>
      <div>
        <p className="text-sidebar-text text-sm font-medium">Liam Gallagher</p>
        <p className="text-sidebar-text-muted text-xs">System Admin</p>
      </div>
    </div>
  </div>
</aside>
```

---

### 2. Metric Cards

**Custom MetricCard Component with Variants**:

```tsx
// components/metric-card.tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"
import { TrendingUp, TrendingDown } from "lucide-react"

const metricCardVariants = cva(
  "rounded-2xl p-6 transition-all",
  {
    variants: {
      variant: {
        // Dark variants - using semantic tokens
        dark: "bg-metric-dark-bg text-metric-dark-text",
        "dark-blue": "bg-metric-dark-blue-bg text-metric-dark-blue-text",
        "dark-purple": "bg-metric-dark-purple-bg text-metric-dark-purple-text",

        // Light variants - using semantic tokens
        light: "bg-metric-light-bg text-metric-light-text",
        "light-blue": "bg-metric-light-blue-bg text-metric-light-blue-text",
        "light-purple": "bg-metric-light-purple-bg text-metric-light-purple-text",
        "light-yellow": "bg-metric-light-yellow-bg text-metric-light-yellow-text",
      },
    },
    defaultVariants: {
      variant: "dark",
    },
  }
)

export interface MetricCardProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof metricCardVariants> {
  title: string
  value: string | number
  unit?: string
  subtitle?: string
  badge?: {
    label: string
    variant?: "normal" | "high" | "optimal"
  }
  trend?: {
    value: string
    direction: "up" | "down" | "neutral"
  }
}

const MetricCard = React.forwardRef<HTMLDivElement, MetricCardProps>(
  ({ className, variant, title, value, unit, subtitle, badge, trend, ...props }, ref) => {
    const isDark = variant?.includes("dark")

    // Get subtitle color based on variant
    const getSubtitleColor = () => {
      if (variant === "dark") return "text-metric-dark-subtitle"
      if (variant === "dark-blue") return "text-metric-dark-blue-subtitle"
      if (variant === "dark-purple") return "text-metric-dark-purple-subtitle"
      if (variant === "light") return "text-metric-light-subtitle"
      if (variant === "light-blue") return "text-metric-light-blue-subtitle"
      if (variant === "light-purple") return "text-metric-light-purple-subtitle"
      if (variant === "light-yellow") return "text-metric-light-yellow-subtitle"
      return "opacity-70"
    }

    return (
      <div ref={ref} className={cn(metricCardVariants({ variant }), className)} {...props}>
        {/* Header */}
        <div className="flex items-center justify-between mb-2">
          <h3 className={cn(
            "text-sm font-medium",
            isDark ? "text-current/90" : "text-current"
          )}>
            {title}
          </h3>
          {badge && (
            <Badge variant={badge.variant || "normal"}>
              {badge.label}
            </Badge>
          )}
        </div>

        {/* Value */}
        <div className="mb-1">
          <span className="text-3xl font-bold">{value}</span>
          {unit && (
            <span className={cn(
              "text-lg ml-1",
              getSubtitleColor()
            )}>
              {unit}
            </span>
          )}
        </div>

        {/* Footer */}
        <div className="flex items-center justify-between">
          {subtitle && (
            <p className={cn(
              "text-sm",
              getSubtitleColor()
            )}>
              {subtitle}
            </p>
          )}

          {trend && (
            <div className={cn(
              "flex items-center gap-1 text-sm",
              trend.direction === "up" && (isDark ? "text-brand-success/80" : "text-brand-accent"),
              trend.direction === "down" && "text-red-400",
              trend.direction === "neutral" && "text-text-muted"
            )}>
              {trend.direction === "up" && <TrendingUp className="w-4 h-4" />}
              {trend.direction === "down" && <TrendingDown className="w-4 h-4" />}
              <span>{trend.value}</span>
            </div>
          )}
        </div>
      </div>
    )
  }
)
MetricCard.displayName = "MetricCard"

export { MetricCard, metricCardVariants }
```

**Usage Examples**:

```tsx
import { MetricCard } from "@/components/metric-card"

{/* Dark Green Metric */}
<MetricCard
  variant="dark"
  title="Total Sales"
  value="Rp 15,245,600"
  subtitle="Today"
  badge={{ label: "normal", variant: "normal" }}
  trend={{ value: "+5.2%", direction: "up" }}
/>

{/* Light Mint Metric */}
<MetricCard
  variant="light"
  title="Orders"
  value={142}
  subtitle="Total Orders"
  trend={{ value: "+12.8%", direction: "up" }}
/>

{/* Light Blue Metric */}
<MetricCard
  variant="light-blue"
  title="Customers"
  value={89}
  unit="customers"
  subtitle="Active Today"
/>

{/* Dark Blue Metric */}
<MetricCard
  variant="dark-blue"
  title="Revenue"
  value="Rp 1.2M"
  subtitle="This Month"
  badge={{ label: "high", variant: "high" }}
/>
```

---

### 3. Page Header

**Structure** (Using Semantic Tokens):
```tsx
<header className="mb-6">
  <div className="flex items-center justify-between mb-4">
    <div>
      <h1 className="text-2xl font-bold text-text-primary flex items-center gap-2">
        Hello, Liam Gallagher! 👋
      </h1>
      <p className="text-text-secondary text-sm mt-1">
        What are you looking for today?
      </p>
    </div>

    <div className="flex items-center gap-2">
      <div className="px-3 py-1.5 bg-status-active-bg rounded-full flex items-center gap-2">
        <div className="w-2 h-2 bg-brand-accent rounded-full"></div>
        <span className="text-status-active-text text-sm font-medium">
          Real-time monitoring active
        </span>
      </div>
    </div>
  </div>
</header>
```

---

### 4. Filter Section

**Design**: Row of dropdown filters with "Apply Filter" button

```tsx
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Label } from "@/components/ui/label";

<div className="bg-white rounded-xl p-4 mb-6 shadow-sm">
  <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
    <div className="space-y-2">
      <Label>Filter Type</Label>
      <Select defaultValue="individual">
        <SelectTrigger>
          <SelectValue placeholder="Select type" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="individual">Individual Device</SelectItem>
          <SelectItem value="group">Device Group</SelectItem>
        </SelectContent>
      </Select>
    </div>

    <div className="space-y-2">
      <Label>Select Device</Label>
      <Select defaultValue="main-floor1">
        <SelectTrigger>
          <SelectValue placeholder="Select device" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="main-floor1">Main Building - Floor 1</SelectItem>
          <SelectItem value="main-floor2">Main Building - Floor 2</SelectItem>
        </SelectContent>
      </Select>
    </div>

    <div className="space-y-2">
      <Label>Data Mode</Label>
      <Select defaultValue="realtime">
        <SelectTrigger>
          <SelectValue placeholder="Select mode" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="realtime">Real-Time</SelectItem>
          <SelectItem value="historical">Historical</SelectItem>
        </SelectContent>
      </Select>
    </div>

    <div className="space-y-2">
      <Label>Time Period</Label>
      <div className="flex gap-2">
        <Select defaultValue="today">
          <SelectTrigger className="flex-1">
            <SelectValue placeholder="Select period" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="today">Today</SelectItem>
            <SelectItem value="week">This Week</SelectItem>
            <SelectItem value="month">This Month</SelectItem>
          </SelectContent>
        </Select>
        <Button variant="brand">
          Apply Filter
        </Button>
      </div>
    </div>
  </div>
</div>
```

---

### 5. Content Cards

**Design**: White background, subtle shadow, rounded corners (Using Semantic Tokens)

```tsx
<div className="bg-background rounded-xl p-6 shadow-sm">
  <div className="flex items-center justify-between mb-4">
    <div>
      <h2 className="text-lg font-semibold text-text-primary">
        Energy Consumption Overview
      </h2>
      <p className="text-sm text-text-secondary mt-1">
        Distribution of energy consumption across all live devices for today
      </p>
    </div>

    <button className="px-3 py-1.5 text-sm text-text-secondary hover:bg-background-subtle rounded-lg transition-colors">
      Export
    </button>
  </div>

  {/* Card Content */}
  <div className="space-y-4">
    {/* Charts, tables, etc. */}
  </div>
</div>
```

---

### 6. Badges

**Custom Badge Variants Configuration**:

```tsx
// components/ui/badge.tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-xs font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default: "bg-background-subtle text-text-primary hover:bg-border",

        // TOKO ANAK BANGSA status variants - using semantic tokens
        normal: "bg-status-normal-bg text-status-normal-text",
        high: "bg-status-high-bg text-status-high-text",
        optimal: "bg-status-optimal-bg text-status-optimal-text",
        active: "bg-status-active-bg text-status-active-text",

        // Standard variants - using semantic tokens
        success: "bg-status-success-bg text-status-success-text",
        warning: "bg-status-warning-bg text-status-warning-text",
        error: "bg-status-error-bg text-status-error-text",
        info: "bg-status-optimal-bg text-status-optimal-text",

        // Outline variants
        outline: "border border-border text-text-secondary",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />
}

export { Badge, badgeVariants }
```

**Usage Examples**:

```tsx
import { Badge } from "@/components/ui/badge";

{/* Normal Status */}
<Badge variant="normal">normal</Badge>

{/* High Status */}
<Badge variant="high">high</Badge>

{/* Optimal Status */}
<Badge variant="optimal">optimal</Badge>

{/* Active with Indicator */}
<Badge variant="active">
  <div className="w-1.5 h-1.5 bg-brand-accent rounded-full"></div>
  Active
</Badge>

{/* Success */}
<Badge variant="success">Completed</Badge>

{/* Warning */}
<Badge variant="warning">Pending</Badge>

{/* Error */}
<Badge variant="error">Failed</Badge>
```

---

### 7. Buttons

**Custom Button Variants Configuration**:

First, extend the Button component with TOKO ANAK BANGSA brand variants:

```tsx
// components/ui/button.tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-lg text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-border-focus disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        // TOKO ANAK BANGSA Primary (Brand Green) - using semantic tokens
        default: "bg-brand-primary text-text-inverse hover:bg-brand-primary-hover",

        // Brand variants - using semantic tokens
        brand: "bg-brand-secondary text-brand-secondary-foreground hover:bg-brand-secondary-hover",
        "brand-light": "bg-brand-accent text-brand-accent-foreground hover:bg-brand-accent-hover",

        // Standard variants - using semantic tokens
        destructive: "bg-status-error-text text-text-inverse hover:bg-status-error-text/90",
        outline: "border border-border bg-background hover:bg-background-subtle hover:text-text-primary",
        secondary: "bg-background-subtle text-text-primary hover:bg-border",
        ghost: "hover:bg-background-subtle hover:text-text-primary",
        link: "text-brand-secondary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 px-3",
        lg: "h-11 px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
```

**Usage Examples**:

```tsx
import { Button } from "@/components/ui/button";
import { Download, Plus, Trash2 } from "lucide-react";
```

**Primary Brand Button** (Dark Green):
```tsx
<Button variant="default">
  Apply Filter
</Button>
```

**Brand Button** (Medium Green):
```tsx
<Button variant="brand">
  <Plus className="w-4 h-4" />
  Add Product
</Button>
```

**Brand Light Button** (Light Green):
```tsx
<Button variant="brand-light">
  Save Draft
</Button>
```

**Secondary Button**:
```tsx
<Button variant="outline">
  Cancel
</Button>
```

**Destructive Button**:
```tsx
<Button variant="destructive">
  <Trash2 className="w-4 h-4" />
  Delete
</Button>
```

**Icon Button**:
```tsx
<Button variant="ghost" size="icon">
  <Download className="w-5 h-5" />
</Button>
```

**Small Button**:
```tsx
<Button variant="brand" size="sm">
  Quick Action
</Button>
```

**Large Button**:
```tsx
<Button variant="brand" size="lg">
  Complete Checkout
</Button>
```

---

### 8. Forms

**Using shadcn/ui Form with Zod Validation and React Hook Form**:

First, install required dependencies:
```bash
pnpm add react-hook-form @hookform/resolvers zod
```

**Complete Form Example**:

```tsx
"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import * as z from "zod"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

// Define Zod schema
const productFormSchema = z.object({
  name: z.string().min(3, {
    message: "Product name must be at least 3 characters.",
  }),
  category: z.string({
    required_error: "Please select a category.",
  }),
  description: z.string().min(10, {
    message: "Description must be at least 10 characters.",
  }).optional(),
  priceA: z.coerce.number().min(0, {
    message: "Price must be a positive number.",
  }),
  priceB: z.coerce.number().min(0, {
    message: "Price must be a positive number.",
  }),
  priceC: z.coerce.number().min(0, {
    message: "Price must be a positive number.",
  }),
  stock: z.coerce.number().int().min(0, {
    message: "Stock must be a positive integer.",
  }),
})

type ProductFormValues = z.infer<typeof productFormSchema>

export function ProductForm() {
  // Initialize form with React Hook Form + Zod
  const form = useForm<ProductFormValues>({
    resolver: zodResolver(productFormSchema),
    defaultValues: {
      name: "",
      category: "",
      description: "",
      priceA: 0,
      priceB: 0,
      priceC: 0,
      stock: 0,
    },
  })

  // Form submit handler
  function onSubmit(data: ProductFormValues) {
    console.log(data)
    // Handle form submission (API call, etc.)
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        {/* Text Input */}
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Product Name *</FormLabel>
              <FormControl>
                <Input placeholder="Enter product name" {...field} />
              </FormControl>
              <FormDescription>
                This name will be visible to customers
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Select Dropdown */}
        <FormField
          control={form.control}
          name="category"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Category *</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select category" />
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  <SelectItem value="food">Food & Beverages</SelectItem>
                  <SelectItem value="sembako">Sembako</SelectItem>
                  <SelectItem value="household">Household Items</SelectItem>
                </SelectContent>
              </Select>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Textarea */}
        <FormField
          control={form.control}
          name="description"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Description</FormLabel>
              <FormControl>
                <Textarea
                  placeholder="Enter product description"
                  rows={4}
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Number Input Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <FormField
            control={form.control}
            name="priceA"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Price A (Wholesale) *</FormLabel>
                <FormControl>
                  <Input type="number" placeholder="0" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="priceB"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Price B (Retail) *</FormLabel>
                <FormControl>
                  <Input type="number" placeholder="0" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="priceC"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Price C (Member) *</FormLabel>
                <FormControl>
                  <Input type="number" placeholder="0" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
        </div>

        {/* Submit Buttons */}
        <div className="flex gap-3">
          <Button type="submit" variant="brand">
            Save Product
          </Button>
          <Button type="button" variant="outline" onClick={() => form.reset()}>
            Reset
          </Button>
        </div>
      </form>
    </Form>
  )
}
```

**Reusable Form Schema Patterns**:

```tsx
// lib/validations/product.ts
import * as z from "zod"

export const productSchema = z.object({
  name: z.string().min(3).max(100),
  categoryId: z.string(),
  description: z.string().min(10).optional(),

  // Multi-tier pricing
  pricing: z.object({
    cost: z.coerce.number().min(0),
    priceA: z.coerce.number().min(0),
    priceB: z.coerce.number().min(0),
    priceC: z.coerce.number().min(0),
  }),

  // Unit packages
  units: z.object({
    dusToPack: z.coerce.number().int().min(1).default(1),
    packToPcs: z.coerce.number().int().min(1).default(1),
  }),

  // Inventory
  stock: z.coerce.number().int().min(0),

  // Shipping (conditional)
  shipping: z.object({
    weight: z.coerce.number().min(0).optional(),
    dimensions: z.object({
      width: z.coerce.number().min(0).optional(),
      length: z.coerce.number().min(0).optional(),
      height: z.coerce.number().min(0).optional(),
    }).optional(),
  }).optional(),
})

export type ProductFormValues = z.infer<typeof productSchema>
```

**Customer Address Form Example**:

```tsx
// lib/validations/address.ts
import * as z from "zod"

export const addressSchema = z.object({
  label: z.enum(["home", "office", "other"]),
  recipientName: z.string().min(3),
  phone: z.string().regex(/^\+62\d{9,12}$/, "Invalid phone number"),
  addressLine1: z.string().min(10),
  addressLine2: z.string().optional(),
  city: z.string(),
  cityId: z.number().int(),
  province: z.string(),
  postalCode: z.string().regex(/^\d{5}$/, "Invalid postal code"),
  isPrimary: z.boolean().default(false),
})
```

**Form Validation Best Practices**:

1. **Always use Zod schemas** for type-safe validation
2. **Use `z.coerce.number()`** for number inputs to handle string-to-number conversion
3. **Provide clear error messages** in the schema
4. **Use FormDescription** for helpful hints
5. **Use FormMessage** to display validation errors
6. **Group related fields** (e.g., pricing, dimensions)
7. **Use conditional validation** for optional sections

---

### 9. Tables

**Design**: Clean, alternating rows, hover states (Using Semantic Tokens)

```tsx
<div className="overflow-x-auto">
  <table className="w-full">
    <thead>
      <tr className="border-b border-border">
        <th className="px-4 py-3 text-left text-sm font-medium text-text-secondary">
          Product Name
        </th>
        <th className="px-4 py-3 text-left text-sm font-medium text-text-secondary">
          Category
        </th>
        <th className="px-4 py-3 text-right text-sm font-medium text-text-secondary">
          Price
        </th>
        <th className="px-4 py-3 text-right text-sm font-medium text-text-secondary">
          Stock
        </th>
      </tr>
    </thead>
    <tbody>
      <tr className="border-b border-border-muted hover:bg-background-subtle transition-colors">
        <td className="px-4 py-3 text-sm text-text-primary">Indomie Goreng</td>
        <td className="px-4 py-3 text-sm text-text-secondary">Instant Noodles</td>
        <td className="px-4 py-3 text-sm text-text-primary text-right">Rp 3,000</td>
        <td className="px-4 py-3 text-sm text-text-primary text-right">250 PCS</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

### 10. Charts

**Design**: Clean, colored, with legends (Using Semantic Tokens)

Use **Chart.js** or **Recharts** for visualizations.

**Note**: For charts, we use the actual hex color values from our theme since Recharts doesn't support Tailwind classes directly. Reference the theme configuration for these values.

```tsx
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend } from 'recharts';

// Import theme colors from your Tailwind config or define them
const CHART_COLORS = {
  textSecondary: '#6B7280',   // text-text-secondary
  brandAccent: '#7AC29A',     // brand-accent
  error: '#991B1B',           // status-error-text
}

<LineChart width={800} height={300} data={data}>
  <XAxis dataKey="time" stroke={CHART_COLORS.textSecondary} />
  <YAxis stroke={CHART_COLORS.textSecondary} />
  <Tooltip />
  <Legend />
  <Line
    type="monotone"
    dataKey="actual"
    stroke={CHART_COLORS.brandAccent}
    strokeWidth={2}
    dot={{ fill: CHART_COLORS.brandAccent, r: 3 }}
  />
  <Line
    type="monotone"
    dataKey="max"
    stroke={CHART_COLORS.error}
    strokeWidth={2}
    strokeDasharray="5 5"
  />
</LineChart>
```

**Pro Tip**: Create a `chart-colors.ts` file that exports your theme colors for use in chart libraries:

```typescript
// lib/chart-colors.ts
export const CHART_COLORS = {
  // Brand colors
  brandPrimary: '#2B5F4C',
  brandSecondary: '#3D7A5E',
  brandAccent: '#7AC29A',
  brandSuccess: '#D4F1E3',

  // Text colors
  textPrimary: '#111827',
  textSecondary: '#6B7280',
  textMuted: '#9CA3AF',

  // Status colors
  statusSuccess: '#065F46',
  statusWarning: '#92400E',
  statusError: '#991B1B',
  statusInfo: '#1E3A8A',

  // Background colors
  background: '#FFFFFF',
  backgroundMuted: '#F9FAFB',
  border: '#E5E7EB',
} as const
```

---

## Spacing System

**Consistent spacing using Tailwind scale**:

```css
0: 0px
1: 0.25rem (4px)
2: 0.5rem (8px)
3: 0.75rem (12px)
4: 1rem (16px)
5: 1.25rem (20px)
6: 1.5rem (24px)
8: 2rem (32px)
10: 2.5rem (40px)
12: 3rem (48px)
16: 4rem (64px)
```

**Component Spacing**:
- Card padding: `p-6` (24px)
- Section gap: `mb-6` (24px)
- Grid gap: `gap-4` (16px)
- Button padding: `px-4 py-2` (16px/8px)

---

## Border Radius

```css
rounded-sm: 0.125rem (2px)
rounded: 0.25rem (4px)
rounded-md: 0.375rem (6px)
rounded-lg: 0.5rem (8px)
rounded-xl: 0.75rem (12px)
rounded-2xl: 1rem (16px)
rounded-full: 9999px
```

**Usage**:
- Metric cards: `rounded-2xl`
- Content cards: `rounded-xl`
- Buttons: `rounded-lg`
- Inputs: `rounded-lg`
- Badges: `rounded-full`

---

## Shadows

```css
shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05)
shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1)
shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1)
shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1)
```

**Usage**:
- Cards: `shadow-sm`
- Dropdowns: `shadow-md`
- Modals: `shadow-lg`

---

## Responsive Breakpoints

```css
sm: 640px   /* Mobile landscape */
md: 768px   /* Tablet */
lg: 1024px  /* Desktop */
xl: 1280px  /* Large desktop */
2xl: 1536px /* Extra large */
```

---

## Icons

**Library**: Lucide React (or Heroicons)

**Sizes**:
- Small: `w-4 h-4` (16px)
- Medium: `w-5 h-5` (20px)
- Large: `w-6 h-6` (24px)

```tsx
import { TrendingUp, Download, Settings } from 'lucide-react';

{/* Using semantic token */}
<TrendingUp className="w-5 h-5 text-brand-accent" />

{/* Secondary icon */}
<Download className="w-5 h-5 text-text-secondary" />

{/* Icon in button */}
<Button variant="brand">
  <Settings className="w-4 h-4" />
  Settings
</Button>
```

---

## Animations

**Transitions**:
```css
transition-colors duration-200
transition-all duration-300
```

**Hover States**:
- Buttons: Scale slightly + color change
- Cards: Subtle elevation
- Links: Color change

---

## Accessibility

**Focus States** (Using Semantic Tokens):
```css
focus:ring-2 focus:ring-border-focus focus:ring-offset-2
focus:outline-none
```

**Focus Example**:
```tsx
<button className="px-4 py-2 bg-brand-primary text-text-inverse rounded-lg focus:outline-none focus:ring-2 focus:ring-border-focus focus:ring-offset-2">
  Click me
</button>
```

**Color Contrast**:
- ✅ Minimum 4.5:1 for normal text
- ✅ Minimum 3:1 for large text
- ✅ Dark green sidebar (`bg-sidebar-bg`) with white text (`text-sidebar-text`) = High contrast
- ✅ Primary text (`text-text-primary`) on white background = High contrast
- ✅ All semantic tokens tested for WCAG AA compliance

**Keyboard Navigation**:
- ✅ All interactive elements focusable
- ✅ Clear focus indicators using `focus:ring-border-focus`
- ✅ Logical tab order
- ✅ Skip links for screen readers

---

## Variant-Based Component Pattern

**TOKO ANAK BANGSA** uses a **variant-based** approach for all components. This means:

✅ **DO**: Use component variants
```tsx
<Button variant="brand">Save</Button>
<Badge variant="success">Active</Badge>
<MetricCard variant="dark" />
```

❌ **DON'T**: Manually add className overrides
```tsx
<Button className="bg-emerald-600 hover:bg-emerald-700">Save</Button>
```

**Benefits**:
1. **Consistency**: All components follow the same pattern
2. **Type Safety**: TypeScript ensures only valid variants are used
3. **Maintainability**: Update colors in one place
4. **Reusability**: Easy to apply brand styles
5. **Intellisense**: IDE autocomplete for variants

---

## Component Library Setup

### Install shadcn/ui

```bash
npx shadcn-ui@latest init
```

### Install Required Components

```bash
# Core components
npx shadcn-ui@latest add button
npx shadcn-ui@latest add input
npx shadcn-ui@latest add label
npx shadcn-ui@latest add select
npx shadcn-ui@latest add textarea
npx shadcn-ui@latest add form
npx shadcn-ui@latest add badge
npx shadcn-ui@latest add card
npx shadcn-ui@latest add table
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add popover
npx shadcn-ui@latest add toast
npx shadcn-ui@latest add tabs
```

### Install Additional Dependencies

```bash
# Form handling
pnpm add react-hook-form @hookform/resolvers zod

# Charts
pnpm add recharts

# Icons
pnpm add lucide-react

# Class variance authority (for variants)
pnpm add class-variance-authority clsx tailwind-merge
```

### shadcn/ui Configuration

```json
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css"
  },
  "rsc": true,
  "tsx": true,
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

**Note**: The complete Tailwind theme configuration is defined at the beginning of this document in the [Tailwind Theme Configuration](#tailwind-theme-configuration) section.

---

## Example: Dashboard Page

**Complete Dashboard with Semantic Tokens**:

```tsx
// app/dashboard/page.tsx
'use client';

import { TrendingUp, TrendingDown } from 'lucide-react';
import { MetricCard } from '@/components/metric-card';
import { Sidebar } from '@/components/sidebar';
import { FilterSection } from '@/components/filter-section';
import { SalesChart } from '@/components/sales-chart';
import { TopProducts } from '@/components/top-products';

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-background-muted">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <main className="ml-[200px] p-6">
        {/* Header */}
        <header className="mb-6">
          <h1 className="text-2xl font-bold text-text-primary flex items-center gap-2">
            Hello, Budi Santoso! 👋
          </h1>
          <p className="text-sm text-text-secondary mt-1">
            What are you looking for today?
          </p>
        </header>

        {/* Filters */}
        <FilterSection />

        {/* Metric Cards - Using Semantic Tokens */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <MetricCard
            variant="dark"
            title="Total Sales"
            value="Rp 15,245,600"
            subtitle="Today"
            badge={{ label: "normal", variant: "normal" }}
            trend={{ value: "+5.2%", direction: "up" }}
          />

          <MetricCard
            variant="light"
            title="Orders"
            value={142}
            subtitle="Total Orders"
            trend={{ value: "+12.8%", direction: "up" }}
          />

          <MetricCard
            variant="light-blue"
            title="Customers"
            value={89}
            subtitle="Active Customers"
            trend={{ value: "-2.1%", direction: "down" }}
          />

          <MetricCard
            variant="dark-blue"
            title="Products"
            value={523}
            subtitle="In Stock"
            badge={{ label: "optimal", variant: "optimal" }}
          />
        </div>

        {/* Charts Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <SalesChart />
          <TopProducts />
        </div>
      </main>
    </div>
  );
}
```

---

## Summary

**TOKO ANAK BANGSA Design System**:
- ✅ **Semantic Theme Tokens**: All colors defined in `tailwind.config.ts` with semantic naming
- ✅ **No Hardcoded Colors**: Components use `bg-brand-primary`, `text-text-secondary`, etc. instead of `bg-emerald-800`
- ✅ **Variant-Based Components**: All components use Class Variance Authority (cva) for type-safe variants
- ✅ **Dark Green Brand** (`#2B5F4C`): Professional, modern color palette
- ✅ **Clean Layout**: Sidebar navigation with metric cards
- ✅ **Professional Typography**: Inter font family
- ✅ **Data-Focused**: Optimized for business metrics and analytics
- ✅ **Accessible**: WCAG AA compliant with proper focus states
- ✅ **Responsive**: Mobile-first design with Tailwind breakpoints
- ✅ **Type-Safe**: Zod validation + React Hook Form + shadcn/ui components
- ✅ **Built with**: shadcn/ui + Tailwind CSS + Class Variance Authority

**Key Files**:
- `tailwind.config.ts`: Complete theme configuration with semantic tokens
- `app/globals.css`: CSS variables for shadcn/ui compatibility
- `lib/chart-colors.ts`: Theme colors for chart libraries
- `components/ui/*`: shadcn/ui components with brand customization
- `components/metric-card.tsx`: Custom MetricCard component

**Reference Images**: `docs/ui-sample/dashboard.png`, `docs/ui-sample/analytics.png`

**Design Principles**:
1. **Consistency**: Use semantic tokens everywhere
2. **Maintainability**: Change colors in one place (theme config)
3. **Type Safety**: Variants provide autocomplete and type checking
4. **Scalability**: Easy to add dark mode or additional themes
5. **Developer Experience**: Clear, predictable naming conventions

---

**Last Updated**: 2024-12-13
