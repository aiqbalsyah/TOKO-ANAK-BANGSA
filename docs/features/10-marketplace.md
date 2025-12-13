# Marketplace (Online Store) 🛒

**Category**: E-COMMERCE, CUSTOMER-FACING
**Priority**: SHOULD HAVE (MVP)
**Phase**: 2-3

---

## Overview

Marketplace provides an online storefront where customers can browse products, add items to cart, checkout, and track orders. Each tenant gets their own marketplace with a unique URL (e.g., `toko-makmur.tokoanak.id`), customizable branding, and full e-commerce functionality. The marketplace integrates with inventory, payment gateways (Midtrans), and order management systems.

### Why This Matters

- **Revenue Expansion**: Sell 24/7 online, not just in-store hours
- **Reach**: Customers can shop from anywhere in Indonesia
- **Customer Convenience**: Browse and order from mobile/desktop
- **Reduced Overhead**: No need for physical store expansion
- **Data Collection**: Understand online customer behavior
- **Multi-channel**: Unified inventory across POS and marketplace

---

## Business Requirements

### Primary Goals

1. **Product Catalog**: Display all available products with images and descriptions
2. **Shopping Cart**: Add products, adjust quantities, apply discounts
3. **Checkout**: Seamless checkout with multiple payment methods
4. **Order Tracking**: Customers can track order status and shipment
5. **Customer Accounts**: Registration, login, order history, wishlist
6. **Product Search**: Fast product discovery with filters
7. **Reviews & Ratings**: Customer reviews and product ratings (future)

### Problems Solved

- **Limited Hours**: Online store open 24/7 vs physical store hours
- **Geographic Reach**: Serve customers beyond local area
- **Customer Preferences**: Many customers prefer online shopping
- **Price Transparency**: Customers can compare prices before buying
- **Order History**: Customers can easily reorder favorite products
- **Inventory Sync**: Real-time stock prevents overselling

---

## Features

### 1. Storefront & Product Catalog

**Description**: Public-facing product catalog with search and filtering.

**Capabilities**:
- Display all active products
- Product grid/list view toggle
- Product images with zoom
- Product details (name, description, price, stock availability)
- Multi-tier pricing (show Tier B/C based on customer type)
- Category browsing
- Product search with autocomplete
- Filters (category, brand, price range, availability)
- Sort (newest, price low-high, price high-low, popular)
- SEO-friendly URLs

**Storefront Layout**:
```
┌──────────────────────────────────────────┐
│ [LOGO] Toko Makmur        🔍 Search  🛒 │
├──────────────────────────────────────────┤
│ Home | Categories | About | Contact     │
├──────────────────────────────────────────┤
│ ┌────────────┐  ┌────────────┐          │
│ │ Indomie    │  │ Indomie    │          │
│ │ Goreng     │  │ Soto       │          │
│ │ [Image]    │  │ [Image]    │          │
│ │ IDR 3,000  │  │ IDR 3,000  │          │
│ │ In Stock ✓ │  │ In Stock ✓ │          │
│ │ [Add Cart] │  │ [Add Cart] │          │
│ └────────────┘  └────────────┘          │
│                                          │
│ [Load More Products...]                 │
├──────────────────────────────────────────┤
│ Footer: About | Terms | Contact         │
└──────────────────────────────────────────┘
```

**User Flow** (Browse Products):
1. Customer visits: `toko-makmur.tokoanak.id`
2. Homepage displays featured products
3. Customer clicks category: "Mie Instan"
4. 50 products shown in grid view
5. Customer filters: Price < IDR 5,000
6. 35 products match
7. Customer sorts: Price Low to High
8. Customer views product: "Indomie Goreng"
9. Product page shows:
   - Images (3 photos)
   - Description
   - Price: IDR 3,000 (Tier B)
   - Stock: In Stock (450 PCS available)
   - [Add to Cart] button

---

### 2. Product Search & Discovery

**Description**: Fast product search with autocomplete and suggestions.

**Search Features**:
- Real-time autocomplete
- Search suggestions based on popular queries
- Fuzzy matching (typo tolerance)
- Search filters (category, brand, price)
- Recently viewed products
- Recommended products

**User Flow** (Search Products):
1. Customer types in search: "indo"
2. Autocomplete shows:
   ```
   Suggestions:
   🔍 Indomie Goreng
   🔍 Indomie Soto
   🔍 Indomilk
   🔍 Indocafe

   Popular Searches:
   - Indomie
   - Indomilk Susu
   ```
3. Customer selects: "Indomie Goreng"
4. Search results: 3 variants
   - Indomie Goreng Original
   - Indomie Goreng Jumbo
   - Indomie Goreng Pedas
5. Customer adds to cart

**Category Navigation**:
```
Categories:
📦 Makanan & Minuman
  ├─ Mie Instan (125 products)
  ├─ Minuman (87 products)
  ├─ Snack (156 products)
  └─ Bumbu Dapur (45 products)

📦 Sembako
  ├─ Beras (12 products)
  ├─ Minyak Goreng (8 products)
  ├─ Gula (5 products)
  └─ Tepung (15 products)

📦 Peralatan Rumah Tangga (34 products)
```

---

### 3. Shopping Cart

**Description**: Add products and manage cart before checkout.

**Capabilities**:
- Add products to cart
- Adjust quantities (+/- buttons)
- Remove items
- View subtotal per item
- View cart total
- Apply promo codes/vouchers
- Save cart (persist for logged-in users)
- Cart notifications (low stock warning)
- Continue shopping or checkout

**Cart Display**:
```
🛒 Shopping Cart (3 items)

┌─────────────────────────────────────────┐
│ Indomie Goreng                          │
│ [Image] IDR 3,000 x 10 PCS              │
│ Subtotal: IDR 30,000                    │
│ [−][10][+] [Remove]                     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Indomie Soto                            │
│ [Image] IDR 3,000 x 5 PCS               │
│ Subtotal: IDR 15,000                    │
│ [−][5][+] [Remove]                      │
│ ⚠️ Only 3 left in stock                 │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Minyak Goreng 2L                        │
│ [Image] IDR 35,000 x 2 PCS              │
│ Subtotal: IDR 70,000                    │
│ [−][2][+] [Remove]                      │
└─────────────────────────────────────────┘

Subtotal: IDR 115,000
Shipping: IDR 15,000
Tax (11%): IDR 14,300
─────────────────────────
Total: IDR 144,300

[Continue Shopping] [Proceed to Checkout]
```

**User Flow** (Add to Cart):
1. Customer viewing: "Indomie Goreng"
2. Clicks [Add to Cart]
3. Popup: "Added to cart! (10 PCS)"
4. Cart icon shows badge: 🛒 (1)
5. Customer continues shopping
6. Adds more products
7. Cart badge updates: 🛒 (3)
8. Customer clicks cart icon
9. Cart sidebar opens
10. Reviews items
11. Clicks [Checkout]

---

### 4. Checkout Process

**Description**: Seamless multi-step checkout flow.

**Checkout Steps**:

**Step 1: Shipping Address**
- Select saved address or add new
- Full name, phone, complete address
- Delivery instructions
- Save address for future orders

**Step 2: Shipping Method**
- JNE Regular (3-5 days) - IDR 15,000
- JNE Express (1-2 days) - IDR 25,000
- J&T Regular (3-5 days) - IDR 12,000
- J&T Express (1-2 days) - IDR 20,000
- Store Pickup (free) - Available today

**Step 3: Payment Method**
- QRIS (GoPay, OVO, Dana, ShopeePay)
- Virtual Account (BCA, Mandiri, BNI, BRI)
- Credit/Debit Card (Visa, MasterCard)
- Bank Transfer (manual confirmation)
- Cash on Delivery (COD) - if enabled

**Step 4: Order Review**
- Review items, shipping, payment
- Apply promo code (if any)
- Agree to terms & conditions
- Place order

**User Flow** (Complete Checkout):
1. Customer clicks [Checkout] from cart
2. Login required (or guest checkout)
3. Step 1: Shipping Address
   - Selects saved address: "Rumah"
   - Jl. Sudirman No. 123, Jakarta Selatan
4. Step 2: Shipping Method
   - Selects: JNE Regular (IDR 15,000, 3-5 days)
5. Step 3: Payment Method
   - Selects: QRIS
6. Step 4: Order Review
   ```
   Order Summary:
   Items (3): IDR 115,000
   Shipping (JNE): IDR 15,000
   Tax (11%): IDR 14,300
   ─────────────────────────
   Total: IDR 144,300

   Ship to:
   Rumah - Jl. Sudirman No. 123, Jakarta Selatan

   Payment: QRIS
   ```
7. Customer checks: ☑ I agree to Terms & Conditions
8. Customer clicks [Place Order]
9. System creates order #ORD-MKT-20241213-001
10. Redirects to payment page
11. Shows QRIS code
12. Customer scans with GoPay app
13. Payment confirmed
14. Order status: Paid → Confirmed
15. Confirmation page:
    ```
    ✅ Order Confirmed!
    Order #ORD-MKT-20241213-001
    Total: IDR 144,300
    Payment: QRIS (Paid)

    Estimated Delivery: Dec 18-20, 2024

    [View Order Details] [Track Order]
    ```
16. Confirmation email sent

---

### 5. Order Tracking

**Description**: Customers can track their orders in real-time.

**Capabilities**:
- View order status
- Track shipment with tracking number
- Estimated delivery date
- Order history
- Reorder with one click
- Request cancellation (if not shipped)
- Contact support

**Order Statuses**:
```
Pending → Confirmed → Processing → Packed → Shipped → Delivered → Completed
        ↘ Cancelled
```

**Order Tracking Page**:
```
Order #ORD-MKT-20241213-001
Placed: Dec 13, 2024 14:30
Status: Shipped 📦

┌─────────────────────────────────────────┐
│ ✅ Order Placed - Dec 13, 14:30         │
│ ✅ Payment Confirmed - Dec 13, 14:32    │
│ ✅ Processing - Dec 14, 09:00           │
│ ✅ Packed - Dec 14, 15:00               │
│ ✅ Shipped - Dec 15, 10:00              │
│    JNE Tracking: JNE1234567890          │
│    [Track Shipment]                     │
│ ⏳ In Transit - Expected Dec 18-20      │
│ ⏳ Delivered                            │
└─────────────────────────────────────────┘

Items (3):
- Indomie Goreng x 10
- Indomie Soto x 5
- Minyak Goreng 2L x 2

Total: IDR 144,300

Ship to:
Rumah
Jl. Sudirman No. 123
Jakarta Selatan, DKI Jakarta 12345

[Cancel Order] [Contact Support]
```

**Shipment Tracking** (JNE Integration):
```
JNE Tracking: JNE1234567890

Dec 15, 10:00 - Package picked up (Jakarta)
Dec 15, 18:00 - In transit to sorting facility
Dec 16, 08:00 - Arrived at Jakarta Hub
Dec 16, 20:00 - In transit to Jakarta Selatan
Dec 17, 09:00 - Out for delivery
Dec 17, 14:30 - Delivered ✅
```

---

### 6. Customer Account

**Description**: Customer profiles with order history and preferences.

**Customer Profile Features**:
- Personal information (name, phone, email)
- Saved addresses (multiple)
- Order history
- Wishlist (favorite products)
- Loyalty points (future)
- Notification preferences

**Customer Dashboard**:
```
👤 Welcome, John Doe!

┌──────────────────────────────────────┐
│ My Orders (12 orders)                │
│ [View All Orders]                    │
│                                      │
│ Recent Orders:                       │
│ #ORD-001 - Dec 13 - Shipped         │
│ #ORD-002 - Dec 10 - Delivered       │
│ #ORD-003 - Dec 5 - Completed        │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ My Addresses (3)                     │
│ [Manage Addresses]                   │
│                                      │
│ ⭐ Rumah (Default)                   │
│ 📍 Kantor                            │
│ 📍 Orang Tua                         │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ Wishlist (5 items)                   │
│ [View Wishlist]                      │
└──────────────────────────────────────┘

[Edit Profile] [Change Password] [Logout]
```

**User Flow** (Reorder):
1. Customer logs in
2. Navigates to: My Orders
3. Views order: #ORD-002
4. Clicks [Reorder]
5. All items from order added to cart:
   - Indomie Goreng x 10
   - Indomie Soto x 5
   - Minyak Goreng 2L x 2
6. Customer reviews cart
7. Adjusts quantities if needed
8. Proceeds to checkout
9. Completes new order

---

### 7. Promo Codes & Discounts

**Description**: Apply promotional codes and discounts at checkout.

**Discount Types**:
- Percentage off (10% off, 20% off)
- Fixed amount (IDR 10,000 off, IDR 25,000 off)
- Free shipping
- Buy X Get Y (Buy 2 get 1 free)
- Minimum purchase (IDR 100K min for 10% off)
- First order discount (new customers)
- Loyalty rewards (repeat customers)

**Promo Code Examples**:
```
WELCOME10 - 10% off first order (max IDR 50K)
FREESHIP - Free shipping (min IDR 100K)
BUY2GET1 - Buy 2 Indomie DUS, get 1 free
LOYAL20 - 20% off for repeat customers
FLASH50 - IDR 50K off (min IDR 200K, valid today only)
```

**User Flow** (Apply Promo):
1. Customer in checkout
2. Subtotal: IDR 150,000
3. Customer enters promo code: "WELCOME10"
4. Clicks [Apply]
5. System validates:
   - Code valid ✓
   - First order ✓
   - No minimum purchase requirement ✓
6. Discount applied:
   ```
   Subtotal: IDR 150,000
   Discount (WELCOME10): -IDR 15,000
   Shipping: IDR 15,000
   Tax (11%): IDR 16,500
   ─────────────────────────
   Total: IDR 166,500
   ```
7. Customer saves IDR 15,000 ✓
8. Completes order

---

### 8. Product Reviews & Ratings (Future)

**Description**: Customers can review and rate products after purchase.

**Capabilities**:
- 5-star rating system
- Written review with photos
- Helpful votes (upvote/downvote)
- Verified purchase badge
- Store response to reviews
- Filter reviews (rating, date, helpful)

**Product Page with Reviews**:
```
Indomie Goreng
★★★★★ 4.8/5 (245 reviews)

Top Reviews:
┌────────────────────────────────────────┐
│ ★★★★★ by Ibu Siti (Verified Purchase) │
│ "Enak dan harga terjangkau!"          │
│ Dec 10, 2024                           │
│ 👍 12 people found this helpful        │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ ★★★★☆ by Pak Budi (Verified Purchase) │
│ "Pengiriman cepat, tapi kemasan agak   │
│  basah. Overall ok."                   │
│ Dec 8, 2024                            │
│ 👍 5 people found this helpful         │
│                                        │
│ Store Response:                        │
│ "Terima kasih feedback-nya! Kami akan │
│  perbaiki packaging. Sorry!"           │
└────────────────────────────────────────┘

[See All Reviews]
```

---

## Use Cases

### Use Case 1: First-time Customer Order

**Scenario**: New customer discovers marketplace, creates account, places first order.

**Steps**:
1. Customer Googles: "beli indomie online jakarta"
2. Finds: toko-makmur.tokoanak.id
3. Browses products
4. Adds to cart:
   - Indomie Goreng: 20 PCS (2 PACK)
   - Indomie Soto: 10 PCS (1 PACK)
5. Clicks [Checkout]
6. Prompted to login/register
7. Chooses: Register
8. Fills form:
   - Name: John Doe
   - Email: john@gmail.com
   - Phone: +628123456789
   - Password: ••••••••
9. Confirms email (verification link sent)
10. Continues checkout
11. Adds shipping address
12. Selects shipping: JNE Regular
13. Enters promo: WELCOME10 (10% off)
14. Selects payment: QRIS
15. Reviews order: IDR 68,850 (with discount)
16. Places order
17. Scans QRIS with GoPay
18. Payment confirmed
19. Order #ORD-MKT-20241213-001 created
20. Confirmation email sent
21. Customer receives order in 3 days
22. Happy customer! Likely to reorder ✓

---

### Use Case 2: Repeat Customer Quick Reorder

**Scenario**: Existing customer quickly reorders favorite products.

**Steps**:
1. Customer receives WhatsApp: "Indomie stock ready!"
2. Customer clicks marketplace link
3. Already logged in (saved session)
4. Navigates to: My Orders
5. Finds previous order: #ORD-002
6. Clicks [Reorder]
7. Cart populated with previous items
8. Reviews cart, adds 2 more products
9. Clicks [Quick Checkout]
10. System pre-fills:
    - Saved address (default)
    - Preferred shipping (JNE Regular)
    - Saved payment (QRIS)
11. Customer just clicks [Place Order]
12. Order placed in 30 seconds! ⚡
13. Payment with saved QRIS
14. Order confirmed
15. Total time: <2 minutes from click to order ✓

---

### Use Case 3: Cart Abandonment Recovery

**Scenario**: Customer adds products but doesn't checkout, receives reminder.

**Steps**:
1. Customer browses marketplace
2. Adds 5 products to cart: IDR 250,000
3. Closes browser (didn't checkout)
4. 24 hours later: System sends reminder email
   ```
   Subject: You left something in your cart!

   Hi John,

   You have 5 items waiting in your cart (IDR 250,000).

   🛒 Complete your order now and get 5% off with code: COMEBACK5

   [Complete My Order]

   Valid for 48 hours.
   ```
5. Customer clicks email link
6. Marketplace opens with cart preserved
7. Applies promo: COMEBACK5
8. Discount: -IDR 12,500
9. Completes checkout
10. Cart recovery successful! ✓

---

## Business Rules

### Product Display

- Only active products shown
- Out of stock products shown but cannot be added to cart
- Archived products not visible
- Price shown based on customer tier (default Tier B for guest)
- Stock availability updated real-time

### Cart & Checkout

- Cart expires after 30 days (guest) or persists (logged in)
- Stock reserved during checkout (15 minutes)
- Cannot checkout if any item out of stock
- Minimum order: IDR 25,000 (configurable)
- Maximum order: IDR 10,000,000 per transaction

### Pricing & Discounts

- Guest customers see Tier B (retail) prices
- Logged-in customers see tier-based prices
- Only one promo code per order
- Discounts cannot reduce total below IDR 0
- Free shipping applies after discounts

### Order Processing

- Order auto-cancelled if payment not received in 24 hours
- Cannot cancel order after "Shipped" status
- Refunds processed to original payment method
- Return period: 7 days from delivery

---

## Edge Cases

### Out of Stock During Checkout

- **Problem**: Product in stock when added to cart, sold out during checkout
- **Solution**: Re-check stock before payment, show error if insufficient
- **UX**: "Indomie Goreng out of stock. Remove from cart or reduce quantity."

### Payment Successful But Order Not Created

- **Problem**: Midtrans webhook successful but order creation failed
- **Solution**: Retry order creation with idempotency key
- **Fallback**: Manual order creation by admin with payment proof

### Address Validation Failure

- **Problem**: Customer enters invalid address (delivery impossible)
- **Solution**: Google Maps API validation, suggest corrections
- **UX**: "Address not found. Did you mean: Jl. Sudirman No. 123?"

### Promo Code Already Used

- **Problem**: Customer tries to use one-time promo code twice
- **Solution**: Track promo code usage per customer
- **UX**: "Promo WELCOME10 already used. Try another code."

---

## Future Enhancements

### Advanced Features
- Wishlist with price drop alerts
- Product recommendations (AI-based)
- Live chat support
- Push notifications (order updates)
- Mobile app (iOS/Android)
- Voice search
- Augmented reality (AR) product preview

### Social Commerce
- Instagram shop integration
- WhatsApp catalog sync
- Facebook Marketplace integration
- TikTok Shop integration
- Social media sharing (share products)

### Loyalty & Gamification
- Loyalty points system
- Member tiers (Bronze/Silver/Gold)
- Referral program
- Daily check-in rewards
- Gamified shopping (spin wheel, scratch cards)

---

## Success Metrics

- **Conversion Rate**: % of visitors who place orders (target: >2%)
- **Average Order Value**: Avg order amount (target: > IDR 150K)
- **Cart Abandonment Rate**: % of carts not checked out (target: <70%)
- **Repeat Purchase Rate**: % of customers who order again (target: >30%)
- **Customer Acquisition Cost**: Marketing spend / new customers
- **Customer Lifetime Value**: Avg revenue per customer over lifetime
- **Page Load Time**: Avg page load speed (target: <2 seconds)
- **Mobile Traffic**: % of visitors on mobile (expect: >60%)

---

## Dependencies

- **Product Management** (03): Product catalog
- **Inventory Management** (04): Real-time stock availability
- **Customer Management** (07): Customer accounts and tiers
- **Order Management** (06): Order creation and tracking
- **Financial Management** (09): Payment gateway integration
- **Notifications** (12): Email/WhatsApp order updates

---

**Last Updated**: 2024-12-13
