# TOKO ANAK BANGSA - Documentation

Welcome to **TOKO ANAK BANGSA** documentation! This is your complete guide to understanding, building, and deploying the platform.

**Product Name**: TOKO ANAK BANGSA
**Type**: Multi-Tenant POS & Marketplace Platform
**Market**: Indonesia

---

## 📚 Documentation Index

### 🎯 Start Here

1. **[Project Context](./00-PROJECT-CONTEXT.md)** ⭐ **READ FIRST**
   - Complete project overview
   - Vision, mission, and goals
   - Business model and target users
   - Tech stack and architecture
   - Success metrics and phases

### 🏗️ Architecture

2. **[Architecture Overview](./architecture/README.md)**
   - System architecture
   - Firebase ecosystem
   - Multi-tenant data model
   - Security and scalability

3. **[Modular Architecture Guide](./architecture/modular-architecture.md)** ⭐ **IMPORTANT**
   - Service layer pattern
   - Component-based design
   - Dependency injection
   - Testing modular services
   - Clean code practices

### 🎨 Design

**[UI Design System](./design/ui-design-system.md)** ⭐ **DESIGN REFERENCE**
   - Color palette (Dark Green primary)
   - Typography (Inter font)
   - Component library (shadcn/ui)
   - Layout patterns
   - Responsive design
   - Based on: `docs/ui-sample/`

### ✨ Features

4. **[MVP Features](./features/01-MVP-WEB-FEATURES.md)**
   - Phase 1 must-have features
   - MoSCoW prioritization
   - Detailed feature specifications

5. **Feature Specifications**:
   - **[POS Cashier - In-Store Transactions](./features/pos-cashier/pos-cashier-transactions.md)** ⭐ **NEW** - Cash, EDC, QRIS, Transfer payments
   - **[Shipping Configuration](./features/store-management/shipping-configuration.md)** - Enable/disable shipping, pick-up only stores
   - **[Multi-Language Support (i18n)](./features/i18n-multi-language.md)** - Indonesian & English
   - More feature docs in `features/` folder...

### 🏃 Sprint Planning

6. **[Sprint 0: Infrastructure Setup](./sprint/sprint-00-infrastructure-setup.md)** ⭐ **START HERE**
   - 2-week infrastructure setup plan
   - Monorepo scaffolding
   - Firebase configuration
   - CI/CD pipeline
   - Ready to start building!

7. **[Sprint Status](./sprint/status.yaml)**
   - Current sprint tracking
   - Story management
   - Team assignments

8. **[Story Categories](./sprint/categories.yaml)**
   - All feature categories for `pnpm story:create`
   - Includes: POS, CASHIER, RECEIPT categories

### 💻 Development

9. **Development Guides**:
   - **[Modular Architecture Guide](./architecture/modular-architecture.md)** ✅ - Service & component patterns
   - Setup guide (coming soon)
   - Coding standards (coming soon)
   - Firebase development (coming soon)
   - Testing strategy (coming soon)

---

## 🚀 Quick Start

### For New Developers

1. **Read** [Project Context](./00-PROJECT-CONTEXT.md) to understand the project
2. **Follow** [Sprint 0 Guide](./sprint/sprint-00-infrastructure-setup.md) to setup infrastructure
3. **Create stories** using `pnpm story:create` (after Sprint 0)
4. **Start building!**

### For Product/Business Team

1. **Read** [Project Context](./00-PROJECT-CONTEXT.md) for business overview
2. **Review** [MVP Features](./features/01-MVP-WEB-FEATURES.md) for scope
3. **Check** [Sprint Status](./sprint/status.yaml) for progress

---

## 📋 Current Sprint

**Sprint 0: Infrastructure Setup**
- **Duration**: 2 weeks
- **Goal**: Complete development infrastructure
- **Status**: Not started
- **Next**: Follow [Sprint 0 plan](./sprint/sprint-00-infrastructure-setup.md)

---

## 🎯 Project Phases

### Phase 1: Web Platform (MVP) - 8-10 weeks
**Goal**: Launch functional web marketplace

**Features**:
- Multi-tenant stores
- Product management (multi-tier pricing, unit packages)
- Marketplace (responsive web)
- Checkout & payment (Midtrans)
- Shipping (RajaOngkir)
- Order management
- Basic analytics

### Phase 1.5: Financial Management - 4-6 weeks
**Features**: Purchasing + Accounts Payable

### Phase 2: Complete ERP - 4-6 weeks
**Features**: Accounts Receivable + Financial reports

### Phase 3: Mobile App - 2-3 months
**Features**: React Native Expo (iOS & Android)

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 16 (App Router)
- **UI**: shadcn/ui, TanStack Table
- **State**: Zustand
- **Data**: TanStack Query
- **i18n**: next-intl (Indonesian + English)

### Backend
- **Database**: Firebase Firestore
- **Auth**: Firebase Auth
- **Storage**: Firebase Storage
- **Functions**: Cloud Functions
- **Hosting**: Firebase App Hosting

### Integrations
- **Payment**: Midtrans (Indonesia)
- **Shipping**: RajaOngkir (Indonesia)

---

## 📁 Repository Structure

```
pos-app-v1/
├── apps/              # Next.js applications
├── packages/          # Shared packages
├── functions/         # Cloud Functions
├── docs/              # 📚 Documentation (you are here)
├── scripts/           # Utility scripts
└── firebase/          # Firebase config
```

---

## 🎮 Available Commands

```bash
# Development
pnpm dev                    # Start all apps
pnpm build                  # Build all apps
pnpm lint                   # Lint all packages

# Firebase
firebase emulators:start    # Start emulators
firebase deploy             # Deploy

# Story Management
pnpm story:create           # Create new story (after Sprint 0)
```

---

## 🎉 Key Features (Competitive Advantages)

1. ✅ **Indonesian Market Fit**: DUS/PACK/PCS, tempo/kredit, RajaOngkir, Midtrans
2. ✅ **Multi-Tier Pricing**: Wholesale + Retail + Member
3. ✅ **POS Cashier**: In-store transactions with Cash, EDC, QRIS, Transfer
4. ✅ **Financial Management**: AP/AR tracking
5. ✅ **All-in-One**: Store + Marketplace + ERP
6. ✅ **Multi-Language**: Indonesian (default) + English

---

**Last Updated**: 2024-12-13
**Version**: 1.0.0
**Status**: Planning Phase → Ready for Sprint 0
