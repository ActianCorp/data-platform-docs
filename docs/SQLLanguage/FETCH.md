---
title: "FETCH"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "FETCH.htm"
canonical_id: "actian-data-platform-fetch"
---

## FETCH

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The FETCH statement fetches data from a database cursor into host language variables.

The FETCH statement has the following formats:

Non-dynamic version:

```
EXEC SQL FETCH [FROM] cursor_name              INTO variable[:indicator_var] {, variable[:indicator_var]};
```

Dynamic version:

```
EXEC SQL FETCH [FROM] cursor_name USING DESCRIPTOR descriptor_name;
```

**FROM cursor_name**

:   Specifies the name of an open cursor. Cursor_name can be either a string constant or a host language variable.

**USING DESCRIPTOR descriptor_name**

:   Identifies an SQLDA that contains type descriptions of one or more host language variables. Each element of the SQLDA is assigned the corresponding value in the current row of the cursor. For more information, see [Embedded SQL](../SQLLanguage/Embedded_SQL.md).

#### Description

The FETCH statement retrieves the results of the SELECT statement that is executed when a cursor is opened. When a cursor is opened, the cursor is positioned immediately before the first result row. The FETCH statement advances the cursor to the first (or next) row and loads the values in that row into the specified variables. Each FETCH statement advances the cursor one row.

There must be a one-to-one correspondence between variables specified in the INTO or USING clause of FETCH and expressions in the SELECT clause of the DECLARE CURSOR statement. If the number of variables does not match the number of expressions, the preprocessor generates a warning and, at runtime, the SQLCA variable sqlwarn3 is set to W.

The variables listed in the INTO clause can include structures that substitute for some or all of the variables. The structure is expanded by the preprocessor into the names of its individual variables; therefore, placing a structure name in the INTO clause is equivalent to enumerating all members of the structure in the order in which they were declared.

The variables listed in the INTO clause or within the descriptor must be type-compatible with the values being retrieved. If a result expression is nullable, the host language variable that receives that value must have an associated null indicator.

If the statement does not fetch a row—a condition that occurs after all rows in the set have been processed—the sqlcode of the SQLCA is set to 100 (condition not found) and no values are assigned to the variables.

The statement must be terminated according to the rules of the host language.

#### Readonly Cursors and Performance

For read-only cursors, Actian Data Platform prefetches rows to improve performance. To disable prefetching or specify the number of rows that are prefetched, use the SET_SQL(PREFETCHROWS) statement.

#### Usage in OpenAPI, ODBC, JDBC, .NET

In OpenAPI, ODBC, JDBC, and .NET, the fetch concept is supported through interface-specific calls.

#### Permissions

This statement is available to all users.

#### Fetch Locking

Depending on the lock level chosen, appropriate shared resource locks are acquired.

#### Related Statements

OPEN

CLOSE

[SELECT (Interactive)](../SQLLanguage/SELECT_(Interactive).md)
