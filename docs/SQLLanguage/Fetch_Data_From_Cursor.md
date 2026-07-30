---
title: "Fetch Data From Cursor"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Fetch_Data_From_Cursor.htm"
canonical_id: "actian-data-platform-fetch-data-from-cursor"
---

## Fetch Data From Cursor

The FETCH statement advances the position of the cursor through the result rows returned by the select. Using the FETCH statement, your application can process the rows one at a time. The syntax of the FETCH statement is:

```
EXEC SQL FETCH cursor_name
```

```
INTO variable{, variable};
```

The FETCH statement advances the cursor to the first or next row in the set, and loads the values indicated in the SELECT clause of the DECLARE CURSOR statement into host language variables.

To illustrate, the example of cursor processing shown previously contains the following DECLARE CURSOR statement:

```
EXEC SQL DECLARE c1 CURSOR FOR     SELECT ename, sal     FROM employee     FOR UPDATE OF sal;
```

Later in the program, the following FETCH statement appears:

```
EXEC SQL FETCH c1 INTO :name, :salary;
```

This FETCH statement puts the values from the columns, ename and sal, of the current row into the host language variables, name and salary.

Because the FETCH statement operates on a single row at a time, it is ordinarily placed inside a host language loop.

You can detect when you have fetched the last row in the result table in the following ways:

- The sqlcode variable in the SQLCA is set to 100 if an attempt is made to fetch past the last row of the result table.
- After the last row is retrieved, succeeding fetches do not affect the contents of the host language variables specified in the INTO clause of the FETCH statement.

- The WHENEVER NOT FOUND statement specifies an action to be performed when the cursor moves past the last row.
- The SQLSTATE variable returns 02000 when the last row has been fetched.

Cursors can only move forward through a set of rows. To refetch a row, close and reopen a cursor.
