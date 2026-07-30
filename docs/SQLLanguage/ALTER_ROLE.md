---
title: "ALTER ROLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_ROLE.htm"
canonical_id: "actian-data-platform-alter-role"
---

## ALTER ROLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The ALTER ROLE statement changes the attributes associated with a role identifier.

Use ADD PRIVILEGES to give the user additional privileges. Use DROP PRIVILEGES to remove privileges from the user. You cannot use either ADD PRIVILEGES or DROP PRIVILEGES if with_optionis specified in the with_clause.

#### Syntax

The ALTER ROLE statement has the following format:

```
[EXEC SQL] ALTER ROLE role_id {, role_id}[ADD PRIVILEGES ( priv {,priv} ) |  DROP PRIVILEGES ( priv {,priv} )][WITH with_option {,with_option}]with_option = NOPASSWORD | PASSWORD = 'role_password' | EXTERNAL_PASSWORD               | NOPRIVILEGES | PRIVILEGES = ( priv {,priv} )               | NOSECURITY_AUDIT | SECURITY_AUDIT = (audit_opt {,audit_opt})
```

**role_id**

:   Specifies an existing role ID created with the CREATE ROLE statement. If one or more of the specified role identifiers do not exist, the Actian Data Platform issues a warning, but all valid role identifiers are processed.

**priv**

:   Specifies a subject privilege, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

!!! note "Note"

    These are requestable privileges. They must be activated using the SET SESSION ADD PRIVILEGES statement.

**role_password**

:   Defines the password for the role.

**Caution!**If no password is specified, any session has access to the specified role identifier and its associated permissions.

**audit_opt**

:   Defines security audit options, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

## ALTER ROLE Examples

Change the attributes associated with a role identifier:

1. Change the password for the role identifier, new_accounts, to eggbasket.

```
ALTER ROLE new_accounts WITH     PASSWORD = 'eggbasket';
```

2. Remove the password associated with the identifier, chk_inventory.

```
ALTER ROLE chk_inventory WITH NOPASSWORD;
```

3. In an application, change the password for the role identifier, mon_end_report to goodnews.

```
EXEC SQL ALTER ROLE mon_end_report WITH    PASSWORD = goodnews;
```
