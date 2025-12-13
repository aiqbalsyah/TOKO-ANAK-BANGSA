# Sprint 1 - Core POS Features

**Status**: 📋 Planning
**Planned Start**: TBD
**Planned End**: TBD
**Prerequisites**: Sprint 0 completed ✅

---

## Sprint Goal

Build the foundational POS (Point of Sale) features for the Store Portal, including authentication, basic product management, simple checkout flow, and essential dashboard.

---

## Target Deliverables

### 1. Authentication System 🔐

#### Stories to Create
- **STORE-001**: Email/Password Authentication
  - Sign up flow
  - Login flow
  - Password reset
  - Email verification

- **STORE-002**: Google OAuth Integration
  - Google sign-in button
  - OAuth flow
  - Account linking

- **STORE-003**: Role-Based Access Control (RBAC)
  - Owner role setup
  - Admin role
  - Staff role
  - Cashier role
  - Permission middleware

### 2. Product Management 📦

#### Stories to Create
- **STORE-004**: Product Listing Page
  - Display all products
  - Search/filter functionality
  - Pagination
  - Product grid/list view

- **STORE-005**: Add New Product
  - Product form
  - Category selection
  - Pricing setup
  - SKU generation

- **STORE-006**: Product Image Upload
  - Firebase Storage integration
  - Image optimization
  - Multiple image support
  - Thumbnail generation

- **STORE-007**: Product Variants
  - Size/color variants
  - Variant pricing
  - Variant inventory tracking

- **STORE-008**: Inventory Management
  - Stock level tracking
  - Low stock alerts
  - Inventory adjustments
  - Stock history

### 3. Point of Sale (POS) 💰

#### Stories to Create
- **STORE-009**: POS Checkout Interface
  - Product search/scan
  - Cart management
  - Quantity adjustment
  - Total calculation

- **STORE-010**: Cash Payment Processing
  - Cash amount input
  - Change calculation
  - Transaction recording
  - Receipt generation

- **STORE-011**: Order Management
  - Order list view
  - Order details
  - Order status tracking
  - Order history

### 4. Dashboard & Reports 📊

#### Stories to Create
- **STORE-012**: Dashboard Overview
  - Today's sales summary
  - Total transactions count
  - Top products
  - Quick stats widgets

- **STORE-013**: Sales Report
  - Daily sales chart
  - Sales by category
  - Sales by time period
  - Export to CSV

### 5. Customer Management 👥

#### Stories to Create
- **STORE-014**: Customer Database
  - Add customer
  - Customer list
  - Customer profile
  - Purchase history

- **STORE-015**: Customer Lookup in POS
  - Quick search
  - Link transaction to customer
  - Customer loyalty tracking

### 6. Infrastructure & DevOps 🛠️

#### Stories to Create
- **INFRA-001**: CI/CD Pipeline Setup
  - GitHub Actions workflow
  - Automated testing
  - Auto-deploy to staging
  - Manual deploy to production

- **INFRA-002**: Firebase Emulators Setup
  - Emulator configuration
  - Local development workflow
  - Test data seeding

- **INFRA-003**: Testing Framework
  - Unit test setup (Vitest)
  - Component testing (React Testing Library)
  - E2E tests (Playwright)

---

## Technical Requirements

### Database Schema (Firestore)

#### Collections to Create

1. **tenants** (stores)
   ```typescript
   {
     id: string;
     name: string;
     slug: string;
     ownerId: string;
     settings: TenantSettings;
     status: 'active' | 'suspended';
     createdAt: Timestamp;
   }
   ```

2. **products**
   ```typescript
   {
     id: string;
     tenantId: string;
     name: string;
     sku: string;
     price: number;
     category: string;
     images: string[];
     stock: number;
     variants?: ProductVariant[];
   }
   ```

3. **orders**
   ```typescript
   {
     id: string;
     tenantId: string;
     orderNumber: string;
     items: OrderItem[];
     total: number;
     paymentMethod: 'cash' | 'card';
     status: 'pending' | 'completed';
     createdAt: Timestamp;
   }
   ```

4. **customers**
   ```typescript
   {
     id: string;
     tenantId: string;
     name: string;
     phone: string;
     email?: string;
     totalOrders: number;
     totalSpent: number;
   }
   ```

### API Endpoints (Flask)

#### To Implement

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/products` - List products
- `POST /api/products` - Create product
- `PUT /api/products/:id` - Update product
- `POST /api/orders` - Create order
- `GET /api/reports/sales` - Sales report
- `POST /api/upload/image` - Upload product image

### UI Components Needed

#### shadcn/ui Components to Add

- DataTable (for product/order lists)
- Form components (Select, Textarea, etc.)
- Dialog/Modal
- Tabs
- Badge
- Avatar
- Dropdown Menu
- Command (for search)
- Calendar/DatePicker (for reports)

---

## Success Criteria

### Minimum Viable Product (MVP)

By end of Sprint 1, a store owner should be able to:

1. ✅ Sign up and create their store
2. ✅ Log in with email/password or Google
3. ✅ Add products with images and pricing
4. ✅ Track product inventory
5. ✅ Process a cash sale through POS
6. ✅ View daily sales summary
7. ✅ Add customers to database
8. ✅ Generate and print receipts

### Performance Targets

- Page load time: <2 seconds
- Search results: <500ms
- Checkout flow: <5 clicks
- Build time: <1 minute

### Quality Targets

- TypeScript strict mode: 100%
- Test coverage: >70%
- ESLint errors: 0
- Accessibility score: >90

---

## Story Creation Workflow

To create stories for this sprint:

```bash
# Run the story creation script
pnpm story:create

# Follow the prompts:
# 1. Enter story title
# 2. Select scope (store-portal, api, or cross)
# 3. Select type (feature, bugfix, etc.)
# 4. Select category (AUTH, POS, PRODUCTS, etc.)
# 5. Assign to team member
# 6. Add brief description

# The script will:
# - Generate story ID (e.g., STORE-001)
# - Create todo file in docs/todos/
# - Update docs/sprint/status.yaml
# - Create and checkout git branch
# - Copy /fill-story command to clipboard
```

### Example Story Creation

```bash
$ pnpm story:create

Story title: Email/Password Authentication
Select scope: 2 (store-portal)
Select type: 1 (feature)
Select category: 1 (AUTH)
Assignee: iqbal
Description: Implement email/password authentication with sign up, login, and password reset

✓ Created story: STORE-001
✓ Branch: feature/store-portal/email-password-authentication
✓ Run: /fill-story docs/todos/email-password-authentication.md
```

---

## Dependencies & Risks

### Dependencies

- ✅ Sprint 0 infrastructure completed
- ⏳ Firebase projects created manually
- ⏳ Firebase Authentication enabled
- ⏳ Firebase Storage enabled
- ⏳ Domain configured (optional)

### Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Firebase quota limits | High | Monitor usage, upgrade plan if needed |
| Image upload performance | Medium | Implement compression, lazy loading |
| Complex variant logic | Medium | Start simple, iterate based on feedback |
| Learning curve (Next.js 16) | Low | Documentation available, team training |

---

## Estimation

### Story Points Breakdown

- Authentication: 8 points
- Product Management: 13 points
- POS Checkout: 8 points
- Dashboard: 5 points
- Customer Management: 5 points
- Infrastructure: 8 points

**Total**: ~47 story points

### Time Estimate

- Assuming 1 developer
- Estimated: 2-3 weeks
- Buffer: +1 week for testing/refinement

---

## Acceptance Criteria

### Sprint Complete When:

1. All MVP features working in development
2. Deployed to staging environment
3. QA testing completed
4. Documentation updated
5. Demo prepared for stakeholders

---

## Next Steps

1. **Review this plan** with stakeholders
2. **Create stories** using `pnpm story:create`
3. **Set up Firebase projects** manually (if not done)
4. **Enable Firebase services** (Auth, Storage)
5. **Start Sprint 1** development

---

## Notes

- Keep stories small and focused (1-3 days max)
- Use feature flags for work-in-progress features
- Deploy to staging frequently
- Get user feedback early and often

---

*Sprint 1 Planning created on 2024-12-13*
*Status: Awaiting approval to begin*
