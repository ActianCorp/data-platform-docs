---
title: "TRUNCATE TABLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "TRUNCATE_TABLE.htm"
canonical_id: "actian-data-platform-truncate-table"
---

## TRUNCATE TABLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The TRUNCATE TABLE statement deletes all data from a table and its indexes.

This statement has the following format:

```
TRUNCATE TABLE [schema.]tablename
```

**tablename**

:   Specifies the name of the table. The user must own the table or have MODIFY permission for the table.

This statement deletes all rows and releases the file space back to the operating system. TRUNCATE TABLE takes an exclusive lock on the table so concurrent operations against the table being truncated must wait until the operation is completed and the lock is released when the transaction is committed or rolled back.

The TRUNCATE TABLE operation fails if:

- Removing all rows will result in a foreign-key constraint violation
- A concurrent DML or truncate operation on the same table commits in the meantime

- A background update-propagation operation on the same table commits in the meantime
- The table is referenced by another table’s foreign key, and a concurrent DML operation on the referencing table commits in the meantime

TRUNCATE TABLE performs the same operation as MODIFY...TO TRUNCATED:

```
TRUNCATE TABLE foo
```

is identical to

```
MODIFY foo TO TRUNCATED
```

For Ingres tables with secondary indexes, any indexes not created WITH PERSISTENCE are dropped.
