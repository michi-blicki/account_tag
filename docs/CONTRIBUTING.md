# Contributing Guidelines

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be respectful and inclusive in all interactions.

## How to Contribute

### Report Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Title**: A clear, concise description of the issue
- **Reproduction Steps**: Step-by-step instructions to reproduce the behavior
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Screenshots**: If applicable, add screenshots to help explain your problem
- **Environment**:
  - Odoo version (18.0)
  - Operating system and version
  - Any relevant module versions

### Suggest Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Title**: A clear, concise description of the enhancement
- **Current Behavior**: Describe the current limitation
- **Proposed Behavior**: Describe the desired functionality
- **Motivation**: Explain why this enhancement would be useful
- **Examples**: Provide examples of how the enhancement would be used

### Pull Requests

We welcome pull requests! Please follow these guidelines:

#### Before You Start

1. Fork the repository
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/my-feature-name
   # or
   git checkout -b fix/my-bug-fix
   ```
3. Ensure your local environment is set up correctly

#### Code Style

- Follow [Python PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Follow [Odoo Coding Guidelines](https://github.com/odoo/odoo/wiki/CodeGuidelines)
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and reasonably short

#### XML/View Guidelines

- Properly indent XML (2 spaces)
- Use descriptive record IDs
- Group related fields in `<group>` elements
- Use appropriate string attributes for labels
- Follow Odoo view structure conventions

#### Commit Messages

Write clear, descriptive commit messages:

```
[FEATURE] Brief description of the feature

Longer explanation of what this commit does.
If needed, explain the motivation and design decisions.

Fixes #123 (if related to an issue)
```

**Format**: `[TYPE] Subject`

Types:
- `[FEATURE]`: New feature
- `[FIX]`: Bug fix
- `[REFACTOR]`: Code refactoring
- `[DOCS]`: Documentation updates
- `[TEST]`: Test additions or changes
- `[CHORE]`: Build, CI, or dependency updates

#### Testing

Before submitting a pull request:

1. Test your changes thoroughly
2. Test on a fresh Odoo 18 installation
3. Test with multiple companies if applicable
4. Test both enabled and disabled states
5. Check for any console errors in the browser

#### Documentation

- Update README.md if you add new features
- Add/update docstrings in Python code
- Update user guide if user-facing changes are made
- Add your changes to CHANGELOG.md

#### Pull Request Process

1. Update documentation and CHANGELOG.md
2. Ensure no unused imports or variables
3. Write a clear description of your changes
4. Reference any related issues using `Fixes #123`
5. Submit your PR with a clear title and description

**PR Title Format**: Same as commit messages
**PR Description**: Should include:
- What changes were made
- Why these changes are necessary
- How to test the changes
- Any breaking changes (if applicable)

## Development Setup

### Prerequisites

- Odoo 18 Community Edition
- Git
- A code editor (VS Code recommended)
- PostgreSQL

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/account_tag.git
cd account_tag

# Create a feature branch
git checkout -b feature/your-feature

# Make your changes and test
# ...

# Commit your changes
git add .
git commit -m "[FEATURE] Your feature description"

# Push to your fork
git push origin feature/your-feature
```

### Testing Your Changes

1. Copy the module to your Odoo addons directory
2. Restart Odoo
3. Update module list
4. Install/upgrade the module
5. Thoroughly test all functionality

## Reporting Security Vulnerabilities

If you discover a security vulnerability, please email security@blicki.ch instead of using the issue tracker.

## Documentation

- Keep documentation accurate and up-to-date
- Use clear language suitable for both developers and end-users
- Include examples where helpful
- Update docs when code changes affect functionality

## Recognition

Contributors will be recognized in:
- CHANGELOG.md
- GitHub contributors list
- Project acknowledgments

## Questions?

Feel free to open a discussion issue or contact us at info@blicki.ch

## License

By contributing, you agree that your contributions will be licensed under the same AGPL-3 license as the project.

---

Thank you for contributing to make this project better!
