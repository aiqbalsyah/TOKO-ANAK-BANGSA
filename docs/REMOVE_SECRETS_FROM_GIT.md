# Emergency: Remove Secrets from Git History

**⚠️ CRITICAL: If you've pushed `.env` files or secrets to git, follow these steps immediately!**

---

## 🚨 Immediate Actions (Do This First!)

### Step 1: Rotate ALL Compromised Credentials

**Assume all secrets in the pushed file are now public.** Immediately invalidate/rotate:

#### Firebase Credentials
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. **Revoke Service Account Keys:**
   - Project Settings > Service Accounts
   - Delete compromised service account key
   - Generate new private key
   - Update local `.env.local` and production secrets

3. **Regenerate API Keys (if needed):**
   - Project Settings > General
   - Note: Firebase client API keys are public-facing, but still rotate if concerned
   - Update Web App configuration

#### Midtrans Payment Keys
1. Go to [Midtrans Dashboard](https://dashboard.midtrans.com/)
2. Settings > Access Keys
3. Regenerate Server Key and Client Key
4. Update `.env.local` and production environment variables

#### Other Services
- **SendGrid/Email**: Regenerate API keys
- **Google Maps**: Regenerate API key with restrictions
- **WhatsApp Business**: Regenerate access tokens
- **Any other API keys**: Rotate immediately

### Step 2: Notify Your Team

```bash
# Send urgent message to team:
⚠️ SECURITY ALERT: .env file was pushed to git.
All credentials are being rotated.
DO NOT PULL until cleanup is complete.
```

---

## 🔧 Method 1: BFG Repo-Cleaner (Recommended - Fastest)

BFG is faster and easier than git filter-branch.

### Install BFG

```bash
# macOS
brew install bfg

# Or download directly
# https://rtyley.github.io/bfg-repo-cleaner/
```

### Remove .env Files from History

```bash
# 1. Clone a fresh copy (don't use your working repo)
cd /tmp
git clone --mirror https://github.com/your-org/pos_app_v1.git
cd pos_app_v1.git

# 2. Run BFG to remove all .env files
bfg --delete-files .env
bfg --delete-files .env.local
bfg --delete-files .env.staging
bfg --delete-files .env.production
bfg --delete-files serviceAccountKey.json

# 3. Clean up the repository
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 4. Force push (⚠️ DESTRUCTIVE - coordinate with team!)
git push --force

# 5. Clean up
cd ..
rm -rf pos_app_v1.git
```

### Team Members Must Re-clone

After force push, all team members must:

```bash
# DON'T pull - delete local repo and re-clone
cd ~/projects
rm -rf pos_app_v1
git clone https://github.com/your-org/pos_app_v1.git
cd pos_app_v1

# Create new .env.local with rotated credentials
cp .env.example .env.local
# Fill in NEW credentials
```

---

## 🔧 Method 2: git filter-branch (Built-in, Slower)

Use if you can't install BFG.

### Remove Specific Files

```bash
# 1. Backup your repository first!
cd /path/to/pos_app_v1
git clone . ../pos_app_v1-backup

# 2. Remove .env files from all commits
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env .env.local .env.staging .env.production serviceAccountKey.json" \
  --prune-empty --tag-name-filter cat -- --all

# 3. Clean up references
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 4. Force push (⚠️ DESTRUCTIVE - coordinate with team!)
git push --force --all
git push --force --tags
```

---

## 🔧 Method 3: git-filter-repo (Most Powerful)

Modern alternative to filter-branch.

### Install

```bash
# macOS
brew install git-filter-repo

# Or with pip
pip3 install git-filter-repo
```

### Remove Files

```bash
# 1. Clone fresh copy
git clone https://github.com/your-org/pos_app_v1.git pos_app_v1-clean
cd pos_app_v1-clean

# 2. Remove files
git filter-repo --invert-paths \
  --path .env \
  --path .env.local \
  --path .env.staging \
  --path .env.production \
  --path apps/api/serviceAccountKey.json

# 3. Add remote back (filter-repo removes it)
git remote add origin https://github.com/your-org/pos_app_v1.git

# 4. Force push
git push --force --all
git push --force --tags
```

---

## ⚠️ Important Notes

### Before Force Pushing

1. **Coordinate with team:**
   ```bash
   # Announce in team chat:
   ⚠️ About to force push to remove secrets.
   STOP working and DO NOT push/pull for next 10 minutes.
   You will need to re-clone the repository.
   ```

2. **Verify no one is working:**
   - Check if anyone has uncommitted changes
   - Schedule during low-activity time

3. **Backup everything:**
   ```bash
   git clone . ../pos_app_v1-backup-$(date +%Y%m%d)
   ```

### After Force Push

1. **Verify secrets are gone:**
   ```bash
   # Search entire history
   git log --all --full-history -- .env
   # Should return nothing

   # Search for specific strings
   git log --all -p -S "FIREBASE_API_KEY" | grep "FIREBASE_API_KEY"
   # Should return nothing
   ```

2. **Update .gitignore:**
   ```bash
   # Verify .gitignore is correct
   cat .gitignore | grep .env

   # Should see:
   # .env*
   # !.env.example
   ```

3. **Test that .env.local is ignored:**
   ```bash
   cp .env.example .env.local
   # Add fake data to .env.local
   git status
   # .env.local should NOT appear
   ```

---

## 📋 Team Re-clone Instructions

Send this to your team after force push:

```bash
# ⚠️ IMPORTANT: Repository was cleaned. Follow these steps:

# 1. Backup any uncommitted work
cd ~/projects/pos_app_v1
git diff > ~/my-changes.patch  # Save your changes
git stash  # Or stash changes

# 2. Delete local repository
cd ~/projects
rm -rf pos_app_v1

# 3. Fresh clone
git clone https://github.com/your-org/pos_app_v1.git
cd pos_app_v1

# 4. Create new .env.local with NEW credentials
cp .env.example .env.local
# Fill in rotated credentials (get from team lead)

# 5. Restore your work (if you had uncommitted changes)
git apply ~/my-changes.patch  # Or git stash pop

# 6. Install dependencies
pnpm install
cd apps/api && pip install -r requirements.txt
```

---

## 🔒 Prevention for Future

### 1. Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Prevent committing .env files

FILES=$(git diff --cached --name-only | grep -E '\.env$|\.env\.|serviceAccountKey\.json')

if [ -n "$FILES" ]; then
    echo "❌ ERROR: Attempting to commit sensitive files:"
    echo "$FILES"
    echo ""
    echo "These files should never be committed!"
    echo "Add them to .gitignore and use .env.example instead."
    exit 1
fi
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

### 2. GitHub Secret Scanning

Enable in repository settings:
- Settings > Security > Code security and analysis
- Enable "Secret scanning"
- Enable "Push protection"

### 3. Use git-secrets

```bash
# Install
brew install git-secrets

# Setup for repository
cd pos_app_v1
git secrets --install
git secrets --register-aws  # Add AWS patterns

# Add custom patterns
git secrets --add 'FIREBASE_API_KEY.*'
git secrets --add 'MIDTRANS.*KEY.*'
git secrets --add 'serviceAccountKey'

# Scan history
git secrets --scan-history
```

### 4. Team Training

- Review `docs/SECURITY.md` with all developers
- Require reading before first commit
- Periodic security training

---

## 📱 If Repository is Public

### Additional Urgent Steps

1. **Assume breach is public:**
   - Credentials are compromised
   - Search GitHub/web for your repo name + "env"
   - Check if anyone forked the repo

2. **Make repository private temporarily:**
   - Settings > General > Danger Zone
   - Change visibility to Private
   - Clean history
   - Consider keeping private

3. **Notify affected parties:**
   - If contains customer data: GDPR breach notification
   - Document incident for compliance

4. **Review security:**
   - Audit Firebase security rules
   - Check Firestore/Storage access logs
   - Review authentication logs
   - Monitor for unusual activity

---

## ✅ Verification Checklist

After cleanup:

- [ ] All secrets rotated and invalidated
- [ ] Force push completed successfully
- [ ] Team notified and repositories re-cloned
- [ ] Verified secrets not in history: `git log --all -p -S "SECRET_TEXT"`
- [ ] `.gitignore` correctly ignores `.env*` files
- [ ] `.env.example` has only placeholder values
- [ ] Pre-commit hook installed
- [ ] GitHub secret scanning enabled
- [ ] Tested that `.env.local` is ignored
- [ ] All team members using new credentials
- [ ] Production environment variables updated
- [ ] Incident documented for future reference

---

## 🆘 Need Help?

If you're unsure about any step:

1. **Stop and ask for help** - don't make it worse
2. **Consult with senior developers**
3. **Consider professional security audit** if breach is serious
4. **GitHub Support** can help with repository issues

---

## 📚 Resources

- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
- [git-filter-repo](https://github.com/newren/git-filter-repo)
- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [git-secrets](https://github.com/awslabs/git-secrets)

---

**Remember: Prevention is better than cure. Always double-check before committing!**

**Last Updated**: 2024-12-13
