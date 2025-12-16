"""
Role models for dynamic role-based access control (RBAC)
Mirrors Zod schemas from @toko/shared-types/src/schemas/role.ts
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any, Literal
from datetime import datetime
from enum import Enum


# System Role IDs (constants)
class SystemRoleID:
    SUPER_ADMIN = "super_admin"
    OWNER = "owner"
    MEMBER = "member"


# Role Level Constants
class RoleLevel:
    SUPER_ADMIN = 100
    OWNER = 90
    ADMIN = 70
    MANAGER = 50
    STAFF = 30
    VIEWER = 10


# User Permissions Schema (mirrors TypeScript UserPermissions)
class UserPermissions(BaseModel):
    # Products
    canCreateProducts: bool = False
    canEditProducts: bool = False
    canDeleteProducts: bool = False
    canViewProducts: bool = True

    # Orders/Sales
    canCreateOrders: bool = False
    canEditOrders: bool = False
    canDeleteOrders: bool = False
    canViewOrders: bool = True
    canRefundOrders: bool = False

    # Customers
    canManageCustomers: bool = False
    canViewCustomers: bool = True

    # Inventory
    canManageInventory: bool = False
    canViewInventory: bool = True

    # Reports
    canViewReports: bool = False
    canExportReports: bool = False

    # Settings
    canManageSettings: bool = False
    canManageUsers: bool = False
    canManagePayments: bool = False

    class Config:
        # Allow field names to use camelCase (matching TypeScript)
        populate_by_name = True


# System Role Schema (static, read-only)
class SystemRole(BaseModel):
    id: str  # 'super_admin', 'owner', 'member'
    name: str
    description: str
    level: int = Field(ge=90, le=100, description="System roles are level 90+")
    permissions: UserPermissions
    isSystemRole: Literal[True] = True
    isActive: bool = True
    createdAt: datetime
    updatedAt: datetime

    class Config:
        populate_by_name = True


# Tenant Role Schema (dynamic, tenant-specific)
class TenantRole(BaseModel):
    id: str  # UUID
    tenantId: str  # UUID
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

    # Hierarchy
    level: int = Field(ge=1, le=89, description="Custom roles are level 1-89")
    inheritsFrom: Optional[str] = None  # Parent role ID

    # Permissions
    permissions: UserPermissions

    # Metadata
    isCustom: Literal[True] = True
    isActive: bool = True
    createdBy: str  # User ID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        populate_by_name = True

    @validator('level')
    def validate_level(cls, v):
        if v < 1 or v > 89:
            raise ValueError('Custom role level must be between 1 and 89')
        return v


# Create Tenant Role Input
class CreateTenantRoleInput(BaseModel):
    tenantId: str
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    level: int = Field(ge=1, le=89)
    inheritsFrom: Optional[str] = None
    permissions: UserPermissions

    class Config:
        populate_by_name = True

    @validator('level')
    def validate_level(cls, v):
        if v < 1 or v > 89:
            raise ValueError('Custom role level must be between 1 and 89')
        return v


# Update Tenant Role Input
class UpdateTenantRoleInput(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    level: Optional[int] = Field(None, ge=1, le=89)
    inheritsFrom: Optional[str] = None
    permissions: Optional[Dict[str, bool]] = None  # Partial permissions
    isActive: Optional[bool] = None

    class Config:
        populate_by_name = True

    @validator('level')
    def validate_level(cls, v):
        if v is not None and (v < 1 or v > 89):
            raise ValueError('Custom role level must be between 1 and 89')
        return v


# Role Query Schema
class RoleQuery(BaseModel):
    tenantId: str
    isCustom: Optional[bool] = None
    isActive: Optional[bool] = None
    minLevel: Optional[int] = Field(None, ge=1, le=100)
    maxLevel: Optional[int] = Field(None, ge=1, le=100)
    search: Optional[str] = None  # Search by name or description
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=20, ge=1, le=100)

    class Config:
        populate_by_name = True


# Clone Role Input
class CloneRoleInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    tenantId: str

    class Config:
        populate_by_name = True


# Helper function to get default permissions by system role ID
def get_default_permissions_by_system_role(role_id: str) -> UserPermissions:
    """Get default permissions for system roles"""

    all_permissions = UserPermissions(
        canCreateProducts=True,
        canEditProducts=True,
        canDeleteProducts=True,
        canViewProducts=True,
        canCreateOrders=True,
        canEditOrders=True,
        canDeleteOrders=True,
        canViewOrders=True,
        canRefundOrders=True,
        canManageCustomers=True,
        canViewCustomers=True,
        canManageInventory=True,
        canViewInventory=True,
        canViewReports=True,
        canExportReports=True,
        canManageSettings=True,
        canManageUsers=True,
        canManagePayments=True,
    )

    base_permissions = UserPermissions(
        canViewProducts=True,
        canViewOrders=True,
        canViewCustomers=True,
        canViewInventory=True,
    )

    if role_id in [SystemRoleID.SUPER_ADMIN, SystemRoleID.OWNER]:
        return all_permissions
    elif role_id == SystemRoleID.MEMBER:
        return base_permissions
    else:
        return base_permissions


# Helper function to merge permissions
def merge_permissions(parent: UserPermissions, child: Dict[str, bool]) -> UserPermissions:
    """Merge parent permissions with child overrides"""
    parent_dict = parent.dict()
    merged = {**parent_dict, **child}
    return UserPermissions(**merged)


# Helper function to check permission by level
def has_permission_by_level(user_level: int, required_level: int) -> bool:
    """Check if user level meets required level (higher = more authority)"""
    return user_level >= required_level


# Default System Roles (seed data)
DEFAULT_SYSTEM_ROLES = [
    {
        "id": SystemRoleID.SUPER_ADMIN,
        "name": "Super Admin",
        "description": "Platform administrator with full access to all tenants and system settings",
        "level": RoleLevel.SUPER_ADMIN,
        "permissions": get_default_permissions_by_system_role(SystemRoleID.SUPER_ADMIN).dict(),
        "isSystemRole": True,
        "isActive": True,
    },
    {
        "id": SystemRoleID.OWNER,
        "name": "Owner",
        "description": "Tenant owner with full access to all tenant features and settings",
        "level": RoleLevel.OWNER,
        "permissions": get_default_permissions_by_system_role(SystemRoleID.OWNER).dict(),
        "isSystemRole": True,
        "isActive": True,
    },
    {
        "id": SystemRoleID.MEMBER,
        "name": "Member",
        "description": "Basic tenant member with view-only access",
        "level": RoleLevel.VIEWER,
        "permissions": get_default_permissions_by_system_role(SystemRoleID.MEMBER).dict(),
        "isSystemRole": True,
        "isActive": True,
    },
]


# Role Templates (starting points for custom roles)
ROLE_TEMPLATES = {
    "ADMIN": {
        "name": "Admin",
        "description": "Administrator with most permissions except ownership transfer",
        "level": RoleLevel.ADMIN,
        "permissions": UserPermissions(
            canCreateProducts=True,
            canEditProducts=True,
            canDeleteProducts=True,
            canViewProducts=True,
            canCreateOrders=True,
            canEditOrders=True,
            canDeleteOrders=True,
            canViewOrders=True,
            canRefundOrders=True,
            canManageCustomers=True,
            canViewCustomers=True,
            canManageInventory=True,
            canViewInventory=True,
            canViewReports=True,
            canExportReports=True,
            canManageUsers=True,
        ).dict(),
    },
    "MANAGER": {
        "name": "Manager",
        "description": "Store manager with product and order management permissions",
        "level": RoleLevel.MANAGER,
        "permissions": UserPermissions(
            canCreateProducts=True,
            canEditProducts=True,
            canViewProducts=True,
            canCreateOrders=True,
            canEditOrders=True,
            canViewOrders=True,
            canManageCustomers=True,
            canViewCustomers=True,
            canManageInventory=True,
            canViewInventory=True,
            canViewReports=True,
        ).dict(),
    },
    "CASHIER": {
        "name": "Cashier",
        "description": "Cashier with order creation and basic customer management",
        "level": RoleLevel.STAFF,
        "permissions": UserPermissions(
            canViewProducts=True,
            canCreateOrders=True,
            canEditOrders=True,
            canViewOrders=True,
            canManageCustomers=True,
            canViewCustomers=True,
        ).dict(),
    },
    "INVENTORY_MANAGER": {
        "name": "Inventory Manager",
        "description": "Specialized role for inventory and product management",
        "level": RoleLevel.STAFF,
        "permissions": UserPermissions(
            canCreateProducts=True,
            canEditProducts=True,
            canViewProducts=True,
            canManageInventory=True,
            canViewInventory=True,
            canViewReports=True,
        ).dict(),
    },
}
