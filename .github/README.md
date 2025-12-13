# GitHub Configuration

This directory contains GitHub-specific configuration files for the TOKO ANAK BANGSA project.

## Files Overview

### GitHub Copilot

**`copilot-instructions.md`**
- Workspace-level instructions for GitHub Copilot
- Contains project architecture, coding patterns, and conventions
- Includes commit message format and examples
- Automatically used by Copilot when generating code suggestions

### CI/CD Workflows

**`workflows/ci.yml`**
- Continuous Integration pipeline
- Runs on push to `main` and `develop` branches
- Jobs:
  - TypeScript type checking
  - ESLint linting
  - Build all apps and packages
  - Python tests and linting (Black, Flake8, pytest)
  - Security audit
  - Check for TODO/FIXME comments

### Issue Templates

**`ISSUE_TEMPLATE/bug_report.md`**
- Template for reporting bugs
- Includes sections for:
  - Bug description and steps to reproduce
  - Environment details (browser, OS, device)
  - Console output and screenshots
  - Priority and affected applications

**`ISSUE_TEMPLATE/feature_request.md`**
- Template for suggesting new features
- Includes sections for:
  - User story and problem statement
  - Proposed solution and alternatives
  - Acceptance criteria and use cases
  - Technical considerations and scope estimation

**`ISSUE_TEMPLATE/config.yml`**
- Configuration for issue templates
- Disables blank issues
- Provides links to documentation and discussions

### Pull Request Template

**`PULL_REQUEST_TEMPLATE.md`**
- Standard template for all pull requests
- Includes sections for:
  - Description and related story/issue
  - Type of change and affected applications
  - Testing checklist
  - Code quality and security checklist
  - Deployment notes and rollback plan

## Using GitHub Copilot

GitHub Copilot will automatically read `copilot-instructions.md` when:
- Writing new code
- Suggesting completions
- Generating commit messages
- Answering questions in Copilot Chat

### Commit Message Suggestions

When writing commit messages, Copilot will suggest messages following this format:

```
<type>(<scope>): <description>
```

**Examples:**
```bash
feat(api): add product search endpoint
fix(store-portal): resolve cart total calculation
refactor(marketplace): simplify checkout flow
docs(readme): update installation steps
```

### Code Generation

Copilot will follow these patterns:
- Use Server Components by default in Next.js
- Include next-intl for translations
- Implement tenant isolation in all database queries
- Use Zod schemas from `@toko/shared-types`
- Follow error handling patterns
- Use shadcn/ui components from `@toko/ui-web`

## CI/CD Pipeline

### Running Locally

Before pushing, ensure all checks pass:

```bash
# Type check
pnpm typecheck

# Lint
pnpm lint

# Build
pnpm build

# Python tests (in apps/api)
cd apps/api
black . --check
flake8 .
pytest
```

### Pipeline Triggers

The CI pipeline runs on:
- Push to `main` branch (deploys to production)
- Push to `develop` branch (deploys to staging)
- Pull requests to `main` or `develop`

### Required Checks

All checks must pass before merging:
- ✅ TypeScript type checking
- ✅ ESLint (no errors)
- ✅ Build succeeds for all apps
- ✅ Python formatting (Black)
- ✅ Python linting (Flake8)
- ✅ All tests pass

## Creating Issues

### Bug Report

1. Click "New Issue"
2. Select "Bug Report" template
3. Fill in all required sections:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details
   - Console output/screenshots
4. Add appropriate labels: `bug`, `priority:high`, etc.

### Feature Request

1. Click "New Issue"
2. Select "Feature Request" template
3. Fill in all sections:
   - User story
   - Problem statement
   - Proposed solution
   - Acceptance criteria
   - Technical considerations
4. Add labels: `enhancement`, `scope:medium`, etc.

## Creating Pull Requests

1. Create a feature branch following naming convention:
   ```bash
   git checkout -b feature/store-portal/product-management
   ```

2. Make your changes following the patterns in:
   - `apps/*/CLAUDE.md` - AI quick reference
   - `apps/*/docs/dev-guide/01-setup.md` - Complete setup guide

3. Update story file in `docs/todos/` with progress

4. Commit with conventional commit messages:
   ```bash
   git commit -m "feat(store-portal): add product list page"
   ```

5. Push and create PR:
   ```bash
   git push origin feature/store-portal/product-management
   ```

6. Fill in the PR template:
   - Link to story/issue
   - Describe changes made
   - Add screenshots if UI changes
   - Complete all checklists

7. Request review from team members

## GitHub Actions Secrets

Required secrets for CI/CD:

- `NEXT_PUBLIC_FIREBASE_API_KEY` - Firebase API key for builds
- Other Firebase config variables as needed

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Last Updated**: 2024-12-13
