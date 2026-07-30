---
title: "CREATE ROLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_ROLE.htm"
canonical_id: "actian-data-platform-create-role"
---

## CREATE ROLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE ROLE statement defines one or more role identifiers and their associated password. Role identifiers are used to associate privileges with applications. After the role identifiers are created and privileges have been granted to them, use them with the CONNECT statement to associate those privileges with the session. For information about the privileges granted to role identifiers, see [GRANT (role)](../SQLLanguage/GRANT_(role).md).

Only users who have been granted access to a role can use a role. The creator of a role is automatically granted access to that role.

#### Syntax

The CREATE ROLE statement has the following format:

```
[EXEC SQL] CREATE ROLE role_id {, role_id}[WITH with_option {,with_option}]
```

```
with_option = NOPASSWORD | PASSWORD = 'role_password'
```

```
               | PASSWORD = X'encrypted_role_password'
```

```
                  | EXTERNAL_PASSWORD
```

```
                  | NOPRIVILEGES | PRIVILEGES = ( priv {,priv} )
```

**role_id**

:   Specifies the role name to be created. Must be a valid object name that is unique among all role, group, and user identifier names in the installation.

:   If an invalid role identifier is specified, Actian Data Platform returns an error but processes all valid role identifiers.

:   Role identifiers are stored in the iirole catalog of the iidbdb.

**role_password**

:   Allows a user to change his password. In addition, users with the MAINTAIN_USERS privilege can change or remove any password. If role_password contains uppercase or special characters, enclose it in single quotes. Any blanks in the password are removed when the password is stored.

:   Limits: Role_password can be no longer than 24 characters

:   Default: NOPASSWORD if the password clause is omitted.

:   To remove the password associated with role_id, specify NOPASSWORD.

:   To allow a user's password to be passed to an external authentication server for authentication, specify EXTERNAL_PASSWORD.

**priv**

:   Specifies a subject privilege, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

!!! note "Note"

    These are requestable privileges. They must be activated using the SET SESSION ADD PRIVILEGES statement.

:   Default: NOPRIVILEGES if the privileges clause is omitted.

## CREATE ROLE Examples

1. Create a role identifier and password for the inventory application of a bookstore.

```
CREATE ROLE bks_onhand WITH PASSWORD = 'hgwells';
```

2. Create a role identifier with no password for the daily sales application of the bookstore.

```
CREATE ROLE dly_sales WITH NOPASSWORD;
```

3. Create a role identifier and its password for the new employee application of the bookstore.

```
CREATE ROLE new_emp WITH PASSWORD = 'good luck';
```

4. In an application, create a role identifier and its password for an accounts payable application.

```
EXEC SQL CREATE ROLE acct_pay WITH PASSWORD = piper;
```

5. Create a role with a password and additional privileges.

```
CREATE ROLE sysop    WITH PASSWORD = 'sysoppwd',    PRIVILEGES = (OPERATOR);
```

6. Create a role with external password verification.

```
CREATE ROLE sysop    WITH EXTERNAL_PASSWORD;
```
