# TOKO ANAK BANGSA

> Multi-tenant POS & Marketplace Platform for Indonesian SMEs

A modern, scalable platform built with Next.js 16, Flask API, and Firebase, designed to empower Indonesian small and medium enterprises with powerful e-commerce and point-of-sale capabilities.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development](#development)
- [Deployment](#deployment)
- [Documentation](#documentation)
- [Contributing](#contributing)

---

## Features

### Multi-tenant Architecture
- **Isolated Data**: Each store has isolated data with row-level security
- **Custom Domains**: Support for custom store domains
- **Role-based Access**: Owner, Admin, Staff, and Cashier roles
- **Subscription Plans**: Free, Basic, Pro, and Enterprise tiers

### Applications
1. **Store Portal** (Port 3000) - POS & Store Management
2. **Marketplace** (Port 3001) - Public E-commerce Platform
3. **Company Profile** (Port 3002) - Landing Page
4. **Platform Admin** (Port 3003) - Platform Management Dashboard
5. **Flask API** (Port 8080) - Backend Services

### Core Capabilities
- Point of Sale (POS) system
- Inventory management
- Customer relationship management
- Multi-channel selling (online + offline)
- Real-time analytics
- Payment gateway integration
- Invoice and receipt generation
- Multi-language support (Indonesian, English)

---

## Technology Stack

### Frontend
- **Framework**: Next.js 16 (App Router)
- **Language**: TypeScript 5.8
- **UI Library**: React 19
- **Styling**: Tailwind CSS + shadcn/ui
- **State Management**: React Context + Hooks
- **Validation**: Zod schemas
- **Internationalization**: next-intl

### Backend
- **API**: Python Flask 3.1
- **Runtime**: Python 3.12
- **CORS**: Flask-CORS

### Database & Services
- **Database**: Firebase Firestore (NoSQL)
- **Authentication**: Firebase Auth
- **Storage**: Firebase Storage
- **Real-time**: Firebase Realtime Database
- **Hosting**: Firebase App Hosting

### Development Tools
- **Monorepo**: Turborepo + pnpm workspaces
- **Linting**: ESLint 9 (flat config)
- **Formatting**: Prettier
- **Type Checking**: TypeScript
- **Package Building**: tsup

---

## Project Structure

```
pos_app_v1/
├── apps/
│   ├── api/                    # Flask API (Python 3.12)
│   ├── store-portal/           # Store Portal (Next.js 16)
│   ├── marketplace/            # Marketplace (Next.js 16)
│   ├── company-profile/        # Company Profile (Next.js 16)
│   └── platform-admin/         # Platform Admin (Next.js 16)
├── packages/
│   ├── firebase-client/        # Firebase SDK wrapper
│   ├── shared-types/           # Zod schemas & TypeScript types
│   └── ui-web/                 # shadcn/ui components
├── firebase/
│   ├── firestore.rules         # Firestore security rules
│   ├── storage.rules           # Storage security rules
│   └── database.rules.json     # RTDB security rules
├── apphosting.*.yaml           # Firebase App Hosting configs
├── firebase.json               # Firebase configuration
├── turbo.json                  # Turborepo configuration
├── pnpm-workspace.yaml         # pnpm workspace configuration
├── .env.local                  # Development environment
├── .env.staging                # Staging environment
├── .env.production             # Production environment
├── DEVELOPER_GUIDE.md          # Component architecture guide
└── ENVIRONMENTS.md             # Environment configuration guide
```

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js**: >= 20.0.0 ([Download](https://nodejs.org/))
- **pnpm**: >= 10.0.0 (`npm install -g pnpm`)
- **Python**: >= 3.12 ([Download](https://www.python.org/))
- **Firebase CLI**: Latest version (`npm install -g firebase-tools`)
- **Git**: Latest version ([Download](https://git-scm.com/))

### Verify Installation

```bash
node --version    # Should be >= 20.0.0
pnpm --version    # Should be >= 10.0.0
python --version  # Should be >= 3.12
firebase --version
git --version
```

---

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd pos_app_v1
```

### 2. Install Dependencies

```bash
# Install JavaScript/TypeScript dependencies
pnpm install

# Install Python dependencies for Flask API
cd apps/api
pip install -r requirements.txt
cd ../..
```

### 3. Environment Setup

```bash
# Copy environment variables
cp .env.local .env.local.backup  # Backup if exists
```

Make sure `.env.local` contains your Firebase development credentials. See [ENVIRONMENTS.md](./ENVIRONMENTS.md) for details.

### 4. Build Shared Packages

```bash
# Build all shared packages (required before running apps)
pnpm build
```

### 5. Start Development Servers

#### Option A: Run All Apps

```bash
pnpm dev
```

This starts:
- Store Portal: http://localhost:3000
- Marketplace: http://localhost:3001
- Company Profile: http://localhost:3002
- Platform Admin: http://localhost:3003
- Flask API: http://localhost:8080

#### Option B: Run Specific Apps

```bash
# Run only Store Portal
pnpm dev:store-portal

# Run only Marketplace
pnpm dev:marketplace

# Run only Company Profile
pnpm dev:company-profile

# Run only Platform Admin
pnpm dev:platform-admin

# Run only Flask API
pnpm dev:api
```

---

## Development

### Available Commands

```bash
# Development
pnpm dev                        # Run all apps
pnpm dev:store-portal           # Run store portal only
pnpm dev:marketplace            # Run marketplace only
pnpm dev:company-profile        # Run company profile only
pnpm dev:platform-admin         # Run platform admin only
pnpm dev:api                    # Run Flask API only

# Building
pnpm build                      # Build all apps and packages
pnpm build:store-portal         # Build store portal only
pnpm build:marketplace          # Build marketplace only
pnpm build:company-profile      # Build company profile only
pnpm build:platform-admin       # Build platform admin only

# Code Quality
pnpm typecheck                  # TypeScript type checking
pnpm lint                       # Lint all code
pnpm test                       # Run tests (when available)
pnpm clean                      # Clean build artifacts

# Firebase
pnpm firebase:emulators         # Start Firebase emulators
firebase login                  # Login to Firebase
firebase use <project-id>       # Switch Firebase project
```

### Adding Dependencies

```bash
# Add to specific app
pnpm --filter @toko/store-portal add package-name

# Add to shared package
pnpm --filter @toko/ui-web add package-name

# Add dev dependency to root
pnpm add -D -w package-name
```

### Creating a New Page

See the [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md) for detailed instructions on creating new pages with the proper component architecture.

Example structure:
```
components/pages/dashboard/
├── index.tsx              # Main component (composition)
├── components/            # Sub-components (presentation)
│   ├── stats-grid.tsx
│   └── recent-orders.tsx
├── hooks/                 # Custom hooks (logic)
│   └── use-dashboard-data.ts
└── utils/                 # Helper functions
    └── format-stats.ts
```

### Firebase Emulators

For local development with Firebase emulators:

```bash
# Start emulators
pnpm firebase:emulators

# In another terminal, set environment variable
export NEXT_PUBLIC_USE_FIREBASE_EMULATOR=true

# Then start your apps
pnpm dev
```

---

## Deployment

### Prerequisites

1. Firebase projects set up for dev, staging, and production
2. Firebase CLI authenticated: `firebase login`
3. Environment variables configured in Firebase App Hosting

### Deploy to Development

```bash
# Switch to dev project
firebase use dev

# Deploy specific app
pnpm deploy:store-portal
pnpm deploy:marketplace
pnpm deploy:company-profile
pnpm deploy:platform-admin
pnpm deploy:api

# Or deploy all apps
pnpm deploy:all
```

### Deploy to Staging

```bash
# Switch to staging project
firebase use staging

# Deploy all
pnpm deploy:all
```

### Deploy to Production

```bash
# Switch to production project
firebase use prod

# Deploy all
pnpm deploy:all
```

### Firebase App Hosting Targets

Each app has its own App Hosting configuration:

- `apphosting.store-portal.yaml` - Store Portal
- `apphosting.marketplace.yaml` - Marketplace
- `apphosting.company-profile.yaml` - Company Profile
- `apphosting.platform-admin.yaml` - Platform Admin
- `apphosting.api.yaml` - Flask API

See [ENVIRONMENTS.md](./ENVIRONMENTS.md) for detailed environment setup and deployment procedures.

---

## Documentation

- **[DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md)** - Complete guide for developers including component architecture, best practices, and workflow
- **[ENVIRONMENTS.md](./ENVIRONMENTS.md)** - Environment configuration and deployment guide

### External Resources

- [Next.js 16 Documentation](https://nextjs.org/docs)
- [React 19 Documentation](https://react.dev/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [shadcn/ui Documentation](https://ui.shadcn.com)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Zod Documentation](https://zod.dev)
- [Turborepo Documentation](https://turbo.build/repo/docs)
- [pnpm Workspaces](https://pnpm.io/workspaces)

---

## Troubleshooting

### TypeScript Errors

If you encounter TypeScript errors about missing types from shared packages:

```bash
# Build shared packages first
pnpm build

# Or run in dev mode (auto-builds on changes)
pnpm dev
```

### Import Resolution Issues

```bash
# Clear Next.js cache
rm -rf apps/*/.next

# Reinstall dependencies
rm -rf node_modules
pnpm install
```

### Firebase Connection Issues

Check that your environment variables are correctly set:

```bash
# Verify .env.local has the correct Firebase config
cat .env.local
```

### Port Already in Use

If you get "port already in use" errors:

```bash
# Find process using the port (example: 3000)
lsof -i :3000

# Kill the process
kill -9 <PID>
```

---

## Contributing

### Branch Naming

- `feature/` - New features
- `fix/` - Bug fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation updates
- `chore/` - Maintenance tasks

### Commit Messages

Follow conventional commits:

```
feat(store-portal): add dashboard page
fix(marketplace): resolve product search issue
docs(readme): update installation steps
chore(deps): upgrade Next.js to 16.1.0
```

### Development Workflow

1. Create feature branch: `git checkout -b feature/dashboard-page`
2. Make changes following the [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md)
3. Type check: `pnpm typecheck`
4. Lint: `pnpm lint`
5. Commit: `git commit -m "feat(store-portal): add dashboard page"`
6. Push and create PR: `git push origin feature/dashboard-page`

---

## Project Status

**Current Phase**: Sprint 0 - Infrastructure Setup

### Completed
- ✅ Monorepo setup with Turborepo + pnpm
- ✅ All 4 Next.js 16 apps initialized
- ✅ Flask API structure
- ✅ Shared packages (firebase-client, shared-types, ui-web)
- ✅ Firebase configuration (Firestore, Auth, Storage, RTDB)
- ✅ Security rules for all Firebase services
- ✅ Multi-environment setup (dev, staging, prod)
- ✅ Firebase App Hosting configurations
- ✅ Developer documentation

### In Progress
- 🔄 i18n configuration with next-intl
- 🔄 CI/CD pipeline with GitHub Actions

### Upcoming
- 📋 Core POS features
- 📋 Marketplace features
- 📋 Payment gateway integration
- 📋 Testing setup
- 📋 Performance optimization

---

## License

Proprietary - All rights reserved

---

## Support

For questions or issues:

1. Check the [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md)
2. Search existing GitHub issues
3. Contact the development team
4. Create a new GitHub issue with detailed reproduction steps

---

**Built with ❤️ for Indonesian SMEs**
