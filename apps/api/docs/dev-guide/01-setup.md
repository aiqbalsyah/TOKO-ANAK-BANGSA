# API - Development Setup Guide

**Project**: Flask REST API
**Tech Stack**: Python 3.12, Flask, Firebase Admin SDK, Gunicorn
**Purpose**: Backend REST API for TOKO ANAK BANGSA platform

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (included with Python)
- **pnpm** - For monorepo scripts (if using monorepo commands)
- **Firebase CLI** - For deployment: `npm install -g firebase-tools`

---

## Initial Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd pos_app_v1
```

### 2. Python Virtual Environment

Create and activate a Python virtual environment:

**macOS/Linux:**
```bash
cd apps/api
python3.12 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
cd apps/api
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Key Dependencies:**
- `Flask` - Web framework
- `firebase-admin` - Firebase Admin SDK (Firestore, Auth, Storage)
- `pydantic` - Data validation
- `gunicorn` - Production WSGI server
- `python-dotenv` - Environment variable management

### 4. Environment Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
PORT=8080

# Firebase Configuration (from Firebase Console)
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account-key.json

# API Configuration
API_PREFIX=/api
CORS_ORIGINS=http://localhost:3000,http://localhost:3001

# Optional: Firebase Admin SDK initialization
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com
```

### 5. Firebase Service Account

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to Project Settings → Service Accounts
4. Click "Generate New Private Key"
5. Save the JSON file to `apps/api/` directory
6. Update `GOOGLE_APPLICATION_CREDENTIALS` in `.env` to point to this file

**Security Warning:** Never commit service account keys to Git! Add to `.gitignore`.

---

## Running the Application

### Development Server

**Option 1: Direct Flask command**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

flask run --debug --port 8080
```

**Option 2: Using monorepo script (from root)**
```bash
# From project root
pnpm dev:api
```

The API will be available at: `http://localhost:8080`

### Test the API

```bash
# Health check
curl http://localhost:8080/
curl http://localhost:8080/api/health

# Example endpoint
curl http://localhost:8080/api/hello
```

---

## Project Structure

### Current Structure
```
apps/api/
├── app.py                  # Main Flask application entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Local environment (gitignored)
├── .python-version         # Python version (3.12)
├── apphosting.yaml         # Firebase App Hosting config
├── venv/                   # Virtual environment (gitignored)
├── docs/                   # Documentation
│   ├── dev-guide/          # Developer guides
│   └── todos/              # Story/task files
└── README.md               # Project overview
```

### Planned Structure (As Features Are Implemented)
```
apps/api/
├── app.py                  # Main Flask application
├── config.py               # Configuration management
├── requirements.txt        # Dependencies
├── routes/                 # API route handlers
│   ├── __init__.py
│   ├── auth.py             # Authentication endpoints
│   ├── tenants.py          # Tenant management
│   ├── products.py         # Product CRUD
│   ├── inventory.py        # Inventory management
│   ├── orders.py           # Order management
│   ├── customers.py        # Customer management
│   ├── suppliers.py        # Supplier & purchasing
│   ├── financials.py       # Financial reports
│   └── webhooks.py         # Payment webhooks (Midtrans)
├── models/                 # Pydantic data models
│   ├── __init__.py
│   ├── tenant.py
│   ├── product.py
│   ├── order.py
│   ├── customer.py
│   └── payment.py
├── services/               # Business logic layer
│   ├── __init__.py
│   ├── auth_service.py
│   ├── tenant_service.py
│   ├── product_service.py
│   ├── inventory_service.py
│   ├── order_service.py
│   ├── payment_service.py
│   └── notification_service.py
├── middleware/             # Flask middleware
│   ├── __init__.py
│   ├── auth.py             # JWT authentication
│   ├── tenant.py           # Tenant isolation
│   └── error_handler.py    # Error handling
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── firebase.py         # Firebase Admin SDK initialization
│   ├── validators.py       # Custom validators
│   └── decorators.py       # Custom decorators
└── tests/                  # Unit tests
    ├── __init__.py
    ├── test_auth.py
    ├── test_products.py
    └── test_orders.py
```

---

## Development Workflow

### 1. Install New Dependency

```bash
# Activate virtual environment
source venv/bin/activate

# Install package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### 2. Run Tests

```bash
# Install pytest (if not already)
pip install pytest pytest-cov

# Run tests
pytest

# Run with coverage
pytest --cov=.
```

### 3. Code Formatting & Linting

```bash
# Install formatting tools
pip install black flake8 isort

# Format code
black .

# Sort imports
isort .

# Lint code
flake8 .
```

---

## Firebase App Hosting Deployment

The API is deployed on Firebase App Hosting (serverless Flask).

### Deploy to Production

```bash
# Login to Firebase
firebase login

# Deploy API
firebase deploy --only apphosting:api

# View logs
firebase apphosting:backends:get api
```

### Configuration (`apphosting.yaml`)

```yaml
# Firebase App Hosting configuration
runConfig:
  runtime: python312
  entrypoint: gunicorn app:app

env:
  - variable: FLASK_APP
    value: app.py
  - variable: FLASK_ENV
    value: production
  - variable: PORT
    value: "8080"
```

---

## Common Issues & Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'flask'`

**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: Firebase Admin SDK initialization fails

**Solution:** Check that:
1. Service account JSON file exists
2. `GOOGLE_APPLICATION_CREDENTIALS` points to correct file
3. File has correct permissions (readable)

### Issue: Port 8080 already in use

**Solution:** Kill the process using port 8080 or use a different port:
```bash
# Find process
lsof -ti:8080

# Kill process
kill -9 $(lsof -ti:8080)

# Or use different port
flask run --port 8081
```

### Issue: CORS errors from frontend

**Solution:** Update `CORS_ORIGINS` in `.env` to include frontend URL:
```env
CORS_ORIGINS=http://localhost:3000,http://localhost:3001,http://localhost:3002
```

---

## API Development Guidelines

### 1. Route Organization

- Group related endpoints in separate route modules
- Use Blueprint for route organization
- Follow RESTful conventions

**Example:**
```python
# routes/products.py
from flask import Blueprint, jsonify, request

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def list_products():
    return jsonify({"products": []})

@products_bp.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify({"id": product_id})
```

### 2. Error Handling

Always use proper HTTP status codes and consistent error format:

```python
# Success
return jsonify({"success": True, "data": result}), 200

# Created
return jsonify({"success": True, "data": created}), 201

# Bad Request
return jsonify({"success": False, "error": "Invalid input"}), 400

# Unauthorized
return jsonify({"success": False, "error": "Unauthorized"}), 401

# Not Found
return jsonify({"success": False, "error": "Resource not found"}), 404

# Server Error
return jsonify({"success": False, "error": "Internal server error"}), 500
```

### 3. Authentication

Use Firebase Auth tokens for authentication:

```python
from firebase_admin import auth

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return None
```

### 4. Data Validation

Use Pydantic models for request/response validation:

```python
from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

# In route
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = ProductRequest(**request.json)
        # Process validated data
        return jsonify({"success": True}), 201
    except ValidationError as e:
        return jsonify({"success": False, "errors": e.errors()}), 400
```

---

## Environment Variables Reference

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `FLASK_APP` | Flask application entry point | `app.py` | Yes |
| `FLASK_ENV` | Environment mode | `development` | Yes |
| `FLASK_DEBUG` | Enable debug mode | `True` | Dev only |
| `PORT` | API server port | `8080` | Yes |
| `GOOGLE_APPLICATION_CREDENTIALS` | Firebase service account key | `./serviceAccountKey.json` | Yes |
| `FIREBASE_PROJECT_ID` | Firebase project ID | `toko-anak-bangsa` | Yes |
| `API_PREFIX` | API route prefix | `/api` | No |
| `CORS_ORIGINS` | Allowed CORS origins | `http://localhost:3000` | Yes |

---

## Useful Commands

```bash
# Start development server
pnpm dev:api

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Add new dependency
pip install package-name && pip freeze > requirements.txt

# Run tests
pytest

# Format code
black . && isort .

# Type checking (if using mypy)
mypy .

# Deploy to Firebase
firebase deploy --only apphosting:api

# View deployment logs
firebase apphosting:logs api
```

---

## Next Steps

1. Read `02-architecture.md` (when available) to understand system design
2. Read `03-coding-standards.md` (when available) for code conventions
3. Review feature documentation in `/docs/features/`
4. Check `/docs/todos/` for available development tasks

---

**Last Updated**: 2024-12-13
