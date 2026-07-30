---
title: "DECLARE CURSOR Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DECLARE_CURSOR_Examples.htm"
canonical_id: "actian-data-platform-declare-cursor-examples"
---

## DECLARE CURSOR Examples

1. Declare a cursor for a retrieval of employees from the shoe department, ordered by name (ascending) and salary (descending). (This can also be specified as a select loop.)

```
EXEC SQL DECLARE cursor1 CURSOR FOR    SELECT ename, sal    FROM employee    WHERE dept = 'shoes'    ORDER BY 1 ASC, 2 DESC;
```

2. Declare two cursors for the department and employee tables, and open them in a master-detail fashion.

```
EXEC SQL DECLARE master_cursor CURSOR FOR    SELECT * FROM dept    ORDER BY dno;EXEC SQL DECLARE detail_cursor CURSOR FOR    SELECT * FROM employee    WHERE edept = :dno    ORDER BY ename;    EXEC SQL OPEN master_cursor;loop while more departmentEXEC SQL FETCH master_cursor    INTO :dname, :dno, :dfloor, :dsales;if not found break loop;/*    ** For each department retrieve all the    ** employees and display the department     ** and employee data.*/EXEC SQL OPEN detail_cursor;loop while more employeesEXEC SQL FETCH detail_cursor    INTO :name, :age, :idno, :salary, :edept;    /*    ** For each department retrieve all the    ** employees and display the department     ** and employee data.    */process and display data;END LOOP;    EXEC SQL CLOSE detail_cursor;END LOOP;EXEC SQL CLOSE master_cursor;
```
