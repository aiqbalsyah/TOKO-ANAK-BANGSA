# API-001: Auth API - Registration & Login

## Overview
Implement user registration and login endpoints with JWT authentication, email verification, and password reset functionality for the TOKO ANAK BANGSA platform.

## User Story
As a **store owner** or **customer**, I want to register an account and securely log in to the platform so that I can access protected features and manage my data with proper authentication.

## Acceptance Criteria

### Registration (POST /api/auth/register)
- [ ] Accept email, password, name, and role (owner/customer) in request body
- [ ] Validate email format and uniqueness
- [ ] Validate password strength (min 8 chars, uppercase, lowercase, number)
- [ ] Hash password using bcrypt before storing
- [ ] Create user document in Firebase Auth
- [ ] Create user profile in Firestore `users` collection
- [ ] Send email verification link
- [ ] Return success response with user data (excluding password)
- [ ] Return appropriate error for duplicate email
- [ ] Return appropriate error for weak password

### Login (POST /api/auth/login)
- [ ] Accept email and password in request body
- [ ] Validate credentials against Firebase Auth
- [ ] Generate JWT access token (expires in 15 minutes)
- [ ] Generate JWT refresh token (expires in 7 days)
- [ ] Return tokens and user data (excluding password)
- [ ] Return 401 error for invalid credentials
- [ ] Return 403 error for unverified email

### Email Verification (POST /api/auth/verify-email)
- [ ] Accept verification token from email link
- [ ] Validate token and update user's `emailVerified` status
- [ ] Return success message
- [ ] Return error for invalid/expired token

### Password Reset - Request (POST /api/auth/forgot-password)
- [ ] Accept email address
- [ ] Check if user exists
- [ ] Generate secure reset token (valid for 1 hour)
- [ ] Store token hash in Firestore with expiration
- [ ] Send password reset email with link
- [ ] Return success message (even if email doesn't exist - security)

### Password Reset - Complete (POST /api/auth/reset-password)
- [ ] Accept reset token and new password
- [ ] Validate token and check expiration
- [ ] Validate new password strength
- [ ] Hash new password
- [ ] Update user password in Firebase Auth
- [ ] Invalidate reset token
- [ ] Return success message
- [ ] Return error for invalid/expired token

### Get Current User (GET /api/auth/me)
- [ ] Require valid JWT in Authorization header
- [ ] Extract user ID from JWT
- [ ] Fetch and return user profile from Firestore
- [ ] Return 401 for missing/invalid token

### Update Profile (PUT /api/auth/me)
- [ ] Require valid JWT in Authorization header
- [ ] Accept name, phone, avatar URL
- [ ] Validate input data
- [ ] Update user profile in Firestore
- [ ] Return updated user data
- [ ] Return 401 for missing/invalid token

## Technical Design

### API Endpoints

```python
# Registration
POST   /api/auth/register
Request:
{
  "email": "owner@example.com",
  "password": "SecurePass123",
  "name": "John Doe",
  "role": "owner"  # or "customer"
}
Response: 201
{
  "success": true,
  "message": "Registration successful. Please check your email for verification.",
  "user": {
    "id": "user123",
    "email": "owner@example.com",
    "name": "John Doe",
    "role": "owner",
    "emailVerified": false,
    "createdAt": "2024-12-13T..."
  }
}

# Login
POST   /api/auth/login
Request:
{
  "email": "owner@example.com",
  "password": "SecurePass123"
}
Response: 200
{
  "success": true,
  "accessToken": "eyJhbGc...",
  "refreshToken": "eyJhbGc...",
  "user": {
    "id": "user123",
    "email": "owner@example.com",
    "name": "John Doe",
    "role": "owner",
    "emailVerified": true
  }
}

# Email Verification
POST   /api/auth/verify-email
Request:
{
  "token": "verification-token-here"
}
Response: 200
{
  "success": true,
  "message": "Email verified successfully"
}

# Forgot Password
POST   /api/auth/forgot-password
Request:
{
  "email": "owner@example.com"
}
Response: 200
{
  "success": true,
  "message": "Password reset email sent"
}

# Reset Password
POST   /api/auth/reset-password
Request:
{
  "token": "reset-token-here",
  "newPassword": "NewSecurePass456"
}
Response: 200
{
  "success": true,
  "message": "Password reset successful"
}

# Get Current User
GET    /api/auth/me
Headers: Authorization: Bearer <access-token>
Response: 200
{
  "success": true,
  "user": {
    "id": "user123",
    "email": "owner@example.com",
    "name": "John Doe",
    "role": "owner",
    "phone": "+62812...",
    "avatar": "https://...",
    "emailVerified": true,
    "createdAt": "2024-12-13T...",
    "updatedAt": "2024-12-13T..."
  }
}

# Update Profile
PUT    /api/auth/me
Headers: Authorization: Bearer <access-token>
Request:
{
  "name": "John Smith",
  "phone": "+628123456789",
  "avatar": "https://storage.googleapis.com/..."
}
Response: 200
{
  "success": true,
  "user": { ... updated user data ... }
}
```

### Database Schema (Firestore)

```typescript
// Collection: users
{
  id: string;                    // Firebase Auth UID
  email: string;
  name: string;
  role: 'owner' | 'admin' | 'staff' | 'cashier' | 'customer';
  phone?: string;
  avatar?: string;
  emailVerified: boolean;
  tenantId?: string;             // For store users (owner/admin/staff/cashier)
  createdAt: Timestamp;
  updatedAt: Timestamp;
}

// Collection: password_reset_tokens
{
  id: string;
  userId: string;
  tokenHash: string;
  expiresAt: Timestamp;
  used: boolean;
  createdAt: Timestamp;
}
```

### Authentication Flow

1. **Registration**:
   - Validate input → Create Firebase Auth user → Create Firestore user document → Send verification email → Return success

2. **Login**:
   - Validate credentials with Firebase Auth → Check email verified → Generate JWT tokens → Return tokens + user data

3. **Email Verification**:
   - Validate token → Update Firebase Auth emailVerified → Update Firestore user → Return success

4. **Password Reset**:
   - Request: Check user exists → Generate token → Store hash → Send email
   - Complete: Validate token → Check expiration → Update Firebase Auth password → Invalidate token

### Security Measures

- Password hashing with bcrypt (salt rounds: 10)
- JWT tokens with short expiration (access: 15min, refresh: 7 days)
- Email verification required before full access
- Password reset tokens expire in 1 hour
- Rate limiting on auth endpoints (10 requests/minute per IP)
- CORS configuration for allowed origins only
- Input validation and sanitization
- SQL injection prevention (using Firestore SDK)

## Implementation Checklist

### Phase 1: Project Setup
- [ ] Install required packages:
  ```bash
  pip install flask flask-cors firebase-admin pyjwt bcrypt python-dotenv
  ```
- [ ] Create `apps/api/requirements.txt` with dependencies
- [ ] Set up environment variables in `.env`:
  - `FIREBASE_PROJECT_ID`
  - `JWT_SECRET_KEY`
  - `JWT_ALGORITHM=HS256`
  - `ACCESS_TOKEN_EXPIRE_MINUTES=15`
  - `REFRESH_TOKEN_EXPIRE_DAYS=7`
  - `EMAIL_VERIFICATION_URL`
  - `PASSWORD_RESET_URL`

### Phase 2: Core Authentication Module
- [ ] Create `apps/api/auth/` directory structure:
  ```
  apps/api/auth/
  ├── __init__.py
  ├── routes.py          # Auth endpoints
  ├── utils.py           # JWT, password hashing
  ├── validators.py      # Input validation
  └── email.py           # Email sending
  ```
- [ ] Implement JWT utilities in `utils.py`:
  - `generate_access_token(user_id, role)`
  - `generate_refresh_token(user_id)`
  - `verify_token(token)`
  - `hash_password(password)`
  - `verify_password(password, hashed)`
- [ ] Implement validators in `validators.py`:
  - `validate_email(email)`
  - `validate_password(password)` - 8+ chars, upper, lower, number
  - `validate_registration_data(data)`
  - `validate_login_data(data)`

### Phase 3: Registration Endpoint
- [ ] Create POST `/api/auth/register` in `routes.py`
- [ ] Validate request data (email, password, name, role)
- [ ] Check email uniqueness in Firebase Auth
- [ ] Hash password with bcrypt
- [ ] Create Firebase Auth user
- [ ] Create Firestore user document in `users` collection
- [ ] Generate email verification token
- [ ] Send verification email
- [ ] Return success response with user data
- [ ] Handle errors (duplicate email, weak password, etc.)

### Phase 4: Login Endpoint
- [ ] Create POST `/api/auth/login` in `routes.py`
- [ ] Validate request data (email, password)
- [ ] Verify credentials with Firebase Auth
- [ ] Check if email is verified
- [ ] Fetch user profile from Firestore
- [ ] Generate access and refresh tokens
- [ ] Return tokens and user data
- [ ] Handle errors (invalid credentials, unverified email)

### Phase 5: Email Verification
- [ ] Create POST `/api/auth/verify-email` in `routes.py`
- [ ] Validate verification token
- [ ] Update Firebase Auth `emailVerified` status
- [ ] Update Firestore user document
- [ ] Return success message
- [ ] Handle invalid/expired token errors

### Phase 6: Password Reset
- [ ] Create POST `/api/auth/forgot-password` endpoint
- [ ] Validate email exists
- [ ] Generate secure reset token
- [ ] Store token hash in `password_reset_tokens` collection
- [ ] Send password reset email
- [ ] Return success message
- [ ] Create POST `/api/auth/reset-password` endpoint
- [ ] Validate reset token and expiration
- [ ] Validate new password strength
- [ ] Update Firebase Auth password
- [ ] Mark token as used in Firestore
- [ ] Return success message

### Phase 7: Protected Endpoints
- [ ] Create authentication middleware/decorator
- [ ] Implement `@require_auth` decorator:
  - Extract JWT from Authorization header
  - Verify token
  - Attach user data to request context
  - Return 401 for invalid/missing token
- [ ] Create GET `/api/auth/me` endpoint (protected)
- [ ] Fetch and return current user from Firestore
- [ ] Create PUT `/api/auth/me` endpoint (protected)
- [ ] Validate and update user profile
- [ ] Return updated user data

### Phase 8: Email Service Integration
- [ ] Set up email service (Firebase Auth email templates or SendGrid)
- [ ] Create email templates:
  - Verification email template
  - Password reset email template
  - Welcome email template (optional)
- [ ] Implement `send_verification_email(email, token)`
- [ ] Implement `send_password_reset_email(email, token)`
- [ ] Test email delivery

### Phase 9: Testing
- [ ] Test registration with valid data
- [ ] Test registration with duplicate email (should fail)
- [ ] Test registration with weak password (should fail)
- [ ] Test login with valid credentials
- [ ] Test login with invalid credentials (should fail)
- [ ] Test login with unverified email (should fail)
- [ ] Test email verification flow
- [ ] Test password reset request
- [ ] Test password reset completion
- [ ] Test password reset with expired token (should fail)
- [ ] Test GET /api/auth/me with valid token
- [ ] Test GET /api/auth/me without token (should fail 401)
- [ ] Test PUT /api/auth/me with valid data
- [ ] Test JWT token expiration
- [ ] Manual testing with Postman/Thunder Client

### Phase 10: Code Quality & Review
- [ ] Run `pnpm typecheck` (N/A for Python, but check if applicable)
- [ ] Run `pnpm lint` or Python linter (flake8, pylint)
- [ ] Add docstrings to all functions
- [ ] Add inline comments for complex logic
- [ ] Review error handling
- [ ] Review security measures
- [ ] Run `/bmad:bmm:workflows:code-review` workflow
- [ ] Address any issues found during code review
- [ ] Final testing after fixes

## Dependencies

### Required Packages
- `flask` - Web framework
- `flask-cors` - CORS support
- `firebase-admin` - Firebase Admin SDK
- `pyjwt` - JWT token generation/verification
- `bcrypt` - Password hashing
- `python-dotenv` - Environment variable management
- `email-validator` - Email validation

### External Services
- **Firebase Authentication** - User management
- **Firestore** - User profile storage
- **Email Service** - Verification and reset emails (Firebase Auth or SendGrid)

### Prerequisites
- Sprint 0 infrastructure completed
- Firebase project created and configured
- Firebase Admin SDK credentials available
- Email service configured

## Testing

### Unit Tests (Future)
```python
# tests/test_auth.py
def test_register_success():
    # Test successful registration
    pass

def test_register_duplicate_email():
    # Test duplicate email error
    pass

def test_login_success():
    # Test successful login
    pass

def test_login_invalid_credentials():
    # Test invalid credentials error
    pass

def test_password_reset_flow():
    # Test complete password reset flow
    pass
```

### Manual Testing Checklist

**Registration:**
- [ ] Register with valid email/password
- [ ] Register with duplicate email (should fail)
- [ ] Register with weak password (should fail)
- [ ] Register with invalid email format (should fail)
- [ ] Verify email sent
- [ ] Verify user created in Firebase Auth
- [ ] Verify user document created in Firestore

**Login:**
- [ ] Login with valid credentials
- [ ] Login with invalid password (should fail)
- [ ] Login with non-existent email (should fail)
- [ ] Login with unverified email (should fail)
- [ ] Verify access and refresh tokens returned
- [ ] Verify user data returned (no password)

**Email Verification:**
- [ ] Click verification link from email
- [ ] Verify email marked as verified in Firebase
- [ ] Verify login works after verification
- [ ] Test with invalid token (should fail)

**Password Reset:**
- [ ] Request password reset
- [ ] Verify email sent
- [ ] Click reset link and set new password
- [ ] Verify login works with new password
- [ ] Test with expired token (should fail after 1 hour)
- [ ] Test with used token (should fail)

**Protected Endpoints:**
- [ ] Access /api/auth/me with valid token
- [ ] Access /api/auth/me without token (should fail 401)
- [ ] Access /api/auth/me with expired token (should fail 401)
- [ ] Update profile with valid data
- [ ] Update profile with invalid data (should fail)

### API Testing (Postman/Thunder Client)
```json
// Collection: Auth API Tests
{
  "name": "TOKO ANAK BANGSA - Auth API",
  "requests": [
    {
      "name": "Register",
      "method": "POST",
      "url": "http://localhost:8080/api/auth/register",
      "body": {
        "email": "test@example.com",
        "password": "SecurePass123",
        "name": "Test User",
        "role": "owner"
      }
    },
    {
      "name": "Login",
      "method": "POST",
      "url": "http://localhost:8080/api/auth/login",
      "body": {
        "email": "test@example.com",
        "password": "SecurePass123"
      }
    },
    // ... other endpoints
  ]
}
```

## Notes

### Security Considerations
- **Never return passwords** in API responses
- **Always hash passwords** before storing
- **Use HTTPS** in production
- **Implement rate limiting** to prevent brute force attacks
- **Validate all inputs** to prevent injection attacks
- **Use secure JWT secret** (generate random 256-bit key)
- **Implement CSRF protection** for state-changing operations
- **Log authentication events** for security auditing

### Edge Cases
- **Concurrent registrations** with same email - use Firebase Auth's built-in uniqueness
- **Email verification timeout** - tokens valid for 24 hours, allow resend
- **Password reset abuse** - rate limit requests (max 3 per hour per email)
- **Token refresh** - implement refresh token rotation for security
- **Account lockout** - lock account after 5 failed login attempts (future)
- **Multi-device sessions** - allow multiple active sessions, track in Firestore (future)

### Future Enhancements
- [ ] Google OAuth integration (API-002)
- [ ] Facebook OAuth integration
- [ ] Multi-factor authentication (MFA)
- [ ] Session management (view/revoke active sessions)
- [ ] Account lockout after failed attempts
- [ ] Login activity log
- [ ] Remember me functionality
- [ ] Device fingerprinting
- [ ] Suspicious activity detection

### Performance Considerations
- **Database queries**: Minimize reads/writes to Firestore
- **Token generation**: Cache JWT public keys
- **Email sending**: Use queue for async processing (future)
- **Password hashing**: Bcrypt is CPU-intensive, consider async processing

### Compliance
- **GDPR**: Allow users to export/delete their data
- **Indonesian regulations**: Follow local data privacy laws
- **Email consent**: Include unsubscribe option in emails
- **Data retention**: Define policy for inactive accounts

---

**Story Status**: Ready for implementation
**Estimated Effort**: 8-12 hours
**Priority**: HIGH (Blocking other features)
