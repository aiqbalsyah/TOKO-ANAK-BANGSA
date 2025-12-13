import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { notFound } from 'next/navigation';
import '@toko/ui-web/styles';
import './globals.css';
import { ToastProvider, ToastViewport } from '@toko/ui-web';
import { locales } from '@/i18n/request';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Platform Admin - TOKO ANAK BANGSA',
  description: 'Platform administration and management system',
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
      <body className={inter.className}>
        <ToastProvider>
          {children}
          <ToastViewport />
        </ToastProvider>
      </body>
    </html>
  );
}
