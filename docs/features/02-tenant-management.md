# Tenant (Store) Management 🏪

**Category**: STORE, ADMIN
**Priority**: MUST HAVE (MVP)
**Phase**: 1

---

## Overview

Tenant Management allows store owners to register their business on the platform, configure store settings, manage staff members, and handle multi-location operations. Each tenant (store) is completely isolated with its own data, ensuring privacy and security in the multi-tenant architecture.

### Why This Matters

- **Business Independence**: Each store operates independently with isolated data
- **Customization**: Stores can configure settings specific to their business needs
- **Scalability**: Support for multiple branches as business grows
- **Team Collaboration**: Manage staff with different roles and permissions
- **Subscription Flexibility**: Choose plan that fits business size and needs

---

## Business Requirements

### Primary Goals

1. **Store Onboarding**: Easy registration process for new store owners
2. **Business Configuration**: Comprehensive settings for store operations
3. **Staff Management**: Add, remove, and assign roles to team members
4. **Multi-location Support**: Manage multiple branches (Pro/Enterprise plans)
5. **Subscription Management**: Flexible plans with usage-based billing
6. **Brand Identity**: Logo, colors, and store customization

### Problems Solved

- **Data Isolation**: Each store's data is completely separated and secure
- **Business Hours**: Configure operating hours and holidays specific to each store
- **Tax Compliance**: Set up tax rates according to local regulations
- **Team Organization**: Clear roles and permissions for staff members
- **Growth Support**: Easily add branches as business expands
- **Cost Control**: Pay only for features and capacity needed

---

## Features

### 1. Store Registration

**Description**: New store owners can register their business on the platform.

**Capabilities**:
- Business information capture (name, category, type)
- Auto-generate store slug for marketplace URL
- Owner account creation (if not exists)
- Address and location setup
- Contact information (phone, WhatsApp, email, website)
- Initial subscription plan selection

**User Flow**:
1. Owner completes authentication signup
2. Owner fills store registration form:
   - Store name
   - Business category (grocery, fashion, electronics, etc.)
   - Business type (retail, wholesale, both)
   - Complete address
   - Contact details
3. System validates data and generates unique slug
4. System creates tenant record
5. Owner assigned as tenant owner
6. Owner redirected to dashboard

**Business Rules**:
- Store slug must be unique across platform
- Slug auto-generated from store name (URL-friendly)
- Default to "Free" plan on initial registration
- Owner must have verified email

---

### 2. Store Settings & Configuration

**Description**: Comprehensive settings to customize store operations.

**General Settings**:
- Timezone (default: Asia/Jakarta)
- Language (Indonesian/English)
- Currency (IDR)
- Date format (DD/MM/YYYY or MM/DD/YYYY)
- Time format (12h or 24h)

**Business Settings**:
- Operating hours per day of week
- Holiday dates
- Store description and about text
- Return policy
- Terms and conditions

**Tax Settings**:
- Enable/disable tax
- Tax name (e.g., "PPN" for Indonesian VAT)
- Tax rate (e.g., 11% for Indonesia)
- Tax included in price or added at checkout
- Tax number (NPWP in Indonesia)

**Pricing Settings**:
- Default price tier (A/B/C)
- Allow price override by cashier
- Rounding method (up, down, nearest)
- Decimal places (0-2)

**Inventory Settings**:
- Track stock enabled/disabled
- Allow negative stock
- Low stock threshold (global default)
- Auto-reorder enabled/disabled

**Receipt Settings**:
- Show logo on receipts
- Show store address
- Show tax number
- Footer message
- Paper size (58mm or 80mm thermal)

**Notification Settings**:
- Email notifications
- SMS notifications
- WhatsApp notifications
- Low stock alerts
- Daily sales report

---

### 3. Staff & User Management

**Description**: Manage team members with different roles and permissions.

**Capabilities**:
- Invite staff via email
- Assign roles (Admin, Staff, Cashier)
- Restrict access to specific branches
- View all team members
- Remove staff members
- Track staff activity

**User Roles**:

**Owner**:
- Full access to everything
- Manage staff and permissions
- View all reports
- Configure settings
- Manage subscription

**Admin**:
- Manage products, inventory, customers
- Process orders and refunds
- View reports
- Cannot manage users or subscription

**Staff**:
- Manage products and inventory
- Process orders
- Limited report access

**Cashier**:
- POS transactions only
- Cannot modify data

**User Flow** (Invite Staff):
1. Owner navigates to Staff Management
2. Owner clicks "Invite Staff Member"
3. Owner enters email, name, and role
4. System sends invitation email
5. Staff member receives email with activation link
6. Staff member creates password and activates account
7. Staff member can log in and access assigned features

---

### 4. Multi-location / Branch Management

**Description**: Manage multiple store locations (Pro/Enterprise plans).

**Capabilities**:
- Add multiple branches/locations
- Centralized or branch-specific inventory
- Branch-specific staff assignment
- Branch-specific reports
- Transfer inventory between branches

**Use Cases**:
- Chain stores with multiple locations
- Warehouse + retail outlets
- Different cities or regions
- Centralized HQ with distributed branches

**Business Rules**:
- Free plan: 1 branch only
- Basic plan: 1 branch only
- Pro plan: Up to 5 branches
- Enterprise plan: Unlimited branches

---

### 5. Branding & Customization

**Description**: Customize store appearance and identity.

**Capabilities**:
- Upload store logo
- Upload banner image
- Set primary and secondary brand colors
- Customize marketplace storefront
- Custom domain (Enterprise plan)

**User Flow** (Upload Logo):
1. Owner navigates to Store Settings > Branding
2. Owner clicks "Upload Logo"
3. Owner selects image file (PNG/JPG, max 2MB)
4. System uploads to Firebase Storage
5. System generates thumbnail
6. Logo displayed on receipts, marketplace, and portal

---

### 6. Subscription & Billing

**Description**: Manage subscription plans and billing.

**Subscription Plans**:

**Free Plan** (IDR 0):
- Max 50 products
- Max 2 staff
- 1 branch
- Basic reports
- Email support
- Marketplace listing (with platform fee)

**Basic Plan** (IDR 99,000/month):
- Max 500 products
- Max 5 staff
- 1 branch
- Standard reports
- Email support
- Reduced platform fees

**Pro Plan** (IDR 299,000/month):
- Max 5,000 products
- Max 20 staff
- Up to 5 branches
- Advanced reports
- Mobile app
- API access
- Priority support
- No platform fees

**Enterprise Plan** (Custom):
- Unlimited products
- Unlimited staff
- Unlimited branches
- Custom reports
- API access
- Dedicated account manager
- SLA guarantee
- Custom domain

**Capabilities**:
- View current plan and usage
- Upgrade/downgrade plan
- View billing history
- Download invoices
- Update payment method
- Cancel subscription

**User Flow** (Upgrade Plan):
1. Owner navigates to Subscription
2. Owner views current plan and usage
3. Owner clicks "Upgrade to Pro"
4. System calculates prorated amount
5. Owner confirms upgrade
6. Payment processed via Midtrans
7. Plan activated immediately
8. New limits applied

**Business Rules**:
- Proration: Credit for unused time on downgrade
- Grace period: 7 days after payment failure
- Feature access: Limited features if subscription expired
- Data retention: 30 days after cancellation

---

## Use Cases

### Use Case 1: New Store Registration

**Scenario**: "Toko Makmur" owner wants to join the platform.

**Steps**:
1. Owner creates account (email verification)
2. Owner fills store registration:
   - Name: "Toko Makmur"
   - Category: Grocery
   - Type: Retail
   - Address: Jl. Sudirman No. 123, Jakarta
   - Phone: +62211234567
3. System generates slug: "toko-makmur"
4. System creates tenant with Free plan
5. Owner can now add products and staff

---

### Use Case 2: Configure Business Hours

**Scenario**: Store opens 8 AM - 8 PM on weekdays, later on weekends.

**Steps**:
1. Owner navigates to Settings > Business Hours
2. Owner sets weekday hours: 08:00 - 20:00
3. Owner sets Saturday hours: 08:00 - 22:00
4. Owner sets Sunday hours: 10:00 - 18:00
5. Owner adds holidays: Dec 25, Jan 1
6. System saves configuration
7. Marketplace shows accurate operating hours

---

### Use Case 3: Invite Cashier

**Scenario**: Owner hires new cashier "Budi" to operate POS.

**Steps**:
1. Owner goes to Staff Management
2. Owner clicks "Invite Staff"
3. Owner enters:
   - Email: budi@gmail.com
   - Name: Budi Santoso
   - Role: Cashier
4. System sends invitation email to Budi
5. Budi receives email, clicks activation link
6. Budi creates password
7. Budi logs in and accesses POS only

---

### Use Case 4: Upgrade to Pro Plan

**Scenario**: Store growing, needs more products and branches.

**Steps**:
1. Owner hits 50 product limit on Free plan
2. Owner navigates to Subscription
3. System shows: "You've reached 50/50 products. Upgrade to add more."
4. Owner clicks "Upgrade to Pro"
5. System shows: IDR 299,000/month, 5,000 products, 5 branches
6. Owner confirms and pays via credit card
7. Plan upgraded immediately
8. Owner can now add more products and branches

---

## Business Rules

### Store Slug

- Must be unique across all tenants
- Auto-generated from store name: "Toko Makmur" → "toko-makmur"
- Only lowercase letters, numbers, hyphens
- Cannot be changed after creation (to preserve marketplace URLs)

### Staff Invitation

- Invitation valid for 7 days
- Max 3 pending invitations per staff email
- Staff must accept invitation before expiry
- Invitation revoked if email not verified in 7 days

### Subscription Limits

**Product Limits**:
- Free: 50, Basic: 500, Pro: 5,000, Enterprise: Unlimited
- Cannot add products beyond limit
- Soft delete counts toward limit

**Staff Limits**:
- Free: 2, Basic: 5, Pro: 20, Enterprise: Unlimited
- Owner always counted as 1 staff
- Inactive staff still count toward limit

**Branch Limits**:
- Free: 1, Basic: 1, Pro: 5, Enterprise: Unlimited
- Default branch created automatically
- Cannot delete last branch

### Data Retention

- **Active subscription**: Data retained indefinitely
- **Cancelled subscription**: Data retained 30 days, then deleted
- **Downgrade**: Features locked but data retained
- **Export**: Owners can export all data before cancellation

---

## Edge Cases

### Store Slug Conflict

- **Problem**: Two stores want same slug "toko-makmur"
- **Solution**: Auto-append number: "toko-makmur-2", "toko-makmur-3"
- **Alternative**: Allow owner to customize slug during registration

### Owner Account Deletion

- **Problem**: Owner wants to delete account but store still exists
- **Solution**: Require ownership transfer to another Admin first
- **Alternative**: Auto-promote oldest Admin to Owner role

### Subscription Downgrade with Excess Data

- **Problem**: Pro plan (5,000 products) downgrades to Basic (500 products) but has 1,200 products
- **Solution**: Allow downgrade but lock product creation until count reduced
- **UX**: Show warning: "You have 1,200 products. Basic plan allows 500. Archive 700 products to continue."

### Payment Failure

- **Problem**: Credit card payment fails
- **Solution**: 7-day grace period with daily email reminders
- **Actions**: After grace period, downgrade to Free plan

---

## Future Enhancements

### Advanced Features
- Store analytics dashboard
- Customer loyalty program settings
- Multi-currency support
- Custom email templates
- Webhook integrations
- API keys management

### Multi-tenant Features
- Franchise management (parent-child tenants)
- White-label marketplace
- Custom domain per tenant
- Tenant-specific themes

### Operational
- Automated backup scheduling
- Data import/export tools
- Bulk staff invitation
- Activity audit logs
- Compliance reports (tax, financial)

---

## Success Metrics

- **Store Registration Rate**: # of stores registered per month
- **Activation Rate**: % of registered stores that add products
- **Subscription Upgrade Rate**: % of Free users upgrading to paid
- **Staff Utilization**: Avg # of staff per active store
- **Feature Adoption**: % of stores using multi-branch

---

## Dependencies

- **Authentication** (01): User accounts and roles
- **Firebase Firestore**: Tenant data storage
- **Firebase Storage**: Logo and banner images
- **Payment Gateway** (Midtrans): Subscription billing

---

**Last Updated**: 2024-12-13
