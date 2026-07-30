---
title: "DROP USER"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_USER.htm"
canonical_id: "actian-data-platform-drop-user"
---

## DROP USER

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP USER statement deletes an existing user.

Users that own databases cannot be dropped. If a user that owns database objects is dropped, the objects are not dropped.

This statement has the following format:

```
DROP USER user_name;
```
