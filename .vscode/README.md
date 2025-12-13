# VSCode Configuration

This directory contains Visual Studio Code workspace settings and configurations for the TOKO ANAK BANGSA project.

## Files Overview

### `settings.json`
Workspace-level settings for VSCode that configure:
- **Editor**: Format on save, rulers, tab size
- **File handling**: EOL, trim whitespace, exclusions
- **TypeScript**: Workspace TypeScript version, import preferences
- **Python**: Black formatter, Flake8 linting, virtual environment
- **ESLint**: Working directories for monorepo
- **Tailwind CSS**: Class regex for cva and cn utilities
- **i18n Ally**: Locale paths for next-intl

### `extensions.json`
Recommended VSCode extensions for the project:
- **TypeScript/JavaScript**: ESLint, Prettier
- **React/Next.js**: ES7 React snippets, Simple React snippets
- **Tailwind CSS**: IntelliSense
- **Python**: Python, Pylance, Black formatter
- **i18n**: i18n Ally for translation management
- **Firebase**: VSFire
- **Git**: GitLens
- **Utilities**: Error Lens, TODO Tree, Path IntelliSense
- **GitHub Copilot**: AI pair programming

### `launch.json`
Debug configurations for:
- **Next.js Apps**: Client-side (Chrome) and server-side (Node) debugging
- **Flask API**: Python debugging with Flask
- **Compound configs**: Full-stack debugging (Frontend + Backend)

### `tasks.json`
Pre-configured tasks for common operations:
- Development servers (all apps or specific apps)
- Build tasks
- Type checking
- Linting
- Firebase emulators
- Sprint management (create story)
- Python operations
- Git operations

### `snippets.code-snippets`
Custom code snippets for:
- Next.js components (server and client)
- Custom hooks
- API routes
- Zod schemas
- Flask routes
- Pydantic models
- Firestore queries
- Testing patterns
- Commit messages

## Getting Started

### 1. Install Recommended Extensions

When you open the project, VSCode will prompt you to install recommended extensions. Click "Install All" or install them manually:

```bash
# Essential extensions
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension bradlc.vscode-tailwindcss
code --install-extension ms-python.python
code --install-extension ms-python.black-formatter
code --install-extension lokalise.i18n-ally
```

### 2. Set Up Python Virtual Environment

The workspace is configured to use the Flask API's virtual environment:

```bash
cd apps/api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

VSCode will automatically detect this virtual environment.

### 3. Configure TypeScript

The workspace uses the local TypeScript version from `node_modules`. Accept the prompt to use the workspace TypeScript version when it appears.

## Using Debug Configurations

### Debug Next.js App (Client-side)

1. Start the development server:
   ```bash
   pnpm dev:store-portal
   ```

2. Press `F5` or go to Run & Debug panel
3. Select "Store Portal (Client)"
4. Set breakpoints in your code
5. Debug in Chrome DevTools

### Debug Next.js App (Server-side)

1. Go to Run & Debug panel
2. Select "Store Portal (Server)"
3. Press `F5` to start debugging
4. Set breakpoints in API routes or Server Components

### Debug Flask API

1. Go to Run & Debug panel
2. Select "Flask API"
3. Press `F5` to start debugging
4. Set breakpoints in Python code

### Full-Stack Debugging

1. Go to Run & Debug panel
2. Select "Full Stack (Store Portal + API)"
3. Press `F5`
4. Both frontend and backend will start with debugging enabled

## Using Tasks

### Run Tasks

Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and type "Tasks: Run Task"

**Common tasks:**
- `Dev: All Apps` - Start all development servers
- `Dev: Store Portal` - Start only Store Portal
- `Dev: Flask API` - Start only Flask API
- `Build: All` - Build all apps and packages
- `TypeCheck: All` - Run TypeScript type checking
- `Lint: All` - Run ESLint on all code
- `Sprint: Create Story` - Interactive story creation

### Default Build Task

Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux) to run the default build task.

## Using Code Snippets

### TypeScript/React Snippets

Type the prefix and press `Tab`:

- `nxpage` - Next.js Server Page Component
- `nxclient` - Next.js Client Component
- `nxhook` - Custom React Hook
- `nxapi` - Next.js API Route Handler
- `zodschema` - Zod Schema with TypeScript type
- `fsquery` - Firestore Query (Frontend)
- `loading` - Loading State Component
- `errorstate` - Error State Component
- `testcomponent` - React Component Test

### Python Snippets

- `flaskroute` - Flask Blueprint Route
- `pydantic` - Pydantic Model
- `fsquerypy` - Firestore Query (Backend)
- `pytest` - Python Test Function

### Git Snippets

- `commit` - Conventional Commit Message

**Example usage:**

1. Type `nxpage` in a `.tsx` file
2. Press `Tab`
3. Fill in the placeholders:
   - Component name
   - Translation namespace
   - Title key

## Workspace Settings Explained

### Format on Save

The workspace is configured to:
- Format files on save using Prettier
- Auto-fix ESLint issues
- Organize imports

**To disable for a specific file:**
```typescript
// prettier-ignore
const messyCode = { a:1,b:2,c:3 };
```

### File Watchers

The workspace excludes these directories from file watching to improve performance:
- `node_modules/`
- `.next/`
- `.turbo/`
- `dist/`
- `__pycache__/`

### Python Configuration

The workspace uses:
- **Formatter**: Black (line length 88)
- **Linter**: Flake8
- **Type Checker**: Pylance (basic mode)
- **Virtual Environment**: `apps/api/venv`

### Tailwind CSS IntelliSense

IntelliSense works for:
- Regular Tailwind classes
- CVA (Class Variance Authority) in `@toko/ui-web`
- `cn()` utility function

**Example:**
```tsx
<div className="flex items-center gap-4">  // IntelliSense works
```

### i18n Ally

The i18n Ally extension provides:
- Inline translation preview
- Translation key navigation
- Missing translation warnings
- Quick translation editing

**Configuration:**
- Locales: `apps/*/messages` directories
- Framework: next-intl
- Key style: nested

## Troubleshooting

### ESLint Not Working

1. Ensure you're in a workspace folder with `package.json`
2. Run `pnpm install` to install dependencies
3. Reload VSCode: `Cmd+Shift+P` → "Developer: Reload Window"

### TypeScript Errors

1. Ensure workspace TypeScript is selected:
   - `Cmd+Shift+P` → "TypeScript: Select TypeScript Version"
   - Choose "Use Workspace Version"
2. Build shared packages: `pnpm build`
3. Restart TypeScript server: `Cmd+Shift+P` → "TypeScript: Restart TS Server"

### Python IntelliSense Not Working

1. Select the correct Python interpreter:
   - `Cmd+Shift+P` → "Python: Select Interpreter"
   - Choose `apps/api/venv/bin/python`
2. Install Pylance extension
3. Reload VSCode

### Format on Save Not Working

1. Check if file type has a formatter configured in `settings.json`
2. Ensure Prettier extension is installed
3. Check for `.prettierrc` in project root
4. Try manual format: `Cmd+Shift+P` → "Format Document"

## Customizing Settings

### User Settings vs Workspace Settings

**Workspace settings** (`.vscode/settings.json`):
- Apply only to this project
- Shared with team via Git
- Good for project-specific conventions

**User settings** (`~/Library/Application Support/Code/User/settings.json`):
- Apply to all projects
- Not shared with team
- Good for personal preferences

### Override Workspace Settings

To override workspace settings for yourself:
1. Open User Settings: `Cmd+,` (Mac) or `Ctrl+,` (Windows)
2. Search for the setting
3. Change it in User Settings (takes precedence)

### Add Custom Snippets

1. `Cmd+Shift+P` → "Preferences: Configure User Snippets"
2. Select "snippets.code-snippets (Workspace)"
3. Add your snippet following the existing format

## Keyboard Shortcuts

Common shortcuts in this workspace:

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| Run Task | `Cmd+Shift+P` → Tasks | `Ctrl+Shift+P` → Tasks |
| Build (Default) | `Cmd+Shift+B` | `Ctrl+Shift+B` |
| Start Debugging | `F5` | `F5` |
| Format Document | `Shift+Option+F` | `Shift+Alt+F` |
| Organize Imports | `Shift+Option+O` | `Shift+Alt+O` |
| Quick Fix | `Cmd+.` | `Ctrl+.` |
| Go to Definition | `F12` | `F12` |
| Find References | `Shift+F12` | `Shift+F12` |
| Rename Symbol | `F2` | `F2` |

## Additional Resources

- [VSCode Documentation](https://code.visualstudio.com/docs)
- [TypeScript in VSCode](https://code.visualstudio.com/docs/languages/typescript)
- [Python in VSCode](https://code.visualstudio.com/docs/languages/python)
- [Debugging in VSCode](https://code.visualstudio.com/docs/editor/debugging)
- [Tasks in VSCode](https://code.visualstudio.com/docs/editor/tasks)

---

**Last Updated**: 2024-12-13
