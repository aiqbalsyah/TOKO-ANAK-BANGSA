# Claude Code Guide - API

**Project**: Flask REST API
**Tech Stack**: Python 3.12, Flask, Firebase Admin SDK, Gunicorn
**Purpose**: Backend REST API for TOKO ANAK BANGSA platform

---

## Quick Start for AI Assistants

When working on this project with Claude Code, follow this workflow:

### 1. Understand the Project

**Read these first:**
- `apps/api/README.md` - Project overview
- `apps/api/docs/dev-guide/01-setup.md` - Complete setup guide, patterns, and best practices

**Documentation structure:**
- Feature specs: `docs/features/01-14.md` - Business requirements and API specifications
- Dev guide: `apps/api/docs/dev-guide/` - Development patterns and setup
- Shared types: `packages/shared-types/` - Request/response schemas (Zod)

### 2. Working on Stories

**When filling a story** (via `/fill-story` command):

1. **Identify the feature**: Read the relevant feature file from `docs/features/`
   - Example: Products → `docs/features/03-product-management.md`

2. **Find API endpoints**: Use exact endpoint definitions from the feature file's "API Endpoints" section

3. **Check data models**: Follow Firestore collection structures from "Data Models" section

4. **Reference dev-guide**: Follow patterns in `apps/api/docs/dev-guide/01-setup.md`
   - Error handling patterns
   - Request/response format
   - Authentication middleware
   - Firestore operations

### 3. Implementation Patterns

**API Route Structure:**

```python
# apps/api/routes/products.py
from flask import Blueprint, jsonify, request
from firebase_admin import firestore

products_bp = Blueprint('products', __name__)
db = firestore.client()

@products_bp.route('/api/products', methods=['GET'])
def list_products():
    try:
        # Get tenant_id from auth middleware
        tenant_id = request.tenant_id

        # Query Firestore
        products_ref = db.collection('products')
        query = products_ref.where('tenant_id', '==', tenant_id)
        docs = query.stream()

        products = []
        for doc in docs:
            product = doc.to_dict()
            product['id'] = doc.id
            products.append(product)

        return jsonify({
            'success': True,
            'data': products
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@products_bp.route('/api/products', methods=['POST'])
def create_product():
    try:
        # Validate request
        data = request.get_json()

        # Validate with Zod schema (via @toko/shared-types)
        # Note: Python API should define Pydantic models that match Zod schemas

        # Add tenant isolation
        data['tenant_id'] = request.tenant_id
        data['created_at'] = firestore.SERVER_TIMESTAMP
        data['updated_at'] = firestore.SERVER_TIMESTAMP

        # Save to Firestore
        doc_ref = db.collection('products').add(data)
        product_id = doc_ref[1].id

        return jsonify({
            'success': True,
            'data': {'id': product_id, **data}
        }), 201

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
```

**Error Response Format:**

```python
# Success
{
    "success": True,
    "data": { ... }
}

# Error
{
    "success": False,
    "error": "Error message"
}
```

**Authentication Middleware:**

```python
# Check Firebase ID token from Authorization header
# Add tenant_id to request object for tenant isolation
```

### 4. File Organization

Follow this structure when creating new features:

```
apps/api/
├── routes/
│   ├── products.py          # Product endpoints
│   ├── inventory.py         # Inventory endpoints
│   └── orders.py            # Order endpoints
├── models/                  # Pydantic models (Python equivalent of Zod)
│   ├── product.py
│   └── order.py
├── services/                # Business logic
│   ├── product_service.py
│   └── order_service.py
└── middleware/
    ├── auth.py              # Firebase auth verification
    └── tenant.py            # Tenant isolation
```

### 5. Key Principles

**Always follow these rules:**

1. **Tenant Isolation**: All data must include `tenant_id` and be filtered by tenant
2. **Authentication**: Verify Firebase ID token on protected routes
3. **Error Handling**: Always return proper HTTP status codes and error format
4. **Validation**: Validate all input data (use Pydantic models)
5. **Timestamps**: Add `created_at` and `updated_at` to all documents
6. **API Endpoints**: Use exact endpoints from feature documentation

### 6. Testing

**Before marking story as complete:**

1. Run type checking: `mypy .` (if using type hints)
2. Test with API client (Postman/curl):
   ```bash
   # Create product
   curl -X POST http://localhost:8080/api/products \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <firebase-token>" \
     -d '{"name":"Test Product","price":10000}'

   # Get products
   curl http://localhost:8080/api/products \
     -H "Authorization: Bearer <firebase-token>"
   ```
3. Check Firestore to verify data is saved correctly
4. Test error cases (invalid input, unauthorized access)

### 7. Common Operations

**Firestore Operations:**

```python
from firebase_admin import firestore

db = firestore.client()

# Create
doc_ref = db.collection('products').add({'name': 'Product'})

# Read one
doc = db.collection('products').document('doc_id').get()
data = doc.to_dict()

# Read many (with filter)
query = db.collection('products').where('tenant_id', '==', 'tenant-1')
docs = query.stream()

# Update
db.collection('products').document('doc_id').update({
    'name': 'New Name',
    'updated_at': firestore.SERVER_TIMESTAMP
})

# Delete
db.collection('products').document('doc_id').delete()
```

### 8. Deployment

API is deployed on Firebase App Hosting. Configuration in `apphosting.yaml`.

To deploy:
```bash
firebase deploy --only apphosting:api
```

---

## Quick Reference

**Documentation:**
- Setup: `apps/api/docs/dev-guide/01-setup.md`
- Features: `docs/features/01-14.md`
- Shared types: `packages/shared-types/README.md`

**Commands:**
```bash
# Setup
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
flask run --debug --port 8080

# From root
pnpm dev:api
```

**Environment Variables:**
- `GOOGLE_APPLICATION_CREDENTIALS` - Path to Firebase service account key
- `FLASK_ENV` - development/production
- `PORT` - 8080

---

**Last Updated**: 2024-12-13
