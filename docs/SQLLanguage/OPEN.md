---
title: "OPEN"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "OPEN.htm"
canonical_id: "actian-data-platform-open"
---

## OPEN

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The OPEN statement opens a cursor for processing.

The OPEN statement has the following format:

Non-dynamic version:

```
EXEC SQL OPEN cursor_name FOR READONLY;
```

Dynamic version:

```
EXEC SQL OPEN cursor_name [FOR READONLY]               [USING variable {, variable} |               USING DESCRIPTOR descriptor_name];
```

**FOR READONLY**

:   (Default) Opens the cursor for reading only.

**USING variable {,variable} | USING DESCRIPTOR descriptor_name**

:   Provides values for the constants that are in the prepared SELECT statement.

#### Description

The OPEN statement executes the SELECT statement specified when the cursor was declared and positions the cursor immediately before the first row returned. (To actually retrieve the rows, use the [FETCH](../SQLLanguage/FETCH.md) statement.)

A cursor must be opened before it can be used in a data manipulation statement (such as FETCH) and a cursor must be declared before it can be opened.

When a cursor that was declared for a dynamically prepared SELECT statement is opened, use the USING clause if the prepared SELECT statement contains constants specified with question marks. For information about using question marks to specify constants in prepared statements, see [PREPARE](../SQLLanguage/PREPARE.md).

The USING clause provides the values for these “unspecified” constants in the prepared SELECT so that the OPEN statement can execute the SELECT. For example, assume that your application contains the following dynamically prepared SELECT statement:

```
statement_buffer =    'select * from' + table_name + 'where low < ?    and high > ?';exec sql prepare sel_stmt from :statement_buffer;
```

When opening the cursor for this prepared SELECT statement, values for the question marks must be provided in the WHERE clause. The USING clause performs this task. For example:

```
declare the cursor for sel_stmt;assign values to variables named "low" and "high";exec sql open cursor1    using :low, :high;
```

The values in the low and high variables replace the question marks in the WHERE clause and Actian Data Platform evaluates the SELECT statement accordingly. If an SQLDA is used, the values that replace the question marks are taken from variables to which the sqlvar elements point. Before using the descriptor in an OPEN CURSOR statement, allocate the SQLDA and the variables to which the sqlvar elements point, and place values in the variables. For more information about the SQLDA and its sqlvar elements, see [Embedded SQL](../SQLLanguage/Embedded_SQL.md).

More than one cursor can be opened at the same time. The same cursor can be opened and closed (with the CLOSE statement) successive times in a single program. An open cursor must be closed before it can be reopened.

A string constant or a host language variable can be used to specify the cursor_name. The open statement must be terminated according to the rules of your host language.

#### Permissions

This statement is available to all users.

#### Related Statements

[CLOSE](../SQLLanguage/CLOSE.md)

[DECLARE CURSOR](../SQLLanguage/DECLARE_CURSOR.md)[](../SQLLanguage/DECLARE_CURSOR.md)

[FETCH](../SQLLanguage/FETCH.md)[](../SQLLanguage/FETCH.md)

## OPEN Examples

1. Declare and open a cursor.

```
exec sql declare cursor1 cursor for    select :one + 1, ename, age    from employee    where age :minage;...exec sql open cursor1;
```

    When the OPEN statement is encountered, the variables, one and minage, are evaluated. The first statement that follows the opening of a cursor must be a FETCH statement to define the cursor position and retrieve data into the indicated variables:

```
exec sql fetch cursor1    into :two, :name, :age;
```

    The value of the expression, :one + 1, is assigned to the variable, two, by the fetch.

2. The following example demonstrates the dynamic SQL syntax. In a typical application the prepared statement and its parameters are constructed dynamically.

```
select_buffer =     'select * from employee where eno = ?';exec sql prepare select1 from :select_buffer;exec sql declare cursor2 cursor for select1;eno = 1234;exec sql open cursor2 using :eno;
```
