# Authentication & Authorization 🔐

**Category**: AUTH
**Priority**: MUST HAVE (MVP)
**Phase**: 1

---

## Overview

Authentication and authorization system that allows users to securely register, log in, and access the TOKO ANAK BANGSA platform based on their roles. The system supports both traditional email/password authentication and social login (Google OAuth), with built-in security features like email verification, password reset, and role-based access control.

### Why This Matters

- **Security**: Protects user accounts and sensitive business data
- **Access Control**: Ensures users only access features appropriate to their role
- **User Experience**: Seamless login experience with multiple authentication methods
- **Trust**: Email verification and password reset build user confidence
- **Compliance**: Meets security standards for e-commerce and financial data

---

## Business Requirements

### Primary Goals

1. **Secure User Access**: Allow users to create accounts and log in securely
2. **Role-Based Access**: Different permissions for Owners, Staff, Cashiers, and Customers
3. **Account Recovery**: Users can reset forgotten passwords via email
4. **Email Verification**: Confirm user email addresses to prevent fraud
5. **Social Login**: Quick registration/login using Google account
6. **Session Management**: Automatic logout and session security

### Problems Solved

- **Account Security**: Prevent unauthorized access to stores and customer data
- **Forgotten Passwords**: Easy password recovery without admin intervention
- **Spam Accounts**: Email verification reduces fake registrations
- **User Convenience**: Social login reduces friction in signup process
- **Multi-device Access**: Users can log in from multiple devices securely

---

## Features

### 1. Email/Password Registration

**Description**: Users can create accounts using email address and password.

**Capabilities**:
- Email format validation
- Password strength requirements (8+ chars, uppercase, lowercase, number)
- Unique email enforcement (one account per email)
- Automatic email verification sent on registration
- Encrypted password storage (bcrypt hashing)

**User Flow**:
1. User enters email, password, name, and role
2. System validates email format and password strength
3. System checks if email already exists
4. System creates account and sends verification email
5. User clicks verification link in email
6. Email is verified, user can now log in

---

### 2. Email/Password Login

**Description**: Registered users can log in with their credentials.

**Capabilities**:
- Secure password verification
- Generate JWT access token (15 min expiry)
- Generate JWT refresh token (7 day expiry)
- Return user profile data on successful login
- Error handling for invalid credentials

**User Flow**:
1. User enters email and password
2. System verifies credentials
3. System checks if email is verified
4. System generates access and refresh tokens
5. User redirected to appropriate dashboard based on role

**Security Features**:
- Failed login attempt tracking
- Account lockout after 5 failed attempts (15 min)
- Email notification on suspicious login activity

---

### 3. Email Verification

**Description**: Users must verify their email address before full access.

**Capabilities**:
- Verification email sent automatically on registration
- Verification link valid for 24 hours
- Resend verification email (max 3 times per hour)
- Visual indicator for unverified accounts

**Business Rules**:
- Unverified users cannot log in to Store Portal
- Unverified customers can browse but not purchase
- Verification required before password reset

**User Flow**:
1. User registers account
2. System sends verification email
3. User clicks link in email
4. System marks email as verified
5. User can now access full features

---

### 4. Password Reset

**Description**: Users can reset forgotten passwords via email.

**Capabilities**:
- Request password reset by email
- Secure reset token sent via email (1 hour validity)
- Set new password with strength validation
- Token can only be used once
- Old password immediately invalidated

**User Flow**:
1. User clicks "Forgot Password" on login page
2. User enters email address
3. System sends password reset email
4. User clicks reset link in email
5. User enters new password (with confirmation)
6. System validates new password and updates account
7. User can log in with new password

**Security Features**:
- Rate limiting: 3 reset requests per hour per email
- Reset tokens expire after 1 hour
- Notification email sent when password is reset

---

### 5. Google OAuth (Social Login)

**Description**: Quick registration and login using Google account.

**Capabilities**:
- Sign up with Google in one click
- Log in with Google in one click
- Auto-populate name and email from Google
- Use Google profile picture as avatar
- Email automatically verified

**User Flow** (New User):
1. User clicks "Continue with Google"
2. Google login popup appears
3. User selects Google account
4. System receives Google user info
5. System creates new account with verified email
6. User redirected to platform

**User Flow** (Existing User):
1. User clicks "Continue with Google"
2. Google login popup appears
3. System matches Google email to existing account
4. User logged in automatically

---

### 6. Role-Based Access Control (RBAC)

**Description**: Different user roles have different permissions and access levels.

**User Roles**:

**Owner** (Store Portal):
- Full access to all store features
- Can manage staff and permissions
- Can view all reports and analytics
- Can configure store settings
- Can manage subscription and billing

**Admin** (Store Portal):
- Can manage products, inventory, customers
- Can process orders and refunds
- Can view most reports
- Cannot manage subscription or delete store

**Staff** (Store Portal):
- Can manage products and inventory
- Can process orders
- Limited report access
- Cannot manage users or settings

**Cashier** (Store Portal):
- Can only access POS system
- Can process transactions
- Can search products
- Cannot modify inventory or view reports

**Customer** (Marketplace):
- Can browse and search products
- Can make purchases
- Can manage orders and addresses
- Can write reviews
- Cannot access store management

**Platform Admin** (Platform Admin Portal):
- Can manage all tenants/stores
- Can view platform analytics
- Can moderate content
- System configuration access

---

### 7. Session Management

**Description**: Secure handling of user sessions across devices.

**Capabilities**:
- JWT-based authentication
- Access token (short-lived: 15 minutes)
- Refresh token (long-lived: 7 days)
- Automatic token refresh
- Revoke tokens on logout
- Max 5 active sessions per user

**Security Features**:
- Tokens stored securely (HTTP-only cookies for web)
- Automatic logout after 30 days of inactivity
- Device tracking (browser, OS, IP)
- Suspicious activity detection

---

### 8. Profile Management

**Description**: Users can view and update their profile information.

**Editable Fields**:
- Full name
- Phone number
- Avatar/profile picture
- Language preference (Indonesian/English)
- Timezone

**Non-Editable Fields**:
- Email (requires separate verification flow)
- Role (only Owner/Admin can change)
- Account creation date

---

## Use Cases

### Use Case 1: Store Owner First-Time Registration

**Scenario**: Toko Makmur owner wants to start using the platform.

**Steps**:
1. Owner visits registration page
2. Owner enters: Email (makmur@toko.com), Password, Full Name, Phone
3. Owner selects role: "Store Owner"
4. System creates account and sends verification email
5. Owner checks email and clicks verification link
6. Email verified, owner can now log in
7. Owner proceeds to create store/tenant profile

---

### Use Case 2: Customer Quick Checkout with Google

**Scenario**: Customer wants to buy products but doesn't want to create password.

**Steps**:
1. Customer browses marketplace, adds products to cart
2. Customer clicks "Checkout"
3. System prompts to login or register
4. Customer clicks "Continue with Google"
5. Customer selects Google account in popup
6. System creates account automatically (email verified)
7. Customer completes checkout immediately

---

### Use Case 3: Cashier Forgot Password

**Scenario**: Cashier forgot password and cannot access POS.

**Steps**:
1. Cashier clicks "Forgot Password" on login screen
2. Cashier enters email address
3. System sends password reset email
4. Cashier checks email and clicks reset link
5. Cashier enters new password (must meet strength requirements)
6. System confirms password reset
7. Cashier logs in with new password

---

### Use Case 4: Failed Login Attempts

**Scenario**: Someone tries to brute-force an account.

**Steps**:
1. Attacker tries login with wrong password (attempt 1-4)
2. System tracks failed attempts
3. Attacker tries again (attempt 5)
4. System locks account for 15 minutes
5. System sends email notification to account owner
6. After 15 minutes, account auto-unlocks
7. Legitimate user can log in normally

---

## Business Rules

### Password Requirements

- Minimum 8 characters
- At least 1 uppercase letter (A-Z)
- At least 1 lowercase letter (a-z)
- At least 1 number (0-9)
- Maximum 128 characters
- Special characters allowed but not required

### Email Verification

- Verification link valid for 24 hours
- Max 3 verification emails per hour
- Unverified users have limited access:
  - Store users: Cannot log in to portal
  - Customers: Can browse but cannot purchase

### Account Security

- Account locked after 5 failed login attempts
- Lockout duration: 15 minutes
- Password reset token valid for 1 hour
- Maximum 3 password reset requests per hour per email

### Session Limits

- Maximum 5 active sessions (devices) per user
- Oldest session auto-revoked when limit exceeded
- Automatic logout after 30 days of inactivity
- Tokens invalidated on password change

---

## Edge Cases

### Email Change

- **Problem**: User wants to change email address
- **Solution**: Require verification of new email before changing
- **Flow**: Request change → Verify new email → Update email

### Multiple Google Accounts

- **Problem**: User has multiple Google accounts
- **Solution**: Each Google account linked to separate platform account
- **Note**: Users cannot merge accounts (future enhancement)

### Deleted Store Owner

- **Problem**: Owner deletes account but store still exists
- **Solution**: Require ownership transfer before account deletion
- **Alternative**: Promote Admin to Owner role

### Concurrent Login Sessions

- **Problem**: User logs in from 2 devices simultaneously
- **Solution**: Allow up to 5 concurrent sessions
- **Benefit**: Users can access from phone, tablet, desktop

---

## Future Enhancements

### Multi-Factor Authentication (MFA)
- SMS verification code
- Authenticator app (Google Authenticator, Authy)
- Required for Pro/Enterprise plans
- Optional for other plans

### Additional Social Logins
- Facebook OAuth
- Apple Sign-In
- Phone number login (OTP)

### Advanced Security
- Biometric authentication (mobile app)
- Hardware security keys (U2F)
- Risk-based authentication
- Login location tracking
- Suspicious activity alerts

### Account Features
- Account deletion (GDPR compliance)
- Data export (GDPR compliance)
- Login activity history
- Trusted devices management
- Session management (view/revoke active sessions)

---

## Success Metrics

- **Registration Completion Rate**: % of users who complete registration
- **Email Verification Rate**: % of users who verify email within 24 hours
- **Login Success Rate**: % of successful logins vs failed attempts
- **Password Reset Rate**: % of users who use password reset
- **Social Login Adoption**: % of users using Google OAuth

---

## Dependencies

- **Firebase Authentication**: User management and OAuth
- **Firebase Firestore**: User profile storage
- **Email Service**: Verification and password reset emails
- **JWT Library**: Token generation and validation

---

**Last Updated**: 2024-12-13
