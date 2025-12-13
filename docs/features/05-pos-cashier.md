# POS / Cashier 💰

**Category**: POS, CASHIER, PAYMENT
**Priority**: MUST HAVE (MVP)
**Phase**: 1

---

## Overview

The Point of Sale (POS) system enables cashiers to process in-store transactions quickly and efficiently. It supports product search by name/SKU/barcode, multi-tier pricing based on customer type, multiple payment methods (cash, card, digital wallet), and receipt generation. The POS is optimized for speed and ease of use.

### Why This Matters

- **Revenue Generation**: Core system for processing in-store sales
- **Customer Experience**: Fast checkout improves customer satisfaction
- **Operational Efficiency**: Barcode scanning and shortcuts speed up transactions
- **Accuracy**: Automated calculations reduce errors
- **Flexibility**: Support for Indonesian payment methods and pricing tiers

---

## Business Requirements

### Primary Goals

1. **Fast Transaction Processing**: Quick product lookup and checkout
2. **Multi-tier Pricing**: Apply correct price tier (A/B/C) based on customer
3. **Payment Flexibility**: Support cash, card, QRIS, and split payments
4. **Receipt Generation**: Print thermal receipts instantly
5. **Offline Support**: Queue transactions when internet down (Pro+)
6. **Customer Linking**: Associate transactions with customer accounts

### Problems Solved

- **Slow Checkout**: Barcode scanning and keyboard shortcuts speed up process
- **Pricing Errors**: Automatic tier-based pricing prevents mistakes
- **Payment Complexity**: Support for multiple Indonesian payment methods
- **Customer Service**: Quick search and product information access
- **Accountability**: Track which cashier processed each transaction

---

## Features

### 1. Product Search & Selection

**Description**: Fast product lookup for adding to cart.

**Search Methods**:
- **Barcode Scan**: Fastest method, instant product add
- **Text Search**: Type product name/SKU
- **Category Browse**: Navigate by category
- **Favorites**: Quick access to frequently sold products

**User Flow** (Barcode Scan):
1. Customer brings product to counter
2. Cashier scans barcode with scanner
3. Product instantly added to cart
4. Price shown based on customer tier
5. Quantity defaults to 1 (can be changed)

**User Flow** (Text Search):
1. Cashier clicks search box (or presses F2)
2. Cashier types "indo"
3. Autocomplete shows matching products
4. Cashier selects "Indomie Goreng"
5. Product added to cart

**Keyboard Shortcuts**:
- `F2`: Focus search box
- `F3`: Customer lookup
- `F4`: Apply discount
- `F9`: Hold transaction
- `F12`: Complete payment
- `ESC`: Clear cart

---

### 2. Cart Management

**Description**: Add, remove, and modify items in transaction cart.

**Capabilities**:
- Add products to cart
- Change quantity (+ / - buttons or keyboard)
- Remove individual items
- Clear entire cart
- Apply item-level discounts
- Apply cart-level discounts
- Add transaction notes

**Cart Display**:
```
╔═══════════════════════════════════════════════════════╗
║ CART                                                  ║
╠═══════════════════════════════════════════════════════╣
║ Indomie Goreng                              IDR 3,000 ║
║ Qty: 10 PCS                       Sub: IDR 30,000 ║
║ [Remove]                                              ║
╠═══════════════════════════════════════════════════════╣
║ Indomie Soto                                IDR 3,000 ║
║ Qty: 5 PCS                        Sub: IDR 15,000 ║
║ [Remove]                                              ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║ Subtotal:                               IDR 45,000 ║
║ Discount:                                IDR 5,000 ║
║ Tax (11%):                               IDR 4,400 ║
║ ───────────────────────────────────────────────────── ║
║ TOTAL:                                  IDR 44,400 ║
╚═══════════════════════════════════════════════════════╝
```

---

### 3. Multi-tier Pricing (Customer-based)

**Description**: Automatically apply correct price tier based on customer type.

**Price Tiers**:
- **Tier A (Grosir)**: For wholesale customers
- **Tier B (Eceran)**: For retail/walk-in customers (default)
- **Tier C (Premium)**: For VIP/premium customers

**User Flow**:
1. Cashier starts new transaction
2. Default customer: "Unknown" (Tier B pricing)
3. Cashier scans product: "Indomie Goreng"
4. Price shown: IDR 3,000 (Tier B)
5. Cashier looks up customer: "Toko Makmur"
6. Customer type: Wholesale (Tier A)
7. Price auto-updates: IDR 3,000 → IDR 2,500
8. All cart items repriced to Tier A

**Business Rules**:
- Unknown customer = Tier B (default)
- Customer tier cannot be changed mid-transaction
- Price override requires manager approval (optional setting)

---

### 4. Payment Processing

**Description**: Support for multiple Indonesian payment methods.

**Payment Methods**:

**Cash**:
- Enter cash amount received
- Auto-calculate change
- Suggest denominations for change
- Open cash drawer (if connected)

**Card (Debit/Credit)**:
- Manual entry or EDC terminal
- Card payment reference number
- Card type (Visa, MasterCard, etc.)

**QRIS (Digital Wallet)**:
- Display QRIS code
- Customer scans with GoPay/OVO/Dana/ShopeePay
- Wait for payment confirmation
- Auto-complete transaction on success

**Bank Transfer**:
- Virtual account number
- Manual verification by cashier
- Payment proof upload (optional)

**Split Payment** (Enterprise):
- Combine multiple payment methods
- Example: IDR 25,000 cash + IDR 19,400 QRIS

**User Flow** (Cash Payment):
1. Cart total: IDR 44,400
2. Cashier clicks "Cash Payment"
3. Cashier enters amount: IDR 50,000
4. System calculates change: IDR 5,600
5. System suggests: 1x IDR 5,000 + 1x IDR 500 + 1x IDR 100
6. Cashier confirms payment
7. Receipt printed
8. Transaction complete

**User Flow** (QRIS Payment):
1. Cart total: IDR 44,400
2. Cashier clicks "QRIS Payment"
3. System generates QRIS code
4. Customer scans code with e-wallet app
5. System waits for confirmation (30s timeout)
6. Payment confirmed
7. Receipt printed
8. Transaction complete

---

### 5. Receipt Generation

**Description**: Print thermal receipts with transaction details.

**Receipt Content**:
```
═══════════════════════════════════════
          TOKO ANAK BANGSA
      Jl. Sudirman No. 123
         Jakarta Selatan
      Tel: +62 21 1234 5678
═══════════════════════════════════════
Date: 13/12/2024          Time: 14:30
Cashier: Budi Santoso
Trans #: TRX-20241213-001
Customer: Toko Makmur (Wholesale)
═══════════════════════════════════════
Indomie Goreng
10 PCS @ IDR 2,500      IDR 25,000

Indomie Soto
5 PCS @ IDR 2,500       IDR 12,500
───────────────────────────────────────
Subtotal:                  IDR 37,500
Discount:                  IDR 5,000
Tax (PPN 11%):             IDR 3,575
═══════════════════════════════════════
TOTAL:                    IDR 36,075

Cash:                     IDR 40,000
Change:                    IDR 3,925
═══════════════════════════════════════
     Terima kasih atas kunjungan Anda!
       Barang yang sudah dibeli
         tidak dapat dikembalikan
═══════════════════════════════════════
           Powered by
        TOKO ANAK BANGSA Platform
═══════════════════════════════════════
```

**Receipt Options**:
- Print receipt (thermal printer)
- Email receipt to customer
- WhatsApp receipt (Pro+)
- Save as PDF

**Receipt Settings** (from Tenant Settings):
- Show/hide logo
- Show/hide store address
- Show/hide tax number (NPWP)
- Custom footer message
- Paper size (58mm or 80mm)

---

### 6. Customer Lookup & Linking

**Description**: Link transactions to customer accounts for history and loyalty.

**Capabilities**:
- Search customer by name/phone
- Quick add new customer
- View customer info (tier, credit limit, debt)
- Apply customer-specific pricing
- Track customer purchase history

**User Flow**:
1. Cashier presses F3 (Customer Lookup)
2. Cashier types phone: "0812"
3. System shows matching customers
4. Cashier selects: "Toko Makmur"
5. Customer info displayed:
   - Name: Toko Makmur
   - Type: Wholesale (Tier A)
   - Credit Limit: IDR 5,000,000
   - Current Debt: IDR 1,200,000
6. Cart prices auto-update to Tier A
7. Transaction linked to customer

**Unknown Customer**:
- Walk-in customer without account
- Default name: "Unknown Customer"
- Tier B (retail) pricing applied
- Transaction still recorded (no customer link)

---

### 7. Discounts & Promotions

**Description**: Apply discounts at item or cart level.

**Discount Types**:
- **Percentage**: e.g., 10% off
- **Fixed Amount**: e.g., IDR 5,000 off
- **Buy X Get Y**: e.g., Buy 2 get 1 free
- **Bundle**: e.g., 3 items for IDR 10,000

**Discount Application**:
- **Item-level**: Discount on specific product
- **Cart-level**: Discount on total
- **Manager Approval**: Required for discounts > 20% (configurable)

**User Flow** (Apply Discount):
1. Cashier adds products to cart
2. Subtotal: IDR 50,000
3. Cashier presses F4 (Discount)
4. Cashier enters: 10% or IDR 5,000
5. System applies discount
6. New total: IDR 45,000
7. Discount shown on receipt

---

### 8. Transaction Hold & Recall

**Description**: Temporarily save transaction and recall later.

**Use Cases**:
- Customer forgets wallet
- Customer adds more items
- Handle multiple customers alternately
- Shift change (transfer to next cashier)

**User Flow**:
1. Cashier processes transaction (cart has items)
2. Customer needs to get more cash
3. Cashier presses F9 (Hold)
4. Transaction saved with hold ID
5. Cashier helps next customer (new transaction)
6. First customer returns
7. Cashier recalls held transaction by ID
8. Complete payment

---

### 9. Offline Mode (Pro/Enterprise)

**Description**: Process transactions when internet is down.

**Capabilities**:
- Queue transactions locally
- Auto-sync when connection restored
- Local product cache
- Prevent overselling (local stock check)

**User Flow**:
1. Internet connection lost
2. System shows "Offline Mode" indicator
3. Cashier continues processing transactions
4. Transactions saved to local queue
5. Internet connection restored
6. System auto-syncs queued transactions
7. Stock and reports updated

**Limitations in Offline Mode**:
- Cannot check real-time stock from other branches
- Cannot process QRIS payments (cash/card only)
- Customer lookup limited to cached data

---

## Use Cases

### Use Case 1: Simple Cash Transaction

**Scenario**: Walk-in customer buys 10 Indomie.

**Steps**:
1. Cashier starts new transaction
2. Customer: Unknown (Tier B pricing)
3. Cashier scans barcode 10 times (or changes qty to 10)
4. Product: "Indomie Goreng"
5. Price: IDR 3,000 × 10 = IDR 30,000
6. Tax (11%): IDR 3,300
7. Total: IDR 33,300
8. Cashier enters cash: IDR 50,000
9. Change: IDR 16,700
10. Receipt printed
11. Transaction complete (15 seconds)

---

### Use Case 2: Wholesale Customer with Multiple Items

**Scenario**: Wholesale customer (Tier A) buys mixed products.

**Steps**:
1. Cashier looks up customer: "Toko Makmur"
2. Customer type: Wholesale (Tier A)
3. Cashier scans products:
   - Indomie Goreng: 50 PCS @ IDR 2,500 = IDR 125,000
   - Indomie Soto: 30 PCS @ IDR 2,500 = IDR 75,000
   - Minyak Goreng: 10 L @ IDR 18,000 = IDR 180,000
4. Subtotal: IDR 380,000
5. Tax: IDR 41,800
6. Total: IDR 421,800
7. Payment: QRIS
8. Receipt printed with customer name

---

### Use Case 3: Split Payment (Cash + QRIS)

**Scenario**: Customer pays partially with cash, rest with QRIS.

**Steps**:
1. Cart total: IDR 100,000
2. Customer has: IDR 50,000 cash + QRIS
3. Cashier clicks "Split Payment"
4. Cashier enters cash: IDR 50,000
5. Remaining: IDR 50,000
6. Customer scans QRIS for IDR 50,000
7. Both payments confirmed
8. Receipt shows both payment methods
9. Transaction complete

---

### Use Case 4: Transaction Hold & Recall

**Scenario**: Customer forgets wallet, returns 10 minutes later.

**Steps**:
1. Cashier processes cart: IDR 150,000
2. Customer realizes forgot wallet
3. Cashier presses F9 (Hold Transaction)
4. System saves transaction: Hold ID #001
5. Cashier helps next 3 customers
6. First customer returns with cash
7. Cashier clicks "Recall Transaction"
8. Enters Hold ID: #001
9. Transaction reloaded
10. Payment processed
11. Receipt printed

---

## Business Rules

### Pricing

- Default customer: Tier B (retail)
- Customer-specific tier applied when customer selected
- Price override requires manager PIN (configurable)
- Discounts > 20% require manager approval

### Payment

- Minimum cash denomination: IDR 100
- QRIS timeout: 30 seconds (configurable)
- Card payment requires reference number
- Split payment: Enterprise plan only

### Receipt

- Receipt must include: Date, time, cashier, items, total, payment
- Tax line shown if tax enabled in settings
- Customer name shown if transaction linked
- Receipt number auto-generated: TRX-YYYYMMDD-XXX

### Transaction Validation

- Cannot complete transaction with empty cart
- Cannot sell product with insufficient stock (unless negative stock allowed)
- Cannot apply discount larger than subtotal
- Payment amount must be ≥ total

---

## Edge Cases

### Out of Stock During Transaction

- **Problem**: Product scanned but stock just sold out
- **Solution**: Real-time stock check, show error if insufficient
- **UX**: "Insufficient stock. Available: 5 PCS. Requested: 10 PCS"

### Barcode Not Found

- **Problem**: Barcode scanned but product doesn't exist
- **Solution**: Show error, prompt manual search
- **UX**: "Product not found. Barcode: 8993451234567. Search manually?"

### Payment Failure (QRIS Timeout)

- **Problem**: Customer scans QRIS but payment not confirmed in 30s
- **Solution**: Cancel payment, try again or use different method
- **UX**: "Payment timeout. Please try again or use cash/card."

### Printer Jam/Offline

- **Problem**: Receipt printer not working
- **Solution**: Save receipt as PDF, email to customer, fix printer
- **UX**: "Printer offline. Receipt saved as PDF. Send to customer?"

---

## Future Enhancements

### Advanced Features
- Customer loyalty points integration
- Gift cards and vouchers
- Layaway/installment plans
- Return/exchange processing directly in POS
- Multi-currency support

### Hardware Integration
- Barcode scanner (USB/Bluetooth)
- Cash drawer integration
- Customer display (pole display)
- Receipt printer (thermal)
- Scale integration (for weighted products)
- Card payment terminal (EDC)

### Analytics
- Cashier performance reports
- Peak hours analysis
- Average transaction value
- Products per transaction
- Payment method distribution

---

## Success Metrics

- **Transaction Speed**: Avg time from scan to receipt
- **Payment Method Distribution**: % of each payment type
- **Average Transaction Value**: Revenue per transaction
- **Items Per Transaction**: Avg products per sale
- **Cashier Efficiency**: Transactions per hour per cashier

---

## Dependencies

- **Product Management** (03): Product catalog and pricing
- **Inventory Management** (04): Real-time stock checking
- **Customer Management** (07): Customer data and tier
- **Tenant Management** (02): Store settings and branding

---

**Last Updated**: 2024-12-13
