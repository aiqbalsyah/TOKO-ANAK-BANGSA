"""
Flask extensions
Shared instances of Flask extensions to avoid circular imports
"""
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize limiter (will be bound to app in app.py)
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per hour", "50 per minute"],
    storage_uri="memory://",
    strategy="fixed-window",
)
