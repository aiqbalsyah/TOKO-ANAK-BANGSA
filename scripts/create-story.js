#!/usr/bin/env node

/**
 * Create Story Script
 * Creates a new story with todo file and updates sprint status
 * Works on Windows, macOS, and Linux
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { execSync } = require('child_process');

// Config
const SPRINT_STATUS = 'docs/sprint/status.yaml';
const CATEGORIES_FILE = 'docs/sprint/categories.yaml';
const ROOT_TODOS = 'docs/todos';
const API_TODOS = 'apps/api/docs/todos';
const STORE_PORTAL_TODOS = 'apps/store-portal/docs/todos';
const MARKETPLACE_TODOS = 'apps/marketplace/docs/todos';
const COMPANY_PROFILE_TODOS = 'apps/company-profile/docs/todos';
const PLATFORM_ADMIN_TODOS = 'apps/platform-admin/docs/todos';

// Default categories for TOKO ANAK BANGSA
const DEFAULT_CATEGORIES = {
  AUTH: 'Authentication & Authorization',
  POS: 'Point of Sale',
  INVENTORY: 'Inventory Management',
  PRODUCTS: 'Product Management',
  ORDERS: 'Order Management',
  CUSTOMERS: 'Customer Management',
  REPORTS: 'Reports & Analytics',
  MARKETPLACE: 'Marketplace Features',
  STORE: 'Store Management',
  PAYMENTS: 'Payment Integration',
  NOTIFICATIONS: 'Notifications',
  SETTINGS: 'Settings & Configuration',
  ADMIN: 'Platform Admin',
  INFRA: 'Infrastructure & DevOps',
  OTHER: 'Other',
};

// Load categories from file or use defaults
function loadCategories() {
  if (fs.existsSync(CATEGORIES_FILE)) {
    const content = fs.readFileSync(CATEGORIES_FILE, 'utf8');
    const categories = {};
    const lines = content.split('\n');
    for (const line of lines) {
      const match = line.match(/^\s*(\w+):\s*["']?(.+?)["']?\s*$/);
      if (match) {
        categories[match[1]] = match[2];
      }
    }
    return Object.keys(categories).length > 0 ? categories : DEFAULT_CATEGORIES;
  }
  return DEFAULT_CATEGORIES;
}

// Save categories to file
function saveCategories(categories) {
  const dir = path.dirname(CATEGORIES_FILE);
  fs.mkdirSync(dir, { recursive: true });
  let content = '# Story Categories\n# Format: KEY: Description\n\n';
  for (const [key, desc] of Object.entries(categories)) {
    content += `${key}: "${desc}"\n`;
  }
  fs.writeFileSync(CATEGORIES_FILE, content, 'utf8');
}

// Colors (ANSI codes work on most terminals including Windows Terminal)
const colors = {
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  reset: '\x1b[0m',
};

// Helper functions
function printHeader() {
  console.log(`${colors.blue}================================================${colors.reset}`);
  console.log(`${colors.blue}  TOKO ANAK BANGSA Story Creator${colors.reset}`);
  console.log(`${colors.blue}================================================${colors.reset}`);
  console.log('');
}

function printSuccess(msg) {
  console.log(`${colors.green}✓ ${msg}${colors.reset}`);
}

function printError(msg) {
  console.log(`${colors.red}✗ ${msg}${colors.reset}`);
}

function printInfo(msg) {
  console.log(`${colors.yellow}→ ${msg}${colors.reset}`);
}

// Create readline interface
function createPrompt() {
  return readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
}

// Promisified question
function question(rl, query) {
  return new Promise((resolve) => {
    rl.question(query, resolve);
  });
}

// Get next story ID by scanning existing files
function getNextStoryId(prefix) {
  let maxNum = 0;
  const dirs = [ROOT_TODOS, API_TODOS, STORE_PORTAL_TODOS, MARKETPLACE_TODOS, COMPANY_PROFILE_TODOS, PLATFORM_ADMIN_TODOS];

  // Check sprint status file
  if (fs.existsSync(SPRINT_STATUS)) {
    const content = fs.readFileSync(SPRINT_STATUS, 'utf8');
    const regex = new RegExp(`${prefix}-(\\d+)`, 'g');
    let match;
    while ((match = regex.exec(content)) !== null) {
      const num = parseInt(match[1], 10);
      if (num > maxNum) maxNum = num;
    }
  }

  // Check todo directories
  for (const dir of dirs) {
    if (fs.existsSync(dir)) {
      const files = fs.readdirSync(dir);
      for (const file of files) {
        const match = file.match(new RegExp(`${prefix}-(\\d+)`));
        if (match) {
          const num = parseInt(match[1], 10);
          if (num > maxNum) maxNum = num;
        }
      }
    }
  }

  return maxNum + 1;
}

// Convert title to kebab-case filename
function toKebabCase(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/-+/g, '-');
}

// Generate todo file content - minimal placeholder for AI to fill
function generateTodoContent(storyId, title, description, scope) {
  const scopePath = scope === 'cross' ? 'docs/features/' : `apps/${scope}/docs/dev-guide/`;

  return `# ${storyId}: ${title}

## Overview
${description}

<!--
  AI TODO: Use /fill-story command to generate full content.

  Documentation to reference:
  - Feature specs: docs/features/ (find relevant feature file)
  - Dev guide: ${scopePath}01-setup.md
  - Shared packages: packages/*/docs/dev-guide/01-setup.md

  The /fill-story command will automatically read these docs and fill this file.
-->

## User Story
<!-- AI: Generate user story based on overview and feature docs -->

## Acceptance Criteria
<!-- AI: Generate acceptance criteria from feature requirements -->

## Technical Design
<!-- AI: Generate technical design based on scope: ${scope} and feature docs -->

## Implementation Checklist
<!-- AI: Generate implementation checklist following dev-guide patterns -->

## Dependencies
<!-- AI: List prerequisite features, packages, and services -->

## Testing
<!-- AI: Generate testing requirements from feature acceptance criteria -->

## Notes
<!-- AI: Add edge cases and considerations from feature documentation -->
`;
}

// Generate Claude prompt for filling the todo
function generateClaudePrompt(storyId, title, description, scope, category, todoFile) {
  const scopeDocs = {
    api: 'apps/api/docs/dev-guide/01-setup.md and relevant feature docs from docs/features/',
    'store-portal': 'apps/store-portal/docs/dev-guide/01-setup.md and relevant feature docs',
    marketplace: 'apps/marketplace/docs/dev-guide/01-setup.md and relevant feature docs',
    'company-profile': 'apps/company-profile/docs/dev-guide/01-setup.md and relevant feature docs',
    'platform-admin': 'apps/platform-admin/docs/dev-guide/01-setup.md and relevant feature docs',
    cross: 'docs/features/ directory and all app-specific dev-guides',
  };

  const categoryToFeature = {
    AUTH: '01-authentication.md',
    STORE: '02-tenant-management.md',
    PRODUCTS: '03-product-management.md',
    INVENTORY: '04-inventory-management.md',
    POS: '05-pos-cashier.md',
    ORDERS: '06-order-management.md',
    CUSTOMERS: '07-customer-management.md',
    SUPPLIERS: '08-supplier-purchasing.md',
    PAYMENTS: '09-financial-management.md',
    MARKETPLACE: '10-marketplace.md',
    REPORTS: '11-reports-analytics.md',
    NOTIFICATIONS: '12-notifications.md',
    SETTINGS: '13-settings.md',
    ADMIN: '14-platform-admin.md',
  };

  const featureFile = categoryToFeature[category] || 'Check all relevant features';

  return `
Fill in the todo file for story ${storyId}.

**Story Details:**
- ID: ${storyId}
- Title: ${title}
- Description: ${description}
- Scope: ${scope}
- Category: ${category}
- Todo File: ${todoFile}

**Documentation to Read:**
1. **Feature docs**: docs/features/${featureFile}
   - Read Business Requirements, Features, User Flows, API Endpoints, Data Models
2. **Dev guide**: ${scopeDocs[scope]}
   - Follow project structure and implementation patterns
3. **Shared packages**:
   - packages/firebase-client/docs/dev-guide/01-setup.md (for Firebase usage)
   - packages/shared-types/docs/dev-guide/01-setup.md (for types and schemas)
   - packages/ui-web/docs/dev-guide/01-setup.md (for UI components)

**Instructions:**
1. Identify and read the relevant feature documentation
2. Generate complete content for the todo file following the project patterns
3. Use exact API endpoints from feature documentation
4. Follow data models from feature documentation
5. Include detailed acceptance criteria based on the description and feature specs
6. Create implementation checklist following the dev-guide patterns
7. Consider edge cases from feature documentation

**Required Sections:**
- User Story (As a... I want... so that...)
- Acceptance Criteria (specific, testable checkboxes from feature requirements)
- Technical Design (API endpoints from feature docs, database from data models, UI changes)
- Implementation Checklist (per-project tasks following dev-guide structure)
- Dependencies (prerequisite features, packages, services)
- Testing requirements
- Notes (edge cases, considerations from feature docs)

Please read the todo file and fill in all sections based on the description and feature documentation.
`;
}

// Main function
async function main() {
  const rl = createPrompt();

  try {
    printHeader();

    // Step 1: Get story title
    console.log(`${colors.yellow}Enter story title:${colors.reset}`);
    const storyTitle = await question(rl, '> ');

    if (!storyTitle.trim()) {
      printError('Story title is required');
      process.exit(1);
    }

    // Step 2: Select project scope
    console.log('');
    console.log(`${colors.yellow}Select project scope:${colors.reset}`);
    console.log('  1) api              - Flask API Backend');
    console.log('  2) store-portal     - Store Portal (POS & Store Management)');
    console.log('  3) marketplace      - Marketplace (E-commerce)');
    console.log('  4) company-profile  - Company Profile (Landing Page)');
    console.log('  5) platform-admin   - Platform Admin');
    console.log('  6) cross            - Cross-project (multiple apps)');
    console.log('');
    const scopeChoice = await question(rl, 'Enter choice (1-6): ');

    let scope, prefix;
    switch (scopeChoice) {
      case '1':
        scope = 'api';
        prefix = 'API';
        break;
      case '2':
        scope = 'store-portal';
        prefix = 'STORE';
        break;
      case '3':
        scope = 'marketplace';
        prefix = 'MKT';
        break;
      case '4':
        scope = 'company-profile';
        prefix = 'CORP';
        break;
      case '5':
        scope = 'platform-admin';
        prefix = 'ADMIN';
        break;
      case '6':
        scope = 'cross';
        prefix = 'STORY';
        break;
      default:
        printError('Invalid choice');
        process.exit(1);
    }

    // Step 3: Select story type
    console.log('');
    console.log(`${colors.yellow}Select story type:${colors.reset}`);
    console.log('  1) feature    - New feature');
    console.log('  2) bugfix     - Bug fix');
    console.log('  3) refactor   - Code refactoring');
    console.log('  4) chore      - Maintenance task');
    console.log('  5) docs       - Documentation');
    console.log('');
    const typeChoice = await question(rl, 'Enter choice (1-5): ');

    const typeMap = { '1': 'feature', '2': 'bugfix', '3': 'refactor', '4': 'chore', '5': 'docs' };
    const storyType = typeMap[typeChoice] || 'feature';

    // Step 4: Select category
    console.log('');
    console.log(`${colors.yellow}Select feature category:${colors.reset}`);

    const categories = loadCategories();
    const catKeys = Object.keys(categories);
    const catMap = {};

    catKeys.forEach((key, index) => {
      const num = index + 1;
      catMap[String(num)] = key;
      console.log(`  ${num}) ${key.padEnd(10)} - ${categories[key]}`);
    });

    const newCatNum = catKeys.length + 1;
    console.log(`  ${newCatNum}) NEW        - Create new category`);
    console.log('');
    const catChoice = await question(rl, `Enter choice (1-${newCatNum}): `);

    let category;
    if (catChoice === String(newCatNum)) {
      // Create new category
      console.log('');
      console.log(`${colors.yellow}Enter new category key (uppercase, e.g., MUSIC):${colors.reset}`);
      const newKey = (await question(rl, '> ')).toUpperCase().replace(/[^A-Z0-9]/g, '');

      if (!newKey) {
        printError('Category key is required');
        process.exit(1);
      }

      console.log(`${colors.yellow}Enter category description:${colors.reset}`);
      const newDesc = await question(rl, '> ');

      if (!newDesc) {
        printError('Category description is required');
        process.exit(1);
      }

      // Add new category and save
      categories[newKey] = newDesc;
      saveCategories(categories);
      printSuccess(`Added new category: ${newKey} - ${newDesc}`);
      category = newKey;
    } else {
      category = catMap[catChoice] || 'OTHER';
    }

    // Step 5: Get assignee
    console.log('');
    console.log(`${colors.yellow}Assignee (leave empty for unassigned):${colors.reset}`);
    console.log('  Available: iqbal, team');
    const assigneeInput = await question(rl, '> ');
    const assignee = assigneeInput.trim() || 'null';
    const assigneeDisplay = assignee === 'null' ? 'unassigned' : assignee;

    // Step 6: Brief description
    console.log('');
    console.log(`${colors.yellow}Brief description (one line):${colors.reset}`);
    const description = await question(rl, '> ');

    rl.close();

    // Generate story ID
    const storyNum = getNextStoryId(prefix);
    const storyId = `${prefix}-${String(storyNum).padStart(3, '0')}`;

    // Generate filename
    const filename = toKebabCase(storyTitle);

    // Generate branch name
    const branchName = `${storyType}/${scope}/${filename}`;

    // Determine todo directory
    const todoDirMap = {
      api: API_TODOS,
      'store-portal': STORE_PORTAL_TODOS,
      marketplace: MARKETPLACE_TODOS,
      'company-profile': COMPANY_PROFILE_TODOS,
      'platform-admin': PLATFORM_ADMIN_TODOS,
      cross: ROOT_TODOS,
    };
    const todoDir = todoDirMap[scope];
    const todoFile = path.join(todoDir, `${filename}.md`);

    // Create directory if needed
    fs.mkdirSync(todoDir, { recursive: true });

    // Write todo file
    const todoContent = generateTodoContent(storyId, storyTitle, description, scope);
    fs.writeFileSync(todoFile, todoContent, 'utf8');
    printSuccess(`Created todo file: ${todoFile}`);

    // Update sprint status.yaml
    console.log('');
    printInfo('Updating sprint status...');

    const sprintEntry = `  - id: ${storyId}
    title: "${storyTitle}"
    type: ${storyType}
    project: ${scope}
    assignee: ${assignee}
    status: in-progress
    branch: "${branchName}"
    docs: "${todoFile}"
    category: ${category}`;

    if (fs.existsSync(SPRINT_STATUS)) {
      let sprintContent = fs.readFileSync(SPRINT_STATUS, 'utf8');
      if (sprintContent.includes('stories:')) {
        // Append after "stories:" line
        sprintContent = sprintContent.replace(/^(stories:)/m, `$1\n${sprintEntry}`);
      } else {
        // Add stories section
        sprintContent += `\nstories:\n${sprintEntry}\n`;
      }
      fs.writeFileSync(SPRINT_STATUS, sprintContent, 'utf8');
    } else {
      fs.writeFileSync(SPRINT_STATUS, `stories:\n${sprintEntry}\n`, 'utf8');
    }

    printSuccess(`Updated sprint status: ${SPRINT_STATUS}`);

    // Create and checkout new branch
    console.log('');
    printInfo(`Creating and switching to branch: ${branchName}`);

    try {
      execSync(`git checkout -b "${branchName}"`, { stdio: 'pipe' });
      printSuccess(`Switched to branch: ${branchName}`);
    } catch (e) {
      try {
        execSync(`git checkout "${branchName}"`, { stdio: 'pipe' });
        printSuccess(`Switched to existing branch: ${branchName}`);
      } catch (e2) {
        printError(`Failed to create/checkout branch: ${branchName}`);
        console.log(`You can manually create it with: git checkout -b ${branchName}`);
      }
    }

    // Generate Claude prompt
    const claudePrompt = generateClaudePrompt(storyId, storyTitle, description, scope, category, todoFile);

    // Summary
    console.log('');
    console.log(`${colors.green}================================================${colors.reset}`);
    console.log(`${colors.green}  Story Created Successfully!${colors.reset}`);
    console.log(`${colors.green}================================================${colors.reset}`);
    console.log('');
    console.log(`  ${colors.yellow}Story ID:${colors.reset}    ${storyId}`);
    console.log(`  ${colors.yellow}Title:${colors.reset}       ${storyTitle}`);
    console.log(`  ${colors.yellow}Type:${colors.reset}        ${storyType}`);
    console.log(`  ${colors.yellow}Project:${colors.reset}     ${scope}`);
    console.log(`  ${colors.yellow}Category:${colors.reset}    ${category}`);
    console.log(`  ${colors.yellow}Assignee:${colors.reset}    ${assigneeDisplay}`);
    console.log(`  ${colors.yellow}Branch:${colors.reset}      ${branchName}`);
    console.log(`  ${colors.yellow}Todo File:${colors.reset}   ${todoFile}`);
    // Copy fill command to clipboard (macOS)
    const fillCommand = `/fill-story ${todoFile}`;
    try {
      execSync(`echo "${fillCommand}" | pbcopy`, { stdio: 'pipe' });

      // Terminal bell to alert user
      process.stdout.write('\x07');

      console.log('');
      console.log(`${colors.green}================================================${colors.reset}`);
      console.log(`${colors.green}  ✓ Ready! Command copied to clipboard${colors.reset}`);
      console.log(`${colors.green}================================================${colors.reset}`);
      console.log('');
      console.log(`  ${colors.yellow}>>> Press Cmd+V now to fill the story <<<${colors.reset}`);
      console.log('');
      console.log(`  ${colors.blue}${fillCommand}${colors.reset}`);
      console.log('');
    } catch (e) {
      console.log('');
      console.log(`${colors.blue}================================================${colors.reset}`);
      console.log(`${colors.blue}  Run this in Claude Code to fill the story:${colors.reset}`);
      console.log(`${colors.blue}================================================${colors.reset}`);
      console.log('');
      console.log(`  ${colors.green}${fillCommand}${colors.reset}`);
      console.log('');
    }
  } catch (error) {
    rl.close();
    printError(`Error: ${error.message}`);
    process.exit(1);
  }
}

main();
