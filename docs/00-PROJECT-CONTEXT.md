# TOKO ANAK BANGSA - Project Context

**Product Name**: TOKO ANAK BANGSA
**Version**: 1.0.0
**Last Updated**: 2024-12-13
**Status**: Planning Phase

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Vision & Mission](#vision--mission)
3. [Business Model](#business-model)
4. [Target Users](#target-users)
5. [Tech Stack](#tech-stack)
6. [Architecture](#architecture)
7. [Core Features](#core-features)
8. [Success Metrics](#success-metrics)
9. [Development Phases](#development-phases)

---

## Project Overview

**TOKO ANAK BANGSA** is a multi-tenant SaaS platform designed for Indonesian SMEs to:
- Create and manage their own online stores
- Sell products with multi-tier pricing (wholesale, retail, member)
- Manage inventory with multiple unit packages (DUS, PACK, PCS)
- Handle purchasing and supplier relationships
- Manage financial operations (accounts payable & receivable)
- Reach customers through a unified marketplace

This is **NOT just e-commerce** - it's a **complete business management system** (ERP-lite) tailored for Indonesian retail and wholesale businesses.

---

## Vision & Mission

### Vision
To become the #1 platform for Indonesian SMEs to digitize their wholesale and retail operations, enabling them to compete in the modern digital economy.

### Mission
- **Empower SMEs**: Provide enterprise-grade tools at affordable prices
- **Simplify Operations**: Consolidate store management, inventory, and finances in one platform
- **Enable Growth**: Help businesses scale from traditional to digital operations
- **Local Focus**: Built specifically for Indonesian market needs (DUS/PACK/PCS, tempo/kredit, RajaOngkir, Midtrans)

---

## Business Model

### Two-Sided Marketplace (B2B2C)

**Supply Side (Store Owners)**
- Target: Traditional retailers, wholesalers, distributors
- Value Prop: "Launch your online store in 5 minutes, manage everything from one dashboard"
- Pain Points Solved:
  - Expensive/complex platforms (Shopify too expensive)
  - Manual processes (Excel spreadsheets, paper books)
  - No proper multi-tier pricing support
  - No integrated hutang/piutang management

**Demand Side (Customers)**
- Target: Wholesale buyers, retail consumers, resellers
- Value Prop: "Discover and buy from local stores, unified mobile experience"
- Pain Points Solved:
  - Generic marketplaces (Shopee/Tokopedia) overwhelming
  - Want to support local businesses
  - Need wholesale pricing options

### Revenue Model (Freemium + Transaction Fee)

**Free Tier**:
- Up to 50 products
- Unlimited orders
- 2.5% + Rp 2,000 per transaction
- Basic features

**Pro Tier (Rp 99,000/month)**:
- Unlimited products
- Custom domain
- 1.5% + Rp 1,500 per transaction
- Advanced analytics
- Multi-user access (RBAC)
- Hutang/Piutang management

**Enterprise (Custom pricing)**:
- Multi-store
- API access
- Dedicated support
- White-label option

---

## Target Users

### Primary Users

**1. Store Owners (Supply Side)**
- **Profile**: Traditional retailers, toko kelontong, grosir, distributors
- **Size**: 1-50 employees, Rp 10M - 500M annual revenue
- **Current Tools**: Excel, paper books, WhatsApp for orders
- **Goals**: Digitize operations, expand customer reach, better financial management
- **Key Needs**: Multi-tier pricing, hutang/piutang tracking, inventory management

**2. Wholesale Customers (Demand Side - Type A)**
- **Profile**: Resellers, sub-distributors, large buyers
- **Behavior**: Buy in bulk (DUS/PACK), negotiate pricing, credit terms
- **Key Needs**: Wholesale prices, credit facilities, bulk ordering

**3. Retail Customers (Demand Side - Type B)**
- **Profile**: End consumers, small buyers
- **Behavior**: Buy in smaller quantities (PACK/PCS), immediate payment
- **Key Needs**: Retail prices, easy checkout, product discovery

### Secondary Users

**4. Store Staff (Multi-user RBAC)**
- **Roles**: Owner, Manager, Admin, Staff, Viewer
- **Key Needs**: Role-based permissions, order processing, inventory updates

**5. Platform Administrators (Internal)**
- **Key Needs**: Tenant management, analytics, content moderation

---

## Tech Stack

### Frontend

**Web Apps (Next.js 16)**:
- **Store Portal**: Store owner dashboard (`apps/store-portal/`)
- **Marketplace**: Customer-facing marketplace (`apps/marketplace/`)
- **Company Profile**: Marketing site (`apps/company-profile/`)
- **Platform Admin**: Internal admin (`apps/platform-admin/`)

**UI Libraries**:
- **shadcn/ui**: Web components
- **TanStack Table**: Data tables
- **TanStack Query**: Data fetching & caching
- **Zustand**: State management

### Backend

**Firebase Ecosystem**:
- **Firestore**: NoSQL database (multi-tenant)
- **Firebase Auth**: User authentication
- **Firebase Storage**: File storage (product images)
- **Firebase RTDB**: Real-time features (cart, inventory)
- **Cloud Functions**: Serverless backend (Node.js triggers)
- **Firebase App Hosting**: Next.js hosting

**API Layer**:
- **FastAPI (Python)**: REST API (optional, for complex logic)
- **Cloud Run**: API hosting (if using FastAPI)

### Integrations

- **Midtrans**: Payment gateway (Indonesia)
- **RajaOngkir**: Shipping cost calculator (Indonesia)
- **SendGrid/Mailgun**: Email (via Firebase Extensions)
- **Twilio**: SMS notifications (via Firebase Extensions)

### DevOps

- **Monorepo**: Turborepo + pnpm workspaces
- **CI/CD**: GitHub Actions
- **Hosting**: Firebase App Hosting
- **Region**: asia-southeast1 (Jakarta, Indonesia)

---

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    WEB APPLICATIONS                      │
│  (Next.js on Firebase App Hosting)                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Store Portal  │  Marketplace  │  Company  │  Admin     │
│  (Owner App)   │  (Customer)   │  Profile  │  (Internal)│
│                                                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│              FIREBASE BACKEND SERVICES                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Firestore  │  Auth  │  Storage  │  RTDB  │  Functions │
│  (Database) │  (JWT) │  (Images) │  (RT)  │  (Lambda)  │
│                                                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│            EXTERNAL INTEGRATIONS                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Midtrans  │  RajaOngkir  │  Email  │  SMS             │
│  (Payment) │  (Shipping)  │  (SMTP) │  (Twilio)        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Multi-Tenant Data Model

**Firestore Collections**:
```
firestore/
├── tenants/                     # Stores (multi-tenant root)
│   └── {tenantId}/
│       ├── members/            # RBAC (owner, manager, staff, etc.)
│       ├── products/           # Products with multi-tier pricing
│       ├── orders/             # Orders
│       ├── customers/          # Store-specific customers
│       ├── suppliers/          # Supplier management
│       ├── purchase_orders/    # Purchasing
│       ├── accounts_payable/   # AP - Store debt to suppliers
│       └── accounts_receivable/ # AR - Customer debt to store
│
├── users/                       # Global user profiles
├── products_public/             # Marketplace view (denormalized)
├── orders_global/               # Customer's cross-store orders
└── categories/                  # Global product categories
```

**Security**: Firebase Security Rules (row-level security equivalent)

**See**: `docs/architecture/` for detailed architecture documentation

---

## Core Features

### Phase 1: MVP (Web-First) - 8-10 weeks

**Must-Have Features**:

1. **Authentication & Multi-Tenancy**
   - Store owner registration
   - Customer registration
   - Multi-tenant store creation
   - Firebase Auth integration

2. **Product Management** ⭐
   - Multi-tier pricing (Price A, B, C)
   - Unit packages (DUS, PACK, PCS with conversion)
   - Cost tracking & margin calculation
   - Product CRUD operations
   - Image upload
   - Categories

3. **Marketplace**
   - Store discovery
   - Product browsing
   - Product search (basic)
   - Responsive web (mobile-friendly)

4. **Shopping & Checkout**
   - Shopping cart
   - Checkout flow
   - Midtrans payment integration
   - RajaOngkir shipping calculation
   - Multiple payment methods

5. **Order Management**
   - Order processing (store owner)
   - Order tracking (customer)
   - Order status workflow
   - Invoice generation

6. **Basic Analytics**
   - Sales dashboard
   - Revenue reports
   - Product performance

### Phase 1.5: Financial Management - 4-6 weeks

7. **Purchasing Management**
   - Supplier management
   - Purchase orders
   - Goods receiving
   - Cost tracking

8. **Accounts Payable (AP)**
   - Auto-create from purchase orders
   - Supplier payment tracking
   - Aging reports
   - Payment reminders

### Phase 2: Complete ERP - 4-6 weeks

9. **Accounts Receivable (AR)**
   - Customer credit management
   - Credit sales
   - Collection tracking
   - Payment reminders

10. **Advanced Features**
    - Multi-user RBAC
    - Advanced analytics
    - Financial reports
    - Cash flow management

### Phase 3: Mobile App - 2-3 months

11. **Mobile App (React Native Expo)**
    - Native iOS & Android
    - All marketplace features
    - Push notifications
    - Offline support

**See**: `docs/features/` for detailed feature specifications

---

## Success Metrics

### Launch Criteria (Phase 1)
- ✅ 10 pilot stores onboarded
- ✅ 100+ products listed
- ✅ 50+ transactions completed
- ✅ Payment & shipping working
- ✅ Positive feedback from stores

### 3-Month Goals
- 100 active stores
- 500+ products
- Rp 100M GMV (Gross Merchandise Value)
- 70% month-over-month growth
- 10+ paying Pro subscribers

### 6-Month Goals
- 500 active stores
- 5,000+ products
- Rp 1B GMV
- 50+ paying Pro subscribers
- Mobile app launched

### Key Metrics to Track
- **GMV**: Total transaction value
- **Active Stores**: Stores with >1 order/month
- **Conversion Rate**: Visitor → Purchase
- **Retention**: Store owner retention rate
- **ARPU**: Average revenue per store
- **CAC**: Customer acquisition cost
- **LTV**: Lifetime value per store

---

## Development Phases

### Phase 1: Web Platform (MVP) - 8-10 weeks
**Goal**: Launch functional web marketplace

**Sprint Breakdown**:
- Sprint 0 (2 weeks): Infrastructure setup, Firebase, monorepo
- Sprint 1 (2 weeks): Auth & Store creation
- Sprint 2 (3 weeks): Product management with multi-tier pricing
- Sprint 3 (2 weeks): Marketplace browsing
- Sprint 4 (2 weeks): Cart & Checkout
- Sprint 5 (2 weeks): Payment & Shipping integration
- Sprint 6 (2 weeks): Order management
- Sprint 7 (2 weeks): Polish & Beta launch

**Deliverable**: Web platform (responsive, mobile-friendly)

### Phase 1.5: Purchasing & AP - 4-6 weeks
**Goal**: Add supplier management and accounts payable

**Deliverable**: Complete purchasing workflow with AP tracking

### Phase 2: AR & Financial Reports - 4-6 weeks
**Goal**: Complete financial cycle with accounts receivable

**Deliverable**: Full ERP-lite system with financial management

### Phase 3: Mobile App - 2-3 months
**Goal**: Launch native mobile app

**Deliverable**: iOS and Android apps on stores

---

## Project Structure

```
pos-app-v1/
├── apps/
│   ├── store-portal/           # Next.js (Store Owner)
│   ├── marketplace/            # Next.js (Customer)
│   ├── company-profile/        # Next.js (Marketing)
│   └── platform-admin/         # Next.js (Admin)
│
├── packages/
│   ├── firebase-client/        # Shared Firebase SDK
│   ├── shared-types/           # Zod schemas & types
│   └── ui-web/                 # shadcn components
│
├── functions/                  # Cloud Functions (Node.js)
├── firebase/                   # Firebase config & rules
│
├── docs/                       # 📚 Documentation (you are here)
│   ├── 00-PROJECT-CONTEXT.md   # This file
│   ├── architecture/           # Architecture docs
│   ├── features/               # Feature specifications
│   ├── sprint/                 # Sprint planning
│   └── development/            # Dev guides
│
├── scripts/                    # Utility scripts
│   └── create-story.js         # BMAD story creation
│
├── apphosting.*.yaml           # Firebase App Hosting configs
├── firebase.json               # Firebase configuration
├── turbo.json                  # Turborepo config
└── pnpm-workspace.yaml         # pnpm monorepo
```

---

## Competitive Advantage

**Why This Will Win**:

1. ✅ **Indonesian Market Fit**: DUS/PACK/PCS, tempo/kredit, RajaOngkir, Midtrans
2. ✅ **Multi-tier Pricing**: Wholesale + Retail + Member pricing (Shopee/Tokopedia don't have this)
3. ✅ **Financial Management**: AP/AR tracking (Shopify doesn't have this)
4. ✅ **All-in-One**: Store + Marketplace + ERP in one platform
5. ✅ **Affordable**: 1/10th the cost of Shopify
6. ✅ **Local**: Built by Indonesians, for Indonesians

---

## Next Steps

1. ✅ **Complete Documentation** (in progress)
2. ⏳ **Sprint 0: Infrastructure Setup**
   - Firebase project creation
   - Monorepo scaffolding
   - CI/CD pipeline
3. ⏳ **Sprint 1: Begin Development**
   - Auth implementation
   - Store creation flow

---

## References

- [Architecture Documentation](./architecture/)
- [Feature Specifications](./features/)
- [Sprint Planning](./sprint/)
- [Development Guides](./development/)

---

**Document Maintained By**: Development Team
**Last Review**: 2024-12-13
