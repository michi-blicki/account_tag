# Architecture

## Module Overview

The `account_tag` module is a lightweight extension to Odoo's native account tagging system, designed to provide enhanced configuration and management capabilities for account tags in multi-company environments.

## Model Hierarchy

```
account.account.tag (inherited)
├── company_ids (Many2many → res.company)
├── code (Char)
├── parent_id (Many2one → account.account.tag)
└── child_ids (One2many ← account.account.tag.parent_id)
```

## Core Components

### 1. Data Model (`models/account_account_tag.py`)

**Inherited Model**: `account.account.tag`

#### New Fields

| Field | Type | Purpose | Required |
|-------|------|---------|----------|
| `company_ids` | Many2many | Associates tags with specific companies | Yes |
| `code` | Char | Unique alphanumeric identifier | Yes |
| `parent_id` | Many2one | Links to parent tag for hierarchy | No |
| `child_ids` | One2many | Reverse relation for child tags | Auto |

#### Features

- **Multi-Company Support**: Tags can be filtered and applied per company
- **Hierarchical Organization**: Support for tag taxonomy and categorization
- **Unique Identification**: Code field enables programmatic access and integration

### 2. User Interface (`views/account_account_tag.xml`)

#### Records

**Form View** (`account_account_tag_view_form`)
- Main editing interface for account tags
- Organized sections:
  - **Title Section**: Tag name with active/archived status
  - **Account Tag Definition**: Code and parent tag selection
  - **Configuration Group**: Applicability, color, companies, country
  - **Child Tags Section**: Inline list of related child tags

**List View** (`account_account_tag_view_list`)
- Quick overview of all tags
- Sortable columns: Code, Name, Parent, Applicability, Color, Country, Companies
- Supports multi-select for bulk operations

**Action Window** (`action_account_account_tag`)
- Main entry point for tag management
- Default view order: List → Form
- Access control: `group_account_readonly`
- Parent menu: `account.account_account_menu`

**Menu Item** (`account_account_tag_menu`)
- Located in: Invoicing / Configuration / Accounting
- Sequence: 3
- Group restriction: Account readonly group

## Data Flow

```
User Interface
    ↓
Form/List View (XML)
    ↓
account.account.tag Model
    ↓
Odoo ORM Layer
    ↓
Database
```

## Integration Points

### With Core Modules

- **account**: Native Odoo accounting module
  - Inherits from `account.account.tag`
  - Uses tags for account categorization
  - Respects existing tag functionality

### With Multi-Company

- **res.company**: Many-to-many relationship
  - Restricts tag visibility per company
  - Enables company-specific configurations

## Security

### Access Control

```xml
<record id="account_account_tag_menu" ...>
    <field name="groups">account.group_account_readonly</field>
</record>
```

Only users with the "Account / Read-only" group can access the menu.

### Field-Level Security

Standard Odoo field-level security applies. Custom security rules can be added via:
- `security/ir.model.access.csv` (record rules)
- ACL definitions (if needed)

## Extension Points

### Inheriting This Module

```python
class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'
    
    # Add your custom fields here
    custom_field = fields.Char('Custom Field')
```

### Overriding Views

```xml
<record id="account_account_tag_view_form" model="ir.ui.view">
    <field name="inherit_id" ref="account_tag.account_account_tag_view_form"/>
    <!-- Your modifications -->
</record>
```

## Performance Considerations

### Optimization Notes

1. **Many2many Field**: `company_ids` uses indexed storage for efficient filtering
2. **Parent-Child Relations**: No deep recursion is implemented; manual depth limits recommended
3. **View Rendering**: Child tags are rendered inline; consider pagination for large datasets

### Recommendations

- Index custom searches on `code` field for better query performance
- Use domain filters when querying tags across multiple companies
- Implement batch operations for bulk tag creation/modification

## Version Compatibility

- **Odoo Version**: 18.0
- **Edition**: Community
- **Python**: 3.8+
- **Database**: PostgreSQL 12+

## Future Enhancement Possibilities

1. **Bulk Operations**: Import/export functionality
2. **Tag Templates**: Predefined tag sets for quick setup
3. **Reporting**: Advanced tag usage analytics
4. **Validation Rules**: Custom validation for tag codes
5. **Approval Workflow**: Tag change approval process
