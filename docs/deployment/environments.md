# Environment Configuration Guide

This document explains how to configure environments for TOKO ANAK BANGSA platform.

## Overview

The platform supports three environments:
- **Development** - Local development with Firebase dev project
- **Staging** - Pre-production testing with Firebase staging project
- **Production** - Live production with Firebase prod project

## Environment Files

### `.env.local` (Development - Local)
Used for local development on your machine.

```bash
# Copy from .env.example
cp .env.example .env.local
```

This file is **gitignored** and contains your local development credentials.

### `.env.staging` (Staging)
Used for staging deployments via CI/CD.

This file **IS committed** to git and contains staging credentials.

### `.env.production` (Production)
Used for production deployments via CI/CD.

This file **IS committed** to git but sensitive values should be managed via GitHub Secrets or Firebase App Hosting environment variables.

## Firebase Projects

### Development
- **Project ID**: `toko-anak-bangsa-dev`
- **Console**: https://console.firebase.google.com/project/toko-anak-bangsa-dev
- **Purpose**: Local development and testing

### Staging
- **Project ID**: `toko-anak-bangsa-staging`
- **Console**: https://console.firebase.google.com/project/toko-anak-bangsa-staging
- **Purpose**: Pre-production testing, QA, demo

### Production
- **Project ID**: `toko-anak-bangsa-prod` (to be created)
- **Console**: https://console.firebase.google.com/project/toko-anak-bangsa-prod
- **Purpose**: Live production environment

## Local Development

### Using Firebase Dev Project

```bash
# 1. Copy environment template
cp .env.example .env.local

# 2. Install dependencies
pnpm install

# 3. Start development servers
pnpm dev                    # All apps
pnpm dev:api                # Flask API only

# 4. Start Firebase Emulators (optional)
pnpm firebase:emulators
```

### Using Firebase Emulators

For complete offline development:

1. Update `.env.local`:
   ```bash
   NEXT_PUBLIC_USE_FIREBASE_EMULATOR=true
   ```

2. Start emulators:
   ```bash
   pnpm firebase:emulators
   ```

3. Access Emulator UI:
   - **Emulator UI**: http://localhost:4000
   - **Auth Emulator**: http://localhost:9099
   - **Firestore Emulator**: http://localhost:8080
   - **Storage Emulator**: http://localhost:9199
   - **RTDB Emulator**: http://localhost:9000

## Deployment

### Deploy to Staging

```bash
# Deploy all apps to staging
firebase use staging
firebase deploy --only hosting,apphosting

# Or deploy specific app
firebase deploy --only apphosting:store-portal
```

### Deploy to Production

```bash
# Deploy all apps to production
firebase use prod
firebase deploy --only hosting,apphosting

# Or deploy specific app
firebase deploy --only apphosting:marketplace
```

## CI/CD with GitHub Actions

The project uses GitHub Actions for automated deployments.

### Staging Deployment
- **Trigger**: Push to `develop` branch
- **Environment**: Staging
- **Uses**: `.env.staging` values

### Production Deployment
- **Trigger**: Push to `main` branch
- **Environment**: Production
- **Uses**: `.env.production` values + GitHub Secrets

## Environment Variables

### Required Variables

#### Firebase Configuration
```bash
NEXT_PUBLIC_FIREBASE_API_KEY=          # Firebase API Key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=      # Auth domain
NEXT_PUBLIC_FIREBASE_PROJECT_ID=       # Project ID
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=   # Storage bucket
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID= # Sender ID
NEXT_PUBLIC_FIREBASE_APP_ID=           # App ID
NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID=   # Analytics measurement ID
NEXT_PUBLIC_FIREBASE_DATABASE_URL=     # Realtime Database URL
```

#### App Configuration
```bash
NEXT_PUBLIC_APP_ENV=                   # development | staging | production
NEXT_PUBLIC_USE_FIREBASE_EMULATOR=     # true | false
NEXT_PUBLIC_APP_URL=                   # App base URL
NEXT_PUBLIC_API_URL=                   # API base URL
```

### Optional Variables

#### Third-party Services
```bash
# Payment Gateway (Midtrans)
NEXT_PUBLIC_MIDTRANS_CLIENT_KEY=
MIDTRANS_SERVER_KEY=                   # Server-side only

# WhatsApp Business API
WHATSAPP_API_TOKEN=                    # Server-side only

# Email Service
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
```

## Security Best Practices

### 1. Never Commit Secrets
- `.env.local` is gitignored - contains local secrets
- Use GitHub Secrets for CI/CD sensitive values
- Use Firebase App Hosting environment variables for runtime secrets

### 2. Use Environment-Specific Credentials
- Each environment has its own Firebase project
- Never use production credentials in development
- Rotate API keys regularly

### 3. Validate Environment Variables
All Next.js apps should validate required environment variables on startup:

```typescript
// lib/env.ts
const requiredEnvVars = [
  'NEXT_PUBLIC_FIREBASE_API_KEY',
  'NEXT_PUBLIC_FIREBASE_PROJECT_ID',
  // ... other required vars
];

requiredEnvVars.forEach((envVar) => {
  if (!process.env[envVar]) {
    throw new Error(`Missing required environment variable: ${envVar}`);
  }
});
```

## Troubleshooting

### Issue: Firebase not connecting

**Solution**: Check that environment variables are correctly set
```bash
# In your Next.js app, add logging
console.log('Firebase Config:', {
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  // ... other config
});
```

### Issue: Emulators not connecting

**Solution**: Ensure emulators are running and `NEXT_PUBLIC_USE_FIREBASE_EMULATOR=true`
```bash
# Check emulator status
firebase emulators:start

# Check connection in browser console
# Should show: "Connecting to Auth emulator at localhost:9099"
```

### Issue: Different environment variables between apps

**Solution**: Ensure all apps load from the same `.env.local` file at the root
```bash
# In Next.js config
env: {
  NEXT_PUBLIC_FIREBASE_API_KEY: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  // ... explicitly define all variables
}
```

## Port Assignments

### Applications
- **store-portal**: http://localhost:3000
- **marketplace**: http://localhost:3001
- **company-profile**: http://localhost:3002
- **platform-admin**: http://localhost:3003
- **Flask API**: http://localhost:8080

### Firebase Emulators
- **Emulator UI**: http://localhost:4000
- **Firestore**: http://localhost:8080
- **Auth**: http://localhost:9099
- **Storage**: http://localhost:9199
- **RTDB**: http://localhost:9000

## Additional Resources

- [Firebase Documentation](https://firebase.google.com/docs)
- [Next.js Environment Variables](https://nextjs.org/docs/basic-features/environment-variables)
- [Firebase App Hosting](https://firebase.google.com/docs/app-hosting)
