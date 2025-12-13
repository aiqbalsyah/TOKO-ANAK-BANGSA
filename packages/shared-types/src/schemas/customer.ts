import { z } from 'zod';

/**
 * Customer Type
 */
export const CustomerTypeSchema = z.enum(['retail', 'wholesale', 'regular', 'vip']);
export type CustomerType = z.infer<typeof CustomerTypeSchema>;

/**
 * Customer Status
 */
export const CustomerStatusSchema = z.enum(['active', 'inactive', 'blocked']);
export type CustomerStatus = z.infer<typeof CustomerStatusSchema>;

/**
 * Customer Address
 */
export const CustomerAddressSchema = z.object({
  id: z.string().uuid(),
  label: z.string().optional(), // e.g., "Home", "Office", "Warehouse"
  recipientName: z.string().min(1),
  phoneNumber: z.string().min(10),
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
  isDefault: z.boolean().default(false),
  notes: z.string().optional(),
});
export type CustomerAddress = z.infer<typeof CustomerAddressSchema>;

/**
 * Customer Loyalty Points
 */
export const CustomerLoyaltySchema = z.object({
  points: z.number().int().min(0).default(0),
  tier: z.enum(['bronze', 'silver', 'gold', 'platinum']).default('bronze'),
  lifetimeSpent: z.number().min(0).default(0),
  lifetimeOrders: z.number().int().min(0).default(0),
});
export type CustomerLoyalty = z.infer<typeof CustomerLoyaltySchema>;

/**
 * Customer Schema
 */
export const CustomerSchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid(),

  // Basic info
  name: z.string().min(1, 'Customer name is required'),
  email: z.string().email().optional(),
  phoneNumber: z.string().min(10, 'Phone number must be at least 10 digits'),
  alternatePhone: z.string().optional(),

  // Customer type and status
  type: CustomerTypeSchema.default('retail'),
  status: CustomerStatusSchema.default('active'),

  // Additional info
  dateOfBirth: z.date().optional(),
  gender: z.enum(['male', 'female', 'other']).optional(),
  company: z.string().optional(), // For B2B customers
  taxId: z.string().optional(), // NPWP for Indonesian businesses

  // Addresses
  addresses: z.array(CustomerAddressSchema).default([]),
  defaultAddressId: z.string().uuid().optional(),

  // Loyalty and stats
  loyalty: CustomerLoyaltySchema.default({
    points: 0,
    tier: 'bronze',
    lifetimeSpent: 0,
    lifetimeOrders: 0,
  }),

  // Financial
  creditLimit: z.number().min(0).default(0), // For wholesale customers
  currentDebt: z.number().min(0).default(0),

  // Notes
  notes: z.string().optional(),
  internalNotes: z.string().optional(), // Only visible to staff

  // Tags
  tags: z.array(z.string()).default([]),

  // User association (if customer has an account)
  userId: z.string().optional(),

  // Timestamps
  createdAt: z.date(),
  updatedAt: z.date(),
  createdBy: z.string(),
  lastOrderAt: z.date().optional(),
});
export type Customer = z.infer<typeof CustomerSchema>;

/**
 * Create Customer Input
 */
export const CreateCustomerInputSchema = CustomerSchema.omit({
  id: true,
  tenantId: true,
  loyalty: true,
  currentDebt: true,
  createdAt: true,
  updatedAt: true,
  createdBy: true,
  lastOrderAt: true,
}).extend({
  addresses: z.array(CustomerAddressSchema.omit({ id: true })).optional(),
});
export type CreateCustomerInput = z.infer<typeof CreateCustomerInputSchema>;

/**
 * Update Customer Input
 */
export const UpdateCustomerInputSchema = CustomerSchema.partial().omit({
  id: true,
  tenantId: true,
  loyalty: true,
  currentDebt: true,
  createdAt: true,
  updatedAt: true,
  createdBy: true,
  lastOrderAt: true,
});
export type UpdateCustomerInput = z.infer<typeof UpdateCustomerInputSchema>;

/**
 * Add Customer Address Input
 */
export const AddCustomerAddressInputSchema = CustomerAddressSchema.omit({ id: true });
export type AddCustomerAddressInput = z.infer<typeof AddCustomerAddressInputSchema>;

/**
 * Update Customer Address Input
 */
export const UpdateCustomerAddressInputSchema = CustomerAddressSchema.partial().omit({ id: true });
export type UpdateCustomerAddressInput = z.infer<typeof UpdateCustomerAddressInputSchema>;

/**
 * Customer Query/Filter Input
 */
export const CustomerQuerySchema = z.object({
  tenantId: z.string().uuid().optional(),
  type: CustomerTypeSchema.optional(),
  status: CustomerStatusSchema.optional(),
  search: z.string().optional(), // Search by name, email, phone
  tags: z.array(z.string()).optional(),
  hasDebt: z.boolean().optional(),
  loyaltyTier: z.enum(['bronze', 'silver', 'gold', 'platinum']).optional(),
  sortBy: z.enum(['name', 'createdAt', 'lastOrderAt', 'lifetimeSpent']).default('createdAt'),
  sortOrder: z.enum(['asc', 'desc']).default('desc'),
  page: z.number().int().min(1).default(1),
  limit: z.number().int().min(1).max(100).default(20),
});
export type CustomerQuery = z.infer<typeof CustomerQuerySchema>;
