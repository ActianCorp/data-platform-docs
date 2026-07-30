---
title: "RENAME TABLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RENAME_TABLE.htm"
canonical_id: "actian-data-platform-rename-table"
---

## RENAME TABLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

This statement renames tables. For an alternative method of renaming tables, see [ALTER TABLE](../SQLLanguage/ALTER_TABLE.md).

This statement has the following format:

```
[EXEC SQL] RENAME TABLE [schema.]table_name TO new_table_name
```

Indexes, grants, comments, synonyms, and sequences are automatically transferred to the newly renamed table or column.

The rename operation will fail with an error if any views depend on the old table name.

Forms, join definitions, or reports that refer to the old table name will be invalidated, and must be recreated and reloaded.

For more information, see [Rules and Restrictions on Renaming Tables](../SQLLanguage/ALTER_TABLE...ALTER_COLUMN_Restrictions.md).

## RENAME TABLE Example

Rename a table:

```
RENAME TABLE oldtbl TO newtbl
```
