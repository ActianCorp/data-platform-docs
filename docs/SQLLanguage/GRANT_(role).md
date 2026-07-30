---
title: "GRANT (role)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "GRANT_(role).htm"
canonical_id: "actian-data-platform-grant-role"
---

## GRANT (role)

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The GRANT (role) statement controls additional access to role objects created by the CREATE ROLE command. (When a role is created, an implicit grant is issued on the role to the user creating the role.) Role access can only be granted to specific users or to public.

#### Syntax

The GRANT (role) statement has the following format:

```
[EXEC SQL] GRANT role {, role}              TO PUBLIC | [USER] auth_id {, auth_id};
```

## GRANT (role) Example

Enable the user, bspring, to access sysop role:

```
GRANT sysop TO bspring
```
