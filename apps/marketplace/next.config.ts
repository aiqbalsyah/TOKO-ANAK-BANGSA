import type { NextConfig } from 'next';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./i18n/request.ts');

const nextConfig: NextConfig = {
  reactStrictMode: true,
  transpilePackages: ['@toko/ui-web', '@toko/firebase-client', '@toko/shared-types'],

  env: {
    NEXT_PUBLIC_APP_NAME: 'Marketplace',
    NEXT_PUBLIC_APP_VERSION: '1.0.0',
  },

  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'firebasestorage.googleapis.com',
      },
      {
        protocol: 'https',
        hostname: '**.firebasestorage.app',
      },
    ],
  },
};

export default withNextIntl(nextConfig);
