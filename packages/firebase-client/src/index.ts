/**
 * TOKO ANAK BANGSA - Firebase Client
 * Shared Firebase SDK initialization and helpers
 */

import { initializeApp, getApps, FirebaseApp } from 'firebase/app';
import { getAuth, Auth, connectAuthEmulator } from 'firebase/auth';
import { getFirestore, Firestore, connectFirestoreEmulator } from 'firebase/firestore';
import { getStorage, FirebaseStorage, connectStorageEmulator } from 'firebase/storage';
import { getDatabase, Database, connectDatabaseEmulator } from 'firebase/database';

// Firebase configuration from environment variables
const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
  databaseURL: process.env.NEXT_PUBLIC_FIREBASE_DATABASE_URL,
};

// Check if running in emulator mode
const useEmulator = process.env.NEXT_PUBLIC_USE_FIREBASE_EMULATOR === 'true';

// Initialize Firebase (singleton pattern)
let app: FirebaseApp;
let auth: Auth;
let db: Firestore;
let storage: FirebaseStorage;
let rtdb: Database;

function initializeFirebase() {
  // Only initialize once
  if (getApps().length === 0) {
    app = initializeApp(firebaseConfig);
  } else {
    app = getApps()[0];
  }

  // Initialize services
  auth = getAuth(app);
  db = getFirestore(app);
  storage = getStorage(app);
  rtdb = getDatabase(app);

  // Connect to emulators in development
  if (useEmulator && typeof window !== 'undefined') {
    try {
      connectAuthEmulator(auth, 'http://localhost:9099', { disableWarnings: true });
      connectFirestoreEmulator(db, 'localhost', 8080);
      connectStorageEmulator(storage, 'localhost', 9199);
      connectDatabaseEmulator(rtdb, 'localhost', 9000);
      console.log('✅ Connected to Firebase Emulators');
    } catch (error) {
      console.warn('⚠️ Firebase Emulator connection failed:', error);
    }
  }

  return { app, auth, db, storage, rtdb };
}

// Initialize Firebase on module load
const firebase = initializeFirebase();

// Export initialized instances
export const firebaseApp = firebase.app;
export const firebaseAuth = firebase.auth;
export const firebaseDb = firebase.db;
export const firebaseStorage = firebase.storage;
export const firebaseRtdb = firebase.rtdb;

// Re-export Firebase types for convenience
export type { User } from 'firebase/auth';
export type {
  DocumentData,
  DocumentReference,
  CollectionReference,
  QueryDocumentSnapshot,
  QuerySnapshot,
} from 'firebase/firestore';

// Re-export common Firebase functions
export {
  // Auth
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  sendPasswordResetEmail,
  updateProfile,
  GoogleAuthProvider,
  signInWithPopup,
} from 'firebase/auth';

export {
  // Firestore
  collection,
  doc,
  getDoc,
  getDocs,
  addDoc,
  setDoc,
  updateDoc,
  deleteDoc,
  query,
  where,
  orderBy,
  limit,
  startAfter,
  onSnapshot,
  serverTimestamp,
  Timestamp,
  increment,
  arrayUnion,
  arrayRemove,
} from 'firebase/firestore';

export {
  // Storage
  ref,
  uploadBytes,
  uploadBytesResumable,
  getDownloadURL,
  deleteObject,
  listAll,
} from 'firebase/storage';

export {
  // Realtime Database
  ref as rtdbRef,
  set as rtdbSet,
  get as rtdbGet,
  update as rtdbUpdate,
  remove as rtdbRemove,
  onValue,
  push,
} from 'firebase/database';
