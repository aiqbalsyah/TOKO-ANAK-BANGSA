# TOKO ANAK BANGSA - Features Documentation

Complete feature set for the multi-tenant POS & Marketplace platform for Indonesian SMEs.

---

## Table of Contents

1. [Platform Overview](#platform-overview)
2. [User Roles & Permissions](#user-roles--permissions)
3. [Core Features](#core-features)
4. [Feature Roadmap](#feature-roadmap)
5. [Technical Requirements](#technical-requirements)

---

## Platform Overview

### Vision
Empower Indonesian small and medium enterprises (SMEs) with an integrated POS and marketplace platform that handles both in-store and online sales.

### Platform Components

1. **Store Portal** - POS & store management for store owners/staff
2. **Marketplace** - Public e-commerce platform for customers
3. **Company Profile** - Platform landing page and information
4. **Platform Admin** - Platform administration and management
5. **API Backend** - Centralized Flask API for all operations

### Business Model

- **Multi-tenant**: Each store is an isolated tenant with own data
- **Subscription-based**: Free, Basic, Pro, Enterprise tiers
- **Transaction fees**: Small percentage on marketplace sales
- **Value-added services**: Premium features, integrations, support

---

## User Roles & Permissions

### Store Roles

#### 1. Owner
- Full access to everything
- Can manage users and permissions
- Can view all reports and analytics
- Can configure store settings
- Can manage subscriptions

#### 2. Admin
- Can manage products, inventory, customers
- Can process orders and refunds
- Can view reports
- Cannot manage users or subscriptions

#### 3. Staff
- Can manage products and inventory
- Can process orders
- Limited report access
- Cannot manage users

#### 4. Cashier
- Can process POS transactions only
- Can search products
- Cannot modify inventory
- Cannot access reports

### Platform Roles

#### 1. Platform Admin
- Can manage all tenants
- Can view platform analytics
- Can moderate content
- Can manage subscriptions
- System configuration access

#### 2. Platform Support
- Can view tenant data (read-only)
- Can assist with issues
- Cannot modify data

### Customer Roles

#### 1. Guest
- Can browse marketplace
- Can view products and stores
- Must register to purchase

#### 2. Registered Customer
- Can purchase from marketplace
- Can manage orders
- Can save favorites
- Can write reviews

---

## Core Features

### 1. Authentication & Authorization 🔐

#### Features
- **Email/Password Registration & Login**
  - Email verification
  - Password reset flow
  - Remember me functionality

- **Social Login**
  - Google OAuth
  - Facebook OAuth (future)

- **Role-Based Access Control (RBAC)**
  - Dynamic permissions per role
  - Resource-level permissions
  - Action-level permissions

- **Multi-Factor Authentication (MFA)** (Pro/Enterprise)
  - SMS verification
  - Authenticator app

- **Session Management**
  - Automatic logout
  - Session timeout
  - Device management

#### API Endpoints
```
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/logout
POST   /api/auth/verify-email
POST   /api/auth/forgot-password
POST   /api/auth/reset-password
POST   /api/auth/google
GET    /api/auth/me
PUT    /api/auth/me
```

---

### 2. Tenant (Store) Management 🏪

#### Features
- **Store Registration**
  - Business information
  - Owner details
  - Store category/type
  - Automatic slug generation

- **Store Settings**
  - Store name and description
  - Business hours
  - Contact information
  - Logo and banner upload
  - Currency settings
  - Tax configuration

- **Multi-location Support** (Pro/Enterprise)
  - Multiple store branches
  - Centralized inventory
  - Branch-specific reports

- **Subscription Management**
  - Plan selection (Free/Basic/Pro/Enterprise)
  - Billing information
  - Usage tracking
  - Plan upgrades/downgrades

#### API Endpoints
```
POST   /api/tenants
GET    /api/tenants/:id
PUT    /api/tenants/:id
DELETE /api/tenants/:id
GET    /api/tenants/:id/settings
PUT    /api/tenants/:id/settings
GET    /api/tenants/:id/subscription
PUT    /api/tenants/:id/subscription
```

---

### 3. Product Management 📦

#### Features
- **Product CRUD**
  - Add/edit/delete products
  - Product name, description, SKU
  - Product categories
  - Product tags
  - Product status (active/inactive)

- **Product Images**
  - Multiple images per product
  - Image upload to Firebase Storage
  - Automatic thumbnail generation
  - Image reordering
  - Alt text for SEO

- **Product Variants**
  - Size variants (S, M, L, XL, etc.)
  - Color variants
  - Custom variant types
  - Variant-specific pricing
  - Variant-specific SKU
  - Variant images

- **Multi-tier Pricing** (Indonesia-specific)
  - **Tier A (Wholesale)**: Lowest price for resellers
  - **Tier B (Retail)**: Standard retail price
  - **Tier C (Premium)**: Suggested marketplace price
  - Price history tracking

- **Unit Packages** (Indonesia-specific)
  - **DUS (Box)**: e.g., 1 DUS = 12 PCS
  - **PACK**: e.g., 1 PACK = 6 PCS
  - **PCS (Pieces)**: Single unit
  - Automatic conversion
  - Package-based inventory

- **Barcode/QR Code**
  - Barcode scanning support
  - QR code generation
  - Multiple barcodes per product

- **Product Search & Filter**
  - Full-text search
  - Category filter
  - Price range filter
  - Stock status filter
  - Tag filter

#### API Endpoints
```
GET    /api/products
POST   /api/products
GET    /api/products/:id
PUT    /api/products/:id
DELETE /api/products/:id
POST   /api/products/:id/images
DELETE /api/products/:id/images/:imageId
POST   /api/products/:id/variants
PUT    /api/products/:id/variants/:variantId
DELETE /api/products/:id/variants/:variantId
GET    /api/products/search
GET    /api/categories
POST   /api/categories
```

---

### 4. Inventory Management 📊

#### Features
- **Stock Tracking**
  - Real-time stock levels
  - Stock by variant
  - Stock by location (multi-branch)
  - Reserved stock (pending orders)

- **Stock Adjustments**
  - Manual stock in/out
  - Reason codes
  - Adjustment history
  - Audit trail

- **Low Stock Alerts**
  - Configurable thresholds
  - Email notifications
  - Dashboard warnings
  - Auto-reorder suggestions

- **Stock Transfers** (Multi-branch)
  - Transfer between locations
  - Transfer requests
  - Transfer tracking
  - Transfer history

- **Inventory Reports**
  - Current stock levels
  - Stock movement history
  - Stock value report
  - Dead stock analysis

#### API Endpoints
```
GET    /api/inventory
GET    /api/inventory/:productId
POST   /api/inventory/adjust
POST   /api/inventory/transfer
GET    /api/inventory/alerts
GET    /api/inventory/reports/stock-level
GET    /api/inventory/reports/movement
```

---

### 5. Point of Sale (POS) 💰

#### Features
- **POS Interface**
  - Product search by name/SKU/barcode
  - Quick add to cart
  - Quantity adjustment
  - Price override (with permission)
  - Discount application
  - Note/memo field

- **Cart Management**
  - Add/remove items
  - Update quantities
  - Apply discounts (item/cart level)
  - Apply taxes
  - Calculate total automatically

- **Payment Processing**
  - **Cash Payment**
    - Cash amount input
    - Change calculation
    - Cash drawer integration
  - **Card Payment** (Basic+)
    - Credit/debit card
    - Manual entry or terminal
  - **Digital Wallet** (Pro+)
    - GoPay, OVO, Dana
    - QR code display
  - **Bank Transfer** (Pro+)
    - Virtual account
    - Manual verification
  - **Split Payment** (Enterprise)
    - Multiple payment methods in one transaction

- **Receipt Generation**
  - Thermal printer support
  - PDF receipt
  - Email receipt
  - WhatsApp receipt (Pro+)
  - Customizable templates

- **Customer Lookup**
  - Search by name/phone
  - Quick add customer
  - Link transaction to customer
  - Customer credit/debt tracking

- **Offline Mode** (Pro+)
  - Queue transactions when offline
  - Auto-sync when online
  - Local data caching

#### API Endpoints
```
POST   /api/pos/transactions
GET    /api/pos/transactions/:id
POST   /api/pos/transactions/:id/payment
GET    /api/pos/products/search
GET    /api/pos/customers/search
POST   /api/pos/receipts/:transactionId/print
POST   /api/pos/receipts/:transactionId/email
```

---

### 6. Order Management 📋

#### Features
- **Order Processing**
  - Create orders (POS/marketplace)
  - Order status tracking
  - Order timeline/history
  - Order notes

- **Order Status Flow**
  ```
  Pending → Confirmed → Processing → Packed → Shipped → Delivered → Completed
          ↘ Cancelled
  ```

- **Order Details**
  - Order number generation
  - Customer information
  - Item list with variants
  - Payment details
  - Shipping details
  - Status history

- **Order Search & Filter**
  - By order number
  - By customer
  - By date range
  - By status
  - By payment method

- **Returns & Refunds**
  - Return request
  - Return approval workflow
  - Refund processing
  - Inventory return

- **Order Fulfillment**
  - Pick list generation
  - Packing slip
  - Shipping label
  - Tracking number

#### API Endpoints
```
GET    /api/orders
POST   /api/orders
GET    /api/orders/:id
PUT    /api/orders/:id
DELETE /api/orders/:id
PUT    /api/orders/:id/status
POST   /api/orders/:id/refund
GET    /api/orders/search
```

---

### 7. Customer Management 👥

#### Features
- **Customer Database**
  - Customer profile
  - Contact information
  - Shipping addresses
  - Purchase history
  - Customer notes

- **Customer Credit (AR - Accounts Receivable)**
  - Credit limit per customer
  - Credit balance tracking
  - Credit transactions
  - Payment history
  - Overdue alerts
  - Credit reports

- **Customer Segmentation**
  - Regular/VIP/Wholesale
  - Purchase frequency
  - Total spent
  - Custom tags

- **Customer Loyalty** (Pro+)
  - Points system
  - Rewards program
  - Tier levels
  - Redemption

#### API Endpoints
```
GET    /api/customers
POST   /api/customers
GET    /api/customers/:id
PUT    /api/customers/:id
DELETE /api/customers/:id
GET    /api/customers/:id/orders
GET    /api/customers/:id/credit
POST   /api/customers/:id/credit/add
POST   /api/customers/:id/credit/payment
```

---

### 8. Supplier & Purchasing Management 🏭

#### Features
- **Supplier Database**
  - Supplier profile
  - Contact information
  - Product catalog
  - Payment terms
  - Supplier notes

- **Purchase Orders**
  - Create PO
  - Send PO to supplier
  - PO approval workflow
  - PO tracking
  - Receive goods

- **Accounts Payable (AP - Store Debt to Suppliers)**
  - Outstanding balance per supplier
  - Payment due dates
  - Payment history
  - Overdue alerts
  - AP aging report

- **Supplier Payments**
  - Record payments
  - Partial payments
  - Payment methods
  - Payment receipts

#### API Endpoints
```
GET    /api/suppliers
POST   /api/suppliers
GET    /api/suppliers/:id
PUT    /api/suppliers/:id
GET    /api/purchase-orders
POST   /api/purchase-orders
GET    /api/purchase-orders/:id
PUT    /api/purchase-orders/:id/status
POST   /api/purchase-orders/:id/receive
GET    /api/suppliers/:id/payables
POST   /api/suppliers/:id/payments
```

---

### 9. Financial Management 💳

#### Features
- **Cash Flow Management**
  - Cash in/out recording
  - Opening/closing balance
  - Daily cash summary
  - Cash reconciliation

- **Payment Methods**
  - Cash
  - Credit/Debit Card
  - Bank Transfer
  - Digital Wallets (GoPay, OVO, Dana)
  - Customer Credit
  - Split payments

- **Payment Gateway Integration**
  - **Midtrans** (Primary)
    - Credit card
    - Virtual account
    - E-wallet
    - QR code
    - Installment (Pro+)

- **Expense Tracking**
  - Record expenses
  - Expense categories
  - Expense reports
  - Receipt attachments

- **Financial Reports**
  - Profit & Loss statement
  - Cash flow statement
  - Balance sheet
  - Sales summary
  - Expense summary

#### API Endpoints
```
GET    /api/cashflow
POST   /api/cashflow/in
POST   /api/cashflow/out
GET    /api/cashflow/summary
POST   /api/payments/midtrans/charge
POST   /api/payments/midtrans/notification
GET    /api/expenses
POST   /api/expenses
GET    /api/reports/profit-loss
GET    /api/reports/cashflow
```

---

### 10. Marketplace Features 🛒

#### Features
- **Store Discovery**
  - Browse stores
  - Search stores
  - Store categories
  - Featured stores
  - Store ratings

- **Product Catalog**
  - Browse products across stores
  - Product search
  - Category navigation
  - Filter & sort
  - Product comparison

- **Product Details**
  - Images gallery
  - Description
  - Variants selector
  - Price tiers (if applicable)
  - Stock availability
  - Reviews & ratings

- **Shopping Cart**
  - Add to cart
  - Cart management
  - Multiple stores in cart
  - Cart summary

- **Checkout**
  - Guest or registered checkout
  - Shipping address
  - Shipping method selection
  - Payment method selection
  - Order review
  - Order confirmation

- **Shipping Integration**
  - **RajaOngkir API**
    - Calculate shipping cost
    - Multiple courier support (JNE, TIKI, PosIndonesia)
    - Real-time rates
    - Origin-destination calculation

- **Product Reviews**
  - Rate products (1-5 stars)
  - Write reviews
  - Upload images
  - Helpful votes
  - Store responses

- **Wishlist** (Registered users)
  - Save favorites
  - Share wishlist
  - Move to cart

#### API Endpoints
```
GET    /api/marketplace/stores
GET    /api/marketplace/stores/:slug
GET    /api/marketplace/products
GET    /api/marketplace/products/:id
POST   /api/marketplace/cart
GET    /api/marketplace/cart
PUT    /api/marketplace/cart/:itemId
DELETE /api/marketplace/cart/:itemId
POST   /api/marketplace/checkout
POST   /api/marketplace/shipping/calculate
GET    /api/marketplace/reviews/:productId
POST   /api/marketplace/reviews
```

---

### 11. Reports & Analytics 📈

#### Features
- **Sales Reports**
  - Daily sales summary
  - Sales by period (daily/weekly/monthly)
  - Sales by product
  - Sales by category
  - Sales by customer
  - Sales by payment method
  - Sales trend analysis

- **Product Reports**
  - Best sellers
  - Worst sellers
  - Product performance
  - Stock value report
  - Dead stock report

- **Customer Reports**
  - Customer acquisition
  - Customer retention
  - Customer lifetime value
  - Top customers
  - Customer segmentation

- **Financial Reports**
  - Revenue report
  - Expense report
  - Profit margin
  - Cash flow report
  - AR/AP aging

- **Dashboard**
  - Today's sales
  - Weekly comparison
  - Monthly targets
  - Quick stats
  - Recent transactions
  - Low stock alerts
  - Pending orders

- **Export Functionality**
  - Export to CSV
  - Export to Excel
  - Export to PDF
  - Scheduled reports (Pro+)

#### API Endpoints
```
GET    /api/reports/sales/summary
GET    /api/reports/sales/by-product
GET    /api/reports/sales/by-category
GET    /api/reports/sales/trend
GET    /api/reports/products/best-sellers
GET    /api/reports/customers/top
GET    /api/reports/financial/revenue
GET    /api/reports/export
```

---

### 12. Notifications 🔔

#### Features
- **In-App Notifications**
  - New orders
  - Low stock alerts
  - Payment received
  - Customer messages
  - System announcements

- **Email Notifications**
  - Order confirmation
  - Shipping updates
  - Payment receipts
  - Password reset
  - Weekly reports

- **WhatsApp Notifications** (Pro+)
  - Order notifications
  - Receipt delivery
  - Shipping updates
  - Marketing messages

- **SMS Notifications** (Enterprise)
  - Order updates
  - OTP verification
  - Critical alerts

#### API Endpoints
```
GET    /api/notifications
PUT    /api/notifications/:id/read
PUT    /api/notifications/read-all
DELETE /api/notifications/:id
POST   /api/notifications/settings
```

---

### 13. Settings & Configuration ⚙️

#### Features
- **Store Settings**
  - Business information
  - Operating hours
  - Contact details
  - Logo and branding
  - Tax configuration
  - Currency settings

- **User Management**
  - Add/remove users
  - Assign roles
  - Set permissions
  - User activity log

- **Receipt Customization**
  - Header/footer text
  - Logo placement
  - Font selection
  - Additional information

- **Notification Preferences**
  - Email settings
  - WhatsApp settings
  - In-app settings
  - Notification types

- **Integration Settings**
  - Payment gateway
  - Shipping provider
  - Accounting software (future)

- **Printer Configuration**
  - Thermal printer setup
  - Label printer setup
  - Test print

#### API Endpoints
```
GET    /api/settings
PUT    /api/settings
GET    /api/settings/users
POST   /api/settings/users
PUT    /api/settings/users/:id
DELETE /api/settings/users/:id
PUT    /api/settings/notifications
PUT    /api/settings/integrations
```

---

### 14. Platform Admin Features 🛠️

#### Features
- **Tenant Management**
  - View all tenants
  - Tenant details
  - Suspend/activate tenants
  - Tenant statistics

- **Platform Analytics**
  - Total revenue
  - Active tenants
  - Transaction volume
  - Growth metrics
  - System health

- **Content Moderation**
  - Review product listings
  - Review store information
  - Handle reports
  - Ban inappropriate content

- **Subscription Management**
  - View all subscriptions
  - Manage plans
  - Process upgrades/downgrades
  - Handle billing issues

- **Support System**
  - View support tickets
  - Tenant impersonation (with audit)
  - System logs
  - Error tracking

#### API Endpoints
```
GET    /api/admin/tenants
GET    /api/admin/tenants/:id
PUT    /api/admin/tenants/:id/status
GET    /api/admin/analytics
GET    /api/admin/moderation/pending
PUT    /api/admin/moderation/:id/approve
PUT    /api/admin/moderation/:id/reject
GET    /api/admin/subscriptions
```

---

## Feature Roadmap

### Phase 1: MVP (Sprint 1-3)

**Priority: HIGH** ⭐⭐⭐

- ✅ Authentication & Authorization
- ✅ Tenant Management (basic)
- ✅ Product Management (basic, no variants)
- ✅ Inventory Tracking (basic)
- ✅ POS System (cash only)
- ✅ Order Management (basic)
- ✅ Customer Database
- ✅ Basic Dashboard
- ✅ Basic Reports

**Goal**: Store owners can register, add products, and process in-store cash sales.

---

### Phase 2: Enhanced POS (Sprint 4-6)

**Priority: HIGH** ⭐⭐⭐

- Product Variants
- Multi-tier Pricing (A/B/C)
- Unit Packages (DUS/PACK/PCS)
- Multiple Payment Methods
- Receipt Customization
- Customer Credit (AR)
- Low Stock Alerts
- Enhanced Reports

**Goal**: Full-featured POS system for Indonesian SMEs.

---

### Phase 3: Marketplace (Sprint 7-10)

**Priority: MEDIUM** ⭐⭐

- Store Discovery
- Product Catalog
- Shopping Cart
- Checkout Flow
- Shipping Integration (RajaOngkir)
- Payment Gateway (Midtrans)
- Product Reviews
- Order Tracking

**Goal**: Launch public marketplace for customer purchases.

---

### Phase 4: Financial Management (Sprint 11-13)

**Priority: MEDIUM** ⭐⭐

- Supplier Management
- Purchase Orders
- Accounts Payable (AP)
- Enhanced Customer Credit
- Cash Flow Management
- Expense Tracking
- Financial Reports
- Multi-location Support

**Goal**: Complete financial management for growing businesses.

---

### Phase 5: Advanced Features (Sprint 14+)

**Priority: LOW** ⭐

- WhatsApp Integration
- Email Marketing
- Customer Loyalty
- Offline Mode
- Advanced Analytics
- API Access for Integrations
- Mobile Apps (iOS/Android)
- Multi-currency
- International Shipping

**Goal**: Enterprise-grade features for scaling businesses.

---

## Technical Requirements

### Performance

- **Page Load**: < 2 seconds
- **API Response**: < 500ms (p95)
- **Search Results**: < 300ms
- **Image Load**: < 1 second
- **Database Queries**: < 100ms

### Scalability

- Support 10,000+ tenants
- Handle 100,000+ products per tenant
- Process 1,000+ transactions/minute
- Store 1M+ customer records

### Security

- HTTPS everywhere
- RBAC for all resources
- Multi-tenant data isolation
- Regular security audits
- PCI DSS compliance (for payments)
- GDPR compliance (for data)

### Availability

- 99.9% uptime SLA
- Automated backups (daily)
- Disaster recovery plan
- Zero-downtime deployments

### Compliance

- Indonesian tax regulations
- Data residency (Indonesia)
- E-commerce regulations
- Privacy laws

---

## Success Metrics

### Business Metrics

- **Active Tenants**: Number of stores actively using the platform
- **GMV (Gross Merchandise Value)**: Total sales value
- **Transaction Count**: Total transactions processed
- **Customer Retention**: % of tenants staying after 3/6/12 months
- **Revenue**: Platform revenue from subscriptions + fees

### Technical Metrics

- **System Uptime**: 99.9%+
- **API Response Time**: < 500ms
- **Error Rate**: < 0.1%
- **Page Load Time**: < 2s
- **Search Performance**: < 300ms

### User Metrics

- **Daily Active Users (DAU)**: Store owners logging in daily
- **Feature Adoption**: % using each feature
- **Time to First Sale**: Time from registration to first transaction
- **Customer Satisfaction**: NPS score > 50

---

## API Architecture

### RESTful Principles

- Resource-based URLs
- HTTP methods (GET, POST, PUT, DELETE)
- JSON request/response
- Proper status codes
- Pagination for lists
- Filtering and sorting

### Authentication

- JWT tokens
- Refresh token rotation
- Token expiration
- Multi-device support

### Rate Limiting

- Per-tenant limits
- Per-endpoint limits
- Graceful degradation
- Rate limit headers

### API Versioning

- URL-based versioning (`/api/v1/`)
- Backward compatibility
- Deprecation notices
- Migration guides

---

**Last Updated**: 2024-12-13
**Status**: Living Document
**Next Review**: Before Sprint 1
