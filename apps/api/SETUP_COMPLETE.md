# ✅ Setup Complete - Flask API

**Date**: 2025-12-13
**Status**: Ready for Development

---

## What's Been Set Up

### 1. Environment Configuration ✅

**`.env` file created** with:
- Firebase service account configured
- Secure JWT secret keys generated
- CORS origins configured
- All necessary environment variables

**Python environment**:
- Python 3.12 virtual environment created
- All dependencies installed (including pydantic)
- Virtual environment location: `venv/`

### 2. Firebase Integration ✅

**Service Account**: `firebase-service-account.json`
- Project ID: `toko-anak-bangsa-dev`
- Successfully authenticated
- Firestore API enabled and tested

**Firestore Database**:
- Collections initialized:
  - `system_roles` - Seeded with 3 default roles (super_admin, owner, member)
  - `tenant_roles` - Ready for custom roles
  - `users` - Ready for user data

### 3. Auth System Implementation ✅

**All endpoints implemented and registered**:
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - Email/password login
- `POST /api/auth/google` - Google OAuth
- `POST /api/auth/logout` - Logout
- `POST /api/auth/refresh` - Token refresh
- `GET /api/auth/me` - Get user info
- `PATCH /api/auth/profile` - Update profile
- `POST /api/auth/verify-email` - Email verification
- `POST /api/auth/resend-verification` - Resend verification
- `POST /api/auth/forgot-password` - Password reset request
- `POST /api/auth/reset-password` - Reset password
- `DELETE /api/auth/account` - Delete account

**Security features**:
- Rate limiting on all endpoints (flask-limiter)
- JWT token authentication (15 min access, 7 day refresh)
- Account lockout after 5 failed login attempts
- Password strength validation
- Input sanitization via Pydantic models

**Dynamic Role System**:
- Hierarchical RBAC (levels 1-100)
- System roles (90-100): super_admin, owner, member
- Custom tenant roles (1-89) with inheritance
- Permission resolution and merging

### 4. Server Tested ✅

Flask app successfully:
- Loads without errors
- Initializes Firebase Admin SDK
- Registers all blueprints and routes
- Responds to health checks

**Test results**:
```json
GET /api/health
{
  "status": "ok",
  "service": "TOKO ANAK BANGSA API",
  "firebase": "initialized"
}

GET /
{
  "status": "healthy",
  "message": "TOKO ANAK BANGSA API",
  "version": "1.0.0"
}
```

---

## How to Run

### Development Server

**Option 1: Direct Flask**
```bash
cd apps/api
source venv/bin/activate
flask run --debug --port=8080
```

**Option 2: From project root (using pnpm)**
```bash
pnpm dev:api
```

The API will be available at: `http://localhost:8080`

### Environment Variables

Located in `apps/api/.env`:
- `FLASK_APP=app.py`
- `FLASK_ENV=development`
- `PORT=8080`
- `FIREBASE_SERVICE_ACCOUNT_PATH=./firebase-service-account.json`
- `FIREBASE_PROJECT_ID=toko-anak-bangsa-dev`
- `JWT_SECRET_KEY=<generated>`
- `SECRET_KEY=<generated>`
- `CORS_ORIGINS=http://localhost:3000,...`

---

## What Requires Firebase for Full Testing

Some features are stubbed and require Firebase setup for email functionality:

1. **Email Sending** (marked with TODO in code):
   - Verification emails (`send_verification_email`)
   - Password reset emails (`send_password_reset_email`)

   **To enable**: Configure Firebase Email Extension or SMTP in `.env`

2. **Token Revocation** (marked with TODO):
   - Currently uses soft logout
   - Full implementation needs token blacklist (Redis recommended)

---

## Files Created/Modified

### New Files
- `.env` - Environment configuration
- `venv/` - Python virtual environment
- `extensions.py` - Flask extensions (limiter)
- `models/user.py` - User Pydantic models
- `models/role.py` - Role system models
- `services/auth_service.py` - Auth business logic (590 lines)
- `services/role_service.py` - Role management (300+ lines)
- `middleware/auth.py` - JWT & RBAC middleware
- `routes/auth.py` - Auth endpoints (500+ lines)
- `scripts/init_firestore.py` - Database seeding

### Modified Files
- `app.py` - Added limiter, blueprint registration
- `requirements.txt` - Added flask-limiter
- `packages/shared-types/src/schemas/user.ts` - Dynamic role references
- `packages/shared-types/src/schemas/role.ts` - Role schemas
- `docs/sprint/status.yaml` - Updated story status

---

## Next Steps

### Phase 10: Testing & Validation

Now that the setup is complete, you can:

1. **Test endpoints with Postman/curl**:
   ```bash
   # Register a user
   curl -X POST http://localhost:8080/api/auth/register \
     -H "Content-Type: application/json" \
     -d '{
       "email": "test@example.com",
       "password": "Test123!",
       "displayName": "Test User"
     }'

   # Login
   curl -X POST http://localhost:8080/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{
       "email": "test@example.com",
       "password": "Test123!"
     }'
   ```

2. **Run code review** (optional):
   ```bash
   /bmad:bmm:workflows:code-review
   ```

3. **Configure email service** (for production):
   - Option A: Firebase Email Extension
   - Option B: SMTP (Gmail, SendGrid, etc.)

4. **Deploy to Firebase App Hosting**:
   ```bash
   firebase deploy --only apphosting:api
   ```

### Phase 11: Move to Next Story

Once testing is complete, the auth system is ready for production. You can:
- Mark story API-003 as complete
- Create a pull request
- Move to the next feature (Tenant Management, Product Management, etc.)

---

## Troubleshooting

**Issue**: Port 8080 already in use
```bash
# Use a different port
flask run --port=5001

# Or kill the process using port 8080
lsof -ti:8080 | xargs kill -9
```

**Issue**: Firebase permission denied
- Check that service account has Firestore permissions
- Verify Firestore API is enabled in Google Cloud Console

**Issue**: Pydantic not installing
- This guide uses Python 3.12 (required for pydantic 2.10.5)
- Python 3.14 is not yet supported by pydantic-core

---

## Documentation

- **Dev Guide**: `apps/api/docs/dev-guide/01-setup.md`
- **Feature Spec**: `docs/features/01-authentication.md`
- **Story File**: `apps/api/docs/todos/auth-sytem-and-profile-management.md`
- **Shared Types**: `packages/shared-types/`

---

**Setup completed by**: Claude Code
**Implementation status**: Phases 1-9 complete, ready for testing
