import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@toko/ui-web';

export function WelcomeCard() {
  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <CardTitle>Store Portal</CardTitle>
        <CardDescription>POS & Store Management System</CardDescription>
      </CardHeader>
      <CardContent>
        <div>
          <h2 className="text-lg font-semibold">TOKO ANAK BANGSA</h2>
          <p className="text-sm text-muted-foreground">
            Multi-tenant POS & Marketplace Platform for Indonesian SMEs
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
