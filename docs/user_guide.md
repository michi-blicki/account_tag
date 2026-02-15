# User Guide

## Getting Started

### Accessing Account Tags

1. Log in to Odoo as a user with accounting permissions
2. Navigate to **Invoicing** module
3. Go to **Configuration / Accounting / Account Tags**
4. You'll see the Account Tags management interface

### Understanding Account Tags

Account tags are labels used to categorize and organize accounts in your chart of accounts. This module enhances the native Odoo tagging system with additional features:

- **Code**: Unique identifier for the tag
- **Hierarchy**: Parent-child relationships for tag organization
- **Multi-Company**: Assign tags to specific companies
- **Color**: Visual identification of tag types
- **Applicability**: Define if tag applies to Sales, Purchases, or Both

## Creating Account Tags

### Step-by-Step Guide

1. Click the **Create** button in the Account Tags list
2. Fill in the tag details:

   | Field | Description | Required |
   |-------|-------------|----------|
   | **Tag Name** | Display name of the tag | Yes |
   | **Code** | Unique alphanumeric code (e.g., "TAX", "ASSET") | Yes |
   | **Parent Tag** | Select a parent for hierarchical organization | No |
   | **Applicability** | Choose: Purchases, Sales, or Both | Default: Both |
   | **Color** | Select a color from the color picker | Optional |
   | **Companies** | Select which companies this tag applies to | Yes |
   | **Country** | Specify a country for localization | Optional |

3. Click **Save**

### Example: Creating Tax Tags

```
Tag Name: "Tax On Supplies"
Code: "TAX_SUP"
Parent Tag: "Tax Tags" (if exists)
Applicability: Both
Companies: [Your Company]
Country: [Your Country]
```

## Managing Tag Hierarchies

### Creating Parent Tags

1. Create a tag without a parent (the "Parent Tag" field will be empty)
2. This becomes a parent tag
3. Save the tag

### Adding Child Tags

#### Method 1: Create and Link Child Tags

1. Create a new tag
2. In the "Parent Tag" field, select the parent tag
3. Save

#### Method 2: Add from Parent View

1. Open a parent tag in edit mode
2. Scroll to the "Child Tags" section
3. Click **Add a line** in the child tags table
4. Fill in:
   - **Code**: Child tag code
   - **Name**: Child tag name
   - **Country**: (Optional)
   - **Companies**: Select companies
5. Click **Save**

### Organizing Your Tags

**Example Hierarchy**:
```
├─ Financial Tags
│  ├─ Assets
│  ├─ Liabilities
│  └─ Equity
├─ Tax Tags
│  ├─ VAT
│  └─ Income Tax
└─ Reporting Tags
   ├─ Profit Center
   └─ Cost Center
```

## Managing Companies

### Assigning Tags to Companies

1. Open the tag you want to configure
2. In the "Companies" field, click to open the company selector
3. Choose one or more companies
4. Click outside the field to confirm
5. Save the tag

### Viewing Tags by Company

1. In the Account Tags list view
2. Use the "Companies" column to see which companies have access to each tag
3. Filter by company using the search filter at the top

**Filter Example**:
- Search: `Companies: [Your Company]`
- This shows only tags assigned to your company

## Editing Account Tags

### Modifying Existing Tags

1. Open the Account Tags list
2. Click on the tag you want to edit
3. Modify the fields as needed
4. Click **Save**

### Archiving Tags

To archive a tag (hide it without deleting):

1. Open the tag in edit mode
2. In the "Status" header area, toggle **Active** to OFF
3. Save
4. The tag will show as "(Archived)" on the form
5. Archived tags won't appear in normal dropdown selections

### Restoring Archived Tags

1. In the tag list, add filter: `Active: False`
2. Find and open the archived tag
3. Toggle **Active** to ON
4. Save

## Using Account Tags

### Applying Tags to Accounts

1. Navigate to **Accounting / Configuration / Chart of Accounts**
2. Open an account you want to tag
3. In the "Account Tags" section, select applicable tags
4. Save the account

### Tag-Based Reporting

Account tags are used in various reports:

- **Tax Reports**: Use tax-related tags for tax calculations
- **Financial Analysis**: Tags enable custom reporting views
- **Account Filtering**: Filter accounts by their tags in reports

### Bulk Tag Operations

Currently, bulk tag assignment must be done individually. Consider:

1. Creating a consistent tagging scheme first
2. Using parent tags to organize related tags
3. Assigning company tags systematically

## Best Practices

### Naming Conventions

Use consistent naming for better organization:

```
Good Examples:
- TAX_VAT_IN
- ACT_BANK_MAIN
- LEG_REPORTING

Avoid:
- tax123
- stuff
- temporary_tag
```

### Code Field Usage

The code field should be:
- **Unique**: No duplicate codes within the system
- **Meaningful**: Reflects the tag's purpose
- **Uppercase**: For better visibility in reports
- **Short**: Keep codes concise (max 20 characters)

### Company Assignment

- Assign tags to all companies that use them
- Review and update company assignments when companies are added
- Use filtering to verify assignment completeness

### Color Coding

Use colors strategically:
- **Red**: High-priority or tax-related tags
- **Green**: Assets and income tags
- **Blue**: General operational tags
- **Yellow**: Cost centers and special reporting

## Advanced Features

### Filtering and Searching

In the Account Tags list:

1. **Search by Code**: Type in the search box `code: TAX`
2. **Filter by Applicability**: `applicability: Purchases`
3. **Filter by Country**: `country_id: Switzerland`
4. **Combine Filters**: `code: TAX & applicability: Sales`

### Exporting Tag Data

1. Open the Account Tags list
2. Select tags you want to export (if needed)
3. Use the export button (⬇ icon) in the top menu
4. Choose format (CSV, Excel)
5. Download the file

### Integration with Other Modules

Account tags can be used by:

- **Tax Reporting**: For tax-specific tag sets
- **Financial Reporting**: For custom report grouping
- **Account Analysis**: For account categorization in reports
- **Custom Modules**: Via Python API queries

## Troubleshooting

### Issue: "Companies" field is required but empty

**Solution**: 
1. Assign at least one company to each tag
2. Ensure the tag is relevant for your company setup

### Issue: Child tags not appearing

**Solution**:
1. Ensure the parent tag is saved first
2. Refresh the page (Ctrl+R)
3. Check that parent-child links are correct

### Issue: Tag changes not reflected in reports

**Solution**:
1. Refresh the report view
2. Clear browser cache (Ctrl+Shift+Delete)
3. Restart Odoo if changes persist

### Issue: Permission denied when editing tags

**Solution**:
1. Ensure you have accounting permissions
2. Ask your administrator for the "Account / Read-only" group access
3. You may need "Account / Accountant" group for full access

## Support and Help

For additional help:

- Check the [Architecture Guide](./architecture.md)
- Review [Installation Guide](./installation.md)
- Contact your Odoo administrator
- Visit https://www.blicki.ch for support
