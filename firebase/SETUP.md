# Firebase Setup Guide

This guide walks you through setting up Firebase for TOKO ANAK BANGSA.

## Prerequisites

1. Google account
2. Firebase CLI installed

## Step 1: Install Firebase CLI (if not installed)

```bash
npm install -g firebase-tools
```

Verify installation:
```bash
firebase --version
```

## Step 2: Login to Firebase

```bash
firebase login
```

This will open a browser for authentication.

## Step 3: Create Firebase Projects

You need to create 3 Firebase projects (one for each environment):

### Option A: Via Firebase Console (Recommended for first time)

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Create these projects:
   - **Dev**: `toko-anak-bangsa-dev`
   - **Staging**: `toko-anak-bangsa-staging`
   - **Prod**: `toko-anak-bangsa-prod`

For each project:
- Disable Google Analytics (or enable if you want)
- Select region: `asia-southeast1` (Jakarta, Indonesia)

### Option B: Via CLI

```bash
# Create dev project
firebase projects:create toko-anak-bangsa-dev \
  --display-name "TOKO ANAK BANGSA - Development"

# Create staging project
firebase projects:create toko-anak-bangsa-staging \
  --display-name "TOKO ANAK BANGSA - Staging"

# Create production project
firebase projects:create toko-anak-bangsa-prod \
  --display-name "TOKO ANAK BANGSA - Production"
```

## Step 4: Enable Firebase Services

For **EACH** project (dev, staging, prod), enable these services via Firebase Console:

### 4.1 Authentication
1. Go to Firebase Console → Your Project → Authentication
2. Click "Get Started"
3. Enable sign-in methods:
   - ✅ Email/Password
   - ✅ Google (optional)
4. Click "Save"

### 4.2 Firestore Database
1. Go to Firestore Database
2. Click "Create database"
3. Select **Production mode** (we'll deploy our custom rules)
4. Choose location: `asia-southeast1` (Jakarta)
5. Click "Enable"

### 4.3 Storage
1. Go to Storage
2. Click "Get started"
3. Select **Production mode** (we'll deploy our custom rules)
4. Choose location: `asia-southeast1`
5. Click "Done"

### 4.4 Realtime Database
1. Go to Realtime Database
2. Click "Create Database"
3. Choose location: `asia-southeast1`
4. Start in **locked mode** (we'll deploy our custom rules)
5. Click "Enable"

## Step 5: Deploy Security Rules

Switch to dev environment and deploy rules:

```bash
# Use dev project
firebase use dev

# Deploy Firestore rules
firebase deploy --only firestore:rules

# Deploy Storage rules
firebase deploy --only storage:rules

# Deploy Realtime Database rules
firebase deploy --only database:rules
```

Repeat for staging and prod:
```bash
firebase use staging
firebase deploy --only firestore:rules,storage:rules,database:rules

firebase use prod
firebase deploy --only firestore:rules,storage:rules,database:rules
```

## Step 6: Get Firebase Config

For each project, get the web app config:

1. Go to Firebase Console → Project Settings
2. Scroll to "Your apps"
3. Click "Web" (</>) to add a web app
4. Register app with nickname:
   - Dev: "Store Portal Dev", "Marketplace Dev", etc.
   - Staging: "Store Portal Staging", etc.
   - Prod: "Store Portal Prod", etc.
5. Copy the `firebaseConfig` object

## Step 7: Setup Environment Variables

Create `.env.local` files for each Next.js app:

### apps/store-portal/.env.local
```bash
NEXT_PUBLIC_FIREBASE_API_KEY=your-api-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-auth-domain
NEXT_PUBLIC_FIREBASE_PROJECT_ID=toko-anak-bangsa-dev
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-storage-bucket
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
NEXT_PUBLIC_FIREBASE_APP_ID=your-app-id
```

Repeat for `marketplace`, `company-profile`, and `platform-admin`.

**IMPORTANT**: Never commit `.env.local` to git!

## Step 8: Start Firebase Emulators (Local Development)

```bash
firebase use dev
firebase emulators:start
```

Or use the monorepo command:
```bash
pnpm firebase:emulators
```

Emulator UI will be available at: `http://localhost:4000`

## Step 9: Verify Setup

Check that emulators are running:
- Auth Emulator: `http://localhost:9099`
- Firestore Emulator: `http://localhost:8080`
- Storage Emulator: `http://localhost:9199`
- Realtime Database Emulator: `http://localhost:9000`
- Emulator UI: `http://localhost:4000`

## Troubleshooting

### Emulators won't start
```bash
# Kill any processes using the ports
lsof -ti:4000,8080,9099,9000,9199 | xargs kill -9

# Try again
firebase emulators:start
```

### Can't switch projects
```bash
# List available projects
firebase projects:list

# Use specific project
firebase use toko-anak-bangsa-dev
```

## Next Steps

After Firebase setup is complete:
- ✅ Create shared packages (`firebase-client`, `shared-types`, `ui-web`)
- ✅ Initialize Next.js apps
- ✅ Connect apps to Firebase

---

**Need Help?**
- [Firebase Documentation](https://firebase.google.com/docs)
- [Firebase Emulators](https://firebase.google.com/docs/emulator-suite)
