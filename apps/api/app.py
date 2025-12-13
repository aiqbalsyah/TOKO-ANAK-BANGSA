"""
TOKO ANAK BANGSA - Flask API
Main application entry point
"""
import os
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# CORS configuration
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",  # Store Portal
            "http://localhost:3001",  # Marketplace
            "http://localhost:3002",  # Company Profile
            "http://localhost:3003",  # Platform Admin
        ]
    }
})

# Health check endpoint
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
        "service": "TOKO ANAK BANGSA API"
    })

# Example API endpoint
@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from TOKO ANAK BANGSA API!"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
