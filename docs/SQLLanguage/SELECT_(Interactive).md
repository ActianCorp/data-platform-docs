---
title: "SELECT (Interactive)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SELECT_(Interactive).htm"
canonical_id: "actian-data-platform-select-interactive"
---

## SELECT (Interactive)

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The SELECT (interactive) statement returns values from tables or views.

**Notes:**

- SELECT queries that access both Actian Data Platform and standard Ingres tables cannot execute.
- Similarly, INSERT...SELECT and CREATE AS SELECT do not work if the SELECT statement references both Actian Data Platform and Ingres tables.

This statement has the following format:

```
[WITH common_table_expression]
```

```
SELECT [FIRST rowCount] [ALL | DISTINCT]  * | expression [AS result_column]
```

```
              {, expression [[AS] result_column]}
```

```
              [FROM from_source {, from_source}
```

```
              [WHERE search_condition] WHERE (clause)
```

```
              [GROUP BY [ALL | DISTINCT] grouping element {, grouping element}]
```

```
              [HAVING search_condition] HAVING (clause)
```

```
              {UNION [ALL] | INTERSECT | EXCEPT
```

```
              (select)}
```

```
              [ORDER BY ordering-expression [ASC | DESC]
```

```
                            {, ordering-expression [ASC | DESC]}
```

```
                                [NULLS {FIRST | LAST}]];
```

```
              [LIMIT n]
```

```
              [OFFSET n]
```

```
              [FETCH FIRST|NEXT n ROWS|ROW ONLY]
```

```
              [WITH options]
```

Syntax elements are described in [WITH (common_table_expression)](../SQLLanguage/WITH_(common_table_expression).md) and [SELECT Statement Clauses](../SQLLanguage/SELECT_(Interactive).md).

## SELECT Statement Clauses

The SELECT statement has the following clauses:

- SELECT
- FROM

- WHERE
- GROUP BY

- HAVING
- ORDER BY

- LIMIT
- OFFSET

- FETCH FIRST
- UNION

- INTERSECT
- EXCEPT

- WITH

### SELECT Clause

The SELECT clause specifies which values are to be returned. To display all the columns of a table, use the asterisk wildcard character (*). For example, the following query displays all rows and columns from the employees table:

```
SELECT * FROM employee;
```

To select specific columns, specify the column names. For example, the following query displays all rows, but only two columns from the employees table:

```
SELECT emp_name, emp_no FROM employee;
```

To specify the table from which the column is to be selected, use the table.column_name syntax. For example:

```
SELECT managers.name, employee.name        FROM manager, employee...
```

In the preceding example, both source tables contain a column called name. The column names are preceded by the name of the source table; the first column of the result table contains the values from the name column of the manager table, and the second column contains the values from the name column of the employee table. If a column name is used in more than one of the source tables, qualify the column name with the table to which it belongs, or with a correlation name. For more information, see [FROM Clause](../SQLLanguage/SELECT_(Interactive).md).

The number of rows in the result table can be limited using the FIRST clause. RowCountis a positive integer value that indicates the maximum rows in the result table. The query is effectively evaluated without concern for the FIRST clause, but only the first “n” rows (as defined by rowCount) are returned. This clause cannot be used in a WHERE clause subselect and it can only be used in the first of a series of UNIONed selects. However, it can be used in the CREATE TABLE...AS SELECT and INSERT INTO...SELECT statements.

To eliminate duplicate rows from the result table, specify the keyword DISTINCT. To preserve duplicate rows, specify the keyword ALL. By default, duplicate rows are preserved.

For example, the following table contains order information; the partno column contains duplicate values, because different customers have placed orders for the same part:

| partno | customerno | qty | unit_price |
| --- | --- | --- | --- |
| 123-45 | 101 | 10 | 10.00 |
| 123-45 | 202 | 100 | 10.00 |
| 543-21 | 987 | 2 | 99.99 |
| 543-21 | 654 | 33 | 99.99 |
| 987-65 | 321 | 20 | 29.99 |

The following query displays the part numbers for which there are orders on file:

```
SELECT DISTINCT partno FROM orders
```

The result table looks like this:

| Partno |
| --- |
| 123-45 |
| 543-21 |
| 987-65 |

A constant value****can be included in the result table. For example:

```
SELECT 'Name:', emp_name, CURRENT_DATE,         IFNULL(edept,'Unassigned')        FROM employee;
```

The preceding query selects all rows from the employee table; the result table is composed of the string constant 'Name:', the name of the employee, today's date, and the employee's department, or if there is no department assigned, the string constant 'Unassigned'.

The result table looks like this (depending, of course, on the data in the employee table):

| COL1 | Emp_name | COL3 | COL4 |
| --- | --- | --- | --- |
| Name: | Mike Sannicandro | 1998-08-08 | Shipping |
| Name: | Dave Murtagh | 1998-08-08 | Purchasing |
| Name: | Benny Barth | 1998-08-08 | Unassigned |
| Name: | Dean Reilly | 1998-08-08 | Lumber |
| Name: | Al Obidinski | 1998-08-08 | Unassigned |

The SELECT clause can be used to obtain values calculated from the contents of a table. For example, the following query calculates the weekly salary of each employee based on their annual salary:

```
SELECT emp_name, salary/52 FROM employee_dim;
```

[Aggregate Functions](../SQLLanguage/SQL_Functions.md) can be used to calculate values based on the contents of a column. For example, the following query returns the highest, lowest, and average salary from the employee_dim table:

```
SELECT MAX(salary), MIN(salary), AVG(salary)         FROM employee_dim;
```

These values are based on the amounts stored in the salary column.

The SELECT clause can contain any [SQL Functions](../SQLLanguage/SQL_Functions.md). Especially useful in analytical processing are the windowing aggregate functions and the analytical functions (see [Analytical Functions](../SQLLanguage/SQL_Functions.md)).

To specify a name for a column in the result table, use the AS result_column clause. In the following example, the name, weekly_salary, is assigned to the second result column:

```
SELECT emp_name, salary/52 AS weekly_salary        FROM employee_dim;
```

If a result column name is omitted for columns that are not drawn directly from a table (for example, calculated values or constants), the result columns are assigned the default name COLn, wheren is the column number; result columns are numbered from left to right. Column names cannot be assigned in SELECT clauses that use the asterisk wildcard (*) to select all the columns in a table.

More information:

[SQL Functions](../SQLLanguage/SQL_Functions.md)

[Aggregate Functions](../SQLLanguage/SQL_Functions.md)

[Window Functions](../SQLLanguage/SQL_Functions.md)

[Window Functions](../SQLLanguage/SQL_Functions.md)

### FROM Clause

The FROM clause specifies the source tables and views from which data is to be read. The specified tables and views must exist at the time the query is issued. The from_source parameter can be:

- One or more tables or views, specified using the following syntax:

```
[schema.]table [[AS] corr_name]
```

    where table is the name of a table, view, or synonym.

- A join between two or more tables or views, specified using the following syntax:

```
source join_type JOIN source ON search_condition
```

    or

```
source join_type JOIN source USING (column {, column})
```

    or

```
source CROSS JOIN source
```

    For more information about specifying join sources, see [ANSI/ISO Join Syntax](../SQLLanguage/SELECT_(Interactive).md).

- A derived table (see [Subqueries in the FROM Clause (Derived Tables)](../SQLLanguage/Subqueries.md)) specified using the following syntax:

```
(select_stmt) corr_name [(column_list)]
```

    where select_stmt is a SELECT statement with no ORDER BY clause, corr_name is a mandatory correlation name, and column_list is an optional list of override names for the columns in the SELECT list of the select_list.

A maximum of 126 tables can be specified in a query, including the tables in the FROM list, tables in subselects, and tables and views resulting from the expansion of the definitions of any views included in the query.

The following is an example of selecting the COUNT from a table named with a user name. If the user name contains non-alphanumeric characters, it must be enclosed in quotation marks (").

```
SELECT COUNT * FROM "firstname.lastname".customer
```

### WHERE Clause

The WHERE clause specifies criteria that restrict the contents of the results table. You can test for simple relationships or, using subselects, for relationships between a column and a set of columns.

Using a simple WHERE clause, the contents of the results table can be restricted, as follows:

Comparisons:

```
SELECT ename FROM employee_dim
```

```
       WHERE manager = 'Al Obidinski';
```

```
SELECT emp_name FROM employee_dim
```

```
       WHERE salary > 50000;
```

Ranges:

```
SELECT ordnum FROM orders        WHERE odate BETWEEN DATE('2014-01-01') AND CURRENT_DATE;
```

Set membership:

```
SELECT * FROM orders        WHERE partno IN ('123-45', '678-90');
```

Pattern matching:

```
SELECT * FROM employee_dim        WHERE emp_name LIKE 'A%';
```

Nulls:

```
SELECT emp_name FROM employee_dim        WHERE dept_no IS NULL;
```

Combined restrictions using logical operators:

```
SELECT emp_name FROM employee_dim        WHERE dept_no IS NULL AND        hiredate = CURRENT_DATE;
```

!!! note "Note"

    Aggregate functions cannot appear in a WHERE clause.

More information:

[Predicates in SQL](../SQLLanguage/Predicates_in_SQL.md)

### GROUP BY Clause

The GROUP BY clause groups the selected rows based on identical values in a column or expression. This clause is typically used with aggregate functions to generate a single result row for each set of unique values in a set of columns or expressions.

A simple GROUP BY clause consists of a list of one or more columns or expressions that define the sets of rows that aggregations (like SUM, COUNT, MIN, MAX, and AVG) are to be performed on. A change in the value of any of the GROUP BY columns or expressions triggers a new set of rows to be aggregated.

If the GROUP BY clause contains CUBE or ROLLUP options, it creates superaggregate (subtotal) groupings in addition to the ordinary grouping.

GROUP BY has the following format:

```
GROUP BY [ALL | DISTINCT] grouping element {,grouping element}
```

where grouping element is:

```
column list | ROLLUP (column list) | CUBE (column list) | GROUPING SETS (grouping element {,grouping element} | ( )
```

and where:

**ALL | DISTINCT**

:   Retains (ALL) or eliminates (DISTINCT) duplicate values in the result set. Default: ALL

**column list**

:   Specifies one or more columns or expressions, each separated by a comma.

**ROLLUP (column list)**

:   Calculates group subtotals from right to left. Generates the simple GROUP BY aggregate rows, superaggregate rows, and a grand total row.

**CUBE (column list)**

:   Produces one row for each unique combination of expressions in the column list. Generates simple GROUP BY aggregate rows, superaggregate rows, cross-tabular rows, and a grand total row.

**GROUPING SETS**

:   Totals only the specified groups instead of the full set of aggregations generated by using CUBE or ROLLUP. GROUPING SETS syntax can be defined over simple column sets or CUBEs or ROLLUPs.

**( )**

:   Generates a total (that is, an aggregation computed over the entire set of input rows).

#### Simple GROUP BY Queries

The following query, which uses a simple GROUP BY clause, obtains the number of orders for each part number in the orders table:

```
SELECT partno, count(*) FROM ordersGROUP BY partno;
```

The preceding query returns one row for each part number in the orders table, even though there can be many orders for the same part number.

Nulls are used to represent unknown data, and two nulls are typically not considered to be equal in SQL comparisons. However, the GROUP BY clause treats nulls as equal and returns a single row for nulls in a grouped column or expression.

Grouping can be performed on multiple columns or expressions. For example, to display the number of orders for each part placed each day:

```
SELECT odate, partno, count(*) FROM ordersGROUP BY odate, partno;
```

If you specify the GROUP BY clause, columns referenced must be all the columns in the SELECT clause that do not contain an aggregate function. These columns can either be the column, an expression, or the ordinal number in the column list.

For example:

```
SELECT cust_no,
```

```
       CURRENT_DATE - odate AS days_since_order_placed,
```

```
       COUNT(*) AS number_of_orders
```

```
FROM orders
```

```
GROUP BY cust_no,
```

```
CURRENT_DATE - odate
```

```
ORDER BY 1, 2;
```

```

```

```
SELECT cust_no,
```

```
       CURRENT_DATE - odate AS days_since_order_placed,
```

```
       COUNT(*) AS number_of_orders
```

```
FROM orders
```

```
GROUP BY cust_no, 2
```

```
ORDER BY 1, 2;
```

#### ROLLUP, CUBE, and GROUPING SETS Queries

The GROUPING SETS extension to the GROUP BY clause includes:

- ROLLUP and CUBE
- GROUPING SETS expression

- GROUPING function

These extensions reduce the complexity of your SQL while allowing efficient analysis across multiple dimensions.

ROLLUP performs aggregations at increasing levels up to a grand total. When multiple columns are specified, say GROUP BY ROLLUP(c1, c2, c3), ROLLUP generates the GROUP BY aggregate rows for each unique combination of values of (c1, c2, c3), plus superaggregate rows for each unique combination of values of (c1, c2), and (c1).

ROLLUP also generates a superaggregate row for the entire set of input rows.

The order of the columns specified in ROLLUP() can change the result and the number of rows in the result set.

List each employee's salary, the subtotal of all salaries in each department, and the total salary amount:

```
SELECT deptno, empno, SUM(sal) AS salary,
```

```
CASE GROUPING(deptno, empno) WHEN 0 THEN ' ' WHEN 1 THEN 'department total' WHEN 3 THEN 'grand total' END
```

```
FROM salary GROUP BY ROLLUP(deptno, empno);
```

```

```

```
deptno     empno     salary     col4--------------------------------------------
```

```
(null)     (null)     46800     grand total
```

```
100        (null)      4400     department total
```

```
300        (null)      8800     department total
```

```
400        (null)      6500     department total
```

```
500        (null)     10400     department total
```

```
800        (null)     16700     department total
```

```
100          840       4400
```

```
300          499       1150
```

```
300          521       1400
```

```
300          654       1500
```

```
300          698        850
```

```
300          844       1150
```

```
300          900       2750
```

```
400          789       6500
```

```
500          299       3900
```

```
500          371       2200
```

```
500          473       2200
```

```
500          902       2100
```

```
800            5      10500
```

```
800          854       6200
```

CUBE generates the GROUP BY aggregate rows, plus superaggregate rows for each unique combination of expressions in the column list. So CUBE(c1, c2, c3) produces aggregate rows for each unique combination of (c1, c2, c3), as well as superaggregate rows for each unique combination of values of (c1, c2), (c1, c3), (c2, c3), (c1), (c2), and (c3), and a grand total row for the entire set of input rows. The order of the columns specified in CUBE() has no effect.

CUBE is useful for situations that require cross-tabular reports.

Show each job and salary by department, totals for each department, and totals for the entire company:

```
SELECT deptno,
```

```
       job,
```

```
       count(*),
```

```
       sum(sal)
```

```
  FROM emp
```

```
 GROUP BY CUBE(deptno,job);
```

```

```

```
   DEPTNO JOB         COUNT(*)   SUM(SAL)
```

```
--------- --------- ---------   ---------
```

```
       10 CLERK              1       1300
```

```
       10 DIRECTOR           1       2450
```

```
       10 CEO                1       9000
```

```
       10                    3      12750
```

```

```

```
       20 CLERK              2       1300
```

```
       20 PROGRAMMER         2       5000
```

```
       20 DIRECTOR           1       2975
```

```
       20                    5       9275
```

```

```

```
       30 CLERK              1        950
```

```
       30 DIRECTOR           1       2850
```

```
       30 SALESMAN           4       5600
```

```
       30                    6       9400
```

```

```

```
          PROGRAMMER         2       5000
```

```
          CLERK              4       3550
```

```
          DIRECTOR           3       8275
```

```
          CEO                1       9000
```

```
          SALESMAN           4       5600
```

```
                            14      31425
```

The GROUPING SETS syntax lets you define multiple independent sets of grouping columns on which the aggregates are to be computed. You can specify GROUPING SETS when you do not need all the groupings that are generated by using ROLLUP or CUBE and when aggregations are required on distinct sets of grouping columns. ROLLUP and CUBE are simply special short forms for specific sets of GROUPING SETS.

Each grouping set defines a set of columns for which an aggregate result is computed. The final result set is the set of distinct rows from the individual grouping column specifications in the grouping sets. GROUPING SETS syntax can be defined over simple column sets or CUBEs or ROLLUPs. In effect, CUBE and ROLLUP are simply short forms for specific varieties of GROUPING SETS.

A GROUPING SETS query can be considered to be simply a UNION of each of the individual groupings defined in the GROUPING SETs syntax (or CUBE or ROLLUP).

Show sales totals for division and region:

```
SELECT division, region, SUM(sales) AS sales FROM div_sales
```

```
GROUP BY GROUPING SETS (division, region);
```

```

```

```
division     region     sales
```

```
-----------------------------
```

```
capital      (null)        58
```

```
energy       (null)       155
```

```
technology   (null)       206
```

```
home         (null)       109
```

```
(null)       us           174
```

```
(null)       europe       124
```

```
(null)       pacific       86
```

```
(null)       americas      80
```

```
(null)       mea           64
```

The empty grouping set—GROUP BY()—simply defines an aggregation to be computed over the entire source set of rows (a simple aggregate).

The GROUPING() function (see [GROUPING](../SQLLanguage/SQL_Functions.md)) can be used to simplify a query that needs many GROUP BY levels. The function argument is a list of one or more columns or expressions in parentheses. Each parameter must appear in the GROUP BY clause. The result is an integer consisting of “n” binary digits, where “n” is the number of parameters to the function. For each result row of the grouped query, the digit corresponding to the nth parameter of the GROUPING function is 0 if the result row is based on a value of the nth parameter, else 1.

For example, for the following clause:

```
GROUP BY CUBE (c1, c2, c3)
```

GROUPING(c1, c2, c3) returns 0 for the <C1, C2, C3> rows, 4 for the <C2, C3> rows, 1 for the <C1, C2> rows, and so forth. Likewise, GROUPING(C3, C1) returns 3 for <C2> rows, 1 for <C3> rows, 0 for <C1, C3> rows and <C1, C2, C3> rows.

### HAVING Clause

The HAVING clause filters the results of the GROUP BY clause by using an aggregate function. The HAVING clause uses the same restriction operators as the WHERE clause.

For example, to return parts that have sold more than ten times on a particular day during the past week:

```
SELECT odate, partno, count(*) FROM ordersGROUP BY odate, partnoWHERE odate >= (CURRENT_DATE - INTERVAL '7' day)HAVING count(*) > 10;
```

Any columns or expressions contained in the HAVING clause must follow the same limitations described for the SELECT clause.

### ORDER BY Clause

The ORDER BY clause allows you to specify the columns on which the results table is to be sorted. For example, if the employees table contains the following data:

| emp_name | dept_no | manager |
| --- | --- | --- |
| Murtagh | Shipping | Myron |
| Obidinski | Lumber | Myron |
| Reilly | Finance | Costello |
| Barth | Lumber | Myron |
| Karol | Editorial | Costello |
| Smith | Shipping | Myron |
| Loram | Editorial | Costello |
| Delore | Finance | Costello |
| Kugel | food prep | Snowden |

then this query:

```
SELECT manager, emp_name, dept_no FROM employee_dimORDER BY manager, dept_no, emp_name
```

produces the following list of managers, the departments they manage, and the employees in each department:

| Manager | Department | Employee |
| --- | --- | --- |
| Costello | Editorial | Karol |
| Costello | Editorial | Loram |
| Costello | Finance | Delore |
| Costello | Finance | Reilly |
| Myron | Lumber | Barth |
| Myron | Lumber | Obidinski |
| Myron | Shipping | Murtagh |
| Myron | Shipping | Smith |
| Snowden | food prep | Kugel |

and this query:

```
SELECT emp_name, dept_no, manager FROM employee_dimORDER BY emp_name
```

produces this alphabetized employee list:

| Employee | Department | Manager |
| --- | --- | --- |
| Barth | Lumber | Myron |
| Delore | Finance | Costello |
| Karol | Editorial | Costello |
| Kugel | food prep | Snowden |
| Loram | Editorial | Costello |
| Murtagh | Shipping | Myron |
| Obidinski | Lumber | Myron |
| Reilly | Finance | Costello |
| Smith | Shipping | Myron |

To display result columns sorted in descending order (reverse numeric or alphabetic order), specify ORDER BY column_name DESC. For example, to display the employees in each department from oldest to youngest:

```
SELECT dept_no, emp_name, emp_age FROM employee_dimORDER BY dept_no, emp_age DESC;
```

If a nullable column is specified in the ORDER BY clause, nulls are sorted to the end of the results table by default. When using the DESC modifier the NULLS are moved to the beginning of the output. To modify this behavior use the NULLS LAST or NULLS FIRST modifier.

```
SELECT dcolumn FROM dtestUNION ALLSELECT zcolumn FROM ztestORDER BY dcolumn NULLS FIRST;
```

```
SELECT dcolumn FROM dtestUNION ALLSELECT zcolumn FROM ztestORDER BY dcolumn DESC NULLS LAST;
```

**Notes:**

- If the ORDER BY clause is omitted, the order of the rows in the results table is not guaranteed to have any relationship to the****storage structure or key structure of the source tables.
- There may be occasions where a column name is repeated in the output of an SQL statement, for example, where the same column name is repeated over several tables used in a join. The parser does not generate an error where such an ambiguity exists.

    In such cases, we recommend that you clarify your intent by qualifying the column used in the ORDER BY clause by using its table name as a prefix.

In union selects, the result column names must either be the column names from the SELECT clause of the first SELECT statement, or the number of the result column. For example:

```
SELECT dcolumn FROM dtestUNION ALLSELECT zcolumn FROM ztestORDER BY dcolumn
```

In addition to specifying individual column names as the ordering-expressions of the ORDER BY clause, the results table can also be sorted on the value of an expression.

For example, the query:

```
SELECT emp_name, dept_no, manager FROM employee_dim       ORDER BY manager||dept_no
```

produces the employee list ordered on the concatenation of the manager and dept_no values.

| emp_name | dept_no | manager |
| --- | --- | --- |
| Loram | Editorial | Costello |
| Karol | Editorial | Costello |
| Delore | Finance | Costello |
| Reilly | Finance | Costello |
| Murtagh | Shipping | Myron |
| Obidinski | Lumber | Myron |
| Barth | Lumber | Myron |
| Smith | Shipping | Myron |
| Kugel | food prep | Snowden |

ORDER BY BOOLEAN results in grouping rows in the order: FALSE, TRUE, NULL unless other modifiers are applied.

!!! note "Note"

    The ORDER BY clause must contain a column name or expression that is in the select list.

Incorrect:

```
SELECT DISTINCT col1, col2 FROM table ORDER BY col3;
```

Correct:

```
SELECT DISTINCT col1, col2, col3 FROM table ORDER BY col3;
```

```
SELECT DISTINCT emp_name, dept_no, employee_id FROM employee_dim ORDER BY employee_id;
```

### LIMIT Clause

The LIMIT clause syntax is `LIMIT``n` where n is a positive integer. It limits the result set to the specified number of rows. For example, the following query returns 50 rows from the result set:

```
SELECT * FROM mytable LIMIT 50
```

### FETCH FIRST Clause and OFFSET Clause

The OFFSET clause and FETCH FIRST clause are used to return a subset of rows from a result set.

A query can use any combination of the ORDER BY, OFFSET, and FETCH FIRST clauses, but in that order only.

The OFFSET and FETCH FIRST clauses can be used only once per query, and cannot be used in unions or view definitions. They cannot be used in subselects, except a subselect in a CREATE TABLE statement or an INSERT statement.

The FETCH FIRST clause cannot be used in the same SELECT statement as SELECT FIRST rowcount.

The OFFSET clause syntax is as follows:

```
OFFSET n
```

where n is a positive integer, a host variable, or a procedure parameter or local variable.

For example, the following query returns rows starting from the 25th row of the result set:

```
SELECT * FROM MYTABLE ORDER BY COL1 OFFSET 25
```

The FETCH FIRST clause syntax is as follows:

```
FETCH FIRST n ROWS ONLY
```

where n is a positive integer, a host variable, or procedure parameter or local variable.

For example, the following query fetches only the first 10 rows of the result set:

```
SELECT * FROM MYTABLE ORDER BY COL1 FETCH FIRST 10 ROWS ONLY
```

In the FETCH FIRST clause, the keywords FIRST and NEXT, and the keywords ROWS and ROW are interchangeable. Because you can offset and fetch first in the same query, NEXT is an alternative for readability. For example:

```
OFFSET 10 FETCH NEXT 25 ROWS ONLY
```

### UNION Clause

The UNION clause combines the results of SELECT statements into a single result table.

The following example lists all employees in the table of active employees plus those in the table of retired employees:

```
SELECT ename FROM active_empsUNIONSELECT ename FROM retired_emps;
```

By default, the UNION clause eliminates any duplicate rows in the result table. To retain duplicates, specify UNION ALL. Any number of SELECT statements can be combined using the UNION clause, and both UNION and UNION ALL can be used when combining multiple tables.

If you know that the result sets you want to combine from the different SELECT statements are unique, or if uniqueness is not a concern, then use UNION ALL to get better performance.

Unions are subject to the following restrictions:

- The SELECT statements must return the same number of columns.
- The columns returned by the SELECT statements must correspond in order and data type, although the column names do not have to be identical.

- The SELECT statements cannot include individual ORDER BY clauses.

To sort the result table, specify the ORDER BY clause following the last SELECT statement. The result columns returned by a union are named according to the first SELECT statement.

By default, unions are evaluated from left to right. To specify a different order of evaluation, use parentheses.

Any number of SELECT statements can be combined using the UNION clause. A maximum of 126 tables is allowed in a query.

### INTERSECT Clause

The INTERSECT clause takes the results of two SELECT statements and returns only rows that appear in both result tables. INTERSECT removes duplicate rows from the final result table. INTERSECT does not support the ALL option.

The following example returns all rows from the employee table where salary is between 75000 and 100000:

```
SELECT * FROM employee WHERE salary >= 75000
```

```
INTERSECT
```

```
SELECT * FROM employee WHERE salary <= 100000;
```

### EXCEPT Clause

The EXCEPT clause takes the results of two SELECT statements and returns the rows of the first result table that do not appear in the second result table. EXCEPT removes duplicate rows from the final result table. EXCEPT does not support the ALL option.

The following example returns all rows from the employee table where salary is greater than 100000:

```
SELECT * FROM employee WHERE salary >= 75000
```

```
EXCEPT
```

```
SELECT * FROM employee WHERE salary <= 100000;
```

### WITH Clause for SELECT

The WITH clause on the SELECT statement consists of a comma-separated list of one or more of the following options:

**[NO]QEP**

:   Specifies whether to display a diagrammatic representation of the query execution plan chosen for the query by the optimizer.

:   Default: WITH NOQEP

**[NO]GREEDY**

:   Enables or disables the exhaustive enumeration heuristic of the query optimizer for complex queries.

:   When the query references a large number of tables, the greedy enumeration heuristic enables the optimizer to produce a query plan much faster than with its default technique of exhaustive searching for query execution plans.

**MAX_PARALLEL n**

:   Sets the parallelism level for the query, where n is an integer from 1 to 256.

:   The value of n should not exceed the number of CPU cores visible to the operating system. Your query may run at a lower level of parallelism than requested if other parallel queries are running concurrently.

**[NO]UNION_FLATTEN**

:   Turns union flattening on or off. Overrides the SET [NO]UNION_FLATTENING statement for the duration of the statement.

## Query Evaluation

The logic applied to the evaluation of SELECT statements, as described here, does not precisely reflect how Actian Data Platform evaluates your query to determine the most efficient way to return results. However, by applying this logic to your queries and data, the results of your queries can be anticipated.

1. **Evaluate the FROM clause.**

    Combine all the sources specified in the FROM clause to create aCartesian product (a table composed of all the rows and columns of the sources). If joins are specified, evaluate each join to obtain its results table, combine it with the other sources in the FROM clause. If SELECT DISTINCT is specified, discard duplicate rows.

2. **Apply the WHERE clause.**

    Discard rows in the result table that do not fulfill the restrictions specified in the WHERE clause.

3. **Apply the GROUP BY clause.**

    Group results according to the columns specified in the GROUP BY clause.

4. **Apply the HAVING clause.**

    Discard rows in the result table that do not fulfill the restrictions specified in the HAVING clause.

5. **Evaluate the SELECT clause.**

    Discard columns that are not specified in the SELECT clause. (In case of SELECT FIRST n… UNION SELECT …, the first n rows of the result from union are chosen.)

6. **Perform any intersections, unions, or exceptions**.

    Combine result tables as specified in the UNION, INTERSECT, or EXCEPT clause.

    INTERSECT takes precedence over UNION and EXCEPT. For example, in SELECT…UNION SELECT …INTERSECT SELECT… will perform the INTERSECT first, then the UNION.

    In case of SELECT FIRST n… UNION SELECT …, the first n rows of the result from union are chosen.

7. **Apply the ORDER BY clause.**

    Sort the result rows as specified.

## Syntax for Specifying Tables and Views

The syntax rules for specifying table names in queries also apply to views.

To select data from a table you own, specify the name. To select data from a table you do not own, specify schema.table, where schema is the name of the user that owns the table. However, if the table is owned by the database DBA, the schema qualifier is not required. You must have the appropriate permissions to access the table (or view) granted by the owner.

A correlation name can be specified for any table in the FROM clause. A correlation name is an alias (or alternate name) for the table. For example:

```
SELECT... FROM employees e, managers m...
```

The preceding example assigns the correlation name “e” to the employees table and “m” to the managers table. Correlation names are useful for abbreviating long table names and for queries that join columns in the same table.

If a correlation name is assigned to a table, the table must be referred to by the correlation name. For example:

Correct:

```
SELECT e.name, m.name FROM employees e, managers m...
```

Incorrect:

```
SELECT employees.name, managers.name FROM employees e, managers m...
```

## Joins

Joins combine information from multiple tables and views into a single result table, according to column relationships specified in the WHERE clause.

For example, given the following two tables:

| ename | edeptno |
| --- | --- |
| Benny Barth | 10 |
| Dean Reilly | 11 |
| Rudy Salvini | 99 |
| Tom Hart | 123 |

**Department Table**

| ddeptno | dname |
| --- | --- |
| 10 | Lumber |
| 11 | Sales |
| 99 | Accounting |
| 123 | Finance |

The following query joins the two tables on the relationship of equality between values in the edeptno and ddeptno columns. The result is a list of employees and the names of the departments in which they work:

```
SELECT ename, dname FROM employees, departments       WHERE edeptno = ddeptno;
```

A table can be joined to itself using correlation names; this is useful when listing hierarchical information. For example, the following query displays the name of each employee and the name of the manager for each employee.

```
SELECT e.ename, m.ename        FROM employees e, employees m       WHERE e.mgr = m.eno
```

Tables can be joined on any number of related columns. The data types of the join columns must be comparable.

### Join Relationships

The simple joins illustrated in the two preceding examples depend on equal values in the join columns. This type of join is called an equijoin. Other types of relationships can be specified in a join. For example, the following query lists salespersons who have met or exceeded their sales quota:

```
SELECT s.name, s.sales_ytd       FROM sales s, quotas q       WHERE s.empnum = d.empnum AND              s.sales_ytd >= d.quota;
```

### ANSI/ISO Join Syntax

In addition to performing joins using the approach described in the Joins section, ANSI syntax described in the 1992 ANSI/ISO SQL standard can be used. The ANSI syntax provides a more precise way of specifying joins that are otherwise identical to those produced from the traditional syntax. The ANSI syntax also allows the specification of outer joins.

An outer join returns not only the rows of the join sources that join together according to a specified search condition, but also rows from one or both sources that do not have a matching row in the other source. For rows included in the outer join that do not have a matching row from the other source, null values are returned in all columns of the other source.

An outer join is the union of two SELECT statements: the first query returns rows that fulfill the join condition and the second query returns nulls for rows that do not fulfill the join condition.

The ANSI syntax is specified in the FROM clause, as follows:

```
source join_type JOIN source ON search_condition
```

or

```
source join_type JOIN source USING (column {,column})
```

or

```
source CROSS JOIN source
```

where:

**source**

:   Specifies the table, view, or join where the data for the left or right side of the join originates.

**join_type**

:   Specifies the type of join as one of the following:

INNER

:   (Default) Specifies an inner join.

LEFT [OUTER]

:   Specifies a left outer join, which returns all values from the left source.

RIGHT [OUTER]

:   Specifies a right outer join, which returns all values from the right source.

FULL [OUTER]

:   Specifies a full outer join, which returns all values from both left and right sources.

!!! note "Note"

    RIGHT and LEFT joins are the mirror image of each other: (table1 RIGHT JOIN table2) returns the same results as (table2 LEFT JOIN table1).

**ON search_condition**

:   Is a valid restriction, subject to the rules for the WHERE clause. The search_condition must not include aggregate functions or subselects. Matching pairs of rows in the join result are those that satisfy the search_condition.

**USING (column {,column})**

:   Is an alternate form of the search_condition. Each column in the USING clause must exist unambiguously in each join source. An ON search_conditionis effectively generated in which the search_condition compares the columns of the USING clause from each join source.

**CROSS JOIN**

:   Is a cross product join of all rows of the join sources.

By default, joins are evaluated left to right. To override the default order of evaluation, use parentheses. A join source can itself be a join, and the results of joins can be joined with the results of other joins, as illustrated in the following pseudocode:

```
(A join B) join (C join D)
```

The placement of restrictions is important in obtaining correct results. For example:

```
A join B on cond1 and cond2
```

does not return the same results as:

```
A join B on cond1 where cond2
```

In the first example, the restriction determines which rows in the join result table are assigned null values; in the second example, the restriction determines which rows are omitted from the result table.

The following examples are identical and use an outer join in the FROM clause to display all employees along with the name of their department, if any. One uses the ON clause and the other uses an equivalent USING clause:

```
SELECT e.ename, d.dname FROM(employees e LEFT JOIN departments d ON e.dept = d.dept);
```

```
SELECT e.ename, d.dname FROM(employees e LEFT JOIN departments d USING (dept));
```

#### Cross Join Example

The following is an example of a cross join. A cross join returns a Cartesian product. Every row of one table is combined with every row of another table.

```
SELECT
```

```
      e.last_name,
```

```
      d.dept_name
```

```
FROM
```

```
      emp e CROSS JOIN dept d;
```

```

```

```
last_name  dept_name
```

```
Smith      HR
```

```
Smith      Sales
```

```
Smith      Admin
```

```
Smith      Support
```

```
Smith      Services
```

```
Jones      HR
```

```
Jones      Sales
```

```
Jones      Admin
```

```
Jones      Support
```

```
Jones      Services
```

```
Green      HR
```

```
Green      Sales
```

```
Green      Admin
```

```
Green      Support
```

```
Green      Services
```

```
White      HR
```

```
White      Sales
```

```
White      Admin
```

```
White      Support
```

```
White      Services
```

```
Mustard    HR
```

```
Mustard    Sales
```

```
Mustard    Admin
```

```
Mustard    Support
```

```
Mustard    Services
```

```
Scarlet    HR
```

```
Scarlet    Sales
```

```
Scarlet    Admin
```

```
Scarlet    Support
```

```
Scarlet    Services
```

The cross join is equivalent to joining tables and leaving off the WHERE clause.

```
SELECT
```

```
      e.last_name,
```

```
      d.dept_name
```

```
FROM
```

```
      emp e,
```

```
      dept d;
```

## SELECT Examples

1. Find the amount of business that was billed, shipped, and returned in the last quarter of 2011:

```
SELECT   l_returnflag, l_linestatus, sum(l_quantity) as sum_qty,
```

```
         sum(l_extendedprice) as sum_base_price,
```

```
         sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
```

```
         sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
```

```
         avg(l_quantity) as avg_qty, avg(l_extendedprice) as avg_price,
```

```
         avg(l_discount) as avg_disc, count(*) as count_order
```

```
FROM     lineitem
```

```
WHERE    l_shipdate <= date '2011-12-01' - interval '90' day
```

```
GROUP BY l_returnflag, l_linestatus
```

```
ORDER BY l_returnflag, l_linestatus;
```

2. Find the top ten brands for sales orders placed in 2011:

```
SELECT FIRST 10 p.p_brand, SUM(l_extendedprice) total_priceFROM lineitem lINNER JOIN part p ON p.p_partkey = l.l_partkeyINNER JOIN orders o ON o.o_orderkey = l.l_orderkeyWHERE o.o_orderdate BETWEEN '2011-01-01' AND '2011-12-31'GROUP BY p.p_brandORDER BY total_price DESC;
```
