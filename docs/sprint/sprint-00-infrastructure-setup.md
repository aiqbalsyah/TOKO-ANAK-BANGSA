# Sprint 0: Infrastructure Setup

**Duration**: 2 weeks
**Goal**: Setup complete development infrastructure and deployment pipeline
**Team**: All developers

---

## Sprint Goals

By the end of Sprint 0, we will have:

✅ Monorepo scaffolded and running locally
✅ Firebase project configured (dev, staging, prod)
✅ All Next.js apps initialized
✅ Shared packages created
✅ CI/CD pipeline working
✅ Firebase App Hosting configured
✅ Local development environment with emulators
✅ Team can start building features in Sprint 1

---

## Tasks Breakdown

### Week 1: Project Structure & Firebase Setup

#### Day 1-2: Monorepo Scaffolding

**Tasks**:
1. Initialize monorepo with Turborepo
2. Configure pnpm workspace
3. Setup project structure
4. Configure TypeScript (shared config)
5. Setup ESLint & Prettier

**Deliverables**:
```
pos-app-v1/
├── apps/
│   ├── store-portal/        # Next.js app (initialized)
│   ├── marketplace/          # Next.js app (initialized)
│   ├── company-profile/      # Next.js app (initialized)
│   └── platform-admin/       # Next.js app (initialized)
├── packages/
│   ├── firebase-client/      # Firebase SDK wrapper
│   ├── shared-types/         # Zod schemas & types
│   └── ui-web/               # shadcn components
├── functions/                # Cloud Functions
├── turbo.json
├── pnpm-workspace.yaml
└── package.json
```

**Commands**:
```bash
# Initialize Turborepo
npx create-turbo@latest

# Install dependencies
pnpm install

# Verify setup
pnpm build
pnpm dev
```

---

#### Day 3-4: Firebase Project Setup

**Tasks**:
1. Create Firebase projects (dev, staging, prod)
2. Initialize Firebase in project
3. Configure Firestore
4. Configure Firebase Auth
5. Configure Firebase Storage
6. Setup Firebase RTDB
7. Create initial Security Rules
8. Setup Firebase Emulators

**Deliverables**:
- Firebase projects created:
  - `pos-marketplace-dev`
  - `pos-marketplace-staging`
  - `pos-marketplace-prod`
- `firebase.json` configured
- `.firebaserc` with project aliases
- Firestore rules file (`firebase/firestore.rules`)
- Storage rules file (`firebase/storage.rules`)
- Emulators running locally

**Commands**:
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Create projects
firebase projects:create pos-marketplace-dev
firebase projects:create pos-marketplace-staging
firebase projects:create pos-marketplace-prod

# Initialize Firebase
firebase init

# Start emulators
firebase emulators:start
```

---

#### Day 5: Shared Packages Setup

**Task 1: Firebase Client Package**

Location: `packages/firebase-client/`

```typescript
// packages/firebase-client/src/index.ts
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';
import { getStorage } from 'firebase/storage';

export const firebaseApp = initializeApp({
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
});

export const db = getFirestore(firebaseApp);
export const auth = getAuth(firebaseApp);
export const storage = getStorage(firebaseApp);
```

**Task 2: Shared Types Package**

Location: `packages/shared-types/`

```typescript
// packages/shared-types/src/product.ts
import { z } from 'zod';

export const ProductSchema = z.object({
  id: z.string(),
  tenantId: z.string(),
  name: z.string().min(1),
  description: z.string().optional(),
  // ... more fields
});

export type Product = z.infer<typeof ProductSchema>;
```

**Task 3: UI Components Package**

Location: `packages/ui-web/`

- Initialize shadcn/ui
- Create shared components (Button, Input, Form, etc.)
- Export components for use in Next.js apps

---

### Week 2: Next.js Apps & Deployment

#### Day 6-7: Next.js Apps Initialization

**Task 1: Store Portal** (`apps/store-portal/`)

```bash
cd apps
npx create-next-app@latest store-portal --typescript --tailwind --app
```

Features:
- App Router (Next.js 13+)
- TypeScript
- Tailwind CSS
- next-intl (i18n)
- Firebase integration
- shadcn/ui

**Task 2: Marketplace** (`apps/marketplace/`)

Same setup as Store Portal

**Task 3: Company Profile** (`apps/company-profile/`)

Static site with marketing content

**Task 4: Platform Admin** (`apps/platform-admin/`)

Internal admin dashboard

**Deliverables**:
- All 4 Next.js apps running locally
- Each app connected to Firebase
- Each app has i18n configured (id, en)
- Basic homepage for each app

---

#### Day 8-9: Firebase App Hosting Configuration

**Tasks**:
1. Create `apphosting.*.yaml` files for each app
2. Configure environment variables
3. Test local deployment
4. Deploy to dev environment

**Files to Create**:
- `apphosting.store-portal.yaml`
- `apphosting.marketplace.yaml`
- `apphosting.company-profile.yaml`
- `apphosting.platform-admin.yaml`

**Test Deployment**:
```bash
# Deploy to dev
firebase use dev
firebase deploy --only hosting:store-portal

# Verify
# Visit: https://store-portal-dev.web.app
```

---

#### Day 10: CI/CD Pipeline Setup

**GitHub Actions Workflow**:

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Firebase

on:
  push:
    branches:
      - main        # Production
      - develop     # Staging
      - dev         # Development

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install

      - name: Build
        run: pnpm build

      - name: Deploy to Firebase
        uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: ${{ secrets.GITHUB_TOKEN }}
          firebaseServiceAccount: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
          projectId: pos-marketplace-${{ github.ref == 'refs/heads/main' && 'prod' || github.ref == 'refs/heads/develop' && 'staging' || 'dev' }}
          channelId: live
```

**Setup Secrets**:
- Add `FIREBASE_SERVICE_ACCOUNT` to GitHub Secrets
- Test deployment on push to dev branch

---

### Additional Tasks

#### Cloud Functions Setup

**Location**: `functions/`

```bash
cd functions
npm init -y
npm install firebase-functions firebase-admin
```

**Create Basic Function**:

```javascript
// functions/src/index.ts
import * as functions from 'firebase-functions';

export const helloWorld = functions.https.onRequest((request, response) => {
  response.json({ message: "Hello from Firebase!" });
});
```

**Deploy**:
```bash
firebase deploy --only functions
```

---

#### Environment Variables

**Create `.env.local` files**:

```bash
# apps/store-portal/.env.local
NEXT_PUBLIC_FIREBASE_API_KEY=your-api-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-auth-domain
NEXT_PUBLIC_FIREBASE_PROJECT_ID=pos-marketplace-dev
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-storage-bucket
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id
```

**Note**: Do NOT commit `.env.local` to git. Add to `.gitignore`.

---

#### Documentation

**Update README.md**:

```markdown
# POS Marketplace

Multi-tenant SaaS platform for Indonesian SMEs.

## Quick Start

### Prerequisites
- Node.js 20+
- pnpm 8+
- Firebase CLI

### Installation
\```bash
# Install dependencies
pnpm install

# Setup Firebase
firebase login
firebase use dev

# Start emulators
firebase emulators:start

# Start development (in another terminal)
pnpm dev
\```

### Available Commands
- `pnpm dev` - Start all apps in development mode
- `pnpm build` - Build all apps
- `pnpm lint` - Lint all packages
- `pnpm test` - Run tests
- `pnpm story:create` - Create new story

### Project Structure
- `apps/` - Next.js applications
- `packages/` - Shared packages
- `functions/` - Cloud Functions
- `firebase/` - Firebase configuration
- `docs/` - Documentation

## Documentation
See `docs/` folder for complete documentation.
```

---

## Sprint 0 Checklist

### Infrastructure
- [ ] Monorepo initialized with Turborepo
- [ ] pnpm workspace configured
- [ ] TypeScript configured
- [ ] ESLint & Prettier configured

### Firebase
- [ ] Firebase projects created (dev, staging, prod)
- [ ] Firebase initialized in project
- [ ] Firestore configured
- [ ] Auth configured
- [ ] Storage configured
- [ ] RTDB configured
- [ ] Security Rules created
- [ ] Emulators running

### Packages
- [ ] `firebase-client` package created
- [ ] `shared-types` package created
- [ ] `ui-web` package created (shadcn)

### Apps
- [ ] `store-portal` app initialized
- [ ] `marketplace` app initialized
- [ ] `company-profile` app initialized
- [ ] `platform-admin` app initialized
- [ ] All apps connected to Firebase
- [ ] i18n configured (id, en)
- [ ] All apps running locally

### Deployment
- [ ] App Hosting configs created
- [ ] Deployed to dev environment
- [ ] CI/CD pipeline working
- [ ] GitHub Actions configured

### Documentation
- [ ] README.md updated
- [ ] Contributing guide created
- [ ] Development guide created

### Testing
- [ ] Can run `pnpm dev` successfully
- [ ] Can access all apps locally
- [ ] Firebase emulators working
- [ ] Can deploy to Firebase
- [ ] CI/CD pipeline passing

---

## Success Criteria

At the end of Sprint 0:

✅ **Local Development Works**:
- Run `pnpm dev` → All apps start
- Access apps at localhost
- Firebase emulators running
- Hot reload working

✅ **Deployment Works**:
- Push to dev branch → Auto-deploys to Firebase
- All apps accessible via Firebase URLs
- No deployment errors

✅ **Team Can Start Development**:
- Clear project structure
- Documentation complete
- Development environment setup guide
- Ready to create stories and begin Sprint 1

---

## Risks & Mitigation

**Risk 1**: Firebase quota limits on free tier
- **Mitigation**: Use emulators for development, only deploy for testing

**Risk 2**: Monorepo complexity
- **Mitigation**: Use Turborepo for simple, fast builds

**Risk 3**: Team unfamiliar with Firebase
- **Mitigation**: Create clear documentation, pair programming

---

## Next Steps

After Sprint 0 completion:

1. ✅ Sprint 0 Review
2. ✅ Demo working infrastructure to team
3. ✅ Sprint 1 Planning
4. ⏳ Begin feature development (Auth & Store Creation)

---

**Sprint Owner**: Tech Lead
**Last Updated**: 2024-12-13
