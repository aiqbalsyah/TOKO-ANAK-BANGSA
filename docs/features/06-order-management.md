# Order Management 📋

**Category**: ORDER, FULFILLMENT
**Priority**: MUST HAVE (MVP)
**Phase**: 2

---

## Overview

Order Management handles the complete lifecycle of customer orders from creation to fulfillment, including order status tracking, fulfillment workflow, returns & refunds, and shipping integration. Orders can originate from both in-store POS transactions and online marketplace purchases.

### Why This Matters

- **Unified System**: Single view for POS and marketplace orders
- **Customer Satisfaction**: Track and fulfill orders promptly
- **Operational Efficiency**: Streamlined fulfillment workflow
- **Accountability**: Complete audit trail for all orders
- **Revenue Management**: Returns and refunds handled properly

---

## Business Requirements

### Primary Goals

1. **Order Tracking**: Real-time status for all orders (POS & marketplace)
2. **Fulfillment Workflow**: Pick → Pack → Ship → Deliver process
3. **Returns & Refunds**: Handle customer returns and process refunds
4. **Order Search**: Fast lookup by order number, customer, date
5. **Shipping Integration**: Label generation and tracking (marketplace)
6. **Multi-source**: Support both in-store and online orders

### Problems Solved

- **Order Visibility**: Track all orders in one place
- **Fulfillment Bottlenecks**: Identify and resolve delays
- **Customer Inquiries**: Quick order status lookup
- **Return Processing**: Standardized return workflow
- **Inventory Sync**: Automatic stock updates on order changes

---

## Features

### 1. Order Creation

**Description**: Create orders from POS or marketplace.

**Order Sources**:
- **POS**: In-store transactions (instant completion)
- **Marketplace**: Online orders (pending → fulfilled)
- **Manual**: Admin creates order for customer (phone/WhatsApp)

**Order Information**:
- Order number (auto-generated)
- Customer information
- Order date & time
- Items (products, quantities, prices)
- Payment method & status
- Shipping method & address (marketplace only)
- Order notes

**User Flow** (POS Order):
1. Cashier processes POS transaction
2. Payment completed
3. Receipt printed
4. System creates order with status "Completed"
5. Stock automatically deducted
6. Order appears in order list

**User Flow** (Marketplace Order):
1. Customer places order on marketplace
2. System creates order with status "Pending"
3. Stock reserved (not yet deducted)
4. Owner receives notification
5. Owner reviews and confirms order
6. Status changes to "Confirmed"
7. Fulfillment process begins

---

### 2. Order Status Tracking

**Description**: Track order progress through fulfillment stages.

**Order Status Flow** (Marketplace):
```
Pending → Confirmed → Processing → Packed → Shipped → Delivered → Completed
        ↘ Cancelled
```

**Status Descriptions**:

**Pending**:
- New order from marketplace
- Awaiting store confirmation
- Payment may still be processing
- Stock reserved but not deducted

**Confirmed**:
- Store accepted the order
- Payment confirmed
- Stock deducted from inventory
- Ready for processing

**Processing**:
- Order being prepared
- Picking items from shelves
- Checking product condition
- Preparing for packing

**Packed**:
- Items packed and ready to ship
- Shipping label generated
- Waiting for courier pickup
- Customer notified

**Shipped**:
- Package handed to courier
- Tracking number assigned
- Customer can track shipment
- Estimated delivery date provided

**Delivered**:
- Package delivered to customer
- Confirmation from courier
- Waiting for customer feedback (optional)

**Completed**:
- Order successfully fulfilled
- Customer satisfied
- Final status (cannot be changed)

**Cancelled**:
- Order cancelled by store or customer
- Stock returned to inventory
- Refund processed (if payment received)

---

### 3. Order Fulfillment Workflow

**Description**: Step-by-step process to fulfill marketplace orders.

**Fulfillment Steps**:

**Step 1: Pick**
- Print pick list (items to collect)
- Locate items in warehouse/store
- Check product condition & expiry
- Mark items as picked

**Step 2: Pack**
- Select appropriate packaging
- Pack items securely
- Include invoice/packing slip
- Add promotional materials (optional)
- Mark as packed

**Step 3: Ship**
- Generate shipping label
- Attach label to package
- Hand to courier
- Update tracking number
- Mark as shipped

**Step 4: Confirm Delivery**
- Courier confirms delivery
- Auto-update status to "Delivered"
- Request customer review (optional)
- Complete order

**User Flow**:
1. Owner views "Confirmed" orders
2. Owner clicks "Start Fulfillment"
3. System generates pick list
4. Staff collects items
5. Staff marks items as picked
6. Staff packs items
7. System generates shipping label
8. Staff prints label, attaches to package
9. Courier picks up package
10. Staff enters tracking number
11. Status updated to "Shipped"
12. Customer receives tracking notification

---

### 4. Order Search & Filtering

**Description**: Fast order lookup and filtering.

**Search By**:
- Order number
- Customer name/phone
- Date range
- Product name
- Payment status

**Filter By**:
- Status (all, pending, confirmed, shipped, etc.)
- Source (POS, marketplace, manual)
- Payment method (cash, card, QRIS, transfer)
- Date range (today, this week, this month, custom)
- Branch (multi-location)

**User Flow**:
1. Owner navigates to Orders
2. Selects filter: "Status: Shipped"
3. Selects date: "This Week"
4. System shows 25 orders shipped this week
5. Owner can export to Excel

---

### 5. Returns & Refunds

**Description**: Handle customer returns and process refunds.

**Return Reasons**:
- Product defective/damaged
- Wrong item shipped
- Item not as described
- Customer changed mind (within return period)
- Size/color doesn't fit

**Return Workflow**:

**Step 1: Customer Requests Return**
- Customer contacts store
- Explains reason for return
- Provides order number

**Step 2: Store Reviews Request**
- Owner/staff checks return policy
- Reviews order details
- Approves or rejects return

**Step 3: Product Return**
- Customer ships product back (or brings to store)
- Store receives and inspects product
- Confirms product condition

**Step 4: Process Refund**
- Calculate refund amount
- Deduct restocking fee (if applicable)
- Process refund via original payment method
- Return product to inventory (if resalable)

**Step 5: Complete Return**
- Update order status
- Notify customer of refund
- Close return request

**User Flow**:
1. Customer emails: "Want to return Order #1234"
2. Owner views order: IDR 150,000 (Paid via QRIS)
3. Order date: 5 days ago (within 7-day return period)
4. Owner approves return request
5. Customer ships product back
6. Owner receives product, inspects condition (Good)
7. Owner processes refund: IDR 150,000 to customer e-wallet
8. Owner returns product to inventory (+1 stock)
9. Order status updated: "Returned/Refunded"
10. Customer receives refund notification

**Business Rules**:
- Return period: 7 days from delivery (configurable)
- Product must be unopened/unused
- Original packaging required
- Shipping cost non-refundable (customer pays return shipping)
- Restocking fee: 0-10% (configurable)

---

### 6. Order Notes & Communication

**Description**: Internal notes and customer communication.

**Capabilities**:
- Add internal notes (staff only)
- Customer messages (visible to customer)
- Status update notifications (auto)
- Attach files/photos (damaged product proof)

**User Flow**:
1. Order status: "Packed"
2. Staff adds note: "Customer requested gift wrap - added"
3. Customer cannot see internal note
4. Staff sends message to customer: "Your order is ready for shipping!"
5. Customer receives notification

---

## Use Cases

### Use Case 1: Process Marketplace Order

**Scenario**: Customer orders 3 products online, store fulfills and ships.

**Steps**:
1. Customer places order on marketplace: IDR 250,000
2. System creates order #ORD-001, status: "Pending"
3. Payment processing via Midtrans
4. Payment confirmed
5. System updates status: "Confirmed"
6. Stock reserved (not yet deducted)
7. Owner receives notification
8. Owner clicks "Start Fulfillment"
9. System generates pick list
10. Staff collects 3 products from shelves
11. Staff marks items as "Picked"
12. Stock deducted from inventory
13. Staff packs items securely
14. System generates shipping label (JNE Regular)
15. Staff prints label, attaches to package
16. Staff marks as "Shipped", enters tracking: JNE1234567890
17. Customer receives tracking notification
18. 2 days later: Package delivered
19. Status auto-updates: "Delivered"
20. After 1 day: Status changes to "Completed"

---

### Use Case 2: Cancel Order (Out of Stock)

**Scenario**: Customer orders product, but it's out of stock.

**Steps**:
1. Customer orders "Minyak Goreng 5L": IDR 100,000
2. Order status: "Pending"
3. Owner reviews order
4. Owner checks stock: 0 available
5. Owner clicks "Cancel Order"
6. Owner selects reason: "Out of Stock"
7. Owner adds message: "Sorry, product out of stock. Refund processed."
8. System processes refund: IDR 100,000
9. Status updated: "Cancelled"
10. Customer receives cancellation notification + refund

---

### Use Case 3: Process Return & Refund

**Scenario**: Customer returns damaged product.

**Steps**:
1. Customer receives order, product damaged
2. Customer contacts store via WhatsApp
3. Owner reviews order #ORD-002: IDR 150,000 (delivered 2 days ago)
4. Owner approves return request
5. Customer ships product back to store
6. 3 days later: Store receives return package
7. Owner inspects product: Confirmed damaged
8. Owner clicks "Process Return"
9. Return reason: "Product Defective"
10. Refund amount: Full IDR 150,000
11. Owner processes refund to customer's e-wallet
12. Product marked as "Damaged" (not returned to inventory)
13. Status updated: "Returned/Refunded"
14. Customer receives refund notification

---

## Business Rules

### Order Numbering

- Format: `ORD-{SOURCE}-{DATE}-{COUNTER}`
- Example: `ORD-MKT-20241213-001` (Marketplace)
- Example: `ORD-POS-20241213-045` (POS)
- Sequential per day, resets at midnight

### Order Cancellation

- **Before "Processing"**: Can cancel anytime
- **After "Processing"**: Requires manager approval
- **After "Shipped"**: Cannot cancel (must use return process)
- Refund processed within 24 hours for cancelled orders

### Returns

- Return period: 7 days from delivery (configurable)
- Product categories with no returns (e.g., perishables)
- Return approval required by owner/admin
- Restocking fee (0-10%) configurable

### Stock Management

- **Pending**: Stock reserved (held but not deducted)
- **Confirmed**: Stock deducted from inventory
- **Cancelled**: Reserved stock released
- **Returned**: Stock returned to inventory (if resalable)

---

## Edge Cases

### Order Confirmed But Stock Depleted

- **Problem**: Order confirmed but stock sold in-store meanwhile
- **Solution**: Real-time stock check before confirmation
- **Fallback**: Cancel order, refund customer, apologize

### Partial Fulfillment

- **Problem**: Customer orders 5 items, only 3 in stock
- **Solution**: Allow partial shipment with price adjustment
- **Alternative**: Cancel entire order, suggest alternatives

### Lost/Damaged in Transit

- **Problem**: Package lost or damaged by courier
- **Solution**: File claim with courier, full refund to customer
- **Insurance**: Automatic insurance for orders > IDR 500,000

### Customer Not Home (Delivery Failed)

- **Problem**: Courier cannot deliver, customer not home
- **Solution**: Courier reschedules delivery
- **After 3 attempts**: Package returned to store, customer contacted

---

## Future Enhancements

### Advanced Features
- Automated order routing (nearest branch)
- Order prioritization (VIP customers first)
- Batch fulfillment (multiple orders at once)
- Gift messages and wrapping
- Scheduled delivery (customer picks time slot)

### Integration
- Multi-courier comparison (best rate/time)
- Real-time tracking updates
- Auto-import tracking from courier API
- WhatsApp order notifications
- SMS delivery notifications

### Analytics
- Fulfillment time analysis
- Return rate by product
- Cancellation reasons analysis
- Peak order times
- Average order value trends

---

## Success Metrics

- **Order Fulfillment Time**: Avg time from order to ship
- **On-Time Delivery Rate**: % of orders delivered on time
- **Return Rate**: % of orders returned
- **Cancellation Rate**: % of orders cancelled
- **Customer Satisfaction**: Review scores for fulfillment

---

## Dependencies

- **Product Management** (03): Product catalog
- **Inventory Management** (04): Stock tracking
- **Customer Management** (07): Customer data
- **POS/Cashier** (05): In-store order creation
- **Marketplace** (10): Online order creation

---

**Last Updated**: 2024-12-13
