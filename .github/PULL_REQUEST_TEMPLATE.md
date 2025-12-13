## Description

<!-- Provide a brief description of the changes in this PR -->

## Related Story/Issue

<!-- Link to the story file or issue -->
- Story: `docs/todos/[story-file].md` or Issue #XXX
- Fixes #XXX (if applicable)

## Type of Change

<!-- Mark the relevant option with an 'x' -->

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update
- [ ] 🔧 Refactoring (no functional changes)
- [ ] 🎨 UI/UX improvements
- [ ] ⚡ Performance improvement
- [ ] 🧪 Test coverage improvement

## Affected Applications

<!-- Mark all that apply -->

- [ ] `apps/api` - Flask API
- [ ] `apps/store-portal` - Store Portal
- [ ] `apps/marketplace` - Marketplace
- [ ] `apps/company-profile` - Company Profile
- [ ] `apps/platform-admin` - Platform Admin
- [ ] `packages/firebase-client` - Firebase SDK wrapper
- [ ] `packages/shared-types` - Types & schemas
- [ ] `packages/ui-web` - UI components
- [ ] `docs/` - Documentation only

## Changes Made

<!-- Provide a detailed list of changes -->

### Features Added
-

### Bugs Fixed
-

### Technical Changes
-

### Database/Schema Changes
- [ ] Firestore collections modified
- [ ] Security rules updated
- [ ] Migrations required

## Screenshots/Videos

<!-- If applicable, add screenshots or videos demonstrating the changes -->

| Before | After |
|--------|-------|
|        |       |

## Testing

<!-- Describe the tests you ran and how to reproduce -->

### Manual Testing Steps

1.
2.
3.

### Automated Tests

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] All tests passing locally

### Test Coverage

<!-- Mark what you tested -->

- [ ] Tested on Desktop (Chrome, Firefox, Safari)
- [ ] Tested on Mobile (iOS, Android)
- [ ] Tested with Indonesian (id) locale
- [ ] Tested with English (en) locale
- [ ] Tested multi-tenant isolation
- [ ] Tested role-based access control

## Checklist

<!-- Ensure all items are checked before requesting review -->

### Code Quality

- [ ] Code follows project conventions (see `apps/*/CLAUDE.md`)
- [ ] TypeScript types are properly defined
- [ ] Python code follows PEP 8 style guide
- [ ] No console.log() or debugging code left
- [ ] Error handling is implemented
- [ ] Loading states are handled

### Documentation

- [ ] Updated relevant documentation in `docs/`
- [ ] Updated README.md if needed
- [ ] Updated CLAUDE.md if patterns changed
- [ ] Added comments for complex logic
- [ ] Updated story file with progress

### Security & Performance

- [ ] Tenant isolation verified (all queries filter by tenant_id)
- [ ] No sensitive data exposed in client-side code
- [ ] Environment variables used correctly
- [ ] Images optimized
- [ ] No unnecessary re-renders
- [ ] Database queries optimized

### Internationalization

- [ ] All user-facing text uses next-intl translations
- [ ] Translations added to `messages/id.json` and `messages/en.json`
- [ ] Date/currency formatting uses Indonesian locale

### Build & Deploy

- [ ] `pnpm typecheck` passes
- [ ] `pnpm lint` passes with no warnings
- [ ] `pnpm build` succeeds
- [ ] No breaking changes to shared packages

## Deployment Notes

<!-- Any special instructions for deployment? -->

- [ ] Database migrations required
- [ ] Environment variables need updating
- [ ] Firebase security rules need deployment
- [ ] Third-party service configuration needed

### Rollback Plan

<!-- How to rollback if something goes wrong? -->



## Additional Context

<!-- Add any other context about the PR here -->



---

## Reviewer Checklist

<!-- For reviewers -->

- [ ] Code follows project patterns and best practices
- [ ] Changes are well-tested
- [ ] Documentation is adequate
- [ ] No security vulnerabilities introduced
- [ ] Performance impact is acceptable
- [ ] Multi-tenant isolation verified
