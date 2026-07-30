---
title: "Execute a Dynamic Non-select Statement"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Execute_a_Dynamic_Non-select_Statement.htm"
canonical_id: "actian-data-platform-execute-a-dynamic-non-select-statement"
---

## Execute a Dynamic Non-select Statement

To execute a dynamic non-select statement, use either the EXECUTE IMMEDIATE statement or the PREPARE and EXECUTE statements. EXECUTE IMMEDIATE is most useful if the program executes the statement only once within a transaction. If the program executes the statement many times within a transaction, for example, within a program loop, use the PREPARE and EXECUTE combination: prepare the statement once, execute it as many times as necessary.

If the program does not know whether the statement is a SELECT statement, the program can prepare and describe the statement. The results returned by the DESCRIBE statement indicate whether the statement was a select. For more information, see [Execute a Dynamic SELECT Statement](../SQLLanguage/Execute_a_Dynamic_SELECT_Statement.md).

### Using EXECUTE IMMEDIATE to Execute a Non-select Statement

EXECUTE IMMEDIATE executes an SQL statement specified using a string literal or host language variable. Use this statement to execute all but a few of the SQL statements; the exceptions are listed in [EXECUTE IMMEDIATE Statement](../SQLLanguage/Dynamic_SQL_Statements.md).

For non-select statements, the syntax of EXECUTE IMMEDIATE is as follows:

```
EXEC SQL EXECUTE IMMEDIATE statement_string;
```

For example, the following statement executes a DROP statement specified as a string literal:

```
/*** Statement specification included ** in string literal. The string literal does ** NOT include 'exec sql' or ';'*/exec sql execute immediate 'drop table employee';
```

The following example reads SQL statements from a file into a host string variable buffer and executes the contents of the variable. If the variable includes a statement that cannot be executed by EXECUTE IMMEDIATE , or if another error occurs, the loop is broken.

```
exec sql begin declare section;     character buffer(100);exec sql end declare section;open file;loop while not end of file and not error     read statement from file into buffer;          exec sql execute immediate :buffer;end loop;close file;
```

If only the statement parameters (such as an employee name or number) change at runtime, EXECUTE IMMEDIATE is not needed. A value can be replaced with a host language variable. For instance, the following example increases the salaries of employees whose employee numbers are read from a file:

```
loop while not end of file and not errorread number from file;     exec sql update employee          set sal = sal * 1.1           where eno = :number;end loop;
```

### Preparing and Executing a Non-select Statement

The PREPARE and EXECUTE statements can also execute dynamic non-select statements. These statements enable your program to save a statement string and execute it as many times as necessary. A prepared statement is discarded when the transaction in which it was prepared is rolled back or committed. If a statement with the same name as an existing statement is prepared, the new statement supersedes the old statement.

The following example demonstrates how a runtime user can prepare a dynamically specified SQL statement and execute it a specific number of times:

```
read SQL statement from terminal into buffer;     exec sql prepare s1 from :buffer;read number in N     loop N times          exec sql execute s1;     end loop;
```

The following example creates a table whose name is the same as the user name, and inserts a set of rows with fixed-typed parameters (the user’s children) into the table:

```
get user name from terminal;buffer = 'create table ' + user_name +      '(child char(15), age integer)';exec sql execute immediate :buffer;buffer = 'insert into ' + user_name +      '(child, age) values (?, ?)';exec sql prepare s1 from :buffer;read child's name and age from terminal;loop until no more children     exec sql execute s1 using :child, :age;          read child's name and age from terminal;end loop;
```

For a list of statements that cannot be executed using PREPARE and EXECUTE, see [PREPARE and EXECUTE Statements](../SQLLanguage/Dynamic_SQL_Statements.md).
