---
title: "DROP"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP.htm"
canonical_id: "actian-data-platform-drop"
---

## DROP

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP statement destroys one or more tables, views, or indexes.

!!! note "Note"

    An index with in-memory updates cannot be dropped. Use the MODIFY...TO COMBINE command to write the in-memory changes to disk.

This statement has the following format:

```
DROP [objecttype] [IF EXISTS] [schema.]objectname {, [schema.]objectname} [RESTRICT | CASCADE];
```

**objecttype**

:   Specifies the type of object, which can be one of the following keywords:

    TABLE

    VIEW

    INDEX

**IF EXISTS**

:   Suppresses error reporting for the specified object if the object does not exist or exists but is not owned by you. Typically, the IF EXISTS clause is used prior to issuing the corresponding CREATE statement to ensure that the CREATE statement does not fail due to an existing object of that type.

**objectname**

:   Specifies the name of a table, view, or index.

**RESTRICT**

:   Aborts the DROP statement with error if any objects (such as views, synonyms, or referential constraints) depend on the object being dropped.

:   This is the default for INDEX.

**CASCADE**

:   Drops all dependent objects. This is the default for TABLE and VIEW.

## DROP Examples

1. Drop the sales_fact and time_dimension tables:

```
DROP TABLE sales_fact, time_dimension;
```

2. Drop the idx index:

```
DROP INDEX idx;
```
