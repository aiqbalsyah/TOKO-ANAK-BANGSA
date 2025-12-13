# Security Guidelines

**TOKO ANAK BANGSA** - Security Best Practices

This document outlines security practices for protecting sensitive data in this project.

---

## Environment Variables Security

### ✅ What's Protected

All environment files with real values are **automatically ignored** by git:

```
.env*                  # All .env files are ignored
!.env.example          # EXCEPT .env.example (template only)
```

### ⚠️ NEVER Commit These Files

**Forbidden files** (already in `.gitignore`):
- `.env.local` - Local development environment
- `.env.development` - Development environment
- `.env.staging` - Staging environment
- `.env.production` - Production environment
- Any file matching `.env*` pattern

### ✅ Safe to Commit

**Allowed files**:
- `.env.example` - Template with placeholder values only

---

## Setting Up Environment Variables

### For Local Development

1. **Copy the template:**
   ```bash
   cp .env.example .env.local
   ```

2. **Get Firebase credentials:**
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Select your project
   - Go to Project Settings > General > Your apps
   - Copy the configuration values

3. **Fill in `.env.local` with real values:**
   ```env
   NEXT_PUBLIC_FIREBASE_API_KEY=AIzaSy... (your actual key)
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-actual-project-id
   # ... etc
   ```

4. **NEVER commit `.env.local`:**
   ```bash
   # Verify it's ignored
   git status
   # .env.local should NOT appear in the list
   ```

### For Firebase Admin SDK (Backend)

The Flask API needs Firebase Admin SDK credentials.

**Option 1: Service Account JSON File (Local Development)**

1. Download service account key:
   - Firebase Console > Project Settings > Service Accounts
   - Click "Generate new private key"
   - Save as `apps/api/serviceAccountKey.json`

2. This file is automatically ignored by git:
   ```bash
   # apps/api/.gitignore includes:
   serviceAccountKey.json
   *-firebase-adminsdk-*.json
   ```

**Option 2: Environment Variable (Production)**

Set the entire JSON as an environment variable:
```env
FIREBASE_SERVICE_ACCOUNT_KEY='{"type":"service_account",...}'
```

---

## Production Deployment

### GitHub Secrets (for CI/CD)

Store sensitive values in GitHub repository secrets:

1. Go to: Repository > Settings > Secrets and variables > Actions
2. Add secrets:
   - `NEXT_PUBLIC_FIREBASE_API_KEY`
   - `FIREBASE_SERVICE_ACCOUNT_KEY`
   - `MIDTRANS_SERVER_KEY`
   - etc.

3. Reference in GitHub Actions:
   ```yaml
   env:
     NEXT_PUBLIC_FIREBASE_API_KEY: ${{ secrets.NEXT_PUBLIC_FIREBASE_API_KEY }}
   ```

### Firebase App Hosting

Set environment variables in Firebase:

1. Go to Firebase Console > App Hosting
2. Select your backend
3. Add environment variables:
   - Variables starting with `NEXT_PUBLIC_` will be available in the browser
   - Other variables are server-side only

---

## Sensitive Files Checklist

### ⛔ NEVER Commit

- [ ] `.env.local` (local development)
- [ ] `.env.staging` (staging environment)
- [ ] `.env.production` (production environment)
- [ ] `serviceAccountKey.json` (Firebase Admin SDK)
- [ ] `*-firebase-adminsdk-*.json` (Firebase service accounts)
- [ ] `.env` (generic environment file)
- [ ] Any file with API keys, passwords, or tokens

### ✅ Safe to Commit

- [x] `.env.example` (template with placeholders only)
- [x] `.gitignore` (protects sensitive files)
- [x] `apps/api/.gitignore` (protects Python/Flask sensitive files)
- [x] Documentation files
- [x] Configuration files without secrets

---

## Git Security Checks

### Before Every Commit

1. **Check what you're committing:**
   ```bash
   git status
   git diff
   ```

2. **Verify no secrets are staged:**
   ```bash
   git diff --cached
   ```

3. **Search for potential secrets:**
   ```bash
   # Check for API keys
   git diff --cached | grep -i "api.key\|secret\|password\|token"
   ```

### If You Accidentally Committed Secrets

**⚠️ STOP! Do not push to remote!**

1. **Remove the file from git (keep local copy):**
   ```bash
   git rm --cached .env.production
   ```

2. **Amend the commit:**
   ```bash
   git commit --amend
   ```

3. **If already pushed to remote:**
   - Immediately rotate/invalidate the exposed credentials
   - Use `git filter-branch` or BFG Repo-Cleaner to remove from history
   - Force push (DANGEROUS - coordinate with team first)
   - Consider the credentials compromised permanently

---

## VSCode & GitHub Configuration

### VSCode Settings (`.vscode/`)

**Safe to commit:**
- `settings.json` - Workspace settings (no secrets)
- `extensions.json` - Recommended extensions
- `launch.json` - Debug configurations
- `tasks.json` - Build tasks
- `snippets.code-snippets` - Code snippets

**What's protected:**
- `.vscode/settings.local.json` - Personal overrides (if created)

### GitHub Configuration (`.github/`)

**Safe to commit:**
- `workflows/` - CI/CD workflows
- `ISSUE_TEMPLATE/` - Issue templates
- `PULL_REQUEST_TEMPLATE.md` - PR template
- `copilot-instructions.md` - Copilot guidance

**What requires secrets:**
- Secrets referenced in workflows use GitHub Secrets (not in code)

---

## Firebase Security Rules

Security is enforced at the **Firebase level**, not just in code:

### Firestore Security Rules

Located in: `firebase/firestore.rules`

```javascript
// Example: Tenant isolation
match /products/{productId} {
  allow read, write: if request.auth != null
    && request.resource.data.tenant_id == request.auth.token.tenant_id;
}
```

### Storage Security Rules

Located in: `firebase/storage.rules`

```javascript
// Example: Authenticated uploads only
match /uploads/{userId}/{fileName} {
  allow write: if request.auth != null && request.auth.uid == userId;
}
```

**Deploy security rules:**
```bash
firebase deploy --only firestore:rules
firebase deploy --only storage
```

---

## Multi-tenant Security

### Critical: Tenant Isolation

**Every database query MUST filter by `tenant_id`:**

**✅ Correct:**
```typescript
const q = query(
  collection(db, 'products'),
  where('tenant_id', '==', tenantId)  // ✅ Tenant isolation
);
```

**❌ Wrong:**
```typescript
const q = query(collection(db, 'products'));  // ❌ NO TENANT FILTER!
```

### Backend Middleware

The Flask API should have middleware to inject `tenant_id`:

```python
@app.before_request
def inject_tenant_id():
    # Extract tenant_id from JWT token
    request.tenant_id = get_tenant_from_token()
```

---

## API Security

### Authentication

- All API routes (except public endpoints) require Firebase Auth token
- Token verification happens on every request
- Tokens expire after 1 hour (configurable)

### CORS Configuration

```python
# apps/api/main.py
CORS(app, origins=[
    'http://localhost:3000',  # Store Portal
    'http://localhost:3001',  # Marketplace
    'https://your-production-domain.com'
])
```

### Rate Limiting

Consider implementing rate limiting for:
- Login endpoints (prevent brute force)
- Public API endpoints (prevent abuse)
- Payment endpoints (prevent fraud)

---

## Dependencies Security

### Regular Updates

```bash
# Update JavaScript dependencies
pnpm update --latest

# Check for vulnerabilities
pnpm audit

# Update Python dependencies
pip list --outdated
pip install --upgrade package-name
```

### CI/CD Security Checks

The GitHub Actions workflow (`.github/workflows/ci.yml`) includes:
- `pnpm audit` - Check for vulnerable npm packages
- Security scanning (add tools like Snyk or Dependabot)

---

## Incident Response

### If Credentials Are Compromised

1. **Immediately rotate/invalidate:**
   - Firebase API keys (regenerate in console)
   - Service account keys (revoke and generate new)
   - Third-party API keys (Midtrans, SendGrid, etc.)

2. **Review access logs:**
   - Firebase Console > Authentication > Users
   - Firebase Console > Firestore > Usage
   - Check for unauthorized access

3. **Notify affected parties:**
   - If user data accessed, follow GDPR/data breach protocols
   - Document incident for compliance

4. **Update security measures:**
   - Review and update security rules
   - Audit all environment configurations
   - Add additional monitoring

---

## Security Checklist

### Development

- [ ] Using `.env.local` for local development
- [ ] Never committing environment files
- [ ] All database queries include tenant isolation
- [ ] Using HTTPS for all external API calls
- [ ] Validating all user input (Zod schemas)

### Code Review

- [ ] No hardcoded secrets in code
- [ ] Proper error handling (no sensitive info in errors)
- [ ] Authentication required on protected routes
- [ ] Tenant isolation verified
- [ ] Input validation implemented

### Deployment

- [ ] Environment variables set in Firebase App Hosting
- [ ] GitHub Secrets configured for CI/CD
- [ ] Firebase Security Rules deployed
- [ ] CORS configured correctly
- [ ] SSL/TLS certificates valid

### Monitoring

- [ ] Error tracking enabled (Sentry or similar)
- [ ] Firebase monitoring enabled
- [ ] Alert on suspicious activity
- [ ] Regular security audits

---

## Additional Resources

- [Firebase Security Best Practices](https://firebase.google.com/docs/rules)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Next.js Environment Variables](https://nextjs.org/docs/basic-features/environment-variables)

---

**Last Updated**: 2024-12-13

**Maintainers**: Review this document quarterly and update as needed.
