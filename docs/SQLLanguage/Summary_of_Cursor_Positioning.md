---
title: "Summary of Cursor Positioning"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Summary_of_Cursor_Positioning.htm"
canonical_id: "actian-data-platform-summary-of-cursor-positioning"
---

## Summary of Cursor Positioning

The following table summarizes the effects of cursor statements on cursor positioning:

| Statement | Effect on Cursor Position |
| --- | --- |
| OPEN | Cursor positioned before first row in set. |
| FETCH | Cursor moves to next row in set. If it is already on the last row, the cursor moves beyond the set and its position becomes undefined. |
| CLOSE | Cursor and set of rows become undefined. |

### Dynamically Specifying Cursor Names

A dynamically specified cursor name (a cursor name specified using a host string variable) can be used to scan a table that contains rows that are related hierarchically, such as a table of employees and managers.

In a relational database, this tree structure is represented as a relationship between two columns. In an employee table, employees are assigned an ID number. One of the columns in the employee table contains the ID number of each employee’s manager. The ID number column establishes the relationships between employees and managers.

To use dynamically specified cursor names to scan this kind of table, do the following:

- Write a routine that uses a cursor to retrieve all the employees that work for a manager.
- Create a loop that calls this routine for each row that is retrieved and dynamically specifies the name of the cursor to be used by the routine.

The following example retrieves rows from the employee table, which has the following format:

```
exec sql declare employee table
```

```
     (ename          varchar(32),
```

```
     title           varchar(20),
```

```
     manager         varchar(32));
```

This program scans the employee table and prints out all employees and the employees that they manage.

```
/* This program will print each manager (starting with the top manager)
```

```
** and who they manage, for the entire company. */
```

```

```

```
exec sql include sqlca;
```

```

```

```
/* main program */
```

```
exec sql begin declare section;
```

```
     manager character_string(32)
```

```
exec sql end declare section;
```

```

```

```
exec sql connect dbname;
```

```

```

```
exec sql whenever not found goto closedb;
```

```
exec sql whenever sqlerror call sqlprint;
```

```

```

```
/* Retrieve top manager */
```

```
exec sql select ename into :topmanager
```

```
     from employee
```

```
     where title = 'President';
```

```

```

```
/* start with top manager */
```

```
print “President”, topmanager
```

```
call printorg(1, “President”);
```

```

```

```
closedb:
```

```
exec sql disconnect;
```

```

```

```
/* This subroutine retrieves and displays employees who report to a given manager. This subroutine is called recursively to determine if a given employee is also a manager and if so, it will display who reports to them.
```

```
*/
```

```

```

```
subroutine printorg(level, manager)
```

```
level integer;
```

```

```

```
exec sql begin declare section;
```

```
     manager character_string(32)
```

```
     ename character_string(32)
```

```
     title character_string(20);
```

```
exec sql end declare section;
```

```

```

```
/* set cursor name to 'c1', 'c2', ...  */
```

```
cname = 'c' + level
```

```

```

```
exec sql declare :cname cursor for
```

```
     select ename, title, manager from employee
```

```
          where manager = :manager
```

```
          order by ename;
```

```

```

```
exec sql whenever not found goto closec;
```

```

```

```
exec sql open :cname;
```

```

```

```
loop
```

```
     exec sql fetch :cname into :ename, :title,
```

```
          :manager;
```

```

```

```
/* Print employee's name and title */
```

```
          print title, ename
```

```

```

```
/* Find out who (if anyone) reports to this
```

```
     employee */
```

```
          printorg(level+1, ename);
```

```
end loop
```

```

```

```
closec:
```

```
exec sql close :cname;
```
