# Inventory Management 📊

**Category**: INVENTORY, STOCK
**Priority**: MUST HAVE (MVP)
**Phase**: 1-2

---

## Overview

Inventory Management provides real-time stock tracking, stock adjustments, low stock alerts, and inventory movement history. The system tracks inventory in base units (PCS) with support for package-based purchases and sales, ensuring accurate stock levels across all operations.

### Why This Matters

- **Stock Accuracy**: Prevent overselling and stockouts
- **Cost Control**: Track inventory value and prevent losses
- **Operational Efficiency**: Automated stock updates from POS and purchases
- **Business Intelligence**: Understand product movement and demand
- **Multi-location**: Support for branch-to-branch transfers (Pro/Enterprise)

---

## Business Requirements

### Primary Goals

1. **Real-time Stock Tracking**: Automatic updates from sales and purchases
2. **Stock Adjustments**: Manual corrections with audit trail
3. **Low Stock Alerts**: Notifications when products need reordering
4. **Stock Transfers**: Move inventory between branches (multi-location)
5. **Inventory Reports**: Stock levels, movement history, valuation
6. **Stock Opname**: Physical count reconciliation

### Problems Solved

- **Overselling**: Real-time stock prevents selling out-of-stock items
- **Stockouts**: Low stock alerts enable proactive reordering
- **Theft/Loss**: Stock adjustments with reason codes track discrepancies
- **Multi-location**: Transfer inventory between branches
- **Valuation**: Track total inventory value for accounting

---

## Features

### 1. Real-time Stock Tracking

**Description**: Automatic stock updates from all transactions.

**Capabilities**:
- Auto-decrease stock on sales (POS and marketplace orders)
- Auto-increase stock on purchases from suppliers
- Track stock by product and variant
- Reserved stock for pending orders
- Available stock calculation (total - reserved)
- Stock by branch (multi-location)

**Stock Calculation**:
```
Available Stock = Total Stock - Reserved Stock

Example:
Total Stock: 500 PCS
Reserved (pending orders): 50 PCS
Available: 450 PCS
```

**User Flow** (Automatic Update):
1. Customer purchases 10 PCS of "Indomie Goreng"
2. POS transaction completed
3. System automatically deducts 10 PCS from stock
4. Stock updated: 500 → 490 PCS
5. If stock drops below threshold, alert triggered

---

### 2. Stock Adjustments

**Description**: Manual stock corrections with reason codes and audit trail.

**Capabilities**:
- Adjust stock up (stock in)
- Adjust stock down (stock out)
- Require reason code for all adjustments
- Optional notes/description
- Audit trail (who, when, why, how much)
- Adjustment history report

**Common Reason Codes**:
- **Damaged**: Product damaged/defective
- **Expired**: Product past expiration date
- **Theft**: Stock loss due to theft
- **Found**: Stock found during count
- **Return to Supplier**: Defective items returned
- **Promotional**: Free samples/giveaways
- **Correction**: Fix counting error

**User Flow** (Stock Adjustment):
1. Staff navigates to Inventory > Stock Adjustment
2. Searches product: "Indomie Goreng"
3. Current stock shown: 500 PCS
4. Selects adjustment type: "Stock Out"
5. Enters quantity: 10 PCS
6. Selects reason: "Damaged"
7. Adds note: "Water damage from roof leak"
8. Confirms adjustment
9. Stock updated: 500 → 490 PCS
10. Adjustment logged in history

---

### 3. Low Stock Alerts

**Description**: Automated notifications when stock drops below threshold.

**Capabilities**:
- Set threshold per product (or use global default)
- Email alerts to owner/staff
- Dashboard notifications (red badge)
- Alert history log
- Suggested reorder quantity
- Snooze alerts temporarily

**Alert Triggers**:
```
Alert When: Available Stock ≤ Low Stock Threshold

Example Product: "Indomie Goreng"
Low Stock Threshold: 100 PCS
Current Stock: 95 PCS
→ Alert Triggered ✓
```

**User Flow**:
1. "Indomie Goreng" sold, stock drops to 95 PCS
2. Threshold is 100 PCS
3. System triggers low stock alert
4. Owner receives email: "Low Stock Alert: Indomie Goreng"
5. Dashboard shows red badge on product
6. Owner reviews and creates purchase order
7. After restock, alert auto-clears

**Business Rules**:
- Alert sent once when crossing threshold
- No repeated alerts until stock rises above threshold then drops again
- Can temporarily snooze alert (7 days)
- Archived products don't trigger alerts

---

### 4. Stock Transfers (Multi-location)

**Description**: Transfer inventory between store branches (Pro/Enterprise).

**Capabilities**:
- Create transfer request from Branch A to Branch B
- Transfer approval workflow
- Track transfer status (pending, in transit, received)
- Transfer history log
- Automatic stock adjustment on both branches

**Transfer Statuses**:
- **Pending**: Transfer created, awaiting approval
- **Approved**: Transfer approved, ready to ship
- **In Transit**: Items shipped, not yet received
- **Received**: Items received, stock updated
- **Cancelled**: Transfer cancelled

**User Flow**:
1. Branch A (Jakarta) has excess stock: 1000 PCS
2. Branch B (Bandung) needs stock: 50 PCS
3. Branch B manager creates transfer request:
   - From: Branch A
   - Product: "Indomie Goreng"
   - Quantity: 200 PCS
4. Branch A manager approves request
5. Status: "In Transit"
6. Physical items shipped to Branch B
7. Branch B receives items, confirms receipt
8. System updates stock:
   - Branch A: 1000 → 800 PCS
   - Branch B: 50 → 250 PCS
9. Transfer completed

---

### 5. Stock Opname (Physical Count)

**Description**: Physical inventory count reconciliation.

**Capabilities**:
- Schedule stock opname (daily, weekly, monthly)
- Print count sheets
- Record physical counts
- Compare system vs physical
- Auto-generate stock adjustments for variances
- Opname history report

**User Flow**:
1. Owner schedules monthly stock opname
2. System generates count sheet (all products + system stock)
3. Staff physically counts each product:
   - "Indomie Goreng": System 500 PCS, Physical 485 PCS
   - "Indomie Soto": System 300 PCS, Physical 305 PCS
4. Staff enters physical counts into system
5. System calculates variances:
   - "Indomie Goreng": -15 PCS (shortage)
   - "Indomie Soto": +5 PCS (surplus)
6. System generates adjustment report
7. Staff reviews and confirms adjustments
8. Stock updated to match physical count
9. Variance report saved for accounting

---

### 6. Inventory Valuation

**Description**: Calculate total inventory value based on cost prices.

**Capabilities**:
- Total inventory value (all products)
- Inventory value by category
- Inventory value by branch
- FIFO/LIFO/Average cost methods
- Inventory aging report
- Dead stock identification

**Calculation**:
```
Inventory Value = Σ (Stock Quantity × Cost Price)

Example:
Product A: 500 PCS × IDR 2,200 = IDR 1,100,000
Product B: 300 PCS × IDR 5,000 = IDR 1,500,000
Product C: 100 PCS × IDR 10,000 = IDR 1,000,000
Total Inventory Value = IDR 3,600,000
```

---

### 7. Inventory Movement History

**Description**: Complete audit trail of all stock movements.

**Capabilities**:
- View all stock movements per product
- Filter by date range, type, branch
- Movement types:
  - Sale (POS/Marketplace)
  - Purchase (Supplier)
  - Adjustment (Manual)
  - Transfer (Between branches)
- Export to CSV/Excel
- Movement summary by period

**User Flow**:
1. Owner views "Indomie Goreng" inventory
2. Clicks "Movement History"
3. System shows all movements:
   - Dec 13, 10:00 - Sale: -10 PCS (490 → 480)
   - Dec 13, 09:30 - Adjustment (Damaged): -5 PCS (495 → 490)
   - Dec 12, 14:00 - Purchase: +100 PCS (395 → 495)
   - Dec 12, 11:00 - Sale: -20 PCS (415 → 395)
4. Owner can filter by date or type
5. Export to Excel for analysis

---

## Use Cases

### Use Case 1: Low Stock Reorder

**Scenario**: "Indomie Goreng" drops below reorder point.

**Steps**:
1. Daily sales reduce stock from 105 to 95 PCS
2. Low stock threshold: 100 PCS
3. System sends email alert to owner
4. Dashboard shows red badge on product
5. Owner reviews alert
6. Owner creates purchase order: 500 PCS from supplier
7. Purchase received, stock updated: 95 → 595 PCS
8. Alert auto-clears (stock above threshold)

---

### Use Case 2: Damaged Stock Adjustment

**Scenario**: 10 boxes of "Indomie Goreng" damaged by water leak.

**Steps**:
1. Staff discovers damage (10 PCS unusable)
2. Staff goes to Inventory > Stock Adjustment
3. Selects product: "Indomie Goreng"
4. Current stock: 500 PCS
5. Adjustment type: Stock Out
6. Quantity: 10 PCS
7. Reason: Damaged
8. Note: "Water damage from roof leak - Row 3"
9. System updates stock: 500 → 490 PCS
10. Adjustment logged for accounting

---

### Use Case 3: Stock Transfer Between Branches

**Scenario**: Jakarta branch has excess, Bandung branch needs stock.

**Steps**:
1. Bandung manager checks stock: 30 PCS (low)
2. Jakarta stock: 800 PCS (excess)
3. Bandung manager creates transfer request:
   - From: Jakarta
   - Product: "Indomie Goreng"
   - Quantity: 200 PCS
4. Jakarta manager receives notification
5. Jakarta manager approves transfer
6. Jakarta warehouse ships 200 PCS to Bandung
7. Status updated: "In Transit"
8. Bandung receives shipment (2 days later)
9. Bandung confirms receipt in system
10. Stock updated:
    - Jakarta: 800 → 600 PCS
    - Bandung: 30 → 230 PCS

---

### Use Case 4: Monthly Stock Opname

**Scenario**: End-of-month physical inventory count.

**Steps**:
1. Owner schedules stock opname: Dec 31, 2024
2. System generates count sheet (500 products)
3. Staff physically counts all products (3 hours)
4. Staff enters counts into system
5. System compares system vs physical:
   - 480 products: Match ✓
   - 15 products: Shortage (-25 total)
   - 5 products: Surplus (+8 total)
6. Staff reviews variances
7. Staff confirms adjustments
8. System updates stock to match physical
9. Variance report generated for owner review
10. Owner investigates significant variances

---

## Business Rules

### Stock Deduction Priority

1. **Sales (POS/Marketplace)**: Immediate deduction
2. **Reserved Stock**: Held for pending orders (24 hours)
3. **Manual Adjustment**: Requires approval (Owner/Admin)

### Negative Stock

- **Default**: Not allowed (configurable in tenant settings)
- **If disabled**: Cannot sell when stock = 0
- **If enabled**: Can sell, stock goes negative (warning shown)

### Low Stock Threshold

- **Per Product**: Can override global setting
- **Global Default**: Set in tenant settings (e.g., 100 PCS)
- **Alert Frequency**: Once per crossing (no spam)

### Stock Transfers

- **Approval Required**: Yes (Branch A manager approval)
- **In-Transit Stock**: Deducted from source, not yet added to destination
- **Failed Transfer**: Can be cancelled, stock returned to source

### Stock Opname

- **Frequency**: Recommended monthly (configurable)
- **Variance Tolerance**: Alert if variance > 5% (configurable)
- **Adjustment Approval**: Large variances require owner approval

---

## Edge Cases

### Reserved Stock Expiration

- **Problem**: Order pending 24 hours, stock reserved
- **Solution**: After 24 hours, release reserved stock
- **Alternative**: Order cancelled, stock immediately released

### Concurrent Sales (Same Product)

- **Problem**: 2 cashiers sell last 10 PCS simultaneously
- **Solution**: First transaction succeeds, second fails (insufficient stock)
- **Prevention**: Real-time stock locking during transaction

### Stock Transfer In Transit Lost

- **Problem**: Shipment lost/damaged during transfer
- **Solution**: Cancel transfer, stock returned to source branch
- **Record**: Log incident for insurance claim

### Variant vs Main Stock Confusion

- **Problem**: Product has variants, staff adjusts main stock (should adjust variant)
- **Solution**: Disable main stock adjustment if variants exist
- **UX**: "This product has variants. Adjust stock per variant."

---

## Future Enhancements

### Advanced Features
- Batch/lot number tracking (for expiry management)
- Serial number tracking (for electronics)
- Automated reorder points (AI-based)
- Stock forecasting (predict demand)
- Barcode-based stock counting (scan-to-count)
- Stock aging analysis (slow-moving items)

### Integration
- Supplier integration (EDI orders)
- Warehouse Management System (WMS)
- Barcode label printing
- RFID tracking

### Reporting
- Stock turn ratio
- Dead stock analysis
- Inventory aging report
- Stock variance trends
- ABC analysis (classify by value)

---

## Success Metrics

- **Stock Accuracy Rate**: % of products with correct stock count
- **Stockout Incidents**: # of times products sold out
- **Low Stock Alert Response Time**: Avg time to reorder after alert
- **Inventory Turnover**: How fast inventory sells
- **Stock Adjustment Frequency**: # of manual adjustments per month

---

## Dependencies

- **Product Management** (03): Product data and pricing
- **POS/Cashier** (05): Automatic stock deduction on sales
- **Supplier & Purchasing** (08): Stock increase from purchases
- **Tenant Management** (02): Multi-branch settings

---

**Last Updated**: 2024-12-13
