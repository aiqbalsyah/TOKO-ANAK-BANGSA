# MVP Features - Web Platform (Phase 1)

**Timeline**: 8-10 weeks
**Scope**: Web-first (responsive, mobile-friendly web apps)
**Deferr

ed**: Native mobile app (Phase 3)

---

## MoSCoW Prioritization

- **MUST HAVE**: Essential for MVP launch
- **SHOULD HAVE**: Important but can be added post-MVP (Phase 1.5)
- **COULD HAVE**: Nice to have (Phase 2)
- **WON'T HAVE**: Explicitly deferred (Phase 3+)

---

## MUST HAVE (MVP - Phase 1)

### 1. Authentication & Multi-Tenancy

**Category**: AUTH

**Features**:
- ✅ Store owner registration (email/password)
- ✅ Customer registration (email/password)
- ✅ Google Sign-In (optional OAuth)
- ✅ Firebase Auth integration
- ✅ JWT token management
- ✅ Password reset
- ✅ Email verification

**Acceptance Criteria**:
- Store owners can register and create account
- Customers can register for marketplace
- Users receive email verification
- Secure authentication with Firebase Auth
- Session management with JWT

---

### 2. Store Management (Multi-Tenant)

**Category**: STORE

**Features**:
- ✅ Store creation flow
- ✅ Store profile setup (name, slug, logo, banner)
- ✅ Store address configuration
- ✅ Business information
- ✅ Store settings (basic)
- ✅ Store status (active/inactive)

**Acceptance Criteria**:
- Store owner can create new store after registration
- Store has unique slug (URL-friendly identifier)
- Store profile is publicly visible on marketplace
- Store owner can upload logo and banner
- Store owner can configure business address

---

### 3. Product Management (Multi-Tier Pricing) ⭐

**Category**: PRODUCT_PRICING, PRODUCT_UNITS

**Features**:
- ✅ Product CRUD operations
- ✅ **Multi-tier pricing** (Price A, B, C for Wholesale, Retail, Member)
- ✅ **Unit packages** (DUS, PACK, PCS with conversion rates)
- ✅ Cost tracking per product
- ✅ Automatic margin calculation
- ✅ Product images (multiple images per product)
- ✅ Product description (rich text)
- ✅ Product categories
- ✅ Product status (active/inactive/draft)
- ✅ Inventory tracking (with unit conversion)

**Acceptance Criteria**:
- Store owner can create product with multiple units (DUS, PACK, PCS)
- Store owner can set conversion rates (1 DUS = X PACK, 1 PACK = Y PCS)
- Store owner can set cost price per base unit
- Store owner can set 3 price tiers (A, B, C) for each unit
- System auto-calculates profit margin for each tier
- Inventory tracked in base units (PCS) with automatic conversion
- Store owner can upload multiple product images
- Product images stored in Firebase Storage

**Example**:
```
Product: Indomie Goreng
Units:
  - 1 DUS = 40 PACK
  - 1 PACK = 5 PCS

Cost: Rp 600/PCS

Pricing:
  Tier A (Wholesale):
    - DUS: Rp 140,000 (margin: 16.7%)
    - PACK: Rp 3,600 (margin: 20%)
    - PCS: Rp 750 (margin: 25%)

  Tier B (Retail):
    - DUS: Rp 150,000
    - PACK: Rp 4,000
    - PCS: Rp 850

Inventory: 2,000 PCS = 10 DUS = 400 PACK
```

---

### 4. Customer Type & Pricing

**Category**: CUSTOMER

**Features**:
- ✅ Customer type classification (Type A, B, C)
- ✅ Price display based on customer type
- ✅ Default pricing for unregistered (Type B - Retail)

**Acceptance Criteria**:
- Store owner can assign customer type (A, B, C)
- Customers see appropriate prices based on their type
- Unregistered customers see retail prices (Tier B)
- Price tier displayed on product detail page

---

### 5. Customer Address Management

**Category**: CUSTOMER, SHIPPING

**Features**:
- ✅ Customer address book (multiple addresses)
- ✅ Add/edit/delete addresses
- ✅ Set primary/default address
- ✅ Address labels (Home, Office, Other)
- ✅ RajaOngkir city/province integration
- ✅ Address selection at checkout
- ✅ Store shipping origin configuration

**Acceptance Criteria**:
- Customers can save multiple delivery addresses
- Customers can set default address
- Default address auto-selected at checkout
- Address includes: name, phone, full address, city (RajaOngkir), province, postal code
- Store owners can configure shipping origin with RajaOngkir city
- Shipping cost calculated based on store origin and customer destination

---

### 6. Marketplace (Customer-Facing)

**Category**: MARKETPLACE, DISCOVERY

**Features**:
- ✅ Homepage (featured stores, trending products)
- ✅ Store listing page
- ✅ Store detail page (store profile + products)
- ✅ Product listing (all products, by store, by category)
- ✅ Product detail page (images, description, pricing, units)
- ✅ Basic product search (by name)
- ✅ Category filtering
- ✅ Responsive design (mobile-friendly web)

**Acceptance Criteria**:
- Customers can browse stores on marketplace
- Customers can view store profile and products
- Customers can search for products
- Customers can filter by category
- Product detail shows all available units and prices
- Fully responsive (works on mobile browsers)

---

### 7. Shopping Cart

**Category**: CHECKOUT

**Features**:
- ✅ Add to cart (with unit selection)
- ✅ Cart persistence (logged-in users)
- ✅ Cart management (quantity, unit, remove)
- ✅ Cart grouped by store (multi-store cart support)
- ✅ Price calculation per item
- ✅ Subtotal per store
- ✅ Cart notes/special instructions

**Acceptance Criteria**:
- Customers can select unit type (DUS, PACK, PCS) when adding to cart
- Cart persists across sessions for logged-in users
- Cart displays correct price for customer's tier
- Multi-store cart supported (separate checkout per store)
- Cart shows quantity in selected unit

---

### 8. POS Cashier - In-Store Transactions

**Category**: POS, CASHIER, PAYMENT

**Features**:
- ✅ POS cashier interface for in-store sales
- ✅ Product search and selection
- ✅ Customer type selection (A, B, C pricing)
- ✅ Multiple payment methods:
  - Cash payment (with change calculation)
  - EDC machine (card terminal)
  - QRIS
  - Direct bank transfer
- ✅ Receipt printing (thermal printer support)
- ✅ Hold/Resume orders
- ✅ Barcode scanner support (optional)
- ✅ Real-time inventory updates
- ✅ Separate order tracking (POS vs Online)

**Acceptance Criteria**:
- Cashier can process walk-in customer purchases
- Support for cash, EDC, QRIS, and bank transfer payments
- Immediate receipt printing
- Orders marked as "POS" source (vs "online")
- Inventory automatically deducted
- Customer type determines pricing tier
- POS orders immediately completed (no shipping)
- Cashier can hold incomplete orders and resume later

---

### 9. Online Checkout & Payment (Midtrans)

**Category**: CHECKOUT, MIDTRANS

**Features**:
- ✅ Checkout flow (address, shipping, payment)
- ✅ Shipping address management
- ✅ Midtrans payment gateway integration
- ✅ Multiple payment methods:
  - E-wallets (GoPay, OVO, DANA, ShopeePay)
  - Bank Transfer (BCA, Mandiri, BNI, BRI, Permata)
  - Credit/Debit Cards
  - QRIS
  - Convenience stores (Indomaret, Alfamart)
- ✅ Payment status tracking
- ✅ Order creation on successful payment
- ✅ Payment confirmation
- ✅ Invoice generation

**Acceptance Criteria**:
- Customers can enter/select shipping address
- Customers can select payment method from Midtrans
- Payment processed via Midtrans Snap
- Order created only after successful payment
- Customer receives order confirmation email
- Invoice generated with order details

---

### 10. Shipping Integration (RajaOngkir)

**Category**: SHIPPING

**Features**:
- ✅ Store address configuration (shipping origin)
- ✅ RajaOngkir API integration
- ✅ Real-time shipping cost calculation
- ✅ Multiple courier support (JNE, TIKI, POS, etc.)
- ✅ Service type selection (REG, YES, OKE, etc.)
- ✅ Shipping cost display at checkout
- ✅ Weight-based calculation

**Acceptance Criteria**:
- Store owner can configure store address (shipping origin)
- Customers see real shipping costs at checkout
- Customers can select courier and service type
- Shipping cost automatically calculated based on:
  - Origin (store address)
  - Destination (customer address)
  - Weight (product weight × quantity)
- Shipping cost added to order total

---

### 11. Order Management

**Category**: ORDER, ORDER_STATUS

**Features**:
- ✅ Order creation (on payment success)
- ✅ Order listing (store owner view)
- ✅ Order detail view
- ✅ Order status workflow:
  - Pending payment
  - Paid
  - Processing
  - Shipped
  - Delivered
  - Cancelled
- ✅ Order status updates (store owner)
- ✅ Customer order history
- ✅ Customer order tracking
- ✅ Order notifications (email)
- ✅ Invoice view/print

**Acceptance Criteria**:
- Orders automatically created on payment success
- Store owner can view all orders
- Store owner can update order status
- Customer can view order history
- Customer can track order status
- Email notifications sent on status changes
- Invoice can be printed/downloaded

---

### 12. Basic Analytics (Store Owner)

**Category**: ANALYTICS

**Features**:
- ✅ Sales dashboard overview
- ✅ Total revenue (today, this week, this month)
- ✅ Order count
- ✅ Recent orders list
- ✅ Top-selling products
- ✅ Basic charts (revenue trend)

**Acceptance Criteria**:
- Store owner sees sales overview on dashboard
- Revenue and order metrics displayed
- Top-selling products identified
- Simple line chart showing revenue trend
- Recent orders shown for quick access

---

### 13. Platform Admin (Basic)

**Category**: ADMIN, TENANT_MGMT

**Features**:
- ✅ Platform admin login
- ✅ Store listing (all tenants)
- ✅ Store approval/rejection (if moderation enabled)
- ✅ Basic platform analytics:
  - Total stores
  - Total products
  - Total orders
  - GMV (Gross Merchandise Value)

**Acceptance Criteria**:
- Platform admin can log in
- Admin can view all stores
- Admin can approve/suspend stores
- Admin sees platform-wide metrics

---

## SHOULD HAVE (Phase 1.5 - Post-MVP)

### 12. Multi-User Access (RBAC)

**Category**: RBAC

**Features**:
- Store owner can invite team members
- Role assignment (Owner, Manager, Admin, Staff, Viewer)
- Permission matrix per role
- Activity logs (who did what)

**Deferred to**: Phase 1.5 (4-6 weeks after MVP)

---

### 13. Advanced Product Features

**Category**: PRODUCT_VARIANT, PRODUCT

**Features**:
- Product variants (size, color, etc.)
- Bulk product upload (CSV)
- Product duplication
- Product export

**Deferred to**: Phase 1.5

---

### 14. Purchasing Management

**Category**: PURCHASING, SUPPLIER

**Features**:
- Supplier management
- Purchase orders (PO)
- Goods receiving
- Cost tracking

**Deferred to**: Phase 1.5

---

### 15. Accounts Payable (AP)

**Category**: ACCOUNTS_PAYABLE

**Features**:
- AP tracking (store debt to suppliers)
- Payment recording
- Aging reports
- Payment reminders

**Deferred to**: Phase 1.5

---

## COULD HAVE (Phase 2)

### 16. Accounts Receivable (AR)

**Category**: ACCOUNTS_RECEIVABLE

**Features**:
- Customer credit limits
- Credit sales
- AR tracking
- Collection management
- Payment reminders

**Deferred to**: Phase 2

---

### 17. Advanced Analytics & Reports

**Category**: REPORTS, ANALYTICS

**Features**:
- Profit & loss statement
- Cash flow statement
- Advanced charts
- Export reports (PDF, Excel)
- Date range filtering

**Deferred to**: Phase 2

---

### 18. Marketing & Promotions

**Category**: MARKETPLACE

**Features**:
- Discount codes/coupons
- Flash sales
- Product bundles
- Free shipping promotions
- Loyalty points

**Deferred to**: Phase 2

---

### 19. Reviews & Ratings

**Category**: REVIEWS

**Features**:
- Product reviews
- Store ratings
- Review moderation
- Review photos

**Deferred to**: Phase 2

---

## WON'T HAVE (Deferred to Phase 3)

### 20. Native Mobile App

**Scope**: React Native Expo

**Features**:
- Native iOS & Android apps
- Push notifications
- Offline support
- Camera/barcode scanner
- Mobile-specific gestures

**Deferred to**: Phase 3 (2-3 months after Phase 2)

**Note**: MVP will have responsive web that works on mobile browsers

---

## Summary

**MVP Phase 1 (8-10 weeks)**:
- 13 core feature groups
- Web-only (responsive)
- Focus: Marketplace + POS Cashier + Multi-tier pricing + Basic operations

**Phase 1.5 (4-6 weeks)**:
- RBAC
- Purchasing + AP

**Phase 2 (4-6 weeks)**:
- AR
- Advanced analytics
- Marketing features

**Phase 3 (2-3 months)**:
- Native mobile app

**Total to Full Platform**: ~6-7 months

---

## Next Steps

1. ✅ Create story files for each feature using `pnpm story:create`
2. ⏳ Organize stories by sprint
3. ⏳ Begin Sprint 0 (infrastructure)
4. ⏳ Execute MVP features sprint by sprint

---

**Document Maintained By**: Development Team
**Last Review**: 2024-12-13
