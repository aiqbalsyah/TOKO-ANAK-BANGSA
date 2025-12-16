"""
Role Management Routes
Handles role CRUD operations, templates, cloning, and user assignments
"""

from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from models.role import (
    CreateTenantRoleInput,
    UpdateTenantRoleInput,
    RoleQuery,
    CloneRoleInput,
)
from services.role_service import get_role_service
from middleware.auth import require_auth, require_role_level
from extensions import limiter

# Create Blueprint
roles_bp = Blueprint('roles', __name__, url_prefix='/api/roles')


@roles_bp.route('', methods=['GET'])
@require_auth
@require_role_level(70)  # Admin level or higher
@limiter.limit("30 per hour")
def list_roles():
    """
    List all roles for tenant (system + custom)

    Query Parameters:
    - tenantId (required): UUID of tenant
    - isCustom (optional): Filter by custom/system roles
    - isActive (optional): Filter by active status
    - minLevel (optional): Minimum role level
    - maxLevel (optional): Maximum role level
    - search (optional): Search name/description
    - page (optional): Page number (default: 1)
    - limit (optional): Items per page (default: 20)

    Returns:
    - 200: List of roles with pagination
    - 400: Invalid query parameters
    - 401: Unauthorized
    - 403: Insufficient permissions
    """
    try:
        # Parse query parameters
        tenant_id = request.args.get('tenantId')
        if not tenant_id:
            return jsonify({'success': False, 'error': 'tenantId is required'}), 400

        # Build filters
        filters = {
            'isCustom': request.args.get('isCustom', type=lambda v: v.lower() == 'true') if request.args.get('isCustom') else None,
            'isActive': request.args.get('isActive', type=lambda v: v.lower() == 'true') if request.args.get('isActive') else None,
            'minLevel': request.args.get('minLevel', type=int),
            'maxLevel': request.args.get('maxLevel', type=int),
            'search': request.args.get('search'),
            'page': request.args.get('page', default=1, type=int),
            'limit': request.args.get('limit', default=20, type=int),
        }

        # Get role service
        role_service = get_role_service()

        # List roles
        roles = role_service.list_roles(tenant_id, filters)

        # Apply pagination
        page = filters['page']
        limit = filters['limit']
        start = (page - 1) * limit
        end = start + limit

        paginated_roles = roles[start:end]
        total = len(roles)

        return jsonify({
            'success': True,
            'data': paginated_roles,
            'meta': {
                'total': total,
                'page': page,
                'limit': limit,
                'hasNext': end < total
            }
        }), 200

    except Exception as e:
        print(f"List roles error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('/<role_id>', methods=['GET'])
@require_auth
@limiter.limit("50 per hour")
def get_role(role_id):
    """
    Get role details with effective permissions

    Query Parameters:
    - tenantId (required): UUID of tenant

    Returns:
    - 200: Role details
    - 400: Missing tenantId
    - 401: Unauthorized
    - 403: Cannot access role from different tenant
    - 404: Role not found
    """
    try:
        tenant_id = request.args.get('tenantId')
        if not tenant_id:
            return jsonify({'success': False, 'error': 'tenantId is required'}), 400

        role_service = get_role_service()
        role = role_service.get_role(role_id, tenant_id)

        if not role:
            return jsonify({'success': False, 'error': 'Role not found'}), 404

        return jsonify({'success': True, 'data': role}), 200

    except PermissionError as e:
        return jsonify({'success': False, 'error': str(e)}), 403
    except Exception as e:
        print(f"Get role error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('', methods=['POST'])
@require_auth
@require_role_level(70)  # Admin level or higher
@limiter.limit("10 per hour")
def create_role():
    """
    Create custom role

    Request Body:
    {
      "tenantId": "tenant-uuid",
      "name": "Store Manager",
      "description": "Manages daily operations",
      "level": 50,
      "inheritsFrom": "owner" (optional),
      "permissions": {...}
    }

    Returns:
    - 201: Role created successfully
    - 400: Invalid request data
    - 401: Unauthorized
    - 403: Insufficient permissions
    - 409: Role with this name already exists
    """
    try:
        # Validate request
        data = CreateTenantRoleInput(**request.get_json())

        # Get current user ID from auth middleware
        created_by = request.user_id

        # Create role
        role_service = get_role_service()
        role = role_service.create_role(data.dict(), created_by)

        return jsonify({'success': True, 'data': role}), 201

    except ValidationError as e:
        return jsonify({'success': False, 'error': e.errors()}), 400
    except ValueError as e:
        # Duplicate name or validation error
        return jsonify({'success': False, 'error': str(e)}), 409
    except Exception as e:
        print(f"Create role error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('/<role_id>', methods=['PATCH'])
@require_auth
@require_role_level(70)  # Admin level or higher
@limiter.limit("20 per hour")
def update_role(role_id):
    """
    Update custom role

    Query Parameters:
    - tenantId (required): UUID of tenant

    Request Body:
    {
      "name": "Senior Store Manager" (optional),
      "description": "Updated description" (optional),
      "level": 55 (optional),
      "permissions": {...} (optional),
      "isActive": true (optional)
    }

    Returns:
    - 200: Role updated successfully
    - 400: Invalid request data
    - 401: Unauthorized
    - 403: Cannot modify system roles
    - 404: Role not found
    """
    try:
        tenant_id = request.args.get('tenantId')
        if not tenant_id:
            return jsonify({'success': False, 'error': 'tenantId is required'}), 400

        # Validate request
        data = UpdateTenantRoleInput(**request.get_json())

        # Update role (only include non-None fields)
        updates = {k: v for k, v in data.dict().items() if v is not None}

        role_service = get_role_service()
        role = role_service.update_role(role_id, tenant_id, updates)

        return jsonify({'success': True, 'data': role}), 200

    except ValidationError as e:
        return jsonify({'success': False, 'error': e.errors()}), 400
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 404
    except PermissionError as e:
        return jsonify({'success': False, 'error': str(e)}), 403
    except Exception as e:
        print(f"Update role error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('/<role_id>', methods=['DELETE'])
@require_auth
@require_role_level(90)  # Owner level only
@limiter.limit("5 per hour")
def delete_role(role_id):
    """
    Delete custom role (soft delete)

    Query Parameters:
    - tenantId (required): UUID of tenant

    Returns:
    - 200: Role deleted successfully
    - 400: Missing tenantId
    - 401: Unauthorized
    - 403: Cannot delete system roles or insufficient permissions
    - 404: Role not found
    - 409: Cannot delete role with assigned users
    """
    try:
        tenant_id = request.args.get('tenantId')
        if not tenant_id:
            return jsonify({'success': False, 'error': 'tenantId is required'}), 400

        role_service = get_role_service()
        role_service.delete_role(role_id, tenant_id)

        return jsonify({'success': True, 'message': 'Role deleted successfully'}), 200

    except ValueError as e:
        # Check error message to determine status code
        error_msg = str(e)
        if 'users still have this role' in error_msg:
            return jsonify({'success': False, 'error': error_msg}), 409
        else:
            return jsonify({'success': False, 'error': error_msg}), 404
    except PermissionError as e:
        return jsonify({'success': False, 'error': str(e)}), 403
    except Exception as e:
        print(f"Delete role error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('/templates', methods=['GET'])
@require_auth
@limiter.limit("50 per hour")
def get_role_templates():
    """
    Get predefined role templates

    Returns:
    - 200: List of role templates
    - 401: Unauthorized
    """
    try:
        role_service = get_role_service()
        templates = role_service.get_role_templates()

        return jsonify({'success': True, 'data': templates}), 200

    except Exception as e:
        print(f"Get templates error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('/<role_id>/clone', methods=['POST'])
@require_auth
@require_role_level(70)  # Admin level or higher
@limiter.limit("10 per hour")
def clone_role(role_id):
    """
    Clone existing role

    Request Body:
    {
      "name": "Cloned Store Manager",
      "tenantId": "tenant-uuid"
    }

    Returns:
    - 201: Role cloned successfully
    - 400: Invalid request data
    - 401: Unauthorized
    - 403: Insufficient permissions
    - 404: Source role not found
    - 409: Role with new name already exists
    """
    try:
        # Validate request
        data = CloneRoleInput(**request.get_json())

        # Get current user ID
        cloned_by = request.user_id

        # Clone role
        role_service = get_role_service()
        cloned_role = role_service.clone_role(
            role_id,
            data.name,
            data.tenantId,
            cloned_by
        )

        return jsonify({'success': True, 'data': cloned_role}), 201

    except ValidationError as e:
        return jsonify({'success': False, 'error': e.errors()}), 400
    except ValueError as e:
        error_msg = str(e)
        if 'not found' in error_msg:
            return jsonify({'success': False, 'error': error_msg}), 404
        else:
            return jsonify({'success': False, 'error': error_msg}), 409
    except Exception as e:
        print(f"Clone role error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@roles_bp.route('/<role_id>/users', methods=['GET'])
@require_auth
@require_role_level(70)  # Admin level or higher
@limiter.limit("30 per hour")
def get_users_with_role(role_id):
    """
    Get list of users with specific role

    Query Parameters:
    - tenantId (required): UUID of tenant
    - page (optional): Page number (default: 1)
    - limit (optional): Items per page (default: 20)

    Returns:
    - 200: List of users with this role
    - 400: Missing tenantId
    - 401: Unauthorized
    - 403: Insufficient permissions
    """
    try:
        tenant_id = request.args.get('tenantId')
        if not tenant_id:
            return jsonify({'success': False, 'error': 'tenantId is required'}), 400

        page = request.args.get('page', default=1, type=int)
        limit = request.args.get('limit', default=20, type=int)

        # Get users with role
        role_service = get_role_service()
        users = role_service.get_users_with_role(role_id, tenant_id)

        # Apply pagination
        start = (page - 1) * limit
        end = start + limit

        paginated_users = users[start:end]
        total = len(users)

        return jsonify({
            'success': True,
            'data': paginated_users,
            'meta': {
                'total': total,
                'page': page,
                'limit': limit,
                'hasNext': end < total
            }
        }), 200

    except Exception as e:
        print(f"Get users with role error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
