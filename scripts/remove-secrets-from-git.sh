#!/bin/bash

# ==============================================================================
# Emergency: Remove Secrets from Git History
# ==============================================================================
#
# This script helps remove sensitive files from git history using BFG.
#
# ⚠️ WARNING: This script will rewrite git history!
# - Coordinate with your team before running
# - All team members will need to re-clone the repository
# - Make a backup before running
#
# Usage:
#   ./scripts/remove-secrets-from-git.sh
#
# ==============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_error() {
    echo -e "${RED}❌ ERROR: $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  WARNING: $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Function to ask for confirmation
confirm() {
    read -p "$(echo -e ${YELLOW}$1${NC}) [y/N]: " -n 1 -r
    echo
    [[ $REPLY =~ ^[Yy]$ ]]
}

# ==============================================================================
# Pre-flight Checks
# ==============================================================================

print_info "Starting secret removal process..."
echo

# Check if BFG is installed
if ! command -v bfg &> /dev/null; then
    print_error "BFG Repo-Cleaner is not installed!"
    echo
    echo "Install with:"
    echo "  macOS:  brew install bfg"
    echo "  Other:  Download from https://rtyley.github.io/bfg-repo-cleaner/"
    exit 1
fi

print_success "BFG Repo-Cleaner is installed"

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not in a git repository!"
    exit 1
fi

print_success "Git repository detected"

# Get repository info
REPO_ROOT=$(git rev-parse --show-toplevel)
REPO_NAME=$(basename "$REPO_ROOT")
REMOTE_URL=$(git config --get remote.origin.url || echo "none")

echo
print_info "Repository: $REPO_NAME"
print_info "Location: $REPO_ROOT"
print_info "Remote: $REMOTE_URL"
echo

# ==============================================================================
# Safety Checks and Warnings
# ==============================================================================

print_warning "THIS WILL REWRITE GIT HISTORY!"
echo
echo "Before proceeding, ensure:"
echo "  1. ✅ You have rotated/invalidated all compromised credentials"
echo "  2. ✅ You have notified your team"
echo "  3. ✅ No one is currently working on the repository"
echo "  4. ✅ You have a backup of the repository"
echo

if ! confirm "Have you completed all the above steps?"; then
    print_error "Aborted. Complete the safety checks first."
    echo
    echo "See docs/REMOVE_SECRETS_FROM_GIT.md for detailed instructions."
    exit 1
fi

echo

# ==============================================================================
# Create Backup
# ==============================================================================

print_info "Creating backup..."

BACKUP_DIR="$HOME/git-backups"
BACKUP_NAME="${REPO_NAME}-backup-$(date +%Y%m%d-%H%M%S)"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_NAME"

mkdir -p "$BACKUP_DIR"

if git clone "$REPO_ROOT" "$BACKUP_PATH" 2>/dev/null; then
    print_success "Backup created: $BACKUP_PATH"
else
    print_error "Failed to create backup"
    exit 1
fi

echo

# ==============================================================================
# Files to Remove
# ==============================================================================

print_info "Specify files to remove from history..."
echo

# Default files to remove
FILES_TO_REMOVE=(
    ".env"
    ".env.local"
    ".env.development"
    ".env.staging"
    ".env.production"
    "serviceAccountKey.json"
)

echo "Default files to remove:"
for file in "${FILES_TO_REMOVE[@]}"; do
    echo "  - $file"
done
echo

if confirm "Add more files to remove?"; then
    echo
    echo "Enter file names (one per line, empty line to finish):"
    while true; do
        read -p "> " filename
        if [ -z "$filename" ]; then
            break
        fi
        FILES_TO_REMOVE+=("$filename")
    done
fi

echo
print_info "Files to remove from history:"
for file in "${FILES_TO_REMOVE[@]}"; do
    echo "  - $file"
done
echo

if ! confirm "Proceed with removing these files?"; then
    print_error "Aborted by user"
    exit 1
fi

echo

# ==============================================================================
# Create Mirror Clone for BFG
# ==============================================================================

print_info "Creating mirror clone for BFG..."

TEMP_DIR=$(mktemp -d)
MIRROR_PATH="$TEMP_DIR/${REPO_NAME}.git"

if git clone --mirror "$REPO_ROOT" "$MIRROR_PATH" 2>/dev/null; then
    print_success "Mirror clone created: $MIRROR_PATH"
else
    print_error "Failed to create mirror clone"
    rm -rf "$TEMP_DIR"
    exit 1
fi

cd "$MIRROR_PATH"
echo

# ==============================================================================
# Run BFG to Remove Files
# ==============================================================================

print_info "Running BFG Repo-Cleaner..."
echo

for file in "${FILES_TO_REMOVE[@]}"; do
    print_info "Removing: $file"
    if bfg --delete-files "$file" --no-blob-protection .; then
        print_success "Removed: $file"
    else
        print_warning "File not found in history: $file"
    fi
done

echo

# ==============================================================================
# Clean Up Repository
# ==============================================================================

print_info "Cleaning up repository..."

git reflog expire --expire=now --all
git gc --prune=now --aggressive

print_success "Repository cleaned"
echo

# ==============================================================================
# Verify Removal
# ==============================================================================

print_info "Verifying files are removed..."
echo

VERIFICATION_FAILED=false

for file in "${FILES_TO_REMOVE[@]}"; do
    if git log --all --full-history -- "$file" 2>/dev/null | grep -q "commit"; then
        print_error "File still in history: $file"
        VERIFICATION_FAILED=true
    else
        print_success "Verified removed: $file"
    fi
done

echo

if [ "$VERIFICATION_FAILED" = true ]; then
    print_error "Some files were not completely removed!"
    print_warning "Check manually before force pushing."
    cd "$REPO_ROOT"
    rm -rf "$TEMP_DIR"
    exit 1
fi

print_success "All files verified removed from history!"
echo

# ==============================================================================
# Force Push
# ==============================================================================

print_warning "Ready to force push to remote"
echo
echo "This will:"
echo "  1. Overwrite the remote repository history"
echo "  2. Require all team members to re-clone"
echo "  3. Cannot be undone easily"
echo

if confirm "Force push to remote NOW?"; then
    print_info "Force pushing..."

    if git push --force --all && git push --force --tags; then
        print_success "Force push completed!"
    else
        print_error "Force push failed!"
        print_info "You can manually push from: $MIRROR_PATH"
        cd "$REPO_ROOT"
        exit 1
    fi
else
    print_info "Skipped force push"
    print_info "You can manually force push from: $MIRROR_PATH"
    print_info "Run: cd $MIRROR_PATH && git push --force --all"
fi

echo

# ==============================================================================
# Cleanup and Final Instructions
# ==============================================================================

cd "$REPO_ROOT"

print_info "Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

echo
print_success "===== SECRET REMOVAL COMPLETE ====="
echo
echo "Next steps:"
echo
echo "1. Verify removal in your repository:"
echo "   cd $REPO_ROOT"
echo "   git fetch --all"
echo "   git log --all --full-history -- .env"
echo
echo "2. Team members must re-clone:"
echo "   rm -rf pos_app_v1"
echo "   git clone $REMOTE_URL"
echo
echo "3. Update .env.local with NEW rotated credentials"
echo
echo "4. Document this incident for future reference"
echo
print_warning "Backup location: $BACKUP_PATH"
print_warning "Keep this backup until you're sure everything works!"
echo
