# Supplier & Purchasing 📦

**Category**: PROCUREMENT, ACCOUNTS PAYABLE
**Priority**: MUST HAVE (MVP)
**Phase**: 2

---

## Overview

Supplier & Purchasing Management handles the complete procurement lifecycle from supplier onboarding to purchase order creation, goods receipt, and payment processing. The system tracks accounts payable (AP), manages supplier relationships, and ensures accurate inventory updates from purchases. Indonesian B2B payment terms ("tempo") are fully supported.

### Why This Matters

- **Inventory Replenishment**: Systematic ordering process ensures stock availability
- **Cost Control**: Track purchase costs and negotiate better supplier terms
- **Supplier Relationships**: Maintain good relationships with payment tracking
- **Cash Flow Management**: Monitor accounts payable and payment schedules
- **Inventory Accuracy**: Automatic stock updates on goods receipt
- **Business Intelligence**: Purchase analytics for better decision making

---

## Business Requirements

### Primary Goals

1. **Supplier Database**: Maintain comprehensive supplier contact and payment information
2. **Purchase Orders**: Create and manage purchase orders with approval workflow
3. **Goods Receipt**: Receive stock and update inventory automatically
4. **Accounts Payable**: Track supplier debts and payment schedules
5. **Purchase History**: Analyze purchasing patterns and supplier performance
6. **Purchase Returns**: Handle defective products and returns to supplier
7. **Payment Terms**: Support Indonesian credit terms (Net 30/60/90 days)

### Problems Solved

- **Stock Management**: Prevent stockouts with systematic ordering
- **Payment Tracking**: Never miss supplier payment deadlines
- **Cost Visibility**: Understand true product costs including shipping
- **Supplier Performance**: Track delivery times and product quality
- **Cash Flow**: Plan payments based on due dates
- **Audit Trail**: Complete record of all purchases and payments

---

## Features

### 1. Supplier Management

**Description**: Maintain database of suppliers with contact and payment information.

**Capabilities**:
- Add and edit supplier profiles
- Supplier contact information (name, phone, email, WhatsApp)
- Supplier business information (company name, tax ID/NPWP)
- Supplier bank account details (for payments)
- Supplier address (pickup/delivery location)
- Payment terms per supplier (Net 30/60/90, Cash on Delivery)
- Supplier status (Active/Inactive/Blocked)
- Supplier notes and tags
- Supplier documents (contracts, agreements)

**Supplier Information**:
```
Supplier: PT Indofood Distribusi

Contact Person: Pak Ahmad
Phone: +62812-3456-7890
Email: ahmad@indofood.com
WhatsApp: +62812-3456-7890

Business Info:
Company: PT Indofood Distribusi Nusantara
Tax ID/NPWP: 01.234.567.8-901.000
Address: Jl. Industri No. 123, Jakarta Utara

Bank Account:
Bank: BCA
Account Number: 1234567890
Account Name: PT Indofood Distribusi

Payment Terms: Net 30
Credit Limit: IDR 100,000,000
Current Debt: IDR 15,000,000

Status: Active ✓
```

**User Flow** (Add Supplier):
1. Staff navigates to Suppliers > Add New
2. Fills supplier information:
   - Company name: "PT Indofood"
   - Contact person: "Pak Ahmad"
   - Phone: +62812-3456-7890
   - Email: ahmad@indofood.com
3. Sets payment terms: Net 30
4. Adds bank account details
5. Sets credit limit (optional)
6. Adds notes and tags
7. Saves supplier
8. Supplier available for purchase orders

---

### 2. Purchase Order Creation

**Description**: Create purchase orders to order stock from suppliers.

**Capabilities**:
- Create new purchase order (PO)
- Add multiple products to PO
- Specify quantities and unit prices
- Calculate total with tax
- Add shipping/handling costs
- Set expected delivery date
- PO approval workflow (optional)
- Send PO to supplier (email/WhatsApp)
- PO status tracking (Draft, Sent, Confirmed, Partially Received, Received, Cancelled)

**Purchase Order Information**:
```
Purchase Order #PO-20241213-001

Supplier: PT Indofood
Date: Dec 13, 2024
Expected Delivery: Dec 20, 2024
Payment Terms: Net 30

Items:
1. Indomie Goreng
   Qty: 10 DUS (400 PCS)
   Unit Price: IDR 90,000/DUS
   Subtotal: IDR 900,000

2. Indomie Soto
   Qty: 5 DUS (200 PCS)
   Unit Price: IDR 90,000/DUS
   Subtotal: IDR 450,000

Subtotal: IDR 1,350,000
Shipping: IDR 50,000
Tax (11%): IDR 154,000
Total: IDR 1,554,000

Payment Due: Jan 12, 2025 (Net 30)
Status: Sent
```

**User Flow** (Create PO):
1. Staff navigates to Purchasing > Create PO
2. Selects supplier: "PT Indofood"
3. System loads supplier payment terms: Net 30
4. Staff adds products:
   - Search "Indomie Goreng"
   - Qty: 10 DUS (system converts: 400 PCS)
   - Unit Price: IDR 90,000/DUS
5. Adds more products
6. Adds shipping cost: IDR 50,000
7. Reviews PO total: IDR 1,554,000
8. Sets expected delivery: Dec 20, 2024
9. Saves PO as "Draft"
10. Gets approval from manager (if required)
11. Sends PO to supplier via email
12. PO status: "Sent"
13. Awaits supplier confirmation

**PO Approval Workflow** (Enterprise):
```
PO > IDR 10,000,000 requires approval

1. Staff creates PO: IDR 15,000,000
2. Status: "Pending Approval"
3. Notification sent to Owner/Admin
4. Manager reviews PO
5. Manager approves or rejects
6. If approved: Status → "Approved", can be sent
7. If rejected: Status → "Rejected", staff notified
```

---

### 3. Goods Receipt (Stock In)

**Description**: Receive goods from supplier and update inventory.

**Capabilities**:
- Receive against purchase order
- Record received quantities
- Handle partial receipts (receive some items, rest later)
- Quality inspection notes
- Reject damaged/defective items
- Automatic stock increase
- Update PO status
- Generate goods received note (GRN)
- Barcode scanning for verification

**User Flow** (Full Receipt):
1. Goods arrive from PT Indofood
2. Staff navigates to Purchasing > Receive Goods
3. Selects PO: #PO-20241213-001
4. System shows PO items:
   - Indomie Goreng: Ordered 400 PCS, Received 0 PCS
   - Indomie Soto: Ordered 200 PCS, Received 0 PCS
5. Staff inspects physical goods
6. Staff enters received quantities:
   - Indomie Goreng: 400 PCS ✓
   - Indomie Soto: 200 PCS ✓
7. All items received in good condition
8. Staff confirms receipt
9. System updates:
   - Inventory: Indomie Goreng +400 PCS, Indomie Soto +200 PCS
   - PO Status: "Received"
   - Accounts Payable: Debt to PT Indofood +IDR 1,554,000
   - Payment Due: Jan 12, 2025
10. Goods Received Note (GRN) generated
11. GRN printed/saved

**User Flow** (Partial Receipt):
1. Goods arrive but incomplete shipment
2. Staff selects PO: #PO-20241213-001
3. Staff enters received quantities:
   - Indomie Goreng: 400 PCS ✓ (complete)
   - Indomie Soto: 100 PCS (only half received)
4. Staff adds note: "Supplier short 100 PCS Indomie Soto, will deliver tomorrow"
5. Staff confirms partial receipt
6. System updates:
   - Inventory: Indomie Goreng +400 PCS, Indomie Soto +100 PCS
   - PO Status: "Partially Received"
   - Accounts Payable: Debt +IDR 1,329,000 (prorated)
7. PO remains open for remaining 100 PCS
8. Next day: Remaining 100 PCS received
9. Staff records second receipt: 100 PCS
10. PO Status: "Received" (complete)

**User Flow** (Reject Damaged Items):
1. Staff inspects delivered goods
2. Finds 50 PCS Indomie damaged (wet packaging)
3. Staff enters:
   - Indomie Goreng: Received 350 PCS (accepted)
   - Indomie Goreng: Rejected 50 PCS (damaged)
4. Rejection reason: "Water damage - wet packaging"
5. Photo uploaded as proof
6. System updates:
   - Inventory: +350 PCS (only accepted items)
   - PO Status: "Partially Received"
   - Supplier notified of rejection
7. Supplier ships replacement 50 PCS
8. Replacement received, PO completed

---

### 4. Accounts Payable (Supplier Payments)

**Description**: Track debts to suppliers and process payments.

**Why AP Matters** (Indonesian Context):
Indonesian B2B suppliers commonly offer "tempo" payment terms where store pays after 30/60/90 days. This requires careful tracking to:
- Maintain good supplier relationships (pay on time)
- Manage cash flow (schedule payments)
- Negotiate better terms (pay early, get discount)
- Avoid supply disruption (overdue = supplier stops supplying)

**Capabilities**:
- View all supplier debts (accounts payable)
- Track payment due dates
- Process payments (cash, bank transfer)
- Record partial payments
- Payment allocation to specific POs/invoices
- Overdue payment alerts
- Payment history per supplier
- Early payment discounts (future)

**Accounts Payable Dashboard**:
```
Total Accounts Payable: IDR 45,000,000

Due This Week: IDR 8,500,000
Due This Month: IDR 18,000,000
Overdue: IDR 2,000,000 ⚠️

Top 5 Suppliers by Debt:
1. PT Indofood - IDR 15,000,000 (Due: Dec 20)
2. PT Unilever - IDR 8,500,000 (Due: Dec 15) ⚠️ Due Soon
3. PT Mayora - IDR 7,200,000 (Due: Jan 5)
4. CV Mitra Jaya - IDR 5,800,000 (Due: Dec 28)
5. Toko Grosir ABC - IDR 2,000,000 (Overdue 15 days) ⚠️

Upcoming Payments (Next 7 Days):
- Dec 15: PT Unilever - IDR 8,500,000
- Dec 18: PT Mayora - IDR 3,200,000
- Dec 20: PT Indofood - IDR 15,000,000
Total: IDR 26,700,000
```

**User Flow** (Pay Supplier):
1. Staff navigates to Suppliers > PT Indofood > Payments
2. System shows outstanding invoices:
   ```
   Invoice #INV-001: IDR 1,554,000 (Due: Dec 20) - Not Overdue
   Invoice #INV-002: IDR 2,800,000 (Due: Dec 15) - Due in 2 days
   Invoice #INV-003: IDR 3,200,000 (Due: Dec 10) - Overdue 3 days ⚠️

   Total Debt: IDR 7,554,000
   Overdue: IDR 3,200,000
   ```
3. Owner approves payment: IDR 5,000,000
4. Staff selects payment method: Bank Transfer
5. Staff allocates payment (oldest first):
   - Invoice #INV-003: IDR 3,200,000 → PAID ✓
   - Invoice #INV-002: IDR 1,800,000 (partial)
6. Remaining:
   - Invoice #INV-002: IDR 1,000,000 remaining
   - Invoice #INV-001: IDR 1,554,000 (untouched)
7. Total debt: IDR 2,554,000
8. Payment recorded
9. Bank transfer reference: BCA-20241213-001
10. Payment receipt generated
11. Supplier receives payment confirmation

**Overdue Payment Handling**:

**User Flow**:
1. Invoice #INV-003 (IDR 3.2M) due Dec 10
2. Today: Dec 24 (14 days overdue)
3. System sends alert to owner:
   ```
   ⚠️ OVERDUE PAYMENT ALERT

   Supplier: PT Indofood
   Invoice: #INV-003
   Amount: IDR 3,200,000
   Due Date: Dec 10, 2024
   Overdue: 14 days

   Action Required:
   - Process payment immediately
   - Contact supplier to explain delay
   - Risk: Supplier may stop supplying
   ```
4. Owner processes payment
5. Overdue alert cleared
6. Good supplier relationship maintained

**Business Rules**:
- Payments allocated to oldest invoice first (FIFO)
- Can manually allocate to specific invoices
- Overdue alerts sent at 7, 14, 30 days
- Payment approval required for amounts > IDR 10M (configurable)
- Payment proof (bank receipt) attachment recommended

---

### 5. Purchase History & Analytics

**Description**: Track purchasing patterns and supplier performance.

**Capabilities**:
- View all purchase orders by supplier
- Total purchase value per supplier
- Average order size
- Purchase frequency
- On-time delivery rate
- Product price history (track price changes)
- Best pricing suppliers per product
- Purchase trends analysis

**Supplier Analytics**:
```
Supplier: PT Indofood

Total Purchase Value: IDR 450,000,000 (YTD)
Total Orders: 87 POs
Average Order: IDR 5,172,414
Purchase Frequency: 7.3 times/month
Relationship Since: Jan 2023

Performance:
- On-time Delivery: 92% (80/87 orders)
- Damaged Items: 0.8% (very good)
- Price Stability: Stable (±2% variance)
- Payment Terms: Net 30
- Credit Limit: IDR 100,000,000
- Current Utilization: 15%

Top 5 Products Purchased:
1. Indomie Goreng - 45,000 PCS (IDR 112.5M)
2. Indomie Soto - 32,000 PCS (IDR 80M)
3. Sarimi Goreng - 18,000 PCS (IDR 45M)
4. Pop Mie - 12,000 PCS (IDR 36M)
5. Supermie - 8,500 PCS (IDR 21.25M)
```

**Price Tracking**:
```
Product: Indomie Goreng (Per DUS)

Price History:
- Dec 2024: IDR 90,000/DUS (current)
- Oct 2024: IDR 88,000/DUS (-2.3% change)
- Aug 2024: IDR 85,000/DUS (-3.5% change)
- Jun 2024: IDR 90,000/DUS (same as current)

Supplier Comparison (Current Prices):
1. PT Indofood: IDR 90,000/DUS ⭐ Best Price
2. CV Mitra Jaya: IDR 92,000/DUS (+2.2%)
3. Toko Grosir ABC: IDR 95,000/DUS (+5.5%)

Recommendation: Continue purchasing from PT Indofood
```

---

### 6. Purchase Returns (Return to Supplier)

**Description**: Return defective or wrong products to supplier.

**Capabilities**:
- Create return request
- Link to original purchase order
- Specify return reason
- Upload proof photos
- Track return status (Requested, Approved, Shipped, Refunded)
- Receive credit note or replacement
- Automatic stock adjustment

**Return Reasons**:
- Product defective/damaged
- Wrong product delivered
- Expired or near-expiry products
- Quality not as specified
- Order error (over-delivery)

**User Flow** (Return Defective Products):
1. Staff discovers 50 PCS Indomie damaged (from PO-001)
2. Staff navigates to Purchasing > Returns
3. Creates return request:
   - PO Reference: #PO-20241213-001
   - Product: Indomie Goreng
   - Quantity: 50 PCS
   - Reason: Damaged - wet packaging
   - Photos: [uploaded 3 photos]
4. Sends return request to supplier
5. Supplier approves return
6. Staff ships products back to supplier
7. Status: "Shipped"
8. Supplier receives return
9. Options:
   a) Replacement: Supplier ships 50 new PCS
   b) Credit Note: IDR 112,500 credit for future purchases
10. Staff selects: Replacement
11. Replacement received
12. Stock updated: +50 PCS
13. Return completed

---

### 7. Supplier Credit Terms & Relationships

**Description**: Manage payment terms and supplier relationships.

**Payment Terms**:
```
Common Indonesian B2B Terms:

Cash on Delivery (COD):
- Pay upon delivery
- No credit extended
- Usually for new suppliers or small orders

Net 30:
- Payment due 30 days after invoice date
- Most common for established suppliers
- Example: Invoice Dec 13 → Pay by Jan 12

Net 60:
- Payment due 60 days after invoice
- For very trusted suppliers
- Better cash flow management

Net 90:
- Payment due 90 days after invoice
- Rare, only for strategic suppliers
- Maximum cash flow benefit

2/10 Net 30 (Early Payment Discount):
- 2% discount if paid within 10 days
- Otherwise Net 30
- Example: IDR 1M → Pay IDR 980K if paid by Dec 23
```

**Supplier Negotiation**:

**Use Case**: Negotiate better terms with high-volume supplier

**Steps**:
1. Review purchase data: PT Indofood
2. Total purchases: IDR 450M (YTD)
3. Current terms: Net 30
4. Always pay on time: 100% payment rate
5. Owner contacts supplier
6. Proposal: Extend to Net 60 (better cash flow)
7. Supplier agrees (loyal customer)
8. Update supplier payment terms: Net 60
9. Future orders automatically Net 60
10. Cash flow improvement: Extra 30 days payment time

---

## Use Cases

### Use Case 1: Create Purchase Order

**Scenario**: Stock low on Indomie products, create PO to replenish.

**Steps**:
1. Staff checks inventory: Indomie Goreng at 80 PCS (threshold: 100)
2. Staff creates PO: Suppliers > PT Indofood > New PO
3. Adds products:
   - Indomie Goreng: 20 DUS (800 PCS) @ IDR 90K = IDR 1.8M
   - Indomie Soto: 10 DUS (400 PCS) @ IDR 90K = IDR 900K
4. Subtotal: IDR 2.7M
5. Shipping: IDR 75K (included by supplier if > IDR 2M)
6. Tax (11%): IDR 305,250
7. Total: IDR 3,080,250
8. Expected delivery: Dec 20 (7 days)
9. Payment terms: Net 30 (due Jan 12)
10. Sends PO to supplier via email
11. Supplier confirms: Will deliver Dec 19
12. PO Status: "Confirmed"
13. Staff awaits delivery

---

### Use Case 2: Receive Goods & Update Stock

**Scenario**: Supplier delivers goods, staff receives and updates inventory.

**Steps**:
1. Dec 19: Delivery truck arrives
2. Driver hands invoice: #INV-PT-INDO-001
3. Staff navigates to Purchasing > Receive Goods
4. Selects PO: #PO-20241213-001
5. Physically counts delivered items:
   - Indomie Goreng: 20 DUS (800 PCS) ✓
   - Indomie Soto: 10 DUS (400 PCS) ✓
6. Inspects condition: All good ✓
7. Confirms receipt in system
8. System updates:
   - Inventory: Indomie Goreng 80→880 PCS, Indomie Soto 150→550 PCS
   - Low stock alert cleared ✓
   - AP: Debt to PT Indofood +IDR 3,080,250
   - Payment Due: Jan 12, 2025
9. GRN printed, signed by driver
10. Goods moved to warehouse

---

### Use Case 3: Partial Delivery & Backorder

**Scenario**: Supplier delivers partial order, rest on backorder.

**Steps**:
1. PO: 20 DUS Indomie Goreng, 10 DUS Indomie Soto
2. Delivery arrives with only:
   - 20 DUS Indomie Goreng ✓
   - 5 DUS Indomie Soto (short 5 DUS)
3. Driver explains: Indomie Soto stock shortage, rest next week
4. Staff receives partial:
   - Indomie Goreng: 20 DUS (800 PCS) - FULL
   - Indomie Soto: 5 DUS (200 PCS) - PARTIAL
5. System calculates prorated amount:
   - Original total: IDR 3,080,250
   - Delivered value: IDR 2,305,188 (prorated)
6. Inventory updated: +800 PCS Goreng, +200 PCS Soto
7. AP: Debt +IDR 2,305,188 (not full amount)
8. PO Status: "Partially Received"
9. Dec 26: Remaining 5 DUS Soto delivered
10. Second receipt recorded: +200 PCS
11. AP: Debt +IDR 775,062 (balance)
12. PO Status: "Received" (complete)

---

### Use Case 4: Return Damaged Goods

**Scenario**: Received products are damaged, return to supplier.

**Steps**:
1. Staff unpacks Indomie delivery
2. Discovers 3 DUS (120 PCS) with water damage
3. Staff creates return:
   - PO: #PO-20241213-001
   - Product: Indomie Goreng
   - Qty: 3 DUS (120 PCS)
   - Reason: Water damage
   - Photos: [3 images uploaded]
4. Sends return request to supplier
5. Supplier reviews photos
6. Supplier approves return
7. Supplier courier picks up damaged goods
8. Options presented:
   a) Replacement: Ship 3 new DUS
   b) Credit Note: IDR 270K credit
9. Store chooses: Replacement
10. 2 days later: Replacement delivered
11. Staff receives: 3 DUS (120 PCS) ✓
12. Stock updated: +120 PCS
13. Return completed, no cost impact

---

### Use Case 5: Pay Supplier Debt

**Scenario**: Payment due date approaching, process payment to supplier.

**Steps**:
1. Dec 18: System shows upcoming payment
   ```
   ⏰ PAYMENT DUE SOON

   Supplier: PT Indofood
   Amount: IDR 8,500,000
   Due Date: Dec 20, 2024 (2 days)
   ```
2. Owner reviews cash flow: Sufficient ✓
3. Owner approves payment
4. Finance staff processes bank transfer:
   - Amount: IDR 8,500,000
   - To: PT Indofood (BCA 1234567890)
   - Reference: Payment PO-20241213-001
5. Bank transfer completed
6. Staff records payment in system:
   - Date: Dec 18
   - Method: Bank Transfer
   - Reference: BCA-20241218-001
   - Receipt uploaded
7. System updates:
   - AP reduced: IDR 8.5M
   - Invoice marked PAID ✓
   - Payment history updated
8. Email sent to supplier: "Payment processed"
9. Good supplier relationship maintained ✓

---

## Business Rules

### Purchase Orders

- PO number auto-generated: `PO-{DATE}-{COUNTER}`
- PO > IDR 10,000,000 requires approval (configurable)
- PO can be edited in "Draft" status only
- Once sent, PO requires supplier confirmation to modify
- Cancelled POs do not affect inventory or AP

### Goods Receipt

- Must receive against a PO (no direct stock entry)
- Partial receipts allowed
- Can receive more than ordered (if agreed with supplier)
- Stock updated only on confirmed receipt
- Receipt date affects cost calculation (FIFO/LIFO)

### Accounts Payable

- Payment terms set per supplier (default: Net 30)
- Payments allocated to oldest invoice first (FIFO)
- Can manually allocate to specific invoices
- Overdue alerts at 7, 14, 30 days
- Cannot delete supplier with outstanding debt

### Supplier Management

- Supplier code/ID unique per tenant
- Tax ID/NPWP required for official tax invoices
- Inactive suppliers hidden from PO creation
- Blocked suppliers cannot receive new POs
- Supplier performance tracked automatically

---

## Edge Cases

### PO Created But Supplier Confirms Different Quantity

- **Problem**: PO for 10 DUS, supplier can only supply 7 DUS
- **Solution**: Update PO quantity, recalculate total, resend for confirmation
- **Alternative**: Keep original PO, receive partial, create new PO for balance

### Receive More Than Ordered

- **Problem**: PO for 10 DUS, supplier delivers 12 DUS
- **Solution**: Allow over-receipt with approval, adjust invoice amount
- **UX**: "Received 12 DUS > Ordered 10 DUS. Accept extra 2 DUS? Cost will increase."

### Supplier Price Changed After PO Sent

- **Problem**: PO at IDR 90K/DUS, invoice shows IDR 95K/DUS
- **Solution**: Flag discrepancy, require approval to receive
- **UX**: "Price mismatch: PO IDR 90K, Invoice IDR 95K (+5.5%). Approve to continue?"

### Payment Made But Not Recorded

- **Problem**: Finance paid supplier outside system
- **Solution**: Manual payment entry with proof upload
- **Audit**: Log who entered, when, with receipt required

### Supplier Delivers Wrong Product

- **Problem**: Ordered Indomie Goreng, received Indomie Soto
- **Solution**: Reject receipt, create return, supplier ships correct product
- **Stock**: No stock update until correct product received

---

## Future Enhancements

### Advanced Features
- Automated reorder points (AI-based demand forecasting)
- Supplier performance scoring (quality, delivery, pricing)
- Purchase requisitions (staff requests, manager approves)
- Blanket POs (ongoing orders, recurring deliveries)
- Drop shipping (supplier ships direct to customer)
- Consignment inventory (stock owned by supplier until sold)

### Integration
- Supplier EDI integration (electronic PO submission)
- Email parsing (auto-create PO from supplier emails)
- WhatsApp ordering (send PO via WhatsApp)
- Accounting software integration (AP sync)
- Payment gateway (direct supplier payment online)

### Analytics
- Supplier comparison reports (best pricing, delivery, quality)
- Purchase forecasting (predict future needs)
- Seasonal buying analysis
- ABC analysis (classify suppliers by value)
- Cost trend analysis (identify price increases)

---

## Success Metrics

- **PO Cycle Time**: Avg time from PO creation to goods receipt
- **Supplier On-time Delivery**: % of orders delivered on time
- **Purchase Order Accuracy**: % of POs received without discrepancies
- **Payment Timeliness**: % of supplier payments made on time
- **Stock Availability**: % of time products are in stock
- **Cost Variance**: Difference between PO price and invoice price
- **Supplier Retention**: % of suppliers active > 1 year

---

## Dependencies

- **Product Management** (03): Product catalog for PO items
- **Inventory Management** (04): Stock updates on goods receipt
- **Tenant Management** (02): Supplier scoped to tenant
- **Financial Management** (09): AP tracking and payment processing

---

**Last Updated**: 2024-12-13
