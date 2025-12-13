# Development Workflow Guide

Complete guide for the TOKO ANAK BANGSA development workflow using the story-driven approach.

---

## Table of Contents

1. [Story Creation](#story-creation)
2. [Development Process](#development-process)
3. [Story Workflow](#story-workflow)
4. [Git Workflow](#git-workflow)
5. [Deployment Workflow](#deployment-workflow)
6. [Common Commands](#common-commands)

---

## Story Creation

### Using the Story Creation Script

Create new user stories with the interactive script:

```bash
pnpm story:create
```

### Interactive Prompts

The script will ask for:

1. **Story Title**: Clear, concise title (e.g., "Email/Password Authentication")

2. **Project Scope**: Select from:
   - `1) api` - Flask API Backend
   - `2) store-portal` - Store Portal (POS & Store Management)
   - `3) marketplace` - Marketplace (E-commerce)
   - `4) company-profile` - Company Profile (Landing Page)
   - `5) platform-admin` - Platform Admin
   - `6) cross` - Cross-project (multiple apps)

3. **Story Type**: Select from:
   - `1) feature` - New feature
   - `2) bugfix` - Bug fix
   - `3) refactor` - Code refactoring
   - `4) chore` - Maintenance task
   - `5) docs` - Documentation

4. **Category**: Select from predefined categories (see `docs/sprint/categories.yaml`):
   - AUTH, POS, PRODUCT, ORDER, CASHIER, etc.
   - Or create a new category

5. **Assignee**: Team member name (or leave empty for unassigned)

6. **Description**: Brief one-line description of the story

### What the Script Does

After you complete the prompts, the script will:

1. ✅ Generate unique story ID (e.g., `STORE-001`, `API-001`)
2. ✅ Create todo file in appropriate directory (`apps/*/docs/todos/` or `docs/todos/`)
3. ✅ Update sprint status (`docs/sprint/status.yaml`)
4. ✅ Create and checkout git branch (e.g., `feature/store-portal/email-password-authentication`)
5. ✅ Copy `/fill-story` command to clipboard (macOS)

### Example Session

```bash
$ pnpm story:create

================================================
  TOKO ANAK BANGSA Story Creator
================================================

Enter story title:
> Email/Password Authentication

Select project scope:
  1) api              - Flask API Backend
  2) store-portal     - Store Portal (POS & Store Management)
  3) marketplace      - Marketplace (E-commerce)
  4) company-profile  - Company Profile (Landing Page)
  5) platform-admin   - Platform Admin
  6) cross            - Cross-project (multiple apps)

Enter choice (1-6): 2

Select story type:
  1) feature    - New feature
  2) bugfix     - Bug fix
  3) refactor   - Code refactoring
  4) chore      - Maintenance task
  5) docs       - Documentation

Enter choice (1-5): 1

Select feature category:
  1) AUTH        - Authentication & Authorization
  2) POS         - Point of Sale
  3) PRODUCT     - Product Management
  ...

Enter choice (1-XX): 1

Assignee (leave empty for unassigned):
  Available: iqbal, team
> iqbal

Brief description (one line):
> Implement email/password authentication with sign up, login, and password reset

✓ Created todo file: apps/store-portal/docs/todos/email-password-authentication.md
✓ Updated sprint status: docs/sprint/status.yaml
✓ Switched to branch: feature/store-portal/email-password-authentication

================================================
  Story Created Successfully!
================================================

  Story ID:    STORE-001
  Title:       Email/Password Authentication
  Type:        feature
  Project:     store-portal
  Category:    AUTH
  Assignee:    iqbal
  Branch:      feature/store-portal/email-password-authentication
  Todo File:   apps/store-portal/docs/todos/email-password-authentication.md

================================================
  ✓ Ready! Command copied to clipboard
================================================

  >>> Press Cmd+V now to fill the story <<<

  /fill-story apps/store-portal/docs/todos/email-password-authentication.md
```

---

## Development Process

### 1. Fill the Story (Using Claude)

After creating the story, the todo file contains placeholder sections. Use Claude to fill it:

```bash
# The command is already in your clipboard (macOS)
# Just paste it in Claude Code:
/fill-story apps/store-portal/docs/todos/email-password-authentication.md
```

Claude will:
- Read the DEVELOPER_GUIDE.md
- Generate complete user story
- Create detailed acceptance criteria
- Design technical implementation
- Generate implementation checklist
- Add testing requirements

### 2. Review the Story

Open the filled story file and review:
- User story format
- Acceptance criteria
- Technical design
- Implementation tasks
- Dependencies
- Testing strategy

### 3. Start Development

You're already on the story branch, so start coding:

```bash
# Check current branch
git branch

# You should see: feature/store-portal/email-password-authentication

# Start development server
pnpm dev:store-portal

# Or run all apps
pnpm dev
```

### 4. Implement Features

Follow the implementation checklist in the story file:

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3
- ...

Check off tasks as you complete them.

### 5. Testing

Run tests as you develop:

```bash
# Type check
pnpm typecheck

# Lint
pnpm lint

# Build
pnpm build

# Run tests (when available)
pnpm test
```

### 6. Commit Changes

Commit frequently with meaningful messages:

```bash
git add .
git commit -m "feat(store-portal): implement login form component"
```

### 7. Update Story Status

Edit `docs/sprint/status.yaml` to update story status:

```yaml
stories:
  - id: STORE-001
    title: "Email/Password Authentication"
    type: feature
    project: store-portal
    assignee: iqbal
    status: in_progress  # Change from 'backlog' to 'in_progress'
    branch: "feature/store-portal/email-password-authentication"
    docs: "apps/store-portal/docs/todos/email-password-authentication.md"
    category: AUTH
```

---

## Story Workflow

### Story Status Flow

```
backlog → in_progress → review → done
```

1. **backlog**: Story created, not started
2. **in_progress**: Currently being worked on
3. **review**: Code complete, in PR review
4. **done**: Merged to main, deployed

### Story File Location

Stories are created in:

- **App-specific**: `apps/{app-name}/docs/todos/{story-file}.md`
  - e.g., `apps/store-portal/docs/todos/email-password-authentication.md`

- **Cross-project**: `docs/todos/{story-file}.md`
  - For stories affecting multiple apps

### Sprint Tracking

All active stories are tracked in:
```
docs/sprint/status.yaml
```

This file contains:
- Current sprint info
- Team members
- All stories with status
- Branch names
- Assignees

---

## Git Workflow

### Branch Naming Convention

Format: `{type}/{scope}/{story-slug}`

Examples:
- `feature/store-portal/email-password-authentication`
- `bugfix/api/fix-product-query`
- `refactor/marketplace/simplify-checkout`
- `chore/cross/update-dependencies`

### Commit Message Convention

Follow conventional commits:

```
{type}({scope}): {description}

feat(store-portal): add login form component
fix(api): resolve product query timeout
refactor(marketplace): simplify checkout flow
docs(readme): update installation steps
chore(deps): upgrade Next.js to 16.1.0
```

### Pull Request Workflow

1. Push your branch:
   ```bash
   git push origin feature/store-portal/email-password-authentication
   ```

2. Create PR on GitHub

3. Update story status to `review` in `status.yaml`

4. Request review from team

5. Address feedback

6. Merge when approved

7. Update story status to `done`

8. Delete branch

---

## Deployment Workflow

### Development Environment

```bash
# Make sure you're using dev Firebase project
firebase use dev

# Deploy specific app
pnpm deploy:store-portal

# Or deploy all
pnpm deploy:all
```

### Staging Environment

```bash
# Switch to staging
firebase use staging

# Deploy
pnpm deploy:all
```

### Production Environment

```bash
# Switch to production
firebase use prod

# Deploy (careful!)
pnpm deploy:all
```

---

## Common Commands

### Story Management

```bash
# Create new story
pnpm story:create

# View sprint status
cat docs/sprint/status.yaml

# View story categories
cat docs/sprint/categories.yaml
```

### Development

```bash
# Run all apps
pnpm dev

# Run specific app
pnpm dev:store-portal
pnpm dev:marketplace
pnpm dev:company-profile
pnpm dev:platform-admin
pnpm dev:api

# Type check
pnpm typecheck

# Lint
pnpm lint

# Build all
pnpm build

# Build specific app
pnpm build:store-portal
```

### Firebase

```bash
# Switch environment
firebase use dev
firebase use staging
firebase use prod

# Deploy
pnpm deploy:store-portal
pnpm deploy:marketplace
pnpm deploy:company-profile
pnpm deploy:platform-admin
pnpm deploy:api
pnpm deploy:all

# Start emulators
pnpm firebase:emulators
```

### Git

```bash
# Check branch
git branch

# Create branch (done by story script)
git checkout -b feature/store-portal/new-feature

# Commit
git add .
git commit -m "feat(store-portal): add new feature"

# Push
git push origin feature/store-portal/new-feature

# Switch back to main
git checkout main
git pull origin main
```

---

## Quick Reference

### Story Creation Flow

1. `pnpm story:create` → Answer prompts
2. Paste `/fill-story` command in Claude
3. Review generated story
4. Start development (already on branch)
5. Implement following checklist
6. Test and commit
7. Push and create PR
8. Merge and deploy

### Daily Workflow

```bash
# Morning: Pull latest
git checkout main
git pull origin main

# Create story for today's work
pnpm story:create

# Develop
pnpm dev:store-portal

# Test
pnpm typecheck
pnpm lint

# Commit
git add .
git commit -m "feat: description"

# Push
git push origin feature/scope/story-name

# Evening: Create PR
# Open GitHub and create PR
```

---

## Tips & Best Practices

### Story Creation

- ✅ Keep story titles clear and concise
- ✅ Use descriptive branch names
- ✅ Fill out all prompts completely
- ✅ Review generated story before starting
- ❌ Don't skip the description
- ❌ Don't create stories without planning

### Development

- ✅ Work on one story at a time
- ✅ Commit frequently with clear messages
- ✅ Test before committing
- ✅ Keep branches up to date with main
- ❌ Don't commit broken code
- ❌ Don't mix multiple stories in one branch

### Deployment

- ✅ Test in development first
- ✅ Deploy to staging for QA
- ✅ Only deploy to production when approved
- ❌ Don't deploy untested code
- ❌ Don't skip staging environment

---

## Troubleshooting

### Story Creation Issues

**Problem**: Script can't find git repository
- Solution: Make sure you're in the project root directory

**Problem**: Branch already exists
- Solution: The script will checkout the existing branch

**Problem**: Can't copy to clipboard (non-macOS)
- Solution: Manually copy the `/fill-story` command shown

### Git Issues

**Problem**: Changes on wrong branch
- Solution: Stash changes, switch branch, apply stash
  ```bash
  git stash
  git checkout correct-branch
  git stash pop
  ```

**Problem**: Merge conflicts
- Solution: Resolve conflicts manually, then:
  ```bash
  git add .
  git commit
  ```

---

## Getting Help

- Check [DEVELOPER_GUIDE.md](../DEVELOPER_GUIDE.md) for architecture
- Check [README.md](../README.md) for setup
- Check [ENVIRONMENTS.md](../ENVIRONMENTS.md) for deployment
- Check story files for implementation details
- Ask in team chat

---

**Happy coding! 🚀**
