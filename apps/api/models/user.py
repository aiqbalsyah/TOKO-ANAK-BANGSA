"""
User models for authentication and profile management
Mirrors Zod schemas from @toko/shared-types/src/schemas/user.ts
Uses dynamic roleId references instead of hardcoded role enums
"""

from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


# User Status
class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


# User Profile
class UserProfile(BaseModel):
    displayName: str = Field(..., min_length=1, description="User's display name")
    photoURL: Optional[str] = Field(None, description="Profile picture URL")
    phoneNumber: Optional[str] = Field(None, min_length=10, description="Phone number")
    bio: Optional[str] = Field(None, max_length=500, description="User bio")

    class Config:
        populate_by_name = True


# Tenant Member (User's role assignment within a tenant)
# Uses roleId reference instead of hardcoded enum
class TenantMember(BaseModel):
    tenantId: str = Field(..., description="Tenant UUID")
    userId: str = Field(..., description="User ID")
    roleId: str = Field(..., description="Role ID (references system_roles or tenant_roles)")

    # Optional permission overrides for this specific user
    customPermissions: Optional[dict] = Field(
        None, description="Custom permission overrides for this user"
    )

    # Metadata
    joinedAt: datetime = Field(..., description="When user joined tenant")
    assignedBy: Optional[str] = Field(None, description="User ID who assigned this role")
    status: UserStatus = Field(default=UserStatus.ACTIVE, description="Member status")
    expiresAt: Optional[datetime] = Field(None, description="Optional role expiration")

    class Config:
        populate_by_name = True
        use_enum_values = True


# User Schema
class User(BaseModel):
    id: str = Field(..., description="Firebase Auth UID")
    email: EmailStr = Field(..., description="User email")
    emailVerified: bool = Field(default=False, description="Email verification status")
    profile: UserProfile = Field(..., description="User profile data")

    # Multi-tenant memberships with role references
    tenants: List[TenantMember] = Field(
        default=[], description="List of tenant memberships"
    )

    # Platform-level status
    status: UserStatus = Field(default=UserStatus.ACTIVE, description="Account status")

    # Timestamps
    createdAt: datetime = Field(..., description="Account creation time")
    updatedAt: datetime = Field(..., description="Last update time")
    lastLoginAt: Optional[datetime] = Field(None, description="Last login time")

    # Security fields (optional, for tracking)
    failedLoginAttempts: int = Field(default=0, description="Failed login counter")
    lockedUntil: Optional[datetime] = Field(None, description="Account lock expiration")

    class Config:
        populate_by_name = True
        use_enum_values = True


# Registration Request
class RegisterRequest(BaseModel):
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    displayName: str = Field(..., min_length=1, description="Display name")
    phoneNumber: Optional[str] = Field(None, description="Phone number (optional)")

    @validator('password')
    def validate_password_strength(cls, v):
        """Validate password meets strength requirements"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v

    class Config:
        populate_by_name = True


# Login Request
class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., description="User password")

    class Config:
        populate_by_name = True


# Google OAuth Request
class GoogleAuthRequest(BaseModel):
    idToken: str = Field(..., description="Google ID token")

    class Config:
        populate_by_name = True


# Update Profile Request
class UpdateProfileRequest(BaseModel):
    displayName: Optional[str] = Field(None, min_length=1)
    phoneNumber: Optional[str] = Field(None, min_length=10)
    photoURL: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=500)

    class Config:
        populate_by_name = True


# Forgot Password Request
class ForgotPasswordRequest(BaseModel):
    email: EmailStr = Field(..., description="User email")

    class Config:
        populate_by_name = True


# Reset Password Request
class ResetPasswordRequest(BaseModel):
    token: str = Field(..., description="Password reset token")
    newPassword: str = Field(..., min_length=8, description="New password")

    @validator('newPassword')
    def validate_password_strength(cls, v):
        """Validate new password meets strength requirements"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v

    class Config:
        populate_by_name = True


# Verify Email Request
class VerifyEmailRequest(BaseModel):
    token: str = Field(..., description="Email verification token")

    class Config:
        populate_by_name = True


# Refresh Token Request
class RefreshTokenRequest(BaseModel):
    refreshToken: str = Field(..., description="JWT refresh token")

    class Config:
        populate_by_name = True


# Delete Account Request
class DeleteAccountRequest(BaseModel):
    password: str = Field(..., description="Current password for confirmation")

    class Config:
        populate_by_name = True


# Invite User to Tenant Input
class InviteUserInput(BaseModel):
    email: EmailStr = Field(..., description="User email to invite")
    roleId: str = Field(..., description="Role ID to assign")
    customPermissions: Optional[dict] = Field(None, description="Custom permission overrides")
    expiresAt: Optional[datetime] = Field(None, description="Optional role expiration")

    class Config:
        populate_by_name = True


# Update Tenant Member Input
class UpdateTenantMemberInput(BaseModel):
    roleId: Optional[str] = Field(None, description="New role ID")
    customPermissions: Optional[dict] = Field(None, description="Custom permission overrides")
    status: Optional[UserStatus] = Field(None, description="Member status")
    expiresAt: Optional[datetime] = Field(None, description="Role expiration")

    class Config:
        populate_by_name = True
        use_enum_values = True


# Token Response
class TokenResponse(BaseModel):
    accessToken: str = Field(..., description="JWT access token")
    refreshToken: str = Field(..., description="JWT refresh token")
    expiresIn: int = Field(..., description="Token expiry in seconds")

    class Config:
        populate_by_name = True


# Auth Response (includes user and tokens)
class AuthResponse(BaseModel):
    user: User = Field(..., description="User data")
    tokens: TokenResponse = Field(..., description="Auth tokens")

    class Config:
        populate_by_name = True


# API Response wrapper
class ApiResponse(BaseModel):
    success: bool = Field(..., description="Request success status")
    data: Optional[dict] = Field(None, description="Response data")
    error: Optional[str] = Field(None, description="Error message if failed")

    class Config:
        populate_by_name = True
