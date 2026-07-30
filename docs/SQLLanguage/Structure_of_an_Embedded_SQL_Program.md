---
title: "Structure of an Embedded SQL Program"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Structure_of_an_Embedded_SQL_Program.htm"
canonical_id: "actian-data-platform-structure-of-an-embedded-sql-program"
---

## Structure of an Embedded SQL Program

In general, SQL statements can be embedded anywhere in a program that host language statements are allowed.

The following example shows a simple embedded SQL program that retrieves an employee name and salary from the database and prints them on a standard output device. The statements that begin with the words EXEC SQL are embedded SQL statements. The sequence of statements in this example illustrates a pattern common to most embedded SQL programs.

```
begin programexec sql include sqlca;exec sql begin declare section;          name character_string(15);          salary float;exec sql end declare section;exec sql whenever sqlerror stop;exec sql connect personnel;exec sql select ename, sal          into :name, :salary          from employee          where eno = 23;print name, salary;exec sql disconnect;end program
```

Each program statement is described here:

```
exec sql include sqlca;
```

    The INCLUDE statement incorporates the SQL error and status handling mechanism—the SQL Communications Area (SQLCA)—into the program. The SQLCA is used by the WHENEVER statement, which appears later in the program.

```
exec sql begin declare section;
```

    Next is an SQL declaration section. Host language variables must be declared to SQL prior to their use in any embedded SQL statements. Host language variables are described in detail in the next section.

```
exec sql whenever sqlerror stop;
```

    The WHENEVER statement that follows uses information from the SQLCA to control program execution under error or exception conditions. In general, an error handling mechanism must precede all executable embedded SQL statements in a program. For more information about error handling, see [Error Handling](../SQLLanguage/Error_Handling.md).

```
exec sql connect personnel;
```

    Next is a series of SQL and host language statements. The first statement initiates access to the personnel database. A CONNECT statement must precede any references to a database.

```
exec sql select ename, sal          into :name, :salary          from employee          where eno = 23;
```

    Next is the familiar SELECT statement, containing a clause that begins with the keyword INTO. The INTO clause associates values retrieved by the SELECT statement with host language variables in the program. Following the INTO keyword are the two host language variables previously declared to SQL: name and salary.

```
print name, salary;
```

    This host language statement prints the values contained in the variables.

```
exec sql disconnect;
```

    The last SQL statement in the program severs the connection of the program to the database.
