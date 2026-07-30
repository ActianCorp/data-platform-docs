---
title: "DROP SCHEMA"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_SCHEMA.htm"
canonical_id: "actian-data-platform-drop-schema"
---

## DROP SCHEMA

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP SCHEMA statement drops the specified schema and its collection of database objects (that were defined in the [CREATE SCHEMA](../SQLLanguage/CREATE_SCHEMA.md) command).

The DROP SCHEMA statement has the following format:

```
DROP SCHEMA schema_name RESTRICT | CASCADE
```

**RESTRICT**

:   Does not drop the schema if one or more objects are associated with it.

**CASCADE**

:   Deletes all objects (tables, views, grants) that are associated with the schema.

#### Embedded Usage

In an embedded DROP SCHEMA statement, schema_name cannot be specified using a host string variable. Schema_name can be specified as the target of a dynamic SQL statement string.

#### Permissions

You must own the schema.
