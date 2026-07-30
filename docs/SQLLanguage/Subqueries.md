---
title: "Subqueries"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Subqueries.htm"
canonical_id: "actian-data-platform-subqueries"
---

## Subqueries

A subquery(or subselect) is a SELECT statement nested within another SELECT statement.

## Subqueries in the WHERE Clause

A subquery in a WHERE clause can be used to qualify a column against a set of rows.

For example, the following subquery returns the department numbers for departments on the third floor. The outer query retrieves the names of employees who work on the third floor.

```
SELECT enameFROM employeeWHERE dept IN       (SELECT dno       FROM dept       WHERE floor = 3);
```

Subqueries often take the place of expressions in predicates. Subqueries can be used in place of expressions only in the specific instances outlined in the descriptions of [Predicates in SQL](../SQLLanguage/Predicates_in_SQL.md).

The syntax of the subquery is identical to that of the select, except the SELECT clause must contain only one element. A subquery can see correlation names defined (explicitly or implicitly) outside the subquery. For example:

```
SELECT enameFROM employee empxWHERE salary >        (SELECT AVG(salary)       FROM employee empy       WHERE empy.dept = empx.dept);
```

The preceding subquery uses a correlation name (empx) defined in the outer query. The reference, empx.dept, must be explicitly qualified here. Otherwise the dept column is assumed to be implicitly qualified by empy. The overall query is evaluated by assigning empx each of its values from the employee table and evaluating the subquery for each value of empx.

!!! note "Note"

    Although aggregate functions cannot appear directly in a WHERE clause, they can appear in the SELECT or HAVING clause of a subquery that appears in a WHERE clause.

## Subqueries in the FROM Clause (Derived Tables)

Derived tables let you create or simplify complex queries. Useful in data warehousing applications, they provide a way to isolate complex portions of query syntax from the rest of a query.

A derived table is the coding of a SELECT in the FROM clause of a SELECT statement. The derived table must always use a correlation name.

For example:

```
SELECT relid, x.attname
```

```
FROM (SELECT attrelid, attrelidx, attname,
```

```
      attfrml FROM iiattribute) x, iirelation
```

```
WHERE reltid = attrelid AND reltidx = x.attrelidx
```

The derived table behaves like an inline view; the rows of the result set of the derived table are read and joined to the rest of the query. If possible, the derived table is flattened into the containing query to permit the query compiler to better optimize the query as a whole.

Some complex queries cannot be implemented without using either pre-defined views or derived tables. The derived table approach is more concise than pre-defined views, and avoids having to define persistent objects, such as views, that may be used for a single query only.

For example, consider a query that joins information to some aggregate expressions. Derived tables allow the aggregates to be defined and joined to non-aggregated rows of some other tables all in the same query. Without derived tables, a persistent view would have to be defined to compute the aggregates. Then a query would have to be coded to join the aggregate view to the non-aggregated data.

### Derived Table Syntax

The SELECT in the FROM clause must be enclosed in parentheses and must include a correlation name.

Following the correlation name, the derived table can include an override list of column names in parentheses, or these column names can be coded with AS clauses in the SELECT list of the derived table.

Columns in the derived table can be referenced in SELECT, ON, WHERE, GROUP BY, and HAVING clauses of the containing query, qualified by the correlation name, if necessary.

Example Queries Using Derived Tables

```
SELECT e.ename FROM employee e,
```

```
    (SELECT AVG(e1.salary), e1.dno FROM employee e1
```

```
        GROUP BY e1.dno) e2 (avgsal, dno)
```

```
    WHERE e.dno = e2.dno AND e.salary > e2.avgsal
```

Changing columns names with AS clause:

```
SELECT e.ename FROM employee e,
```

```
    (SELECT AVG(e1.salary) AS avgsal, e1.dno FROM employee e1
```

```
        GROUP BY e1.dno) e2
```

```
    WHERE e.dno = e2.dno AND e.salary > e2.avgsal
```

Example Query Using Derived Tables and Scalar Subquery

```
SELECT relid, x.attname
```

```
FROM (SELECT attrelid, attrelidx, attname,attfrml
```

```
      FROM attribute WHERE attrelid=(SELECT MAX(reltid) FROM relation)) x, relation
```

```
WHERE reltid = attrelid AND reltidx = x.attrelidx
```

## Subqueries in the Target List, SET and VALUE Clauses (Scalar Subqueries)

Scalar subqueries allow for the result of a query to be used in other expression contexts such as in the target list, as in the examples below.

Example query using target list scalar subquery:

```
SELECT s.i,(SELECT p.j FROM ptbl p  WHERE s.i=p.i) FROM stbl s
```

Example UPDATEs using a scalar subquery in the SET clause:

```
UPDATE stbl s SET s.j=(SELECT p.i FROM ptbl p WHERE s.i=p.i)
```

```
UPDATE stbl s SET s.i = (SELECT p.i FROM ptbl p WHERE s.i=p.i) WHERE (SELECT p.i FROM ptbl p WHERE s.i=p.i) IS NOT NULL;
```

Example INSERT using a scalar subquery in the VALUES clause:

Only non-correlated subquery in an INSERT VALUES clause.

```
INSERT INTO stbl (I, j)
```

```
       VALUES ( (SELECT MAX(p.i) FROM ptbl p, stbl s WHERE s.i = p.i ), 1);
```

!!! note "Note"

    In the INSERT VALUES clause there is no outer row to correlate between the table into which rows are being inserted and the tables in the VALUES clause.

## Scalar Subqueries

A scalar subquery is a subquery that selects only one column or expression and returns one row. A scalar subquery can be used anywhere in an SQL query that a column or expression can be used.

A scalar subquery can be used in the following contexts:

- The select list of a query (that is, the expressions between the SELECT and FROM keywords)
- In a WHERE or ON clause of a containing query

- The JOIN clause of a query
- WHERE clause that contains CASE, IF, COALESCE, and NULLIF expressions

- Source to an UPDATE statement when the subquery refers to more than the modified table
- Qualifier to a DELETE statement where the subquery identifies the rows to delete

- The VALUES clause of an INSERT statement
- As an operand in any expression

Scalar subqueries can be used to compute several different types of aggregations (max and avg) all in the same SQL statement. The following query uses both scalar subqueries and in-line views:

```
SELECT
```

```
 emp.salary,
```

```
 (SELECT MAX(salary) FROM emp mx WHERE emp.dept = mx.dept) AS highest_salary,
```

```
  MAX(nondept.salary) max_nondept_salary,
```

```
  empname AS employee_name,
```

```
  (SELECT bonus FROM commission WHERE commission.dept = emp.dept) AS bonus,
```

```
   DECIMAL((SELECT AVG(bonus) FROM commission WHERE bonus != 0),8,3) AS avg_commission,
```

```
   dept_name
```

```
FROM emp, (SELECT dept_name FROM dept WHERE dept = emp.dept) dept1,
```

```
 (SELECT MAX(salary) FROM emp mx where emp.dept != mx.dept) nondept(salary)
```

```
GROUP BY 1,2,4,5,6,7;
```

Scalar subqueries can also be used for inserting into tables, based on values from other tables. The following examples use scalar subquery to compute the maximum credit for Bill and insert this value into a max_credit table.

```
INSERT INTO max_credit (name,max_credit) VALUES (
```

```
   'Bill',
```

```
   SELECT MAX(credit) FROM credit_table WHERE name = 'Bill'
```

```
);
```

```

```

```
INSERT INTO emp_salary_summary
```

```
(sum_salaries, max_salary,min_salary, avg_salary)
```

```
VALUES (
```

```
   (SELECT SUM(salary) from emp),
```

```
   (SELECT MAX(salary) from emp),
```

```
   (SELECT MIN(salary) from emp),
```

```
   (SELECT AVG(salary) from emp));
```

A valid scalar subquery must produce at most a single value. That is, the result should consist of zero or one rows of one column.

!!! note "Note"

    Actian Data Platform does not perform a cardinality check on scalar subqueries. To avoid potentially wrong results, make sure the scalar subquery returns no more than one row.
