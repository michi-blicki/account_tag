# Technical Specification

## Overview

This document provides technical specifications for the Account Account Tag Enhancement module.

## Module Information

| Property | Value |
|----------|-------|
| **Technical Name** | account_tag |
| **Display Name** | Account Account Tag Enhancement |
| **Module Type** | Accounting Enhancement |
| **License** | AGPL-3 |
| **Odoo Version** | 18.0 |
| **Edition** | Community |
| **Author** | Michael Blickenstorfer |
| **Author Website** | https://www.blicki.ch |

## Dependencies

### Required Modules

```
- account (core Odoo module)
```

### Optional Modules

None. This module is designed to work independently once the accounting module is installed.

## Database Schema

### New Fields on account.account.tag

#### company_ids (Many2many)
- **Model**: res.company
- **Required**: True
- **Store**: True
- **Copy**: True
- **Index**: False
- **String**: "Companies"
- **Purpose**: Associate tags with specific companies

#### code (Char)
- **Required**: True
- **String**: "Code"
- **Purpose**: Unique identifier for the tag
- **Max Length**: Default (typically 255 characters)

#### parent_id (Many2one)
- **Model**: account.account.tag
- **OnDelete**: cascade
- **String**: "Parent Tag"
- **Required**: False
- **Purpose**: Establish parent-child tag relationships

#### child_ids (One2many)
- **Related Field**: parent_id
- **String**: "Child Tags"
- **ReadOnly**: True
- **Purpose**: Reverse relationship for accessing child tags

## Model Structure

```python
class AccountAccountTag(models.Model):
    _name = 'account.account.tag'
    _inherit = 'account.account.tag'
    
    company_ids = fields.Many2many(
        'res.company',
        string='Companies',
        required=True,
        store=True,
        copy=True,
        index=False
    )
    code = fields.Char(
        string='Code',
        required=True
    )
    parent_id = fields.Many2one(
        'account.account.tag',
        string='Parent Tag',
        ondelete='cascade'
    )
    child_ids = fields.One2many(
        'account.account.tag',
        'parent_id',
        string='Child Tags'
    )
```

## View Architecture

### Form View (`account_account_tag_view_form`)

**Structure**:
- Title section with name and status
- Account Tag Definition group
- Configuration group (applicability, color, companies, country)
- Child Tags inline list

**Widgets Used**:
- `color`: Color picker widget for the color field
- `many2many_tags`: Tag display for company_ids with restricted options
- Default widgets for other fields

### List View (`account_account_tag_view_list`)

**Columns Displayed** (in order):
1. code
2. name
3. parent_id
4. applicability
5. color
6. country_id
7. company_ids (with many2many_tags widget)

## Access Control

### Menu Access

- **Menu ID**: account_account_tag_menu
- **Security Group**: account.group_account_readonly
- **Parent Menu**: account.account_account_menu
- **Sequence**: 3

### Data Access Rules

Standard Odoo security is applied. Additional record rules can be created via XML records in a security folder if needed.

## API Specifications

### Creating Tags

```python
tag = self.env['account.account.tag'].create({
    'name': 'Tag Name',
    'code': 'TAG_CODE',
    'company_ids': [(6, 0, [company_id])],
    'applicability': 'both',  # or 'purchases', 'sales'
    'parent_id': parent_tag_id or None,
})
```

### Searching Tags

```python
# By code
tag = self.env['account.account.tag'].search([('code', '=', 'CODE')], limit=1)

# By company
tags = self.env['account.account.tag'].search([
    ('company_ids', 'in', company_id)
])

# Hierarchical search
parent_tags = self.env['account.account.tag'].search([
    ('parent_id', '=', False)  # Top-level tags
])

# Child tags of a parent
children = parent_tag.child_ids
```

### Updating Tags

```python
tag.write({
    'code': 'NEW_CODE',
    'company_ids': [(6, 0, [new_company_id])],
    'parent_id': new_parent_id,
})
```

## ORM Operations

### Cascade Behavior

- When a parent tag is deleted, all child tags are also deleted (cascade)
- Changing parent-child relationships updates the reverse relation automatically

### Copy Behavior

- When a tag is copied (duplicated):
  - The `company_ids` many2many relationship is copied
  - Code must be manually changed to ensure uniqueness
  - The parent_id reference is copied (set to the same parent)

## Integration Points

### With account Module

The module inherits from `account.account.tag` without overriding any existing methods. All existing functionality is preserved while new features are added.

### With Multi-Company Features

- Tags respect Odoo's multi-company architecture
- Access to tags can be filtered by company context
- Company filtering is handled through the company_ids field

## Performance Characteristics

### Indexing

- No special indexing is added for this module
- Many2many field (`company_ids`) uses Odoo's default many2many table indexing
- Searches on `code` should be reasonably fast due to standard indexing

### Query Optimization

For large tag hierarchies, consider:
- Limiting depth of parent-child relationships
- Using selective searches instead of loading all tags
- Caching frequently accessed tag hierarchies

## Data Migration

No data migration is required as the module:
- Only adds new fields to an existing model
- Preserves all existing tag data
- Makes company_ids required but provides reasonable defaults

## File Structure

```
account_tag/
├── __init__.py              # Module initialization
├── __manifest__.py          # Module manifest
├── LICENSE                  # AGPL-3 license
├── README.md               # Main documentation
├── docs/
│   ├── CHANGELOG.md        # Version history
│   ├── architecture.md     # Architecture documentation
│   ├── installation.md     # Installation guide
│   ├── user_guide.md       # End-user guide
│   ├── CONTRIBUTING.md     # Contribution guidelines
│   └── technical_spec.md   # This file
├── models/
│   ├── __init__.py
│   └── account_account_tag.py
├── views/
│   ├── __init__.py
│   └── account_account_tag.xml
└── security/
    └── ir.model.access.csv (if applicable)
```

## Version History

### 18.0.1.0.0 (2026-02-15)

- Initial release for Odoo 18.0 Community Edition
- Added company_ids field
- Added code field
- Added parent-child tag relationships
- Enhanced UI with form and list views
- Full documentation

## Maintenance Notes

- Module is lightweight and has minimal dependencies
- No scheduled actions or cron jobs required
- No background processes required
- Straightforward backup and restore procedures

## Future Considerations

- Template system for pre-configured tag sets
- Bulk import/export functionality
- Advanced reporting features
- Integration with financial reporting modules
