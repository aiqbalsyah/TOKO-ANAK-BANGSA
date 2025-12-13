# @toko/firebase-client

Shared Firebase SDK wrapper for TOKO ANAK BANGSA.

## Features

- ✅ Singleton Firebase initialization
- ✅ Automatic emulator detection
- ✅ TypeScript types
- ✅ Re-exports common Firebase functions
- ✅ Tree-shakeable

## Installation

This is a workspace package. It's automatically available to all apps in the monorepo.

```typescript
import { firebaseAuth, firebaseDb, signInWithEmailAndPassword } from '@toko/firebase-client';
```

## Usage

### Authentication

```typescript
import { firebaseAuth, signInWithEmailAndPassword, onAuthStateChanged } from '@toko/firebase-client';

// Sign in
const userCredential = await signInWithEmailAndPassword(
  firebaseAuth,
  'user@example.com',
  'password'
);

// Listen to auth state
onAuthStateChanged(firebaseAuth, (user) => {
  if (user) {
    console.log('User signed in:', user.uid);
  } else {
    console.log('User signed out');
  }
});
```

### Firestore

```typescript
import { firebaseDb, collection, getDocs, addDoc } from '@toko/firebase-client';

// Get documents
const querySnapshot = await getDocs(collection(firebaseDb, 'products'));
querySnapshot.forEach((doc) => {
  console.log(doc.id, doc.data());
});

// Add document
await addDoc(collection(firebaseDb, 'products'), {
  name: 'Indomie Goreng',
  price: 3000,
  createdAt: serverTimestamp(),
});
```

### Storage

```typescript
import { firebaseStorage, ref, uploadBytes, getDownloadURL } from '@toko/firebase-client';

// Upload file
const storageRef = ref(firebaseStorage, 'products/image.jpg');
await uploadBytes(storageRef, file);

// Get download URL
const url = await getDownloadURL(storageRef);
```

### Realtime Database

```typescript
import { firebaseRtdb, rtdbRef, rtdbSet, onValue } from '@toko/firebase-client';

// Write data
await rtdbSet(rtdbRef(firebaseRtdb, 'cart/' + userId), {
  items: [],
  updatedAt: Date.now(),
});

// Listen to data
onValue(rtdbRef(firebaseRtdb, 'cart/' + userId), (snapshot) => {
  const data = snapshot.val();
  console.log('Cart:', data);
});
```

## Environment Variables

Required in `.env.local`:

```bash
# Development Environment
NEXT_PUBLIC_FIREBASE_API_KEY=AIzaSyC68GKzgFvNP7iJ7JLETqGLdZvXZ4F7RHI
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=toko-anak-bangsa-dev.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=toko-anak-bangsa-dev
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=toko-anak-bangsa-dev.firebasestorage.app
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=194271264648
NEXT_PUBLIC_FIREBASE_APP_ID=1:194271264648:web:584d8ae0cd934bc2a3c43d
NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID=G-KGJQ07H709
NEXT_PUBLIC_FIREBASE_DATABASE_URL=https://toko-anak-bangsa-dev.firebaseio.com

# Enable Firebase Emulators (development only)
NEXT_PUBLIC_USE_FIREBASE_EMULATOR=false
```

**Note**: For production, use your production Firebase project credentials.

## Emulator Support

When `NEXT_PUBLIC_USE_FIREBASE_EMULATOR=true`, the package automatically connects to local emulators:

- Auth: `http://localhost:9099`
- Firestore: `localhost:8080`
- Storage: `localhost:9199`
- Realtime Database: `localhost:9000`

## Development

```bash
# Build package
pnpm build

# Watch mode
pnpm dev

# Type check
pnpm typecheck
```

## Exports

### Initialized Instances
- `firebaseApp` - Firebase App instance
- `firebaseAuth` - Auth instance
- `firebaseDb` - Firestore instance
- `firebaseStorage` - Storage instance
- `firebaseRtdb` - Realtime Database instance

### Re-exported Functions
All common Firebase functions are re-exported for convenience. See `src/index.ts` for the full list.
