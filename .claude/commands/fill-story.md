# Fill Story Command - TOKO ANAK BANGSA

Fill in a story todo file with detailed content based on the overview/brief description and feature documentation.

## Instructions

1. **Read the todo file** at: $ARGUMENTS
2. **Extract story details** from the file header (ID, title, overview)
3. **Determine project scope** from the file path:
   - `apps/api/docs/todos/` → Flask API Backend
   - `apps/store-portal/docs/todos/` → Store Portal (Next.js)
   - `apps/marketplace/docs/todos/` → Marketplace (Next.js)
   - `apps/company-profile/docs/todos/` → Company Profile (Next.js)
   - `apps/platform-admin/docs/todos/` → Platform Admin (Next.js)
   - `docs/todos/` → Cross-project scope

4. **Read relevant documentation**:

   **Feature Documentation** (ALWAYS READ - Primary Source):
   - `docs/features/01-authentication.md` - User authentication & session management
   - `docs/features/02-tenant-management.md` - Multi-tenant isolation
   - `docs/features/03-product-management.md` - Product CRUD, variants, pricing
   - `docs/features/04-inventory-management.md` - Stock tracking, adjustments
   - `docs/features/05-pos-cashier.md` - Point of Sale operations
   - `docs/features/06-order-management.md` - Order processing & fulfillment
   - `docs/features/07-customer-management.md` - Customer database, tiers, credit
   - `docs/features/08-supplier-purchasing.md` - Supplier management & procurement
   - `docs/features/09-financial-management.md` - Cash flow, expenses, reporting
   - `docs/features/10-marketplace.md` - Online storefront & e-commerce
   - `docs/features/11-reports-analytics.md` - Business intelligence & insights
   - `docs/features/12-notifications.md` - Alerts & communication
   - `docs/features/13-settings.md` - Configuration & preferences
   - `docs/features/14-platform-admin.md` - System administration

   **Development Setup Guides** (For implementation details):
   - `apps/[app-name]/docs/dev-guide/01-setup.md` - Project-specific setup
   - `packages/[package-name]/docs/dev-guide/01-setup.md` - Package usage

   **Project READMEs** (For quick reference):
   - `apps/[app-name]/README.md` - Project overview
   - `packages/[package-name]/README.md` - Package overview

5. **Identify and read relevant feature documentation**:

   **Step 1: Determine which feature(s) the story relates to:**
   - Authentication/Login → `01-authentication.md`
   - Store/Tenant setup → `02-tenant-management.md`
   - Products/SKU/Variants → `03-product-management.md`
   - Stock/Inventory → `04-inventory-management.md`
   - Cashier/POS → `05-pos-cashier.md`
   - Orders/Sales → `06-order-management.md`
   - Customers/Tiers → `07-customer-management.md`
   - Suppliers/Purchasing → `08-supplier-purchasing.md`
   - Cash flow/Expenses → `09-financial-management.md`
   - Online store → `10-marketplace.md`
   - Reports/Analytics → `11-reports-analytics.md`
   - Notifications/Alerts → `12-notifications.md`
   - Settings/Config → `13-settings.md`
   - Platform admin → `14-platform-admin.md`

   **Step 2: Read the identified feature file(s) thoroughly:**
   - **Business Requirements** - Understand goals and problems being solved
   - **Features** - Review detailed capabilities and sub-features
   - **User Flows** - Follow interaction patterns and workflows
   - **API Endpoints** - Use exact endpoint definitions (method, path, auth)
   - **Data Models** - Follow Firestore collections and field structures
   - **Dependencies** - Note required features and integrations
   - **Edge Cases** - Consider validation rules and error scenarios

   **Step 3: Check related features for dependencies:**
   - Example: Product story may need Customer tiers (07) for pricing
   - Example: Order story needs Products (03), Customers (07), and Inventory (04)

6. **Generate complete content** for all sections:

   ### User Story
   - Format: "As a [user role], I want to [action] so that [benefit]"
   - Use roles from feature documentation (Owner, Admin, Staff, Cashier, Customer, Platform Admin)

   ### Acceptance Criteria
   - Specific, testable checkboxes
   - Reference feature documentation requirements and acceptance criteria
   - Include edge cases from "Edge Cases" section in feature docs
   - API response validation (match data models in feature docs)
   - Follow user flows from feature documentation

   ### Technical Design

   **For API stories:**
   - API endpoints (use exact endpoints from feature documentation)
   - Request/response schemas (use Zod from @toko/shared-types)
   - Database operations (Firestore collections from feature data models)
   - Error handling (follow patterns in apps/api/docs/dev-guide/01-setup.md)
   - Authentication/authorization (using Firebase Admin SDK)
   - Reference: `apps/api/docs/dev-guide/01-setup.md` for API development guidelines

   **For Frontend stories:**
   - Component structure (follow project structure in dev-guide)
   - API integration (@toko/firebase-client - see packages/firebase-client/docs/dev-guide/01-setup.md)
   - State management (React hooks, Zustand if needed)
   - Form validation (Zod schemas from @toko/shared-types)
   - UI components (@toko/ui-web - see packages/ui-web/docs/dev-guide/01-setup.md)
   - Reference: `apps/[app-name]/docs/dev-guide/01-setup.md` for app-specific patterns

   ### Implementation Checklist

   **Phase 1: Setup**
   - Create necessary files following project structure
   - Import required dependencies

   **Phase 2: Implementation**
   - Implement core functionality
   - Follow modular architecture (components/pages/[feature]/)
   - Use shared packages (@toko/firebase-client, @toko/shared-types, @toko/ui-web)

   **Phase 3: Testing & Validation**
   - Run `pnpm typecheck` (must pass)
   - Run `pnpm lint` (must pass)
   - Manual testing checklist
   - Test all acceptance criteria

   **Phase 4: Code Review** (ALWAYS include)
   - Run `/bmad:bmm:workflows:code-review` workflow
   - Address any issues found
   - Re-run typecheck and lint after fixes

   ### Dependencies
   - List prerequisite stories
   - List required packages
   - List external services (Firebase, Midtrans, etc.)

   ### Testing
   - Unit tests (when applicable)
   - API testing (Postman/Thunder Client)
   - UI testing (manual checklist)
   - Edge cases

   ### Notes
   - Edge cases from feature documentation "Edge Cases & Validation" section
   - Implementation considerations from "Technical Considerations" section
   - Future enhancements from "Future Enhancements" section
   - Security considerations from "Security & Permissions" section
   - Business rules from "Business Requirements" section

7. **Update the todo file** with generated content
8. **Remove HTML comment placeholders** (<!-- AI: ... -->)

## Key References

### Documentation Structure

**Feature Documentation** (`docs/features/`):
- 01-14: Individual feature files with complete specifications
- Each contains: Business Requirements, Features, User Flows, API Endpoints, Data Models, Dependencies

**Development Guides** (`*/docs/dev-guide/`):
- `01-setup.md` - Setup instructions, project structure, development workflow
- Available for all apps and packages

**Project Overview** (`*/README.md`):
- High-level project description
- Quick start guide
- Technology stack

### Architecture Patterns

**API (Flask):**
```python
# apps/api/app.py structure
from flask import Flask, jsonify, request
from flask_cors import CORS

@app.route('/api/resource', methods=['GET', 'POST'])
def handle_resource():
    # Implementation
    pass
```

**Frontend (Next.js):**
```
components/pages/[feature]/
├── index.tsx              # Main component (composition)
├── components/            # Sub-components (presentation)
│   ├── feature-card.tsx
│   └── feature-form.tsx
├── hooks/                 # Custom hooks (logic)
│   └── use-feature-data.ts
└── utils/                 # Helper functions
    └── format-data.ts
```

### Shared Packages

- `@toko/firebase-client` - Firebase SDK (Auth, Firestore, Storage)
- `@toko/shared-types` - Zod schemas and TypeScript types
- `@toko/ui-web` - shadcn/ui components

## Output Format

After filling the story, provide a summary:

```
✅ Story filled successfully!

📋 Generated:
- User Story (for [role])
- [N] Acceptance Criteria
- Technical Design ([API/Frontend] scope)
- [N] Implementation Tasks
- Testing Requirements
- Dependencies & Notes

🎯 Story ready for development!

Next steps:
1. Review the filled story
2. Make any adjustments if needed
3. Run `/bmad:bmm:workflows:dev-story [file]` to start implementation

Or type 'go' to start development immediately.
```

## Example Workflow

### Example: Filling a Product Management Story

**Given story file**: `apps/api/docs/todos/create-product-api.md`

**Workflow:**

1. **Read** the story file to extract:
   - Title: "Create Product API Endpoint"
   - Overview: "Implement POST /api/products endpoint to create new products"

2. **Identify scope**:
   - Path: `apps/api/` → Flask API Backend
   - Topic: Products → Feature file: `03-product-management.md`

3. **Read documentation**:
   - Primary: `docs/features/03-product-management.md`
     - API Endpoints section → Find `POST /api/products`
     - Data Models section → Get Product schema
     - Business Requirements → Understand product rules
   - Secondary: `apps/api/docs/dev-guide/01-setup.md`
     - Review API development patterns
     - Check error handling examples
   - Related: `docs/features/02-tenant-management.md`
     - Products are tenant-isolated

4. **Generate story content**:
   - User Story: "As a store owner, I want to create products via API..."
   - Acceptance Criteria: Based on 03-product-management.md requirements
   - Technical Design:
     - Endpoint: `POST /api/products` (from feature docs)
     - Schema: ProductSchema from @toko/shared-types
     - Firestore: `products` collection (from data model)
   - Implementation: Flask route with validation
   - Testing: API tests with valid/invalid data

5. **Write to file** and confirm ready for development

This ensures all story details are consistent with feature specifications and ready for implementation.
