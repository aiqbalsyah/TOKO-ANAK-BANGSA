# TOKO ANAK BANGSA - Flask API

Backend REST API for TOKO ANAK BANGSA platform.

## Tech Stack

- **Python 3.12**
- **Flask** - Web framework
- **Firebase Admin SDK** - Firestore, Auth, Storage integration
- **Pydantic** - Data validation
- **Gunicorn** - Production server

## Local Development

### Prerequisites

- Python 3.12+
- pip

### Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
flask run --debug --port 8080
```

Or use the monorepo script:
```bash
pnpm dev:api
```

## API Endpoints

### Health Check
```
GET /
GET /api/health
```

### Example
```
GET /api/hello
```

## Firebase App Hosting Deployment

The API is deployed on Firebase App Hosting using `apphosting.yaml`.

```bash
firebase deploy --only apphosting:api
```

## Environment Variables

Set in Firebase App Hosting console or `apphosting.yaml`:

- `FLASK_APP=app.py`
- `FLASK_ENV=production`
- `PORT=8080`

## Project Structure

```
apps/api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── apphosting.yaml     # Firebase App Hosting config
├── .python-version     # Python version
└── README.md           # This file
```

## Future Structure (when implementing features)

```
apps/api/
├── app.py
├── config.py           # Configuration
├── requirements.txt
├── apphosting.yaml
├── routes/             # API routes
│   ├── __init__.py
│   ├── auth.py        # Authentication endpoints
│   ├── products.py    # Product endpoints
│   ├── orders.py      # Order endpoints
│   └── payments.py    # Payment webhooks
├── models/            # Pydantic models
│   ├── __init__.py
│   ├── product.py
│   └── order.py
├── services/          # Business logic
│   ├── __init__.py
│   ├── product_service.py
│   └── order_service.py
└── utils/             # Utilities
    ├── __init__.py
    ├── firebase.py    # Firebase admin initialization
    └── validators.py  # Custom validators
```
