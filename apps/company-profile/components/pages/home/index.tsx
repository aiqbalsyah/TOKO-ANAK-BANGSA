import { HeroHeader } from './components/hero-header';
import { AppsGrid } from './components/apps-grid';
import { EnvironmentInfo } from './components/environment-info';

export function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="w-full max-w-4xl space-y-8">
        <HeroHeader />
        <AppsGrid />
        <EnvironmentInfo />
      </div>
    </main>
  );
}
