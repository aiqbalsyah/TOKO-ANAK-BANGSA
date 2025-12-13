import { z } from 'zod';

/**
 * Product Status
 */
export const ProductStatusSchema = z.enum(['active', 'inactive', 'out_of_stock', 'discontinued']);
export type ProductStatus = z.infer<typeof ProductStatusSchema>;

/**
 * Product Unit
 */
export const ProductUnitSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1, 'Unit name is required'), // e.g., "pcs", "box", "kg", "liter"
  abbreviation: z.string().min(1), // e.g., "pcs", "box", "kg", "L"
  conversionRate: z.number().min(0).default(1), // Conversion to base unit
  isBaseUnit: z.boolean().default(false),
});
export type ProductUnit = z.infer<typeof ProductUnitSchema>;

/**
 * Product Variant
 */
export const ProductVariantSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1, 'Variant name is required'), // e.g., "Small", "Red", "500ml"
  sku: z.string().optional(),
  barcode: z.string().optional(),

  // Pricing
  purchasePrice: z.number().min(0).default(0),
  sellingPrice: z.number().min(0),
  wholesalePrice: z.number().min(0).optional(),
  minWholesaleQty: z.number().int().min(1).optional(),

  // Stock
  stockQuantity: z.number().int().min(0).default(0),
  lowStockThreshold: z.number().int().min(0).optional(),

  // Additional
  weight: z.number().min(0).optional(), // in grams
  images: z.array(z.string().url()).default([]),
  status: ProductStatusSchema.default('active'),
});
export type ProductVariant = z.infer<typeof ProductVariantSchema>;

/**
 * Product Category
 */
export const ProductCategorySchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid(),
  name: z.string().min(1, 'Category name is required'),
  slug: z.string().min(1),
  description: z.string().optional(),
  parentId: z.string().uuid().optional(), // For subcategories
  image: z.string().url().optional(),
  order: z.number().int().default(0),
  createdAt: z.date(),
  updatedAt: z.date(),
});
export type ProductCategory = z.infer<typeof ProductCategorySchema>;

/**
 * Product Schema
 */
export const ProductSchema = z.object({
  id: z.string().uuid(),
  tenantId: z.string().uuid(),

  // Basic info
  name: z.string().min(1, 'Product name is required'),
  slug: z.string().min(1),
  description: z.string().optional(),
  shortDescription: z.string().max(160).optional(),

  // Categorization
  categoryId: z.string().uuid(),
  categoryName: z.string().optional(), // Denormalized for quick access
  brand: z.string().optional(),
  tags: z.array(z.string()).default([]),

  // Images
  images: z.array(z.string().url()).default([]),
  thumbnail: z.string().url().optional(),

  // Pricing (for products without variants)
  sku: z.string().optional(),
  barcode: z.string().optional(),
  purchasePrice: z.number().min(0).default(0),
  sellingPrice: z.number().min(0).default(0),
  wholesalePrice: z.number().min(0).optional(),
  minWholesaleQty: z.number().int().min(1).optional(),

  // Stock (for products without variants)
  stockQuantity: z.number().int().min(0).default(0),
  lowStockThreshold: z.number().int().min(0).default(10),
  trackInventory: z.boolean().default(true),

  // Units and Variants
  unit: ProductUnitSchema.optional(),
  hasVariants: z.boolean().default(false),
  variants: z.array(ProductVariantSchema).default([]),

  // Additional details
  weight: z.number().min(0).optional(), // in grams
  dimensions: z
    .object({
      length: z.number().min(0),
      width: z.number().min(0),
      height: z.number().min(0),
    })
    .optional(),

  // Marketplace settings
  enableMarketplace: z.boolean().default(true),
  marketplaceDescription: z.string().optional(),

  // SEO
  metaTitle: z.string().optional(),
  metaDescription: z.string().optional(),
  metaKeywords: z.array(z.string()).default([]),

  // Status
  status: ProductStatusSchema.default('active'),
  isFeatured: z.boolean().default(false),

  // Timestamps
  createdAt: z.date(),
  updatedAt: z.date(),
  createdBy: z.string(),
  updatedBy: z.string().optional(),
});
export type Product = z.infer<typeof ProductSchema>;

/**
 * Create Product Input
 */
export const CreateProductInputSchema = ProductSchema.omit({
  id: true,
  tenantId: true,
  categoryName: true,
  createdAt: true,
  updatedAt: true,
  createdBy: true,
  updatedBy: true,
}).extend({
  slug: z.string().optional(), // Auto-generated from name if not provided
});
export type CreateProductInput = z.infer<typeof CreateProductInputSchema>;

/**
 * Update Product Input
 */
export const UpdateProductInputSchema = ProductSchema.partial().omit({
  id: true,
  tenantId: true,
  createdAt: true,
  updatedAt: true,
  createdBy: true,
});
export type UpdateProductInput = z.infer<typeof UpdateProductInputSchema>;

/**
 * Product Filter/Query Input
 */
export const ProductQuerySchema = z.object({
  tenantId: z.string().uuid().optional(),
  categoryId: z.string().uuid().optional(),
  status: ProductStatusSchema.optional(),
  search: z.string().optional(),
  minPrice: z.number().min(0).optional(),
  maxPrice: z.number().min(0).optional(),
  isFeatured: z.boolean().optional(),
  tags: z.array(z.string()).optional(),
  sortBy: z.enum(['name', 'price', 'createdAt', 'updatedAt', 'popularity']).default('createdAt'),
  sortOrder: z.enum(['asc', 'desc']).default('desc'),
  page: z.number().int().min(1).default(1),
  limit: z.number().int().min(1).max(100).default(20),
});
export type ProductQuery = z.infer<typeof ProductQuerySchema>;
