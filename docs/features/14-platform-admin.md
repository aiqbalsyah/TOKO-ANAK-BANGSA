# Platform Admin 🔧

**Category**: ADMINISTRATION, SYSTEM MANAGEMENT
**Priority**: MUST HAVE (Platform Operation)
**Phase**: 1 (Foundation)

---

## Overview

Platform Admin provides system-level administration capabilities for managing the entire TOKO ANAK BANGSA platform. This includes tenant management, subscription handling, user administration, system monitoring, analytics, and platform configuration. Platform admins have access to cross-tenant data and controls necessary for platform operations, support, and business growth.

### Why This Matters

- **Platform Operations**: Manage all tenants and users from central dashboard
- **Business Growth**: Track tenant acquisition, retention, and revenue metrics
- **Customer Support**: Quickly assist tenants with issues and configuration
- **System Health**: Monitor performance, uptime, and error rates
- **Revenue Management**: Manage subscriptions, billing, and payments
- **Data Governance**: Ensure data privacy, security, and compliance

---

## Business Requirements

### Primary Goals

1. **Tenant Management**: Create, view, edit, suspend, and delete tenant accounts
2. **User Administration**: Manage platform users across all tenants
3. **Subscription Management**: Handle plans, billing, payments, and upgrades
4. **System Monitoring**: Track platform health, performance, and errors
5. **Analytics & Reporting**: Platform-wide business intelligence
6. **Support Tools**: Impersonate users, view logs, assist with issues
7. **Configuration**: Set platform defaults, feature flags, and system settings

### Problems Solved

- **Tenant Support**: Quickly identify and resolve tenant issues
- **Revenue Visibility**: Track MRR, churn, and growth metrics
- **System Reliability**: Proactively detect and fix issues
- **Fraud Prevention**: Identify suspicious activity and block bad actors
- **Resource Management**: Monitor and optimize platform resource usage
- **Compliance**: Ensure platform meets regulatory requirements

---

## Features

### 1. Platform Dashboard

**Description**: Executive view of platform health and business metrics.

**Key Metrics**:

**Platform Overview**:
```
┌─────────────────────────────────────────────────────┐
│ PLATFORM DASHBOARD - TOKO ANAK BANGSA               │
├─────────────────────────────────────────────────────┤
│                                                     │
│ ┌────────────┐ ┌────────────┐ ┌─────────────────┐ │
│ │ Tenants    │ │ Active     │ │ MRR             │ │
│ │ 1,247      │ │ Users      │ │ IDR 285,000,000 │ │
│ │ ↑ 12% MoM  │ │ 5,834      │ │ ↑ 18% MoM       │ │
│ └────────────┘ └────────────┘ └─────────────────┘ │
│                                                     │
│ Subscription Breakdown:                             │
│ ┌─────────────────────────────────────────────────┐│
│ │ Free: 487 (39%) | Basic: 385 (31%)             ││
│ │ Pro: 298 (24%)  | Enterprise: 77 (6%)          ││
│ └─────────────────────────────────────────────────┘│
│                                                     │
│ System Health:                                      │
│ ┌─────────────────────────────────────────────────┐│
│ │ API Uptime: 99.94% | Avg Response: 125ms       ││
│ │ Error Rate: 0.08%  | Queued Jobs: 234          ││
│ └─────────────────────────────────────────────────┘│
│                                                     │
│ Top Issues (Last 24h):                              │
│ • 3 payment failures (Midtrans timeout)             │
│ • 5 tenants exceeding product limit                 │
│ • 12 low stock alerts triggered                     │
└─────────────────────────────────────────────────────┘
```

---

### 2. Tenant Management

**Description**: Manage all store accounts (tenants) on the platform.

**Tenant List View**:
```
TENANTS (1,247 total)

Filters: [All] [Active] [Trial] [Suspended] [Cancelled]
Search: [Toko...]

Tenant Name        | Plan       | MRR        | Users | Status   | Joined
-------------------|------------|------------|-------|----------|--------
Toko Makmur        | Pro        | IDR 299K   | 8     | Active   | Jan 2023
Warung Sari        | Basic      | IDR 99K    | 3     | Active   | Mar 2024
CV Mitra Jaya      | Enterprise | IDR 2.5M   | 45    | Active   | Jun 2022
Toko Sejahtera     | Free       | IDR 0      | 2     | Trial    | Dec 2024
Toko ABC           | Pro        | IDR 299K   | 5     | Suspended| Aug 2023

[View] [Edit] [Suspend] [Delete]
```

**Tenant Details**:
```
TENANT: Toko Makmur (ID: TNT-20230115-001)

Basic Information:
Owner: Pak Ahmad (ahmad@toko-makmur.com)
Phone: +62 812 3456 7890
Address: Jl. Sudirman No. 123, Jakarta Selatan
NPWP: 01.234.567.8-901.000
Status: ● Active

Subscription:
Current Plan: Pro (IDR 299,000/month)
Billing Cycle: Monthly
Next Billing: Jan 15, 2025
Payment Method: Credit Card (••••4242)
Auto-renew: ☑ Yes

Usage Stats:
Products: 487 / 5,000 (10%)
Staff: 8 / 20 (40%)
Branches: 2 / 5 (40%)
Storage: 2.4 GB / 10 GB (24%)

Activity:
Total Revenue (Platform Fee): IDR 125,000,000
Last Login: 2 hours ago
Support Tickets: 3 (all resolved)

[Edit Tenant] [Change Plan] [Suspend] [Delete]
[View as Tenant] (Impersonate)
```

**Tenant Actions**:

**Create Tenant**:
- Manual tenant creation by admin
- Used for onboarding enterprise clients
- Set custom plan and pricing

**Suspend Tenant**:
- Temporarily disable tenant access
- Reasons: Non-payment, TOS violation, request
- Data retained, can be reactivated

**Delete Tenant**:
- Permanent deletion (30-day grace period)
- Export data before deletion
- Anonymize or hard delete based on GDPR

**Impersonate Tenant**:
- Log in as tenant to troubleshoot issues
- View tenant's dashboard and data
- All actions logged for audit trail
- Warning banner: "Logged in as admin"

---

### 3. User Administration

**Description**: Manage all platform users across tenants.

**User List View**:
```
PLATFORM USERS (5,834 total)

Filters: [All] [Active] [Suspended] [Unverified]
Search: [Name, email...]

Name          | Email              | Role         | Tenant        | Status    | Last Login
--------------|--------------------|--------------| --------------|-----------|-----------
Pak Ahmad     | ahmad@toko.com     | Owner        | Toko Makmur   | Active    | 2h ago
Budi Santoso  | budi@toko.com      | Cashier      | Toko Makmur   | Active    | 5h ago
Siti Rahayu   | siti@warung.com    | Admin        | Warung Sari   | Active    | 1d ago
John Doe      | john@gmail.com     | Customer     | N/A           | Active    | 3d ago
Spam User     | spam@fake.com      | Customer     | N/A           | Suspended | Never

[View] [Suspend] [Delete]
```

**User Actions**:

**Suspend User**:
- Block user access
- Reasons: Fraud, abuse, violation
- Can be reversed

**Reset Password**:
- Generate password reset link
- Send to user's email
- Log action for security

**Merge Accounts**:
- Merge duplicate user accounts
- Transfer order history and data
- Update references

---

### 4. Subscription Management

**Description**: Manage subscription plans, billing, and revenue.

**Subscription Plans**:
```
SUBSCRIPTION PLANS

Plan Name  | Price/mo   | Tenants | Features
-----------|------------|---------|---------------------------
Free       | IDR 0      | 487     | 50 products, 2 staff
Basic      | IDR 99K    | 385     | 500 products, 5 staff
Pro        | IDR 299K   | 298     | 5K products, 20 staff, API
Enterprise | Custom     | 77      | Unlimited, custom features

[Edit Plans] [Create Plan]
```

**Revenue Analytics**:
```
SUBSCRIPTION REVENUE

Monthly Recurring Revenue (MRR): IDR 285,000,000
Annual Run Rate (ARR): IDR 3,420,000,000

MRR Breakdown:
- Free: IDR 0 (487 tenants)
- Basic: IDR 38,115,000 (385 × IDR 99K)
- Pro: IDR 89,102,000 (298 × IDR 299K)
- Enterprise: IDR 157,783,000 (77 tenants, avg IDR 2.05M)

MRR Growth:
- New: +IDR 25M (42 new paid tenants)
- Expansion: +IDR 12M (18 upgrades)
- Contraction: -IDR 5M (8 downgrades)
- Churn: -IDR 8M (12 cancellations)
- Net New MRR: +IDR 24M (+9.2%)

Churn Rate: 1.8% (target: <3%)
LTV/CAC Ratio: 8.5:1 (excellent)
```

**Billing Management**:
```
BILLING ISSUES

Upcoming Renewals (Next 7 Days): 87 tenants (IDR 22.5M)
Failed Payments (Last 24h): 3 tenants (IDR 897K)
  - Toko ABC: Card expired (retry in 3 days)
  - Warung XYZ: Insufficient funds (retry tomorrow)
  - Toko 123: Card declined (contact needed)

Refund Requests: 2 pending
  - Toko Sejahtera: Cancelled within 7 days (approve)
  - Warung Sari: Dissatisfied (review case)

[Process Refunds] [Retry Failed Payments]
```

---

### 5. System Monitoring

**Description**: Monitor platform health, performance, and errors.

**System Health Dashboard**:
```
SYSTEM HEALTH

Uptime (Last 30 Days):
API: 99.94% (4.3 hours downtime)
Web: 99.97% (1.8 hours downtime)
Database: 99.99% (0.5 hours downtime)

Performance:
Avg API Response Time: 125ms (target: <200ms) ✓
95th Percentile: 380ms (target: <500ms) ✓
Database Query Time: 45ms (target: <100ms) ✓

Resources:
CPU Usage: 42% (peak: 78%)
Memory Usage: 58% (peak: 82%)
Disk Usage: 3.2 TB / 10 TB (32%)
Network: 12 Gbps in/out

Background Jobs:
Queued: 234
Processing: 12
Failed (24h): 8 (0.08% failure rate)

[View Detailed Metrics] [Set up Alerts]
```

**Error Monitoring**:
```
ERRORS (Last 24 Hours)

Total Errors: 847 (0.08% error rate)

Top Errors:
1. MidtransTimeoutException - 234 occurrences
   Impact: Payment processing delays
   Status: Investigating (Midtrans API slow response)

2. ProductNotFoundException - 156 occurrences
   Impact: Cart issues on marketplace
   Status: Fixed (cache invalidation issue)

3. DatabaseConnectionTimeout - 45 occurrences
   Impact: Slow page loads
   Status: Monitoring (database connection pool tuning)

4. InvalidTokenException - 89 occurrences
   Impact: User logout
   Status: Expected (expired sessions)

[View Error Details] [Create Incident]
```

**Incident Management**:
```
ACTIVE INCIDENTS

[Critical] Midtrans API Slow Response
Started: 2 hours ago
Impact: Payment processing delayed 5-10s
Affected Tenants: All (1,247)
Status: Investigating
Updates:
  - 14:00: Issue detected, contacted Midtrans
  - 14:30: Midtrans confirms high load on their end
  - 15:00: Midtrans scaling servers, ETA 1 hour

[Resolved] Database Connection Pool Exhausted
Started: 6 hours ago
Resolved: 5 hours ago
Impact: API errors, slow page loads
Root Cause: Connection leak in inventory module
Fix: Deployed hotfix v2.3.1

[View All Incidents]
```

---

### 6. Platform Analytics

**Description**: Business intelligence across all tenants.

**Tenant Analytics**:
```
TENANT METRICS

Total Tenants: 1,247
Active Tenants (90 days): 1,108 (88.9%)
New Tenants (30 days): 42
Churned Tenants (30 days): 12

Tenant Lifetime:
Avg Tenant Age: 14.2 months
Retention Rate:
  - Month 1: 92%
  - Month 3: 78%
  - Month 6: 68%
  - Month 12: 58%
  - Month 24: 45%

Tenant Segmentation:
By Industry:
  - Grocery: 487 (39%)
  - Fashion: 285 (23%)
  - Electronics: 198 (16%)
  - Restaurants: 142 (11%)
  - Others: 135 (11%)

By Location:
  - Jakarta: 385 (31%)
  - Surabaya: 187 (15%)
  - Bandung: 142 (11%)
  - Semarang: 98 (8%)
  - Others: 435 (35%)
```

**Usage Analytics**:
```
PLATFORM USAGE

Total Transactions (Last 30 Days): 2,458,745
Total GMV (Gross Merchandise Value): IDR 1.2 Trillion
Avg Transaction Value: IDR 488,320

Products:
Total Products: 487,234
Products Added (30 days): 12,456
Products Sold (30 days): 3,245,678 units

Customers:
Total Customers: 234,567
New Customers (30 days): 18,456
Repeat Customer Rate: 42%

Orders:
Total Orders: 145,678
Avg Orders per Tenant: 117
Order Fulfillment Time: 2.3 days avg
```

---

### 7. Support Tools

**Description**: Tools for platform admin to assist tenants.

**Tenant Impersonation**:
```
IMPERSONATE TENANT

Select Tenant: [Toko Makmur ▼]
Reason: [Troubleshooting cart issue]
Duration: [1 hour ▼]

[Start Impersonation]

⚠️ Warning:
- All actions logged for audit
- Banner shown to indicate admin mode
- Session expires after duration
- Do not make changes without tenant consent
```

**Activity Logs**:
```
AUDIT LOGS

Filter: [All Actions] [Admin Actions] [Security Events]
Tenant: [All Tenants ▼]
Date: [Last 7 Days ▼]

Timestamp           | User         | Action             | Tenant      | IP Address
--------------------|--------------|--------------------| ------------|--------------
2024-12-13 15:30:25 | admin@toko   | Impersonate Tenant | Toko Makmur | 203.142.x.x
2024-12-13 14:15:10 | admin@toko   | Suspend Tenant     | Spam Store  | 203.142.x.x
2024-12-13 12:05:45 | admin@toko   | Change Plan        | Warung Sari | 203.142.x.x
2024-12-13 10:22:18 | ahmad@toko   | Update Product     | Toko Makmur | 114.79.x.x
```

**Support Tickets**:
```
SUPPORT TICKETS

Status: [Open: 23] [In Progress: 12] [Resolved: 345]

Ticket ID | Tenant        | Subject                   | Priority | Status
----------|---------------|---------------------------|----------|--------
#1234     | Toko Makmur   | Payment not processing    | High     | Open
#1233     | Warung Sari   | Low stock alert not sent  | Medium   | In Progress
#1232     | CV Mitra      | Report export error       | Low      | Resolved

[View Ticket] [Assign to Me]
```

---

### 8. Platform Configuration

**Description**: System-level settings and feature flags.

**Feature Flags**:
```
FEATURE FLAGS

Feature                    | Enabled | Rollout | Description
---------------------------|---------|---------|------------------
marketplace_v2             | ☑ Yes   | 100%    | New marketplace UI
inventory_forecasting      | ☐ No    | 0%      | AI stock prediction
multi_currency             | ☐ No    | 0%      | Currency support
whatsapp_integration       | ☑ Yes   | 50%     | WhatsApp Business
advanced_reports           | ☑ Yes   | 100%    | Enhanced analytics

[Manage Features]
```

**System Settings**:
```
PLATFORM DEFAULTS

New Tenant Defaults:
Default Plan: Free
Trial Period: 14 days
Default Language: Indonesian
Default Currency: IDR
Default Timezone: Asia/Jakarta

Rate Limits:
API Calls: 1000/hour (Free), 10000/hour (Pro)
Webhook Retries: 3 attempts
Email Sending: 100/day (Free), 1000/day (Pro)

Data Retention:
Transaction Data: 3 years (or tenant lifetime)
Deleted Tenant Data: 30 days grace period
Logs: 90 days
Backups: Daily (30 days retention)

[Save Settings]
```

---

## Use Cases

### Use Case 1: Onboard Enterprise Client

**Scenario**: New enterprise client (chain store) wants custom plan.

**Steps**:
1. Admin receives inquiry from "Alfamart" (large chain)
2. Admin navigates to Platform > Tenants > Create Tenant
3. Fills tenant information:
   - Name: Alfamart Indonesia
   - Owner: procurement@alfamart.com
   - Business Type: Retail Chain
4. Creates custom plan:
   - Name: "Alfamart Custom"
   - Price: IDR 25,000,000/month
   - Products: Unlimited
   - Staff: Unlimited
   - Branches: 500
   - Features: All + custom integrations
5. Sets up tenant with demo data
6. Sends onboarding email with credentials
7. Schedules onboarding call
8. Tenant successfully onboarded ✓

---

### Use Case 2: Handle Failed Payment

**Scenario**: Pro tenant's payment fails, admin assists.

**Steps**:
1. **12:00 AM**: Automated billing fails for "Toko Makmur"
2. System creates alert: Card declined
3. **08:00 AM**: Admin reviews failed payments dashboard
4. Finds "Toko Makmur": Pro plan (IDR 299K), card expired
5. Admin contacts tenant via email:
   ```
   Subject: Payment Failed - Action Required

   Hi Pak Ahmad,

   Your payment for Pro plan failed (card expired).

   Please update your payment method:
   [Update Payment Method]

   Your account remains active for 7 days grace period.

   Questions? Reply to this email.

   Best regards,
   TOKO ANAK BANGSA Team
   ```
6. Tenant updates card within 1 hour
7. Admin retries payment manually
8. Payment successful ✓
9. Tenant account continues without interruption

---

### Use Case 3: Investigate System Issue

**Scenario**: Multiple tenants report slow checkout.

**Steps**:
1. **14:00**: 5 support tickets: "Checkout slow/timing out"
2. Admin navigates to System Health dashboard
3. Notices: API response time spiked to 3,500ms (normally 125ms)
4. Checks error logs: 234 MidtransTimeoutException errors
5. Identifies: Midtrans API responding slowly
6. Creates incident: "Midtrans API Slow Response"
7. Contacts Midtrans support
8. Midtrans confirms: High load, scaling servers
9. Admin posts status update:
   ```
   Investigating: Slow Checkout

   We're aware of slow checkout due to payment gateway issues.
   Midtrans is scaling servers, ETA 1 hour.

   Workaround: Use bank transfer or cash payments.

   Updates: status.tokoanak.id
   ```
10. **15:30**: Midtrans issue resolved
11. Admin confirms: Response times back to normal
12. Closes incident
13. Sends follow-up to affected tenants

---

## Business Rules

### Access Control

**Platform Admin Roles**:
- **Super Admin**: Full access to everything
- **Support Admin**: Tenant support, impersonation, tickets
- **Billing Admin**: Subscriptions, billing, refunds
- **Technical Admin**: System monitoring, configuration
- **Read-Only Admin**: View-only access (auditor, analyst)

### Data Privacy

- Admins can view tenant data (with logging)
- Impersonation requires reason and approval
- All admin actions logged for audit
- Sensitive data (passwords, API keys) never shown
- GDPR/Indonesian data protection compliance

### Security

- Admin login requires 2FA (mandatory)
- IP whitelist for admin panel (optional)
- Session timeout: 30 minutes
- Failed login lockout: 3 attempts, 1 hour
- All actions logged with IP address

---

## Future Enhancements

### Advanced Features
- AI-driven tenant health scoring
- Automated churn prediction and prevention
- Self-service tenant management portal
- Advanced fraud detection
- Multi-region deployment management

### Analytics
- Cohort analysis (tenant cohorts)
- Revenue forecasting
- Custom dashboards (drag-drop widgets)
- Real-time analytics
- Data warehouse integration

### Automation
- Automated tenant onboarding
- Auto-scaling based on load
- Automated incident response
- Smart alerting (reduce noise)
- Chatbot support assistant

---

## Success Metrics

- **Platform Uptime**: >99.9%
- **Response Time**: <200ms (95th percentile)
- **Error Rate**: <0.1%
- **Tenant Satisfaction**: >4.5/5
- **Support Response Time**: <2 hours
- **Churn Rate**: <3% monthly
- **MRR Growth**: >10% monthly

---

## Dependencies

- **All Features**: Platform admin manages all features
- **Tenant Management** (02): Core tenant data
- **Authentication** (01): User management
- **Financial Management** (09): Billing and revenue data

---

**Last Updated**: 2024-12-13
