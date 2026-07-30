---
title: "ALTER TABLE...ALTER COLUMN Restrictions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_TABLE...ALTER_COLUMN_Restrictions.htm"
canonical_id: "actian-data-platform-alter-tablealter-column-restrictions"
---

## ALTER TABLE...ALTER COLUMN Restrictions

ALTER TABLE...ALTER COLUMN is supported for Actian Data Platform tables only for changing the default value or changing the masking.

## Rules and Restrictions on Renaming Tables

Be aware of the following guidelines and restrictions when renaming tables:

- You must own any table you rename.
- The name of the new table must conform to the naming rules for tables (see [Object Naming Rules](../SQLLanguage/Object_Naming_Rules.md)).

- There must be no table already existing in the database having the same name and owned by the same user as the new table name. (The new table name will get the same internal relation ID (reltid) as the old table name.)
- Indexes, grants, comments, synonyms, sequences are automatically transferred to the newly renamed table or column.

- The ALTER TABLE or RENAME operation can be rolled back.
- If any views refer to the table being renamed, the rename operation will fail with errors. Names of dependent objects are included in the error log for each dependent object.

- Primary key constraints, foreign key constraints, and unique constraints on the table will be transferred to the new table name.
- Any forms, join definitions, or reports that refer to the old table name will be invalidated.

## Rules and Restrictions on Renaming Columns

Be aware of the following guidelines and restrictions when renaming columns:

- You must own any table containing columns you rename.
- The name of the new column must conform to the naming rules for columns (see [Object Naming Rules](../SQLLanguage/Object_Naming_Rules.md)).

- There must be no column already existing in the table having the same name.
- If any views refer to the table column being renamed, the rename operation will fail with errors.

- The ALTER TABLE RENAME COLUMN operation can be rolled back.
- Any forms, join definitions, or reports that refer to the old table column name will be invalidated.

## Constraint Specifications

When a constraint is added to a table, the table is checked to ensure that its contents do not violate the constraint. If the contents of the table do violate the constraint, the Actian Data Platform returns an error and does not add the constraint.

The following table summarizes the elements of the constraint_clause:

| Type | Keyword | Example |
| --- | --- | --- |
| Referential | REFERENCES | `ALTER TABLE dept_constADD CONSTRAINT chkmgrFOREIGN KEY(mgr) REFERENCES emp(ename);` |
| Unique | UNIQUE | `ALTER TABLE emp_constADD UNIQUE (eno, ename);` |
| Primary key | PRIMARY KEY | `ALTER TABLE emp_constADD CONSTRAINT ekeyPRIMARY KEY(eno);` |

For more information, see [Constraints](../SQLLanguage/CREATE_TABLE.md).

## Named Constraints

If the constraint name is omitted, the Actian Data Platform assigns a name.

To assign a name to a constraint on the ALTER TABLE statement, use the following syntax:

```
ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_clause
```

The keyword CONSTRAINT must be used only when specifying a name.

For example, the following statement adds a named constraint to the dept table:

```
ALTER TABLE dept ADD CONSTRAINT dept_unique UNIQUE(name);
```

The following statement adds an internally named constraint to the dept table:

```
ALTER TABLE dept ADD UNIQUE(name);
```

To drop a constraint, using the following syntax:

```
ALTER TABLE table_name DROP CONSTRAINT constraint_name RESTRICT
```

For example, the following ALTER TABLE statement drops the constraint named dept_unique:

```
ALTER TABLE dept DROP CONSTRAINT dept_unique RESTRICT;
```

To find a system-defined constraint name (valid in interactive SQL but not in the Query Editor):

```
HELP CONSTRAINT table_name;
```

You can also use the following:

```
SELECT * FROM iiconstraints WHERE table_name = table_name;
```

If a system-defined constraint name is being dropped, specify the constraint name using a delimited identifier (that is, in double quotes), because system-defined constraint names include special characters.

## ALTER TABLE Examples

1. Add a column to an existing table:

```
ALTER TABLE emp_const ADD COLUMN location CHAR(10);
```

2. Drop a column from an existing table:

```
ALTER TABLE emp_const DROP COLUMN location RESTRICT;
```

3. Add a table-level constraint

```
ALTER TABLE t1 ADD CONSTRAINT pkey PRIMARY KEY(col1);
```

4. Drop a table-level constraint:

```
ALTER TABLE t2 DROP CONSTRAINT pkey RESTRICT;
```

5. Given the following two tables:

```
CREATE TABLE dept (
```

```
   name CHAR(10) NOT NULL,
```

```
   location CHAR(20),
```

```
CONSTRAINT dept_unique UNIQUE(name);
```

```

```

```
CREATE TABLE emp_const (
```

```
   name CHAR(10) NOT NULL,
```

```
   salary DECIMAL(10,2),
```

```
   dept CHAR(10)
```

```
CONSTRAINT empref REFERENCES dept(name));
```

    The following statement returns an error because there is a referential constraint that depends on dept_unique.

```
ALTER TABLE dept DROP CONSTRAINT dept_unique RESTRICT;
```

    Dropping the empref constraint from table emp_const will work:

```
ALTER TABLE emp_const DROP CONSTRAINT empref RESTRICT;
```

6. Add a column to an existing table. :

```
ALTER TABLE emp_const ADD COLUMN department CHAR(12) NOT NULL WITH DEFAULT
```

!!! note "Note"

    If NOT NULL is specified the WITH DEFAULT is mandatory but no value can be specified.

7. Rename a table:

```
ALTER TABLE tbl RENAME TO newtbl
```

```
RENAME TABLE tbl2 TO newtbl2
```

8. Rename a table column:

```
ALTER TABLE newtbl RENAME COLUMN col1 TO col001
```

9. Add the MASKED attribute to the salary column of the employee table:

```
ALTER TABLE employee ALTER COLUMN salary FLOAT MASKED AS 0;
```

10. Add a sampled min-max index on one column:

```
ALTER TABLE sales_fact ADD MINMAX value WITH MINMAX_SAMPLES;
```
