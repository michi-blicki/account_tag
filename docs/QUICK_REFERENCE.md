# Quick Reference Guide

A concise reference for the Account Account Tag Enhancement module.

## Quick Links

| Resource | Purpose |
|----------|---------|
| [README.md](../README.md) | Main project documentation |
| [Installation Guide](installation.md) | Step-by-step installation instructions |
| [User Guide](user_guide.md) | End-user documentation and tutorials |
| [Architecture](architecture.md) | Technical architecture and design |
| [Technical Spec](technical_spec.md) | Detailed technical specifications |
| [Contributing](CONTRIBUTING.md) | Contribution guidelines |
| [Changelog](CHANGELOG.md) | Version history and updates |

## Module Details

```
Name:           Account Account Tag Enhancement
Technical ID:   account_tag
Version:        18.0.1.0.0
Odoo Version:   18.0 Community Edition
Author:         Michael Blickenstorfer
License:        AGPL-3
Website:        https://www.blicki.ch
```

## Installation Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/account_tag.git /path/to/odoo/addons/

# In Odoo web interface:
# 1. Go to Apps
# 2. Search for "Account Account Tag Enhancement"
# 3. Click Install
```

## Key Features at a Glance

| Feature | Description |
|---------|-------------|
| **Code Field** | Unique alphanumeric identifier for tags |
| **Multi-Company** | Assign tags to specific companies |
| **Hierarchy** | Parent-child tag relationships |
| **Color Coding** | Visual tag identification |
| **Applicability** | Sales, Purchases, or Both |
| **Countries** | Localization support |

## Common Tasks

### Create a New Tag

1. Go to **Invoicing / Configuration / Accounting / Account Tags**
2. Click **Create**
3. Fill: Name, Code, Companies
4. Click **Save**

### Add Child Tags

1. Open a parent tag
2. Scroll to "Child Tags" section
3. Click "Add a line"
4. Fill code and name
5. Save

### Archive a Tag

1. Open the tag
2. Toggle "Active" to OFF
3. Click "Save"

### Filter by Company

1. In tag list, use search filter
2. Type: `Companies: [Your Company]`
3. Press Enter

## Database Schema

```
account.account.tag (inherited)
├── code (Char) - NEW
├── company_ids (Many2many → res.company) - NEW
├── parent_id (Many2one → account.account.tag) - NEW
└── child_ids (One2many ← account.account.tag) - NEW
```

## API Examples

```python
# Create a tag
tag = self.env['account.account.tag'].create({
    'name': 'My Tag',
    'code': 'TAG_CODE',
    'company_ids': [(6, 0, [company_id])],
})

# Find by code
tag = self.env['account.account.tag'].search([
    ('code', '=', 'TAG_CODE')
], limit=1)

# Get child tags
children = tag.child_ids

# Filter by company
tags = self.env['account.account.tag'].search([
    ('company_ids', 'in', company_id)
])
```

## Keyboard Shortcuts

When editing tags in the form view:

| Shortcut | Action |
|----------|--------|
| Ctrl+S | Save |
| Ctrl+K | Quick search |
| Tab | Next field |
| Shift+Tab | Previous field |

## Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| Module not visible | Click "Update Apps List" in Apps menu |
| "Companies" field required | Assign at least one company to the tag |
| Child tags not showing | Ensure parent tag is saved and refresh page |
| Permission denied | Request "Account / Read-only" group access |

## Performance Tips

- Use codes for programmatic access (faster than searching by name)
- Limit parent-child hierarchy depth for better performance
- Use company filtering to reduce data loaded
- Cache frequently accessed tag hierarchies in custom code

## Security Notes

- Tags respect the "Account / Read-only" security group
- Standard Odoo backup procedures apply
- No sensitive data is stored in custom fields
- Tag access is filtered by company context

## Dependencies

```
Required:
└── account (core Odoo module)

Optional:
└── None
```

## File Structure Overview

```
account_tag/
├── __init__.py
├── __manifest__.py
├── LICENSE
├── README.md
├── docs/
│   ├── CHANGELOG.md
│   ├── architecture.md
│   ├── installation.md
│   ├── user_guide.md
│   ├── technical_spec.md
│   ├── CONTRIBUTING.md
│   ├── OCA_SUBMISSION.md
│   └── QUICK_REFERENCE.md (this file)
├── models/
│   ├── __init__.py
│   └── account_account_tag.py
└── views/
    └── account_account_tag.xml
```

## Naming Conventions

```
Tag Codes (examples):
✓ TAX_VAT_IN        (Good: Clear, structured)
✓ ACT_BANK_MAIN     (Good: Meaningful)
✗ tax123            (Bad: Non-standard)
✗ temp_tag          (Bad: Too vague)

Tag Names (examples):
✓ VAT Tax Input     (Good: Descriptive)
✓ Main Bank Account (Good: Clear purpose)
```

## Important Fields

| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| Name | Char | Yes | Tag display name |
| Code | Char | Yes | Unique identifier |
| Company IDs | Many2many | Yes | Company association |
| Parent ID | Many2one | No | Hierarchical parent |
| Applicability | Selection | Yes | Sales/Purchases/Both |
| Color | Integer | No | Visual identification |
| Country | Many2one | No | Localization |
| Active | Boolean | Yes | Archive status |

## Getting Help

**Documentation**: See links at top of this guide
**Issues**: Report on GitHub
**Email**: info@blicki.ch
**Website**: https://www.blicki.ch

## Version Information

Current Version: **18.0.1.0.0**
Release Date: **2026-02-15**
Status: **Stable**

## License

GNU Affero General Public License v3.0 - See LICENSE file for full text.

---

Last Updated: 2026-02-15
