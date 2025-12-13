import createMiddleware from 'next-intl/middleware';
import { locales, defaultLocale } from './i18n/request';

export default createMiddleware({
  // A list of all locales that are supported
  locales,

  // Used when no locale matches
  defaultLocale,

  // Always use a locale prefix (e.g., /en or /id)
  localePrefix: 'always',
});

export const config = {
  // Match only internationalized pathnames
  matcher: ['/', '/(id|en)/:path*'],
};
