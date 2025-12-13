# Reports & Analytics 📊

**Category**: ANALYTICS, BUSINESS INTELLIGENCE
**Priority**: SHOULD HAVE (MVP)
**Phase**: 2-3

---

## Overview

Reports & Analytics provides comprehensive business intelligence through dashboards, reports, and data visualization. Store owners can analyze sales performance, product trends, customer behavior, financial health, and operational metrics to make data-driven decisions. The system generates real-time dashboards and exportable reports for business planning and tax compliance.

### Why This Matters

- **Data-Driven Decisions**: Make decisions based on actual data, not gut feeling
- **Performance Tracking**: Monitor KPIs and progress toward goals
- **Trend Identification**: Spot sales trends, seasonality, and opportunities
- **Problem Detection**: Identify issues early (slow products, cashflow problems)
- **Tax Compliance**: Generate reports required for Indonesian tax filing
- **Business Growth**: Understand what works and scale successful strategies

---

## Business Requirements

### Primary Goals

1. **Sales Analytics**: Track revenue, transactions, and sales trends
2. **Product Performance**: Identify best/worst selling products
3. **Customer Insights**: Understand customer behavior and lifetime value
4. **Financial Reports**: P&L, cash flow, AR/AP, expense analysis
5. **Inventory Reports**: Stock levels, turnover, dead stock
6. **Operational Metrics**: Staff performance, peak hours, efficiency
7. **Export & Sharing**: Export reports to PDF/Excel for stakeholders

### Problems Solved

- **Blind Spots**: See complete picture of business performance
- **Slow Decisions**: Access real-time data for quick decisions
- **Wasted Resources**: Identify and eliminate unprofitable activities
- **Missed Opportunities**: Spot trends and capitalize quickly
- **Tax Preparation**: Reports ready for accountant and tax office
- **Stakeholder Communication**: Professional reports for investors/partners

---

## Features

### 1. Executive Dashboard

**Description**: High-level overview of business performance with key metrics.

**Key Metrics Displayed**:

**Revenue Metrics**:
- Today's revenue (with % change vs yesterday/last week)
- This month revenue (with progress vs target)
- YTD (Year to Date) revenue
- Revenue trend chart (last 30 days)

**Transaction Metrics**:
- Total transactions today
- Average transaction value
- Items per transaction
- Payment method breakdown

**Inventory Metrics**:
- Total products
- Low stock alerts count
- Out of stock count
- Inventory value

**Customer Metrics**:
- New customers today/this month
- Total active customers
- Repeat customer rate
- Top customers by spend

**Financial Health**:
- Gross profit margin
- Net profit margin
- Accounts receivable total
- Accounts payable total
- Cash balance

**Dashboard Layout**:
```
┌──────────────────────────────────────────────────┐
│ 📊 Executive Dashboard - Dec 13, 2024            │
├──────────────────────────────────────────────────┤
│                                                  │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐│
│ │ Today       │ │ This Month  │ │ This Year   ││
│ │ IDR 8.5M    │ │ IDR 185M    │ │ IDR 1.8B    ││
│ │ ↑ 12%       │ │ 92% of goal │ │ ↑ 25%       ││
│ └─────────────┘ └─────────────┘ └─────────────┘│
│                                                  │
│ ┌────────────────────────────────────────────┐  │
│ │ Revenue Trend (Last 30 Days)               │  │
│ │ [Line Chart]                               │  │
│ └────────────────────────────────────────────┘  │
│                                                  │
│ ┌──────────────┐ ┌───────────────────────────┐ │
│ │ Top Products │ │ Low Stock Alerts (12)     │ │
│ │ 1. Indomie   │ │ - Indomie Goreng (85 PCS) │ │
│ │ 2. Minyak    │ │ - Indomilk (42 PCS)       │ │
│ │ 3. Gula      │ │ - Gula Pasir (55 KG)      │ │
│ └──────────────┘ └───────────────────────────┘ │
└──────────────────────────────────────────────────┘
```

---

### 2. Sales Reports

**Description**: Detailed sales analysis across multiple dimensions.

**Report Types**:

**Sales Summary Report**:
- Total sales by period (day/week/month/year)
- Sales trend (growing/declining)
- Comparison to previous period
- Breakdown by payment method
- Breakdown by channel (POS vs Marketplace)
- Breakdown by branch (multi-location)

**Sample Sales Summary**:
```
SALES SUMMARY REPORT
December 2024

Total Sales: IDR 185,000,000
Transactions: 1,247
Avg Transaction: IDR 148,358

Comparison to November:
Revenue: +7.5% (IDR 172M → IDR 185M)
Transactions: +5.2% (1,185 → 1,247)
Avg Transaction: +2.2%

By Channel:
- POS: IDR 125M (68%)
- Marketplace: IDR 60M (32%)

By Payment Method:
- Cash: IDR 70M (38%)
- QRIS: IDR 60M (32%)
- Credit (AR): IDR 35M (19%)
- Card: IDR 20M (11%)

Peak Days:
1. Dec 15 (Fri): IDR 12.5M
2. Dec 22 (Fri): IDR 11.8M
3. Dec 8 (Fri): IDR 10.2M

Peak Hours:
1. 10:00-11:00: IDR 28M
2. 14:00-15:00: IDR 25M
3. 16:00-17:00: IDR 22M
```

**Daily Sales Report**:
```
DAILY SALES REPORT
December 13, 2024

Total Sales: IDR 8,500,000
Transactions: 87
Customers: 65

Hourly Breakdown:
08:00-09:00: IDR 350K (3 transactions)
09:00-10:00: IDR 520K (5 transactions)
10:00-11:00: IDR 1,200K (12 transactions) 🔥
11:00-12:00: IDR 850K (8 transactions)
12:00-13:00: IDR 620K (6 transactions)
13:00-14:00: IDR 480K (4 transactions)
14:00-15:00: IDR 1,100K (11 transactions) 🔥
15:00-16:00: IDR 950K (9 transactions)
16:00-17:00: IDR 1,050K (10 transactions)
17:00-18:00: IDR 720K (7 transactions)
18:00-19:00: IDR 520K (8 transactions)
19:00-20:00: IDR 140K (4 transactions)

Top Selling Products:
1. Indomie Goreng - 245 PCS (IDR 735K)
2. Indomilk Susu - 86 PCS (IDR 516K)
3. Minyak Goreng 2L - 24 PCS (IDR 840K)
```

---

### 3. Product Performance Reports

**Description**: Analyze product sales, profitability, and inventory turnover.

**Report Types**:

**Best Selling Products**:
```
TOP 20 BEST SELLING PRODUCTS
December 2024

Rank | Product           | Units Sold | Revenue    | Profit
-----|-------------------|------------|------------|----------
1    | Indomie Goreng    | 12,500 PCS | IDR 37.5M  | IDR 15M
2    | Indomie Soto      | 8,200 PCS  | IDR 24.6M  | IDR 9.8M
3    | Minyak Goreng 2L  | 1,800 PCS  | IDR 63M    | IDR 18M
4    | Gula Pasir 1kg    | 1,200 PCS  | IDR 18M    | IDR 4.8M
5    | Indomilk Susu     | 2,400 PCS  | IDR 14.4M  | IDR 5.8M
...
```

**Worst Selling Products** (Dead Stock):
```
SLOW-MOVING PRODUCTS
December 2024

Product              | Stock | Last Sale  | Days Since | Action
---------------------|-------|------------|------------|--------
Tepung Tapioka 1kg   | 85    | Nov 15     | 28 days    | Promo
Kecap Manis ABC 600ml| 42    | Oct 28     | 46 days    | Return
Sabun Mandi Lifebuoy | 156   | Nov 22     | 21 days    | Discount
Shampoo Sunsilk      | 38    | Oct 10     | 64 days    | Clearance
```

**Product Profitability Analysis**:
```
PRODUCT PROFITABILITY
December 2024

Product          | Revenue   | COGS      | Gross Profit | Margin
-----------------|-----------|-----------|--------------|-------
Minyak Goreng 2L | IDR 63M   | IDR 45M   | IDR 18M      | 28.6%
Indomie Goreng   | IDR 37.5M | IDR 22.5M | IDR 15M      | 40.0%
Gula Pasir 1kg   | IDR 18M   | IDR 13.2M | IDR 4.8M     | 26.7%
```

**Inventory Turnover**:
```
INVENTORY TURNOVER REPORT
December 2024

Product          | Avg Stock | Sales (Units) | Turnover Ratio
-----------------|-----------|---------------|----------------
Indomie Goreng   | 500 PCS   | 12,500 PCS    | 25x (Excellent)
Indomilk Susu    | 200 PCS   | 2,400 PCS     | 12x (Good)
Minyak Goreng    | 150 PCS   | 1,800 PCS     | 12x (Good)
Tepung Tapioka   | 100 PCS   | 15 PCS        | 0.15x (Poor) ⚠️
```

---

### 4. Customer Analytics

**Description**: Understand customer behavior, segments, and lifetime value.

**Report Types**:

**Customer Segmentation** (RFM Analysis):
```
CUSTOMER SEGMENTATION
December 2024

Segment     | Count | Avg LTV    | Description
------------|-------|------------|---------------------------
Champions   | 28    | IDR 125M   | Frequent buyers, high spend
Loyal       | 45    | IDR 85M    | Regular customers
Potential   | 67    | IDR 42M    | Recent customers, good potential
At Risk     | 23    | IDR 65M    | Haven't bought recently
Lost        | 15    | IDR 38M    | No purchase > 90 days

R = Recency (how recently purchased)
F = Frequency (how often purchased)
M = Monetary (how much spent)
```

**Top Customers by Revenue**:
```
TOP 20 CUSTOMERS
December 2024

Rank | Customer       | Tier | Orders | Revenue   | Avg Order
-----|----------------|------|--------|-----------|----------
1    | Toko Makmur    | A    | 18     | IDR 8.5M  | IDR 472K
2    | Warung Sari    | A    | 15     | IDR 6.8M  | IDR 453K
3    | CV Mitra       | A    | 12     | IDR 5.2M  | IDR 433K
4    | Toko Sejahtera | A    | 14     | IDR 4.9M  | IDR 350K
5    | Ibu Siti       | B    | 32     | IDR 3.2M  | IDR 100K
...
```

**New vs Returning Customers**:
```
CUSTOMER ACQUISITION & RETENTION
December 2024

New Customers: 87 (42% of total transactions)
Returning Customers: 122 (58% of total transactions)

New Customer Revenue: IDR 38M (21%)
Returning Customer Revenue: IDR 147M (79%)

Repeat Purchase Rate: 58%
Customer Retention Rate: 72%
Churn Rate: 28%
```

**Customer Lifetime Value (LTV)**:
```
CUSTOMER LTV ANALYSIS

Average Customer Lifetime Value: IDR 8,500,000

By Tier:
- Tier A (Wholesale): IDR 125,000,000 avg
- Tier B (Retail): IDR 3,200,000 avg
- Tier C (VIP): IDR 18,500,000 avg

LTV to CAC Ratio: 8.5:1 (Excellent)
(Customer Acquisition Cost: IDR 1,000,000)

Payback Period: 2.3 months
```

---

### 5. Financial Reports

**Description**: Comprehensive financial analysis for business and tax purposes.

**Report Types**:

**Profit & Loss Statement**:
(See Feature 09 - Financial Management for detailed P&L)

**Cash Flow Statement**:
(See Feature 09 - Financial Management for detailed Cash Flow)

**Accounts Receivable Aging**:
```
AR AGING REPORT
As of December 13, 2024

Total AR: IDR 35,000,000

Age Bracket    | Amount       | % of Total | # Invoices
---------------|--------------|------------|------------
0-30 days      | IDR 22M      | 63%        | 45
31-60 days     | IDR 8M       | 23%        | 18
61-90 days     | IDR 3.5M     | 10%        | 8
90+ days       | IDR 1.5M     | 4% ⚠️      | 5

Collection Risk: Low (96% current/recent)

Top 5 Overdue Customers:
1. Toko Sejahtera - IDR 850K (92 days) 🚨
2. Warung Jaya - IDR 320K (65 days)
3. CV Mitra - IDR 280K (58 days)
...
```

**Expense Analysis**:
```
EXPENSE BREAKDOWN
December 2024

Total Expenses: IDR 49,000,000

By Category:
1. Salaries & Wages: IDR 18M (37%)
2. Rent: IDR 15M (31%)
3. Marketing: IDR 4.2M (9%)
4. Utilities: IDR 3.5M (7%)
5. Administrative: IDR 2.8M (6%)
6. Maintenance: IDR 1.5M (3%)
7. Insurance: IDR 1.2M (2%)
8. Other: IDR 2.8M (6%)

Budget Variance:
- Under Budget: Utilities (-12%), Marketing (-16%)
- Over Budget: Salaries (+8%) ⚠️

Year-over-Year: +15% (Dec 2023: IDR 42.6M)
```

---

### 6. Inventory Reports

**Description**: Analyze stock levels, movement, and valuation.

**Report Types**:

**Stock Level Report**:
```
INVENTORY STATUS
As of December 13, 2024

Total Products: 487
In Stock: 452 (93%)
Low Stock: 28 (6%) ⚠️
Out of Stock: 7 (1%) ⚠️

Total Inventory Value: IDR 85,000,000

By Category:
- Mie Instan: 125 products, IDR 28M
- Minuman: 87 products, IDR 18M
- Snack: 156 products, IDR 22M
- Sembako: 65 products, IDR 12M
- Others: 54 products, IDR 5M

Low Stock Alerts:
1. Indomie Goreng - 85 PCS (Reorder at 100)
2. Indomilk Susu - 42 PCS (Reorder at 50)
3. Gula Pasir - 55 KG (Reorder at 60)
...
```

**Stock Movement Report**:
```
STOCK MOVEMENT
December 1-13, 2024

Product          | Opening | Purchases | Sales | Adjustments | Closing
-----------------|---------|-----------|-------|-------------|--------
Indomie Goreng   | 500     | +800      | -1,215| 0           | 85
Indomilk Susu    | 180     | +200      | -338  | -20 (damaged)| 42
Minyak Goreng 2L | 120     | +150      | -195  | 0           | 75
```

**Dead Stock Analysis**:
```
DEAD STOCK REPORT
Products with no sales > 60 days

Product              | Stock | Value     | Last Sale | Days
---------------------|-------|-----------|-----------|-----
Shampoo Sunsilk 170ml| 38    | IDR 228K  | Oct 10    | 64
Kecap Manis ABC 600ml| 42    | IDR 336K  | Oct 28    | 46
Sabun Dettol 90g     | 28    | IDR 196K  | Nov 5     | 38

Total Dead Stock Value: IDR 760,000

Recommendation: Clearance sale 30-50% off
```

---

### 7. Operational Reports

**Description**: Track staff performance and operational efficiency.

**Report Types**:

**Staff Performance**:
```
CASHIER PERFORMANCE
December 2024

Cashier      | Transactions | Revenue   | Avg Trans | Errors
-------------|--------------|-----------|-----------|--------
Budi         | 387          | IDR 58M   | IDR 150K  | 2
Siti         | 342          | IDR 52M   | IDR 152K  | 1
Ahmad        | 298          | IDR 45M   | IDR 151K  | 4
Rina         | 220          | IDR 30M   | IDR 136K  | 3

Best Performer: Budi (highest revenue, low errors)
Training Needed: Ahmad (higher error rate)
```

**Peak Hours Analysis**:
```
PEAK HOURS REPORT
December 2024

Busiest Hours:
1. 10:00-11:00 AM - 156 transactions (Avg: IDR 28M/month)
2. 14:00-15:00 PM - 142 transactions (Avg: IDR 25M/month)
3. 16:00-17:00 PM - 128 transactions (Avg: IDR 22M/month)

Slowest Hours:
1. 08:00-09:00 AM - 18 transactions
2. 19:00-20:00 PM - 22 transactions

Recommendation:
- Schedule 3 cashiers during peak hours (10-11 AM, 2-5 PM)
- Reduce to 1 cashier during slow hours (8-9 AM, 7-8 PM)
```

---

### 8. Tax Reports (Indonesian Compliance)

**Description**: Generate reports required for Indonesian tax filing.

**Report Types**:

**PPN (VAT) Report**:
```
LAPORAN PPN (PAJAK PERTAMBAHAN NILAI)
December 2024

Penjualan (Sales):
Penjualan Bruto: IDR 185,000,000
Retur: IDR 3,500,000
Penjualan Netto: IDR 181,500,000
PPN Keluaran (11%): IDR 19,965,000

Pembelian (Purchases):
Pembelian Bruto: IDR 95,000,000
Retur: IDR 2,000,000
Pembelian Netto: IDR 93,000,000
PPN Masukan (11%): IDR 10,230,000

PPN Kurang/(Lebih) Bayar:
PPN Keluaran: IDR 19,965,000
PPN Masukan: (IDR 10,230,000)
PPN Terutang: IDR 9,735,000

Keterangan:
- NPWP: 01.234.567.8-901.000
- Masa Pajak: Desember 2024
- Faktur Pajak: 125 dokumen
```

**PPh (Income Tax) Report**:
```
LAPORAN PPh PASAL 21
(Employee Withholding Tax)
December 2024

Total Salaries Paid: IDR 18,000,000

Employee | Gross Salary | Deductions | Taxable | Tax Withheld
---------|--------------|------------|---------|-------------
Budi     | IDR 6M       | IDR 500K   | IDR 5.5M| IDR 275K
Siti     | IDR 5M       | IDR 400K   | IDR 4.6M| IDR 230K
Ahmad    | IDR 4M       | IDR 300K   | IDR 3.7M| IDR 185K
Rina     | IDR 3M       | IDR 250K   | IDR 2.75M| IDR 138K

Total PPh 21: IDR 828,000
```

---

### 9. Export & Scheduling

**Description**: Export reports and schedule automated delivery.

**Export Formats**:
- PDF (formatted, print-ready)
- Excel (editable, with formulas)
- CSV (raw data for analysis)

**Scheduled Reports** (Pro/Enterprise):
- Daily sales summary (email at 8 AM)
- Weekly performance report (email Monday 9 AM)
- Monthly financial report (email 1st of month)
- Low stock alerts (email when triggered)

**User Flow** (Schedule Report):
1. Owner navigates to Reports > Sales Summary
2. Clicks [Schedule Report]
3. Configures:
   - Frequency: Daily
   - Time: 08:00 AM
   - Recipients: owner@store.com, manager@store.com
   - Format: PDF + Excel
4. Saves schedule
5. System auto-sends report daily at 8 AM

---

## Use Cases

### Use Case 1: Monthly Business Review

**Scenario**: Owner reviews December performance at month-end.

**Steps**:
1. Jan 2: Owner logs in to dashboard
2. Navigates to: Reports > Executive Dashboard
3. Reviews December metrics:
   - Revenue: IDR 185M (target IDR 200M, 92.5%)
   - Transactions: 1,247
   - New customers: 87
   - Profit margin: 16.2%
4. Generates detailed reports:
   - Sales Summary Report (PDF)
   - P&L Statement (Excel)
   - Product Performance (Excel)
5. Analyzes findings:
   - Revenue short of target by IDR 15M
   - Top product: Indomie (IDR 62M, 34%)
   - Dead stock value: IDR 760K
   - Net profit: IDR 30M (good)
6. Makes decisions:
   - Increase marketing in January
   - Clear dead stock with 50% sale
   - Target: IDR 210M for January
7. Exports all reports
8. Presents to team meeting

---

### Use Case 2: Identify Slow-Moving Products

**Scenario**: Stock taking reveals high inventory of slow-moving items.

**Steps**:
1. Staff generates: Dead Stock Report
2. Finds 15 products with no sales > 60 days
3. Total value: IDR 2.5M (tied up capital)
4. Owner reviews products:
   - Shampoo Sunsilk: 38 PCS (64 days no sale)
   - Kecap Manis ABC: 42 PCS (46 days no sale)
   - Sabun Dettol: 28 PCS (38 days no sale)
5. Owner decides: Clearance sale
6. Creates promotion: "50% off slow movers"
7. 2 weeks later: 85% of dead stock sold
8. Recovered: IDR 2.1M cash
9. Lesson: Stock only fast-moving items

---

## Business Rules

### Report Data

- Real-time data (updates every 5 minutes)
- Historical data retained: 3 years (Enterprise), 1 year (Pro/Basic)
- Deleted data not included in reports
- Cancelled transactions excluded from revenue

### Access Control

- Owner: Access to all reports
- Admin: Access to operational reports (not financial)
- Staff: Access to own performance reports only
- Cashier: No access to reports

### Export Limits

- Free: 5 exports/month
- Basic: 50 exports/month
- Pro: Unlimited exports
- Enterprise: Unlimited + automated scheduling

---

## Future Enhancements

### Advanced Analytics
- Predictive analytics (AI-driven forecasting)
- What-if scenarios (simulate business decisions)
- Cohort analysis (track customer groups over time)
- Product affinity analysis (frequently bought together)
- Price elasticity analysis

### Visualizations
- Interactive dashboards (drill-down capability)
- Heat maps (sales by hour/day)
- Geospatial maps (sales by location)
- Real-time dashboards (live updates)
- Mobile analytics app

### Integrations
- Google Data Studio
- Microsoft Power BI
- Tableau
- Export to accounting software
- API for custom integrations

---

## Success Metrics

- **Report Usage**: # of reports generated per month
- **Dashboard Views**: # of dashboard visits per day
- **Data-Driven Decisions**: % of decisions backed by reports
- **Report Accuracy**: % of reports error-free
- **User Satisfaction**: Report usefulness rating (1-5)

---

## Dependencies

- All features (01-10): Reports aggregate data from all modules
- Tenant Management (02): Tenant-scoped reports
- Financial Management (09): Financial report data

---

**Last Updated**: 2024-12-13
