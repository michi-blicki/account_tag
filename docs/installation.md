# Installation Guide

## Prerequisites

### System Requirements

- **Odoo Version**: 18.0 Community Edition
- **Python**: 3.8 or higher
- **Database**: PostgreSQL 12 or higher
- **OS**: Linux, macOS, or Windows with Odoo installation

### Dependencies

- **Core Module**: `account` (included in Odoo Community)
- No additional Python packages required

## Installation Steps

### Option 1: Git Clone (Recommended)

1. Navigate to your Odoo addons directory:
   ```bash
   cd /path/to/odoo/addons
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/account_tag.git
   ```

3. Restart your Odoo service:
   ```bash
   sudo systemctl restart odoo
   ```

4. Update module list in Odoo and install

### Option 2: Manual Installation

1. Download the module as ZIP file
2. Extract to your Odoo addons directory
3. Ensure the folder is named `account_tag`
4. Restart Odoo service
5. Install via the Apps menu

### Option 3: Docker Installation

If running Odoo in Docker:

1. Copy the module to your addons volume:
   ```bash
   docker cp account_tag container_name:/mnt/extra-addons/
   ```

2. Restart the container:
   ```bash
   docker restart container_name
   ```

3. Install via the Odoo interface

## Activation in Odoo

### Method 1: Via Web Interface

1. Log in to Odoo as Administrator
2. Navigate to **Apps** menu
3. Click **Update Apps List** (or refresh)
4. Search for "Account Account Tag Enhancement"
5. Click **Install**

### Method 2: Via Command Line

```bash
# Assuming Odoo is installed in /opt/odoo
cd /opt/odoo
python -m odoo.bin -c config.conf -u account_tag -d database_name
```

### Verification

After installation, verify the module is active:

1. Go to **Settings / Technical / Modules**
2. Search for "account_tag"
3. Confirm status shows as "Installed"

Access the feature:
1. Navigate to **Invoicing / Configuration / Accounting**
2. You should see **Account Tags** in the menu

## Uninstallation

To remove the module:

1. Go to **Apps** menu
2. Search for "Account Account Tag Enhancement"
3. Click **Uninstall**

**Warning**: Uninstalling will not delete existing account tag data, but custom fields and relationships will be removed from the database structure.

## Database Backup

**Highly recommended**: Create a database backup before installation:

```bash
# PostgreSQL backup
pg_dump -U odoo database_name > backup_before_install.sql
```

## Troubleshooting

### Module Not Appearing in App List

**Solution**:
1. Ensure the module is in the correct addons directory
2. Click **Update Apps List** in the Apps menu
3. Clear browser cache (Ctrl+Shift+Delete)
4. Reload the page

### Installation Fails with Dependency Error

**Solution**:
1. Ensure the `account` module is installed
2. Check that the database is properly upgraded
3. Restart Odoo service and retry

### "account.account.tag" Model Not Found

**Solution**:
1. Verify that the `account` module is installed
2. Check the Odoo version is 18.0
3. Look for errors in the Odoo log file

### View Errors After Installation

**Solution**:
1. Restart the Odoo service
2. Clear the view cache: Go to **Settings / Technical / UI Views** and delete cached views
3. Reload the browser page

## Post-Installation Configuration

After successful installation, the module requires no additional configuration. However, you may want to:

1. **Create Initial Tags**: Navigate to the Account Tags menu and create your first tags
2. **Assign Companies**: Set which companies each tag applies to
3. **Configure Hierarchies**: Set up parent-child tag relationships if needed

## Multi-Instance Setup

If running multiple Odoo instances:

1. Copy the module to each instance's addons directory
2. Update apps list for each instance
3. Install separately in each database

## Version Upgrades

When upgrading the module:

1. Pull the latest version:
   ```bash
   cd /path/to/account_tag
   git pull origin main
   ```

2. Restart Odoo service
3. The module will auto-upgrade the database schema if needed

## Getting Help

If you encounter issues during installation:

1. Check the Odoo log file for error messages
2. Consult the [Troubleshooting](#troubleshooting) section
3. Open an issue on the GitHub repository
4. Contact support at https://www.blicki.ch

## Security Considerations

- Ensure proper file permissions on the module directory
- The module respects Odoo's built-in security groups
- No sensitive data is stored in custom fields
- Standard Odoo backup procedures apply
