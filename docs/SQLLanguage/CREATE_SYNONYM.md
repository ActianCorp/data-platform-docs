---
title: "CREATE SYNONYM"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_SYNONYM.htm"
canonical_id: "actian-data-platform-create-synonym"
---

## CREATE SYNONYM

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The CREATE SYNONYM statement defines a synonym for a table, view, or index. A synonym is an alias (alternate name) for an object.

This statement has the following format:

```
CREATE SYNONYM synonym_name FOR [schema.]object
```

**synonym_name**

:   Specifies a valid object name and must not conflict with the names of other tables, views, indexes, or synonyms owned by the user issuing the statement. Synonyms can be used any place that table, view, or index identifiers are required.
