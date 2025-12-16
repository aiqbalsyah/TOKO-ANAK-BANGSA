"""
Initialize Firestore collections and seed system roles
Run this script once to set up the database structure
"""

import os
import sys
from datetime import datetime

# Add parent directory to path to import models
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from firebase_admin import credentials, firestore, initialize_app
from models.role import DEFAULT_SYSTEM_ROLES


def init_firestore():
    """Initialize Firestore and seed system roles"""

    print("🔥 Initializing Firestore...")

    # Initialize Firebase Admin SDK
    # Note: In production, use GOOGLE_APPLICATION_CREDENTIALS env variable
    # For now, Firebase will auto-detect credentials
    try:
        initialize_app()
        print("✅ Firebase Admin SDK initialized")
    except ValueError:
        # App already initialized
        print("ℹ️  Firebase Admin SDK already initialized")

    db = firestore.client()

    # Create system_roles collection and seed with default roles
    print("\n📦 Seeding system_roles collection...")
    system_roles_ref = db.collection('system_roles')

    roles_created = 0
    roles_updated = 0

    for role_data in DEFAULT_SYSTEM_ROLES:
        role_id = role_data['id']

        # Check if role already exists
        role_doc = system_roles_ref.document(role_id).get()

        # Add timestamps
        now = datetime.utcnow()

        if not role_doc.exists:
            # Create new role
            role_data_with_timestamps = {
                **role_data,
                'createdAt': now,
                'updatedAt': now
            }
            system_roles_ref.document(role_id).set(role_data_with_timestamps)
            print(f"  ✅ Created system role: {role_data['name']} (ID: {role_id})")
            roles_created += 1
        else:
            # Update existing role (preserve createdAt, update the rest)
            existing_data = role_doc.to_dict()
            role_data_with_timestamps = {
                **role_data,
                'createdAt': existing_data.get('createdAt', now),
                'updatedAt': now
            }
            system_roles_ref.document(role_id).set(role_data_with_timestamps)
            print(f"  🔄 Updated system role: {role_data['name']} (ID: {role_id})")
            roles_updated += 1

    print(f"\n✅ System roles seeded: {roles_created} created, {roles_updated} updated")

    # Verify tenant_roles collection exists (will be created on first write)
    print("\n📦 Verifying tenant_roles collection...")
    tenant_roles_ref = db.collection('tenant_roles')

    # Collection will be created automatically when first document is added
    # For now, just verify we can access it
    try:
        # Try to query (won't fail even if empty)
        list(tenant_roles_ref.limit(1).stream())
        print("  ✅ tenant_roles collection ready (will be populated when custom roles are created)")
    except Exception as e:
        print(f"  ⚠️  Error verifying tenant_roles collection: {e}")

    # Verify users collection exists
    print("\n📦 Verifying users collection...")
    users_ref = db.collection('users')

    try:
        list(users_ref.limit(1).stream())
        print("  ✅ users collection ready")
    except Exception as e:
        print(f"  ⚠️  Error verifying users collection: {e}")

    print("\n🎉 Firestore initialization complete!")
    print("\n📋 Collections:")
    print("  - system_roles: ✅ Seeded with 3 default roles")
    print("  - tenant_roles: ✅ Ready for custom roles")
    print("  - users: ✅ Ready for user data")

    return {
        'system_roles_created': roles_created,
        'system_roles_updated': roles_updated,
        'status': 'success'
    }


def verify_firestore_setup():
    """Verify Firestore collections are set up correctly"""

    print("\n🔍 Verifying Firestore setup...")

    try:
        initialize_app()
    except ValueError:
        pass  # Already initialized

    db = firestore.client()

    # Check system_roles
    system_roles = list(db.collection('system_roles').stream())
    print(f"\n📊 System Roles: {len(system_roles)} found")
    for role_doc in system_roles:
        role = role_doc.to_dict()
        print(f"  - {role['name']} (level {role['level']})")

    # Check tenant_roles (should be empty initially)
    tenant_roles = list(db.collection('tenant_roles').limit(5).stream())
    print(f"\n📊 Custom Tenant Roles: {len(tenant_roles)} found")
    if tenant_roles:
        for role_doc in tenant_roles:
            role = role_doc.to_dict()
            print(f"  - {role['name']} (tenant: {role['tenantId']})")
    else:
        print("  (No custom roles yet - will be created by tenants)")

    # Check users
    users = list(db.collection('users').limit(5).stream())
    print(f"\n📊 Users: {len(users)} found")
    if users:
        for user_doc in users:
            user = user_doc.to_dict()
            print(f"  - {user.get('email', 'N/A')}")
    else:
        print("  (No users yet)")

    print("\n✅ Verification complete")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Initialize Firestore collections')
    parser.add_argument('--verify', action='store_true', help='Verify setup instead of initializing')
    args = parser.parse_args()

    if args.verify:
        verify_firestore_setup()
    else:
        result = init_firestore()
        print(f"\n📊 Result: {result}")
