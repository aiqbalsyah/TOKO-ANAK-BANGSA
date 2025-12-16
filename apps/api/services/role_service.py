"""
Role Service - Role lookup, permission resolution, and RBAC logic
Handles both system roles and custom tenant roles
"""

from typing import Optional, List, Dict, Any
from firebase_admin import firestore
from datetime import datetime

from models.role import (
    SystemRole,
    TenantRole,
    UserPermissions,
    get_default_permissions_by_system_role,
    SystemRoleID,
    RoleLevel,
    DEFAULT_SYSTEM_ROLES,
)


class RoleService:
    """Service for managing roles and permissions"""

    def __init__(self):
        self.db = firestore.client()
        self._role_cache = {}  # Simple in-memory cache

    def get_role(self, role_id: str, tenant_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Get role by ID (checks both system and tenant roles)

        Args:
            role_id: Role ID to lookup
            tenant_id: Tenant ID (optional, for validation)

        Returns:
            Role data dict or None if not found
        """
        # Check cache first
        cache_key = f"{role_id}:{tenant_id or 'system'}"
        if cache_key in self._role_cache:
            return self._role_cache[cache_key]

        # Try system roles first
        system_role = self._get_system_role(role_id)
        if system_role:
            self._role_cache[cache_key] = system_role
            return system_role

        # Try tenant roles
        if tenant_id:
            tenant_role = self._get_tenant_role(role_id, tenant_id)
            if tenant_role:
                self._role_cache[cache_key] = tenant_role
                return tenant_role

        return None

    def _get_system_role(self, role_id: str) -> Optional[Dict[str, Any]]:
        """Get system role from Firestore"""
        try:
            doc = self.db.collection('system_roles').document(role_id).get()
            if doc.exists:
                role_data = doc.to_dict()
                role_data['id'] = doc.id
                return role_data
        except Exception as e:
            print(f"Error fetching system role {role_id}: {e}")

        return None

    def _get_tenant_role(self, role_id: str, tenant_id: str) -> Optional[Dict[str, Any]]:
        """Get tenant-specific custom role from Firestore"""
        try:
            doc = self.db.collection('tenant_roles').document(role_id).get()
            if doc.exists:
                role_data = doc.to_dict()

                # Validate tenant ownership
                if role_data.get('tenantId') != tenant_id:
                    raise PermissionError(f"Role {role_id} does not belong to tenant {tenant_id}")

                role_data['id'] = doc.id
                return role_data
        except Exception as e:
            print(f"Error fetching tenant role {role_id}: {e}")
            if isinstance(e, PermissionError):
                raise

        return None

    def get_effective_permissions(self, role_id: str, tenant_id: Optional[str] = None) -> UserPermissions:
        """
        Get effective permissions for a role (includes inherited permissions)

        Args:
            role_id: Role ID
            tenant_id: Tenant ID (optional)

        Returns:
            UserPermissions object with all effective permissions
        """
        role = self.get_role(role_id, tenant_id)
        if not role:
            # Default to basic permissions if role not found
            return UserPermissions()

        # Get base permissions from role
        permissions = UserPermissions(**role['permissions'])

        # If role inherits from another, merge parent permissions
        if role.get('inheritsFrom'):
            parent_permissions = self.get_effective_permissions(
                role['inheritsFrom'], tenant_id
            )
            # Merge: parent permissions + role permissions (role overrides)
            permissions = self._merge_permissions(parent_permissions, permissions)

        return permissions

    def _merge_permissions(
        self, parent: UserPermissions, child: UserPermissions
    ) -> UserPermissions:
        """
        Merge parent and child permissions
        Child permissions override parent (allowing both elevation and restriction)
        """
        parent_dict = parent.dict()
        child_dict = child.dict()

        # Child permissions override parent
        merged = {**parent_dict, **child_dict}

        return UserPermissions(**merged)

    def check_permission(
        self, role_id: str, permission_name: str, tenant_id: Optional[str] = None
    ) -> bool:
        """
        Check if a role has a specific permission

        Args:
            role_id: Role ID
            permission_name: Permission to check (e.g., 'canCreateProducts')
            tenant_id: Tenant ID (optional)

        Returns:
            True if permission granted, False otherwise
        """
        permissions = self.get_effective_permissions(role_id, tenant_id)
        return getattr(permissions, permission_name, False)

    def check_level_permission(self, user_level: int, required_level: int) -> bool:
        """
        Check if user level meets required level
        Higher level = more authority

        Args:
            user_level: User's role level
            required_level: Required minimum level

        Returns:
            True if user level >= required level
        """
        return user_level >= required_level

    def list_roles(
        self, tenant_id: Optional[str] = None, include_system: bool = True
    ) -> List[Dict[str, Any]]:
        """
        List all available roles (system + tenant custom roles)

        Args:
            tenant_id: Tenant ID to filter custom roles (optional)
            include_system: Whether to include system roles

        Returns:
            List of role data dicts
        """
        roles = []

        # Get system roles
        if include_system:
            try:
                system_roles_docs = self.db.collection('system_roles').stream()
                for doc in system_roles_docs:
                    role_data = doc.to_dict()
                    role_data['id'] = doc.id
                    roles.append(role_data)
            except Exception as e:
                print(f"Error listing system roles: {e}")

        # Get tenant roles
        if tenant_id:
            try:
                query = self.db.collection('tenant_roles').where('tenantId', '==', tenant_id)
                tenant_roles_docs = query.stream()

                for doc in tenant_roles_docs:
                    role_data = doc.to_dict()
                    role_data['id'] = doc.id
                    roles.append(role_data)
            except Exception as e:
                print(f"Error listing tenant roles: {e}")

        # Sort by level (descending)
        roles.sort(key=lambda r: r.get('level', 0), reverse=True)

        return roles

    def get_user_role_in_tenant(self, user_id: str, tenant_id: str) -> Optional[Dict[str, Any]]:
        """
        Get user's role assignment in a specific tenant

        Args:
            user_id: User ID
            tenant_id: Tenant ID

        Returns:
            User's role data for the tenant (includes roleId, customPermissions)
        """
        try:
            user_doc = self.db.collection('users').document(user_id).get()
            if not user_doc.exists:
                return None

            user_data = user_doc.to_dict()
            tenants = user_data.get('tenants', [])

            # Find tenant membership
            for tenant_member in tenants:
                if tenant_member.get('tenantId') == tenant_id:
                    return tenant_member

            return None
        except Exception as e:
            print(f"Error getting user role in tenant: {e}")
            return None

    def get_user_effective_permissions(
        self, user_id: str, tenant_id: str
    ) -> Optional[UserPermissions]:
        """
        Get effective permissions for a user in a tenant
        Includes role permissions + user-specific custom permissions

        Args:
            user_id: User ID
            tenant_id: Tenant ID

        Returns:
            UserPermissions object or None if user not in tenant
        """
        tenant_member = self.get_user_role_in_tenant(user_id, tenant_id)
        if not tenant_member:
            return None

        role_id = tenant_member.get('roleId')
        if not role_id:
            return None

        # Get base permissions from role
        role_permissions = self.get_effective_permissions(role_id, tenant_id)

        # Apply user's custom permissions (if any)
        custom_permissions = tenant_member.get('customPermissions', {})
        if custom_permissions:
            # Merge: role permissions + user custom permissions (user overrides)
            merged_dict = {**role_permissions.dict(), **custom_permissions}
            return UserPermissions(**merged_dict)

        return role_permissions

    def can_user_perform(
        self, user_id: str, tenant_id: str, permission_name: str
    ) -> bool:
        """
        Check if user can perform a specific action in a tenant

        Args:
            user_id: User ID
            tenant_id: Tenant ID
            permission_name: Permission to check

        Returns:
            True if user has permission, False otherwise
        """
        permissions = self.get_user_effective_permissions(user_id, tenant_id)
        if not permissions:
            return False

        return getattr(permissions, permission_name, False)

    def get_user_role_level(self, user_id: str, tenant_id: str) -> Optional[int]:
        """
        Get user's role level in a tenant

        Args:
            user_id: User ID
            tenant_id: Tenant ID

        Returns:
            Role level (int) or None
        """
        tenant_member = self.get_user_role_in_tenant(user_id, tenant_id)
        if not tenant_member:
            return None

        role_id = tenant_member.get('roleId')
        if not role_id:
            return None

        role = self.get_role(role_id, tenant_id)
        if not role:
            return None

        return role.get('level')

    def can_user_manage_role(
        self, user_id: str, tenant_id: str, target_role_level: int
    ) -> bool:
        """
        Check if user can manage (create/edit/delete) a role of given level
        Rule: User can only manage roles with lower level than their own

        Args:
            user_id: User ID
            tenant_id: Tenant ID
            target_role_level: Level of the role being managed

        Returns:
            True if user can manage the role, False otherwise
        """
        user_level = self.get_user_role_level(user_id, tenant_id)
        if user_level is None:
            return False

        # User can manage roles with lower level
        return user_level > target_role_level

    def create_role(self, data: dict, created_by: str) -> dict:
        """
        Create custom role

        Args:
            data: Role data (tenantId, name, description, level, permissions, inheritsFrom)
            created_by: User ID of creator

        Returns:
            Created role data

        Raises:
            ValueError: If role name already exists in tenant
        """
        # Validate name is unique within tenant
        existing = self.db.collection('tenant_roles')\
            .where('tenantId', '==', data['tenantId'])\
            .where('name', '==', data['name'])\
            .limit(1)\
            .get()

        if len(list(existing)) > 0:
            raise ValueError('Role with this name already exists in tenant')

        # Validate inheritsFrom if provided
        if data.get('inheritsFrom'):
            parent_role = self.get_role(data['inheritsFrom'], data['tenantId'])
            if not parent_role:
                raise ValueError('Parent role not found')

        # Create role
        role_data = {
            **data,
            'isCustom': True,
            'isActive': True,
            'createdBy': created_by,
            'createdAt': firestore.SERVER_TIMESTAMP,
            'updatedAt': firestore.SERVER_TIMESTAMP
        }

        doc_ref = self.db.collection('tenant_roles').add(role_data)
        role_id = doc_ref[1].id

        # Invalidate cache
        self.clear_cache()

        return {**role_data, 'id': role_id}

    def update_role(self, role_id: str, tenant_id: str, updates: dict) -> dict:
        """
        Update custom role

        Args:
            role_id: Role ID to update
            tenant_id: Tenant ID for validation
            updates: Fields to update

        Returns:
            Updated role data

        Raises:
            ValueError: If role not found
            PermissionError: If trying to update system role
        """
        role = self.get_role(role_id, tenant_id)

        if not role:
            raise ValueError('Role not found')

        if role.get('isSystemRole'):
            raise PermissionError('Cannot modify system roles')

        # Validate name uniqueness if updating name
        if 'name' in updates:
            existing = self.db.collection('tenant_roles')\
                .where('tenantId', '==', tenant_id)\
                .where('name', '==', updates['name'])\
                .limit(1)\
                .get()

            for doc in existing:
                if doc.id != role_id:
                    raise ValueError('Role with this name already exists in tenant')

        # Update
        updates['updatedAt'] = firestore.SERVER_TIMESTAMP
        self.db.collection('tenant_roles').document(role_id).update(updates)

        # Invalidate cache
        self.invalidate_role_cache(role_id)

        return self.get_role(role_id, tenant_id)

    def delete_role(self, role_id: str, tenant_id: str) -> None:
        """
        Delete custom role (soft delete recommended)

        Args:
            role_id: Role ID to delete
            tenant_id: Tenant ID for validation

        Raises:
            ValueError: If role not found or users still have this role
            PermissionError: If trying to delete system role
        """
        role = self.get_role(role_id, tenant_id)

        if not role:
            raise ValueError('Role not found')

        if role.get('isSystemRole'):
            raise PermissionError('Cannot delete system roles')

        # Check if users have this role
        count = self.count_users_with_role(role_id, tenant_id)
        if count > 0:
            raise ValueError(f'Cannot delete role. {count} users still have this role. Please reassign users first.')

        # Soft delete (recommended)
        self.db.collection('tenant_roles').document(role_id).update({
            'isActive': False,
            'updatedAt': firestore.SERVER_TIMESTAMP
        })

        # Invalidate cache
        self.invalidate_role_cache(role_id)

    def clone_role(self, role_id: str, new_name: str, tenant_id: str, cloned_by: str) -> dict:
        """
        Clone existing role

        Args:
            role_id: Source role ID
            new_name: Name for cloned role
            tenant_id: Tenant ID
            cloned_by: User ID of cloner

        Returns:
            Cloned role data

        Raises:
            ValueError: If source role not found
        """
        source_role = self.get_role(role_id, tenant_id)

        if not source_role:
            raise ValueError('Source role not found')

        # Create cloned role
        cloned_data = {
            'tenantId': tenant_id,
            'name': new_name,
            'description': f"Cloned from {source_role.get('name', 'unknown')}",
            'level': source_role['level'] if not source_role.get('isSystemRole') else 50,
            'permissions': source_role['permissions']
        }

        if source_role.get('inheritsFrom'):
            cloned_data['inheritsFrom'] = source_role['inheritsFrom']

        return self.create_role(cloned_data, cloned_by)

    def get_role_templates(self) -> List[dict]:
        """
        Get predefined role templates

        Returns:
            List of role template dictionaries
        """
        from models.role import ROLE_TEMPLATES

        return ROLE_TEMPLATES

    def get_users_with_role(self, role_id: str, tenant_id: str) -> List[dict]:
        """
        Get list of users with specific role

        Args:
            role_id: Role ID
            tenant_id: Tenant ID

        Returns:
            List of users with role assignment details
        """
        users = []
        all_users = self.db.collection('users').stream()

        for user in all_users:
            user_data = user.to_dict()
            for tenant in user_data.get('tenants', []):
                if tenant.get('tenantId') == tenant_id and tenant.get('roleId') == role_id:
                    users.append({
                        'userId': user.id,
                        'email': user_data.get('email'),
                        'profile': user_data.get('profile', {}),
                        'roleAssignment': tenant
                    })
                    break

        return users

    def count_users_with_role(self, role_id: str, tenant_id: str) -> int:
        """
        Count users with specific role

        Args:
            role_id: Role ID
            tenant_id: Tenant ID

        Returns:
            Count of users
        """
        return len(self.get_users_with_role(role_id, tenant_id))

    def clear_cache(self):
        """Clear the role cache"""
        self._role_cache = {}

    def invalidate_role_cache(self, role_id: str):
        """Invalidate cache for a specific role"""
        # Remove all cache entries for this role
        keys_to_remove = [k for k in self._role_cache if k.startswith(f"{role_id}:")]
        for key in keys_to_remove:
            del self._role_cache[key]


# Singleton instance
_role_service_instance = None


def get_role_service() -> RoleService:
    """Get or create RoleService singleton"""
    global _role_service_instance
    if _role_service_instance is None:
        _role_service_instance = RoleService()
    return _role_service_instance
