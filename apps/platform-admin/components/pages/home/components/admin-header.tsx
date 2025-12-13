import { CardDescription, CardHeader, CardTitle, Badge } from '@toko/ui-web';

export function AdminHeader() {
  return (
    <CardHeader>
      <div className="flex items-center justify-between">
        <CardTitle>Platform Admin</CardTitle>
        <Badge variant="destructive">Restricted</Badge>
      </div>
      <CardDescription>System Administration & Management</CardDescription>
    </CardHeader>
  );
}
