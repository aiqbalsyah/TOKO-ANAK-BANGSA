# Customer Management 👥

**Category**: CUSTOMER, CRM
**Priority**: SHOULD HAVE (MVP)
**Phase**: 2

---

## Overview

Customer Management enables store owners to build and maintain a comprehensive customer database, track purchase history, manage customer tiers for automatic pricing, handle customer credit (accounts receivable), and create customer loyalty programs. The system supports both individual consumers and business customers (B2B) with Indonesian credit practices like "bon" or "tempo" payment.

### Why This Matters

- **Customer Retention**: Build long-term relationships with repeat customers
- **Personalized Service**: Apply correct pricing tier automatically in POS
- **Credit Management**: Track customer debts and enforce credit limits (common in Indonesian B2B)
- **Marketing Intelligence**: Segment customers for targeted promotions
- **Revenue Growth**: Loyalty programs encourage repeat purchases
- **Better Service**: Quick access to customer history improves service quality
- **Debt Collection**: Systematic tracking of outstanding payments and due dates

---

## Business Requirements

### Primary Goals

1. **Customer Database**: Comprehensive contact and business information management
2. **Customer Tiers**: Automatic tier-based pricing (A/B/C) in POS transactions
3. **Purchase History**: Track all transactions, lifetime value, and purchase patterns
4. **Credit Management**: Accounts receivable (AR) with credit limits and payment terms
5. **Multiple Addresses**: Support for home, office, and warehouse delivery addresses
6. **Customer Segmentation**: Group customers for targeted marketing
7. **Customer Communication**: Notes, tags, and communication history

### Problems Solved

- **Pricing Errors**: Automatic tier application prevents manual pricing mistakes
- **Credit Risk**: Credit limits prevent over-extension of customer credit
- **Lost Sales**: Customer history helps staff recommend relevant products
- **Marketing Waste**: Customer segmentation enables targeted campaigns
- **Debt Management**: Systematic tracking improves collection rates
- **Customer Service**: Quick access to customer info and history

---

## Features

### 1. Customer Profile Management

**Description**: Create and maintain comprehensive customer profiles.

**Capabilities**:
- Add new customers manually or during POS transaction
- Customer types: Individual or Business
- Contact information (name, phone, email, WhatsApp)
- Business information (company name, tax ID/NPWP)
- Profile photo/logo upload
- Customer status (Active/Inactive/Blocked)
- Customer notes (internal, not visible to customer)
- Tags for filtering and segmentation
- Creation date and last updated tracking

**Customer Types**:

**Individual Customers**:
- Personal shoppers
- Walk-in retail customers
- Typically Tier B (retail pricing)
- No credit facilities (cash/digital payment only)
- Example: Household consumers buying groceries

**Business Customers** (B2B):
- Wholesalers, resellers, retailers
- Typically Tier A (wholesale pricing)
- Credit facilities available (payment terms)
- Tax ID required for tax invoices
- Example: "Toko Makmur" (small grocery store buying stock)

**User Flow** (Add Customer):
1. Staff navigates to Customers > Add New
2. Selects customer type: Individual or Business
3. Fills basic information:
   - Name: "Toko Makmur"
   - Business name: "CV. Toko Makmur Jaya"
   - Phone: +62812-3456-7890
   - Email: toko.makmur@gmail.com
   - Tax ID/NPWP: 01.234.567.8-901.000
4. Sets customer tier: Tier A (Wholesale)
5. Adds address information
6. Sets credit terms (if applicable)
7. Adds notes and tags
8. Saves customer
9. Customer available for POS transactions

---

### 2. Customer Tiers & Automatic Pricing

**Description**: Tier-based customer classification with automatic POS pricing.

**Customer Tiers**:

**Tier A - Grosir (Wholesale)**:
- Bulk buyers, resellers, retailers
- Lowest prices (wholesale margin)
- Minimum order quantity may apply
- Credit facilities typically available
- Example: Small shops buying stock for resale

**Tier B - Eceran (Retail)**:
- Walk-in customers, individual consumers
- Standard retail prices
- Default tier for unknown customers
- Usually cash or digital payment
- Example: Household consumers

**Tier C - VIP/Premium**:
- Special customers, corporate clients
- Custom pricing (may be lower or higher than retail)
- Exclusive products or services
- Priority service and support
- Example: Corporate bulk orders, loyal customers

**Automatic Pricing in POS**:

**User Flow**:
1. Cashier starts new POS transaction
2. Default customer: "Unknown" (Tier B pricing)
3. Customer: "Indomie Goreng" scanned
4. Price shown: IDR 3,000 (Tier B)
5. Cashier looks up customer: "Toko Makmur"
6. System detects: Tier A (Wholesale)
7. Price auto-updates: IDR 3,000 → IDR 2,500
8. All cart items repriced to Tier A
9. Transaction completed with wholesale prices

**Business Rules**:
- Customer tier applied automatically when customer selected
- Tier cannot be changed mid-transaction (must cancel and restart)
- Price override requires manager approval (optional setting)
- Tier change logged in customer history

---

### 3. Purchase History & Analytics

**Description**: Comprehensive tracking of customer purchase behavior.

**Capabilities**:
- View all customer transactions (POS + marketplace)
- Total lifetime value (total revenue from customer)
- Purchase frequency (visits per month)
- Average transaction value
- Last purchase date
- Favorite products (most purchased items)
- Purchase trends (growing/declining)
- Product recommendations based on history

**Purchase Analytics**:
```
Customer: Toko Makmur

Lifetime Value: IDR 125,000,000
Total Transactions: 287
Average Transaction: IDR 435,540
Purchase Frequency: 18 times/month
Last Purchase: 2 days ago
Customer Since: Jan 2023 (23 months)

Top 5 Products:
1. Indomie Goreng - 2,400 PCS (IDR 6M)
2. Indomie Soto - 1,800 PCS (IDR 4.5M)
3. Minyak Goreng 2L - 500 PCS (IDR 9M)
4. Gula Pasir 1kg - 400 PCS (IDR 6M)
5. Tepung Terigu 1kg - 350 PCS (IDR 3.5M)
```

**User Flow**:
1. Staff views customer profile: "Toko Makmur"
2. Clicks "Purchase History" tab
3. System shows transaction list:
   - Dec 13: IDR 450,000 (15 items) - Paid
   - Dec 11: IDR 320,000 (12 items) - Paid
   - Dec 9: IDR 560,000 (20 items) - Credit (due Dec 39)
4. Staff filters by date range or product
5. Staff exports to Excel for analysis

**Use Cases**:
- **Reorder Reminder**: "Customer usually buys Indomie every 3 days. Last purchase 4 days ago. Call to check?"
- **Upsell Opportunity**: "Customer always buys Indomie but never buys drinks. Suggest bundle?"
- **Stock Planning**: "Top 10 customers buy 5,000 PCS Indomie/month. Ensure stock available."

---

### 4. Credit Management (Accounts Receivable)

**Description**: Manage customer credit, debt tracking, and payment collection.

**Why Credit Management Matters** (Indonesian Context):
In Indonesia, B2B retail commonly uses "tempo" or "bon" system where customers (small shops) buy products on credit and pay later (Net 30/60/90 days). This is essential for:
- Small retailers with limited cash flow
- Building trust and long-term relationships
- Competitive advantage (offer better terms than competitors)
- Revenue growth (customers buy more on credit)

**Capabilities**:
- Set credit limit per customer
- Track current debt balance
- Payment terms (Net 30/60/90 days)
- Payment due dates and overdue tracking
- Payment history log
- Overdue notifications (email/WhatsApp)
- Credit hold (block sales if over limit or overdue)
- Generate invoices and payment receipts

**Credit Terms**:
```
Payment Terms:
- Net 30: Payment due 30 days after invoice date
- Net 60: Payment due 60 days after invoice date
- Net 90: Payment due 90 days after invoice date
- Cash: Immediate payment (no credit)

Example:
Invoice Date: Dec 13, 2024
Payment Terms: Net 30
Due Date: Jan 12, 2025
```

**User Flow** (Credit Sale):
1. Customer "Toko Makmur" comes to buy stock
2. Cashier looks up customer in POS
3. System shows customer credit info:
   ```
   Customer: Toko Makmur (Tier A)
   Credit Limit: IDR 5,000,000
   Current Debt: IDR 1,200,000
   Available Credit: IDR 3,800,000
   Payment Terms: Net 30
   Status: Active ✓
   ```
4. Cashier scans products, total: IDR 450,000
5. Available credit (IDR 3,800,000) > Transaction (IDR 450,000) ✓
6. Cashier selects payment method: Credit
7. System creates credit invoice
8. New debt: IDR 1,200,000 + IDR 450,000 = IDR 1,650,000
9. Due date: Jan 12, 2025 (30 days from Dec 13)
10. Invoice printed with due date
11. Customer takes products, no cash exchange

**User Flow** (Debt Payment):
1. Customer "Toko Makmur" returns to pay debt
2. Staff navigates to Customers > Toko Makmur > Debt
3. System shows outstanding invoices:
   ```
   Invoice #001: IDR 450,000 (Due: Jan 12) - Not Overdue
   Invoice #002: IDR 320,000 (Due: Jan 8) - Not Overdue
   Invoice #003: IDR 430,000 (Due: Dec 25) - Overdue 19 days ⚠️

   Total Debt: IDR 1,200,000
   Overdue: IDR 430,000
   ```
4. Customer pays: IDR 500,000 (Cash)
5. Staff allocates payment:
   - Invoice #003: IDR 430,000 (paid in full)
   - Invoice #002: IDR 70,000 (partial)
6. System updates:
   - Invoice #003: PAID ✓
   - Invoice #002: IDR 250,000 remaining
   - Total Debt: IDR 1,200,000 - IDR 500,000 = IDR 700,000
7. Receipt generated
8. Available credit updated: IDR 5M - IDR 700K = IDR 4.3M

**Credit Limit Exceeded**:

**User Flow**:
1. Customer "Toko Makmur" wants to buy: IDR 2,500,000
2. Current debt: IDR 3,200,000
3. Credit limit: IDR 5,000,000
4. Available credit: IDR 1,800,000
5. Transaction amount (IDR 2.5M) > Available (IDR 1.8M) ✗
6. System blocks transaction:
   ```
   ❌ Credit Limit Exceeded

   Credit Limit: IDR 5,000,000
   Current Debt: IDR 3,200,000
   Available: IDR 1,800,000

   Transaction: IDR 2,500,000
   Shortage: IDR 700,000

   Options:
   1. Customer pays existing debt first
   2. Reduce order to IDR 1,800,000 or less
   3. Request credit limit increase (Owner approval)
   4. Pay cash for this transaction
   ```
7. Customer chooses to pay existing debt first
8. Customer pays: IDR 1,000,000 toward debt
9. New available credit: IDR 2,800,000
10. Transaction now allowed ✓

**Overdue Debt Handling**:

**User Flow**:
1. Invoice #003 (IDR 430K) due Dec 25
2. Today: Jan 13 (19 days overdue)
3. System sends notification:
   ```
   WhatsApp to Customer:
   "Halo Toko Makmur,

   Invoice #003 (IDR 430,000) sudah jatuh tempo pada 25 Des 2024.
   Mohon segera melakukan pembayaran.

   Terima kasih,
   Toko Anak Bangsa"
   ```
4. If overdue > 30 days, system applies credit hold
5. Customer tries to buy on credit
6. System blocks transaction:
   ```
   ❌ Credit Hold - Overdue Payment

   Invoice #003: IDR 430,000
   Due Date: Dec 25, 2024
   Overdue: 19 days

   Credit sales blocked until overdue payment settled.
   Customer can pay cash or settle debt first.
   ```

**Business Rules**:
- Credit limit enforced strictly (cannot exceed)
- Overdue invoices trigger notifications (7, 14, 30 days)
- Credit hold after 30 days overdue (configurable)
- Partial payments allowed (allocate to oldest invoice first)
- Credit terms set per customer (default: Net 30)
- Owner/Admin can override credit hold (logged in audit trail)

---

### 5. Multiple Delivery Addresses

**Description**: Customers can have multiple saved delivery addresses.

**Capabilities**:
- Add unlimited addresses per customer
- Address types (Home, Office, Warehouse, Other)
- Set default shipping address
- Custom address labels ("Main Store", "Branch 2", etc.)
- Full address with district/city/province
- Delivery instructions per address
- Address verification (future: Google Maps integration)

**Use Cases**:

**B2B Customer with Multiple Locations**:
```
Customer: Toko Makmur

Address 1 (Default): ⭐
Label: Main Store
Type: Office
Address: Jl. Sudirman No. 123, Jakarta Selatan
Phone: +62812-3456-7890
Instructions: "Ring bell at side entrance"

Address 2:
Label: Warehouse
Type: Warehouse
Address: Jl. Industri No. 45, Tangerang
Phone: +62813-1111-2222
Instructions: "Delivery hours: 8AM-4PM only"

Address 3:
Label: Branch Bandung
Type: Office
Address: Jl. Asia Afrika No. 67, Bandung
Phone: +62822-3333-4444
Instructions: "Call before delivery"
```

**User Flow** (Select Address for Order):
1. Customer places marketplace order
2. Checkout page shows saved addresses
3. Customer selects: "Warehouse" address
4. System uses warehouse address for shipping
5. Delivery instructions included in fulfillment

**User Flow** (Add New Address):
1. Customer navigates to Profile > Addresses
2. Clicks "Add Address"
3. Fills form:
   - Label: "Branch Surabaya"
   - Type: Office
   - Full address
   - Phone number
   - Delivery instructions
4. Saves address
5. Address available for future orders

---

### 6. Customer Groups & Segmentation

**Description**: Organize customers into groups for targeted marketing.

**Capabilities**:
- Create custom customer groups
- Group by location (Jakarta, Bandung, etc.)
- Group by tier (A/B/C)
- Group by industry/business type
- Group by purchase behavior
- Assign customers to multiple groups
- Bulk assign customers to group
- Send targeted promotions to group

**Common Customer Groups** (Indonesia):

**Geographic**:
- Jakarta customers
- Bandung customers
- Surabaya customers
- Outer Java customers

**Tier-based**:
- Wholesale customers (Tier A)
- Retail customers (Tier B)
- VIP customers (Tier C)

**Behavior-based**:
- Active buyers (bought in last 30 days)
- Inactive buyers (no purchase > 90 days)
- High-value customers (lifetime value > IDR 10M)
- Frequent buyers (> 10 purchases/month)
- At-risk customers (decreasing purchase frequency)

**Industry**:
- Grocery stores
- Restaurants
- Hotels
- Offices

**User Flow** (Create Group):
1. Staff navigates to Customers > Groups
2. Clicks "Create Group"
3. Enters group details:
   - Name: "Active Jakarta Wholesale"
   - Description: "Wholesale customers in Jakarta with purchase in last 30 days"
4. Sets group criteria (auto-assignment):
   - Location: Jakarta
   - Tier: A (Wholesale)
   - Last purchase: < 30 days ago
5. System auto-assigns matching customers (37 customers)
6. Group created
7. Can now send targeted promotions to this group

**User Flow** (Send Promotion to Group):
1. Staff creates promotion: "10% off Indomie this week"
2. Selects target group: "Active Jakarta Wholesale"
3. Chooses notification method: WhatsApp
4. System sends WhatsApp to 37 customers in group
5. Tracks campaign performance (opens, conversions)

---

### 7. Customer Search & Filtering

**Description**: Fast customer lookup for POS and customer service.

**Search Methods**:
- Text search: Name, business name, phone, email
- Filter by tier (A/B/C)
- Filter by status (Active/Inactive/Blocked)
- Filter by credit status (Has debt/Overdue/Credit hold)
- Filter by location
- Filter by group
- Filter by last purchase date

**User Flow** (POS Customer Lookup):
1. Cashier presses F3 (Customer Lookup)
2. Cashier types: "0812"
3. System shows matching customers:
   ```
   Results for "0812":

   1. Toko Makmur (Tier A) - +62812-3456-7890
      Debt: IDR 1.2M | Last purchase: 2 days ago

   2. Warung Sari (Tier A) - +62812-9999-8888
      Debt: IDR 450K (Overdue 5 days) ⚠️

   3. Ibu Siti (Tier B) - +62812-1111-2222
      No debt | Last purchase: 7 days ago
   ```
4. Cashier selects customer: "Toko Makmur"
5. Customer info loaded in POS
6. Tier A pricing automatically applied

---

### 8. Customer Notes & Tags

**Description**: Add internal notes and tags for customer management.

**Capabilities**:
- Internal notes (staff only, not visible to customer)
- Customer-facing notes (visible on invoices/receipts)
- Tags for categorization and filtering
- Note history (who added, when)
- Rich text notes with attachments

**Use Cases**:

**Internal Notes** (Examples):
- "Customer always requests delivery before 10 AM"
- "Prefers WhatsApp communication over calls"
- "Owner is Pak Budi, very detail-oriented"
- "Always negotiates prices, max 5% discount allowed"
- "Complained about late delivery on Dec 5, offered apology discount"

**Customer-facing Notes** (Examples):
- "Valued customer since 2023"
- "VIP customer - priority handling"
- "Corporate account - requires tax invoice"

**Tags** (Examples):
- `vip`
- `price-sensitive`
- `bulk-buyer`
- `fast-payer`
- `difficult`
- `loyal`
- `corporate`

**User Flow**:
1. Staff views customer profile
2. Adds internal note: "Customer requested invoice be sent to finance@toko.com instead of main email"
3. Adds tag: `bulk-buyer`, `fast-payer`
4. Notes and tags saved
5. Other staff can see notes when serving customer

---

### 9. Customer Import & Export

**Description**: Bulk import/export customer data.

**Capabilities**:
- Import customers from CSV/Excel
- Export customer list to CSV/Excel
- Template download for import
- Validation before import
- Update existing customers on import
- Export with filters (tier, location, etc.)

**User Flow** (Import Customers):
1. Staff navigates to Customers > Import
2. Downloads CSV template
3. Fills template with customer data (200 customers)
4. Uploads CSV file
5. System validates data:
   - 195 valid ✓
   - 5 errors (duplicate phone numbers)
6. Staff fixes errors, re-uploads
7. System imports 200 customers
8. Confirmation shown
9. Customers available in system

---

## Use Cases

### Use Case 1: Wholesale Customer Credit Purchase

**Scenario**: "Toko Makmur" (regular wholesale customer) comes to buy stock on credit.

**Steps**:
1. Customer arrives at store with shopping list
2. Cashier looks up customer: "0812-3456"
3. System shows: "Toko Makmur (Tier A)"
   - Credit Limit: IDR 5,000,000
   - Current Debt: IDR 1,200,000
   - Available: IDR 3,800,000
   - Overdue: None ✓
4. Cashier scans products:
   - Indomie Goreng: 50 PCS @ IDR 2,500 = IDR 125,000
   - Indomie Soto: 30 PCS @ IDR 2,500 = IDR 75,000
   - Minyak Goreng: 10 L @ IDR 18,000 = IDR 180,000
5. Subtotal: IDR 380,000
6. Tax (11%): IDR 41,800
7. Total: IDR 421,800
8. Available credit (IDR 3.8M) > Total (IDR 421K) ✓
9. Cashier selects payment: Credit
10. System creates credit invoice #1234
11. Due date: Jan 13, 2025 (Net 30)
12. Invoice printed with due date
13. New debt: IDR 1,621,800
14. Customer takes products, no cash exchange
15. System sends WhatsApp confirmation with invoice

---

### Use Case 2: Customer Debt Payment

**Scenario**: Customer comes to pay outstanding debt.

**Steps**:
1. Customer "Toko Makmur" visits to pay debt
2. Staff navigates to Customers > Toko Makmur > Debt
3. System shows outstanding invoices:
   - Invoice #1230: IDR 450,000 (Due: Jan 10) - Not due
   - Invoice #1228: IDR 320,000 (Due: Jan 5) - Overdue 8 days ⚠️
   - Invoice #1225: IDR 430,000 (Due: Dec 25) - Overdue 19 days ⚠️
4. Total debt: IDR 1,200,000 (IDR 750K overdue)
5. Customer pays: IDR 800,000 (Cash)
6. Staff allocates payment (oldest first):
   - Invoice #1225: IDR 430,000 → PAID ✓
   - Invoice #1228: IDR 320,000 → PAID ✓
   - Invoice #1230: IDR 50,000 (partial payment)
7. Remaining:
   - Invoice #1230: IDR 400,000 remaining
8. Total debt: IDR 400,000 (no overdue)
9. Receipt printed showing payment allocation
10. Available credit updated: IDR 4,600,000
11. Customer can now purchase on credit again

---

### Use Case 3: Credit Limit Exceeded - Negotiation

**Scenario**: Customer wants to buy but credit limit insufficient.

**Steps**:
1. Customer "Warung Sari" wants to order: IDR 1,500,000
2. Staff checks credit:
   - Credit Limit: IDR 2,000,000
   - Current Debt: IDR 1,300,000
   - Available: IDR 700,000
3. Transaction (IDR 1.5M) > Available (IDR 700K) ✗
4. Staff explains: "Available credit IDR 700K, need IDR 800K more"
5. Options discussed:
   a) Pay existing debt IDR 800K first
   b) Reduce order to IDR 700K
   c) Request credit limit increase
6. Customer chooses option A
7. Customer pays IDR 800K toward debt
8. New debt: IDR 500,000
9. Available credit: IDR 1,500,000 ✓
10. Transaction now allowed
11. Order processed on credit
12. New debt: IDR 2,000,000 (at limit)

---

### Use Case 4: Overdue Debt - Credit Hold

**Scenario**: Customer has overdue debt, system blocks new credit sales.

**Steps**:
1. Customer "Toko Sejahtera" tries to buy on credit
2. Cashier looks up customer
3. System shows warning:
   ```
   ⚠️ CREDIT HOLD - OVERDUE PAYMENT

   Invoice #999: IDR 850,000
   Due Date: Nov 15, 2024
   Overdue: 59 days

   Credit sales blocked. Customer must:
   1. Settle overdue debt, OR
   2. Pay cash for this transaction
   ```
4. Cashier explains situation to customer
5. Customer didn't realize payment overdue
6. Customer pays overdue debt: IDR 850,000 (Cash)
7. Staff records payment, invoice marked PAID
8. Credit hold automatically removed
9. Customer can now buy on credit again
10. Current transaction processed on credit

---

### Use Case 5: New Customer Registration During POS

**Scenario**: Walk-in customer wants wholesale prices but not in system.

**Steps**:
1. Customer "Toko Baru" comes to buy stock
2. Says they're a reseller, wants wholesale price
3. Cashier searches customer: Not found
4. Cashier clicks "Quick Add Customer" in POS
5. Fills quick form:
   - Name: Toko Baru
   - Phone: +62813-5555-6666
   - Type: Business
   - Tier: A (Wholesale)
   - Credit: No (cash only for now)
6. Saves customer
7. Customer automatically selected in POS
8. Tier A prices applied
9. Transaction completed with wholesale pricing
10. After transaction, staff can complete full profile

---

## Business Rules

### Customer Tiers

- Tier A ≤ Tier B ≤ Tier C pricing enforced
- Tier change requires Owner/Admin permission
- Tier applied automatically in POS when customer selected
- Cannot change tier during active transaction
- Tier change history logged

### Credit Management

- Credit limit strictly enforced (cannot exceed)
- Payment terms: Net 30/60/90 (configurable per customer)
- Default payment terms: Net 30
- Overdue notifications sent at 7, 14, 30 days
- Credit hold after 30 days overdue (configurable)
- Partial payments allowed, allocated to oldest invoice first
- Zero or negative credit limit = no credit sales allowed
- Credit transactions require customer selection (cannot use "Unknown")

### Debt Payment Allocation

- Payments allocated to oldest invoice first (FIFO)
- Can manually allocate to specific invoices
- Partial payment must specify which invoices to pay
- Overpayment creates credit balance (future purchases)

### Customer Data

- Phone number must be unique (one customer per phone)
- Email can be shared (family business)
- Tax ID/NPWP required for corporate tax invoices
- Customer cannot be deleted if has outstanding debt
- Customer cannot be deleted if has transaction history (only archive)

---

## Edge Cases

### Customer Wants Credit But No Limit Set

- **Problem**: New customer wants to buy on credit, no credit limit configured
- **Solution**: Staff must set credit limit first (requires Owner/Admin approval)
- **UX**: "Customer has no credit limit. Contact manager to set credit limit."

### Payment Exceeds Total Debt

- **Problem**: Customer pays IDR 1M but debt is only IDR 800K
- **Solution**: Record payment, create credit balance IDR 200K
- **UX**: "Payment (IDR 1M) > Debt (IDR 800K). Credit balance IDR 200K created. Use for future purchases."

### Customer Tier Conflict with Product

- **Problem**: VIP customer (Tier C) but Tier C price > Tier B for some products
- **Solution**: System applies lower price (best price for customer)
- **Business Logic**: Always apply most favorable price to customer

### Duplicate Customer (Same Phone)

- **Problem**: Staff tries to add customer with existing phone number
- **Solution**: System shows existing customer, prompt to edit instead
- **UX**: "Phone +6281234567890 already exists: 'Toko Makmur'. Edit this customer instead?"

### Customer Blocked But Has Credit Balance

- **Problem**: Customer blocked for fraud but has IDR 500K credit balance
- **Solution**: Allow credit balance refund, then block
- **UX**: "Customer has credit balance IDR 500K. Process refund before blocking."

### Credit Limit Decrease Below Current Debt

- **Problem**: Admin decreases credit limit to IDR 2M but current debt is IDR 3M
- **Solution**: Allow decrease, but customer cannot take more credit until debt below limit
- **UX**: Warning shown: "New limit (IDR 2M) < Current debt (IDR 3M). No new credit until debt reduced."

---

## Future Enhancements

### Loyalty & Rewards
- Loyalty points system (1 point per IDR spent)
- Point redemption for discounts/products
- Tier promotion (auto-upgrade active customers)
- Birthday discounts and promotions
- Referral program (refer new customer, get bonus)

### Advanced Analytics
- Customer lifetime value prediction
- Churn risk analysis (at-risk customers)
- Purchase pattern analysis (recommend products)
- Customer segmentation with AI
- Next purchase prediction

### Communication
- WhatsApp integration (order status, payment reminders)
- Email marketing campaigns
- SMS notifications for promotions
- Push notifications (mobile app)
- In-app messaging with customer support

### Credit Management
- Automated payment reminders
- Credit scoring based on payment history
- Dynamic credit limits (auto-adjust based on behavior)
- Collection agency integration (severe overdue)
- Payment plans (installment for large debts)

### Integration
- Import from existing systems (Excel, ERP)
- Export to accounting software
- CRM integration (Salesforce, HubSpot)
- Email marketing tools (Mailchimp)
- Customer data platform (CDP)

---

## Success Metrics

- **Customer Database Growth**: # of active customers per month
- **Tier Distribution**: % of customers in each tier (target: 30% Tier A)
- **Credit Utilization**: Avg credit used vs available (target: 60-70%)
- **Payment Timeliness**: % of invoices paid on time (target: >85%)
- **Overdue Rate**: % of debt overdue (target: <10%)
- **Customer Retention**: % of customers with purchase in last 90 days
- **Lifetime Value**: Avg customer lifetime value (target: growing)
- **Debt Collection Rate**: % of overdue debt collected within 60 days

---

## Dependencies

- **Authentication** (01): Customer accounts for marketplace
- **Tenant Management** (02): Store settings for credit terms
- **Product Management** (03): Product catalog for tier pricing
- **POS/Cashier** (05): Apply customer pricing and credit sales
- **Order Management** (06): Link orders to customers
- **Financial Management** (09): AR tracking and reporting

---

**Last Updated**: 2024-12-13
