import { z } from 'zod';

/**
 * User Status
 */
export const UserStatusSchema = z.enum(['active', 'inactive', 'suspended']);
export type UserStatus = z.infer<typeof UserStatusSchema>;

/**
 * User Permissions (granular permissions)
 */
export const UserPermissionsSchema = z.object({
  // Products
  canCreateProducts: z.boolean().default(false),
  canEditProducts: z.boolean().default(false),
  canDeleteProducts: z.boolean().default(false),
  canViewProducts: z.boolean().default(true),

  // Orders/Sales
  canCreateOrders: z.boolean().default(false),
  canEditOrders: z.boolean().default(false),
  canDeleteOrders: z.boolean().default(false),
  canViewOrders: z.boolean().default(true),
  canRefundOrders: z.boolean().default(false),

  // Customers
  canManageCustomers: z.boolean().default(false),
  canViewCustomers: z.boolean().default(true),

  // Inventory
  canManageInventory: z.boolean().default(false),
  canViewInventory: z.boolean().default(true),

  // Reports
  canViewReports: z.boolean().default(false),
  canExportReports: z.boolean().default(false),

  // Settings
  canManageSettings: z.boolean().default(false),
  canManageUsers: z.boolean().default(false),
  canManagePayments: z.boolean().default(false),
});
export type UserPermissions = z.infer<typeof UserPermissionsSchema>;

/**
 * Tenant Member (User's role assignment within a specific tenant)
 * Roles are now dynamic - roleId references either system_roles or tenant_roles collection
 */
export const TenantMemberSchema = z.object({
  tenantId: z.string().uuid(),
  userId: z.string(),
  roleId: z.string(), // References system_roles/{roleId} or tenant_roles/{roleId}

  // Optional permission overrides for this specific user
  customPermissions: UserPermissionsSchema.partial().optional(),

  // Metadata
  joinedAt: z.date(),
  assignedBy: z.string().optional(),
  status: UserStatusSchema.default('active'),
  expiresAt: z.date().optional(), // Optional role expiration
});
export type TenantMember = z.infer<typeof TenantMemberSchema>;

/**
 * User Profile
 */
export const UserProfileSchema = z.object({
  displayName: z.string().min(1, 'Display name is required'),
  photoURL: z.string().url().optional(),
  phoneNumber: z.string().min(10).optional(),
  bio: z.string().max(500).optional(),
});
export type UserProfile = z.infer<typeof UserProfileSchema>;

/**
 * User Schema
 */
export const UserSchema = z.object({
  id: z.string(), // Firebase Auth UID
  email: z.string().email(),
  emailVerified: z.boolean().default(false),
  profile: UserProfileSchema,

  // Multi-tenant memberships
  tenants: z.array(TenantMemberSchema).default([]),

  // Platform-level status
  status: UserStatusSchema.default('active'),

  // Timestamps
  createdAt: z.date(),
  updatedAt: z.date(),
  lastLoginAt: z.date().optional(),
});
export type User = z.infer<typeof UserSchema>;

/**
 * Create User Input
 */
export const CreateUserInputSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8, 'Password must be at least 8 characters'),
  profile: UserProfileSchema,
});
export type CreateUserInput = z.infer<typeof CreateUserInputSchema>;

/**
 * Update User Profile Input
 */
export const UpdateUserProfileInputSchema = UserProfileSchema.partial();
export type UpdateUserProfileInput = z.infer<typeof UpdateUserProfileInputSchema>;

/**
 * Invite User to Tenant Input
 */
export const InviteUserInputSchema = z.object({
  email: z.string().email(),
  roleId: z.string(), // Reference to role ID (system or custom role)
  customPermissions: UserPermissionsSchema.partial().optional(),
  expiresAt: z.date().optional(),
});
export type InviteUserInput = z.infer<typeof InviteUserInputSchema>;

/**
 * Update Tenant Member Input
 */
export const UpdateTenantMemberInputSchema = z.object({
  roleId: z.string().optional(),
  customPermissions: UserPermissionsSchema.partial().optional(),
  status: UserStatusSchema.optional(),
  expiresAt: z.date().optional(),
});
export type UpdateTenantMemberInput = z.infer<typeof UpdateTenantMemberInputSchema>;
