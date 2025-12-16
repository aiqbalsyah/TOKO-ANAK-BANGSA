import { z } from 'zod';
import { UserPermissionsSchema } from './user';

/**
 * System Role IDs (static, predefined)
 * These are platform-wide roles that cannot be modified or deleted
 */
export const SYSTEM_ROLE_IDS = {
  SUPER_ADMIN: 'super_admin', // Platform administrator
  OWNER: 'owner', // Tenant owner
  MEMBER: 'member', // Basic tenant member
} as const;

/**
 * Role Level Constants
 * Higher level = more permissions
 * Custom roles can be 1-89, system roles are 90+
 */
export const ROLE_LEVELS = {
  SUPER_ADMIN: 100,
  OWNER: 90,
  ADMIN: 70,
  MANAGER: 50,
  STAFF: 30,
  VIEWER: 10,
} as const;

/**
 * System Role Schema (static, read-only)
 * These roles are predefined and cannot be modified by users
 */
export const SystemRoleSchema = z.object({
  id: z.string(), // 'super_admin', 'owner', 'member'
  name: z.string(),
  description: z.string(),
  level: z.number().int().min(90).max(100), // System roles are level 90+
  permissions: UserPermissionsSchema,
  isSystemRole: z.literal(true),
  isActive: z.boolean().default(true),
  createdAt: z.date(),
  updatedAt: z.date(),
});
export type SystemRole = z.infer<typeof SystemRoleSchema>;

/**
 * Tenant Role Schema (dynamic, tenant-specific)
 * Custom roles created by tenant owners/admins
 */
export const TenantRoleSchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid(),
  name: z.string().min(1).max(100),
  description: z.string().max(500).optional(),

  // Hierarchy
  level: z.number().int().min(1).max(89), // Custom roles are level 1-89
  inheritsFrom: z.string().optional(), // Parent role ID (system or custom)

  // Permissions (merged with inherited permissions)
  permissions: UserPermissionsSchema,

  // Metadata
  isCustom: z.literal(true),
  isActive: z.boolean().default(true),
  createdBy: z.string(), // User ID who created this role
  createdAt: z.date(),
  updatedAt: z.date(),
});
export type TenantRole = z.infer<typeof TenantRoleSchema>;

/**
 * Combined Role Schema (union of system and tenant roles)
 * Used when querying roles regardless of type
 */
export const RoleSchema = z.union([SystemRoleSchema, TenantRoleSchema]);
export type Role = z.infer<typeof RoleSchema>;

/**
 * Create Tenant Role Input
 */
export const CreateTenantRoleInputSchema = z.object({
  name: z.string().min(1).max(100),
  description: z.string().max(500).optional(),
  level: z.number().int().min(1).max(89),
  inheritsFrom: z.string().optional(),
  permissions: UserPermissionsSchema,
});
export type CreateTenantRoleInput = z.infer<typeof CreateTenantRoleInputSchema>;

/**
 * Update Tenant Role Input
 */
export const UpdateTenantRoleInputSchema = z.object({
  name: z.string().min(1).max(100).optional(),
  description: z.string().max(500).optional(),
  level: z.number().int().min(1).max(89).optional(),
  inheritsFrom: z.string().optional(),
  permissions: UserPermissionsSchema.partial().optional(),
  isActive: z.boolean().optional(),
});
export type UpdateTenantRoleInput = z.infer<typeof UpdateTenantRoleInputSchema>;

/**
 * Role Query Schema (for filtering/searching roles)
 */
export const RoleQuerySchema = z.object({
  tenantId: z.string().uuid().optional(),
  isActive: z.boolean().optional(),
  isCustom: z.boolean().optional(),
  minLevel: z.number().int().min(1).max(100).optional(),
  maxLevel: z.number().int().min(1).max(100).optional(),
  search: z.string().optional(), // Search by name or description
});
export type RoleQuery = z.infer<typeof RoleQuerySchema>;

/**
 * Helper function to get default permissions by system role ID
 */
export function getDefaultPermissionsBySystemRole(roleId: string): typeof UserPermissionsSchema._type {
  const allPermissions = {
    canCreateProducts: true,
    canEditProducts: true,
    canDeleteProducts: true,
    canViewProducts: true,
    canCreateOrders: true,
    canEditOrders: true,
    canDeleteOrders: true,
    canViewOrders: true,
    canRefundOrders: true,
    canManageCustomers: true,
    canViewCustomers: true,
    canManageInventory: true,
    canViewInventory: true,
    canViewReports: true,
    canExportReports: true,
    canManageSettings: true,
    canManageUsers: true,
    canManagePayments: true,
  };

  const basePermissions = {
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

  switch (roleId) {
    case SYSTEM_ROLE_IDS.SUPER_ADMIN:
    case SYSTEM_ROLE_IDS.OWNER:
      return allPermissions;
    case SYSTEM_ROLE_IDS.MEMBER:
      return basePermissions;
    default:
      return basePermissions;
  }
}

/**
 * Helper function to merge permissions from parent role
 * Child role inherits all parent permissions and can add more
 */
export function mergePermissions(
  parentPermissions: typeof UserPermissionsSchema._type,
  childPermissions: Partial<typeof UserPermissionsSchema._type>
): typeof UserPermissionsSchema._type {
  return {
    ...parentPermissions,
    ...childPermissions,
  };
}

/**
 * Helper function to check if user has permission based on role level
 * Higher level roles automatically have permissions of lower level roles
 */
export function hasPermissionByLevel(userLevel: number, requiredLevel: number): boolean {
  return userLevel >= requiredLevel;
}

/**
 * System Role Definitions (seed data)
 * These should be created when initializing the database
 */
export const DEFAULT_SYSTEM_ROLES: Omit<SystemRole, 'createdAt' | 'updatedAt'>[] = [
  {
    id: SYSTEM_ROLE_IDS.SUPER_ADMIN,
    name: 'Super Admin',
    description: 'Platform administrator with full access to all tenants and system settings',
    level: ROLE_LEVELS.SUPER_ADMIN,
    permissions: getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.SUPER_ADMIN),
    isSystemRole: true,
    isActive: true,
  },
  {
    id: SYSTEM_ROLE_IDS.OWNER,
    name: 'Owner',
    description: 'Tenant owner with full access to all tenant features and settings',
    level: ROLE_LEVELS.OWNER,
    permissions: getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.OWNER),
    isSystemRole: true,
    isActive: true,
  },
  {
    id: SYSTEM_ROLE_IDS.MEMBER,
    name: 'Member',
    description: 'Basic tenant member with view-only access',
    level: ROLE_LEVELS.VIEWER,
    permissions: getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.MEMBER),
    isSystemRole: true,
    isActive: true,
  },
];

/**
 * Example Custom Role Templates
 * These can be used as starting points for custom roles
 */
export const ROLE_TEMPLATES = {
  ADMIN: {
    name: 'Admin',
    description: 'Administrator with most permissions except ownership transfer',
    level: ROLE_LEVELS.ADMIN,
    permissions: {
      ...getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.MEMBER),
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
    },
  },
  MANAGER: {
    name: 'Manager',
    description: 'Store manager with product and order management permissions',
    level: ROLE_LEVELS.MANAGER,
    permissions: {
      ...getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.MEMBER),
      canCreateProducts: true,
      canEditProducts: true,
      canCreateOrders: true,
      canEditOrders: true,
      canManageCustomers: true,
      canManageInventory: true,
      canViewReports: true,
    },
  },
  CASHIER: {
    name: 'Cashier',
    description: 'Cashier with order creation and basic customer management',
    level: ROLE_LEVELS.STAFF,
    permissions: {
      ...getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.MEMBER),
      canCreateOrders: true,
      canEditOrders: true,
      canManageCustomers: true,
    },
  },
  INVENTORY_MANAGER: {
    name: 'Inventory Manager',
    description: 'Specialized role for inventory and product management',
    level: ROLE_LEVELS.STAFF,
    permissions: {
      ...getDefaultPermissionsBySystemRole(SYSTEM_ROLE_IDS.MEMBER),
      canCreateProducts: true,
      canEditProducts: true,
      canManageInventory: true,
      canViewReports: true,
    },
  },
} as const;
