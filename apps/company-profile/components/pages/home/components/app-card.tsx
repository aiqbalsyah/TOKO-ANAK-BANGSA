import { Button, Card, CardContent, CardDescription, CardHeader, CardTitle } from '@toko/ui-web';
import Link from 'next/link';

interface AppCardProps {
  title: string;
  description: string;
  content: string;
  href: string;
  variant?: 'default' | 'outline' | 'secondary';
}

export function AppCard({ title, description, content, href, variant = 'default' }: AppCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground mb-4">{content}</p>
        <Button asChild variant={variant} className="w-full">
          <Link href={href}>{`Open ${title}`}</Link>
        </Button>
      </CardContent>
    </Card>
  );
}
