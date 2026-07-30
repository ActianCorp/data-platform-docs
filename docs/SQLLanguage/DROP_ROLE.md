---
title: "DROP ROLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_ROLE.htm"
canonical_id: "actian-data-platform-drop-role"
---

## DROP ROLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP ROLE statement removes the specified role identifiers from the installation. Any session using a role identifier when the identifier is dropped continues to run with the privileges defined for that identifier.

#### Syntax

The DROP ROLE statement has the following format:

```
[EXEC SQL] DROP ROLE role_id {, role_id};
```

**role_id**

:   Specifies an existing role identifier. If the list of role_ids contains any that do not exist, Actian Data Platform returns an error for each non-existent role_id, but does not terminate the statement. Others in the list that are valid, existing role identifiers, are removed.

## DROP ROLE Example

Drop the sales_report role identifier:

```
DROP ROLE sales_report;
```
