"""
Authentication Service - User registration, login, password management
Handles Firebase Auth integration and JWT token management

NOTE: Password hashing is handled by Firebase Auth, not bcrypt.
Firebase uses industry-standard scrypt algorithm for password hashing.
"""

import os
import secrets
from typing import Optional, Dict, Any, Tuple
from datetime import datetime, timedelta
from firebase_admin import auth, firestore
import jwt

from models.user import (
    User,
    RegisterRequest,
    LoginRequest,
    UserProfile,
    TenantMember,
    TokenResponse,
    UserStatus,
)


class AuthService:
    """Service for authentication and user management"""

    def __init__(self):
        self.db = firestore.client()
        self.jwt_secret = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-this')
        self.jwt_algorithm = 'HS256'
        self.access_token_expiry = 900  # 15 minutes
        self.refresh_token_expiry = 604800  # 7 days
        self.max_failed_attempts = 5
        self.lockout_duration = 900  # 15 minutes

    def register_user(
        self, email: str, password: str, display_name: str, phone_number: Optional[str] = None
    ) -> Tuple[Dict[str, Any], TokenResponse]:
        """
        Register new user with email and password

        Args:
            email: User email
            password: User password (will be hashed)
            display_name: User's display name
            phone_number: Optional phone number

        Returns:
            Tuple of (user_data, tokens)

        Raises:
            ValueError: If email already exists
            Exception: For other Firebase errors
        """
        # Check if user already exists
        try:
            existing_user = auth.get_user_by_email(email)
            if existing_user:
                raise ValueError('Email already registered')
        except auth.UserNotFoundError:
            pass  # User doesn't exist, we can proceed

        # Create Firebase Auth user
        user_record = auth.create_user(
            email=email,
            password=password,
            display_name=display_name,
            phone_number=phone_number,
            email_verified=False,
        )

        # Create Firestore user document
        now = datetime.utcnow()
        user_data = {
            'id': user_record.uid,
            'email': email,
            'emailVerified': False,
            'profile': {
                'displayName': display_name,
                'phoneNumber': phone_number,
                'photoURL': None,
                'bio': None,
            },
            'tenants': [],
            'status': UserStatus.ACTIVE.value,
            'createdAt': now,
            'updatedAt': now,
            'failedLoginAttempts': 0,
        }

        self.db.collection('users').document(user_record.uid).set(user_data)

        # Send verification email
        # TODO: Implement email verification
        # self.send_verification_email(user_record.uid, email)

        # Generate tokens
        tokens = self.generate_tokens(user_record.uid)

        return user_data, tokens

    def login(self, email: str, password: str) -> Tuple[Dict[str, Any], TokenResponse]:
        """
        Login user with email and password

        Args:
            email: User email
            password: User password

        Returns:
            Tuple of (user_data, tokens)

        Raises:
            ValueError: For invalid credentials or locked account
            Exception: For other errors
        """
        # Get user from Firebase Auth
        try:
            user_record = auth.get_user_by_email(email)
        except auth.UserNotFoundError:
            raise ValueError('Invalid email or password')

        # Get user from Firestore
        user_doc = self.db.collection('users').document(user_record.uid).get()
        if not user_doc.exists:
            raise ValueError('User profile not found')

        user_data = user_doc.to_dict()

        # Check if account is locked
        if user_data.get('lockedUntil'):
            locked_until = user_data['lockedUntil']
            if isinstance(locked_until, datetime) and locked_until > datetime.utcnow():
                remaining = int((locked_until - datetime.utcnow()).total_seconds() / 60)
                raise ValueError(
                    f'Account locked due to too many failed login attempts. '
                    f'Try again in {remaining} minutes.'
                )
            else:
                # Lock expired, reset counter
                self.db.collection('users').document(user_record.uid).update({
                    'lockedUntil': None,
                    'failedLoginAttempts': 0,
                })

        # TODO: CRITICAL - Implement password verification
        # SECURITY WARNING: Currently accepts ANY password! Authentication is BROKEN!
        #
        # Firebase Admin SDK doesn't provide password verification.
        # Solutions:
        # 1. Use Firebase Auth REST API signInWithPassword endpoint
        #    https://firebase.google.com/docs/reference/rest/auth#section-sign-in-email-password
        # 2. Use firebase-admin's auth.generate_sign_in_with_email_link()
        # 3. Use custom token approach with Firebase Client SDK
        #
        # Recommended: Use REST API signInWithPassword for direct password verification
        #
        # MUST increment failedLoginAttempts on wrong password and implement lockout!

        # Reset failed attempts on successful login
        self.db.collection('users').document(user_record.uid).update({
            'failedLoginAttempts': 0,
            'lastLoginAt': datetime.utcnow(),
            'updatedAt': datetime.utcnow(),
        })

        # Generate tokens
        tokens = self.generate_tokens(user_record.uid)

        # Update user data with latest login time
        user_data['lastLoginAt'] = datetime.utcnow()

        return user_data, tokens

    def google_login(self, id_token: str) -> Tuple[Dict[str, Any], TokenResponse]:
        """
        Login or register user with Google OAuth

        Args:
            id_token: Google ID token

        Returns:
            Tuple of (user_data, tokens)
        """
        # Verify Google ID token
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token.get('email')
        name = decoded_token.get('name')
        picture = decoded_token.get('picture')

        # Check if user exists
        user_doc = self.db.collection('users').document(uid).get()

        if not user_doc.exists:
            # Create new user
            now = datetime.utcnow()
            user_data = {
                'id': uid,
                'email': email,
                'emailVerified': True,  # Google email is already verified
                'profile': {
                    'displayName': name,
                    'photoURL': picture,
                    'phoneNumber': None,
                    'bio': None,
                },
                'tenants': [],
                'status': UserStatus.ACTIVE.value,
                'createdAt': now,
                'updatedAt': now,
                'lastLoginAt': now,
                'failedLoginAttempts': 0,
            }
            self.db.collection('users').document(uid).set(user_data)
        else:
            # Update existing user
            user_data = user_doc.to_dict()
            self.db.collection('users').document(uid).update({
                'lastLoginAt': datetime.utcnow(),
                'updatedAt': datetime.utcnow(),
            })
            user_data['lastLoginAt'] = datetime.utcnow()

        # Generate tokens
        tokens = self.generate_tokens(uid)

        return user_data, tokens

    def generate_tokens(self, user_id: str) -> TokenResponse:
        """
        Generate JWT access and refresh tokens

        Args:
            user_id: User ID

        Returns:
            TokenResponse with access and refresh tokens
        """
        now = datetime.utcnow()

        # Generate access token
        access_payload = {
            'user_id': user_id,
            'type': 'access',
            'exp': now + timedelta(seconds=self.access_token_expiry),
            'iat': now,
        }
        access_token = jwt.encode(access_payload, self.jwt_secret, algorithm=self.jwt_algorithm)

        # Generate refresh token
        refresh_payload = {
            'user_id': user_id,
            'type': 'refresh',
            'exp': now + timedelta(seconds=self.refresh_token_expiry),
            'iat': now,
        }
        refresh_token = jwt.encode(refresh_payload, self.jwt_secret, algorithm=self.jwt_algorithm)

        return TokenResponse(
            accessToken=access_token,
            refreshToken=refresh_token,
            expiresIn=self.access_token_expiry,
        )

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Verify JWT token and return payload

        Args:
            token: JWT token

        Returns:
            Token payload if valid, None otherwise
        """
        try:
            payload = jwt.decode(token, self.jwt_secret, algorithms=[self.jwt_algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def refresh_access_token(self, refresh_token: str) -> TokenResponse:
        """
        Refresh access token using refresh token

        Args:
            refresh_token: JWT refresh token

        Returns:
            New TokenResponse

        Raises:
            ValueError: If refresh token is invalid
        """
        payload = self.verify_token(refresh_token)
        if not payload or payload.get('type') != 'refresh':
            raise ValueError('Invalid refresh token')

        user_id = payload.get('user_id')
        if not user_id:
            raise ValueError('Invalid refresh token')

        # Generate new tokens
        return self.generate_tokens(user_id)

    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Get user by ID

        Args:
            user_id: User ID

        Returns:
            User data dict or None
        """
        user_doc = self.db.collection('users').document(user_id).get()
        if not user_doc.exists:
            return None

        user_data = user_doc.to_dict()
        user_data['id'] = user_doc.id
        return user_data

    def update_profile(
        self, user_id: str, updates: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update user profile

        Args:
            user_id: User ID
            updates: Profile fields to update

        Returns:
            Updated user data
        """
        # Get current profile
        user_doc = self.db.collection('users').document(user_id).get()
        if not user_doc.exists:
            raise ValueError('User not found')

        current_profile = user_doc.to_dict().get('profile', {})

        # Merge updates
        updated_profile = {**current_profile, **updates}

        # Update in Firestore
        self.db.collection('users').document(user_id).update({
            'profile': updated_profile,
            'updatedAt': datetime.utcnow(),
        })

        # Return updated user
        return self.get_user(user_id)

    def send_verification_email(self, user_id: str, email: str) -> bool:
        """
        Send email verification link to user

        Args:
            user_id: User ID
            email: User email

        Returns:
            True if email sent successfully
        """
        # TODO: Implement email sending with Firebase or SMTP
        # Generate verification token
        verification_token = secrets.token_urlsafe(32)
        expiry = datetime.utcnow() + timedelta(hours=24)

        # Store token in Firestore
        self.db.collection('users').document(user_id).update({
            'emailVerificationToken': verification_token,
            'emailVerificationExpires': expiry,
        })

        # TODO: Send email with verification link
        # verification_link = f"https://yourdomain.com/verify-email?token={verification_token}"
        # send_email(to=email, subject="Verify your email", body=f"Click here: {verification_link}")

        print(f"📧 Verification email would be sent to {email}")
        print(f"   Token: {verification_token}")
        return True

    def resend_verification_email(self, user_id: str) -> bool:
        """
        Resend verification email (rate limited)

        Args:
            user_id: User ID

        Returns:
            True if email sent

        Raises:
            ValueError: If rate limit exceeded
        """
        user = self.get_user(user_id)
        if not user:
            raise ValueError('User not found')

        # TODO: Implement rate limiting (max 3 per hour)
        # For now, just send
        return self.send_verification_email(user_id, user['email'])

    def verify_email(self, token: str) -> bool:
        """
        Verify email with token

        Args:
            token: Verification token

        Returns:
            True if verified successfully

        Raises:
            ValueError: If token invalid or expired
        """
        # Find user by token
        users_ref = self.db.collection('users')
        query = users_ref.where('emailVerificationToken', '==', token).limit(1)
        users = list(query.stream())

        if not users:
            raise ValueError('Invalid verification token')

        user_doc = users[0]
        user_data = user_doc.to_dict()

        # Check expiry
        expires = user_data.get('emailVerificationExpires')
        if expires and expires < datetime.utcnow():
            raise ValueError('Verification token expired')

        # Update user
        self.db.collection('users').document(user_doc.id).update({
            'emailVerified': True,
            'emailVerificationToken': None,
            'emailVerificationExpires': None,
            'updatedAt': datetime.utcnow(),
        })

        # Update Firebase Auth
        auth.update_user(user_doc.id, email_verified=True)

        return True

    def send_password_reset_email(self, email: str) -> bool:
        """
        Send password reset email

        Args:
            email: User email

        Returns:
            True if email sent (or user not found - don't reveal)
        """
        try:
            user_record = auth.get_user_by_email(email)
        except auth.UserNotFoundError:
            # Don't reveal if user exists
            return True

        # Generate reset token
        reset_token = secrets.token_urlsafe(32)
        expiry = datetime.utcnow() + timedelta(hours=1)

        # Store token
        self.db.collection('users').document(user_record.uid).update({
            'passwordResetToken': reset_token,
            'passwordResetExpires': expiry,
        })

        # TODO: Send email with reset link
        # reset_link = f"https://yourdomain.com/reset-password?token={reset_token}"
        # send_email(to=email, subject="Reset your password", body=f"Click here: {reset_link}")

        print(f"📧 Password reset email would be sent to {email}")
        print(f"   Token: {reset_token}")
        return True

    def reset_password(self, token: str, new_password: str) -> bool:
        """
        Reset password with token

        Args:
            token: Reset token
            new_password: New password

        Returns:
            True if reset successful

        Raises:
            ValueError: If token invalid or expired
        """
        # Find user by token
        users_ref = self.db.collection('users')
        query = users_ref.where('passwordResetToken', '==', token).limit(1)
        users = list(query.stream())

        if not users:
            raise ValueError('Invalid reset token')

        user_doc = users[0]
        user_data = user_doc.to_dict()

        # Check expiry
        expires = user_data.get('passwordResetExpires')
        if expires and expires < datetime.utcnow():
            raise ValueError('Reset token expired')

        # Update password in Firebase Auth
        auth.update_user(user_doc.id, password=new_password)

        # Clear reset token and invalidate sessions
        self.db.collection('users').document(user_doc.id).update({
            'passwordResetToken': None,
            'passwordResetExpires': None,
            'updatedAt': datetime.utcnow(),
        })

        # TODO: Send confirmation email
        # send_email(to=user_data['email'], subject="Password changed", body="Your password was reset")

        return True

    def delete_account(self, user_id: str, password: str) -> bool:
        """
        Delete user account

        Args:
            user_id: User ID
            password: Password for confirmation

        Returns:
            True if deleted

        Raises:
            ValueError: If cannot delete (ownership transfer required)
        """
        # Get user
        user = self.get_user(user_id)
        if not user:
            raise ValueError('User not found')

        # Check if user owns any tenants
        tenants = user.get('tenants', [])
        for tenant_member in tenants:
            # TODO: Get role details to check if owner
            role_id = tenant_member.get('roleId')
            if role_id == 'owner':  # System role ID
                raise ValueError(
                    'Cannot delete account. Please transfer store ownership first.'
                )

        # TODO: CRITICAL - Verify password before deletion
        # SECURITY WARNING: Currently accepts ANY password!
        # Use same password verification method as login (Firebase REST API)
        # See login() method TODO for implementation details

        # Soft delete in Firestore
        self.db.collection('users').document(user_id).update({
            'status': UserStatus.INACTIVE.value,
            'deletedAt': datetime.utcnow(),
            'updatedAt': datetime.utcnow(),
        })

        # Delete from Firebase Auth
        # auth.delete_user(user_id)  # Uncomment for hard delete

        # TODO: Send confirmation email

        return True

    def logout(self, user_id: str, token: str) -> bool:
        """
        Logout user and revoke token

        Args:
            user_id: User ID
            token: Access token to revoke

        Returns:
            True if logged out
        """
        # TODO: Implement token blacklist
        # For now, tokens will expire naturally
        # In production, use Redis or Firestore to store blacklisted tokens

        return True


# Singleton instance
_auth_service_instance = None


def get_auth_service() -> AuthService:
    """Get or create AuthService singleton"""
    global _auth_service_instance
    if _auth_service_instance is None:
        _auth_service_instance = AuthService()
    return _auth_service_instance
