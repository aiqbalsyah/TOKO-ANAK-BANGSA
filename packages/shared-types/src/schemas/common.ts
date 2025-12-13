import { z } from 'zod';

/**
 * Pagination Metadata
 */
export const PaginationMetaSchema = z.object({
  page: z.number().int().min(1),
  limit: z.number().int().min(1),
  total: z.number().int().min(0),
  totalPages: z.number().int().min(0),
  hasNext: z.boolean(),
  hasPrev: z.boolean(),
});
export type PaginationMeta = z.infer<typeof PaginationMetaSchema>;

/**
 * Paginated Response
 */
export function PaginatedResponseSchema<T extends z.ZodTypeAny>(dataSchema: T) {
  return z.object({
    data: z.array(dataSchema),
    meta: PaginationMetaSchema,
  });
}

/**
 * API Response (Generic)
 */
export function ApiResponseSchema<T extends z.ZodTypeAny>(dataSchema: T) {
  return z.object({
    success: z.boolean(),
    data: dataSchema.optional(),
    error: z
      .object({
        code: z.string(),
        message: z.string(),
        details: z.any().optional(),
      })
      .optional(),
    timestamp: z.date().default(() => new Date()),
  });
}

/**
 * Error Response
 */
export const ErrorResponseSchema = z.object({
  success: z.literal(false),
  error: z.object({
    code: z.string(),
    message: z.string(),
    details: z.any().optional(),
  }),
  timestamp: z.date().default(() => new Date()),
});
export type ErrorResponse = z.infer<typeof ErrorResponseSchema>;

/**
 * Success Response
 */
export function SuccessResponseSchema<T extends z.ZodTypeAny>(dataSchema: T) {
  return z.object({
    success: z.literal(true),
    data: dataSchema,
    timestamp: z.date().default(() => new Date()),
  });
}

/**
 * ID Parameter
 */
export const IdParamSchema = z.object({
  id: z.string().uuid('Invalid ID format'),
});
export type IdParam = z.infer<typeof IdParamSchema>;

/**
 * Slug Parameter
 */
export const SlugParamSchema = z.object({
  slug: z.string().min(1),
});
export type SlugParam = z.infer<typeof SlugParamSchema>;

/**
 * Date Range Filter
 */
export const DateRangeSchema = z.object({
  startDate: z.date().optional(),
  endDate: z.date().optional(),
});
export type DateRange = z.infer<typeof DateRangeSchema>;

/**
 * Sort Options
 */
export const SortSchema = z.object({
  sortBy: z.string().default('createdAt'),
  sortOrder: z.enum(['asc', 'desc']).default('desc'),
});
export type Sort = z.infer<typeof SortSchema>;

/**
 * File Upload
 */
export const FileUploadSchema = z.object({
  filename: z.string().min(1),
  mimetype: z.string().min(1),
  size: z.number().int().min(1),
  url: z.string().url(),
  path: z.string().optional(),
});
export type FileUpload = z.infer<typeof FileUploadSchema>;

/**
 * Image Upload
 */
export const ImageUploadSchema = FileUploadSchema.extend({
  mimetype: z.string().regex(/^image\/(jpeg|png|gif|webp|svg\+xml)$/),
  width: z.number().int().min(1).optional(),
  height: z.number().int().min(1).optional(),
  thumbnail: z.string().url().optional(),
});
export type ImageUpload = z.infer<typeof ImageUploadSchema>;

/**
 * Audit Log Entry
 */
export const AuditLogSchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid(),
  userId: z.string(),
  userName: z.string().optional(),
  action: z.string(), // e.g., "create", "update", "delete"
  resource: z.string(), // e.g., "product", "order", "customer"
  resourceId: z.string(),
  changes: z.any().optional(), // Object showing what changed
  metadata: z.record(z.any()).optional(),
  ipAddress: z.string().optional(),
  userAgent: z.string().optional(),
  createdAt: z.date(),
});
export type AuditLog = z.infer<typeof AuditLogSchema>;

/**
 * Notification
 */
export const NotificationSchema = z.object({
  id: z.string().uuid(),
  userId: z.string(),
  tenantId: z.string().uuid().optional(),

  type: z.enum(['info', 'success', 'warning', 'error']),
  title: z.string().min(1),
  message: z.string().min(1),

  read: z.boolean().default(false),
  readAt: z.date().optional(),

  actionUrl: z.string().url().optional(),
  actionLabel: z.string().optional(),

  metadata: z.record(z.any()).optional(),

  createdAt: z.date(),
  expiresAt: z.date().optional(),
});
export type Notification = z.infer<typeof NotificationSchema>;

/**
 * Activity Log (simplified audit log for UI)
 */
export const ActivityLogSchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid(),
  userId: z.string(),
  userName: z.string(),
  userAvatar: z.string().url().optional(),

  action: z.string(),
  description: z.string(),
  resourceType: z.string().optional(),
  resourceId: z.string().optional(),

  createdAt: z.date(),
});
export type ActivityLog = z.infer<typeof ActivityLogSchema>;

/**
 * Settings (Generic Key-Value Store)
 */
export const SettingsSchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid().optional(), // Optional for platform-wide settings
  key: z.string().min(1),
  value: z.any(),
  type: z.enum(['string', 'number', 'boolean', 'json', 'array']),
  description: z.string().optional(),
  isPublic: z.boolean().default(false),
  updatedAt: z.date(),
  updatedBy: z.string(),
});
export type Settings = z.infer<typeof SettingsSchema>;
