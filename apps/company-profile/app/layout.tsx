import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { notFound } from 'next/navigation';
import '@toko/ui-web/styles';
import './globals.css';
import { locales } from '@/i18n/request';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'TOKO ANAK BANGSA - Empowering Indonesian SMEs',
  description: 'Multi-tenant POS & Marketplace Platform for Indonesian Small and Medium Enterprises',
};

export default function RootLayout({
  children,
  params: { locale },
}: Readonly<{
  children: React.ReactNode;
  params: { locale: string };
}>) {
  // Validate that the incoming `locale` parameter is valid
  if (!locales.includes(locale as any)) {
    notFound();
  }

  return (
    <html lang={locale}>
      <body className={inter.className}>{children}</body>
    </html>
  );
}
