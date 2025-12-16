# TOKO ANAK BANGSA API - Postman Collection

Complete Postman collection for testing all API endpoints.

## Quick Start

### 1. Import Collection

1. Open Postman
2. Click "Import" button
3. Select `TOKO-ANAK-BANGSA-API.postman_collection.json`
4. Collection will be imported with all endpoints

### 2. Configure Environment

The collection uses variables that are automatically set after certain requests:

**Auto-set Variables:**
- `accessToken` - Set after login/register
- `refreshToken` - Set after login/register
- `userId` - Set after login/register
- `roleId` - Set after creating a role

**Manual Variables:**
- `baseUrl` - Default: `http://localhost:8080`
- `tenantId` - Set this manually after creating a tenant

**To set variables:**
1. Click on the collection
2. Go to "Variables" tab
3. Set `baseUrl` if different from localhost:8080
4. Set `tenantId` once you have a tenant

### 3. Testing Workflow

#### A. Initial Setup
```
1. Health Check > Root          - Verify API is running
2. Health Check > Health        - Check Firebase connection
```

#### B. Authentication Flow
```
1. Authentication > Register    - Create account (auto-sets tokens)
2. Authentication > Get User Info - Verify login
3. Authentication > Update Profile - Test profile update
```

Or use login if account exists:
```
1. Authentication > Login       - Login existing user (auto-sets tokens)
```

#### C. Role Management Flow
```
1. Set `tenantId` variable manually
2. Role Management > Get Role Templates - See available templates
3. Role Management > List Roles - See all roles (system + custom)
4. Role Management > Create Custom Role - Create a role (auto-sets roleId)
5. Role Management > Get Role Details - View role with permissions
6. Role Management > Update Custom Role - Modify role
7. Role Management > Clone Role - Clone existing role
8. Role Management > Get Users with Role - See role assignments
9. Role Management > Delete Custom Role - Remove role (if no users)
```

## Endpoint Groups

### Health Check (3 endpoints)
- `GET /` - Root endpoint
- `GET /api/health` - Health check with Firebase status
- `GET /api/hello` - API info and available endpoints

### Authentication (12 endpoints)
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login with email/password
- `POST /api/auth/google` - Google OAuth login
- `GET /api/auth/me` - Get current user info
- `PATCH /api/auth/profile` - Update user profile
- `POST /api/auth/verify-email` - Verify email with token
- `POST /api/auth/resend-verification` - Resend verification email
- `POST /api/auth/forgot-password` - Request password reset
- `POST /api/auth/reset-password` - Reset password with token
- `POST /api/auth/refresh` - Refresh access token
- `POST /api/auth/logout` - Logout user
- `DELETE /api/auth/account` - Delete user account

### Role Management (8 endpoints)
- `GET /api/roles` - List all roles (system + custom)
- `GET /api/roles/{roleId}` - Get role details
- `POST /api/roles` - Create custom role
- `PATCH /api/roles/{roleId}` - Update custom role
- `DELETE /api/roles/{roleId}` - Delete custom role
- `GET /api/roles/templates` - Get role templates
- `POST /api/roles/{roleId}/clone` - Clone existing role
- `GET /api/roles/{roleId}/users` - Get users with role

## Authentication

Most endpoints require authentication. The collection handles this automatically:

1. After login/register, `accessToken` is saved automatically
2. Authenticated requests use: `Authorization: Bearer {{accessToken}}`
3. If token expires, use the "Refresh Token" request

## Rate Limits

Be aware of rate limits:

**Authentication:**
- Register: 5/hour
- Login: 10/hour
- Verification: 3-5/hour
- Password Reset: 3/hour
- Token Refresh: 30/hour
- Profile Update: 20/hour

**Role Management:**
- List/Get: 30-50/hour
- Create: 10/hour
- Update: 20/hour
- Delete: 5/hour
- Clone: 10/hour

## Common Scenarios

### Scenario 1: New User Registration
```
1. POST /api/auth/register
   Body: { email, password, displayName }
   ✅ Saves accessToken, refreshToken, userId

2. POST /api/auth/verify-email
   Body: { token } (from email - currently stubbed)

3. GET /api/auth/me
   ✅ Verify user is logged in
```

### Scenario 2: Creating Custom Roles
```
1. Set tenantId variable in collection

2. GET /api/roles/templates
   ✅ See available templates

3. POST /api/roles
   Body: { tenantId, name, level, permissions }
   ✅ Creates role, saves roleId

4. GET /api/roles?tenantId={{tenantId}}
   ✅ See all roles including new one
```

### Scenario 3: Token Refresh
```
1. POST /api/auth/refresh
   Body: { refreshToken: "{{refreshToken}}" }
   ✅ Gets new tokens, updates variables
```

## Response Format

All endpoints return consistent format:

**Success:**
```json
{
  "success": true,
  "data": { ... }
}
```

**Error:**
```json
{
  "success": false,
  "error": "Error message"
}
```

## HTTP Status Codes

- `200` - Success (GET, PATCH, DELETE)
- `201` - Created (POST)
- `400` - Bad Request (validation error)
- `401` - Unauthorized (missing/invalid token)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found
- `409` - Conflict (duplicate, constraint violation)
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

## Testing Tips

1. **Start with Health Check** - Always verify API is running first
2. **Register First** - Create an account to get authentication tokens
3. **Save tenantId** - You'll need this for role management
4. **Check Rate Limits** - Don't spam requests
5. **Use Variables** - Tokens are auto-saved, use `{{accessToken}}`
6. **Test Error Cases** - Try invalid data to see error responses

## Scripts

The collection includes test scripts that automatically:
- Save `accessToken` after login/register
- Save `refreshToken` after login/register
- Save `userId` after login/register
- Save `roleId` after creating a role

## Troubleshooting

### "Unauthorized" errors
- Check if `accessToken` is set in variables
- Token may have expired - use "Refresh Token" endpoint
- Re-login if refresh token also expired

### "tenantId is required" errors
- Set `tenantId` variable in collection variables
- You need to create a tenant first (future endpoint)

### "Cannot modify system roles" errors
- Use `roleId` of a custom role, not system roles (owner, member, super_admin)

### Rate limit errors
- Wait for the rate limit window to reset (check error message)
- Rate limits are per IP address per hour

## Next Steps

After importing this collection:
1. Start the Flask API: `flask run --debug --port=8080`
2. Test health check endpoint
3. Register a new user
4. Create a tenant (when tenant endpoints are ready)
5. Test role management endpoints

## Support

For API documentation, see:
- `apps/api/docs/dev-guide/01-setup.md`
- `docs/features/01-authentication.md`
- `apps/api/docs/todos/auth-sytem-and-profile-management.md`
- `apps/api/docs/todos/role-management-api.md`
