# Sprint Management

Coordinate work between developers using the sprint status tracker.

## Quick Start

### Create a New Story

Use the interactive story creator (works on Windows, macOS, Linux):

```bash
pnpm story:create
```

This will:
1. Prompt for story details (title, scope, type, category, assignee)
2. Generate a unique story ID
3. Create a todo file in the correct project folder
4. Update `docs/sprint/status.yaml`
5. Create and switch to a new git branch

### 1. Check Available Stories

```bash
cat docs/sprint/status.yaml
```

Look for stories with `status: backlog` and `assignee: null`.

### 2. Claim a Story

Edit `docs/sprint/status.yaml`:

```yaml
- id: STORY-001
  title: "User authentication flow"
  assignee: brandon      # Your id: brandon, iqbal, or tegar
  status: in_progress    # Change from backlog
  branch: feature/STORY-001-auth-flow
  started_at: "2024-12-02"
```

Commit and push to notify the team:

```bash
git add docs/sprint/status.yaml
git commit -m "claim: STORY-001 - User authentication flow"
git push
```

### 3. Create Feature Branch

```bash
git checkout -b feature/STORY-001-auth-flow
```

### 4. Start Development

```bash
claude
/bmad:bmm:workflows:dev-story
```

### 5. Update Status When Done

```yaml
- id: STORY-001
  title: "User authentication flow"
  assignee: your_id
  status: done           # Change from in_progress
  branch: feature/STORY-001-auth-flow
  started_at: "2024-12-02"
  completed_at: "2024-12-03"
```

## Workflow

```
┌─────────┐    ┌─────────────┐    ┌────────┐    ┌──────┐
│ backlog │ -> │ in_progress │ -> │ review │ -> │ done │
└─────────┘    └─────────────┘    └────────┘    └──────┘
```

## Rules

1. **Pull before claiming** - Always `git pull` before claiming a story
2. **One story at a time** - Don't claim multiple stories
3. **Update status** - Keep status.yaml current
4. **Use branches** - One branch per story
5. **Communicate** - If blocked, update status and notify team
6. **Docs in project** - Create docs in related project folder

## Documentation Location

### Cross-Project Features
Features spanning multiple projects (e.g., "Product management across store and marketplace"):

```
docs/todos/product-sync.md                          # Main feature doc
apps/api/docs/todos/product-sync-api.md             # API implementation
apps/store-portal/docs/todos/product-sync-admin.md  # Store Portal implementation
apps/marketplace/docs/todos/product-sync-display.md # Marketplace implementation
```

### Project-Specific Features
Features for a single project:

```
apps/api/docs/todos/auth-api.md
apps/store-portal/docs/todos/pos-interface.md
apps/marketplace/docs/todos/checkout-flow.md
apps/company-profile/docs/todos/contact-form.md
apps/platform-admin/docs/todos/tenant-management.md
```

### Rule
- **Cross-project** → `docs/todos/` + each app's `docs/todos/`
- **Single project** → only that app's `docs/todos/`

## Todo Format

Always use comprehensive checklist format. Mark each step complete immediately when done.

### Template

```markdown
# Feature: [Feature Name]

## Overview
Clear description of what this feature does and why it's needed.

## User Story
As a [user type], I want to [action] so that [benefit].

## Acceptance Criteria
- [ ] Criteria 1
- [ ] Criteria 2
- [ ] Criteria 3

## Technical Design

### API Changes
- Endpoint: `POST /api/v1/endpoint`
- Request/Response format
- Error codes to handle

### Database Changes
- Collections affected
- New fields or indexes

### UI/UX Changes
- Screens affected
- New components needed

## Implementation Checklist

### API (apps/api)
- [ ] Create route in `routes/`
- [ ] Add Pydantic models in `models/`
- [ ] Implement business logic in `services/`
- [ ] Add middleware for auth/tenant isolation
- [ ] Update Firestore operations
- [ ] Add error handling
- [ ] Write tests

### Frontend (apps/store-portal, marketplace, etc.)
- [ ] Create page in `app/[locale]/(dashboard)/`
- [ ] Build components in `components/`
- [ ] Create custom hooks in `hooks/`
- [ ] Add types from `@toko/shared-types`
- [ ] Use UI components from `@toko/ui-web`
- [ ] Implement form validation with Zod
- [ ] Add translations in `messages/id.json` and `messages/en.json`
- [ ] Test on multiple screen sizes

## Dependencies
- List any blockers or dependencies on other features

## Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing completed

## Notes
Additional context, edge cases, or considerations.

## References
- Related docs or links
- Design files
- API documentation
```

### Example

```markdown
# Feature: Artist Track Orders

## Overview
Allow artists to view and manage all orders for their products. Artists need visibility into order status, customer details, and fulfillment tracking to manage their merchandise business effectively.

## User Story
As an artist, I want to view all orders for my products so that I can track sales and manage fulfillment.

## Acceptance Criteria
- [ ] Artist can view list of all orders
- [ ] Orders show status (pending, shipped, delivered)
- [ ] Artist can filter by date range and status
- [ ] Artist can view order details
- [ ] Artist can mark orders as shipped

## Technical Design

### API Changes
- `GET /api/v1/artist/orders` - List orders with pagination
- `GET /api/v1/artist/orders/:id` - Order details
- `PATCH /api/v1/artist/orders/:id/status` - Update status

### Database Changes
- Query `orders` collection by `artist_id`
- Add index on `artist_id + created_at`

### UI/UX Changes
- New "Orders" tab in artist dashboard
- Order list with filters
- Order detail modal

## Implementation Checklist

### API (projects/api)
- [x] Create `GetArtistOrdersUseCase`
- [x] Create `GetOrderDetailUseCase`
- [x] Create `UpdateOrderStatusUseCase`
- [x] Add routes in `orders.routes.ts`
- [x] Add validation schemas
- [ ] Write unit tests

### Mobile (projects/mobile)
- [x] Create `orders.service.ts`
- [x] Add order types
- [ ] Create orders list screen
- [ ] Create order detail screen
- [ ] Add order filters component
- [ ] Add translations

## Dependencies
- Requires shipping integration (completed)

## Testing
- [x] API endpoints tested via Postman
- [ ] Mobile UI tested on iOS
- [ ] Mobile UI tested on Android

## Notes
- Default to last 30 days
- Max 100 orders per page
- Cache order counts for dashboard

## References
- [Orders API Doc](../api/orders.md)
- [Figma Design](link)
```

### Rules

1. **Mark immediately** - Check off `[x]` each step as soon as it's done
2. **Don't batch** - Never wait until all steps are complete to update
3. **Update often** - Commit todo updates with your code changes
4. **Be specific** - Each step should be a single actionable task
5. **Follow dev-guide** - Use patterns from each project's CLAUDE.md
6. **Clear descriptions** - Anyone should understand what to do

## Branch Naming

Format: `<type>/<project>/<feature>`

### Types
- `feature/` - New features
- `fix/` - Bug fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation only

### Projects
- `api` - Backend API (Flask)
- `store-portal` - Store Portal (POS & Store Management)
- `marketplace` - Marketplace (E-commerce)
- `company-profile` - Company Profile (Landing Page)
- `platform-admin` - Platform Admin
- `cross` - Multiple apps

### Examples

```bash
# Feature branches
git checkout -b feature/api/auth-endpoints
git checkout -b feature/store-portal/pos-interface
git checkout -b feature/marketplace/checkout-flow
git checkout -b feature/company-profile/contact-form
git checkout -b feature/platform-admin/tenant-management

# Bug fix branches
git checkout -b fix/api/auth-token-refresh
git checkout -b fix/store-portal/product-form-validation

# Refactor branches
git checkout -b refactor/api/error-handling
git checkout -b refactor/store-portal/component-structure
```

## Commit Messages

Format: `<type>(<scope>): <description>`

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code change (no new feature or fix) |
| `docs` | Documentation only |
| `style` | Formatting, missing semicolons, etc. |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks, dependencies |

### Scopes

| Scope | Description |
|-------|-------------|
| `api` | Backend API changes |
| `store-portal` | Store Portal changes |
| `marketplace` | Marketplace changes |
| `company-profile` | Company Profile changes |
| `platform-admin` | Platform Admin changes |
| `auth` | Authentication related |
| `products` | Product management |
| `orders` | Order management |
| `payments` | Payment integration |

### Examples

```bash
# Features
git commit -m "feat(api): add product management endpoints"
git commit -m "feat(store-portal): implement POS interface"
git commit -m "feat(marketplace): add shopping cart"

# Bug fixes
git commit -m "fix(api): resolve token refresh issue"
git commit -m "fix(store-portal): product form validation error"

# Refactoring
git commit -m "refactor(api): improve error handling"
git commit -m "refactor(marketplace): simplify cart state"

# Other
git commit -m "docs(api): update product endpoints"
git commit -m "test(api): add auth unit tests"
git commit -m "chore: update dependencies"
```

### Tips

- Keep subject line under 50 characters
- Use imperative mood ("add" not "added")
- No period at the end
- Reference issue/story if applicable: `feat(api): add streaming #STORY-001`

## Daily Sync

Before starting work each day:

```bash
git pull
cat docs/sprint/status.yaml | grep -A5 "in_progress"
```

This shows what everyone is working on.
