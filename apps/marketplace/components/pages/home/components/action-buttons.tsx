import { Button } from '@toko/ui-web';

export function ActionButtons() {
  return (
    <div className="space-y-2">
      <Button className="w-full">Explore Products</Button>
      <Button variant="outline" className="w-full">
        Browse Stores
      </Button>
    </div>
  );
}
