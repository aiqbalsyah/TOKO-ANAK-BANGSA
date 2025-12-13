import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Utility function to merge Tailwind CSS classes with proper precedence
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Format currency to Indonesian Rupiah
 */
export function formatCurrency(amount: number, options?: Intl.NumberFormatOptions): string {
  return new Intl.NumberFormat('id-ID', {
    style: 'currency',
    currency: 'IDR',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
    ...options,
  }).format(amount);
}

/**
 * Format number with thousand separators
 */
export function formatNumber(value: number, options?: Intl.NumberFormatOptions): string {
  return new Intl.NumberFormat('id-ID', options).format(value);
}

/**
 * Format date to Indonesian locale
 */
export function formatDate(date: Date | string, options?: Intl.DateTimeFormatOptions): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  return new Intl.DateTimeFormat('id-ID', {
    dateStyle: 'medium',
    ...options,
  }).format(dateObj);
}

/**
 * Format date and time to Indonesian locale
 */
export function formatDateTime(date: Date | string, options?: Intl.DateTimeFormatOptions): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  return new Intl.DateTimeFormat('id-ID', {
    dateStyle: 'medium',
    timeStyle: 'short',
    ...options,
  }).format(dateObj);
}

/**
 * Truncate text with ellipsis
 */
export function truncate(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength) + '...';
}

/**
 * Generate slug from text
 */
export function slugify(text: string): string {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/**
 * Validate Indonesian phone number
 */
export function isValidPhoneNumber(phone: string): boolean {
  // Indonesian phone numbers: 08xx-xxxx-xxxx or +628xx-xxxx-xxxx
  const phoneRegex = /^(\+62|62|0)[8][1-9][0-9]{6,9}$/;
  const cleanPhone = phone.replace(/[\s-]/g, '');
  return phoneRegex.test(cleanPhone);
}

/**
 * Format Indonesian phone number
 */
export function formatPhoneNumber(phone: string): string {
  const cleanPhone = phone.replace(/[\s-]/g, '');

  if (cleanPhone.startsWith('+62')) {
    return cleanPhone.replace(/(\+62)(\d{3})(\d{4})(\d+)/, '$1 $2-$3-$4');
  } else if (cleanPhone.startsWith('62')) {
    return cleanPhone.replace(/(\d{2})(\d{3})(\d{4})(\d+)/, '+$1 $2-$3-$4');
  } else if (cleanPhone.startsWith('0')) {
    return cleanPhone.replace(/(\d{4})(\d{4})(\d+)/, '$1-$2-$3');
  }

  return phone;
}
