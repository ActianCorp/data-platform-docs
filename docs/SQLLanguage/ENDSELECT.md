---
title: "ENDSELECT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ENDSELECT.htm"
canonical_id: "actian-data-platform-endselect"
---

## ENDSELECT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The ENDSELECT statement terminates a SELECT loop.

The ENDSELECT statement has the following format:

```
EXEC SQL ENDSELECT;
```

The ENDSELECT statement terminates embedded SQL select loops. A select loop (see [Cursors Versus Select Loops](../SQLLanguage/Cursors_Versus_Select_Loops.md)) is a block of code delimited by BEGIN and END statements and associated with a SELECT statement. As the SELECT statement retrieves rows from the database, each row is processed by the code in the select loop.

When the ENDSELECT statement is executed, the program stops retrieving rows from the database and program control is transferred to the first statement following the select loop.

The ENDSELECT statement must be inside the select loop that it is intended to terminate. If an ENDSELECT statement is placed inside a forms code block that is syntactically nested within a select loop, the statement ends the code block as well as the select loop.

The statement must be terminated according to the rules of the host language.

!!! note "Note"

    To find out how many rows were retrieved before the ENDSELECT statement was issued, check the sqlerrd(3) variable of the SQLCA.For more information about the SQLCA, see [Embedded SQL](../SQLLanguage/Embedded_SQL.md).

#### Permissions

This statement is available to all users.

#### Locking

If autocommit is off (default behavior), the ENDSELECT statement does not affect locking. All locks held before the ENDSELECT statement remain. If autocommit is on, the ENDSELECT statement ends the query and locks are dropped.
