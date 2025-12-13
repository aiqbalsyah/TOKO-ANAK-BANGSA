import { z } from 'zod';

/**
 * User Role (within a tenant)
 */
export const UserRoleSchema = z.enum(['owner', 'admin', 'cashier', 'viewer']);
export type UserRole = z.infer<typeof UserRoleSchema>;

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
 * Tenant Member (User's role and permissions within a specific tenant)
 */
export const TenantMemberSchema = z.object({
  tenantId: z.string().uuid(),
  userId: z.string(),
  role: UserRoleSchema,
  permissions: UserPermissionsSchema,
  joinedAt: z.date(),
  invitedBy: z.string().optional(),
  status: UserStatusSchema.default('active'),
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
  role: UserRoleSchema,
  permissions: UserPermissionsSchema.partial(),
});
export type InviteUserInput = z.infer<typeof InviteUserInputSchema>;

/**
 * Update Tenant Member Input
 */
export const UpdateTenantMemberInputSchema = z.object({
  role: UserRoleSchema.optional(),
  permissions: UserPermissionsSchema.partial().optional(),
  status: UserStatusSchema.optional(),
});
export type UpdateTenantMemberInput = z.infer<typeof UpdateTenantMemberInputSchema>;

/**
 * Helper function to get default permissions by role
 */
export function getDefaultPermissionsByRole(role: UserRole): UserPermissions {
  const basePermissions: UserPermissions = {
    canCreateProducts: false,
    canEditProducts: false,
    canDeleteProducts: false,
    canViewProducts: true,
    canCreateOrders: false,
    canEditOrders: false,
    canDeleteOrders: false,
    canViewOrders: true,
    canRefundOrders: false,
    canManageCustomers: false,
    canViewCustomers: true,
    canManageInventory: false,
    canViewInventory: true,
    canViewReports: false,
    canExportReports: false,
    canManageSettings: false,
    canManageUsers: false,
    canManagePayments: false,
  };

  switch (role) {
    case 'owner':
      return Object.fromEntries(Object.keys(basePermissions).map((key) => [key, true])) as UserPermissions;
    case 'admin':
      return {
        ...basePermissions,
        canCreateProducts: true,
        canEditProducts: true,
        canDeleteProducts: true,
        canCreateOrders: true,
        canEditOrders: true,
        canDeleteOrders: true,
        canRefundOrders: true,
        canManageCustomers: true,
        canManageInventory: true,
        canViewReports: true,
        canExportReports: true,
        canManageUsers: true,
      };
    case 'cashier':
      return {
        ...basePermissions,
        canCreateOrders: true,
        canEditOrders: true,
        canViewReports: true,
        canManageCustomers: true,
      };
    case 'viewer':
      return basePermissions;
    default:
      return basePermissions;
  }
}
