'use client';

import { Card, CardContent } from '@toko/ui-web';
import { useAuthState } from './hooks/use-auth-state';
import { WelcomeCard } from './components/welcome-card';
import { AuthStatus } from './components/auth-status';
import { EnvironmentInfo } from './components/environment-info';

export function HomePage() {
  const { user, loading } = useAuthState();

  if (loading) {
    return (
      <main className="flex min-h-screen items-center justify-center p-24">
        <p>Loading...</p>
      </main>
    );
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="w-full max-w-md space-y-4">
        <WelcomeCard />
        <Card>
          <CardContent className="pt-6 space-y-4">
            <AuthStatus user={user} />
            <EnvironmentInfo />
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
