# Product Management 📦

**Category**: PRODUCT, INVENTORY
**Priority**: MUST HAVE (MVP)
**Phase**: 1-2

---

## Overview

Product Management enables store owners and staff to create and manage their product catalog with Indonesian-specific features like multi-tier pricing (Tier A/B/C for wholesale/retail/premium) and unit packages (DUS/PACK/PCS). The system supports product variants, multiple images, categories, and barcode management.

### Why This Matters

- **Revenue Core**: Products are the foundation of all sales transactions
- **Indonesian Market**: Multi-tier pricing supports common Indonesian retail practices
- **Inventory Control**: Proper product setup enables accurate stock tracking
- **Customer Experience**: Rich product information improves sales
- **Operational Efficiency**: Barcode scanning speeds up POS operations

---

## Business Requirements

### Primary Goals

1. **Product Catalog**: Easy creation and management of product listings
2. **Multi-tier Pricing**: Support wholesale (A), retail (B), and premium (C) pricing
3. **Unit Packages**: Indonesian system (DUS, PACK, PCS) for inventory management
4. **Product Variants**: Handle products with multiple sizes, colors, etc.
5. **Visual Merchandising**: Multiple product images for marketplace
6. **Categorization**: Organize products into categories and tags
7. **Barcode Integration**: Fast product lookup via barcode scanning

### Problems Solved

- **Pricing Complexity**: Different prices for different customer types
- **Inventory Units**: Package-based inventory (buy by DUS, sell by PCS)
- **Product Variants**: Single product with multiple SKUs
- **Search & Discovery**: Quick product lookup by name, SKU, or barcode
- **Stock Visibility**: Real-time stock levels prevent overselling
- **Product Organization**: Categories make large catalogs manageable

---

## Features

### 1. Product CRUD Operations

**Description**: Create, read, update, and delete products.

**Capabilities**:
- Add new products with complete information
- Edit product details (name, description, pricing, etc.)
- Archive products (soft delete - data retained)
- Restore archived products
- Duplicate products (copy with modifications)
- Bulk import products from CSV/Excel

**Product Information**:
- Name and description
- SKU (Stock Keeping Unit) - auto-generated or manual
- Barcode (EAN-13, UPC, custom)
- Category and brand
- Tags for filtering
- Status (active/inactive/archived)

**User Flow** (Add Product):
1. Owner/Staff navigates to Products > Add New
2. Fills product form:
   - Name: "Indomie Goreng"
   - SKU: Auto-generated or custom
   - Barcode: 8993451234567
   - Category: Mie Instan
   - Brand: Indofood
3. Sets pricing (Tier A/B/C)
4. Configures unit packages (DUS/PACK)
5. Uploads product images
6. Sets initial stock quantity
7. Saves product
8. Product appears in catalog

---

### 2. Multi-tier Pricing (Indonesian System)

**Description**: Support for 3-tier pricing system common in Indonesian retail.

**Pricing Tiers**:

**Tier A - Grosir (Wholesale)**:
- Lowest price for bulk buyers and resellers
- Typically 10-20% below retail price
- Example: IDR 2,500 (margin: 13% above cost IDR 2,200)

**Tier B - Eceran (Retail)**:
- Standard retail price for walk-in customers
- Default price for unknown customers in POS
- Example: IDR 3,000 (margin: 36% above cost)

**Tier C - Premium (Marketplace)**:
- Highest price, suggested for online marketplace
- Includes platform fees and marketing costs
- Example: IDR 3,500 (margin: 59% above cost)

**User Flow** (Set Pricing):
1. Staff enters cost price: IDR 2,200
2. System suggests prices with 20%/40%/60% markup
3. Staff accepts or adjusts:
   - Tier A: IDR 2,500
   - Tier B: IDR 3,000
   - Tier C: IDR 3,500
4. System calculates and shows profit margins
5. Staff saves pricing

**Business Rules**:
- Tier A ≤ Tier B ≤ Tier C (enforced)
- Cost price required (for profit calculation)
- Price history tracked for analysis
- Bulk price update for category/brand

---

### 3. Unit Packages (Indonesian System)

**Description**: Support for Indonesian package-based inventory system.

**Package Types**:

**DUS (Box/Carton)**:
- Largest package unit
- Example: 1 DUS = 40 PCS
- Used for wholesale purchases
- Can have separate barcode

**PACK (Package)**:
- Medium package unit
- Example: 1 PACK = 5 PCS
- Common retail packaging
- Can have separate barcode

**LUSIN (Dozen)**:
- 12 pieces
- Example: 1 LUSIN = 12 PCS
- Traditional Indonesian measure

**PCS (Pieces)**:
- Base unit for inventory tracking
- Individual item
- All calculations done in PCS

**User Flow** (Set Package Units):
1. Staff creates product: "Indomie Goreng"
2. Sets base unit: PCS
3. Defines packages:
   - 1 DUS = 40 PCS (barcode: 8993451234567-DUS)
   - 1 PACK = 5 PCS (barcode: 8993451234567-PACK)
4. System tracks all inventory in PCS
5. Cashier can sell by DUS/PACK/PCS
6. System auto-converts to PCS

**Use Cases**:
- Purchase: Buy 10 DUS (= 400 PCS) from supplier
- Stock: Inventory shows 400 PCS
- Sale: Customer buys 2 PACK (= 10 PCS)
- Stock: Inventory now 390 PCS

---

### 4. Product Variants

**Description**: Single product with multiple variations (size, color, etc.).

**Capabilities**:
- Create variants with different attributes
- Each variant has own SKU, barcode, pricing, stock
- Variant options: Size, Color, Material, etc.
- Variant-specific images
- Bulk variant creation

**Use Cases**:

**Apparel Example**:
- Product: "Kaos Polos"
- Variants:
  - S - Merah (IDR 50,000, stock: 20)
  - S - Biru (IDR 50,000, stock: 15)
  - M - Merah (IDR 55,000, stock: 25)
  - M - Biru (IDR 55,000, stock: 18)
  - L - Merah (IDR 60,000, stock: 10)
  - L - Biru (IDR 60,000, stock: 12)

**Food Example**:
- Product: "Indomie"
- Variants:
  - Goreng Original (SKU: IDM-GOR, stock: 500)
  - Goreng Jumbo (SKU: IDM-GOR-J, stock: 200)
  - Kuah Soto (SKU: IDM-SOT, stock: 300)

**User Flow**:
1. Staff creates main product: "Kaos Polos"
2. Enables variants
3. Defines variant attributes: Size (S/M/L), Color (Merah/Biru)
4. System generates 6 variants (3 sizes × 2 colors)
5. Staff sets pricing and stock for each variant
6. In POS, cashier selects "Kaos Polos" then chooses variant

---

### 5. Product Images

**Description**: Upload and manage multiple product images.

**Capabilities**:
- Upload up to 10 images per product
- Drag-and-drop reordering
- Set primary/featured image
- Automatic thumbnail generation (300x300px)
- Image optimization (WebP format)
- Alt text for SEO
- Variant-specific images (optional)

**Supported Formats**:
- PNG, JPG, JPEG, WebP
- Max size: 5MB per image
- Recommended: Square ratio (1:1) for best display

**User Flow**:
1. Staff navigates to product edit
2. Clicks "Add Images"
3. Selects multiple images (or drag-drop)
4. System uploads to Firebase Storage
5. System generates thumbnails
6. Staff reorders images by dragging
7. Staff sets first image as primary
8. Images display on marketplace and POS

---

### 6. Categories & Tags

**Description**: Organize products into categories and add searchable tags.

**Categories**:
- Hierarchical structure (future: subcategories)
- Category name, slug, description
- Category image/icon
- Product count per category
- Display order customizable

**Tags**:
- Flexible tagging system
- Auto-complete from existing tags
- Multiple tags per product
- Filter products by tag
- Tag cloud (future)

**Common Categories** (Indonesia):
- Makanan & Minuman (Food & Beverages)
- Sembako (Daily Necessities)
- Elektronik (Electronics)
- Fashion & Pakaian
- Kesehatan & Kecantikan
- Perlengkapan Rumah Tangga

**User Flow** (Create Category):
1. Owner navigates to Categories
2. Clicks "Add Category"
3. Enters name: "Mie Instan"
4. System generates slug: "mie-instan"
5. Uploads category image (optional)
6. Sets display order: 1
7. Saves category
8. Category available for product assignment

---

### 7. Barcode & SKU Management

**Description**: Manage product identification codes for fast lookup.

**SKU (Stock Keeping Unit)**:
- Auto-generated format: `{CATEGORY}-{DATE}-{COUNTER}`
- Example: "MIE-20241213-001"
- Or custom: "IDM-001"
- Unique per tenant
- Searchable in POS

**Barcode**:
- Supports EAN-13, UPC, Code-128, custom
- Can be same across tenants (global product code)
- Package-specific barcodes (DUS, PACK)
- Barcode scanning in POS
- Print barcode labels

**User Flow** (Barcode Scanning in POS):
1. Customer brings product to cashier
2. Cashier scans barcode: 8993451234567
3. System looks up product by barcode
4. Product "Indomie Goreng" added to cart
5. Price shown based on customer tier (A/B/C)

---

### 8. Product Search & Filtering

**Description**: Fast product lookup for POS and inventory management.

**Search Methods**:
- Text search: Name, SKU, brand
- Barcode scan
- Category filter
- Price range filter
- Stock status (in stock / low stock / out of stock)
- Tags filter
- Status (active / inactive)

**Use Cases**:

**POS Search**:
- Cashier types "indo" → Shows: Indomie Goreng, Indomilk, etc.
- Cashier scans barcode → Product instantly added to cart

**Inventory Search**:
- Staff filters by category "Mie Instan"
- Staff filters "Low Stock" → Shows products below threshold
- Staff searches brand "Indofood" → Shows all Indofood products

---

## Use Cases

### Use Case 1: Add Simple Product (No Variants)

**Scenario**: Add "Indomie Goreng" to catalog.

**Steps**:
1. Staff navigates to Products > Add New
2. Fills information:
   - Name: "Indomie Goreng"
   - SKU: "IDM-001" (or auto-generate)
   - Barcode: 8993451234567
   - Category: Mie Instan
   - Brand: Indofood
3. Sets pricing:
   - Cost: IDR 2,200
   - Tier A: IDR 2,500 (Grosir)
   - Tier B: IDR 3,000 (Eceran)
   - Tier C: IDR 3,500 (Marketplace)
4. Sets unit packages:
   - Base: PCS
   - 1 DUS = 40 PCS
   - 1 PACK = 5 PCS
5. Uploads product image
6. Sets initial stock: 500 PCS
7. Sets low stock alert: 100 PCS
8. Saves product
9. Product ready for sale

---

### Use Case 2: Add Product with Variants

**Scenario**: Add "Kaos Polos" with size and color variants.

**Steps**:
1. Staff creates product: "Kaos Polos"
2. Enables variants
3. Defines variant options:
   - Size: S, M, L, XL
   - Color: Hitam, Putih, Merah, Biru
4. System generates 16 variants (4 sizes × 4 colors)
5. Staff sets pricing per size:
   - S: IDR 50,000
   - M: IDR 55,000
   - L: IDR 60,000
   - XL: IDR 65,000
6. Staff sets stock per variant
7. Staff uploads images per color
8. Saves product
9. In POS, cashier selects size and color

---

### Use Case 3: Bulk Price Update

**Scenario**: Supplier raises prices 10%, update all "Indofood" products.

**Steps**:
1. Owner navigates to Products
2. Filters by brand: "Indofood"
3. Selects all products (45 products)
4. Clicks "Bulk Edit"
5. Selects "Update Prices"
6. Chooses "Increase by 10%"
7. Reviews changes preview
8. Confirms update
9. All 45 products updated in one action

---

### Use Case 4: Low Stock Alert

**Scenario**: "Indomie Goreng" stock drops to 95 PCS (threshold: 100).

**Flow**:
1. Customer purchases 10 PCS
2. Stock drops from 105 to 95 PCS
3. System detects below threshold
4. System sends notification to owner:
   - Email: "Low Stock Alert: Indomie Goreng (95/100)"
   - Dashboard: Red badge on product
5. Staff creates purchase order to restock
6. Stock replenished, alert clears

---

## Business Rules

### Multi-tier Pricing

- Tier A ≤ Tier B ≤ Tier C (strictly enforced)
- All tiers required (cannot be empty)
- Cost price required for profit calculation
- Price changes logged in history
- Bulk price update available

### Unit Packages

- All inventory tracked in base unit (PCS)
- Package quantities must be positive integers
- Package barcodes optional but recommended
- Selling price same regardless of package (IDR 3,000 per PCS whether sold as DUS, PACK, or PCS)

### Product Variants

- Product with variants cannot have main stock (only variant stock)
- Each variant must have unique SKU
- Variant options limited to 3 types (e.g., Size, Color, Material)
- Max 50 variants per product

### SKU & Barcode

- SKU must be unique per tenant
- Barcode can duplicate across tenants (global codes)
- SKU cannot be changed after creation (affects inventory history)
- Barcode can be updated

### Stock Management

- Negative stock not allowed (configurable in settings)
- Stock adjustments require reason code
- Stock transfers logged with timestamps
- Low stock threshold per product (overrides global setting)

---

## Edge Cases

### Package Conversion Rounding

- **Problem**: Sell 1.5 DUS (1 DUS = 40 PCS)
- **Solution**: Not allowed - must sell whole packages or convert to PCS
- **UX**: "Cannot sell fractional packages. Sell 1 DUS (40 PCS) or 2 DUS (80 PCS)"

### Variant Stock Confusion

- **Problem**: Product has variants but staff tries to set main product stock
- **Solution**: Disable main product stock if variants exist
- **UX**: "This product has variants. Set stock for each variant individually."

### Barcode Duplication

- **Problem**: Two products have same barcode (legitimate - different stores)
- **Solution**: Search returns both, cashier selects correct one
- **Future**: Prioritize tenant's own products in search results

### Price Tier Violation

- **Problem**: Staff tries to set Tier B (IDR 2,500) lower than Tier A (IDR 3,000)
- **Solution**: Validation error prevents save
- **UX**: "Invalid pricing. Tier B must be ≥ Tier A"

---

## Future Enhancements

### Advanced Features
- Product bundles/kits (sell multiple products as one)
- Product attributes (specifications like weight, dimensions)
- Related products recommendations
- Product reviews and ratings
- Product comparison tool
- Dynamic pricing (time-based discounts)

### Inventory
- Multi-location stock (per branch)
- Stock reservations (pending orders)
- Stock transfer between branches
- Stock opname (physical count)
- Automated reorder points

### E-commerce
- SEO optimization (meta tags, structured data)
- Product videos
- 360° product views
- Wishlist functionality
- Recently viewed products

---

## Success Metrics

- **Products Added**: # of active products per store
- **Pricing Accuracy**: % of products with all 3 tiers set
- **Image Quality**: % of products with images
- **Categorization**: % of products assigned to category
- **Barcode Usage**: % of products with barcodes

---

## Dependencies

- **Tenant Management** (02): Tenant-scoped products
- **Firebase Storage**: Product images
- **Firebase Firestore**: Product data
- **Inventory Management** (04): Stock tracking

---

**Last Updated**: 2024-12-13
