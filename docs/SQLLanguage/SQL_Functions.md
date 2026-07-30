---
title: "SQL Functions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_Functions.htm"
canonical_id: "actian-data-platform-sql-functions"
---

## SQL Functions

Functions can be used in the following SQL statements:

- SELECT
- INSERT

- UPDATE
- DELETE

## Aggregate Functions

Aggregate functions return a single value, calculated from values in a column. They take a set of values as their argument. Aggregate functions are also called set functions.

### Basic Aggregate Functions

A basic aggregate function returns a single value by aggregating multiple rows of data.

The syntax of a basic aggregate function is as follows:

```
function_name ([DISTINCT | ALL] expr)
```

where:

function_name denotes an aggregate function.

expr denotes any expression that does not include an aggregate function reference (at any level of nesting).

DISTINCT eliminates duplicate values of exprwithin a set of input rows to the aggregation. ALL (the default) retains duplicate values of expr.

Null values of exprare ignored by the aggregate functions, with the exception of COUNT(*).

The following example uses the SUM aggregate function to calculate the total of salaries for employees in department 23:

```
SELECT SUM (employee.salary)       FROM employee       WHERE employee.dept = 23;
```

**ANY**

```
ANY
```

:   Result type: INTEGER

:   Returns 1 if any row in the table fulfills the where clause, or 0 if no rows fulfill the WHERE clause.

**AVG**

```
AVG
```

:   Result type: FLOAT, MONEY, DATE (INTERVAL only)

:   Returns the average (sum / count). The sum of the values must be within the range of the result data type.

**COUNT**

```
COUNT
```

:   Result type: INTEGER8

:   Returns count of non-null occurrences.

:   For example, count the number of employees allocated to a department:

```
SELECT COUNT(dept)
```

```
       FROM employee;
```

!!! note "Note"

    Returns INTEGER4 when used against Ingres tables.

:   COUNT_BIG is a synonym for COUNT.

**COUNT(*)**

```
COUNT(*)
```

:   Result type: INTEGER8

:   Returns count of the number of rows in a result table, including rows that contain nulls.

:   For example, the following statement counts the number of employees in department 'PERS':

```
SELECT COUNT(*)       FROM employee       WHERE dept = 'PERS';
```

:   The asterisk (*) argument cannot be qualified with ALL or DISTINCT.

:   Because COUNT(*) counts rows rather than columns, it does not ignore nulls. Consider the following table:

```
NAME               EXEMPTIONS
```

```
Smith              0
```

```
Jones              2
```

```
Tanghetti          4
```

```
Fong               Null
```

```
Stevens            Null
```

:   The expression:

```
COUNT(exemptions)
```

:   returns the value of 3, whereas:

```
COUNT(*)
```

:   returns 5.

:   If the argument to the COUNT function evaluates to an empty set, COUNT returns zero, which is in contrast to other functions, which return a null.

**GROUPING**

```
GROUPING
```

:   Result type: INTEGER

:   Returns an integer value based on its parameters.

:   It can be used to simplify a query that needs many GROUP BY levels by letting you more easily express row filtering conditions.

:   The GROUPING function can have multiple parameters, each of which must be a column or expression in the GROUP BY clause of an aggregate query. The parameters from right to left are represented in the function result by bits from right to left.

:   When CUBE, ROLLUP, or GROUPING SETS syntax is used, result rows from the query can be formed based on the grouping of rows according to different combinations of the grouping columns or expressions. If a result row is based on a grouping that includes a parameter of the grouping function, its bit position in the GROUPING() function result is 0, otherwise 1. This helps you determine which groupings each of the result rows comes from.

:   For example:

```
SELECT sno, pno, SUM(qty), GROUPING(sno, pno) FROM sp    GROUP BY CUBE(sno, pno)
```

:   produces results like:

```
s1   p1   25   0
```

```
s1   p2   30   0
```

```
...
```

```
s1       100   1
```

```
s2        50   1
```

```
...
```

```
     p1   95   2
```

```
     p2   10   2
```

```
...
```

```
        1000   3
```

:   The numbers 0, 1, 2, and 3 are the results of the GROUPING() function. Rows with both sno and pno have a GROUPING() value of 0 because they result from the grouping of both sno and pno. Rows with only sno (superaggregate rows grouped only on sno) have a value of 1 because the rightmost parameter (pno) does not contribute to the grouping. Rows with only pno (superaggregates grouped only on pno) have a value of 2 because the next parameter (sno—in bit position 2) does not contribute. And the last row has a value of 3 because neither sno nor pno are involved in the grouping.

**MAX**

```
MAX
```

:   Result type: Same as argument

:   Returns maximum value.

**MEDIAN**

```
MEDIAN(expr)
```

:   Operand type: All numeric types and ANSIDATE

:   Result type: Same as argument

:   Returns an expression that is the middle of a sorted list of the input expressions. Nulls are ignored. If the number of input expressions is odd, the result is from the expression list. If it is even, the result is the interpolation between the two middle expressions, rounding up for integer expressions.

!!! note "Note"

    The DISTINCT and ALL keywords are not supported.

:   For example:

```
SELECT * FROM temperatures
```

```

```

```
+--------------------+-------------+-----+
```

```
|city                |station      |temp |
```

```
+--------------------+-------------+-----+
```

```
|Los Angeles         |            1| 71.5|
```

```
|Los Angeles         |            2| 72.5|
```

```
|Los Angeles         |            3| 73.5|
```

```
|Los Angeles         |            4| 74.5|
```

```
|Seattle             |            1| 62.5|
```

```
|Seattle             |            2| 64.5|
```

```
|Seattle             |            3| 64.5|
```

```
|Seattle             |            4| 65.5|
```

```
|Seattle             |            5| 66.5|
```

```
+--------------------+-------------+-----+
```

```
(9 rows)
```

```

```

```
SELECT city, MEDIAN (temp) AS median_temp FROM temperatures GROUP BY city
```

```

```

```
+--------------------+-----------------------------------------+
```

```
|city                |median_temp                              |
```

```
+--------------------+-----------------------------------------+
```

```
|Los Angeles         |                                    73.00|
```

```
|Seattle             |                                    64.50|
```

```
+--------------------+-----------------------------------------+
```

```
(2 rows)
```

**MIN**

```
MIN
```

:   Result type: Same as argument

:   Returns minimum value.

**PERCENTILE_CONT**

```
PERCENTILE_CONT(n) WITHIN GROUP(ORDER BY expr)
```

:   Operand type: All numeric types and ANSIDATE

:   Result type: Same as argument

:   Returns a value that corresponds to the given fraction (n) in the sort order, where 0 <= n <= 1. Sorts the input expressions and returns a single expression that is greater than n of the input expressions. Nulls are ignored. For example, if n is .8, the aggregate result will be >= 80% of the input values. The result may be an interpolated value if no input exactly delineates the percentile, rounding up for integer expressions.

:   PERCENTILE_CONT (.5)... is the same as MEDIAN.

!!! note "Note"

    The DISTINCT and ALL keywords are not supported.

:   For example:

```
SELECT city, PERCENTILE_CONT(.75) WITHIN GROUP (ORDER BY temp) AS seventy_fifth_percentile FROM temperatures GROUP BY city
```

```

```

```
+--------------------+-----------------------------------------+
```

```
|city                |seventy_fifth_percentile                 |
```

```
+--------------------+-----------------------------------------+
```

```
|Los Angeles         |                                    73.80|
```

```
|Seattle             |                                    65.50|
```

```
+--------------------+-----------------------------------------+
```

```
(2 rows)
```

**STDDEV_POP**

```
STDDEV_POP
```

:   Result type: FLOAT

:   Computes the population form of the standard deviation (square root of the population variance of the group).

**STDDEV_SAMP**

```
STDDEV_SAMP
```

:   Result type: FLOAT

:   Computes the sample form of the standard deviation (square root of the sample variance of the group).

**SUM**

```
SUM
```

:   Result type: INTEGER, FLOAT, MONEY, DATE (INTERVAL only)

:   Returns column total.

**VAR_POP**

```
VAR_POP
```

:   Result type: FLOAT

:   Computes the population form of the variance (sum of the squares of the difference of each argument value in the group from the mean of the values, divided by the count of the values).

**VAR_SAMP**

```
VAR_SAMP
```

:   Result type: FLOAT

:   Computes the sample form of the variance (sum of the squares of the difference of each argument value in the group from the mean of the values, divided by the count of the values minus 1).

### Regression and Correlation Analysis Aggregate Functions

The following aggregate functions perform a variety of regression and correlation analysis.

Syntax is as follows:

```
function_name(indep_parm, dep_parm)
```

where function_name denotes the function name and the first argument is the independent variable and the second argument is the dependent variable.

Functions for regression and correlation analysis are as follows:

**CORR**

```
CORR(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns correlation coefficient (ratio of the population covariance divided by the product of the population standard deviation of the independent variable and the population standard deviation of the dependent variable).

**COVAR_POP**

```
COVAR_POP(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns population covariance (sum of the products of the difference of the independent variable from its mean, times the difference of the dependent variable from its mean, divided by the number of rows).

**COVAR_SAMP**

```
COVAR_SAMP(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns sample covariance (sum of the products of the difference of the independent variable from its mean, times the difference of the dependent variable from its mean, divided by the number of rows minus 1).

**REGR_AVGX**

```
REGR_AVGX(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns average of the independent variables.

**REGR_AVGY**

```
REGR_AVGY(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns average of the dependent variables.

**REGR_COUNT**

```
REGR_COUNT(indep_parm, dep_parm)
```

:   Result type: INTEGER

:   Returns count of rows with non-null values for both dependent and independent variables.

**REGR_INTERCEPT**

```
REGR_INTERCEPT(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns Y-intercept of the least-squares-fit linear equation determined by the (independent variable, dependent variable) pairs.

**REGR_R2**

```
REGR_R2(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns square of the correlation coefficient.

**REGR_SLOPE**

```
REGR_SLOPE(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns slope of the least-squares-fit linear equation determined by the (independent variable, dependent variable) pairs.

**REGR_SXX**

```
REGR_SXX(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns the sample corrected sum of the squares of the independent variable.

**REGR_SXY**

```
REGR_SXY(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns sum of the product of the independent variable and the dependent variable.

**REGR_SYY**

```
REGR_SYY(indep_parm, dep_parm)
```

:   Result type: FLOAT

:   Returns the sample corrected sum of the squares of the dependent variable.

### String Aggregate Functions

String aggregate functions concatenate a set of string values.

**LISTAGG**

```
LISTAGG ([DISTINCT] value_expr [, 'delimiter'])     [WITHIN GROUP (order-by-clause)]
```

:   Concatenates expressions within a group.

:   Result type: VARCHAR(4000). Longer strings are truncated.

:   where:

DISTINCT

:   Eliminates duplicate values.

value_expr

:   Specifies an expression that can appear in the select list of a query. Can contain constants, row values, operators, scalar functions, and scalar subqueries. Null values in the value_expr column are ignored. The value is cast to char data type before being concatenated.

'delimiter'

:   Defines the separator between concatenated items. The default separator is the empty string.

WITHIN GROUP (order-by-clause)

:   Specifies how the items in the result should be sorted.

:   The following LISTAGG examples are based on this table:

```
DEPT             EMPNO FIRSTNAME  LASTNAME
```

```
----------- ---------- ---------- ----------
```

```
Marketing          101 Douglas    Cray
```

```
Marketing          103 Dong       Luang
```

```
Marketing          105 Dennis     Indolay
```

```
Admin              107 Sherry     Keller
```

```
Admin              109 Carl       Nader
```

```
Admin              111 Ruth       Turret
```

```
Sales              113 Andrew     Bonnet
```

```
Sales              115 Oscar      Hender
```

```
Sales              117 Justin     Braushere
```

```
Sales              119            Smith
```

:   Concatenate the names of all employees, ordered by last name (LISTAGG used as a simple aggregate):

```
SELECT LISTAGG(lastname)     WITHIN GROUP (ORDER BY lastname) AS PERSONNEL     FROM employee;
```

```
PERSONNEL
```

```
-----------------------------------------------------------
```

```
BonnetBraushereCrayHenderIndolayKellerLuangNaderSmithTurret
```

:   Same as previous query, but use a delimiter to separate names with a comma:

```
SELECT LISTAGG(lastname, ',')     WITHIN GROUP (ORDER BY lastname) AS PERSONNEL     FROM employee;
```

```
PERSONNEL
```

```
--------------------------------------------------------------------
```

```
Bonnet,Braushere,Cray,Hender,Indolay,Keller,Luang,Nader,Smith,Turret
```

:   Concatenate employees in each department, ordered by last name (LISTAGG used as a regular aggregate with GROUP BY):

```
SELECT dept, LISTAGG(lastname, ',')     WITHIN GROUP (ORDER BY lastname) AS PERSONNEL     FROM employee GROUP BY dept;
```

```
DEPT        PERSONNEL
```

```
----------- ------------------------------
```

```
Admin       Keller,Nader,Turret
```

```
Marketing   Cray,Indolay,Luang
```

```
Sales       Bonnet,Braushere,Hender,Smith
```

:   Concatenate employee names in the same department, ordered by last name, partitioned by department (LISTAGG used as a windowing aggregate):

```
SELECT dept, firstname, lastname, LISTAGG(lastname, ',')     WITHIN GROUP(ORDER BY lastname)     OVER (PARTITION BY dept) AS PERSONNEL     FROM employee ORDER BY dept, lastname, firstname;
```

```
DEPT        FIRSTNAME  LASTNAME   PERSONNEL IN SAME DEPT
```

```
----------- ---------- ---------- ------------------------------
```

```
Admin       Sherry     Keller     Keller,Nader,Turret
```

```
Admin       Carl       Nader      Keller,Nader,Turret
```

```
Admin       Ruth       Turret     Keller,Nader,Turret
```

```
Marketing   Douglas    Cray       Cray,Indolay,Luang
```

```
Marketing   Dennis     Indolay    Cray,Indolay,Luang
```

```
Marketing   Dong       Luang      Cray,Indolay,Luang
```

```
Sales       Andrew     Bonnet     Bonnet,Braushere,Hender,Smith
```

```
Sales       Justin     Braushere  Bonnet,Braushere,Hender,Smith
```

```
Sales       Oscar      Hender     Bonnet,Braushere,Hender,Smith
```

```
Sales                  Smith      Bonnet,Braushere,Hender,Smith
```

### Ordering Aggregate Functions

Ordering aggregate functions order the aggregated rows.

**FIRST_VALUE WITHIN GROUP and LAST_VALUE WITHIN GROUP**

```
FIRST_VALUE (scalar_value_expression) [null_specification] WITHIN GROUP (order_by_clause)...[group_by_clause]
```

```
LAST_VALUE (scalar_value_expression) [null_specification] WITHIN GROUP (order_by_clause)...[group_by_clause]
```

:   Produces one row per group, or if there is no group_by_clause, a single row

:   where:

scalar_value_expr

:   Specifies any scalar expression that can appear in the select list of a query. Can contain constants, row values, operators, scalar functions, and scalar subqueries.

null specification

:   Indicates whether to include null values in the selection of a first_value or last_value. Valid values are:

RESPECT NULLS

:   (Default) Uses the expression value in the first or last row.

IGNORE NULLS

:   Uses the first or last non-null expression value.

:   The following query shows the employee number (empno) of the highest paid employee in each department:

```
SELECT deptno, FIRST_VALUE(empno)
```

```
WITHIN GROUP (ORDER BY sal DESC) AS "FIRST VALUE"
```

```
FROM emp GROUP BY deptno;
```

```

```

```
    DEPTNO  FIRST VALUE
```

```
----------  -----------
```

```
       100          839
```

```
       200          788
```

```
       300          900
```

### Aggregate Functions and Decimal Data

Given decimal arguments, aggregate functions (with the exception of COUNT) return decimal results.

The following table explains how to determine the scale and precision of results returned for aggregates with decimal arguments:

| Function Name | Precision of Result | Scale of Result |
| --- | --- | --- |
| COUNT | Not applicable | Not applicable |
| SUM | 38 | Same as argument |
| AVG | 38 | Scale of argument + 1 (to a maximum of 38) |
| MAX | Same as argument | Same as argument |
| MEDIAN | Same as argument | Same as argument |
| MIN | Same as argument | Same as argument |
| PERCENTILE_CONT | Same as the ORDER BY expression | Same as the ORDER BY expression |

### GROUP BY Clause with Aggregate Functions

The GROUP BY clause allows aggregate functions to be performed on subsets of the rows in the table. The subsets are defined by the GROUP BY clause.

For example, the following statement selects rows from a table of political candidates, groups the rows by party, and returns the name of each party and the average funding for the candidates in that party.

```
SELECT party, AVG(funding)       FROM candidates       GROUP BY party;
```

### Restrictions on the Use of Aggregate Functions

The following restrictions apply to the use of aggregate functions:

- Aggregate functions cannot be nested.
- Aggregate functions can be used only in SELECT or HAVING clauses.

- If a SELECT or HAVING clause contains an aggregate function, columns not specified in the aggregate must be specified in the GROUP BY clause. For example:

```
SELECT dept, AVG(emp_age)FROM employeeGROUP BY dept;
```

    The above SELECT statement specifies two columns, dept and emp_age, but only emp_age is referenced by the aggregate function, AVG. The dept column must be specified in the GROUP BY clause.

## Window Functions

Window function syntax is required with analytical functions and can also be used with aggregate functions.

A window function is defined “over” a group of rows (a window) from a query. A window function produces a result value for each input row, where the value is computed according to the records in the current window.

A window is defined with an optional partitioning definition and an ordering definition.

- The partitioning defines sets of rows over which the function results are computed. Partitioning is similar to the grouping of a grouped query. Without the partitioning definition, the function will operate over the entire set of records returned by the query.
- The ordering defines the order of rows within a partition, which determines the function values.

!!! note "Note"

    The ordering does not define the order of result rows from the query. If the results of a query need to be sorted, a separate ORDER BY clause is required on the result set.

### Window Function Syntax

A window function has the following format:

```
window_function OVER window_specification
```

where:

**window_function**

:   Specifies an analytical function or an aggregate function.

:   A select list can have more than one function, each with a different OVER clause.

**OVER window_specification**

:   Specifies a named window specification defined elsewhere in the query or a parenthesized optional partitioning definition, ordering definition, and/or frame definition:

```
([PARTITION BY partitioning_list ] [ORDER BY sort_specification_list] [ROWS BETWEEN frame_bound1 AND frame_bound2])
```

**PARTITION BY partitioning_list**

:   Specifies a list of column names or expressions.

**ORDER BY sort_specification_list**

:   Specifies a list of column names or expressions optionally qualified by the ASC or DESC sort directions.

!!! note "Note"

    ORDER BY for an aggregate function is not supported.

**ROWS BETWEEN frame_bound1 AND frame_bound2**

:   Specifies the set of rows in the current partition over which the window function is computed.

:   Window functions that support frame definitions include the aggregates, FIRST_VALUE, and LAST_VALUE.

:   Aggregates support the following options:

ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

ROWS BETWEEN CURRENT ROW AND CURRENT ROW

ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING

:   FIRST_VALUE and LAST_VALUE support the option:

ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

**Note:**ORDER BY is required with frame specifications, even for aggregate functions.

!!! note "Note"

    DISTINCT is not allowed for COUNT, SUM, and AVG if the window specification includes an ORDER BY or a frame definition.

:   An empty window specification, that is, OVER(), causes the function results to be computed across all rows in the table.

### Windowing Aggregate Functions

Aggregate functions can be used as window functions; that is, you can use the OVER clause with aggregate functions.

!!! note "Note"

    The ORDER BY clause in the window specification is required with frame specifications, but is not supported for windowing aggregates without frame specifications.

Example:

This query computes, for each partition, the aggregate over the rows in that partition.

```
SELECT OrderID, ProductID, OrderQty
```

```
     ,SUM(OrderQty) OVER(PARTITION BY OrderID) AS "Total"
```

```
     ,AVG(OrderQty) OVER(PARTITION BY OrderID) AS "Avg"
```

```
     ,COUNT(OrderQty) OVER(PARTITION BY OrderID) AS "Count"
```

```
     ,MIN(OrderQty) OVER(PARTITION BY OrderID) AS "Min"
```

```
     ,MAX(OrderQty) OVER(PARTITION BY OrderID) AS "Max"
```

```
FROM SalesOrderDetail
```

```
WHERE OrderID IN(32548,32553);
```

Results:

```
OrderID   ProductID   OrderQty   Total   Avg   Count   Min   Max
```

```
  32548         776          1      26     2      12     1     6
```

```
  32548         777          3      26     2      12     1     6
```

```
  32548         778          1      26     2      12     1     6
```

```
  32548         771          1      26     2      12     1     6
```

```
  32548         772          1      26     2      12     1     6
```

```
  32548         773          2      26     2      12     1     6
```

```
  32548         774          1      26     2      12     1     6
```

```
  32548         714          3      26     2      12     1     6
```

```
  32548         716          1      26     2      12     1     6
```

```
  32548         709          6      26     2      12     1     6
```

```
  32548         712          2      26     2      12     1     6
```

```
  32548         711          4      26     2      12     1     6
```

```
  32553         772          1      14     1       8     1     4
```

```
  32553         775          4      14     1       8     1     4
```

```
  32553         714          1      14     1       8     1     4
```

```
  32553         716          1      14     1       8     1     4
```

```
  32553         777          2      14     1       8     1     4
```

```
  32553         771          3      14     1       8     1     4
```

```
  32553         773          1      14     1       8     1     4
```

```
  32553         778          1      14     1       8     1     4
```

The multiple coding of the window specification in this query could be avoided as follows:

```
SELECT OrderID, ProductID, OrderQty
```

```
     ,SUM(OrderQty) OVER win1 AS "Total"
```

```
     ,AVG(OrderQty) OVER win1 AS "Avg"
```

```
     ,COUNT(OrderQty) OVER win1 AS "Count"
```

```
     ,MIN(OrderQty) OVER win1 AS "Min"
```

```
     ,MAX(OrderQty) OVER win1 AS "Max"
```

```
FROM SalesOrderDetail
```

```
WHERE OrderID IN(32548,32553)
```

```
WINDOW win1 AS (PARTITION BY OrderID);
```

When the OVER clause is used without a window specification the function results are computed across all rows in the table. The following example returns the row count of the table for each row:

```
foobar(x INTEGER NOT NULL);
```

```
INSERT INTO foobar VALUES (1), (2), (2), (3), (3), (3);
```

```
SELECT x
```

```
    ,ROW_NUMBER() OVER(ORDER BY x) AS row_nbr
```

```
    ,COUNT(*) OVER() AS row_cnt
```

```
FROM foobar
```

```

```

```
x           row_nbr     row_cnt
```

```
-------------------------------
```

```
      1           1           6
```

```
      2           2           6
```

```
      2           3           6
```

```
      3           4           6
```

```
      3           5           6
```

```
      3           6           6
```

Example:

This query computes, for each partition, the sum over the rows in that partition up to the current row as ordered by the ProductID column.

```
SELECT OrderID, ProductID, OrderQty
```

```
     SUM(OrderQty) OVER(PARTITION BY OrderID ORDER BY ProductID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS "Running Total"
```

```
FROM SalesOrderDetail
```

```
WHERE OrderID IN(32548,32553);
```

Results:

```
OrderID    ProductID     OrderQty         Running Total
```

```
-------------------------------------------------------
```

```
  32548          709            6                     6
```

```
  32548          711            4                    10
```

```
  32548          712            2                    12
```

```
  32548          714            3                    15
```

```
  32548          716            1                    16
```

```
  32548          771            1                    17
```

```
  32548          772            1                    18
```

```
  32548          773            2                    20
```

```
  32548          774            1                    21
```

```
  32548          776            1                    22
```

```
  32548          777            3                    25
```

```
  32548          778            1                    26
```

```
  32553          714            1                     1
```

```
  32553          716            1                     2
```

```
  32553          771            3                     5
```

```
  32553          772            1                     6
```

```
  32553          773            1                     7
```

```
  32553          775            4                    11
```

```
  32553          777            2                    13
```

```
  32553          778            1                    14
```

## Analytical Functions

Analytical functions compute an aggregate value based on a group of rows, and can return multiple rows for each group. Analytical functions can be used to calculate percentages or top-N results in a group.

Analytical functions can appear only in the select list of a query or in the ORDER BY clause. They cannot appear in WHERE, ON, HAVING, or GROUP BY clauses. Analytical functions can appear in the select lists of views and derived tables.

Analytical functions are window functions, and thus require an OVER clause.

!!! note "Note"

    The ORDER BY clause within the OVER clause supports the NULLS FIRST / NULLS LAST syntax. The default is NULLS LAST.

**DENSE_RANK**

```
DENSE_RANK()
```

:   Returns the ordinal position of each result row within a partition, based on the sequence defined by the ordering definition for the window. Rows with the same values of their sort specification have the same RANK() value and result in no gaps in the list of ranks. For example: 1, 2, 2, 3, 4, 4, 4, 5.

:   The following query ranks each employee in a department based on his salary. When two employees have the same salary they are assigned the same rank. When multiple rows have the same rank, the next rank in the sequence is consecutive.

```
SELECT empno, deptno, sal,
```

```
       DENSE_RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS rank
```

```
FROM   emp;
```

```

```

```
     EMPNO     DEPTNO        SAL       RANK
```

```
----------  --------- ---------- ----------
```

```
       839        100       4900          1
```

```
       782        100       2350          2
```

```
       934        100       1200          3
```

```
       788        200       2900          1
```

```
       902        200       2900          1
```

```
       566        200       2875          2
```

```
       876        200       1000          3
```

```
       369        200        700          4
```

```
       900        300       2750          1
```

```
       654        300       1500          2
```

```
       521        300       1400          3
```

```
       844        300       1150          4
```

```
       499        300       1150          4
```

```
       698        300        850          5
```

:   The following query uses the DENSE_RANK function and then gets only the rows ranked 1 from each group. You must provide a correlation name (in this case, x) for the subquery:

```
SELECT fname, address FROM (SELECT fname, address,
```

```
       DENSE_RANK() OVER (PARTITION BY fname ORDER BY timestamp DESC) AS rank
```

```
FROM tab1) x WHERE rank = 1;
```

```

```

```
     fname                address
```

```
---------- ------------‑‑‑‑‑‑‑‑‑-
```

```
      Mary   1600 Pennsylvania Av
```

**FIRST_VALUE() OVER() and LAST_VALUE() OVER()**

```
FIRST_VALUE (scalar_value_expression) [null_spec] OVER([partition_by_clause] order_by_clause [frame_spec])
```

```
LAST_VALUE (scalar_value_expression) [null_spec] OVER([partition_by_clause] order_by_clause frame_spec)
```

:   Produces one row per input row. The same value is returned for every row in the partition, or if there is no partition_by_clause, every row in the result.

:   where:

scalar_value_expr

:   Specifies any scalar expression that can appear in the select list of a query. Can contain constants, row values, operators, scalar functions, and scalar subqueries.

null_spec

:   Indicates whether to include null values in the selection of a first_value or last_value. Valid values are:

RESPECT NULLS

:   (Default) Uses the expression value in the first or last row.

IGNORE NULLS

:   Uses the first or last non-null expression value.

OVER ([partition_by_clause] order_by_clauseframe_spec)

:   Defines the window as described in [Window Function Syntax](../SQLLanguage/SQL_Functions.md).

:   For FIRST_VALUE a frame specification is required if using IGNORE NULLS and must be ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING.

:   For LAST_VALUE a frame specification is required and must be ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING.

:   The following query ranks each employee in a department based on his salary:

```
SELECT empno, deptno, sal,
```

```
FIRST_VALUE(empno) OVER (PARTITION BY deptno ORDER BY sal DESC)
```

```
FROM emp;
```

```

```

```
EMPNO      DEPTNO     SAL        FIRST_VALUE
```

```
---------- ---------- ---------- ----------
```

```
       839        100       4900        839
```

```
       782        100       2350        839
```

```
       934        100       1200        839
```

```
       788        200       2900        788
```

```
       902        200       2900        788
```

```
       566        200       2875        788
```

```
       876        200       1000        788
```

```
       369        200        700        788
```

```
       900        300       2750        900
```

```
       654        300       1500        900
```

```
       521        300       1400        900
```

```
       844        300       1150        900
```

```
       499        300       1150        900
```

```
       698        300        850        900
```

**LAG and LEAD**

```
LAG | LEAD (scalar_expression [,offset] [,default]) [RESPECT NULLS | IGNORE NULLS]
```

:   Returns a scalar column value from a row before (LAG) or after (LEAD) the current row. Use LAG to compare values in the current row with values in a previous row. Use LEAD to compare values in the current row with values in a following row.

:   LAG and LEAD are useful for comparing values across multiple rows—for example, across time periods.

:   where:

scalar_expression

:   Is an expression that returns a single value. The expression can be a constant, row value, operator, scalar function, and scalar subquery.

offset

:   Specifies the number of rows of lag or lead from the current row. Must be an expression that resolves to a positive integer. Default is 1.

default

:   Returns the specified value if no lagging or leading row is present (for example, lag of the first value in an ordered set). Default is NULL.

RESPECT NULLS | IGNORE NULLS

:   Indicates whether to include null values in the selection of a lag or lead value. Default is RESPECT NULLS.

:   IGNORE NULLS and offset N returns the N-th previous/following not-NULL value.

:   RESPECT NULLS and offset N returns the N-th previous/following value, counting NULL values.

:   The following query shows the date, the weather, and the previous day's weather:

```
SELECT wdate, forecast, LAG(forecast) OVER(ORDER BY wdate) AS lag
```

```
FROM weather ORDER BY wdate;
```

```

```

```
wdate         forecast      lag
```

```
---------------------------------
```

```
2012-06-12    overcast      NULL
```

```
2012-06-13    sunny         overcast
```

```
2012-06-14    rain          sunny
```

:   The following query finds the salary of each employee in department 300 and lists the next higher salary:

```
SELECT deptno, empno, sal,
```

```
   LEAD(sal) OVER(ORDER BY sal) AS next_sal
```

```
FROM salary WHERE deptno=300;
```

```

```

```
deptno   empno      sal   next_sal
```

```
----------------------------------
```

```
   300     698     1150       1150
```

```
   300     844     1150       1450
```

```
   300     499     1450       1500
```

```
   300     521     1500       2750
```

```
   300     654     2750
```

```
   300     900
```

:   The following example demonstrates the use of IGNORE NULLS:

```
lead_table(c1 INT , c2 INT , c3 INT);
```

```
INSERT INTO lead_table VALUES (1,10,1), (2, 20,2), (NULL, 30,1), (NULL,40,2), (5,50,1);
```

```

```

```
   SELECT
```

```
       c1, c2, c3,
```

```
       LEAD(c1             , 1,100) OVER (ORDER BY c2) AS lead1,
```

```
       LEAD(c1 IGNORE NULLS, 1,200) OVER (ORDER BY c2) AS lead1ign,
```

```
       LAG (c1             , 2,300) OVER (ORDER BY c2) AS lag2,
```

```
       LAG (c1 IGNORE NULLS, 2,400) OVER (ORDER BY c2) AS lag2ign
```

```
   FROM lead_table;
```

```

```

```
   c1     c2    c3   lead1  lead1ign   lag2    lag2ign
```

```
------  ----    --   -----  --------   -----   --------
```

```
    1      10    1       2         2    300        400
```

```
    2      20    2    NULL         5    300        400
```

```
 NULL      30    1    NULL         5      1          1
```

```
 NULL      40    2       5         5      2          1
```

```
    5      50    1     100       200   NULL          1
```

:   Note the difference in results between the lag2 and lag2ign columns.

:   For the fourth row, for RESPECT NULLS the value two rows above is 2.

:   However, for IGNORE NULLS the second non-null value above is 1.

```
   SELECT
```

```
   c1, c2, c3,
```

```
   LEAD(c1             , 1,100) OVER (PARTITION BY c3 ORDER BY c2) AS lead1,
```

```
   LEAD(c1 IGNORE NULLS, 1,200) OVER (PARTITION BY c3 ORDER BY c2) AS lead1ign,
```

```
   LAG (c1             , 1,300) OVER (PARTITION BY c3 ORDER BY c2) AS lag1,
```

```
   LAG (c1 IGNORE NULLS, 1,400) OVER (PARTITION BY c3 ORDER BY c2) AS lag1ign
```

```
   FROM lead_table;
```

```

```

```
   c1   c2   c3   lead1   lead1ign   lag1    lag1ign
```

```
 ----   ---  ---  -----  ---------   ----    -------
```

```
    1   10    1    NULL          5    300        400
```

```
 NULL   30    1       5          5      1          1
```

```
    5   50    1     100        200   NULL          1
```

```
    2   20    2    NULL        200    300        400
```

```
 NULL   40    2     100        200      2          2
```

**NTILE**

```
NTILE(n)
```

:   Divides the rows in an ordered partition into n groups. The groups are numbered, starting at one. For each row, NTILE returns the number of the group to which the row belongs.

:   NTILE can be used, for example, to see what quartile, decile, or percentile a row is in.

:   The following query divides the employees in Department 400 into 4 groups by salary:

```
SELECT Department_ID, Employee_ID, Salary, NTILE(4)
```

```
   OVER (PARTITION BY Department_ID ORDER BY Salary DESC) AS Quartile
```

```
FROM employees WHERE Department_ID = 400;
```

```

```

```
Department_ID    Employee_ID    Salary    Quartile
```

```
------------- -------------- --------- -----------
```

```
          400             50      9000           1
```

```
          400             48      8000           1
```

```
          400             51      7500           1
```

```
          400             54      7000           1
```

```
          400             53      6500           2
```

```
          400             47      6000           2
```

```
          400             44      5000           2
```

```
          400             46      4500           2
```

```
          400             52      4300           3
```

```
          400             45      4000           3
```

```
          400             43      3500           3
```

```
          400             42      3000           4
```

```
          400             41      3000           4
```

```
          400             49      2800           4
```

:   When the number of rows is not divisible byn, the later rows will have the smaller number of rows, so the first and second quartiles have 4 rows whereas the third and fourth have only 3.

**PERCENT_RANK**

```
PERCENT_RANK()
```

:   Calculates the relative rank of a row within a group of rows. PERCENT_RANK returns a number between 0 and 1, which represents the percentage of rows in the group that are less than the current row. If a partition has exactly one row, its percent_rank() is 0. Percent_rank() for the highest value in the group will always be 1.

:   Use this function to determine the relative standing of a value within a result set.

:   The following query calculates, for each employee, the percent rank of the employee's salary in the department:

```
SELECT deptno, empno, sal,
```

```
   PERCENT_RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS pr
```

```
FROM emp
```

```
ORDER BY deptno, pr;
```

```

```

```
       DEPTNO         EMPNO          SAL         PR
```

```
------------- ------------- ------------ ----------
```

```
          100           840         4400      0.000
```

```

```

```
          300           900         2750      0.000
```

```
          300           654         1500      0.200
```

```
          300           521         1400      0.400
```

```
          300           844         1150      0.600
```

```
          300           499         1150      0.600
```

```
          300           698          850      1.000
```

```

```

```
          400           789         6500      0.000
```

```

```

```
          500           299         3900      0.000
```

```
          500           473         2200      0.333
```

```
          500           371         2200      0.333
```

```
          500           900         2100      1.000
```

```

```

```
          800             5        10500      0.000
```

```
          800           854         6200      1.000
```

**RANK**

```
RANK()
```

:   Returns the ordinal position of each result row within a partition, based on the sequence defined by the ordering definition for the window. Rows with the same values of their sort specification have the same RANK() value and result in gaps in the list of ranks. For example: 1, 2, 2, 4, 5, 5, 5, 8.

:   The following query ranks each employee in a department based on his salary. When two employees have the same salary they are assigned the same rank. When multiple rows have the same rank, the next rank in the sequence is not consecutive.

```
SELECT empno, deptno, sal,
```

```
       RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS rank
```

```
FROM   emp;
```

```

```

```
     EMPNO     DEPTNO        SAL       RANK
```

```
---------- ---------- ---------- ----------
```

```
       839        100       4900          1
```

```
       782        100       2350          2
```

```
       934        100       1200          3
```

```
       788        200       2900          1
```

```
       902        200       2900          1
```

```
       566        200       2875          3
```

```
       876        200       1000          4
```

```
       369        200        700          5
```

```
       698        300       2750          1
```

```
       499        300       1500          2
```

```
       844        300       1400          3
```

```
       521        300       1150          4
```

```
       654        300       1150          4
```

```
       900        300        850          6
```

**ROW_NUMBER**

```
ROW_NUMBER()
```

:   Returns the ordinal position of each result row within a partition, based on the sequence defined by the ordering definition for the window. Rows with the same values in their sort specification are ordered arbitrarily. For example: 1, 2, 3, 4, 5.

:   The following query assigns a consecutive number to each row. Rows with matching numbers are ordered arbitrarily.

```
SELECT empno, deptno, sal,
```

```
       ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY sal) AS rownum
```

```
FROM   emp;
```

```

```

```
     EMPNO     DEPTNO        SAL     ROWNUM
```

```
---------- ---------- ---------- ----------
```

```
       934        100       1200          1
```

```
       782        100       2350          2
```

```
       839        100       4900          3
```

```
       369        200        700          1
```

```
       876        200       1000          2
```

```
       566        200       2875          3
```

```
       788        200       2900          4
```

```
       902        200       2900          5
```

```
       900        300        850          1
```

```
       654        300       1150          2
```

```
       521        300       1150          3
```

```
       844        300       1400          4
```

```
       499        300       1500          5
```

```
       698        300       2750          6
```

## Numeric Functions

For trigonometric functions (COS, SIN, TAN), specify argument in radians. To convert degrees to radians, use the formula: radians = degrees / 360 * 2 * pi(). The functions ACOS, ASIN, ATAN, AND ATAN2 return a value in radians.

**ABS**

```
ABS(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: Same as n

:   Absolute value of n

**ACOS**

```
ACOS(n)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Arccosine of cosine value n

**ASIN**

```
ASIN(n)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Arcsine value of sine value n

**ATAN**

```
ATAN(n)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Arctangent of n; returns a value from (-pi/2) to pi/2.

**ATAN2**

```
ATAN2 (x, y)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Arctangent of angle defined by coordinate pair (x, y)

**CEIL**

```
CEIL(n) CEILING(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: Numeric type, based on operand.

:   Returns the smallest whole value greater than or equal to the specified numeric expression.

:   Returns a decimal if input is decimal, and a float if input is float. Coerces other types to decimal or float, according to normal coercion preferences for the input type, and then returns result based on the coerced input.

**COS**

```
COS(n)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Cosine of n; returns a value from -1 to 1.

**EXP**

```
EXP(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: FLOAT

:   Exponential of n

**FLOOR**

```
FLOOR(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: Numeric type, based on operand.

:   Returns the largest whole value less than, or equal to, the specified numeric expression.

:   Returns a decimal if input is decimal, and a float if input is float or money. Coerces other types to decimal or float, according to normal coercion preferences for the input type, and then returns result based on the coerced input.

**LOG**

```
LOG(n)LN(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: FLOAT

:   Natural logarithm of n

**MOD**

```
MOD(n,b)
```

:   Operand type: INTEGER, SMALLINT, INTEGER1, DECIMAL

:   Result type: Same as b

:   n modulo b. The result is the same data type as b. Decimal values are truncated.

**PI**

```
PI()
```

:   Operand type: None

:   Result type: FLOAT

:   Value of pi (ratio of the circumference of a circle to its diameter)

**POWER**

```
POWER(x,y)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   x to the power of y (identical to x ** y)

**ROUND**

```
ROUND(n,i)
```

:   Operand type: All numeric types

:   Result type: Type of n.

:   Rounds value n at the i'th place right or left of the decimal, depending on whether i is greater or less than 0.

:   **Warning!** When used with a floating point argument, rounding errors may occur.

**SIGN**

```
SIGN(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: INTEGER

:   Returns -1 if n < 0, 0 if n = 0, +1 if n > 0

**SIN**

```
SIN(n)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Sine of n; returns a value from -1 to 1.

**SQRT**

```
SQRT(n)
```

:   Operand type: All numeric types and MONEY

:   Result type: FLOAT

:   Square root of n

**TAN**

```
TAN(n)
```

:   Operand type: All numeric types

:   Result type: FLOAT

:   Tangent value of angle n

**TRUNC**

```
TRUNC(x ,y)TRUNCATE(x ,y)
```

:   Operand type: All numeric types

:   Result type: DECIMAL

:   Truncates x at the decimal point, or at y places to the right or left of the decimal, depending on whether y is greater or less than 0.

## String Functions

String functions perform a variety of operations on character data.

String functions can be nested. For example:

```
LEFT(RIGHT(x.name, SIZE(x.name) - 1), 3)
```

returns the substring of x.name from character positions 2 through 4.

The **||** or **+** operator can also be used to concatenate strings:

```
x.lastname ||  ', ' ||  x.firstname
```

!!! note "Note"

    Using **+** should be avoided. It is an overloaded operator and can result in ambiguity when string columns and literals that contain only numeric values are mixed with numeric columns or literals.

SELECT '1' + '40' + '50' returns 14050

SELECT 1 + '40' + '50' returns 91

SELECT '1' + 40 + '50' returns 91

SELECT '1' + 40 || '50' returns 4150

**ASCII**

```
ASCII(v1)
```

:   Result type: Any character type

:   Returns the character equivalent of the valuev1, which is an expression of any type.

**CHARACTER_LENGTH**

```
CHARACTER_LENGTH(c1)
```

:   Result type: INTEGER

:   Returns the number of characters in c1 without trimming blanks, as is done by the LENGTH() function.

!!! note "Note"

    This function does not support NCHAR and NVARCHAR arguments.

**CHAREXTRACT**

```
CHAREXTRACT(c1,n)
```

:   Result type: VARCHAR or NCHAR

:   Returns the nth character or code point ofc1. Ifn is larger than the length of the string, the result is a blank character.

!!! note "Note"

    For Unicode (USC2) strings the value returned is the single USC2 character. For non-Unicode strings the values returned may be 1,2,3 or 4 bytes long depending on the character at offset n characters of c1.

:   SELECT CHAREXTRACT('company',4) returns 'p'

**CHR**

```
CHR(n)
```

:   Result type: CHAR

:   Converts integer into corresponding ASCII code. If n is greater than 255, the conversion is performed on n mod 256.

:   SELECT CHR(65) returns 'A'.

:   SELECT CHR(345) returns 'Y'.

**CONCAT**

```
CONCAT(c1,c2...)
```

:   Result type: Any character or Unicode type, BYTE

:   Concatenates two or more strings.

:   SELECT CONCAT('1', '2', '3', '4') returns '1234'.

:   In earlier releases, to achieve the same result, you must nest the CONCAT function: SELECT CONCAT(CONCAT(CONCAT('1', '2'), '3'), '4').

:   The result size is the sum of the sizes of the arguments. If the result is a c or char string, it is padded with blanks to achieve the proper length. To determine the data type results of concatenating strings, see the table regarding results of string concatenation.

!!! note "Note"

    The concatenation of the BYTE data type cannot be used to create a table column implicitly in Actian Data Platform tables; the result of such concatenation, however, can be inserted into a column with a character data type.

:   Wrong:

```
 CONCAT2 AS SELECT CONCAT(BYTE('1'), 0x42, X'43', CAST('4' AS BYTE));
```

:   Correct:

```
test_concat (col1 VARCHAR(4);
```

```
INSERT INTO test_concat SELECT CONCAT(BYTE('1'), 0x42, X'43', CAST('4' AS BYTE));
```

**INITCAP**

```
INITCAP(c1)
```

:   Result type: Any character or Unicode type

:   Converts all initial characters in c1 to upper case.

```
SELECT INITCAP('This is the final version (VERSION:5.a;6) of Leonard''s will')
```

:   returns:'This Is The Final Version (Version:5.A;6) Of Leonard's Will'

**JARO_WINKLER**

```
JARO_WINKLER(c1,c2)
```

:   Result type: FLOAT4

:   Calculates the Jaro-Winkler similarity between two VARCHAR strings. This is returned as a float value between 0 and 1, where 0.0 means no similarities and 1.0 means the strings are identical.

:   SELECT JARO_WINKLER('same','same') returns 1.0

**LEFT**

```
LEFT(c1,len)
```

:   Result type: Any byte, character, or Unicode type

:   Returns the leftmost len characters ofc1. If the result is a fixed-length c or char string, it is the same length asc1, padded with blanks. The result format is the same as c1. lenwill be converted to a positive integer.

:   If len is not an integer value it will be rounded down equivalent to floor(len). If len is negative the result will be an empty string.

:   SELECT LEFT ('Company',4) returns 'Comp'

**LENGTH**

```
LENGTH(c1)
```

:   Result type: SMALLINT

:   If c1 is a fixed-length char string, returns the length of c1 without trailing blanks. If c1 is a variable-length string, returns the number of characters actually in c1.

:   SELECT LENGTH ('Company') returns 7

**LEVENSHTEIN**

```
LEVENSHTEIN(c1,c1)
```

:   Result type: INTEGER4

:   Calculates the Levenshtein distance between two VARCHAR strings. The Levenshtein distance between two strings is the minimum number of changes that need to be made to convert the source string into the target string.

:   Alias: LEVENSHTEIN_DISTANCE

:   SELECT LEVENSHTEIN('foo','fou') returns 1

**LOCATE**

```
LOCATE(c1,c2)
```

:   Result type: SMALLINT

:   Returns the location of the first occurrence of c2 within c1, including trailing blanks from c2. The location is in the range 1 to size(c1). If c2 is not found, the function returns size(c1) + 1. The function size() is described below, in this table.

:   If c1 and c2 are different string data types, c2 is coerced into the c1 data type.

:   SELECT LOCATE ('Company', 'p') returns 4

**LOWERCASE or LOWER**

```
LOWERCASE(c1)
```

:   or

```
LOWER(c1)
```

:   Result type: Any character or Unicode type

:   Converts all upper case characters inc1 to lower case.

:   SELECT LOWER ('Company') returns 'company'

**LPAD**

```
LPAD(expr1, n [, expr2])
```

:   Result type: Any character type

:   Returns character expression of length n in which expr1 is prepended by n-m blanks (where m is length(expr1)) or, if expr2 is coded, enough copies of expr2 to fill n-m positions at the start of the result string.

:   SELECT LPAD ('Company',20, '-') returns '-------------Company'

**LTRIM**

```
LTRIM(expr)
```

:   Result type: Any character type

:   Returns character expression with leading blanks removed.

:   SELECT LTRIM (' Company') returns 'Company'

**NOTRIM**

```
NOTRIM(c1)
```

:   Result type: Any character string variable

:   Retains trailing blanks when placing a value in a varchar column. This function can be used only in an embedded SQL program.

**OCTET_LENGTH**

```
OCTET_LENGTH(c1)
```

:   Result type: INTEGER

:   Returns the number of 8-bit octets (bytes) in c1 without trimming blanks, as is done by the LENGTH() function.

:   octet(col1 VARCHAR(10), col2 CHAR(10));

:   INSERT INTO octet VALUES ('Company', 'Company')

:   SELECT OCTET_LENGTH (col1) returns 7

:   SELECT LENGTH (col1) returns 7

:   SELECT OCTET_LENGTH (col2) returns 10

:   SELECT LENGTH (col2) returns 7

**POSITION**

```
POSITION(c1 IN c2)POSITION(c1 , c2)
```

:   Result type: SMALLINT

:   ANSI compliant version of LOCATE function. If a match exists, POSITION(c1 IN c2) is equal to LOCATE(c2, c1). If a match does not exist, POSITION returns 0, unlike LOCATE.

:   SELECT POSITION('p', 'Company') returns 4.

:   SELECT POSITION('z', 'Company') returns 0.

:   SELECT LOCATE('Company', 'p') returns 4 (same result as POSITION).

:   SELECT LOCATE('Company', 'z') returns 8 (one more than LENGTH(‘company’).

**REPEAT**

```
REPEAT(c1, n)
```

:   Result type: Any character type

:   Returns c1 (a character string) repeated n times.

:   SELECT REPEAT ('-',10) returns '----------'

:   SELECT REPEAT ('str',3) returns 'strstrstr'

**REPLACE**

```
REPLACE(expr1, expr2, expr3)
```

:   Result type: Any character type

:   Returns character expression derived from expr1 in which all instances of expr2 have been replaced by expr3.

:   SELECT REPLACE('The priory was in the next town','priory','church')

:   returns: 'The church was in the next town'

**REVERSE**

```
REVERSE(c1)
```

:   Result type: CHAR, VARCHAR, NCHAR, NVARCHAR

:   Returns the string c1with the in-memory order of the characters reversed, based on code points. For CHAR and NCHAR, the trailing space is also reversed.

:   Reversal of code points is supported for all string types in both UTF8 and non-UTF8 installations.

    In the following examples, each underline character (_) represents a space.

| Data Type | Input | Output |
| --- | --- | --- |
| CHAR(8) | `hello` | `___olleh` |
| NCHAR(8) | `hello` | `___olleh` |
| VARCHAR(8) | `hello` | `olleh___` |
| NVARCHAR(8) | `hello` | `olleh___` |

    SELECT REVERSE('ecnalubma') returns ambulance.

    Example for Unicode input:

    SELECT REVERSE('Adán') returns nádA. The string 'Adán' is 4 code points:

        - U+0041 Latin Capital Letter A

        - U+0064 Latin Small Letter D

        - U+00E1 Latin Small Letter A with Acute

        - U+006E Latin Small Letter N

```
REVERSE(c1, 'egc')
```

:   Result type: CHAR, VARCHAR, NCHAR, NVARCHAR

:   Returns the string c1with the in-memory order of the characters reversed, based on characters consisting of multiple code points (extended grapheme cluster). For CHAR and NCHAR, the trailing space is also reversed.

:   Reversal of extended grapheme clusters is supported for types CHAR and VARCHAR in case the data is interpreted as UTF8 (due to the installed character set or collation). For types NCHAR and NVARCHAR the reversal of extended grapheme clusters is supported independently of the installed character set.

:   For more information on extended grapheme clusters, see the Unicode Standard Annex #29 “Unicode Text Segmentation” at [https://www.unicode.org/reports/tr29](https://www.unicode.org/reports/tr29).

:   Example for Unicode input:

:   SELECT REVERSE('Adán', 'egc') returns nádA. The string 'Adán' is 5 code points:

        - U+0041 Latin Capital Letter A

        - U+0064 Latin Small Letter D

        - U+0061 Latin Small Letter A

        - U+0301 Combining Acute Accent

        - U+006E Latin Small Letter N

    The a gets acute because U+0061 and U+0301 build a grapheme cluster.

    To determine the number of code points in a string, use the LENGTH() function.

**RIGHT**

```
RIGHT(c1,len)
```

:   Result type: Any character or Unicode type

:   Returns the rightmost len characters ofc1. Trailing blanks are not removed first. If c1 is a fixed-length character string, the result is padded to the same length as c1. If c1 is a variable-length character string, no padding occurs. The result format is the same as c1. lenmust be a positive integer.

:   SELECT RIGHT('The priory was in the next town',9)

:   returns 'next town'

**RPAD**

```
RPAD(expr1, n [, expr2])
```

:   Result type: Any character type

:   Returns character expression of length n in which expr1 is appended by n-m blanks (where m is length(expr1)) or, if expr2 is coded, enough copies of expr2 to fill n-m positions at the end of the result string.

:   SELECT RPAD('Company',12, '-') returns 'Company-----'

:   SELECT RPAD('Company',12, '-x') returns 'Company-x-x-'

**RTRIM**

```
RTRIM(expr)
```

:   Result type: Any character type

:   Returns character expression with trailing blanks removed.

:   SELECT LENGTH(RTRIM('Company ')) returns 7

**SHIFT**

```
SHIFT(c1,nshift)
```

:   Result type: Any character or Unicode type

:   Shifts the string nshift places to the right if nshift > 0 and to the left ifnshift < 0. Ifc1 is a fixed-length character string, the result is padded with blanks to the length of c1. If c1 is a variable-length character string, no padding occurs. The result format is the same as c1.

:   SELECT SHIFT('Company',4) returns ' Com'

:   SELECT SHIFT('Company',‑4) returns 'any '

**SIZE**

```
SIZE(c1)
```

:   Result type: SMALLINT

:   Returns the declared size of c1 without removal of trailing blanks.

:   SELECT SIZE('Company') returns 7

**SOUNDEX**

```
SOUNDEX(c1)
```

:   Result type: Any character type

:   Returns a c1 four-character field that can be used to find similar sounding strings. For example, SMITH and SMYTHE produce the same SOUNDEX code. If there are less than three characters, the result is padded by trailing zero(s). If there are more than three characters, the result is achieved by dropping the rightmost digits.

:   This standard (Russell) soundex function is useful for finding like-sounding strings quickly. A list of similar sounding strings can be shown in a search list rather than only the next strings in the index.

:   SELECT SOUNDEX('Company') returns 'C515'

:   SELECT SOUNDEX ('Company2012') returns 'C515'

**SQUEEZE**

```
SQUEEZE(c1)
```

:   Result type: VARCHAR

:   Compresses white space. White space is defined as any sequence of blanks, null characters, newlines (line feeds), carriage returns, horizontal tabs and form feeds (vertical tabs). Trims white space from the beginning and end of the string, and replaces all other white space with single blanks.

:   This function is useful for comparisons. The value for c1 must be a string of variable‑length character string data type (not fixed-length character data type). The result is the same length as the argument.

:   SELECT SQUEEZE (' Company 2012 ') returns 'Company 2012'

**SUBSTR**

```
SUBSTR(c1, loc [, len])
```

:   Result type: VARCHAR, NVARCHAR

:   Returns part of c1 starting at the locposition and either extending to the end of the string or for the number of characters/code points in the lenoperand.

:   If lenis specified and is less than 1, SUBSTR returns NULL.

:   The locparameter determines the start of the substring to be extracted. If locis less than 0 the position is counted backwards from the end of c1; if locis greater than 0 the position is counted from the beginning. If locis 0 the start position is the first character.

:   After the start of the substring is determined, lencharacters are extracted. If lenis not supplied, the rest of c1 is implied.

:   SELECT SUBSTR('Company 2012',9,2) returns '20'

:   SELECT SUBSTR('Company 2012',9) returns '2012'

:   SELECT SUBSTR('Company 2012',-9,4) returns 'pany'

**SUBSTRING**

```
SUBSTRING(c1 FROM loc [FOR len])SUBSTRING(c1, loc[, len])
```

:   Result type: VARCHAR, NVARCHAR

:   Returns part of c1 starting at the loc position and either extending to the end of the string or for the number of characters/code points in the len operand. The result format is a varchar or nvarchar the size of c1. Unlike SUBSTR, locand lenmust be positive values.

:   SELECT SUBSTRING('Company 2012',9,2) returns '20'

:   SELECT SUBSTRING('Company 2012',9) returns '2012'

:   SELECT SUBSTRING('Company 2012',-9,4) returns an empty string.

**SUBSTRING_INDEX**

```
SUBSTRING_INDEX(str,delim,count)
```

:   Result type: VARCHAR

:   Returns the substring from string strbefore countoccurrences of the delimiter delim. If countis positive, everything to the left of the final delimiter (counting from the left) is returned. If countis negative, everything to the right of the final delimiter (counting from the right) is returned. This function performs a case-sensitive match when searching for delim.

```
test(str VARCHAR(20), cnt INT);
```

```
INSERT INTO test VALUES('www.actian.com', 2);
```

```
INSERT INTO test VALUES('www.actian.com', -2);
```

```
SELECT SUBSTRING_INDEX(str, '.', 2) FROM test;
```

```
+--------------------+
```

```
|col1                |
```

```
+--------------------+
```

```
|www.actian          |
```

```
|www.actian          |
```

```
+--------------------+
```

```
SELECT SUBSTRING_INDEX(str, '.', cnt) FROM test;
```

```
+--------------------+
```

```
|col1                |
```

```
+--------------------+
```

```
|www.actian          |
```

```
|actian.com          |
```

```
+--------------------+
```

!!! note "Note"

    This function works only for data stored in tables created with the VECTORWISE or VECTORWISE_ROW storage structure.

**TRIM**

```
TRIM(c1)
```

:   Result type: VARCHAR

:   Returns c1 without trailing blanks. The result has the same length as c1.

    **ANSI Compliant Version of TRIM:**

```
TRIM([ [BOTH | LEADING | TRAILING] [c1] FROM] c2 )
```

:   Result type:****Any character string variable

:   Returns c2 with all occurrences of c1—which can be only one character—removed from the beginning, end, or both, as specified. BOTH is the default. In the absence of c1, the space is assumed.

:   SELECT 'DEFAULT' , '['||TRIM(' Company ' ) ||']'

:   returns [ Company]

:   SELECT 'BOTH' , '['||TRIM(BOTH ' ' FROM ' Company ' ) ||']'

:   returns [Company]

:   SELECT 'LEADING' , '['||TRIM(LEADING ' ' FROM ' Company ' ) ||']'

:   returns [Company ]

:   SELECT 'TRAILING' , '['||TRIM(TRAILING ' ' FROM ' Company ' ) ||']'

:   returns [ Company]

**UPPERCASE or UPPER**

```
UPPERCASE(c1)
```

:   or

```
UPPER(c1)
```

:   Result type: Any character type

:   Converts all lower case characters in c1to upper case.

### String Functions and the UTF8 Character Set

For the UTF8 character set, the character data is multi-byte string and the actual number of bytes for the data could be more than the number of characters. If the output buffer for any string operation is not sufficiently large to hold the multi-byte string, the result will be truncated at a character boundary.

## Date and Time Functions

Date and time functions operate on a date and time input value and return a string, numeric, or date and time value.

**ADD_MONTHS**

```
ADD_MONTHS(datetime, n)
```

:   Operand type: datetimecan be an ANSIDATE, TIMESTAMP, CHAR, VARCHAR, NCHAR, or NVARCHAR; n is an integer.

:   Result type: Same as the first parameter

:   Adds the number, which represents months, to the date. If the number is negative then the date is reduced by the number of months.

:   Example:

```
SELECT ADD_MONTHS('2012-11-07',2)\g 2013-01-07
```

**DATE_FORMAT**

```
DATE_FORMATDATE_FORMAT(datetime, format)TIME_FORMATTIME_FORMAT(datetime, format)
```

:   TIME_FORMAT is an alias for DATE_FORMAT.

:   Operand type: datetime is a DATE, TIME, or TIMESTAMP; formatis a character string

:   Result type: VARCHAR

:   Returns datetime formatted according to the formatstring.

:   The specifiers in the following table can be used in the format string. The “%” character is required before format specifier characters. If the format specifier is inappropriate to the data type of datetime, then NULL is returned.

| Specifier | Description |
| --- | --- |
| %a | Abbreviated weekday name (Sun..Sat) |
| %b | Abbreviated month name (Jan..Dec) |
| %c | Month, numeric (0..12) |
| %D | Day of the month with English suffix (1st, 2nd, 3rd, …) |
| %d | Day of the month, numeric (01‑31) |
| %e | Day of the month, numeric (1‑31) |
| %f | Microseconds (000000..999999) |
| %H | Hour (00..23) |
| %h | Hour (01..12) |
| %I | Hour (01..12) |
| %i | Minutes, numeric (00..59) |
| %j | Day of year (001..366) |
| %k | Hour (0..23) |
| %l | Hour (1..12) |
| %M | Month name (January..December) |
| %m | Month, numeric (00..12) |
| %p | AM or PM |
| %r | Time, 12-hour (hh:mm:ss followed by AM or PM) |
| %S | Seconds (00..59) |
| %s | Seconds (00..59) |
| %T | Time, 24-hour (hh:mm:ss) |
| %U | Week (00..53), where Sunday is the first day of the week |
| %u | Week (00..53), where Monday is the first day of the week |
| %V | Week (01..53), where Sunday is the first day of the week; used with %X |
| %v | Week (01..53), where Monday is the first day of the week; used with %x |
| %W | Weekday name (Sunday..Saturday) |
| %w | Day of the week (0=Sunday..6=Saturday) |
| %X | Year for the week where Sunday is the first day of the week, numeric, four digits; used with %V |
| %x | Year for the week, where Monday is the first day of the week, numeric, four digits; used with %v |
| %Y | Year, numeric (four digits) |
| %y | Year, numeric (two digits) |
| %% | A literal “%” character |
| %x | x, for any "x" not listed above |

```
DATE_FORMAT('2010-10-03 22:23:00', '%W %M %Y')
```

:   returns 'Sunday October 2010'

```
DATE_FORMAT('2007-10-03 22:23:00', '%H:%i:%s')
```

:   returns '22:23:00'

```
DATE_FORMAT('1900-10-04 22:23:00', '%D %y %a %d %m %b %j')
```

:   returns '4th 00 Thu 04 10 Oct 277'

```
DATE_FORMAT('1997-10-04 22:23:00', '%H %k %I %r %T %S %w')
```

:   returns '22 22 10 10:23:00 PM 22:23:00 00 6'

```
DATE_FORMAT('1999-01-01', '%X %V')
```

:   returns '1998 52'

**DATE_PART**

```
DATE_PART(unit,date)
```

:   Result type: INTEGER

:   Returns an integer containing the specifiedunit component of the input date.

:   The following table lists valid unitparameters. A unit parameter must be specified using a quoted string (for example: 'YEAR'). The parameter is case sensitive.

| Date Portion | How Unit Parameter Is Specified |
| --- | --- |
| Year | YEAR |
| Quarter | QUARTER |
| Month | MONTH |
| Week | WEEK |
| ISO-Week | ISO-WEEK |
| Day of month | DAY |
| Day of week | DAYOFWEEK, DOW* |
| Day of year | DAYOFYEAR, DOY* |
| Hour | HOUR |
| Minute | MINUTE |
| Second | SECOND |
| Milliseconds | MILLISECOND |
| Microseconds | MICROSECOND |
| Nanoseconds | NANOSECOND |
| UNIX timestamp | EPOCH* |
| *EPOCH works only for the CURRENT_TIMESTAMP and CURRENT_DATE selected from a Actian Data Platform table. |

:   Many of these units can also be derived using the EXTRACT function or using explicit, individual extract functions such as HOUR() or MILLISECOND().

:   The DATE_PART function is useful in set functions and in ensuring correct ordering in complex date manipulation. For example, if date_field contains the value 23-oct-2012, then:

```
DATE_PART('MONTH',DATE(date_field))
```

:   returns a value of 10 (representing October), and

```
DATE_PART('DAY',DATE(date_field))
```

:   returns a value of 23.

:   Months are numbered 1 to 12, starting with January. Hours are returned according to the 24-hour clock. Quarters are numbered 1 through 4.

:   Week 1 begins on the first Monday of the year. Dates before the first Monday of the year are considered to be in week 0. However, if you specify ISO-Week, which is ISO 8601 compliant, the week begins on Monday, but the first week is the week that has the first Thursday. The weeks are numbered 1 through 53.

:   Therefore, if you are using Week and the date falls before the first Monday in the current year, date_part returns 0. If you are using ISO-Week and the date falls before the week containing the first Thursday of the year, that date is considered part of the last week of the previous year, and DATE_PART returns either 52 or 53.

:   The following table illustrates the difference between Week and ISO-Week:

| Date Column | Day of Week | Week | ISO-Week |
| --- | --- | --- | --- |
| 02-jan-2009 | Fri | 0 | 1 |
| 04-jan-2009 | Sun | 0 | 1 |
| 02-jan-2010 | Sat | 0 | 53 |
| 04-jan-2010 | Mon | 1 | 1 |
| 02-jan-2011 | Sun | 0 | 52 |
| 04-jan-2011 | Tue | 1 | 1 |
| 02-jan-2012 | Mon | 1 | 1 |
| 04-jan-2012 | Wed | 1 | 1 |

**DATE_TRUNC**

```
DATE_TRUNC(unit,date)
```

:   Operand type: datecan be absolute ANSIDATE, TIME, TIMESTAMP

:   Result type: Same as operand type

:   Returns a date value truncated to the specified unit.

:   The following table lists valid unitparameters. A unit parameter must be specified using a quoted string (for example: 'YEAR'). The parameter and is case sensitive.

| Date Portion | How Unit Parameter Is Specified |
| --- | --- |
| Year | YEAR |
| Quarter | QUARTER |
| Month | MONTH |
| Week | WEEK |
| Day | DAY |
| Hour | HOUR |
| Minute | MINUTE |
| Second | SECOND |
| Milliseconds | MILLISECOND |
| Microseconds | MICROSECOND |
| Nanoseconds | NANOSECOND |

:   Where unit is DAY or greater, the day boundary is taken to be in the user's time zone. For example, the following query against a timestamp with time zone value:

```
SELECT DATE_TRUNC('DAY',TIMESTAMP '2011-02-03 16:12:13.000000000-08:00')
```

:   returns

```
2011-02-03 00:00:00.000000000-08:00
```

:   which retains the original time zone offset.

:   Use the DATE_TRUNC function to group all the dates within the same month or year, and so forth. For example:

```
DATE_TRUNC('MONTH',TIMESTAMP('1998-10-23 12:33:00'))
```

:   returns 1998-10-01, and

```
DATE_TRUNC('YEAR',DATE'1998-10-23')
```

:   returns 1998-01-01.

:   Truncation takes place in terms of calendar years and quarters (January 1, April 1, June 1, October 1).

:   To truncate in terms of a fiscal year, offset the calendar date by the number of months between the beginning of your fiscal year and the beginning of the next calendar year (6 mos for a fiscal year beginning July 1, or 4 mos for a fiscal year beginning September 1):

```
DATE_TRUNC('YEAR',date + INTERVAL '4' MONTH) - INTERVAL '4' MONTH
```

:   Weeks start on Monday. The beginning of a week for an early January date falls into the previous year.

**DAY**

```
DAY('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the day portion of a date or timestamp.

:   `DAY(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 15

**DAYOFMONTH**

```
DAYOFMONTHDAYOFMONTH(datetime)
```

:   Operand type: DATE, TIME, or TIMESTAMP

:   Result type: INTEGER.

:   Returns the day of the month from the specified datetimevalue.

:   `DAYOFMONTH(DATE '2011-02-15')` returns 15

**DAYOFWEEK**

```
DAYOFWEEKDAYOFWEEK(datetime [,n])
```

:   Operand type: datetime is a DATE, TIME, or TIMESTAMP; n is an integer.

:   Result type: INTEGER

:   Returns the day of the week from the specified datetime value, where 1 = Sunday unless n is used to shift the start of week.

:   `DAYOFWEEK(DATE '2011-02-15',4)` returns 6

:   `DAYOFWEEK(DATE '2011-02-15')` returns 3

**DAYOFYEAR**

```
DAYOFYEARDAYOFYEAR(datetime)
```

:   Returns the ordinal number of day in the year, in the range 1 to 366, for datetime.

:   Operand type: DATE, TIME, or TIMESTAMP

:   Result type: INTEGER

:   `DAYOFYEAR(DATE '2011-02-04')` returns 35

**DOY**

:   Same as DAYOFYEAR.

**EXTRACT**

```
EXTRACT (part FROM datetime)
```

:   Operand type: datetimecan be a DATE, TIME, TIMESTAMP, or INTERVAL value expression.

:   Result type: INTEGER

:   Extracts a particular field from a date/time value. Partspecifies the field to extract.

:   A part parameter must be specified using a quoted string (for example: 'YEAR'). The parameter and is case sensitive.

:   Valid values for partare:

YEAR

:   Year field. Range: 0 - 9999

MONTH

:   Month field. Range: 1 - 12

DAY

:   Day field. Range: 1 - 31

HOUR

:   Hour field. Range: 0 - 23

MINUTE

:   Minute field. Range: 0 - 59

SECOND

:   Second field. Range: 0 - 59

MILLISECONDS

:   Fractional seconds as milliseconds. Range: 0 - 999.

MICROSECONDS

:   Fractional seconds as microseconds. Range: 0 - 999.

NANOSECONDS

:   Fractional seconds as nanoseconds. Range: 0 - 999.

TIMEZONE_HOUR

:   Time zone hour offset. Range: -12 - 14.

TIMEZONE_MINUTE

:   Time zone minute offset. Range: 0 - 59

DAYOFWEEK

:   Day of week with Sunday=1. Range: 1 - 7.

DAYOFYEAR

:   Day of year. Range: 1 - 366.

ISO_WEEK

:   Week of year ISO 6801.

QUARTER

:   Year quarter. Range: 1 - 4.

WEEK

:   Week of year. Range: 1 - 53.

WEEK_ISO

:   Week of year ISO 6801.

!!! note "Note"

    The datetimevalue cannot be an interval type on the TIMEZONE_HOUR, TIMEZONE_MINUTE, DAYOFWEEK, DAYOFYEAR, WEEK, ISO_WEEK, QUARTER, and EPOCH functions.

:   Examples:

```
SELECT EXTRACT (YEAR FROM datecol) FROM datetable;
```

```
SELECT EXTRACT (MONTH FROM CURRENT_DATE);
```

```
SELECT EXTRACT (HOUR FROM timecol) FROM datetable;
```

```
SELECT * FROM tx WHERE EXTRACT(HOUR FROM datetable) = 17;
```

**FROM_UNIXTIME**

:   Operand types: INTEGER, character string

:   Formats UNIX timestamp as a date.

```
FROM_UNIXTIME
```

```
FROM_UNIXTIME(i)
```

:   Result type: TIMESTAMP WITHOUT TIME ZONE

:   Returns TIMESTAMP WITHOUT TIME ZONE created from the specified integer, which must be a UNIX time (number of seconds since 1-Jan-1970).

```
FROM_UNIXTIME(i, format)
```

:   Result type: VARCHAR

:   Returns iformatted in UNIX time, according to the specified format.For valid formats, see [DATE_FORMAT](../SQLLanguage/SQL_Functions.md).

```
FROM_UNIXTIME(1196440219)
```

:   returns 2007-11-30 10:30:19.000000

```
FROM_UNIXTIME(1196440219, '%Y %D %M %h:%i:%s %x')
```

:   returns 2007 30th November 10:30:19 2007

!!! note "Note"

    Results from this function are from a GMT offset, which may result in a value that is from '1969-12-31 12:00:00.000000' depending on the actual time zone of the server.

**HOUR**

```
HOUR('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the hour portion of a time or timestamp.

:   `HOUR(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 12

**INTERVAL_DIFF**

```
INTERVAL_DIFF('datetime1', 'datetime2')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTERVAL YEAR TO MONTH

:   Returns the difference between datetime1 and datetime2 expressed as an INTERVAL YEAR TO MONTH.

:   This complements subtraction of TIMESTAMPs that yields an INTERVAL DAY TO SECOND and subtraction of ANSIDATEs that yields an integer.

:   `INTERVAL_DIFF('2010-1-1', '2015-3-1')` returns 5-2

**LAST_DAY**

```
LAST_DAY(datetime)
```

:   Operand type: DATE, TIMESTAMP

:   Result type: DATE or TIMESTAMP depending on input

:   Returns the last day of the month in which the specified date or timestamp falls. Returns NULL if the argument is invalid.

```
LAST_DAY(DATE '2003-02-05')
```

:   returns 2003-02-28

```
LAST_DAY(DATE '2004-02-05')
```

:   returns 2004-02-29

```
LAST_DAY(TIMESTAMP '2004-01-01 01:01:01')
```

:   returns 2004-01-31

```
LAST_DAY(DATE '2003-03-32')
```

:   returns NULL

**MICROSECOND**

```
MICROSECOND('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER4

:   Extracts the fractions of seconds portion of a time or timestamp as microseconds.

:   `MICROSECOND(TIMESTAMP '2006-12-15 12:30:55.1234')`returns 123400

**MILLISECOND**

```
MILLISECOND('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER4

:   Extracts the fractions of seconds portion of a time or timestamp as milliseconds.

:   `MILLISECOND(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 123

**MINUTE**

```
MINUTE('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the minute portion of a time or timestamp.

:   `MINUTE(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 30

**MONTH**

```
MONTH('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the month portion of a date or timestamp.

:   `MONTH(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 12

**MONTHS_BETWEEN**

```
MONTHS_BETWEENMONTH_BETWEEN(date1, date2)
```

:   Operand type: DATE, TIMESTAMP

:   Result type: FLOAT8

:   Returns the number of months between date1and date2, positive if date2precedes date1and negative if date1precedes date2. If the day of date1is the same as the day in date2or both dates are the last days of months, then the result is a whole number of months; otherwise, any time portion is also taken into consideration in the difference, where days are treated as 1/31 of a month.

```
SELECT MONTHS_BETWEEN(DATE'2010-06-15', DATE'2011-06-15');
```

```
-12.000
```

```
SELECT MONTHS_BETWEEN(DATE'2011-06-15', DATE'2011-05-15');
```

```
1.000
```

```
SELECT MONTHS_BETWEEN(DATE'2011-06-30', DATE'2011-05-31');
```

```
1.000
```

```
SELECT MONTHS_BETWEEN(DATE'2011-06-15', DATE'2011-06-01');
```

```
0.452
```

**NANOSECOND**

```
NANOSECOND('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER4

:   Extracts the fractions of seconds portion of a time or timestamp as nanoseconds.

:   `NANOSECOND(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 123400000

**QUARTER**

```
QUARTER('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the quarter of the calendar year that corresponds to the date or timestamp. Quarters are numbered 1 through 4.

:   `QUARTER(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 4

**ROUND(datetime)**

```
ROUND(datetime [,str-interval])
```

:   Operand type: datetimeis a DATE, TIME, or TIMESTAMP; str-interval is a character string

:   Result type: DATE, TIME, or TIMESTAMP

:   Returns datetime rounded up to the unit specified by str-interval. If str-interval is omitted, then datetime is rounded to the nearest day.

:   The str-interval can be any of the following:

| Formats | Description |
| --- | --- |
| CC  CENTURY  CENTURIES | Century |
| D  DY  DAY | Starting day of week |
| DD  DDD  DAYS  J | Day |
| HH  HH12  HR  HRS  HOUR  HOURS | Hour |
| I  IY  IYY  IYYYY  ISO-YR  ISO-YRS  ISO-YEAR  ISO-YEARS | ISO year boundary |
| IW  ISO-WK  ISO-WEEK | Same day of week as 1st of ISO year |
| MI  MIN  MINS  MINUTE  MINUTES | Minute |
| MM  MO  MON  MONTH  MONTHS  RM  MOS | Month |
| Q  QTR  QTRS  QUARTER  QUARTERS | Quarter |
| W | Same day of week as 1st of month |
| WW | Same day of week as 1st of year |
| Y  YEAR  YY  YYY  YYYY | Year |

:   Examples:

```
SELECT ROUND('2013-10-11','CC')\g
```

```
2000-01-01
```

```
SELECT ROUND('23:40:10.123456','MIN')\g
```

```
23:40:00
```

```
SELECT ROUND('2013-10-11 23:40:10.123456','DD')\g
```

```
2013-10-12 00:00:00.000000
```

```
SELECT ROUND('2013-10-11','Q')\g
```

```
2013-10-01
```

```
SELECT ROUND('2013-10-11 23:40:10.123456')\g
```

```
2013-10-12 00:00:00.000000
```

**SECOND**

```
SECOND('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the second portion of a time or timestamp.

:   `SECOND(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 55

**STR_TO_DATE**

```
STR_TO_DATE(str,format)
```

:   Operand type: str and formatare character strings

:   Result type: DATE, TIME, or TIMESTAMP

:   Returns a DATETIME value if the formatstring contains both date and time parts, or a DATE or TIME value if the formatstring contains only a date or time part. If the DATE, TIME, or DATETIME value extracted from string stris illegal, the function returns NULL and produces a warning. This function is the inverse of the DATE_FORMAT() function.

:   The formatstring can contain literal characters and format specifiers beginning with %. Literal characters in formatmust match literally in str. Format specifiers in formatmust match a date or time part in str. For the specifiers that can be used in format, see [DATE_FORMAT](../SQLLanguage/SQL_Functions.md).

```
teststr(str VARCHAR(20));
```

```
INSERT INTO teststr VALUES('01,6,2012');
```

```
SELECT STR_TO_DATE(str,'%d,%m,%Y') FROM teststr;
```

:   returns

```
2012-06-01
```

!!! note "Note"

    This function works only for data stored in tables created with the VECTORWISE or VECTORWISE_ROW storage structure.

**SYSDATE**

```
SYSDATE
```

:   Result type: TIMESTAMP

:   Returns the current date and time set for the operating system on which the database resides. The format returned depends on the default TIMESTAMP format.

:   In distributed SQL statements, this function returns the date and time set for the operating system of your local database.

!!! note "Note"

    When not used inside a TO_CHAR() wrapper function, SYSDATE always returns a date in the default date format.

:   Examples:

```
SELECT SYSDATE\g
```

```
2013-08-06 22:28:35.784654-07:00
```

```
SELECT TO_CHAR(SYSDATE, 'MM-DD-YYYY HH24:MI:SS')\g
```

```
08-06-2013 22:29:58
```

**TIMESTAMPADD**

```
TIMESTAMPADD(interval, n, datetime)
```

:   Operand type: Integer, and DATE, TIME, TIMESTAMP

:   Result type: DATE, TIME, or TIMESTAMP

:   Returns the datetime after adding the specified number of intervals where:

:   intervalis a keyword from the list: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, SECOND, MILLISECOND, MICROSECOND or NANOSECOND. For compatibility, this keyword can be prefixed with SQL_TSI_.

:   n is an integer expression. The value can be positive or negative as needed.

:   datetimeis a column or a datetime expression that can be a DATE, TIMESTAMP, or TIME value.

:   `TIMESTAMPADD(YEAR, 5, '2010-10-05')` returns 2015-10-5

**TIMESTAMPDIFF**

```
TIMESTAMPDIFF(interval, datetime1, datetime2)
```

:   Operand type: Integer, and DATE, TIME, TIMESTAMP

:   Result type: Integer type

:   Returns the integer number of intervals between the two datetimes where:

:   intervalis one of the following keywords: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, SECOND, MILLISECOND, MICROSECOND or NANOSECOND. For compatibility, this keyword can be prefixed with SQL_TSI_.

:   datetime1, datetime2are columns or datetime expressions whose difference is to be determined in terms of the specific interval, and where datetime1is a start time, and datetime2is an end time.

:   The result is an integer value which can also be negative if datetime1chronologically follows datetime2.

:   `TIMESTAMPDIFF(YEAR, '2012-01-01', '2008-01-01')` returns ‑4

**TRUNC**

```
TRUNC(datetime [,str-interval])TRUNCATE(datetime [,str-interval])
```

:   Operand type: datetimeis a DATE, TIME, or TIMESTAMP.

:   Result type: DATE, TIME, or TIMESTAMP

:   Returns datetimetruncated to the unit specified by str-interval. If str-interval is omitted, then datetime is truncated to the nearest day.

:   The str-interval can be any of the following:

| Formats | Description |
| --- | --- |
| CC  CENTURY  CENTURIES | Century |
| D  DY  DAY | Starting day of week |
| DD  DDD  DAYS  J | Day |
| HH  HH12  HR  HRS  HOUR  HOURS | Hour |
| I  IY  IYY  IYYYY  ISO-YR  ISO-YRS  ISO-YEAR  ISO-YEARS | ISO year boundary |
| IW  ISO-WK  ISO-WEEK | Same day of week as 1st of ISO year |
| MI  MIN  MINS  MINUTE  MINUTES | Minute |
| MM  MO  MON  MONTH  MONTHS  RM  MOS | Month |
| Q  QTR  QTRS  QUARTER  QUARTERS | Quarter |
| W | Same day of week as 1st of month |
| WW | Same day of week as 1st of year |
| Y  YEAR  YY  YYY  YYYY | Year |

:   The precision of the result is the default precision for the input data type. For example, if TRUNC operates on a TIME column, the precision returned is 0; if TIMESTAMP, then 6.

:   Examples:

```
SELECT TRUNC('2013-10-11','CC')\g
```

```
2000-01-01
```

```
SELECT TRUNC('2013-10-11 23:40:10.123456','DD')\g
```

```
2013-10-11 00:00:00.000000
```

```
SELECT TRUNC('23:40:10.123456','MIN')\g
```

```
23:40:00
```

```
SELECT TRUNC('2013-10-11 23:40:10.123456')\g
```

```
2013-10-11 00:00:00.000000
```

**UNIX_TIMESTAMP**

```
UNIX_TIMESTAMP()UNIX_TIMESTAMP([datetime])
```

:   Operand type: DATE, TIME, or TIMESTAMP

:   Result type: INTEGER

:   Returns a UNIX timestamp (number of seconds since 1 Jan 1970) for the current time (if no argument is specified) or for the specified date.

:   `UNIX_TIMESTAMP(TIMESTAMP '2007-11-30 10:30:19')`returns 1196440219

!!! note "Note"

    This function returns a valid result up to the year 2038 because the result is always an integer4 value in the range 1 though MAX_I4.

**WEEK**

```
WEEK(date [,mode])
```

:   Operand types: dateis a DATE, TIMESTAMP. The optional modeis an integer.

:   Result type: INTEGER2

:   Returns the week number for date.

:   If the mode parameter is omitted, week 1 begins on the first Monday of the year. Dates before the first Monday of the year are considered to be in week 0. Weeks are numbered 0 to 53 for the single parameter version. (Corresponds to mode 5 in the following table.)

:   The optional modeparameter lets you specify: the starting day of the week (Sunday or Monday); the definition of the first week of the year; and whether any days before the “first week of the year” are in week 0 or in the last week of the prior year.

:   The mode values are:

| Mode | Week starts | Range | Week 1 is the first week... |
| --- | --- | --- | --- |
| 0 | Sunday | 0–53 | with a Sunday in this year |
| 1 | Monday | 0–53 | with more than 3 days this year |
| 2 | Sunday | 1–53 | with a Sunday in this year |
| 3 | Monday | 1–53 | with more than 3 days this year |
| 4 | Sunday | 0–53 | with more than 3 days this year |
| 5 | Monday | 0–53 | with a Monday in this year |
| 6 | Sunday | 1–53 | with more than 3 days this year |
| 7 | Monday | 1–53 | with a Monday in this year |

:   `WEEK(TIMESTAMP '2006-12-15 12:30:55.1234')`returns 50

:   `WEEK(DATE '2008-02-20',1)`returns 8

:   `WEEK(DATE '2008-12-31',1)`returns 53

**WEEK_ISO**

```
WEEKISO('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER1

:   Extracts the number of the week of the year that the date or timestamp refers to, and conforms to ISO 8601 definition for number of the week. Week_iso begins on Monday, but the first week is the week that has the first Thursday of the year. If you are using ISO-Week and the date falls before the week containing the first Thursday of the year, that date is considered part of the last week of the previous year, and date_part returns either 52 or 53.

:   WEEK_ISO is equivalent to WEEK() function with mode 3.

:   `WEEK_ISO(TIMESTAMP '2006-12-15 12:30:55.1234')` returns 50

**YEAR**

```
YEAR('datetime')
```

:   Operand type: DATE, TIME, TIMESTAMP

:   Result type: INTEGER2

:   Extracts the year portion of a date or timestamp.

:   `YEAR(TIMESTAMP '2006-12-15 12:30:55.1234')`returns 2006

**YEARWEEK**

```
YEARWEEK(date [,mode])
```

:   Operand types: dateis a DATE or TIMESTAMP. The optional modeis an integer.

:   Result type: INTEGER4

:   Returns year and week for date.

:   The optional modeparameter lets you specify whether the week starts on Sunday or Monday.

:   Values for the optional mode parameter are shown under WEEK Function.

:   If the modeparameter is omitted, mode 0 is assumed (so that weeks start on Sunday, and week 1 is the first week with a Sunday; dates before the first Sunday of the year are assumed to be in the last week of the prior year).

!!! note "Note"

    YEARWEEK does not return a week as week 0. The modes that would normally return dates early in the year, before the start of week 1, will compute the week as if the given date were an extension of the previous year. That is, for YEARWEEK, mode 0 operates identically to mode 2; similarly mode 1 becomes 3, mode 4 becomes 6, and mode 5 becomes 7.

:   For example: 1 January 2000 is a Saturday and is before the first week of the year, regardless of the mode selected. Therefore, it is treated as being in the last week of 1999. Since the last week of 1999 is week 52 (for all modes), YEARWEEK('2000-01-01',mode) returns 199952 (for all modes).

```
YEARWEEK(DATE '1987-01-01')
```

:   returns 198653

```
YEARWEEK(DATE '2000-01-01,4')
```

:   returns 200001

```
YEARWEEK(DATE '2000-01-01',3)
```

:   returns 199952

## Conversion Functions

Conversion functions convert the expression from one data type into another type. Type conversions can also be specified using the [CAST Expressions](../SQLLanguage/Expressions_in_SQL.md).

**ANSIDATE**

```
ANSIDATE(expr)
```

:   Operand type: CHAR, VARCHAR, ANSIDATE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: ANSIDATE

:   Converts the expression to internal ANSIDATE representation.

**BOOLEAN**

```
BOOLEAN(expr)
```

:   Operand type: CHAR, VARCHAR

:   Result type: BOOLEAN

:   Converts the string 'FALSE' and 'TRUE', without regard to case and where applicable, trailing or internal whitespace, to the corresponding BOOLEAN values.

:   Operand type: INTEGER1, SMALLINT, INTEGER, BIGINT

:   Result type: BOOLEAN

:   Converts the value 0 to FALSE and the value 1 to TRUE.

**CHAR**

```
CHAR(expr [, len])
```

:   Operand type: Any

:   Result type: CHAR

:   Converts argument to char string. If the optional length argument is specified, the function returns the leftmost len bytes. Len must be a positive integer value. If len exceeds the length of theexpr string, it is padded using space characters.

**DECIMAL or NUMERIC**

```
DECIMAL(expr [,precision[,scale]])
```

:   or

```
NUMERIC(expr [,precision[,scale]])
```

:   Operand type: Any except date and time types

:   Result type: DECIMAL

:   Converts any numeric expression to a decimal value. If scale (number of decimal digits) is omitted, the scale of the result is 0. If precision (total number of digits) is omitted, the precision of the result is determined by the data type of the operand, as follows:

:   Operand Default
Data Type Precision

:   tinyint 5

:   smallint 5

:   integer 11

:   bigint 19

:   float 15

:   float4 15

:   decimal 15

:   money 15

:   Decimal overflow occurs if the result contains more digits to the left of the decimal point than the specified or default precision and scale can accommodate.

!!! note "Note"

    Using DECIMAL on a VARCHAR column requires that the precision and scale be provided.

:   `SELECT DECIMAL('12345678.999',14,2);` returns 12345678.99

**DOW**

```
DOW(expr)
```

:   Operand type: Any absolute date

:   Result type: CHAR

:   Converts an absolute date into its day of week (for example, 'Mon,' 'Tue'). The result length is 3.

**FLOAT4**

```
FLOAT4(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL, INTEGER1, SMALLINT, INTEGER

:   Result type: FLOAT4

:   Converts the specified expression to FLOAT4. Numeric overflow can occur if the argument is too large for the result type (possible from string or decimal).

:   The range of values for float4 is processor dependent.

**FLOAT8**

```
FLOAT8(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL INTEGER1, SMALLINT, INTEGER

:   Result type: FLOAT

:   Converts the specified expression to FLOAT. Numeric overflow can occur if the argument is too large for a float (possible from string or decimal).

:   The range of values for float is determined by IEEE_754.

**HEX**

```
HEX(expr)
```

:   Operand type: Any

:   Result type: VARCHAR

:   Returns the hexadecimal representation of the internal Actian Data Platform form of the argument expression. The length of the result is twice the length of the argument, because the hexadecimal equivalent of each byte of the argument requires two bytes.

:   `HEX('ABC')`returns '414243' (ASCII) or 'C1C2C3' (EBCDIC).

:   `HEX(INT4(125))`returns '0000007D', the hexadecimal equivalent of the 4 byte binary integer 125.

**INT1 or TINYINT**

```
INT1(expr)
```

:   or

```
TINYINT(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL INTEGER1, SMALLINT, INTEGER

:   Result type: TINYINT

:   Converts the expression to TINYINT. Decimal, floating point, and string values are truncated by discarding the fractional portion of the argument. Numeric overflow occurs if the argument is too large for the result type.

**INT2 or SMALLINT**

```
INT2(expr)
```

:   or

```
SMALLINT(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL INTEGER1, SMALLINT, INTEGER

:   Result type: SMALLINT

:   Converts the expression to SMALLINT. Decimal, floating point, and string values are truncated by discarding the fractional portion of the argument. Numeric overflow occurs if the argument is too large for the result type.

**INT4 or INT or INTEGER**

```
INT4(expr)
```

:   or

```
IINT(expr)
```

:   or

```
INTEGER(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL INTEGER1, SMALLINT, INTEGER

:   Result type: INTEGER

:   Converts the expression to INTEGER. Decimal, floating point, and string values are truncated by discarding the fractional portion of the argument. Numeric overflow occurs if the argument is too large for the result type.

**INT8 or BIGINT**

```
INT8(expr)
```

:   or

```
BIGINT(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL INTEGER1, SMALLINT, INTEGER

:   Result type: BIGINT

:   Converts the expression to BIGINT. Decimal, floating point, and string values are truncated by discarding the fractional portion of the argument. Numeric overflow occurs if the argument is too large for the result type.

**INTERVAL_DTOS**

```
INTERVAL_DTOS(expr)
```

:   Operand type: CHAR, VARCHAR, INTERVAL DAY TO SECOND

:   Result type: INTERVAL DAY TO SECOND

:   Converts the expression to internal INTERVAL DAY TO SECOND representation.

**INTERVAL_YTOM**

```
INTERVAL_YTOM(expr)
```

:   Operand type: CHAR, VARCHAR, INTERVAL YEAR TO MONTH

:   Result type: INTERVAL YEAR TO MONTH

:   Converts the expression to internal INTERVAL YEAR TO MONTH representation.

**MONEY**

```
MONEY(expr)
```

:   Operand type: CHAR, VARCHAR, FLOAT, MONEY, DECIMAL INTEGER1, SMALLINT, INTEGER

:   Result type: MONEY

:   Converts the expression to internal MONEY representation. Rounds floating point and decimal values, if necessary.

**NCHAR**

```
NCHAR(expr [, len])
```

:   Operand type: Any

:   Result type: NCHAR

:   Converts argument to NCHAR Unicode string. If the optional length argument is specified, the function returns the leftmost len characters. Len must be a positive integer value. If lenexceeds the length of the exprstring, it is padded using space characters.

**NVARCHAR**

```
NVARCHAR(expr [, len])
```

:   Operand type: Any

:   Result type: NVARCHAR

:   Converts argument to NVARCHAR Unicode string. If the optional length argument is specified, the function returns the leftmost len characters.Len must be a positive integer value. If lenexceeds the length of the exprstring, the varying length is set to match the character length of the expr.

**TIME or TIME_WO_TZ**

```
TIME(expr)
```

:   or

```
TIME_WO_TZ(expr)
```

:   Operand type: CHAR, VARCHAR, TIME WITHOUT TIME ZONE, TIME WITH TIME ZONE, TIME WITH LOCAL TIME ZONE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: TIME WITHOUT TIME ZONE

:   Converts the expression to internal TIME WITHOUT TIME ZONE representation.

**TIME_LOCAL**

```
TIME_LOCAL(expr)
```

:   Operand type: CHAR, VARCHAR, TIME WITHOUT TIME ZONE, TIME WITH TIME ZONE, TIME WITH LOCAL TIME ZONE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: TIME WITH LOCAL TIME ZONE

:   Converts the expression to internal TIME WITH LOCAL TIME ZONE representation.

**TIME_WITH_TZ**

```
TIME_WITH_TZ(expr)
```

:   Operand type: CHAR, VARCHAR, TIME WITHOUT TIME ZONE, TIME WITH TIME ZONE, TIME WITH LOCAL TIME ZONE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: TIME WITH TIME ZONE

:   Converts the expression to internal TIME WITH TIME ZONE representation.

**TIMESTAMP or TIMESTAMP_WO_TZ**

```
TIMESTAMP(expr)
```

:   or

```
TIMESTAMP_WO_TZ(expr)
```

:   Operand type: CHAR, VARCHAR, TIME WITHOUT TIME ZONE, TIME WITH TIME ZONE, TIME WITH LOCAL TIME ZONE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: TIMESTAMP WITHOUT TIME ZONE

:   Converts the expression to internal TIMESTAMP WITHOUT TIME ZONE representation.

**TIMESTAMP_LOCAL**

```
TIMESTAMP_LOCAL(expr)
```

:   Operand type: CHAR, VARCHAR, TIME WITHOUT TIME ZONE, TIME WITH TIME ZONE, TIME WITH LOCAL TIME ZONE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: TIMESTAMP WITH LOCAL TIME ZONE

:   Converts the expression to internal TIMESTAMP WITH LOCAL TIME ZONE representation.

**TIMESTAMP_WITH_TZ**

```
TIMESTAMP_WITH_TZ(expr)
```

:   Operand type: CHAR, VARCHAR, TIME WITHOUT TIME ZONE, TIME WITH TIME ZONE, TIME WITH LOCAL TIME ZONE, TIMESTAMP WITHOUT TIME ZONE, TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: TIMESTAMP WITH TIME ZONE

:   Converts the expression to internal TIMESTAMP WITH TIME ZONE representation.

**TO_CHAR**

```
TO_CHAR (datetime [,format])
```

:   Operand type: ANSIDATE, TIMESTAMP, TIMESTAMP WITH TIME ZONE, or TIMESTAMP WITH LOCAL TIME ZONE

:   Result type: VARCHAR

:   Converts a datetime or interval value to a value of VARCHAR data type in the specified date format. If you omit format, then date is converted to a VARCHAR value as follows:

    - ANSIDATE values are converted to values in the default date format.

    - TIMESTAMP and TIMESTAMP WITH LOCAL TIME ZONE values are converted to values in the default timestamp format.

    - TIMESTAMP WITH TIME ZONE values are converted to values in the default timestamp with time zone format.

:   The formatcan be any of the following:

| Format | Description |
| --- | --- |
| punctuation "text" | Preserves literal punctuation and quoted text |
| AD  A.D. | AD indicator |
| AM  A.M.  PM  P.M. | AM/PM indicator |
| CC | Century (Supported in TO_CHAR only.) |
| D | Number of day of week 1 - 7 |
| DAY | Day name padded to suitable width to retain column |
| DD | Day of month 1 - 31 |
| DDD | Day of year 1 - 366 |
| DY | Day name in 3 characters |
| E  EE | Era name (Supported in TO_CHAR only.) |
| FF [1..9] | Fractional seconds |
| FM | Toggle whether formats have leading or trailing blanks |
| FX | Toggle whether exact matching is required |
| HH | Hour of day 1 - 12 |
| HH12 | Hour of day 1 - 12 (Supported in TO_CHAR only.) |
| HH24 | Hour of day 0 - 23 |
| IW | ISO week of year 1 - 53 (Supported in TO_CHAR only.) |
| IYYY  IYY  IY  I | Last 4, 3, 2, 1 digits of ISO year (Supported in TO_CHAR only.) |
| J | Julian day (days since January 1, 4712 BC) |
| MI | Minutes 0 - 59 |
| MM | Month 01 - 12 |
| MON | First 3 characters of month name |
| MONTH | Month name padded to suitable length |
| Q | Quarter 1 - 4 (Supported in TO_CHAR only.) |
| RM | Month in Roman numerals |
| RR | Round year in 2 digits |
| RRRR | Round year in 2 or 4 digits |
| SS | Seconds 0 - 59 |
| SSSS | Seconds since midnight 0 - 86399 |
| TZH | Time zone hour |
| TZM | Time zone minute |
| WW | Week of year 1 - 53 (Supported in TO_CHAR only.) |
| W | Week of month 1 - 5 (Supported in TO_CHAR only.) |
| X | Decimal |
| Y,YYY | Year with comma in this position |
| YEAR | Year spelled out (Supported in TO_CHAR only.) |
| YYYY  YYY  YY  Y | Last 4, 3, 2, or 1 digits of year |

:   For TO_CHAR, the case and punctuation of the format are important. Formats whose results are alphabetic follow the case of the format. For example, 'DY' will yield 'MON' but 'Dy' will yield 'Mon'.

```
SELECT TO_CHAR('2013-07-30 23:42:00.290533-07:00','YEAR-MONTH-DAY HH24:MI:SSXFF6 tzh:tzm');
```

:   returns 2013-JULY-TUESDAY 23:42:00.290533 -07:00

```
SELECT TO_CHAR(SYSDATE,'YYYY-MON-DD');
```

:   returns 2013-JUL-30

```
SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS');
```

:   returns 2013-07-30 23:36:19

**TO_DATE**

```
TO_DATE(char [,format])
```

:   Operand type: CHAR, VARCHAR, NCHAR, or NVARCHAR

:   Result type: ANSIDATE

:   Converts charto a value of ANSIDATE data type.

:   The formatspecifies the datetime format of char. When you omit format, then charmust be in the default date format. Valid values for format are shown under [TO_CHAR](../SQLLanguage/SQL_Functions.md). The case and punctuation of the format are not important.

:   If any part of the date is omitted the first month or first month and first date is automatically added.

:   The following examples converts a character string into a date:

:   `SELECT TO_DATE('2012-Dec-17', 'YYYY-MON-DD');` returns 2012-12-17.

:   `SELECT TO_DATE('20121217', 'YYYYMMDD');` returns 2012-12-17.

:   `SELECT TO_DATE('2012-Dec', 'YYYY-MON');` returns 2012-12-01.

:   `SELECT TO_DATE('2012', 'YYYY');` returns 2012-01-01.

**TO_TIME**

```
TO_TIME_(char [,format])
```

:   Operand type: CHAR, VARCHAR, NCHAR, or NVARCHAR

:   Result type: TIME

:   Converts charto a value of TIME data type.

:   The formatspecifies the datetime format of char. When you omit format, then charmust be in the default timestamp format. Valid values for formatare shown under [TO_CHAR](../SQLLanguage/SQL_Functions.md). The case and punctuation of the format are not important.

:   If any part of the date is omitted the first month or first month and first date is automatically added. The time component is optional. If omitted the default is 00:00:00.

:   The following example converts a character string into a timestamp:

```
SELECT TO_TIME('10:01:59','HH24:MM:SS');
```

:   returns 10:01:59

**TO_TIMESTAMP**

```
TO_TIMESTAMP(char [,format])
```

:   Operand type: CHAR, VARCHAR, NCHAR, or NVARCHAR

:   Result type: TIMESTAMP

:   Converts charto a value of TIMESTAMP data type.

:   The formatspecifies the datetime format of char. When you omit format, then charmust be in the default timestamp format. Valid values for formatare shown under [TO_CHAR](../SQLLanguage/SQL_Functions.md). The case and punctuation of the format are not important.

:   If any part of the date is omitted the first month or first month and first date is automatically added. The time component is optional. If omitted the default is 00:00:00.

:   The following example converts a character string into a timestamp:

```
SELECT TO_TIMESTAMP('2012-Dec-17', 'YYYY-MON-DD');
```

:   returns 2012-12-17 00:00:00.000000

```
SELECT TO_TIMESTAMP('20121217121314', 'YYYYMMDDHH24MISS');
```

:   returns 2012-12-17 12:13:14.000000

```
SELECT TO_TIMESTAMP ('2012-Dec', 'YYYY-MON');
```

:   returns 2012-12-01 00:00:00.000000

```
SELECT TO_TIMESTAMP ('2012', 'YYYY');
```

:   returns 2012-01-01 00:00:00.000000

```
SELECT TO_TIMESTAMP('2013-10-11 20:01:59.123456','YYYY-MM-DD HH24:MI:SSXFF6');
```

:   returns 2013-10-11 20:01:59.123456

**TO_TIMESTAMP_TZ**

```
TO_TIMESTAMP_TZ(char [,format])
```

:   Operand type: CHAR, VARCHAR, NCHAR, or NVARCHAR

:   Result type: TIMESTAMP WITH TIME ZONE

:   Converts charto a value of TIMESTAMP data type.

:   The formatspecifies the datetime format of char. When you omit format, then charmust be in the default timestamp format. Valid values for formatare shown under [TO_CHAR](../SQLLanguage/SQL_Functions.md). The case and punctuation of the format are not important.

:   If any part of the date is omitted the first month or first month and first date is automatically added. The time component is optional. If omitted the default is 00:00:00.

:   The following example converts a character string into a timestamp:

```
SELECT TO_TIMESTAMP_TZ('2012-Dec-17', 'YYYY-MON-DD TZH:MZM');
```

:   returns 2012-12-17 00:00:00.000000-08:00

```
SELECT TO_TIMESTAMP_TZ('2013-10-11 20:01:59.123456-04:00','YYYY-MM-DD HH24:MI:SSXFF6 tzh:tzm');
```

:   returns 2013-10-11 20:01:59.123456-04:00

**VARCHAR**

```
VARCHAR(expr [, len])
```

:   Operand type: Any

:   Result type: VARCHAR

:   Converts argument to VARCHAR string. If the optional length argument is specified, the function returns the leftmostlen bytes. Len must be a positive integer value. If lenexceeds the length of the exprstring, the varying length is set to match the length of the expr.

### Length of Results for Data Type Conversions

When converting decimal values to strings, the length of the result depends on the precision and scale of the decimal column.

Some functions have an optional length parameter. If this parameter is omitted, the length of the result returned by the data type conversion functions c(), char(), varchar(), nchar(), nvarchar(), and text() are as follows:

| Data Type of Argument | Result Length |
| --- | --- |
| CHAR | Length of operand |
| DECIMAL | Depends on precision and scale of column |
| FLOAT and FLOAT4 | 11 characters; 12 characters on IEEE computers |
| INTEGER1 (TINYINT) | Maximum 4 characters |
| INTEGER2 (SMALLINT) | Maximum 6 characters |
| INTEGER4 (INTEGER) | Maximum 11 characters |
| INTEGER8 (BIGINT) | Maximum 19 characters |
| NCHAR | 2 x length of operand |
| NVARCHAR | 2 x length of operand |
| MONEY | 20 characters |
| VARCHAR | Length of operand |

## Bitwise Functions

Actian Data Platform bitwise functions operate only on IPV4 and IPV6 addresses.

**BIT_AND**

```
BIT_AND(expr, expr)
```

:   Operand type: IPV4 or IPV6 addresses

:   Result type: Same as operands

:   Returns the logical AND of the two operands.

```
SELECT BIT_AND(IPV4('255.255.255.0'),IPV4('172.16.254.1'))
```

:   returns (as an IPv4)

```
172.16.254.0
```

**BIT_NOT**

```
BIT_AND(expr)
```

:   Operand type: IPV4 or IPV6 addresses

:   Result type: Same as operand

:   Returns the logical NOT of the operand.

```
SELECT BIT_NOT(IPV4('172.16.254.1'))
```

:   returns (as an IPv4):

```
83.239.1.254
```

**BIT_OR**

```
BIT_OR(expr, expr)
```

:   Operand type: IPV4 or IPV6 addresses

:   Result type: Same as operands

:   Returns the logical OR of the two operands.

```
SELECT BIT_OR(IPV4('255.255.255.0'),ipv4('172.16.254.1'))\g
```

:   returns (as an IPv4):

```
255.255.255.1
```

**BIT_XOR**

```
BIT_XOR(expr, expr)
```

:   Operand type: IPV4 or IPV6 addresses

:   Result type: Same as operands

:   Returns the logical XOR of the two operands.

```
SELECT BIT_XOR(IPV4('255.255.255.0'),IPV4('172.16.254.1'))
```

:   returns (as an IPv4)

```
83.239.1.1
```

## Hashing Functions

Hashing functions generate a fixed length “hash” value for given data. They are useful for summarizing a relatively large data item into a small fixed length representation that usually will be distinct from hashes of dissimilar data. Uniqueness is not guaranteed but the chances of two dissimilar items having the same hash value is very low.

**HASH**

```
HASH(expr)
```

:   Operand type: Any except long types

:   Result type: INTEGER4

:   Generates a four-byte numeric value from expressions of all data types except long types. The implicit size for the expression can affect the result.

```
SELECT HASH(1), HASH(int1(1)), HASH(int2(1)), HASH(int4(1))\g
```

:   returns the following single row:

```
Col1         Col2         Col3          Col4
```

```
--------------------------------------------------
```

```
-1489118143  1526341860   ‑1489118143   1711753094
```

!!! note "Note"

    Because the constant 1 is implicitly a short integer, only the return values for HASH(1) and HASH(int2(1)) match. For the remaining columns, the difference in the number of bytes holding the integer leads to a different hash value. Also, the generated hash value is not guaranteed unique, even if the input values are unique.

**MD5_HEX**

```
MD5_HEX(expr)
```

:   Operand type: CHAR, VARCHAR, NCHAR, NVARCHAR, INTEGER1, INTEGER2, INTEGER4, INTEGER8

:   Result type: CHAR(32)

:   Calculates the MD5 (Message-Digest Algorithm 5) 128-bit hash value (message digest) of expr with respect to its binary representation as given by HEX(expr).

:   Returns the hash value as a lowercase hexadecimal string.

**SHA1_HEX**

```
SHA1_HEX(expr)
```

:   Operand type: CHAR, VARCHAR, NCHAR, NVARCHAR, INTEGER1, INTEGER2, INTEGER4, INTEGER8

:   Result type: CHAR(40)

:   Calculates the SHA-1 (Secure Hash Algorithm 1) 160-bit hash value (message digest) of expr with respect to its binary representation as given by HEX(expr).

:   Returns the hash value as a lowercase hexadecimal string.

**SHA224_HEX**

```
SHA224_HEX(expr)
```

:   Operand type: CHAR, VARCHAR, NCHAR, NVARCHAR, INTEGER1, INTEGER2, INTEGER4, INTEGER8

:   Result type: CHAR(56)

:   Calculates the SHA-2 (Secure Hash Algorithm 2) 224-bit hash value (message digest) of expr with respect to its binary representation as given by HEX(expr).

:   Returns the hash value as a lowercase hexadecimal string.

**SHA256_HEX**

```
SHA256_HEX(expr)
```

:   Operand type: CHAR, VARCHAR, NCHAR, NVARCHAR, INTEGER1, INTEGER2, INTEGER4, INTEGER8

:   Result type: CHAR(64)

:   Calculates the SHA-2 (Secure Hash Algorithm 2) 256-bit hash value (message digest) of expr with respect to its binary representation as given by HEX(expr).

:   Returns the hash value as lowercase hexadecimal string.

**SHA384_HEX**

```
SHA384_HEX(expr)
```

:   Operand type: CHAR, VARCHAR, NCHAR, NVARCHAR, INTEGER1, INTEGER2, INTEGER4, INTEGER8

:   Result type: CHAR(96)

:   Calculates the SHA-2 (Secure Hash Algorithm 2) 384-bit hash value (message digest) of expr with respect to its binary representation as given by HEX(expr).

:   Returns the hash value as lowercase hexadecimal string.

**SHA512_HEX**

```
SHA512_HEX(expr)
```

:   Operand type: CHAR, VARCHAR, NCHAR, NVARCHAR, INTEGER1, INTEGER2, INTEGER4, INTEGER8

:   Result type: CHAR(128)

:   Calculates the SHA-2 (Secure Hash Algorithm 2) 512-bit hash value (message digest) of expr with respect to its binary representation as given by HEX(expr).

:   Returns the hash value as lowercase hexadecimal string.

## Random Number Functions

The random number function is used to generate random values. Use the following statement to set the beginning value for the random functions:

```
[EXEC SQL] SET RANDOM_SEED [value]
```

The seed value can be any integer. There is a global seed value and local seed values. The global value is used until you issue SET RANDOM_SEED, which changes the value of the local seed. Once changed, the local seed is used for the whole session. If you are using the global seed value, the seed is changed whenever a random function executes. This means that other users issuing random calls enhance the “randomness” of the returned value.

If you omit the value, the process ID is multiplied by the number of seconds past 1/1/1970 until now. This value generates a random starting point. You can use value to run a regression test from a static start and get identical results.

The random number functions are:

**RANDOM()**

:   Returns a random integer based on a seed value.

**RANDOMF()**

:   Returns a random float based on a seed value between 0 and 1. This is slower than RANDOM, but produces a more random number.

**RANDOM(l,h)**

:   Returns a random integer within the specified range (that is, l <= x <= h).

**RANDOMF(l,h)**

:   Passing two integer values generates an integer result within the specified range; passing two floats generates a float within the specified range; passing an int and a float causes them to be coerced to an int and generates an integer result within the specified range (that is, l >= x <= h).

!!! note "Note"

    Using the RANDOM() function after issuing SET RANDOM_SEED will not return the same results for Actian Data Platform and Ingres tables. Furthermore, it may not return the same results for every Actian Data Platform query.

## Null Handling Functions

The IFNULL, NVL, and NVL2 functions handle nulls:

**IFNULL**

```
IFNULL(v1,v2)
```

:   Operand types: Any

:   Result type: Any

:   Specifies a value other than a null that is returned to your application when a null is encountered. If the value of the first argument is not null, IFNULL returns the value of the first argument. If the first argument evaluates to a null, IFNULL returns the second argument.

:   For example, the SUM, AVG, MAX, and MIN aggregate functions return a null if the argument to the function evaluates to an empty set. To receive a value instead of a null when the function evaluates to an empty set, use the IFNULL function, as in this example:

```
IFNULL(SUM(employee.salary)/25, -1)
```

:   IFNULL returns the value of the expression sum(employee.salary)/25 unless that expression is null. If the expression is null, the IFNULL function returns -1.

IFNULL Function and Decimal Data

:   If both arguments to an IFNULL function are decimal, the data type of the result returned is decimal, and the precision (total number of digits) and scale (number of digits to the right of the decimal point) of the result is determined as follows:

        - **Precision** – The largest number of digits to the left of the decimal point (precision - scale) plus largest scale (to a maximum of 38)

        - **Scale** – The largest scale

:   If the data type of both arguments to IFNULL function match, then the result will be that data type; if there is just a size difference then the larger will be used.

:   If the two arguments are of differing data types, they must be comparable. For a description of comparable data types, see Assignment Operations. This includes any collation type associated with the parameters; if differing collations are involved, a cast may be needed to make them compatible.

:   When the arguments are different but comparable data types, the following rules are used to determine the data type of the result:

    - The result type is always the higher of the two data types; the order of precedence of the data types is as follows:

    date > money > float8 > float4 > decimal >bigint> integer > smallint > tinyint

    and

    nchar > nvarchar > c > text > char > varchar > byte > byte varying

    - The result length is taken from the longest value. For example: IFNULL with VARCHAR(10) and C(5) results in C(10).

:   Usually the first argument will be nullable but whether the function can return a null value depends only on the second argument; the result will only be nullable if a second argument is also nullable.

**NVL**

```
NVL(v1, v2)
```

:   Operand types: Any

:   Result type: Derived from v1

:   Specifies a value other than a null that is returned to your application when a null is encountered. For example, in NVL(a,b), if 'a' is NULL then return 'b' else return 'a'.

:   The data type returned will be that of the first parameter, possibly with a length increase and made nullable if the second parameter is be nullable.

**NVL2**

```
NVL2(v1, v2, v3)
```

:   Operand types: Any

:   Result type: Derived from v2

:   Returns a different value based on whether the input value is NULL or not. For example, in NVL2(a,b,c), if 'a' is not null then return 'b' else return 'c'.

:   The data type returned will be that of the v2 parameter, possibly with a length increase for v3 and made nullable if either v2 or v3 parameter is nullable.

## IP Network Address Functions

IP network address functions operate on an IPV4 or IPV6 data type or string representing an IPv4 or IPv6 address and return a string in dotted quad or colon-hex format or an IPv4 or IPv6 binary.

**INET_NTOP**

```
INET_NTOP(expr)
```

:   Operand type: IPV4 or IPV6

:   Result type: Dotted quad string or colon-hex string, depending on input type

:   Returns a dotted quad string if the input type is IPV4 or is IPV6 and an IPV4-mapped address.

:   Returns an IPv6 address in rfc5952 style (zero suppressed, shortened, lowercase) if the input type is IPV6 and is not an IPv4-mapped address.

```
SELECT INET_NTOP(INET_PTON('172.16.254.1'))
```

:   returns

```
'172.16.254.1'
```

**INET_PTON**

```
INET_PTON(expr)
```

:   or

```
IPV4(expr)
```

:   Operand type: A string representing an IPv4 network address or an IPv4-mapped IPv6 address

:   Result type: IPv4 binary

:   Converts a string in standard IPv4 dotted-quad notation to its IPv4 binary equivalent.

:   The expression can also be an IPv4-mapped IPv6 address in the form:

:   "::ffff:xxx:xxx" or "::ffff:n.n.n.n"

:   and zero-expanded or uppercased variants of the same. An error occurs if the input is an IPv6 style string that does not represent an IPv4-mapped address.

```
SELECT INET_PTON('172.16.254.1');
```

:   returns the following (using hexadeximal representation):

```
AC10FE01
```

**INET6_NTOP**

```
INET6_NTOP(expr)
```

:   Operand type: IPV4 or IPV6

:   Result type: Colon-hex string

:   Returns an IPv6 address in rfc5952 style (zero suppressed, shortened, lowercase)

```
SELECT INET6_NTOP(INET6_PTON('172.16.254.1'))
```

:   returns

```
'::ffff:ac10:fe01'
```

**INET6_PTON**

```
INET6_PTON(expr)
```

:   or

```
IPV6(expr)
```

:   Operand type: A string representing an IPv4 or IPv6 network address

:   Result type: IPv6 binary

:   Converts a string in standard hex-colon notation to an IPv6 binary equivalent. Also converts an IPv4 address in either ordinary dotted-quad or "::ffff:n.n.n.n" mixed quad notation to an IPv4-mapped address ::ffff:n.n.n.n.

:   The input can be leading-zero-suppressed. Use one “::” to replace the longest sequence of all-zero fields and use lowercase letters. The function also accepts uppercase hexits as input.

```
SELECT INET6_PTON('2001:0DB8:AC10:FE01:0000:0000:0000:0000')
```

:   returns the following (using hexadecimal representation):

```
20010DB8AC10FE010000000000000000
```

## UUID([expr]) Function

With no parameters, UUID([expr]) function creates a 128-bit UUID:

```
> createdb uuiddb
```

```
> sql uuiddb
```

```
* CREATE TABLE uuidtable (u1 UUID, u2 BYTE(16));
```

```
* INSERT INTO uuidtable VALUES (UUID(), UUID());
```

```
//
```

```
// Verify the length in byte format
```

```
//
```

```
* SELECT LENGTH(u1) FROM uuidtable;
```

```
//
```

```
//Length of u1 will be 36 bytes representing the length of the ASCII representation
```

```
//Length of u2 will be 16 bytes, the length of the BYTE(16) representation
```

```
//
```

With a parameter, UUID(expr) will convert that parameter to a UUID, if possible. Character string datatypes need to follow the 36-byte ASCII HEX format including the hyphens: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.

UUIDs stored as BYTE(16) can be readily converted into the UUID datatyape.
