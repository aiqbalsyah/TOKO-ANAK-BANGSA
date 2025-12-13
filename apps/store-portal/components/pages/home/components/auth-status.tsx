import { Button } from '@toko/ui-web';
import type { User } from 'firebase/auth';

interface AuthStatusProps {
  user: User | null;
}

export function AuthStatus({ user }: AuthStatusProps) {
  if (user) {
    return (
      <div className="space-y-2">
        <p className="text-sm">
          <strong>Email:</strong> {user.email}
        </p>
        <p className="text-sm">
          <strong>User ID:</strong> {user.uid}
        </p>
        <Button variant="outline" className="w-full">
          Go to Dashboard
        </Button>
      </div>
    );
  }

  return (
    <div className="space-y-2">
      <p className="text-sm text-muted-foreground">Not signed in</p>
      <Button className="w-full">Sign In</Button>
    </div>
  );
}
