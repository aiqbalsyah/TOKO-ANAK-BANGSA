"""
TOKO ANAK BANGSA - Flask API
Main application entry point
"""
import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials

# Load environment variables
load_dotenv()

# Initialize Firebase Admin SDK
try:
    # Try to initialize with service account file
    service_account_path = os.getenv('FIREBASE_SERVICE_ACCOUNT_PATH')
    if service_account_path and os.path.exists(service_account_path):
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)
        print("✅ Firebase Admin SDK initialized with service account")
    else:
        # Fallback: Initialize with default credentials (for deployment)
        firebase_admin.initialize_app()
        print("✅ Firebase Admin SDK initialized with default credentials")
except ValueError as e:
    # App already initialized
    print("ℹ️  Firebase Admin SDK already initialized")
except Exception as e:
    print(f"⚠️  Firebase initialization error: {e}")
    print("   Some features may not work without Firebase configuration")

# Initialize Flask app
app = Flask(__name__)

# Load Flask config from environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')
app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'

# CORS configuration
cors_origins = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')
CORS(app, resources={
    r"/api/*": {
        "origins": cors_origins,
        "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
    }
})

# Initialize rate limiter
from extensions import limiter
limiter.init_app(app)

# Register blueprints
from routes.auth import auth_bp
from routes.roles import roles_bp

app.register_blueprint(auth_bp)
app.register_blueprint(roles_bp)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

# Health check endpoints
@app.route("/")
def index():
    return jsonify({
        "message": "TOKO ANAK BANGSA API",
        "version": "1.0.0",
        "status": "healthy"
    })

@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "ok",
        "service": "TOKO ANAK BANGSA API",
        "firebase": "initialized" if firebase_admin._apps else "not initialized"
    })

# Example API endpoint
@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from TOKO ANAK BANGSA API!",
        "endpoints": {
            "auth": "/api/auth/*",
            "roles": "/api/roles/*",
            "health": "/api/health"
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
