---
title: "DECLARE CURSOR"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DECLARE_CURSOR.htm"
canonical_id: "actian-data-platform-declare-cursor"
---

## DECLARE CURSOR

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI

The DECLARE CURSOR statement associates a cursor name with a SELECT statement (as described in[SELECT (Interactive)](../SQLLanguage/SELECT_(Interactive).md)).

The DECLARE CURSOR statement has the following format:

```
EXEC SQL DECLARE cursor_name CURSOR               FOR SELECT [ALL | DISTINCT] result_expression {, result_expression}              FROM [schema.]table [correlation] {, [schema.]table [correlation]}              [WHERE search_condition]              [GROUP BY column {, column}]              [HAVING search_condition]              [UNION [all] full_select]              [ORDER BY ordering-expression [ASC | DESC]                             {, ordering-expression [ASC | DESC]}]              [FOR [DEFERRED | DIRECT] UPDATE OF column {, column}]
```

Dynamic SQL form:

```
EXEC SQL DECLARE cursor_name CURSOR              FOR statement_name;
```

**cursor_name**

:   Assigns a name to the cursor. The name can be specified using a quoted or unquoted string literal or a host language string variable. If cursor_name is a reserved word, it must be specified in quotes.

:   Limits: The cursor name cannot exceed 32 bytes.

DECLARE CURSOR is a compile-time statement and must appear before the first statement that references the cursor. Despite its declarative nature, a DECLARE CURSOR statement must not be located in a host language variable declaration section. A cursor cannot be declared for repeated select.

A typical cursor-based program performs these steps:

1. Issue a DECLARE CURSOR statement to associate a cursor with a SELECT statement.
2. Open the cursor. When the cursor is opened, Actian Data Platform executes the SELECT statement that was specified in the DECLARE CURSOR statement.

3. Process rows one at a time. The FETCH statement returns one row from the results of the SELECT statement that was executed when the cursor was opened.
4. Close the cursor by issuing the CLOSE statement.

You can use SELECT * in a cursor SELECT statement.

#### Embedded Usage

Host language variables can be used in the****SELECT statement of a [DECLARE CURSOR](../SQLLanguage/DECLARE_CURSOR.md), to substitute for expressions in the SELECT clause or in the search condition). When the search condition is specified within a single string variable, all the following clauses, such as the ORDER BY clause, can be included within the variable. These variables must be valid at the time of the OPEN statement of the cursor, because the SELECT is evaluated at that time; the variables do not need to have defined values at the point of the DECLARE CURSOR statement. Host language variables cannot be used to specify table, correlation, or column names.

Use the dynamic SQL syntax and specify a prepared statement name (as described in [PREPARE](../SQLLanguage/PREPARE.md)) instead of a SELECT statement. The statement name must identify a SELECT statement that has been prepared previously. The statement name must not be the same as another prepared statement name that is associated with a currently open cursor.

A source file can have multiple cursors, but the same cursor cannot be declared twice. To declare several cursors using the same host language variable to represent cursor_name, it is only necessary to declare the cursor once, because DECLARE CURSOR is a compile-time statement. Multiple declarations of the same cursor_name, even if its actual value is changed between declarations, cause a preprocessor error.

For example, the following statements cause a preprocessor error:

```
EXEC SQL DECLARE :cname[i] CURSOR FOR s1;i = i + 1/* The following statement causes a preprocessor error */EXEC SQL DECLARE :cname[i] CURSOR FOR s2;
```

Declare the cursor only once; the value assigned to the host language variable cursor_name is determined when the OPEN CURSOR statement is executed.

For example:

```
EXEC SQL DECLARE :cname[i] CURSOR FOR :sname[i];LOOP incrementing I       EXEC SQL OPEN :cname[i];END LOOP;
```

If a cursor is declared using a host language variable, all subsequent references to that cursor must use the same variable. At runtime, a dynamically specified cursor name, that is, a cursor declared using a variable, must be unique among all dynamically specified cursor names in an application. Any cursors referenced in a dynamic statement must be unique among all open cursors within the current transaction.

A cursor name declared in one source file cannot be referred to in another file, because the scope of a cursor declaration is the source file. If the cursor is re-declared in another file with the same associated query, it still does not identify the same cursor, not even at runtime. For example, if a cursor c1 is declared in source file, file1, all references to c1 must be made within file1. Failure to follow this rule results in runtime errors.

For example, if you declare cursor c1 in an include file, open it in one file and fetch from it in another file, at runtime Actian Data Platform returns an error indicating that the cursor c1 is not open on the fetch. This rule applies equally to dynamically specified cursor names.

The embedded SQL preprocessor does not generate any code for the DECLARE CURSOR statement. In languages that do not allow empty control blocks, (for example, COBOL, which does not allow empty IF blocks), the DECLARE CURSOR statement must not be the only statement in the block.

#### Usage in OpenAPI

In OpenAPI, Declare Cursor functionality is achieved through query parameters to the IIapi_query() function.

#### Permissions

This statement is available to all users.

#### Related Statements

CLOSE

FETCH

OPEN

[SELECT (Interactive)](../SQLLanguage/SELECT_(Interactive).md)
