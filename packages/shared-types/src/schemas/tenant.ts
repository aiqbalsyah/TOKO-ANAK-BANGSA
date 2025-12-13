import { z } from 'zod';

/**
 * Tenant Status
 */
export const TenantStatusSchema = z.enum(['active', 'suspended', 'pending', 'closed']);
export type TenantStatus = z.infer<typeof TenantStatusSchema>;

/**
 * Tenant Subscription Plan
 */
export const SubscriptionPlanSchema = z.enum(['free', 'basic', 'professional', 'enterprise']);
export type SubscriptionPlan = z.infer<typeof SubscriptionPlanSchema>;

/**
 * Business Type
 */
export const BusinessTypeSchema = z.enum([
  'retail',
  'wholesale',
  'restaurant',
  'cafe',
  'grocery',
  'pharmacy',
  'electronics',
  'fashion',
  'other',
]);
export type BusinessType = z.infer<typeof BusinessTypeSchema>;

/**
 * Store Address
 */
export const StoreAddressSchema = z.object({
  street: z.string().min(1, 'Street address is required'),
  city: z.string().min(1, 'City is required'),
  province: z.string().min(1, 'Province is required'),
  postalCode: z.string().optional(),
  country: z.string().default('Indonesia'),
  coordinates: z
    .object({
      latitude: z.number().min(-90).max(90),
      longitude: z.number().min(-180).max(180),
    })
    .optional(),
});
export type StoreAddress = z.infer<typeof StoreAddressSchema>;

/**
 * Tenant Settings
 */
export const TenantSettingsSchema = z.object({
  currency: z.string().default('IDR'),
  timezone: z.string().default('Asia/Jakarta'),
  language: z.string().default('id'),
  taxEnabled: z.boolean().default(true),
  taxRate: z.number().min(0).max(100).default(11), // PPN 11% in Indonesia
  lowStockThreshold: z.number().int().min(0).default(10),
  enableMarketplace: z.boolean().default(true),
  enableOnlineOrdering: z.boolean().default(false),
});
export type TenantSettings = z.infer<typeof TenantSettingsSchema>;

/**
 * Tenant/Store Schema
 */
export const TenantSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(3, 'Store name must be at least 3 characters'),
  slug: z
    .string()
    .min(3)
    .regex(/^[a-z0-9-]+$/, 'Slug must contain only lowercase letters, numbers, and hyphens'),
  description: z.string().optional(),
  businessType: BusinessTypeSchema,
  ownerId: z.string(),
  ownerName: z.string(),
  ownerEmail: z.string().email(),
  ownerPhone: z.string().min(10, 'Phone number must be at least 10 digits'),

  // Store details
  logo: z.string().url().optional(),
  banner: z.string().url().optional(),
  address: StoreAddressSchema,

  // Settings
  settings: TenantSettingsSchema,

  // Subscription
  subscriptionPlan: SubscriptionPlanSchema.default('free'),
  subscriptionExpiresAt: z.date().optional(),

  // Status
  status: TenantStatusSchema.default('pending'),
  verifiedAt: z.date().optional(),

  // Timestamps
  createdAt: z.date(),
  updatedAt: z.date(),
});
export type Tenant = z.infer<typeof TenantSchema>;

/**
 * Create Tenant Input (for API)
 */
export const CreateTenantInputSchema = TenantSchema.omit({
  id: true,
  createdAt: true,
  updatedAt: true,
  status: true,
  verifiedAt: true,
}).extend({
  slug: z
    .string()
    .min(3)
    .regex(/^[a-z0-9-]+$/)
    .optional(), // Auto-generated from name if not provided
  settings: TenantSettingsSchema.partial(),
});
export type CreateTenantInput = z.infer<typeof CreateTenantInputSchema>;

/**
 * Update Tenant Input (for API)
 */
export const UpdateTenantInputSchema = TenantSchema.partial().omit({
  id: true,
  ownerId: true,
  createdAt: true,
  updatedAt: true,
});
export type UpdateTenantInput = z.infer<typeof UpdateTenantInputSchema>;
