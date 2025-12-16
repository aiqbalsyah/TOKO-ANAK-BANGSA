# API Endpoints Documentation

Complete reference for all TOKO ANAK BANGSA API endpoints.

**Base URL:** `http://localhost:8080` (development)

---

## Table of Contents

- [Health Check](#health-check)
- [Authentication](#authentication)
- [Role Management](#role-management)

---

## Health Check

### Root Endpoint
```
GET /
```
Returns basic API information.

**Response:**
```json
{
  "message": "TOKO ANAK BANGSA API",
  "version": "1.0.0",
  "status": "healthy"
}
```

### Health Check
```
GET /api/health
```
Returns API health status and Firebase connection status.

**Response:**
```json
{
  "status": "ok",
  "service": "TOKO ANAK BANGSA API",
  "firebase": "initialized"
}
```

### Hello
```
GET /api/hello
```
Returns available API endpoints.

**Response:**
```json
{
  "message": "Hello from TOKO ANAK BANGSA API!",
  "endpoints": {
    "auth": "/api/auth/*",
    "roles": "/api/roles/*",
    "health": "/api/health"
  }
}
```

---

## Authentication

All authentication endpoints are prefixed with `/api/auth`.

### Register
```
POST /api/auth/register
```

Register a new user account.

**Rate Limit:** 5 requests/hour

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "Password123!",
  "displayName": "John Doe",
  "phoneNumber": "+628123456789" // optional
}
```

**Success Response (201):**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "user-id",
      "email": "user@example.com",
      "emailVerified": false,
      "profile": {
        "displayName": "John Doe",
        "phoneNumber": "+628123456789"
      },
      "status": "active"
    },
    "tokens": {
      "accessToken": "jwt-access-token",
      "refreshToken": "jwt-refresh-token",
      "expiresIn": 900
    }
  }
}
```

### Login
```
POST /api/auth/login
```

Login with email and password.

**Rate Limit:** 10 requests/hour

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "Password123!"
}
```

**Success Response (200):** Same as Register

### Google OAuth
```
POST /api/auth/google
```

Login or register with Google OAuth.

**Rate Limit:** 10 requests/hour

**Request Body:**
```json
{
  "idToken": "google-id-token"
}
```

**Success Response (200):** Same as Register

### Get User Info
```
GET /api/auth/me
```

Get current user information.

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "user-id",
      "email": "user@example.com",
      "emailVerified": true,
      "profile": { ... },
      "tenants": [ ... ],
      "status": "active"
    }
  }
}
```

### Update Profile
```
PATCH /api/auth/profile
```

Update user profile information.

**Rate Limit:** 20 requests/hour

**Headers:**
```
Authorization: Bearer {access-token}
```

**Request Body:**
```json
{
  "displayName": "Jane Doe",
  "phoneNumber": "+628123456789",
  "bio": "Store owner"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "user": { ... }
  }
}
```

### Verify Email
```
POST /api/auth/verify-email
```

Verify email address with token.

**Rate Limit:** 5 requests/hour

**Request Body:**
```json
{
  "token": "verification-token"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Email verified successfully"
}
```

### Resend Verification
```
POST /api/auth/resend-verification
```

Resend email verification.

**Rate Limit:** 3 requests/hour

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Verification email sent"
}
```

### Forgot Password
```
POST /api/auth/forgot-password
```

Request password reset email.

**Rate Limit:** 3 requests/hour

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Password reset email sent if account exists"
}
```

### Reset Password
```
POST /api/auth/reset-password
```

Reset password with token.

**Rate Limit:** 3 requests/hour

**Request Body:**
```json
{
  "token": "reset-token",
  "newPassword": "NewPassword123!"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Password reset successfully"
}
```

### Refresh Token
```
POST /api/auth/refresh
```

Refresh access token.

**Rate Limit:** 30 requests/hour

**Request Body:**
```json
{
  "refreshToken": "jwt-refresh-token"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "accessToken": "new-jwt-token",
    "refreshToken": "new-refresh-token",
    "expiresIn": 900
  }
}
```

### Logout
```
POST /api/auth/logout
```

Logout current user.

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

### Delete Account
```
DELETE /api/auth/account
```

Delete user account (requires ownership transfer if tenant owner).

**Headers:**
```
Authorization: Bearer {access-token}
```

**Request Body:**
```json
{
  "password": "current-password"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Account deleted successfully"
}
```

---

## Role Management

All role management endpoints are prefixed with `/api/roles`.

**Required Permission:** Admin level (70+) or Owner level (90+) depending on operation.

### List Roles
```
GET /api/roles?tenantId={tenantId}&page=1&limit=20
```

List all roles for a tenant (system + custom).

**Rate Limit:** 30 requests/hour

**Headers:**
```
Authorization: Bearer {access-token}
```

**Query Parameters:**
- `tenantId` (required): Tenant UUID
- `isCustom` (optional): Filter by custom/system roles
- `isActive` (optional): Filter by active status
- `minLevel` (optional): Minimum role level
- `maxLevel` (optional): Maximum role level
- `search` (optional): Search name/description
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 20)

**Success Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "owner",
      "name": "Owner",
      "description": "Tenant owner with full access",
      "level": 90,
      "permissions": { ... },
      "isSystemRole": true,
      "isCustom": false,
      "isActive": true,
      "createdAt": "2024-12-13T10:00:00Z",
      "updatedAt": "2024-12-13T10:00:00Z"
    }
  ],
  "meta": {
    "total": 5,
    "page": 1,
    "limit": 20,
    "hasNext": false
  }
}
```

### Get Role Details
```
GET /api/roles/{roleId}?tenantId={tenantId}
```

Get role details with effective permissions.

**Rate Limit:** 50 requests/hour

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "role-uuid",
    "tenantId": "tenant-uuid",
    "name": "Store Manager",
    "description": "Manages daily operations",
    "level": 50,
    "inheritsFrom": "owner",
    "permissions": { ... },
    "effectivePermissions": { ... },
    "isCustom": true,
    "isActive": true,
    "createdBy": "user-uuid",
    "createdAt": "2024-12-13T10:00:00Z",
    "updatedAt": "2024-12-13T10:00:00Z"
  }
}
```

### Create Custom Role
```
POST /api/roles
```

Create a custom role.

**Rate Limit:** 10 requests/hour

**Permission:** Admin (70+)

**Headers:**
```
Authorization: Bearer {access-token}
```

**Request Body:**
```json
{
  "tenantId": "tenant-uuid",
  "name": "Store Manager",
  "description": "Manages daily operations",
  "level": 50,
  "inheritsFrom": "owner",
  "permissions": {
    "canCreateProducts": true,
    "canEditProducts": true,
    "canDeleteProducts": false,
    "canViewProducts": true,
    "canCreateOrders": true,
    "canEditOrders": true,
    "canDeleteOrders": false,
    "canViewOrders": true,
    "canRefundOrders": false,
    "canManageCustomers": true,
    "canViewCustomers": true,
    "canManageInventory": true,
    "canViewInventory": true,
    "canViewReports": true,
    "canExportReports": false,
    "canManageSettings": false,
    "canManageUsers": false,
    "canManagePayments": false
  }
}
```

**Success Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "role-uuid",
    "tenantId": "tenant-uuid",
    "name": "Store Manager",
    ...
  }
}
```

### Update Custom Role
```
PATCH /api/roles/{roleId}?tenantId={tenantId}
```

Update a custom role.

**Rate Limit:** 20 requests/hour

**Permission:** Admin (70+)

**Headers:**
```
Authorization: Bearer {access-token}
```

**Request Body:** (all fields optional)
```json
{
  "name": "Senior Store Manager",
  "description": "Updated description",
  "level": 55,
  "permissions": {
    "canManageUsers": true
  },
  "isActive": true
}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": { ... }
}
```

### Delete Custom Role
```
DELETE /api/roles/{roleId}?tenantId={tenantId}
```

Delete a custom role (soft delete).

**Rate Limit:** 5 requests/hour

**Permission:** Owner (90+)

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Role deleted successfully"
}
```

**Error if users assigned (409):**
```json
{
  "success": false,
  "error": "Cannot delete role. 5 users still have this role. Please reassign users first."
}
```

### Get Role Templates
```
GET /api/roles/templates
```

Get predefined role templates.

**Rate Limit:** 50 requests/hour

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "name": "Admin",
      "description": "Administrator with most permissions",
      "level": 70,
      "permissions": { ... }
    },
    {
      "name": "Manager",
      "description": "Store manager",
      "level": 50,
      "permissions": { ... }
    },
    {
      "name": "Cashier",
      "description": "Cashier with order creation",
      "level": 30,
      "permissions": { ... }
    },
    {
      "name": "Inventory Manager",
      "description": "Manages inventory only",
      "level": 30,
      "permissions": { ... }
    }
  ]
}
```

### Clone Role
```
POST /api/roles/{roleId}/clone
```

Clone an existing role.

**Rate Limit:** 10 requests/hour

**Permission:** Admin (70+)

**Headers:**
```
Authorization: Bearer {access-token}
```

**Request Body:**
```json
{
  "name": "Cloned Store Manager",
  "tenantId": "tenant-uuid"
}
```

**Success Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "new-uuid",
    "name": "Cloned Store Manager",
    ...
  }
}
```

### Get Users with Role
```
GET /api/roles/{roleId}/users?tenantId={tenantId}&page=1&limit=20
```

Get list of users with specific role.

**Rate Limit:** 30 requests/hour

**Permission:** Admin (70+)

**Headers:**
```
Authorization: Bearer {access-token}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "userId": "user-uuid",
      "email": "user@example.com",
      "profile": {
        "displayName": "John Doe"
      },
      "roleAssignment": {
        "roleId": "role-uuid",
        "assignedAt": "2024-12-13T10:00:00Z",
        "assignedBy": "admin-uuid",
        "customPermissions": { ... }
      }
    }
  ],
  "meta": {
    "total": 3,
    "page": 1,
    "limit": 20,
    "hasNext": false
  }
}
```

---

## Error Responses

All endpoints return errors in this format:

```json
{
  "success": false,
  "error": "Error message description"
}
```

### HTTP Status Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request (validation error)
- `401` - Unauthorized (missing/invalid token)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found
- `409` - Conflict (duplicate, constraint violation)
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

---

## Testing

Use the Postman collection for easy testing:
- Location: `apps/api/docs/postman/TOKO-ANAK-BANGSA-API.postman_collection.json`
- Guide: `apps/api/docs/postman/README.md`

---

## Rate Limiting

Rate limits are per IP address and reset hourly. See individual endpoints for specific limits.

If rate limited, wait for the window to reset or contact support for increased limits.

---

**Last Updated:** 2025-12-13
