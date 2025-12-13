'use client';

import { useEffect, useState } from 'react';
import { firebaseAuth, onAuthStateChanged } from '@toko/firebase-client';
import type { User } from 'firebase/auth';

export function useAuthState() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(firebaseAuth, (currentUser) => {
      setUser(currentUser);
      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  return { user, loading };
}
