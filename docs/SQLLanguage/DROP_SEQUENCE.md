---
title: "DROP SEQUENCE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_SEQUENCE.htm"
canonical_id: "actian-data-platform-drop-sequence"
---

## DROP SEQUENCE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP SEQUENCE statement deletes a sequence from the database catalog.

The DROP SEQUENCE statement has the following format:

```
[EXEC SQL] DROP SEQUENCE [IF EXISTS] [schema.]sequence_name;
```

**IF EXISTS**

:   Suppresses error reporting for the specified object if the object does not exist and the user matches the schema.

**sequence_name**

:   Specifies an existing sequence.

:   Actian Data Platform returns an error for each non-existent sequence name in a list, but does not terminate the statement. Existing sequences for valid names in the list are removed.

#### Permissions

You must have CREATE_SEQUENCE privilege to drop a sequence.

#### Locking and Sequences

In applications, sequences use logical locks that allow multiple transactions to retrieve and update the sequence value while preventing changes to the underlying sequence definition. The logical lock is held until the end of the transaction.

#### Related Statements

[ALTER SEQUENCE](../SQLLanguage/ALTER_SEQUENCE.md)[](../SQLLanguage/ALTER_SEQUENCE.md)

[CREATE SEQUENCE](../SQLLanguage/CREATE_SEQUENCE.md)[](../SQLLanguage/CREATE_SEQUENCE.md)
