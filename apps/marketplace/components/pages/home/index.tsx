import { Card, CardContent, CardDescription, CardHeader, CardTitle, Badge } from '@toko/ui-web';
import { HeroSection } from './components/hero-section';
import { ActionButtons } from './components/action-buttons';
import { EnvironmentInfo } from './components/environment-info';

export function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <Card className="w-full max-w-md">
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle>Marketplace</CardTitle>
            <Badge variant="success">Public</Badge>
          </div>
          <CardDescription>Discover Products from Local SMEs</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <HeroSection />
          <ActionButtons />
          <EnvironmentInfo />
        </CardContent>
      </Card>
    </main>
  );
}
