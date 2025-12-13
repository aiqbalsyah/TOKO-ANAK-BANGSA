import { AppCard } from './app-card';

const apps = [
  {
    title: 'Store Portal',
    description: 'Manage your store operations',
    content: 'Complete POS system for daily sales, inventory, and customer management',
    href: 'http://localhost:3000',
    variant: 'default' as const,
  },
  {
    title: 'Marketplace',
    description: 'Sell to customers nationwide',
    content: 'Reach millions of customers through our online marketplace',
    href: 'http://localhost:3001',
    variant: 'outline' as const,
  },
  {
    title: 'Platform Admin',
    description: 'Platform management',
    content: 'Manage tenants, monitor system health, and configure settings',
    href: 'http://localhost:3003',
    variant: 'secondary' as const,
  },
];

export function AppsGrid() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {apps.map((app) => (
        <AppCard key={app.title} {...app} />
      ))}
    </div>
  );
}
