---
title: "Using Column Masking"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Using_Column_Masking.htm"
canonical_id: "actian-data-platform-using-column-masking"
---

# Using Column Masking

## Column Masking

Column masking (sometimes referred to as data masking) lets you assign the MASKED attribute to columns so that unprivileged users cannot view the data. Users with the UNMASK privilege can see the data that is masked to other users and can also control how that data can be interacted with.

The column mask is essentially an expression mask that can be assigned to a column as a default attribute. Masking does not affect the data at rest in masked columns; the masking is applied when such data is accessed through SQL statements.

To mask a column, use the SQL syntax `MASKED [AS {BASIC | NULL | 0 | ' '}]` as a column attribute on the [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md), CREATE TABLE...AS SELECT statement (which creates a table and loads rows from another table), or ALTER TABLE ALTER COLUMN statement.

The MASKED attribute marks the column as being a protected resource. The attribute can specify that masked data be presented to unprivileged users as asterisks (BASIC) or returned as NULL, zero, or blank.

The SQL function `MASK_COLUMN(expr AS {BASIC | NULL | 0 | ' ' | UNMASK})` can be used by a user with the UNMASK privilege to override the masking or to alter the way the masked data is displayed.

Masking is applied to the column when it is referenced in a query unless a privileged user has specified otherwise using the MASK_COLUMN control in a view. This is typically fine for simple queries that return a result column; the unprivileged user will see the data except for the masked column.

Masking, however, also applies to masked columns that are joined or aggregated upon. By default, for a user without the UNMASK privilege, the values aggregated or joined upon would be masked and not the underlying data. This is intentional, to avoid potential attempts to uncover the actual values of the masked data. If it is necessary to allow a masked column to participate in a join for correctness of a query, then the MASK_COLUMN() function can be used to control what the masking does.

For example:

```
CREATE TABLE employee(
```

```
name VARCHAR(20),
```

```
address VARCHAR(20) MASKED,
```

```
salary FLOAT MASKED AS 0);
```

Users without the UNMASK privilege would see the “address” column presented as asterisks and “salary” replaced with “0.0”.

Users with UNMASK can see these masked columns without any masking and they can also create views that grant controlled access to the masked data.

If there were a need to allow aggregated data such as minimum, maximum, and average salaries to be known, the default masking would return 0 for all these results because the aggregations need the real data. A view, however, can be created to unmask the salary column so that the MIN, MAX, and AVG aggregations can be made on the real data, and the calculations reported accurately.

```
CREATE VIEW employee_salary_stats AS SELECT
```

```
MIN(MASK_COLUMN(salary AS UNMASK)) min_salary,
```

```
MAX(MASK_COLUMN(salary AS UNMASK)) max_salary,
```

```
AVG(MASK_COLUMN(salary AS UNMASK)) average_salary FROM employee;
```

```
GRANT select ON employee_salary_stats TO public;
```

To do this, a user requires the UNMASK privilege, but all other users could then see the results of the query with actual data. Creating views in this manner clearly needs to be done with care so as not to allow the underlying data to be revealed in an uncontrolled manner. To safely reveal the pay ladder without the actual figures would require similar unmasking on the join:

```
CREATE VIEW salary_ladder AS SELECT e.name,COUNT(*)
```

```
FROM employee a LEFT JOIN employee b
```

```
ON MASK_COLUMN(a.salary AS UNMASK)<=MASK_COLUMN(b.salary AS UNMASK)
```

```
GROUP BY a.name ORDER BY 1;
```

```
GRANT select ON salary_ladder TO public;
```

The MASK_COLUMN() function, used in the above example with UNMASK, can also be used with the BASIC, NULL, ' ' and 0 options, to vary the presentation in views. It can also be used to vary the point at which masking is applied.
