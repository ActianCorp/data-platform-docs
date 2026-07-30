---
title: "Non-cursor Select"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Non-cursor_Select.htm"
canonical_id: "actian-data-platform-non-cursor-select"
---

## Non-cursor Select

The non-cursor version of the embedded SELECT statement can be used to retrieve a single row or a set of rows from the database.

If the optional begin-end block syntax is not used, the embedded SELECT statement can retrieve only one row from the database. This kind of SELECT statement is called the singletonselect and is compatible with the ANSI standard. If the singleton select does try to retrieve more than one row, an error occurs and the result variables hold information from the first row.

For example, the following example retrieves a single row from the database:

```
EXEC SQL SELECT ename, sal       INTO :ename, :sal       FROM employee       WHERE eno = :eno;
```

### Select Loops

A select loop can be used to read a table and process its rows individually. When a program needs to read a table without issuing any other database statements during the retrieval (such as for report generation), use a select loop. If other tables must be queried while the current retrieval is in progress, use a cursor.

The BEGIN-END statements delimit the statements in the select loop. The code is executed once for each row as it is returned from the database. Statements cannot be placed between the SELECT statement and the BEGIN statement.

During the execution of the select loop, no other statements that access the database can be issued because this causes a runtime error. For information about manipulating and updating rows and tables within the database while data is being retrieved, see [Embedded SQL](../SQLLanguage/Embedded_SQL.md).

However, if your program is connected to multiple database sessions, you can issue queries from within the select loop by switching to another session. To return to the outer select loop, switch back to the session in which the SELECT statement was issued.

To avoid preprocessor errors, the nested queries cannot be within the syntactic scope of the loop but must be referenced by a subroutine call or some form of a go to statement.

There are two ways to terminate the select loop: run it to completion or issue the endselect statement. A host language go to statement cannot be used to exit or return to the select loop.

To terminate a select loop before all rows are retrieved the application must issue the ENDSELECT statement. The ENDSELECT statement(see [ENDSELECT](../SQLLanguage/ENDSELECT.md)) must be syntactically within the BEGIN - END block that delimits the select loop.

The following example retrieves a set of rows from the database:

```
EXEC SQL SELECT ename, sal, eno       INTO :ename, :sal, :eno       FROM employee       ORDER BY eno;EXEC SQL BEGIN;       browse data;       if error condition then              EXEC SQL ENDSELECT;       end if;EXEC SQL END;
```

### INTO Clause--Retrieve Values into Host Language Variables

The INTO clause specifies the host program variables into which the values retrieved by the select are loaded. There must be a one-to-one correspondence between expressions in the SELECT clause and the variables in the INTO clause. If the statement does not retrieve any rows, the variables are not modified. If the number of values retrieved from the database is different from the number of columns, an error is issued and the sqlwarn3 variable of the SQLCA is assigned the value W. Each result variable can have an indicator variable for null data.

Host language variables can be used as expressions in the SELECT clause and thesearch_condition, in addition to their use in the INTO clause. Variables used in search_conditions must denote constant values and cannot represent names of database columns or include any operators. Host string variables can also substitute for the complete search condition.

The INTO clause can include a structure that substitutes for some or all of the variables. The structure is expanded by the preprocessor into the names of its individual variables. Therefore, placing a structure name in the INTO clause is equivalent to enumerating all members of the structure in the order in which they were declared.

If using SELECT ***** to retrieve into a structure, ensure that the members of the structure have a one-to-one correspondence to the columns in the result table.

#### Use of Host Language Variables in a Union

When SELECT statements are combined using the UNION clause, the INTO clause must appear only after the first list of select result expressions, because all result rows of the SELECT statements that are combined by the UNION clause must be identical. The following example shows the correct use of host language variables in a union; result variables are specified only for the first SELECT statement:

```
EXEC SQL SELECT ename, enumber              INTO :name, :number              FROM employee       UNION       SELECT dname, dnumber              FROM directors              WHERE dnumber < 100;
```

### REPEATED Queries

To reduce the overhead required to repeatedly execute a SELECT query statement, specify the query as REPEATED. For repeated queries, Actian Data Platform saves the query execution plan after the first time the query is executed. This can significantly improve the performance of subsequent executions of the same select.

If your application needs to be able to change the search conditions, dynamically constructed search conditions cannot be used with repeated queries. The saved execution plan is based on the initial value of the search condition and subsequent changes are ignored.
