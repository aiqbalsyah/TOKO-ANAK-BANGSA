import { z } from 'zod';

/**
 * Order Status
 */
export const OrderStatusSchema = z.enum([
  'pending',
  'confirmed',
  'processing',
  'ready',
  'completed',
  'cancelled',
  'refunded',
]);
export type OrderStatus = z.infer<typeof OrderStatusSchema>;

/**
 * Payment Method
 */
export const PaymentMethodSchema = z.enum(['cash', 'debit_card', 'credit_card', 'e_wallet', 'bank_transfer', 'qris']);
export type PaymentMethod = z.infer<typeof PaymentMethodSchema>;

/**
 * Payment Status
 */
export const PaymentStatusSchema = z.enum(['pending', 'paid', 'failed', 'refunded', 'partial']);
export type PaymentStatus = z.infer<typeof PaymentStatusSchema>;

/**
 * Order Type
 */
export const OrderTypeSchema = z.enum(['pos', 'online', 'marketplace', 'wholesale']);
export type OrderType = z.infer<typeof OrderTypeSchema>;

/**
 * Order Line Item (Product in an order)
 */
export const OrderLineItemSchema = z.object({
  id: z.string().uuid(),
  productId: z.string().uuid(),
  productName: z.string(),
  productSku: z.string().optional(),
  variantId: z.string().uuid().optional(),
  variantName: z.string().optional(),

  // Pricing
  unitPrice: z.number().min(0), // Price at the time of order
  quantity: z.number().int().min(1),
  discount: z.number().min(0).default(0), // Discount amount
  discountPercent: z.number().min(0).max(100).default(0),
  tax: z.number().min(0).default(0),
  subtotal: z.number().min(0), // (unitPrice * quantity) - discount + tax

  // Additional
  notes: z.string().optional(),
  thumbnail: z.string().url().optional(),
});
export type OrderLineItem = z.infer<typeof OrderLineItemSchema>;

/**
 * Shipping Address
 */
export const ShippingAddressSchema = z.object({
  recipientName: z.string().min(1),
  phoneNumber: z.string().min(10),
  street: z.string().min(1),
  city: z.string().min(1),
  province: z.string().min(1),
  postalCode: z.string().optional(),
  country: z.string().default('Indonesia'),
  coordinates: z
    .object({
      latitude: z.number().min(-90).max(90),
      longitude: z.number().min(-180).max(180),
    })
    .optional(),
  notes: z.string().optional(),
});
export type ShippingAddress = z.infer<typeof ShippingAddressSchema>;

/**
 * Payment Details
 */
export const PaymentDetailsSchema = z.object({
  method: PaymentMethodSchema,
  status: PaymentStatusSchema,

  // Amount breakdown
  subtotal: z.number().min(0),
  discount: z.number().min(0).default(0),
  tax: z.number().min(0).default(0),
  shippingFee: z.number().min(0).default(0),
  total: z.number().min(0),

  // Payment info
  amountPaid: z.number().min(0).default(0),
  amountDue: z.number().min(0).default(0),
  change: z.number().min(0).default(0), // For cash payments

  // Transaction details
  transactionId: z.string().optional(), // External payment gateway transaction ID
  paidAt: z.date().optional(),
  refundedAt: z.date().optional(),
  refundAmount: z.number().min(0).optional(),
  refundReason: z.string().optional(),
});
export type PaymentDetails = z.infer<typeof PaymentDetailsSchema>;

/**
 * Order Schema
 */
export const OrderSchema = z.object({
  id: z.string().uuid(),
  orderNumber: z.string(), // Human-readable order number (e.g., "ORD-2024-0001")
  tenantId: z.string().uuid(),
  tenantName: z.string(),

  // Customer info
  customerId: z.string().uuid().optional(),
  customerName: z.string().optional(),
  customerEmail: z.string().email().optional(),
  customerPhone: z.string().optional(),

  // Order details
  type: OrderTypeSchema.default('pos'),
  status: OrderStatusSchema.default('pending'),
  items: z.array(OrderLineItemSchema).min(1, 'Order must have at least one item'),

  // Payment
  payment: PaymentDetailsSchema,

  // Shipping (for online/marketplace orders)
  shippingAddress: ShippingAddressSchema.optional(),
  shippingMethod: z.string().optional(),
  trackingNumber: z.string().optional(),

  // Notes and metadata
  notes: z.string().optional(),
  internalNotes: z.string().optional(),
  source: z.string().default('pos'), // pos, marketplace, online_store, etc.

  // Staff info
  createdBy: z.string(), // User ID who created the order
  createdByName: z.string().optional(),
  processedBy: z.string().optional(),
  processedByName: z.string().optional(),

  // Timestamps
  createdAt: z.date(),
  updatedAt: z.date(),
  confirmedAt: z.date().optional(),
  completedAt: z.date().optional(),
  cancelledAt: z.date().optional(),
  cancellationReason: z.string().optional(),
});
export type Order = z.infer<typeof OrderSchema>;

/**
 * Create Order Input
 */
export const CreateOrderInputSchema = z.object({
  customerId: z.string().uuid().optional(),
  customerName: z.string().optional(),
  customerEmail: z.string().email().optional(),
  customerPhone: z.string().optional(),

  type: OrderTypeSchema.default('pos'),
  items: z.array(
    OrderLineItemSchema.omit({ id: true, subtotal: true })
  ).min(1),

  paymentMethod: PaymentMethodSchema,
  discount: z.number().min(0).default(0),
  shippingFee: z.number().min(0).default(0),
  shippingAddress: ShippingAddressSchema.optional(),

  notes: z.string().optional(),
  internalNotes: z.string().optional(),

  amountPaid: z.number().min(0).optional(), // For cash payments
});
export type CreateOrderInput = z.infer<typeof CreateOrderInputSchema>;

/**
 * Update Order Status Input
 */
export const UpdateOrderStatusInputSchema = z.object({
  status: OrderStatusSchema,
  notes: z.string().optional(),
  trackingNumber: z.string().optional(),
  cancellationReason: z.string().optional(),
});
export type UpdateOrderStatusInput = z.infer<typeof UpdateOrderStatusInputSchema>;

/**
 * Process Payment Input
 */
export const ProcessPaymentInputSchema = z.object({
  orderId: z.string().uuid(),
  amountPaid: z.number().min(0),
  paymentMethod: PaymentMethodSchema,
  transactionId: z.string().optional(),
});
export type ProcessPaymentInput = z.infer<typeof ProcessPaymentInputSchema>;

/**
 * Refund Order Input
 */
export const RefundOrderInputSchema = z.object({
  orderId: z.string().uuid(),
  refundAmount: z.number().min(0),
  refundReason: z.string().min(1, 'Refund reason is required'),
  restockItems: z.boolean().default(true),
});
export type RefundOrderInput = z.infer<typeof RefundOrderInputSchema>;

/**
 * Order Query/Filter Input
 */
export const OrderQuerySchema = z.object({
  tenantId: z.string().uuid().optional(),
  customerId: z.string().uuid().optional(),
  status: OrderStatusSchema.optional(),
  type: OrderTypeSchema.optional(),
  paymentStatus: PaymentStatusSchema.optional(),
  search: z.string().optional(), // Search by order number, customer name, etc.
  startDate: z.date().optional(),
  endDate: z.date().optional(),
  sortBy: z.enum(['createdAt', 'updatedAt', 'total', 'orderNumber']).default('createdAt'),
  sortOrder: z.enum(['asc', 'desc']).default('desc'),
  page: z.number().int().min(1).default(1),
  limit: z.number().int().min(1).max(100).default(20),
});
export type OrderQuery = z.infer<typeof OrderQuerySchema>;
