---
title: "Correlation Names"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Correlation_Names.htm"
canonical_id: "actian-data-platform-correlation-names"
---

## Correlation Names

Correlation names are used in queries to clarify the table (or view) to which a column belongs or to abbreviate long table names. For example, the following query uses correlation names to join a table with itself:

```
SELECT a.empname FROM emp a, emp b      WHERE a.mgrname = b.empname      AND a.salary > b.salary;
```

Correlation names can also allow the schema name and table to be clarified for all columns used in queries. For example, the following query uses correlation names to join a table with the same name between schemas:

```
SELECT m.empname FROM my.emp m, your.emp y      WHERE m.mgrname = y.empname      AND m.salary > y.salary;
```

## Correlation Name Rules

Correlation names can be specified in these SQL statements: SELECT, DELETE, UPDATE.

The rules for using correlation names are as follows:

- A single query can reference a maximum of 384 table names (including all base tables referenced by views specified in the query).
- If a correlation name is not specified, the table name implicitly becomes the correlation name. For example, in the following query:

```
DELETE FROM employee      WHERE salary > 100000;
```

    The Actian Data Platform assumes the correlation name of employee for the salary column and interprets the preceding query as:

```
DELETE FROM employee      where employee.salary > 100000;
```

- If a correlation name for a table is specified, use the correlation name (and not the actual table name) within the query. For example, the following query generates a syntax error:

```
/*wrong*/DELETE FROM employee e     WHERE employee.salary > 35000;
```

- A correlation name must be unique. For example, the following statement is illegal because the same correlation name is specified for different tables:

```
/*wrong*/SELECT e.ename FROM employee e, manager e      WHERE e.dept = e.dept;
```

- In nested queries, the Actian Data Platform resolves unqualified column names by checking the tables specified in the nearest FROM clause, then the FROM clause at the next highest level, and so on, until all table references are resolved.

    For example, in the following query, the dno column belongs to the deptsal table, and the dept column to the employee table.

```
SELECT ename FROM employee     WHERE salary >     (SELECT AVG(salary) FROM deptsal      WHERE dno = dept);
```

    Because the columns are specified without correlation names, the Actian Data Platform performs the following steps to determine which table the columns belong to:

dno

:   The Actian Data Platform checks the table specified in the nearest****FROM clause (the deptsal table). The dno column does belong to the deptsal table; the DBMS interprets the column specification as deptsal.dno

dept

:   The Actian Data Platform checks the table specified in the nearest****FROM clause (deptsal). The dept column does not belong to the deptsal table.

:   The Actian Data Platform checks the table specified in the****FROM clause at the next highest level (the employee table). The dept column does belong to the employee table; the column specification is interpreted as employee.dept.

- The Actian Data Platform does not search across subqueries at the same level to resolve unqualified column names. For example, given the query:

```
SELECT * FROM employee WHERE      dept IN (SELECT dept FROM sales_departments           WHERE mgrno=manager_id)     OR     dept IN (SELECT dept FROM mktg_departments           WHERE mgrno=manager_id);
```

    The Actian Data Platform checks the description of the sales_departments table for the mgrno and manager columns; if they are not found, it checks the employee table next, but does not check the mktg_departments table. Similarly, the Actian Data Platform first checks the mktg_departments table for the mgrno and manager_id columns. If they are not found, it checks the employee table, but never checks the sales_departments table.

!!! note "Note"

    We recommend for a query that involves more than one table or view that all columns be specified with the appropriate table name or correlation name even if all columns are unique.
