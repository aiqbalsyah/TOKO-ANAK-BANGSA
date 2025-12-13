import { Button } from '@toko/ui-web';

export function AdminActions() {
  return (
    <div className="space-y-2">
      <Button className="w-full">Sign In as Admin</Button>
      <Button variant="outline" className="w-full">
        View System Status
      </Button>
    </div>
  );
}
