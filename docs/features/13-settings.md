# Settings ⚙️

**Category**: CONFIGURATION, PREFERENCES
**Priority**: MUST HAVE (MVP)
**Phase**: 1-3

---

## Overview

Settings provides comprehensive configuration options for store owners, staff, and customers to customize their experience. This includes tenant-level settings (store operations, payment, tax, integrations), user preferences (notifications, display, language), and system configuration. Settings are organized by category for easy navigation and management.

### Why This Matters

- **Customization**: Each store can configure the system to match their business needs
- **Flexibility**: Adapt the system to different business types and sizes
- **User Experience**: Personal preferences improve usability
- **Compliance**: Configure tax, receipt, and legal settings for Indonesian regulations
- **Integration**: Connect third-party services (payment gateways, shipping, etc.)
- **Control**: Fine-tune system behavior and access permissions

---

## Business Requirements

### Primary Goals

1. **Store Settings**: Configure business operations (hours, tax, pricing)
2. **Payment Settings**: Setup payment methods and gateways
3. **Notification Settings**: Manage notification preferences
4. **Receipt Settings**: Customize receipt format and content
5. **Integration Settings**: Connect third-party services
6. **User Preferences**: Personal settings for individual users
7. **Security Settings**: Password, 2FA, session management

### Problems Solved

- **One-Size-Fits-All**: Settings allow customization per business needs
- **Complex Setup**: Organized settings make configuration easy
- **Compliance**: Tax and legal settings ensure regulatory compliance
- **Integration**: Easy connection to Indonesian services (Midtrans, JNE, etc.)
- **User Control**: Users can customize their experience
- **Security**: Granular security controls protect business data

---

## Features

### 1. Store Settings

**Description**: Core business configuration and operational settings.

**Settings Categories**:

**General Store Information**:
```
Store Name: Toko Makmur
Business Type: ● Retail ○ Wholesale ○ Both
Store Category: Grocery Store

Store Logo: [Upload Image]
Store Banner: [Upload Image]
Favicon: [Upload Image]

Contact Information:
Phone: +62 21 1234 5678
WhatsApp: +62 812 3456 7890
Email: info@toko-makmur.com
Website: www.toko-makmur.com

Physical Address:
Street: Jl. Sudirman No. 123
City: Jakarta Selatan
State/Province: DKI Jakarta
Postal Code: 12345
Country: Indonesia

[Save Changes]
```

**Business Hours**:
```
Operating Hours:

Monday:    ☑ Open  [08:00] to [20:00]
Tuesday:   ☑ Open  [08:00] to [20:00]
Wednesday: ☑ Open  [08:00] to [20:00]
Thursday:  ☑ Open  [08:00] to [20:00]
Friday:    ☑ Open  [08:00] to [22:00]
Saturday:  ☑ Open  [08:00] to [22:00]
Sunday:    ☑ Open  [10:00] to [18:00]

Holidays (Store Closed):
● Dec 25, 2024 - Christmas
● Jan 1, 2025 - New Year
● Feb 10, 2025 - Chinese New Year
[+ Add Holiday]

[Save Changes]
```

**Timezone & Localization**:
```
Timezone: Asia/Jakarta (UTC+7)
Language: ● Indonesian  ○ English
Currency: IDR (Indonesian Rupiah)
Date Format: ● DD/MM/YYYY  ○ MM/DD/YYYY
Time Format: ● 24-hour  ○ 12-hour

Number Format:
Decimal Separator: ● Comma (,)  ○ Period (.)
Thousands Separator: ● Period (.)  ○ Comma (,)
Decimal Places: [0] for IDR

[Save Changes]
```

---

### 2. Tax Settings

**Description**: Configure Indonesian tax rates and compliance.

**Tax Configuration**:
```
Tax Settings:

Enable Tax: ☑ Yes  ☐ No

Tax Name: PPN (Pajak Pertambahan Nilai)
Tax Rate: [11] %
Tax Included in Prices: ☐ Yes  ☑ No (added at checkout)

Tax Number (NPWP):
[01.234.567.8-901.000]

Tax Invoice Settings:
☑ Generate tax invoices for business customers
☑ Require customer NPWP for tax invoices
☑ Auto-number tax invoices (sequence)

Tax Invoice Prefix: FP-
Next Invoice Number: 00001

Tax Reporting:
Monthly Tax Report: ☑ Auto-generate
Quarterly Tax Report: ☑ Auto-generate

[Save Changes]
```

**Tax Exemptions**:
```
Tax-Exempt Products/Categories:
● Basic necessities (Sembako)
● Fresh produce
● Unprocessed foods

Tax-Exempt Customers:
● Government entities (with official PO)
● NGOs (with certificate)

[Manage Exemptions]
```

---

### 3. Pricing & Discount Settings

**Description**: Configure pricing tiers and discount rules.

**Multi-tier Pricing**:
```
Price Tier Configuration:

Tier A (Wholesale):
Name: Grosir
Default Markup: [20] % above cost
Minimum Order: [IDR 500,000]
Eligible Customers: Wholesale customer type

Tier B (Retail):
Name: Eceran
Default Markup: [40] % above cost
Minimum Order: None
Eligible Customers: All customers (default)

Tier C (Premium/Marketplace):
Name: Premium
Default Markup: [60] % above cost
Minimum Order: None
Eligible Customers: Marketplace, VIP customers

Pricing Rules:
☑ Enforce Tier A ≤ Tier B ≤ Tier C
☐ Allow cashier to override prices (requires manager PIN)
☑ Round prices to nearest: [100] IDR

[Save Changes]
```

**Discount Settings**:
```
Discount Configuration:

Maximum Discount (without approval): [20] %
Discounts > 20% require: ● Manager PIN  ○ Owner approval

Discount Types Allowed:
☑ Percentage discount
☑ Fixed amount discount
☑ Buy X Get Y
☐ Tiered discounts (bulk)

Promo Code Settings:
☑ Allow promo codes
Maximum uses per code: [100]
Maximum uses per customer: [1]

[Save Changes]
```

---

### 4. Inventory Settings

**Description**: Configure stock tracking and alerts.

**Inventory Configuration**:
```
Stock Tracking:

Enable Stock Tracking: ☑ Yes  ☐ No
Allow Negative Stock: ☐ Yes  ☑ No
Stock Deduction: ● At checkout  ○ When order confirmed

Low Stock Alerts:
☑ Enable low stock alerts
Global Low Stock Threshold: [100] units
Alert Recipients:
  ☑ owner@store.com
  ☑ inventory@store.com
Alert Frequency: ● Immediate  ○ Daily digest

Stock Adjustment:
Require Reason Code: ☑ Yes
Require Approval (> value): [IDR 1,000,000]
Approved by: ● Owner  ● Admin  ○ Staff

Stock Valuation Method:
● FIFO (First In, First Out)
○ LIFO (Last In, First Out)
○ Weighted Average

[Save Changes]
```

---

### 5. Payment Gateway Settings

**Description**: Configure payment methods and gateway integrations.

**Payment Methods**:
```
Accepted Payment Methods:

In-Store (POS):
☑ Cash
☑ Debit/Credit Card (EDC Terminal)
☑ QRIS (scan at counter)
☑ Bank Transfer
☑ Customer Credit (AR)

Online (Marketplace):
☑ QRIS (GoPay, OVO, Dana, ShopeePay)
☑ Virtual Account (BCA, Mandiri, BNI, BRI)
☑ Credit/Debit Cards (Visa, MasterCard)
☐ Cash on Delivery (COD)
☐ Installments (Kredivo, Akulaku)

[Save Changes]
```

**Midtrans Configuration**:
```
Midtrans Payment Gateway:

Status: ☑ Enabled  ☐ Disabled
Environment: ● Production  ○ Sandbox

API Credentials:
Server Key: [••••••••••••••••••] [Show]
Client Key: [••••••••••••••••••] [Show]
Merchant ID: [M123456]

Payment Settings:
Payment Expiry: [24] hours
Auto-Capture: ☑ Yes  ☐ No (manual)
3D Secure: ☑ Required  ○ Optional

Enabled Payment Channels:
☑ Credit Card (2.9% + IDR 2,000)
☑ GoPay (2%)
☑ ShopeePay (2%)
☑ OVO (1.5%)
☑ QRIS (0.7%)
☑ BCA VA (IDR 4,000/trx)
☑ Mandiri VA (IDR 4,000/trx)
☑ BNI VA (IDR 4,000/trx)
☑ BRI VA (IDR 4,000/trx)

Notification URL (Webhook):
https://api.tokoanak.id/webhooks/midtrans
[Test Connection]

[Save Changes]
```

---

### 6. Receipt Settings

**Description**: Customize receipt format and content.

**Receipt Configuration**:
```
Receipt Settings:

Header:
☑ Show store logo
☑ Show store name
☑ Show store address
☑ Show phone number
☐ Show website

Tax Information:
☑ Show tax number (NPWP)
☑ Show tax breakdown on receipt
☑ Show tax invoice number (for business customers)

Footer Message:
[Terima kasih atas kunjungan Anda!
Barang yang sudah dibeli tidak dapat dikembalikan.]

Disclaimer Text:
[Simpan struk ini sebagai bukti pembayaran yang sah.]

☑ Show "Powered by Toko Anak Bangsa Platform"

Paper Size:
● 58mm (small)  ○ 80mm (standard)

Print Settings:
Auto-print after transaction: ☑ Yes  ☐ No
Number of copies: [1]

[Preview Receipt] [Save Changes]
```

**Receipt Template Preview**:
```
═══════════════════════════════════════
          TOKO ANAK BANGSA
      Jl. Sudirman No. 123
         Jakarta Selatan
      Tel: +62 21 1234 5678
      NPWP: 01.234.567.8-901.000
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

---

### 7. Shipping Settings (Marketplace)

**Description**: Configure shipping methods and courier integrations.

**Shipping Configuration**:
```
Shipping Methods:

Enable Shipping: ☑ Yes  ☐ No

Flat Rate Shipping:
☑ Enabled
Flat Rate: [IDR 15,000]
Free Shipping Minimum: [IDR 100,000]

Courier Integration:
☑ JNE (API connected)
☑ J&T (API connected)
☑ SiCepat (API connected)
☐ Ninja Van
☐ Anteraja

Store Pickup:
☑ Allow store pickup
Pickup Address: [Same as store address]
Pickup Hours: [Same as business hours]

Shipping Zones (Enterprise):
☐ Enable zone-based shipping
(Coming soon)

[Save Changes]
```

**JNE Integration**:
```
JNE Courier Settings:

Status: ☑ Enabled  ☐ Disabled
Environment: ● Production  ○ Testing

API Credentials:
API Key: [••••••••••••••••••] [Show]
Origin City: Jakarta Selatan
Origin Postal Code: 12345

Services Enabled:
☑ JNE Regular (REG)
☑ JNE Express (YES)
☐ JNE Super Speed (SS)

Auto-generate Airwaybill: ☑ Yes  ☐ No
Auto-print Label: ☐ Yes  ☑ No (manual)

[Test Connection] [Save Changes]
```

---

### 8. Notification Settings

**Description**: Configure notification channels and preferences.

(See Feature 12 - Notifications for detailed settings)

```
Notification Preferences:

Email Notifications:
SMTP Server: smtp.gmail.com
Port: 587
Encryption: TLS
From Email: noreply@tokoanak.id
From Name: Toko Anak Bangsa

SMS Notifications (Pro+):
Provider: Zenziva
API Key: [••••••••••••••••••]
Sender ID: TOKO-MAKMUR

WhatsApp Notifications (Enterprise):
Provider: Twilio
Account SID: [••••••••••••••••••]
Auth Token: [••••••••••••••••••]
WhatsApp Number: +62 812 3456 7890

[Save Changes]
```

---

### 9. Security Settings

**Description**: Configure security and access control.

**Password Policy**:
```
Password Requirements:

Minimum Length: [8] characters
Require:
☑ Uppercase letter
☑ Lowercase letter
☑ Number
☐ Special character

Password Expiry: ● Never  ○ Every [90] days

Account Lockout:
Lock after [5] failed login attempts
Lockout Duration: [30] minutes
☑ Send email on account lockout

Session Management:
Session Timeout: [15] minutes (idle)
Maximum Session Duration: [8] hours
☑ Remember me (7 days)

[Save Changes]
```

**Two-Factor Authentication (Enterprise)**:
```
2FA Settings:

Enable 2FA: ☐ Mandatory for all  ☑ Optional  ○ Disabled

2FA Methods:
☑ SMS (one-time code)
☑ Email (one-time code)
☐ Authenticator app (Google Authenticator, Authy)

2FA Required For:
☑ Owner
☑ Admin
☐ Staff
☐ Cashier

[Save Changes]
```

**IP Whitelist (Enterprise)**:
```
IP Access Control:

☐ Restrict access to specific IP addresses

Allowed IP Addresses:
● 203.142.xxx.xxx (Office)
● 114.79.xxx.xxx (Home)
[+ Add IP Address]

☑ Block after 10 failed attempts from same IP
Block Duration: [24] hours

[Save Changes]
```

---

### 10. Integration Settings

**Description**: Connect third-party services and APIs.

**Available Integrations**:

**Payment Gateways**:
- ☑ Midtrans (connected)
- ☐ Xendit
- ☐ Doku

**Shipping Couriers**:
- ☑ JNE (connected)
- ☑ J&T (connected)
- ☐ SiCepat
- ☐ Ninja Van

**Accounting Software** (Pro+):
- ☐ Jurnal.id
- ☐ Accurate Online
- ☐ MYOB
- ☐ QuickBooks

**Marketing Tools**:
- ☐ Google Analytics
- ☐ Facebook Pixel
- ☐ Mailchimp
- ☐ WhatsApp Business API

**E-commerce Platforms** (Enterprise):
- ☐ Tokopedia
- ☐ Shopee
- ☐ Lazada
- ☐ Bukalapak

[Manage Integrations]

---

### 11. User Preferences

**Description**: Personal settings for individual users.

**Display Preferences**:
```
My Preferences:

Interface:
Theme: ● Light  ○ Dark  ○ Auto (follow system)
Language: ● Indonesian  ○ English

Dashboard:
Default View: ● Executive  ○ Sales  ○ Inventory
Refresh Interval: [5] minutes

Notifications:
☑ Email notifications
☑ Push notifications (browser)
☐ SMS notifications
☑ In-app notifications

Quiet Hours:
☑ Enable quiet hours
From: [22:00] To: [07:00]
Except: ☑ Critical alerts

[Save Preferences]
```

**Keyboard Shortcuts**:
```
POS Shortcuts:

F1: Help
F2: Product Search
F3: Customer Lookup
F4: Apply Discount
F9: Hold Transaction
F12: Complete Payment
ESC: Clear Cart

☑ Enable keyboard shortcuts
[Customize Shortcuts] (Enterprise)
```

---

## Business Rules

### Settings Hierarchy

**Platform Level** (by Platform Admin):
- System defaults
- Feature availability by plan
- API rate limits
- Data retention policies

**Tenant Level** (by Store Owner):
- Store information
- Business hours
- Tax settings
- Payment methods
- Receipt format
- Staff permissions

**User Level** (by Individual User):
- Display preferences
- Notification preferences
- Language
- Keyboard shortcuts

### Permission Requirements

**View Settings**: All users
**Edit Store Settings**: Owner, Admin
**Edit Tax Settings**: Owner only
**Edit Payment Settings**: Owner only
**Edit User Preferences**: Own preferences only
**Edit Security Settings**: Owner only
**Manage Integrations**: Owner, Admin (with limitations)

### Validation Rules

- Tax rate: 0-100%
- Discount: 0-100% or fixed amount
- Session timeout: 5-480 minutes
- Password length: 6-50 characters
- Low stock threshold: ≥ 0
- Price markup: ≥ 0%

---

## Edge Cases

### Settings Changed Mid-Transaction

- **Problem**: Owner changes tax rate while cashier processing transaction
- **Solution**: Use tax rate at transaction start time, not current setting
- **Apply**: Tax rate changes apply to new transactions only

### Invalid Payment Gateway Credentials

- **Problem**: Owner enters wrong Midtrans API key
- **Solution**: Validate credentials on save with test API call
- **UX**: "Invalid API key. Please check credentials and try again."

### Conflicting Business Hours

- **Problem**: Set closing time before opening time
- **Solution**: Validation prevents saving invalid hours
- **UX**: "Closing time must be after opening time."

---

## Future Enhancements

### Advanced Settings
- Multi-location settings (different settings per branch)
- Role-based settings access (granular permissions)
- Settings version control (track changes, rollback)
- Settings templates (preset configs for business types)
- Settings import/export

### AI-Powered
- Smart defaults (suggest settings based on business type)
- Optimization recommendations (analyze usage, suggest improvements)
- Automated settings tuning (adjust based on performance)

### Integration
- Settings sync across devices
- Cloud backup of settings
- Settings API for programmatic access
- Webhook for settings changes

---

## Success Metrics

- **Settings Completion Rate**: % of tenants with all required settings configured
- **Default Usage**: % of tenants using default vs custom settings
- **Settings Change Frequency**: Avg # of setting changes per month
- **Integration Adoption**: % of tenants with at least 1 integration connected
- **Error Rate**: % of invalid settings saved (should be 0%)

---

## Dependencies

- **Tenant Management** (02): Tenant-scoped settings
- **Authentication** (01): User preferences
- **All Features**: Settings control behavior of all features

---

**Last Updated**: 2024-12-13
