"""
Authentication Middleware - JWT verification and Firebase Auth integration
"""

from functools import wraps
from flask import request, jsonify
from firebase_admin import auth as firebase_auth
import jwt
import os

from services.auth_service import get_auth_service
from services.role_service import get_role_service


def require_auth(f):
    """
    Decorator to require authentication (JWT or Firebase ID token)

    Usage:
        @app.route('/api/protected')
        @require_auth
        def protected_route():
            user_id = request.user_id  # Added by middleware
            return {'message': 'Hello'}
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'success': False, 'error': 'Unauthorized - No token provided'}), 401

        token = auth_header.split('Bearer ')[1]

        try:
            # Try to verify as Firebase ID token first
            decoded_token = firebase_auth.verify_id_token(token)
            request.user_id = decoded_token['uid']
            request.user_email = decoded_token.get('email')
            return f(*args, **kwargs)
        except Exception as firebase_error:
            # If Firebase verification fails, try JWT
            try:
                auth_service = get_auth_service()
                payload = auth_service.verify_token(token)

                if not payload:
                    return jsonify({'success': False, 'error': 'Invalid or expired token'}), 401

                if payload.get('type') != 'access':
                    return jsonify({'success': False, 'error': 'Invalid token type'}), 401

                request.user_id = payload.get('user_id')

                # Get user email from database
                user = auth_service.get_user(request.user_id)
                if user:
                    request.user_email = user.get('email')

                return f(*args, **kwargs)

            except Exception as jwt_error:
                return (
                    jsonify(
                        {
                            'success': False,
                            'error': 'Invalid token - authentication failed',
                        }
                    ),
                    401,
                )

    return decorated_function


def require_role_level(min_level: int, tenant_param: str = 'tenantId'):
    """
    Decorator to require minimum role level in a tenant

    Args:
        min_level: Minimum required role level
        tenant_param: Request parameter name containing tenant ID (default: 'tenantId')

    Usage:
        @app.route('/api/roles')
        @require_auth
        @require_role_level(70)  # Requires admin level (70) or higher
        def create_role():
            return {'message': 'Role created'}
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Ensure user is authenticated
            if not hasattr(request, 'user_id'):
                return (
                    jsonify(
                        {
                            'success': False,
                            'error': 'Unauthorized - Authentication required',
                        }
                    ),
                    401,
                )

            # Get tenant ID from request
            tenant_id = request.args.get(tenant_param) or request.json.get(tenant_param)
            if not tenant_id:
                return (
                    jsonify({'success': False, 'error': f'Missing required parameter: {tenant_param}'}),
                    400,
                )

            # Check user's role level in tenant
            role_service = get_role_service()
            user_level = role_service.get_user_role_level(request.user_id, tenant_id)

            if user_level is None:
                return (
                    jsonify({'success': False, 'error': 'User not found in tenant'}),
                    403,
                )

            if user_level < min_level:
                return (
                    jsonify(
                        {
                            'success': False,
                            'error': f'Insufficient permissions - Requires role level {min_level} or higher',
                        }
                    ),
                    403,
                )

            # Add tenant_id to request for convenience
            request.tenant_id = tenant_id
            request.user_level = user_level

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def require_permission(permission_name: str, tenant_param: str = 'tenantId'):
    """
    Decorator to require specific permission in a tenant

    Args:
        permission_name: Permission to check (e.g., 'canCreateProducts')
        tenant_param: Request parameter name containing tenant ID

    Usage:
        @app.route('/api/products', methods=['POST'])
        @require_auth
        @require_permission('canCreateProducts')
        def create_product():
            return {'message': 'Product created'}
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Ensure user is authenticated
            if not hasattr(request, 'user_id'):
                return (
                    jsonify({'success': False, 'error': 'Unauthorized'}),
                    401,
                )

            # Get tenant ID
            tenant_id = request.args.get(tenant_param) or request.json.get(tenant_param)
            if not tenant_id:
                return (
                    jsonify({'success': False, 'error': f'Missing parameter: {tenant_param}'}),
                    400,
                )

            # Check permission
            role_service = get_role_service()
            has_permission = role_service.can_user_perform(
                request.user_id, tenant_id, permission_name
            )

            if not has_permission:
                return (
                    jsonify(
                        {
                            'success': False,
                            'error': f'Insufficient permissions - Requires {permission_name}',
                        }
                    ),
                    403,
                )

            # Add tenant_id to request
            request.tenant_id = tenant_id

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def optional_auth(f):
    """
    Decorator for optional authentication
    Adds user_id to request if authenticated, but doesn't require it

    Usage:
        @app.route('/api/public-data')
        @optional_auth
        def public_route():
            if hasattr(request, 'user_id'):
                # User is authenticated
                return {'message': f'Hello {request.user_id}'}
            else:
                # User is not authenticated
                return {'message': 'Hello guest'}
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split('Bearer ')[1]

            try:
                # Try Firebase Auth
                decoded_token = firebase_auth.verify_id_token(token)
                request.user_id = decoded_token['uid']
                request.user_email = decoded_token.get('email')
            except:
                try:
                    # Try JWT
                    auth_service = get_auth_service()
                    payload = auth_service.verify_token(token)
                    if payload and payload.get('type') == 'access':
                        request.user_id = payload.get('user_id')
                except:
                    pass  # Ignore errors for optional auth

        return f(*args, **kwargs)

    return decorated_function
