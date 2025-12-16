"""
Authentication Routes
Handles user registration, login, verification, password reset, etc.
"""

from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from models.user import (
    RegisterRequest,
    LoginRequest,
    GoogleAuthRequest,
    UpdateProfileRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
    VerifyEmailRequest,
    RefreshTokenRequest,
    DeleteAccountRequest,
)
from services.auth_service import get_auth_service
from middleware.auth import require_auth
from extensions import limiter

# Create Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
@limiter.limit("5 per hour")
def register():
    """
    Register new user with email and password

    Request Body:
    {
        "email": "user@example.com",
        "password": "SecurePass123",
        "displayName": "John Doe",
        "phoneNumber": "+628123456789" (optional)
    }

    Response (201):
    {
        "success": true,
        "data": {
            "user": {...},
            "tokens": {...}
        }
    }
    """
    try:
        # Validate request
        data = RegisterRequest(**request.json)

        # Register user
        auth_service = get_auth_service()
        user_data, tokens = auth_service.register_user(
            email=data.email,
            password=data.password,
            display_name=data.displayName,
            phone_number=data.phoneNumber,
        )

        return (
            jsonify(
                {
                    'success': True,
                    'data': {
                        'user': user_data,
                        'tokens': tokens.dict(),
                    },
                }
            ),
            201,
        )

    except ValidationError as e:
        return (
            jsonify(
                {
                    'success': False,
                    'error': 'Validation error',
                    'details': e.errors(),
                }
            ),
            400,
        )
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 409
    except Exception as e:
        print(f"Registration error: {e}")
        return jsonify({'success': False, 'error': 'Registration failed'}), 500


@auth_bp.route('/login', methods=['POST'])
@limiter.limit("10 per hour")
def login():
    """
    Login with email and password

    Request Body:
    {
        "email": "user@example.com",
        "password": "SecurePass123"
    }

    Response (200):
    {
        "success": true,
        "data": {
            "user": {...},
            "tokens": {...}
        }
    }
    """
    try:
        # Validate request
        data = LoginRequest(**request.json)

        # Login user
        auth_service = get_auth_service()
        user_data, tokens = auth_service.login(
            email=data.email,
            password=data.password,
        )

        return jsonify(
            {
                'success': True,
                'data': {
                    'user': user_data,
                    'tokens': tokens.dict(),
                },
            }
        )

    except ValidationError as e:
        return (
            jsonify(
                {
                    'success': False,
                    'error': 'Validation error',
                    'details': e.errors(),
                }
            ),
            400,
        )
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 401
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({'success': False, 'error': 'Login failed'}), 500


@auth_bp.route('/google', methods=['POST'])
@limiter.limit("10 per hour")
def google_auth():
    """
    Login or register with Google OAuth

    Request Body:
    {
        "idToken": "google-id-token"
    }

    Response (200):
    {
        "success": true,
        "data": {
            "user": {...},
            "tokens": {...}
        }
    }
    """
    try:
        # Validate request
        data = GoogleAuthRequest(**request.json)

        # Google login
        auth_service = get_auth_service()
        user_data, tokens = auth_service.google_login(id_token=data.idToken)

        return jsonify(
            {
                'success': True,
                'data': {
                    'user': user_data,
                    'tokens': tokens.dict(),
                },
            }
        )

    except ValidationError as e:
        return (
            jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}),
            400,
        )
    except Exception as e:
        print(f"Google auth error: {e}")
        return jsonify({'success': False, 'error': 'Google authentication failed'}), 500


@auth_bp.route('/logout', methods=['POST'])
@require_auth
def logout():
    """
    Logout user (revoke tokens)

    Headers:
        Authorization: Bearer {access-token}

    Response (200):
    {
        "success": true,
        "message": "Logged out successfully"
    }
    """
    # TODO: Implement token revocation/blacklist
    # Options:
    # 1. Redis blacklist: Store revoked tokens with TTL = token expiry
    # 2. Firestore blacklist: Store in 'revoked_tokens' collection
    # 3. Firebase Auth: Use auth.revoke_refresh_tokens(request.user_id)
    #
    # SECURITY WARNING: Without token revocation, logged-out users can still
    # use their tokens until they expire (15min access, 7 days refresh)
    #
    # Recommended: Use Firebase's revoke_refresh_tokens() for simplicity

    return jsonify({'success': True, 'message': 'Logged out successfully'})


@auth_bp.route('/refresh', methods=['POST'])
@limiter.limit("30 per hour")
def refresh_token():
    """
    Refresh access token using refresh token

    Request Body:
    {
        "refreshToken": "jwt-refresh-token"
    }

    Response (200):
    {
        "success": true,
        "data": {
            "accessToken": "new-jwt-token",
            "refreshToken": "new-refresh-token",
            "expiresIn": 900
        }
    }
    """
    try:
        # Validate request
        data = RefreshTokenRequest(**request.json)

        # Refresh token
        auth_service = get_auth_service()
        tokens = auth_service.refresh_access_token(data.refreshToken)

        return jsonify({'success': True, 'data': tokens.dict()})

    except ValidationError as e:
        return (
            jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}),
            400,
        )
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 401
    except Exception as e:
        print(f"Token refresh error: {e}")
        return jsonify({'success': False, 'error': 'Token refresh failed'}), 500


@auth_bp.route('/me', methods=['GET'])
@require_auth
def get_current_user():
    """
    Get current user profile

    Headers:
        Authorization: Bearer {access-token}

    Response (200):
    {
        "success": true,
        "data": {
            "user": {...}
        }
    }
    """
    try:
        auth_service = get_auth_service()
        user = auth_service.get_user(request.user_id)

        if not user:
            return jsonify({'success': False, 'error': 'User not found'}), 404

        return jsonify({'success': True, 'data': {'user': user}})

    except Exception as e:
        print(f"Get user error: {e}")
        return jsonify({'success': False, 'error': 'Failed to get user'}), 500


@auth_bp.route('/profile', methods=['PATCH'])
@require_auth
@limiter.limit("20 per hour")
def update_profile():
    """
    Update user profile

    Headers:
        Authorization: Bearer {access-token}

    Request Body:
    {
        "displayName": "Jane Doe",
        "phoneNumber": "+628123456789",
        "bio": "Store owner at Toko Makmur"
    }

    Response (200):
    {
        "success": true,
        "data": {
            "user": {...}
        }
    }
    """
    try:
        # Validate request
        data = UpdateProfileRequest(**request.json)

        # Update profile
        auth_service = get_auth_service()
        updates = data.dict(exclude_unset=True)  # Only include provided fields
        user = auth_service.update_profile(request.user_id, updates)

        return jsonify({'success': True, 'data': {'user': user}})

    except ValidationError as e:
        return (
            jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}),
            400,
        )
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 404
    except Exception as e:
        print(f"Update profile error: {e}")
        return jsonify({'success': False, 'error': 'Profile update failed'}), 500


@auth_bp.route('/verify-email', methods=['POST'])
@limiter.limit("5 per hour")
def verify_email():
    """
    Verify email with token

    Request Body:
    {
        "token": "verification-token"
    }

    Response (200):
    {
        "success": true,
        "message": "Email verified successfully"
    }
    """
    try:
        data = VerifyEmailRequest(**request.json)
        auth_service = get_auth_service()
        auth_service.verify_email(data.token)

        return jsonify({'success': True, 'message': 'Email verified successfully'})

    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}), 400
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        print(f"Email verification error: {e}")
        return jsonify({'success': False, 'error': 'Email verification failed'}), 500


@auth_bp.route('/resend-verification', methods=['POST'])
@require_auth
@limiter.limit("3 per hour")
def resend_verification():
    """
    Resend verification email

    Headers:
        Authorization: Bearer {access-token}

    Response (200):
    {
        "success": true,
        "message": "Verification email sent"
    }
    """
    try:
        auth_service = get_auth_service()
        auth_service.resend_verification_email(request.user_id)

        return jsonify({'success': True, 'message': 'Verification email sent'})

    except ValueError as e:
        # Check if it's a rate limit error
        error_msg = str(e)
        if 'rate limit' in error_msg.lower() or 'too many' in error_msg.lower():
            return jsonify({'success': False, 'error': error_msg}), 429
        else:
            return jsonify({'success': False, 'error': error_msg}), 400
    except Exception as e:
        print(f"Resend verification error: {e}")
        return jsonify({'success': False, 'error': 'Failed to send verification email'}), 500


@auth_bp.route('/forgot-password', methods=['POST'])
@limiter.limit("3 per hour")
def forgot_password():
    """
    Request password reset email

    Request Body:
    {
        "email": "user@example.com"
    }

    Response (200):
    {
        "success": true,
        "message": "Password reset email sent if account exists"
    }
    """
    try:
        data = ForgotPasswordRequest(**request.json)
        auth_service = get_auth_service()
        auth_service.send_password_reset_email(data.email)

        # Always return success to avoid email enumeration
        return jsonify({'success': True, 'message': 'Password reset email sent if account exists'})

    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}), 400
    except Exception as e:
        print(f"Forgot password error: {e}")
        # Still return success to avoid revealing if email exists
        return jsonify({'success': True, 'message': 'Password reset email sent if account exists'})


@auth_bp.route('/reset-password', methods=['POST'])
@limiter.limit("3 per hour")
def reset_password():
    """
    Reset password with token

    Request Body:
    {
        "token": "reset-token",
        "newPassword": "NewSecurePass123"
    }

    Response (200):
    {
        "success": true,
        "message": "Password reset successfully"
    }
    """
    try:
        data = ResetPasswordRequest(**request.json)
        auth_service = get_auth_service()
        auth_service.reset_password(data.token, data.newPassword)

        return jsonify({'success': True, 'message': 'Password reset successfully'})

    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}), 400
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        print(f"Reset password error: {e}")
        return jsonify({'success': False, 'error': 'Password reset failed'}), 500


@auth_bp.route('/account', methods=['DELETE'])
@require_auth
def delete_account():
    """
    Delete user account

    Headers:
        Authorization: Bearer {access-token}

    Request Body:
    {
        "password": "current-password"
    }

    Response (200):
    {
        "success": true,
        "message": "Account deleted successfully"
    }
    """
    try:
        data = DeleteAccountRequest(**request.json)
        auth_service = get_auth_service()
        auth_service.delete_account(request.user_id, data.password)

        return jsonify({'success': True, 'message': 'Account deleted successfully'})

    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'details': e.errors()}), 400
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 403
    except Exception as e:
        print(f"Delete account error: {e}")
        return jsonify({'success': False, 'error': 'Account deletion failed'}), 500
