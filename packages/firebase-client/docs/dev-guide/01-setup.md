# Firebase Client - Development Setup Guide

**Project**: Firebase Client Library
**Tech Stack**: TypeScript, Firebase SDK 10, tsup
**Purpose**: Shared Firebase SDK wrapper and utilities for all TOKO ANAK BANGSA applications

---

## Overview

`@toko/firebase-client` is a shared package that provides a centralized Firebase SDK wrapper for all web applications in the monorepo. It handles Firebase initialization, authentication, Firestore, Storage, and other Firebase services with consistent configuration across all apps.

**Why a Shared Package?**
- **Consistency**: Single source of truth for Firebase configuration
- **DRY**: Avoid duplicating Firebase setup code in each app
- **Type Safety**: Centralized TypeScript types for Firebase operations
- **Maintainability**: Update Firebase logic in one place
- **Version Control**: All apps use the same Firebase SDK version

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js 22+** - [Download Node.js](https://nodejs.org/)
- **pnpm 9+** - Install: `npm install -g pnpm`
- **TypeScript knowledge** - This is a TypeScript library

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
packages/firebase-client/
├── src/                    # Source code
│   ├── index.ts            # Main export file
│   ├── auth.ts             # Firebase Auth utilities
│   ├── firestore.ts        # Firestore utilities
│   ├── storage.ts          # Storage utilities
│   ├── config.ts           # Firebase configuration
│   └── types.ts            # TypeScript types
├── dist/                   # Build output (generated)
│   ├── index.js            # CommonJS build
│   ├── index.mjs           # ESM build
│   └── index.d.ts          # Type definitions
├── docs/                   # Documentation
│   └── dev-guide/          # Developer guides
├── package.json            # Package configuration
├── tsconfig.json           # TypeScript configuration
└── README.md               # Package overview
```

---

## Development Workflow

### 1. Build Package

**Development mode (watch):**
```bash
cd packages/firebase-client
pnpm dev
```

This will build the package and watch for changes, automatically rebuilding when you edit source files.

**Production build:**
```bash
pnpm build
```

### 2. Add New Dependency

```bash
cd packages/firebase-client
pnpm add package-name
```

### 3. Type Checking

```bash
pnpm typecheck
```

### 4. Clean Build Artifacts

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
    "build": "tsup src/index.ts --format cjs,esm --dts",
    "dev": "tsup src/index.ts --format cjs,esm --dts --watch"
  }
}
```

**Output formats:**
- **CommonJS** (`dist/index.js`) - For older Node.js/bundlers
- **ESM** (`dist/index.mjs`) - For modern bundlers/Node.js
- **TypeScript declarations** (`dist/index.d.ts`) - For type checking

### Package Exports

The package supports both CommonJS and ESM through `exports` field:

```json
{
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  }
}
```

---

## Using the Package in Apps

### Installation

Apps in the monorepo reference this package via workspace protocol:

```json
{
  "dependencies": {
    "@toko/firebase-client": "workspace:*"
  }
}
```

### Import in Applications

```typescript
// Import Firebase services
import { auth, db, storage } from '@toko/firebase-client';

// Import utilities
import { signInUser, signOutUser } from '@toko/firebase-client';
import { getDocumentById, createDocument } from '@toko/firebase-client';
import { uploadFile, downloadFile } from '@toko/firebase-client';
```

---

## Implementation Examples

### Example: Firebase Configuration

```typescript
// src/config.ts
import { initializeApp, getApps, FirebaseApp } from 'firebase/app';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Singleton pattern - initialize only once
let app: FirebaseApp;

if (getApps().length === 0) {
  app = initializeApp(firebaseConfig);
} else {
  app = getApps()[0];
}

export { app };
```

### Example: Auth Utilities

```typescript
// src/auth.ts
import { getAuth, signInWithEmailAndPassword, signOut } from 'firebase/auth';
import { app } from './config';

export const auth = getAuth(app);

export const signInUser = async (email: string, password: string) => {
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    return { user: userCredential.user, error: null };
  } catch (error: any) {
    return { user: null, error: error.message };
  }
};

export const signOutUser = async () => {
  try {
    await signOut(auth);
    return { success: true, error: null };
  } catch (error: any) {
    return { success: false, error: error.message };
  }
};

export const getCurrentUser = () => {
  return auth.currentUser;
};
```

### Example: Firestore Utilities

```typescript
// src/firestore.ts
import {
  getFirestore,
  collection,
  doc,
  getDoc,
  setDoc,
  addDoc,
  deleteDoc,
  query,
  where,
  getDocs
} from 'firebase/firestore';
import { app } from './config';

export const db = getFirestore(app);

export const getDocumentById = async <T>(
  collectionName: string,
  id: string
): Promise<T | null> => {
  try {
    const docRef = doc(db, collectionName, id);
    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      return { id: docSnap.id, ...docSnap.data() } as T;
    }
    return null;
  } catch (error) {
    console.error('Error fetching document:', error);
    throw error;
  }
};

export const createDocument = async <T>(
  collectionName: string,
  data: Partial<T>
): Promise<string> => {
  try {
    const docRef = await addDoc(collection(db, collectionName), data);
    return docRef.id;
  } catch (error) {
    console.error('Error creating document:', error);
    throw error;
  }
};

export const updateDocument = async <T>(
  collectionName: string,
  id: string,
  data: Partial<T>
): Promise<void> => {
  try {
    const docRef = doc(db, collectionName, id);
    await setDoc(docRef, data, { merge: true });
  } catch (error) {
    console.error('Error updating document:', error);
    throw error;
  }
};

export const deleteDocument = async (
  collectionName: string,
  id: string
): Promise<void> => {
  try {
    const docRef = doc(db, collectionName, id);
    await deleteDoc(docRef);
  } catch (error) {
    console.error('Error deleting document:', error);
    throw error;
  }
};

export const queryDocuments = async <T>(
  collectionName: string,
  field: string,
  operator: any,
  value: any
): Promise<T[]> => {
  try {
    const q = query(
      collection(db, collectionName),
      where(field, operator, value)
    );
    const querySnapshot = await getDocs(q);
    return querySnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    })) as T[];
  } catch (error) {
    console.error('Error querying documents:', error);
    throw error;
  }
};
```

### Example: Storage Utilities

```typescript
// src/storage.ts
import {
  getStorage,
  ref,
  uploadBytes,
  getDownloadURL,
  deleteObject
} from 'firebase/storage';
import { app } from './config';

export const storage = getStorage(app);

export const uploadFile = async (
  path: string,
  file: File
): Promise<string> => {
  try {
    const storageRef = ref(storage, path);
    const snapshot = await uploadBytes(storageRef, file);
    const downloadURL = await getDownloadURL(snapshot.ref);
    return downloadURL;
  } catch (error) {
    console.error('Error uploading file:', error);
    throw error;
  }
};

export const deleteFile = async (path: string): Promise<void> => {
  try {
    const storageRef = ref(storage, path);
    await deleteObject(storageRef);
  } catch (error) {
    console.error('Error deleting file:', error);
    throw error;
  }
};

export const getFileURL = async (path: string): Promise<string> => {
  try {
    const storageRef = ref(storage, path);
    return await getDownloadURL(storageRef);
  } catch (error) {
    console.error('Error getting file URL:', error);
    throw error;
  }
};
```

### Example: Main Export File

```typescript
// src/index.ts
// Export Firebase instances
export { auth, signInUser, signOutUser, getCurrentUser } from './auth';
export { db, getDocumentById, createDocument, updateDocument, deleteDocument, queryDocuments } from './firestore';
export { storage, uploadFile, deleteFile, getFileURL } from './storage';
export { app } from './config';

// Export types
export * from './types';
```

---

## TypeScript Types

### Example Types

```typescript
// src/types.ts
export interface FirebaseUser {
  uid: string;
  email: string | null;
  displayName: string | null;
  photoURL: string | null;
}

export interface FirestoreDocument {
  id: string;
  createdAt: string;
  updatedAt: string;
}

export interface UploadProgress {
  bytesTransferred: number;
  totalBytes: number;
  percentage: number;
}
```

---

## Usage in Applications

### Example: Using in Store Portal

```typescript
// apps/store-portal/lib/firebase.ts
import { auth, db, storage } from '@toko/firebase-client';

export { auth, db, storage };
```

### Example: Using Auth in Login Page

```tsx
// apps/store-portal/app/[locale]/(auth)/login/page.tsx
'use client';

import { signInUser } from '@toko/firebase-client';
import { useState } from 'react';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    const { user, error } = await signInUser(email, password);

    if (error) {
      alert(error);
      return;
    }

    // Redirect to dashboard
    console.log('Logged in:', user);
  };

  return (
    <div>
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}
```

### Example: Using Firestore in Products Page

```tsx
// apps/store-portal/hooks/useProducts.ts
import { useState, useEffect } from 'react';
import { queryDocuments } from '@toko/firebase-client';
import { Product } from '@toko/shared-types';

export function useProducts(tenantId: string) {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await queryDocuments<Product>(
          'products',
          'tenantId',
          '==',
          tenantId
        );
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [tenantId]);

  return { products, loading };
}
```

---

## Testing

### Unit Tests

```bash
# Install testing dependencies
pnpm add -D vitest @vitest/ui

# Run tests
pnpm test
```

### Example Test

```typescript
// src/__tests__/auth.test.ts
import { describe, it, expect } from 'vitest';
import { signInUser } from '../auth';

describe('Auth utilities', () => {
  it('should sign in user with valid credentials', async () => {
    const { user, error } = await signInUser('test@example.com', 'password');

    expect(error).toBeNull();
    expect(user).toBeDefined();
  });
});
```

---

## Common Issues & Troubleshooting

### Issue: Apps not picking up package changes

**Solution:** Rebuild the package:
```bash
cd packages/firebase-client
pnpm build
```

### Issue: Type errors in consuming apps

**Solution:** Regenerate type definitions:
```bash
pnpm clean && pnpm build
```

### Issue: Firebase not initialized

**Solution:** Ensure environment variables are set in consuming apps:
```env
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=...
NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
```

### Issue: Multiple Firebase instances

**Solution:** The package uses singleton pattern. Ensure apps import from `@toko/firebase-client` instead of initializing Firebase themselves.

---

## Best Practices

1. **Single Source of Truth**: All apps should import Firebase from this package, never initialize Firebase directly

2. **Error Handling**: All utility functions should handle errors gracefully and return error objects

3. **Type Safety**: Use TypeScript generics for Firestore operations to ensure type safety

4. **Environment Variables**: Use `NEXT_PUBLIC_*` prefix for client-side Firebase config

5. **Build Before Commit**: Always build the package before committing changes

6. **Versioning**: Update package version when making breaking changes

---

## Useful Commands

```bash
# Build package
pnpm build

# Watch mode (development)
pnpm dev

# Type check
pnpm typecheck

# Clean build artifacts
pnpm clean

# Run tests
pnpm test

# Build from project root (builds all packages)
pnpm build --filter @toko/firebase-client
```

---

## Next Steps

1. Review Firebase documentation: https://firebase.google.com/docs
2. Check consuming apps to see usage examples
3. Add new Firebase services as needed (Functions, Analytics, etc.)
4. Write comprehensive tests for all utilities
5. Document all exported functions with JSDoc comments

---

**Last Updated**: 2024-12-13
