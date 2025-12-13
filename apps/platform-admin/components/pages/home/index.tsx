import { Card, CardContent } from '@toko/ui-web';
import { AdminHeader } from './components/admin-header';
import { AdminInfo } from './components/admin-info';
import { AdminActions } from './components/admin-actions';
import { StatsGrid } from './components/stats-grid';
import { EnvironmentInfo } from './components/environment-info';

export function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <Card className="w-full max-w-md">
        <AdminHeader />
        <CardContent className="space-y-4">
          <AdminInfo />
          <AdminActions />
          <StatsGrid />
          <EnvironmentInfo />
        </CardContent>
      </Card>
    </main>
  );
}
