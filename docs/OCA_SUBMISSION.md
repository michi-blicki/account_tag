# OCA Submission Information

This document contains information relevant for Odoo Community Association (OCA) submission and compliance.

## Module Information

- **Repository**: account_tag
- **Maintainer**: Michael Blickenstorfer (https://www.blicki.ch)
- **License**: AGPL-3
- **Odoo Series**: 18.0
- **Odoo Edition**: Community
- **Python Version**: 3.8+
- **Database**: PostgreSQL 12+

## OCA Compliance Checklist

### Documentation
- [x] README.md with comprehensive documentation
- [x] CHANGELOG.md with version history
- [x] Architecture documentation (architecture.md)
- [x] Installation guide (installation.md)
- [x] User guide (user_guide.md)
- [x] Technical specifications (technical_spec.md)
- [x] Contributing guidelines (CONTRIBUTING.md)

### Code Quality
- [x] Follows Python PEP 8 style guidelines
- [x] Follows Odoo coding guidelines
- [x] Proper error handling
- [x] Logging implemented where appropriate
- [x] No hardcoded values
- [x] Internationalization ready (uses string attributes)

### Security
- [x] AGPL-3 license applied
- [x] Copyright header in files
- [x] Proper access control with security groups
- [x] No hardcoded credentials or sensitive data
- [x] SQL injection prevention (using ORM)
- [x] XSS prevention (using proper escaping)

### Testing
- [x] Module installable without errors
- [x] Views validate correctly
- [x] Model inheritance works as expected
- [x] All fields function correctly
- [x] No dependency issues

### Manifest Quality
- [x] Proper module name and summary
- [x] Correct author information
- [x] Accurate dependencies declaration
- [x] Correct category selection
- [x] Version numbering follows conventions
- [x] License properly declared

## Category

**Selected Category**: `Association`

The module is categorized as "Association" as it enhances accounting functionality with enterprise-grade features typically needed by associations and organizations managing accounts.

### Alternative Categories (if applicable):
- Accounting
- Finance

## Dependencies Analysis

### Required Dependencies
```
account (core Odoo module - always available in Community Edition)
```

### Optional Dependencies
None

### Transitive Dependencies
Automatically resolved through the `account` module dependency.

## Module Size

- **Lines of Code**: ~20 (models)
- **View Lines**: ~100 (XML)
- **Documentation**: Comprehensive
- **Complexity**: Low to Medium

## Version Scheme

This module follows semantic versioning with Odoo version prefix:

```
{odoo_version}.{major}.{minor}.{patch}
Format: 18.0.1.0.0

Breakdown:
- 18.0: Odoo version 18.0
- 1: Major version (feature-complete releases)
- 0: Minor version (backward-compatible features)
- 0: Patch version (bug fixes)
```

## Known Limitations

1. **Hierarchy Depth**: No technical limit, but deep hierarchies may impact performance
2. **Bulk Operations**: Currently limited to individual tag operations
3. **Reporting**: Uses standard Odoo reporting mechanisms
4. **Import/Export**: Standard Odoo import/export available

## Use Cases

### Primary Use Cases

1. **Multi-Company Tag Management**
   - Assign account tags to specific companies
   - Maintain company-specific accounting structures
   - Prevent cross-company tag conflicts

2. **Hierarchical Tag Organization**
   - Create parent-child tag relationships
   - Organize tags by category
   - Streamline tag selection in forms

3. **Tag Identification**
   - Use codes for programmatic access
   - Create meaningful tag references
   - Facilitate reporting and integration

### Secondary Use Cases

- Tax reporting with category-specific tags
- Profit center and cost center organization
- Custom financial reporting structures
- Integration with third-party accounting systems

## Target Users

- **Accountants**: Managing chart of accounts and tag structures
- **Finance Managers**: Organizing financial reporting tags
- **System Administrators**: Setting up multi-company accounting structures
- **Consultants**: Implementing accounting structures for organizations

## Support and Maintenance

### Supported Versions

- Odoo 18.0 Community Edition (primary)

### Support Channels

- GitHub Issues: For bug reports and feature requests
- Email: info@blicki.ch
- Website: https://www.blicki.ch

### Maintenance Level

- **Status**: Active development
- **Support**: Community support via GitHub
- **Response Time**: Best effort basis
- **Update Frequency**: As needed for bug fixes and enhancements

## Installation Requirements

### System Requirements

- PostgreSQL 12+
- Python 3.8+
- Odoo 18.0 Community Edition
- Linux/macOS/Windows with Odoo installation

### Installation Methods Supported

1. Git clone from GitHub
2. Manual download and extraction
3. Docker-based installation
4. Standard Odoo module installation

## Testing Performed

- [x] Install on fresh Odoo 18.0 database
- [x] Create account tags with all features
- [x] Test multi-company assignment
- [x] Test parent-child relationships
- [x] Test form and list views
- [x] Test archiving/unarchiving
- [x] Verify menu access control
- [x] Test data persistence
- [x] Test inheritance integrity

## Compatibility Matrix

| Feature | Odoo 18.0 CE | Status |
|---------|-------------|--------|
| Model inheritance | ✓ | Working |
| Many2many fields | ✓ | Working |
| XML views | ✓ | Working |
| Access control | ✓ | Working |
| Multi-company | ✓ | Working |
| Translations | ✓ | Ready |

## Translation Status

The module is internationalization-ready:
- All user-visible strings use the `string=""` attribute
- All labels use proper Odoo translation strings
- Translation files can be generated using Odoo's extraction tool

## Roadmap

### Planned Features (Future Versions)

- [ ] Tag template system
- [ ] Bulk import/export functionality
- [ ] Advanced reporting features
- [ ] Integration with reporting modules
- [ ] Tag usage analytics
- [ ] Approval workflows

### Backward Compatibility

Current version (18.0.1.0.0) is the first release. Future versions will maintain backward compatibility with existing data.

## OCA Repository Requirements

### File Checklist

- [x] README.md (comprehensive)
- [x] __manifest__.py (properly formatted)
- [x] LICENSE (AGPL-3)
- [x] models/ directory with code
- [x] views/ directory with XML
- [x] docs/ directory with documentation
- [x] No .pyc or __pycache__ files
- [x] No test data or test files (if not applicable)
- [x] Proper .gitignore

### Code Standards

- [x] No trailing whitespace
- [x] Proper line endings (LF)
- [x] Proper indentation (4 spaces for Python, 2 for XML)
- [x] No hardcoded paths
- [x] No hardcoded user data
- [x] Proper logging usage

## Statistical Information

| Metric | Value |
|--------|-------|
| Python Files | 1 |
| Lines of Python Code | ~20 |
| XML Files | 1 |
| Lines of XML Code | ~100 |
| Documentation Files | 6 |
| Total Documentation Lines | ~1000 |
| Complexity | Low |
| Dependencies | 1 (account) |
| New Models | 0 |
| Inherited Models | 1 |
| New Views | 2 |
| New Fields | 4 |

## Contact Information

- **Author**: Michael Blickenstorfer
- **Email**: info@blicki.ch
- **Website**: https://www.blicki.ch
- **Location**: Switzerland

## License Compliance

This module is distributed under the AGPL-3 license. Full license text is included in the LICENSE file. Usage, modification, and distribution must comply with AGPL-3 terms.

## Disclaimer

This module is provided as-is without warranty. Users are responsible for testing in their own environments before deploying to production. Data backup is recommended before installation.
