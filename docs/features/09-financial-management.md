# Financial Management 💰

**Category**: FINANCE, ACCOUNTING
**Priority**: SHOULD HAVE (MVP)
**Phase**: 2-3

---

## Overview

Financial Management provides comprehensive tracking of business finances including cash flow, revenue, expenses, accounts receivable (AR), accounts payable (AP), and profit & loss statements. The system integrates with Indonesian payment gateways (Midtrans) for online payments and provides financial reports for business decision-making and tax compliance.

### Why This Matters

- **Financial Visibility**: Real-time view of business financial health
- **Cash Flow Management**: Track money in and money out
- **Profitability**: Understand which products and customers are profitable
- **Tax Compliance**: Accurate records for Indonesian tax reporting (PPh, PPN)
- **Decision Making**: Data-driven decisions based on financial performance
- **Investor/Lender Ready**: Professional financial reports for funding

---

## Business Requirements

### Primary Goals

1. **Revenue Tracking**: Track all income from sales (POS + marketplace)
2. **Expense Management**: Record and categorize all business expenses
3. **Cash Flow**: Monitor cash inflows and outflows
4. **AR/AP Management**: Track customer credits and supplier debts
5. **P&L Statement**: Generate profit & loss reports
6. **Payment Gateway**: Integrate Midtrans for online payments (QRIS, cards, etc.)
7. **Financial Reports**: Daily, monthly, yearly financial summaries
8. **Tax Reports**: Generate reports for Indonesian tax compliance

### Problems Solved

- **Cash Shortage**: Early warning of cash flow issues
- **Expense Control**: Identify and reduce unnecessary expenses
- **Profitability Analysis**: Understand true business profitability
- **Tax Preparation**: Simplified tax filing with accurate records
- **Financial Planning**: Budget and forecast based on historical data
- **Audit Trail**: Complete record of all financial transactions

---

## Features

### 1. Revenue Tracking

**Description**: Automatic tracking of all business income sources.

**Revenue Sources**:
- POS sales (in-store transactions)
- Marketplace sales (online orders)
- Credit payments from customers
- Other income (returns, misc)

**Capabilities**:
- Automatic revenue recording from POS/marketplace
- Revenue by payment method (cash, card, QRIS, credit, etc.)
- Revenue by product category
- Revenue by branch (multi-location)
- Revenue trends (daily, weekly, monthly)
- Revenue forecasting

**Revenue Dashboard**:
```
Today's Revenue: IDR 8,500,000 (+12% vs yesterday)

Payment Methods:
- Cash: IDR 3,200,000 (38%)
- QRIS: IDR 2,800,000 (33%)
- Card: IDR 1,500,000 (18%)
- Credit: IDR 1,000,000 (12%)

Top Categories:
1. Mie Instan: IDR 3,500,000
2. Minuman: IDR 2,200,000
3. Snack: IDR 1,800,000

This Month: IDR 185,000,000
Last Month: IDR 172,000,000 (+7.5%)

Revenue Target: IDR 200M/month
Progress: 92.5% (IDR 185M / IDR 200M)
```

---

### 2. Expense Management

**Description**: Record and categorize all business expenses.

**Expense Categories**:

**Operational Expenses**:
- Rent (store/warehouse)
- Utilities (electricity, water, internet)
- Salaries & wages
- Insurance
- Maintenance & repairs

**Cost of Goods Sold (COGS)**:
- Product purchases from suppliers
- Shipping & handling
- Import duties (if applicable)

**Marketing & Sales**:
- Advertising (Google Ads, Facebook, etc.)
- Promotional materials
- Marketplace fees
- WhatsApp Business API

**Administrative**:
- Office supplies
- Software subscriptions (this platform!)
- Professional services (accountant, lawyer)
- Bank fees

**Taxes**:
- PPN (VAT - 11% in Indonesia)
- PPh (Income Tax)
- Property tax (PBB)

**Capabilities**:
- Add expense manually
- Categorize expenses
- Attach receipts/invoices (photos/PDFs)
- Recurring expenses (rent, subscriptions)
- Expense approval workflow (Pro/Enterprise)
- Expense reports by category
- Budget tracking (set limits per category)

**User Flow** (Add Expense):
1. Staff navigates to Finance > Expenses > Add New
2. Fills expense details:
   - Date: Dec 13, 2024
   - Category: Utilities
   - Description: "PLN electricity bill - December"
   - Amount: IDR 2,500,000
   - Payment method: Bank Transfer
3. Uploads receipt photo
4. Saves expense
5. If > threshold, requires owner approval
6. Once approved, expense recorded
7. Cash/bank balance updated

**Recurring Expenses**:
```
Setup:
Expense: Store Rent
Amount: IDR 15,000,000/month
Frequency: Monthly
Day: 1st of each month
Category: Rent
Auto-record: Yes

Result:
System automatically creates expense on 1st of each month
Owner receives notification
Owner approves
Expense recorded
```

---

### 3. Cash Flow Management

**Description**: Track all money flowing in and out of the business.

**Cash Flow Components**:

**Operating Activities**:
- Cash from sales (+)
- Payments to suppliers (-)
- Salaries and wages (-)
- Operating expenses (-)

**Investing Activities** (future):
- Purchase of equipment (-)
- Sale of assets (+)

**Financing Activities** (future):
- Loans received (+)
- Loan repayments (-)
- Owner investments (+)
- Owner withdrawals (-)

**Cash Flow Statement**:
```
Cash Flow - December 2024

Opening Balance (Dec 1): IDR 25,000,000

OPERATING ACTIVITIES:
Cash from Sales: +IDR 185,000,000
Customer Payments (AR): +IDR 12,000,000
Supplier Payments (AP): -IDR 95,000,000
Salaries: -IDR 18,000,000
Rent: -IDR 15,000,000
Utilities: -IDR 3,500,000
Other Expenses: -IDR 8,500,000
Net Operating Cash Flow: +IDR 57,000,000

INVESTING ACTIVITIES:
Equipment Purchase: -IDR 5,000,000
Net Investing Cash Flow: -IDR 5,000,000

FINANCING ACTIVITIES:
Owner Investment: +IDR 10,000,000
Net Financing Cash Flow: +IDR 10,000,000

Net Cash Flow: +IDR 62,000,000

Closing Balance (Dec 31): IDR 87,000,000
```

**Capabilities**:
- Real-time cash balance
- Cash flow projections (30/60/90 days)
- Cash flow alerts (low balance warning)
- Multiple cash accounts (bank, petty cash, etc.)
- Cash reconciliation

**Low Cash Alert**:
```
⚠️ LOW CASH ALERT

Current Cash: IDR 8,500,000
Minimum Required: IDR 10,000,000

Upcoming Payments (Next 7 Days):
- Dec 15: Supplier payment - IDR 15,000,000
- Dec 18: Salaries - IDR 18,000,000
Total: IDR 33,000,000

Cash Shortage: IDR 24,500,000

Actions:
1. Collect customer payments (AR: IDR 12M available)
2. Delay supplier payment (negotiate extension)
3. Owner cash injection
```

---

### 4. Accounts Receivable (AR) Management

**Description**: Track money owed by customers (credit sales).

**Capabilities**:
- View all outstanding customer debts
- Track payment due dates
- Aging report (0-30, 31-60, 61-90, 90+ days)
- Collection reminders (automated)
- Write-off bad debts
- AR turnover ratio

**AR Dashboard**:
```
Total Accounts Receivable: IDR 35,000,000

Aging Analysis:
- Current (0-30 days): IDR 22,000,000 (63%)
- 31-60 days: IDR 8,000,000 (23%)
- 61-90 days: IDR 3,500,000 (10%)
- 90+ days (Bad Debt Risk): IDR 1,500,000 (4%) ⚠️

Top 5 Customers by Debt:
1. Toko Makmur - IDR 8,500,000 (Due: Dec 20)
2. Warung Sari - IDR 6,200,000 (Due: Dec 15)
3. Toko Sejahtera - IDR 5,800,000 (Overdue 15 days) ⚠️
4. CV Mitra - IDR 4,500,000 (Due: Jan 5)
5. Toko Baru - IDR 3,000,000 (Due: Dec 25)

Expected Collections (Next 30 Days): IDR 28,500,000
```

**Collection Workflow**:
1. Day 0: Credit sale, invoice sent
2. Day 7: Reminder 1 (automated email/WhatsApp)
3. Day 14: Reminder 2 (phone call from staff)
4. Day 30: Payment due date
5. Day 37: Overdue reminder (urgent)
6. Day 60: Final notice before credit hold
7. Day 90+: Consider bad debt write-off

---

### 5. Accounts Payable (AP) Management

**Description**: Track money owed to suppliers (credit purchases).

**Capabilities**:
- View all outstanding supplier debts
- Track payment due dates
- AP aging report
- Payment scheduling
- Early payment discounts tracking
- AP turnover ratio

**AP Dashboard**:
```
Total Accounts Payable: IDR 45,000,000

Payment Schedule (Next 30 Days):
- Week 1 (Dec 13-19): IDR 12,000,000
- Week 2 (Dec 20-26): IDR 18,000,000
- Week 3 (Dec 27-Jan 2): IDR 8,500,000
- Week 4 (Jan 3-9): IDR 6,500,000

Top 5 Suppliers by Debt:
1. PT Indofood - IDR 15,000,000 (Due: Dec 20)
2. PT Unilever - IDR 8,500,000 (Due: Dec 15)
3. PT Mayora - IDR 7,200,000 (Due: Jan 5)
4. CV Mitra Jaya - IDR 5,800,000 (Due: Dec 28)
5. Toko Grosir ABC - IDR 2,000,000 (Overdue 15 days) ⚠️

Cash Required (Next 30 Days): IDR 45,000,000
Available Cash: IDR 25,000,000
Shortfall: IDR 20,000,000 ⚠️
```

---

### 6. Profit & Loss (P&L) Statement

**Description**: Comprehensive income statement showing profitability.

**P&L Components**:

**Revenue**:
- Gross Sales
- Less: Returns & Refunds
- Net Sales

**Cost of Goods Sold (COGS)**:
- Opening Inventory
- Plus: Purchases
- Less: Closing Inventory
- COGS Total

**Gross Profit** = Net Sales - COGS

**Operating Expenses**:
- Salaries & Wages
- Rent
- Utilities
- Marketing
- Administrative
- Depreciation

**Operating Profit** = Gross Profit - Operating Expenses

**Other Income/Expenses**:
- Interest Income
- Interest Expense
- Other Income

**Net Profit Before Tax** = Operating Profit + Other Income - Other Expenses

**Taxes**:
- Income Tax (PPh)

**Net Profit After Tax**

**Sample P&L Statement**:
```
PROFIT & LOSS STATEMENT
TOKO ANAK BANGSA
December 2024

REVENUE:
Gross Sales                      IDR 188,500,000
Less: Returns & Refunds          IDR   3,500,000
                                 ───────────────
Net Sales                        IDR 185,000,000

COST OF GOODS SOLD:
Opening Inventory (Dec 1)        IDR  45,000,000
Plus: Purchases                  IDR  95,000,000
Less: Closing Inventory (Dec 31) IDR  42,000,000
                                 ───────────────
COGS                             IDR  98,000,000

GROSS PROFIT                     IDR  87,000,000
Gross Margin: 47%

OPERATING EXPENSES:
Salaries & Wages                 IDR  18,000,000
Rent                             IDR  15,000,000
Utilities                        IDR   3,500,000
Marketing & Advertising          IDR   4,200,000
Administrative                   IDR   2,800,000
Maintenance & Repairs            IDR   1,500,000
Insurance                        IDR   1,200,000
Depreciation                     IDR     800,000
Other Operating Expenses         IDR   2,000,000
                                 ───────────────
Total Operating Expenses         IDR  49,000,000

OPERATING PROFIT                 IDR  38,000,000
Operating Margin: 20.5%

OTHER INCOME/EXPENSES:
Interest Income                  IDR     150,000
Other Income                     IDR     350,000
                                 ───────────────
Total Other Income               IDR     500,000

NET PROFIT BEFORE TAX            IDR  38,500,000

TAXES:
Income Tax (PPh 22%)             IDR   8,470,000

NET PROFIT AFTER TAX             IDR  30,030,000
Net Margin: 16.2%
```

**Key Metrics**:
```
Gross Margin: 47% (Target: 40-50%) ✓
Operating Margin: 20.5% (Target: 15-25%) ✓
Net Margin: 16.2% (Target: 10-20%) ✓

Return on Sales: 16.2%
Break-even Revenue: IDR 122,500,000
Actual Revenue: IDR 185,000,000
Above Break-even: 51% ✓
```

---

### 7. Payment Gateway Integration (Midtrans)

**Description**: Accept online payments via Midtrans (Indonesian payment gateway).

**Supported Payment Methods**:

**QRIS (QR Indonesian Standard)**:
- GoPay
- OVO
- Dana
- ShopeePay
- LinkAja
- Bank QRIS

**Virtual Account**:
- BCA
- Mandiri
- BNI
- BRI
- Permata

**Credit/Debit Cards**:
- Visa
- MasterCard
- JCB

**E-wallets**:
- GoPay (direct)
- ShopeePay (direct)

**Bank Transfer**:
- Manual verification

**Capabilities**:
- Payment link generation
- QR code display for QRIS
- Payment status webhook (real-time updates)
- Automatic order confirmation on payment
- Refund processing
- Payment reports
- Settlement tracking

**User Flow** (Customer Pays via QRIS):
1. Customer places marketplace order: IDR 250,000
2. Checkout: Customer selects "QRIS"
3. System calls Midtrans API to create transaction
4. Midtrans returns QRIS code
5. System displays QR code to customer
6. Customer scans with e-wallet app (GoPay)
7. Customer confirms payment in GoPay
8. Midtrans sends webhook: Payment successful
9. System receives webhook
10. Order status: Pending → Paid
11. Fulfillment process begins
12. Customer receives confirmation email

**Midtrans Configuration**:
```
Midtrans Settings:

Environment: Production
Server Key: [encrypted]
Client Key: [encrypted]

Payment Methods Enabled:
☑ QRIS
☑ GoPay
☑ ShopeePay
☑ Virtual Account (BCA, Mandiri, BNI, BRI)
☑ Credit Card (Visa, MasterCard)

Transaction Settings:
Payment Expiry: 24 hours
Auto-capture: Yes
3D Secure: Required for cards
Fraud Detection: Enabled

Fees (example):
- QRIS: 0.7%
- Virtual Account: IDR 4,000/transaction
- Credit Card: 2.9% + IDR 2,000
```

**Refund Processing**:

**User Flow**:
1. Customer requests refund for order #1234
2. Owner approves refund
3. Staff navigates to Orders > #1234 > Refund
4. Refund amount: IDR 250,000 (full refund)
5. Original payment: QRIS (GoPay)
6. System calls Midtrans refund API
7. Midtrans processes refund to customer's GoPay
8. Refund typically completes in 1-3 business days
9. Customer receives refund notification
10. Order status: Refunded

---

### 8. Financial Reports

**Description**: Generate comprehensive financial reports for analysis and compliance.

**Available Reports**:

**Sales Reports**:
- Daily sales summary
- Sales by product/category
- Sales by payment method
- Sales by customer tier
- Sales by branch (multi-location)

**Expense Reports**:
- Expenses by category
- Budget vs actual
- Recurring expenses list
- Expense trends

**Cash Reports**:
- Cash flow statement
- Bank reconciliation
- Petty cash report
- Cash projection

**AR/AP Reports**:
- AR aging report
- Customer payment history
- AP aging report
- Supplier payment history

**Tax Reports**:
- PPN (VAT) calculation
- PPh (Income Tax) calculation
- Tax invoice list
- Monthly tax summary

**Profitability Reports**:
- P&L statement (monthly, quarterly, yearly)
- Product profitability analysis
- Customer profitability analysis
- Branch profitability (multi-location)

**Report Export Formats**:
- PDF (formatted for printing)
- Excel (for analysis)
- CSV (for import to accounting software)

---

### 9. Bank Reconciliation

**Description**: Match bank statements with system records (Pro/Enterprise).

**Capabilities**:
- Import bank statements (CSV/PDF)
- Auto-match transactions
- Flag discrepancies
- Manual matching
- Reconciliation report

**User Flow**:
1. Staff downloads bank statement (CSV from BCA)
2. Staff navigates to Finance > Bank Reconciliation
3. Uploads CSV file
4. System parses statement (250 transactions)
5. Auto-matching:
   - 230 transactions matched ✓
   - 15 transactions unmatched ⚠️
   - 5 in system but not in bank ⚠️
6. Staff reviews unmatched:
   - 10 manual matches found ✓
   - 5 missing receipts (staff adds)
7. Final reconciliation:
   - 245 matched ✓
   - 5 discrepancies (investigated)
8. Reconciliation report generated
9. Accountant reviews and approves

---

## Use Cases

### Use Case 1: Monthly P&L Review

**Scenario**: Owner reviews December P&L to assess business performance.

**Steps**:
1. Jan 5: Owner navigates to Reports > P&L Statement
2. Selects period: December 2024
3. System generates P&L:
   - Revenue: IDR 185M
   - COGS: IDR 98M (53%)
   - Gross Profit: IDR 87M (47%)
   - Expenses: IDR 49M
   - Net Profit: IDR 30M (16.2%)
4. Owner analyzes:
   - Gross margin 47% (good, target 40-50%)
   - Rent IDR 15M (8% of revenue - acceptable)
   - Marketing IDR 4.2M (2.3% - could increase)
   - Net profit 16.2% (excellent, target 10-20%)
5. Owner decisions:
   - Increase marketing budget to grow sales
   - Maintain current expense levels
   - Target: IDR 200M revenue in January
6. Owner exports P&L to PDF
7. Sends to accountant for tax filing

---

### Use Case 2: Cash Flow Crisis Management

**Scenario**: Business faces temporary cash shortage.

**Steps**:
1. Dec 10: Cash balance: IDR 8M
2. Upcoming payments:
   - Dec 15: Salaries IDR 18M
   - Dec 15: Supplier IDR 15M
   - Total needed: IDR 33M
3. Shortfall: IDR 25M ⚠️
4. Owner reviews AR: IDR 35M owed by customers
5. Owner calls top 3 customers with overdue payments:
   - Toko Makmur: Pays IDR 8.5M (was due Dec 20, pays early)
   - Warung Sari: Pays IDR 6.2M (was due Dec 15, on time)
   - Toko Sejahtera: Pays IDR 5.8M (was overdue, finally pays)
6. Collections: IDR 20.5M
7. New cash balance: IDR 28.5M
8. Still short IDR 4.5M
9. Owner negotiates with supplier:
   - PT Indofood: Agrees to extend payment to Dec 22
10. Crisis averted ✓
11. Owner injects IDR 10M personal funds for buffer
12. Implements AR collection policy (stricter credit terms)

---

### Use Case 3: Expense Budget Control

**Scenario**: Marketing expenses exceeding budget.

**Steps**:
1. Dec 20: System sends alert
   ```
   ⚠️ BUDGET ALERT

   Category: Marketing
   Budget: IDR 5,000,000/month
   Spent: IDR 5,200,000 (104%)
   Overspent: IDR 200,000

   Top Expenses:
   - Facebook Ads: IDR 2,800,000
   - Google Ads: IDR 1,500,000
   - Promotional materials: IDR 900,000
   ```
2. Owner reviews marketing expenses
3. Analyzes ROI:
   - Facebook Ads: IDR 2.8M spend → IDR 18M revenue (6.4x ROI) ✓
   - Google Ads: IDR 1.5M spend → IDR 5M revenue (3.3x ROI) ⚠️
   - Promo materials: IDR 900K → Unclear ROI ⚠️
4. Owner decisions:
   - Continue Facebook Ads (high ROI)
   - Reduce Google Ads budget (lower ROI)
   - Stop promo materials (no measurable ROI)
5. Adjusts January budget:
   - Marketing: IDR 4M (reduced from IDR 5M)
   - Focus on high-ROI channels
6. Sets up tracking for all marketing spend

---

## Business Rules

### Revenue Recognition

- Revenue recorded when payment received (cash basis)
- Credit sales recorded when invoice created (accrual basis)
- Returns reduce revenue in the period returned
- Marketplace fees deducted from gross revenue

### Expense Recording

- Expenses > IDR 1,000,000 require receipt/invoice
- Recurring expenses auto-created on schedule
- Expense approval required for amounts > threshold
- All expenses must be categorized

### Cash Management

- Minimum cash balance: IDR 10,000,000 (configurable)
- Low cash alerts sent when below minimum
- Multiple cash accounts supported (bank, petty cash)
- Cash reconciliation required monthly

### AR/AP

- AR collected using FIFO (oldest invoices first)
- AP paid using FIFO (oldest invoices first)
- Write-off bad debts after 180 days overdue (with approval)
- AR/AP reconciliation required monthly

---

## Edge Cases

### Payment Gateway Webhook Failure

- **Problem**: Midtrans payment successful but webhook not received
- **Solution**: Fallback polling every 5 minutes to check status
- **Alert**: Admin notified if webhook missing after 30 minutes

### Duplicate Expense Entry

- **Problem**: Staff enters same expense twice
- **Solution**: Duplicate detection (same amount, date, category)
- **UX**: "Similar expense found: Rent IDR 15M on Dec 1. Is this a duplicate?"

### Bank Reconciliation Mismatch

- **Problem**: Bank shows IDR 50M, system shows IDR 52M
- **Solution**: Review unrecorded transactions, timing differences
- **Workflow**: Flag for accountant review, manual adjustment if needed

### Negative Cash Balance

- **Problem**: More payments than cash available
- **Solution**: Block payments, require owner authorization
- **UX**: "Insufficient cash: Balance IDR 5M, Payment IDR 15M. Owner approval required."

---

## Future Enhancements

### Advanced Features
- Multi-currency support (USD, SGD, etc.)
- Automated invoicing (recurring invoices)
- Budget forecasting with AI
- Financial dashboards with KPIs
- Cost allocation by department/branch
- Variance analysis (budget vs actual)

### Integration
- Accounting software (Jurnal.id, Accurate, MYOB)
- Tax software (OnlinePajak, Klikpajak)
- Bank API integration (auto-sync transactions)
- Payroll integration
- E-invoicing (Faktur Pajak integration)

### Tax Compliance
- Automated PPN calculation and reporting
- PPh calculation (Article 21, 22, 23)
- E-Faktur integration (Indonesian tax invoice)
- Tax filing reminders
- Tax audit trail

---

## Success Metrics

- **Cash Flow Positive Days**: % of days with positive cash flow
- **Profit Margin**: Net profit margin % (target: >10%)
- **AR Collection Time**: Avg days to collect customer payments
- **AP Payment Timeliness**: % of supplier payments made on time
- **Expense Variance**: Actual vs budget variance %
- **Revenue Growth**: Month-over-month revenue growth %
- **Break-even Achievement**: % of days above break-even point

---

## Dependencies

- **Product Management** (03): COGS calculation
- **POS/Cashier** (05): Revenue from sales
- **Order Management** (06): Marketplace revenue
- **Customer Management** (07): AR tracking
- **Supplier & Purchasing** (08): AP tracking, COGS

---

**Last Updated**: 2024-12-13
