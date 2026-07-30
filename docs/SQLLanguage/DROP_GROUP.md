---
title: "DROP GROUP"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_GROUP.htm"
canonical_id: "actian-data-platform-drop-group"
---

## DROP GROUP

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP GROUP statement removes the specified group identifiers from the installation. If any of the specified identifiers does not exist, Actian Data Platform returns an error but does not terminate the statement. Other valid existing group_ids in the statement are deleted.

A group identifier must be empty, that is, have no users in its user list, before it can be dropped. If an attempt is made to drop a group identifier that still has members in its user list, Actian Data Platform returns an error and does not delete the identifier. However, the statement is not terminated. Other group identifiers in the list, if they are empty, are deleted. (Use the [ALTER GROUP](../SQLLanguage/ALTER_GROUP.md) statement to drop all the users from a group's user list.)

Any session using a group identifier when the identifier is dropped continues to run with the privileges defined for that group.

#### Syntax

The DROP GROUP statement has the following format:

```
[EXEC SQL] DROP GROUP group_id {, group_id};
```

## DROP GROUP Examples

1. Drop the group identifier, acct_clerk.

```
DROP GROUP acct_clerk;
```

2. In an application, drop the group identifiers, tel_sales and temp_clerk.

```
EXEC SQL DROP GROUP tel_sales, temp_clerk;
```
