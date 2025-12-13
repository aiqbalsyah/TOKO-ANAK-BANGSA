# Notifications 🔔

**Category**: COMMUNICATION, ALERTS
**Priority**: SHOULD HAVE (MVP)
**Phase**: 2-3

---

## Overview

Notifications keep store owners, staff, and customers informed about important events through multiple channels: email, push notifications, SMS, in-app alerts, and WhatsApp Business. The system sends automated notifications for order updates, inventory alerts, payment reminders, and system events, ensuring timely communication and action.

### Why This Matters

- **Timely Information**: Get notified immediately when action needed
- **Customer Satisfaction**: Keep customers updated on order status
- **Operational Efficiency**: Alerts prevent missed tasks and deadlines
- **Revenue Protection**: Payment and stock alerts prevent revenue loss
- **Multi-channel**: Reach users on their preferred communication channel
- **Automation**: Reduce manual communication overhead

---

## Business Requirements

### Primary Goals

1. **Order Notifications**: Update customers on order status (confirmed, shipped, delivered)
2. **Inventory Alerts**: Notify staff when stock low or out of stock
3. **Payment Reminders**: Alert customers and suppliers about upcoming/overdue payments
4. **System Alerts**: Inform admins about system events (errors, security)
5. **Marketing Messages**: Send promotional campaigns to customers (future)
6. **Multi-channel Delivery**: Email, push, SMS, WhatsApp, in-app
7. **Notification Preferences**: Users can customize which notifications to receive

### Problems Solved

- **Missed Orders**: Auto-notify staff of new marketplace orders
- **Stock Shortages**: Proactive low stock alerts prevent stockouts
- **Late Payments**: Reminders improve AR/AP collection rates
- **Customer Anxiety**: Order updates reduce "where's my order?" inquiries
- **Communication Overhead**: Automated messages save staff time
- **Lost Revenue**: Alerts prevent missed sales opportunities

---

## Features

### 1. Email Notifications

**Description**: Automated email notifications for various events.

**Email Types**:

**Customer Emails**:
- Order confirmation (after payment)
- Order shipped (with tracking number)
- Order delivered
- Password reset
- Email verification
- Receipt/invoice (PDF attachment)
- Return/refund confirmation
- Wishlist price drop (future)

**Store Owner/Staff Emails**:
- New order received
- Low stock alert
- Payment due reminder (AR/AP)
- Daily sales summary
- Weekly performance report
- Monthly financial report
- System alerts (errors, security)

**Email Configuration**:
```
SMTP Settings:
Server: smtp.gmail.com
Port: 587
Encryption: TLS
From Email: noreply@tokoanak.id
From Name: Toko Anak Bangsa

Templates:
- Order Confirmation
- Order Shipped
- Low Stock Alert
- Payment Reminder
(All templates customizable)

Branding:
- Store logo in header
- Store colors
- Custom footer
```

**User Flow** (Order Confirmation Email):
1. Customer places marketplace order
2. Payment confirmed via Midtrans
3. System triggers order confirmation email
4. Email template populated:
   - Order number
   - Items purchased
   - Total amount
   - Shipping address
   - Estimated delivery
5. Email sent via SMTP
6. Customer receives email within 1 minute
7. Email contains:
   ```
   Subject: Order Confirmed #ORD-MKT-20241213-001

   Hi John Doe,

   Thank you for your order!

   Order Number: #ORD-MKT-20241213-001
   Order Date: Dec 13, 2024

   Items:
   - Indomie Goreng x 10 - IDR 30,000
   - Indomie Soto x 5 - IDR 15,000

   Subtotal: IDR 45,000
   Shipping: IDR 15,000
   Total: IDR 60,000

   Shipping Address:
   John Doe
   Jl. Sudirman No. 123
   Jakarta Selatan, DKI Jakarta

   Estimated Delivery: Dec 18-20, 2024

   [Track Your Order]

   Questions? Reply to this email or WhatsApp: +628123456789

   Best regards,
   Toko Makmur Team
   ```

---

### 2. Push Notifications (Mobile/Web)

**Description**: Real-time push notifications to mobile/web apps.

**Push Notification Types**:

**Customer Notifications**:
- Order status updates
- Delivery approaching
- Product back in stock
- Flash sale alert
- Abandoned cart reminder

**Store Staff Notifications**:
- New order received
- Low stock alert
- Payment received
- System alerts

**Web Push** (Browser):
- Enabled in marketplace (customer consent required)
- Works on Chrome, Firefox, Safari
- Shows notification even when tab closed

**Mobile Push** (Future Native App):
- iOS (APNs - Apple Push Notification service)
- Android (FCM - Firebase Cloud Messaging)

**User Flow** (Order Shipped Push):
1. Store staff marks order as "Shipped"
2. System triggers push notification
3. Firebase Cloud Messaging sends push to customer's device
4. Customer's phone shows notification:
   ```
   📦 Toko Makmur

   Your order #ORD-001 has been shipped!
   Track: JNE1234567890

   Tap to track shipment →
   ```
5. Customer taps notification
6. Marketplace app opens to order tracking page

---

### 3. SMS Notifications (Indonesia)

**Description**: SMS notifications via Indonesian SMS gateway.

**SMS Gateway Providers**:
- Twilio (international, reliable)
- Zenziva (Indonesia-focused)
- Raja SMS (Indonesia local)

**SMS Use Cases**:

**High Priority Only** (SMS costs money):
- OTP (One-Time Password) for login/verification
- Payment confirmation
- Order shipped (for high-value orders)
- Payment overdue (AR collection)
- Critical system alerts

**SMS Template** (Order Shipped):
```
Toko Makmur: Order #ORD-001 dikirim via JNE (JNE1234567890).
Estimasi: 18-20 Des. Track: toko.id/track/ORD-001
```

**Configuration**:
```
SMS Settings:
Provider: Zenziva
API Key: [encrypted]
Sender ID: TOKO-MAKMUR (max 11 chars)

SMS Quota:
- Free: 0 SMS/month
- Basic: 100 SMS/month
- Pro: 500 SMS/month
- Enterprise: Unlimited

SMS Cost: IDR 250/SMS (if exceeding quota)
```

---

### 4. WhatsApp Business Notifications

**Description**: WhatsApp notifications via WhatsApp Business API.

**Why WhatsApp for Indonesia**:
- 85%+ smartphone users have WhatsApp
- Preferred communication channel
- Higher open rate than email (95% vs 20%)
- Supports rich media (images, links, buttons)
- Two-way communication

**WhatsApp Business API Setup**:
```
Provider: Twilio (WhatsApp Business Partner)
or
Provider: 360dialog, MessageBird

Requirements:
- Verified business phone number
- Approved message templates
- WhatsApp Business Account

Cost:
- Session Messages (24hr window): Free
- Template Messages: ~IDR 350/message
- User-initiated: Free
```

**WhatsApp Message Templates** (Pre-approved):
```
1. Order Confirmation
"Halo {{customer_name}}, terima kasih telah berbelanja di {{store_name}}!
Order #{{order_number}} telah dikonfirmasi.
Total: {{total}}
Estimasi: {{delivery_date}}
Track: {{tracking_link}}"

2. Order Shipped
"Halo {{customer_name}}, pesanan Anda #{{order_number}} sudah dikirim!
Kurir: {{courier}} ({{tracking_number}})
Estimasi: {{delivery_date}}
Track: {{tracking_link}}"

3. Payment Reminder
"Halo {{customer_name}}, pengingat pembayaran:
Invoice #{{invoice_number}}
Jumlah: {{amount}}
Jatuh Tempo: {{due_date}}
Bayar: {{payment_link}}"
```

**User Flow** (WhatsApp Order Update):
1. Store staff marks order as "Shipped"
2. System triggers WhatsApp notification
3. Message sent via Twilio WhatsApp API
4. Customer receives WhatsApp message:
   ```
   Toko Makmur

   Halo John Doe, pesanan Anda #ORD-MKT-001
   sudah dikirim! 📦

   Kurir: JNE Regular
   No. Resi: JNE1234567890
   Estimasi: 18-20 Des 2024

   [Track Pesanan] → toko.id/track/ORD-001

   Ada pertanyaan? Balas pesan ini.
   ```
5. Customer can reply directly
6. Store receives message in WhatsApp inbox
7. Staff responds

---

### 5. In-App Notifications

**Description**: Notifications shown within the web/mobile app.

**Notification Types**:

**Bell Icon Notifications**:
- New order received
- Low stock alert
- Payment received
- System messages
- Unread count badge

**Toast/Popup Notifications**:
- Success messages ("Product added!")
- Error messages ("Payment failed")
- Info messages ("Stock updated")
- Warning messages ("Low stock: Indomie")

**Notification Center**:
```
🔔 Notifications (5 unread)

Today:
● New order #ORD-001 received - IDR 250K
  5 minutes ago

● Low stock alert: Indomie Goreng (85 PCS)
  2 hours ago

● Payment received from Toko Makmur - IDR 500K
  3 hours ago

Yesterday:
○ Daily sales report ready
  Dec 12, 2024 08:00

○ New customer registered: John Doe
  Dec 12, 2024 14:30

[Mark All as Read] [View All]
```

**User Flow**:
1. New order received from marketplace
2. System creates in-app notification
3. Bell icon shows red badge: 🔔 (1)
4. Owner hears notification sound (if enabled)
5. Owner clicks bell icon
6. Notification panel opens
7. Shows: "New order #ORD-001 - IDR 250K"
8. Owner clicks notification
9. Redirects to order details page
10. Notification marked as read
11. Badge updates: 🔔

---

### 6. Inventory Alerts

**Description**: Automated alerts when stock levels critical.

**Alert Triggers**:

**Low Stock Alert**:
```
Trigger: Available Stock ≤ Low Stock Threshold

Example:
Product: Indomie Goreng
Threshold: 100 PCS
Current: 85 PCS
→ Alert Triggered ✓

Notification sent to:
- Store owner (email + push + in-app)
- Inventory manager (email + in-app)

Message:
"⚠️ Low Stock Alert

Product: Indomie Goreng
Current Stock: 85 PCS
Reorder Level: 100 PCS
Supplier: PT Indofood

Suggested Action: Create Purchase Order

[Create PO] [Snooze Alert]"
```

**Out of Stock Alert**:
```
Trigger: Available Stock = 0

Example:
Product: Indomie Soto
Current: 0 PCS
→ Out of Stock ✓

Notification sent immediately:
"🚨 OUT OF STOCK

Product: Indomie Soto
Last Sale: 10 minutes ago
Pending Orders: 3 orders affected

URGENT: Restock immediately or contact customers.

[Create PO] [Contact Supplier]"
```

**Stock Replenished Notification**:
```
Trigger: Stock increased above threshold after low/out alert

Message:
"✅ Stock Replenished

Product: Indomie Goreng
Previous: 85 PCS
Current: 485 PCS (+400 PCS)

Low stock alert cleared.
All pending orders can be fulfilled."
```

---

### 7. Payment Notifications

**Description**: Reminders for upcoming and overdue payments.

**AR (Customer Payment) Reminders**:

**Payment Due Soon** (7 days before):
```
Email/WhatsApp to Customer:

Subject: Payment Due in 7 Days

Halo Toko Makmur,

Pengingat pembayaran:

Invoice: #INV-001
Amount: IDR 1,554,000
Due Date: Dec 20, 2024 (7 days from now)

Please arrange payment to avoid late fees.

[View Invoice] [Make Payment]

Terima kasih,
Toko Anak Bangsa
```

**Payment Overdue**:
```
Email/WhatsApp to Customer:

Subject: ⚠️ Payment Overdue

Halo Toko Makmur,

Invoice #INV-001 is now OVERDUE:

Amount: IDR 1,554,000
Due Date: Dec 20, 2024 (3 days ago)
Late Fee: IDR 50,000/day

Please settle immediately to avoid credit hold.

[Pay Now] [Contact Us]
```

**AP (Supplier Payment) Reminders**:

**Owner Reminder** (7 days before):
```
Email/In-App to Owner:

Subject: Upcoming Supplier Payment

Payment due in 7 days:

Supplier: PT Indofood
Invoice: #INV-PT-INDO-001
Amount: IDR 3,080,250
Due Date: Jan 12, 2025

Ensure sufficient cash available.

[Schedule Payment] [View Details]
```

---

### 8. Notification Preferences

**Description**: Users can customize which notifications to receive.

**Preference Categories**:

**Order Notifications**:
- ☑ New order received (In-app, Email, Push)
- ☑ Order shipped (In-app, Email, WhatsApp)
- ☐ Order delivered (Email only)

**Inventory Notifications**:
- ☑ Low stock alert (In-app, Email)
- ☑ Out of stock (In-app, Email, SMS)
- ☐ Stock replenished (In-app)

**Payment Notifications**:
- ☑ Payment received (In-app, Email)
- ☑ Payment due (Email, WhatsApp)
- ☑ Payment overdue (Email, WhatsApp, SMS)

**Marketing Notifications** (Customer):
- ☐ Promotional offers (Email, WhatsApp)
- ☐ New product announcements (Email)
- ☐ Flash sales (Push, Email)

**Quiet Hours**:
- No notifications between: 22:00 - 07:00
- Except: Critical alerts (out of stock, payment received)

**User Flow** (Update Preferences):
1. Owner navigates to Settings > Notifications
2. Reviews current preferences
3. Changes:
   - Disables: Order delivered email (too many)
   - Enables: Low stock SMS (critical)
   - Sets quiet hours: 22:00 - 07:00
4. Saves preferences
5. System updates notification rules
6. Future notifications respect preferences

---

## Use Cases

### Use Case 1: Customer Order Journey

**Scenario**: Customer places order, receives updates at each stage.

**Steps**:
1. **Order Placed**:
   - Customer completes checkout
   - Immediately receives:
     - Email: Order confirmation with invoice
     - Push: "Order confirmed!"
     - WhatsApp: Order details + track link

2. **Payment Confirmed** (2 minutes later):
   - Midtrans webhook received
   - Customer receives:
     - Email: Payment confirmation
     - In-app: "Payment successful"

3. **Order Processing** (Next day):
   - Store starts preparing order
   - Customer receives:
     - Push: "We're preparing your order"
     - WhatsApp: "Pesanan sedang diproses"

4. **Order Shipped** (Day 2):
   - Store marks as shipped, adds tracking
   - Customer receives:
     - Email: Shipping confirmation + tracking link
     - Push: "Order shipped! Track: JNE123"
     - WhatsApp: Full shipping details
     - SMS: "Order dikirim JNE123"

5. **In Transit Updates** (Days 3-4):
   - JNE API sends tracking updates
   - Customer receives:
     - Push: Location updates

6. **Delivered** (Day 5):
   - Courier confirms delivery
   - Customer receives:
     - Email: Delivery confirmation + review request
     - Push: "Order delivered!"
     - WhatsApp: "Terima kasih! Please review"

Total: 15 notifications across 4 channels over 5 days
Customer stays fully informed ✓

---

### Use Case 2: Low Stock Alert Response

**Scenario**: Indomie stock drops below threshold, staff responds.

**Steps**:
1. **08:30 AM**: Sale reduces stock 105 → 95 PCS (threshold: 100)
2. **08:30 AM**: System triggers low stock alert
3. **Owner receives**:
   - Email: Low stock alert with suggested PO
   - Push: "⚠️ Low stock: Indomie Goreng"
   - In-app: Notification with [Create PO] button
4. **08:35 AM**: Owner clicks [Create PO]
5. **08:40 AM**: PO created for 500 PCS, sent to supplier
6. **09:00 AM**: Supplier confirms delivery tomorrow
7. **Next day 10:00 AM**: Stock received, updated to 595 PCS
8. **10:01 AM**: System sends:
   - Email: "Stock replenished, alert cleared"
   - In-app: "✅ Indomie Goreng restocked"
9. Crisis averted in 24 hours ✓

---

### Use Case 3: Payment Reminder Campaign

**Scenario**: End of month, send reminders to customers with overdue payments.

**Steps**:
1. **Nov 30**: System identifies overdue invoices
2. Finds 23 customers with overdue > 7 days
3. Total overdue: IDR 15,000,000
4. **Dec 1 08:00 AM**: Automated reminder sent
5. **Customers receive**:
   - WhatsApp: Payment reminder with amount, due date, link
   - Email: Formal invoice + payment instructions
6. **Day 1-3**: 8 customers pay (IDR 5.5M collected)
7. **Day 4**: Second reminder sent to remaining 15
8. **Day 4-7**: 7 more customers pay (IDR 6M collected)
9. **Day 8**: Final notice to 8 remaining customers
10. **Day 8-14**: 5 customers pay (IDR 2.5M collected)
11. **Result**: 20/23 paid (87%), IDR 14M collected
12. Success rate: High ✓

---

## Business Rules

### Notification Delivery

- Email delivery timeout: 30 seconds
- Push notification timeout: 10 seconds
- SMS delivery timeout: 60 seconds
- WhatsApp delivery timeout: 30 seconds
- Retry failed deliveries: 3 times with exponential backoff

### Notification Priority

**Critical** (always sent, ignore quiet hours):
- Payment received
- Out of stock
- Security alerts
- System errors

**High** (sent during business hours only):
- New order
- Low stock
- Payment due soon

**Normal** (respect quiet hours):
- Order updates
- Reports ready
- Marketing messages

### Rate Limiting

- Max 10 push notifications per user per hour
- Max 5 emails per user per hour
- Max 3 SMS per user per day
- Max 5 WhatsApp per user per day
- Prevent spam and cost control

### Data Privacy

- Users can opt-out of marketing messages
- Cannot opt-out of transactional messages (order updates)
- Unsubscribe link in all marketing emails
- GDPR/Indonesian data protection compliance

---

## Future Enhancements

### Advanced Features
- AI-driven notification timing (send when user most likely to engage)
- Predictive alerts (predict stock-out before it happens)
- Personalized notifications (based on user behavior)
- Rich media notifications (images, videos, carousels)
- Interactive notifications (reply, take action directly)

### Additional Channels
- Telegram notifications
- Line messenger (popular in Indonesia)
- Voice call notifications (critical alerts)
- Desktop notifications (Slack, Microsoft Teams integration)

### Automation
- Smart notification bundling (combine multiple low-priority into one)
- Notification scheduling (send at optimal time)
- A/B testing notification templates
- Notification analytics (open rate, click rate, conversion)

---

## Success Metrics

- **Delivery Rate**: % of notifications successfully delivered (target: >98%)
- **Open Rate**: % of emails/push opened (target: Email >20%, Push >60%)
- **Click-Through Rate**: % of notifications clicked (target: >15%)
- **Response Time**: Avg time from notification to action (target: <30 mins)
- **Opt-Out Rate**: % of users unsubscribing (target: <2%)
- **Customer Satisfaction**: Notification usefulness rating (target: >4/5)

---

## Dependencies

- **All Features**: Notifications triggered by events across all modules
- **Tenant Management** (02): Notification preferences per tenant
- **Customer Management** (07): Customer contact information
- **Order Management** (06): Order status updates
- **Inventory Management** (04): Stock alerts

---

**Last Updated**: 2024-12-13
