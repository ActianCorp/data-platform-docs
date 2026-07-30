---
title: "Managing Tables and Views"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "TablesViews.htm"
canonical_id: "actian-data-platform-tablesviews"
---

# Managing Tables and Views

## Table Management

You can perform the following basic operations on tables:

- Create and alter table objects
- View existing table objects, including details such as the rows, columns, statistics, and other properties

- Drop table objects

In SQL, you can accomplish these tasks using the [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md), [ALTER TABLE](../SQLLanguage/ALTER_TABLE.md), [HELP](../SQLLanguage/HELP.md) TABLE, [MODIFY](../SQLLanguage/MODIFY.md) TABLE, and [DROP](../SQLLanguage/DROP.md) statements.

## Tools for Creating a Table

You can create a table by issuing a [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md) statement from any of the following tools:

- A terminal monitor
- Interactive SQL (see [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md))

- An embedded SQL program, Java, .NET scripts

## Table Ownership

New tables are owned by the user who creates them. The owner of the table can perform certain operations on the table that other users are not allowed to do. For example, only the owner (or a user with the security privilege impersonating the owner) can alter or drop a table.

If other users need access to the table, the table owner can grant that permission using table grants. Table grants are enablingpermissions—if no permission is granted, the default is to prohibit access.

## Enable or Disable Journaling

When you create a table, journaling can be enabled by using the WITH JOURNALING option on [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md).

## Duplicate Rows in Tables

A table contains duplicate rows when two or more rows are identical. Duplicate rows are allowed.

## Data Type Conversion Functions for Default Values

When you create or alter a table, you can specify a default value for any column, which is used when no value is specified for the column. Instead of specifying a typical default value of zero or quoted spaces for a column, you may want to substitute a value as the default value for the new column. To do this, use the associated conversion function for the data type assigned to the new column.

The following table lists the data type and an example of its associated conversion function for creating a column:

| Data Type | Default Conversion Function |
| --- | --- |
| char | char(' ') |
| c | c(' ') |
| VARCHAR | VARCHAR(' ') |
| INTEGER8 | INT8(0) |
| INTEGER4 | INT4(0) |
| INTEGER2 | INT2(0) |
| INTEGER1 | INT1(0) |
| FLOAT8 | FLOAT8(0) |
| FLOAT4 | FLOAT4(null) |
| DECIMAL | DECIMAL(0) |
| ANSIDATE | ANSIDATE('') or ANSIDATE(null) |
| TIME WITH TIME ZONE | TIME_WITH_TZ(' ') or TIME_WITH_TZ(null) |
| TIME WITHOUT TIME ZONE | TIME_WO_TZ(' ') or TIME_WO_TZ(null) |
| TIME WITH LOCAL TIME ZONE | TIME_LOCAL(' ') or TIME_LOCAL(null) |
| TIMESTAMP WITH TIME ZONE | TIMESTAMP_WITH_TZ(' ') or TIMESTAMP_WITH_TZ(null) |
| TIMESTAMP WITHOUT LOCAL TIME ZONE | TIMESTAMP_WO_TZ(' ') or TIMESTAMP_WO_TZ(null) |
| TIMESTAMP WITH LOCAL TIME ZONE | TIMESTAMP_LOCAL(' ') or TIMESTAMP_LOCAL(null) |
| INTERVAL DAY TO SECOND | INTERVAL_DTOS(' ') or INTERVAL_DTOS(null) |
| INTERVAL YEAR TO MONTH | INTERVAL_YTOM(' ') or INTERVAL_YTOM(null) |
| MONEY | MONEY(0) |

If the new column is created with no conversion function, the defaults are:

- VARCHAR for character strings
- FLOAT8 for floating point numbers

- Either INTEGER2 or INTEGER4 for integer numbers (depending on the size of the number)

To initialize a column’s value to null, specify the default value of null in any of the numeric conversion functions or the date function. Doing so makes the column nullable.

!!! warning "Important"

    **IMPORTANT!**Do not use null as a default value for character fields—this causes an attempt to create a character field of null length, which cannot be done, and returns an error.

## Constraints

When you create or alter a table, define constraints for the table. Constraints are used to check for appropriate data values whenever data is entered or updated in the table.

Constraints are checked at the end of every statement that modifies the table. If the constraint is violated, the Actian Data Platform returns an error and terminates the statement. If the statement is in a multi-statement transaction, the transaction is not terminated.

Define constraints using the [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md) or [ALTER TABLE](../SQLLanguage/ALTER_TABLE.md) statements.

### Constraint Types

Types of constraints are:

- Unique
- Referential

- Primary key

#### Unique Constraints

You can define unique constraints at both the column and the table level. Columns that you specify as unique or that you use as part of a table-level unique constraint can be nullable. Column-level unique constraints ensure that no two rows in the table can have the same value for that column. At the table level, you can specify several columns, all of which are taken together to determine uniqueness.

For example, if you specify the department name and department location columns to be unique at the table level, no two departments in the same location can have the same name:

```
CREATE TABLE depts ( dname CHAR(10) NOT NULL,
```

```
                     dlocation CHAR(10) NOT NULL)
```

```
CONSTRAINT unique_dept UNIQUE (dname, dlocation));
```

You can specify a maximum of 32 columns in a table-level unique constraint; however, a table can have any number of unique constraints.

In contrast, specifying the department name and department location columns to be unique at the column level is more restrictive—in this case, no two departments can have the same name, regardless of the location, and no two locations can have the same name either.

```
CREATE TABLE dept (dname CHAR(10) UNIQUE NOT NULL,
```

```
                   dlocation CHAR(10) UNIQUE NOT NULL);
```

Unique keys can be nullable. There can be multiple rows with NULL. For multi-column keys (table-level unique constraint), uniqueness is enforced only on keys without NULL in any of the key columns.

#### Referential Constraints

Referential constraints are used to validate an entry against the contents of a column in another table (or another column in the same table), allowing you to maintain the referential integrity of your tables. In SQL, use the REFERENCES option of the [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md) and [ALTER TABLE](../SQLLanguage/ALTER_TABLE.md) statements.

For more information on referential action options, see the SQL Reference Guide.

When defining a referential constraint, you must consider the following points:

- The table that you intend to reference must exist, with the appropriate primary key or unique constraint defined.
- Referencing columns from the table in which the constraints are being defined are compared to columns that make up the primary key or a table-level unique constraint in the referenced, or parent, table.

- The data types of the columns must be comparable, and the referencing columns must correspond in number and position to those in the referenced table.
- You must have references permission for the referenced columns.

The following example of a referential constraint assumes that the employee table exists with a primary key constraint defined involving a name and an employee number column.

This example verifies the contents of the name and empno columns in the manager table against the primary key columns in the employee table, to ensure that anyone entered into the table of managers is on file as an employee.

```
CREATE TABLE manager (name CHAR(10),
```

```
empno CHAR(5),
```

```
...
```

```
FOREIGN KEY (name, empno) REFERENCES emp);
```

#### Primary Key Constraint

Primary key constraints can be used to denote one or more columns, which other tables reference in referential constraints.

!!! note "Note"

    Primary key constraints can be used as an alternative and slightly more restrictive form of unique constraint but need not be used at all.

To define a primary key, you choose which columns are to be part of the key and assign to each a position in the key. Columns that are part of the primary key cannot be nullable, and the primary key is implicitly unique. A table can have only one primary key, which can consist of a maximum of 32 columns.

To create a primary key constraint, use the SQL [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md) or [ALTER TABLE](../SQLLanguage/ALTER_TABLE.md) statements.

For example, using SQL, in the partnumbers table, define the partno column as the primary key. The inventory table has a comparable column named ipartno. A referential constraint can be defined on the inventory table based on the partnumbers table.

```
CREATE TABLE partnumbers  (partno INTO NOT NULL PRIMARY KEY,   desc VARCHAR(20),   type CHAR(1) NOT NULL);
```

```
CREATE TABLE inventory  (ipartno INT NOT NULL,   start_date DATE,   type CHAR(1) NOT NULL,   end_date DATE,   qty INT NOT NULL);
```

```
ALTER TABLE inventory ADD CONSTRAINT fk_ipart FOREIGN KEY (ipartno) REFERENCES partnumbers;
```

In this case, the part numbers in the inventory table are checked against those in the partnumbers table. When defining this referential constraint, it is not necessary to specify the column to be referenced in the partnumbers table because it was defined as the primary key.

## Delete Constraints

To delete a constraint using SQL, use the [ALTER TABLE](../SQLLanguage/ALTER_TABLE.md)...DROP CONSTRAINT statement. When you drop a constraint, you must specify RESTRICT. RESTRICT terminates the operation if there are any constraints that depend on the constraint being dropped.

A view can be thought of as a virtual table. Only the definition for the view is stored, not the data. A table on which a view operates is called a base table.

A view definition can encompass 1 to 380 base tables. It can involve multiple tables joined together by their common columns using a where qualification.

A view can be created on other views or on physical database tables.

A view can be defined on any valid SELECT query that does not contain an ORDER BY, FIRST n, or FETCH FIRST clause.

!!! note "Note"

    Up to 128 table objects (table, view, synonym, and index) can be used in a view with the default DBMS Server stack size. To allow the full count of 380 table objects the stack_size needs to be raised to 1.5m (1572864). Failure to do so may result in the session error E_OP08A2.

Primary uses for views include:

- Providing security by limiting access to specific columns in selected tables, without compromising database design
- Simplifying a commonly used query

- Defining reports
- UNION ALL views that combine tables of current, recent, and archived data

Because a view is a device designed primarily for selecting data, all selects on views are fully supported. Simply use a view name in place of a table name in the SELECT statement. Updating views is also supported on simple single table views (see [Updates on Views](../DataLoading/TablesViews.md)) but updating a database by means of a view is not recommended.

## Views and Permissions

Any user can create a view on any other user’s tables or views, provided they have the permissions required to execute the SELECT statements that define the view. Any user can grant permissions on their views to any other user, provided they either own the base tables in the view or have the with grant option on the permissions they are granting. Granting of permissions is described in the Security Guide.

## Working with View Objects

You can perform the following basic operations on views:

- Create view objects
- View existing view objects, including details such as the view definition, grantees, and rows

- Drop view objects

In SQL, you can accomplish these tasks using the SQL statements CREATE VIEW, HELP, HELP VIEW, and DROP VIEW. For more information, see the SQL Language Guide.

## Updates on Views

Only a limited set of updates on views is supported because of problems that can occur. Updates are not supported on views that have more than one base table, or on any column whose source is not a simple column name (for example, set functions or computations).

Updating is supported only if it can be guaranteed (without looking at the actual data) that the result of updating the view is identical to that of updating the corresponding base table.

!!! note "Note"

    Updating, deleting, or inserting data in a table using views is not recommended. You can update, delete, or insert with SQL statements, but you must abide by the following rules, keeping in mind that an error occurs if you attempt an operation that is not permitted.

### Types of Updates Not Permitted on Views

You cannot perform the following types of updates on a view:

- One that involves a column that is a set function (aggregate) or derived from a computational expression

    In the following example of a SELECT statement used to define a view, you cannot update the tsal column because it is a set function:

```
SELECT dept, SUM(sal) AS tsal  FROM deptinf GROUP BY dept
```

- One that causes more than one table to be updated

    Consider the following example of a SELECT statement used to define a view:

```
SELECT e.name, e.dept, e.div, d.bldg  FROM emp e, deptinf d  WHERE e.dept = d.dname AND e.div = d.div
```

    Updates to this data must be done through the underlying base tables, not this view.

- You can update a column that appears in the qualification of a view definition, as long as the update does not cause the row to disappear from the view. For example, if the WHERE clause is as follows, update the deptno from 5 to 8, but not from 5 to 20:

```
WHERE deptno < 10
```

Aschema is a collection of any of the following database objects:

- Tables
- Views

- Grants

Each user can have only one schema consisting of definitions of the above types of database objects that the user owns. The database objects belong to the specific schema.

By default, the current user’s schema is always assumed.

The following features are available to the DBA and other users to assist in manipulating table data and referencing tables:

- Synonyms for table names
- Temporary tables local to an individual session

- Comments for documenting and describing tables

## Synonyms

The DBA or any user can create synonyms for tables, views, and indexes. These alternate names, or aliases, can be used to define shorthand names in place of long, fully qualified names.

After a synonym is created, it can be referenced the same way as the object for which it was created. For example, if you create a synonym for a table or view, issue SELECT statements using the synonym name, just as you use the table or view name.

### Working with Synonym Objects

You can perform the following basic operations on synonyms:

- Create synonym objects
- View existing synonym objects, including the detailed properties of each individual object

- Drop synonym objects

In SQL, you can accomplish these tasks using the statements [CREATE SYNONYM](../SQLLanguage/CREATE_SYNONYM.md), HELP SYNONYM, and [DROP SYNONYM](../SQLLanguage/DROP_SYNONYM.md).

## Temporary Tables

Temporary tables are useful in applications that need to manipulate intermediate results and minimize the processing overhead associated with creating tables.

Temporary tables reduce overhead in the following ways:

- No logging or locking is performed on temporary tables.
- No page locking is performed on temporary tables.

- Disk space requirements are minimized. If possible, the temporary table is created in memory and never written to disk.
- No system catalog entries are made for temporary tables.

Because no logging is performed, temporary tables can be created, deleted, and modified during an online checkpoint.

Temporary tables are:

- Visible only to the session that creates them
- Deleted automatically when the session ends

- Declarable by any user, whether or not the user has the CREATE_TABLE permission

The [DECLARE GLOBAL TEMPORARY TABLE](../SQLLanguage/DECLARE_GLOBAL_TEMPORARY_TABLE.md) statement is used to create temporary (session-scope) tables.

All temporary tables are automatically deleted at the end of the session. To delete a temporary table before the session ends, issue a DROP TABLE statement.

### Temporary Table Declaration and the Optional SESSION Schema Qualifier

SQL supports two syntaxes for declaring and referencing global temporary tables:

**With the SESSION Schema Qualifier**

:   If the [DECLARE GLOBAL TEMPORARY TABLE](../SQLLanguage/DECLARE_GLOBAL_TEMPORARY_TABLE.md) statement defines the table with the SESSION schema qualifier, then subsequent SQL statements that reference the table must use the SESSION qualifier.

:   When using this syntax, creating permanent and temporary tables with the same name is allowed.

**Without the SESSION Schema Qualifier**

:   If the [DECLARE GLOBAL TEMPORARY TABLE](../SQLLanguage/DECLARE_GLOBAL_TEMPORARY_TABLE.md) statement defines the table without the SESSION schema qualifier, then subsequent SQL statements that reference the table can optionally omit the SESSION qualifier. This feature is useful when writing portable SQL.

:   When using this syntax, creating permanent and temporary tables with the same name is not allowed.

**Notes:**

- In both modes, a session table is local to the session, which means that two sessions can declare a global temporary table of the same name and they do not conflict with each other.
- Syntaxes cannot be mixed in a single session. For example, if the table is declared with SESSION the first time, all declarations must use SESSION.

### Examples of Working with Temporary Tables

To create two temporary tables, names and employees, for the current session, issue the following statements:

```
DECLARE GLOBAL TEMPORARY TABLE SESSION.names  (name VARCHAR(20), empno VARCHAR(5))  ON COMMIT PRESERVE ROWS   WITH NORECOVERY;DECLARE GLOBAL TEMPORARY TABLE SESSION.employees AS  SELECT name, empno FROM employees  ON COMMIT PRESERVE ROWS  WITH NORECOVERY;
```

!!! note "Note"

    The “SESSION.” qualifier in the example is optional. If omitted, the name of the temporary table cannot be the same as any permanent table names.

The names of temporary tables must be unique only in a session.

For more information on working with temporary tables, see the descriptions for [DECLARE GLOBAL TEMPORARY TABLE](../SQLLanguage/DECLARE_GLOBAL_TEMPORARY_TABLE.md) and [DROP](../SQLLanguage/DROP.md) statements.

## Comments to Describe Tables and Views

When working with tables and views in applications, it is helpful to include commentary about the structure and uses of tables and views.

Tables and views can be commented with:

- Comment lines in SQL or a host language, for example, “/*comment*/” or “--comment”
- Comments specified with the COMMENT ON statement

### The COMMENT ON Statement

The [COMMENT ON](../SQLLanguage/COMMENT_ON.md) statement lets you add commentary to SQL programs. Using this statement, you can create a comment for the table, view, and for individual columns in the table.

For example, to add a remark on the name column and on the status column of the employee table:

```
COMMENT ON employee IS  'This is the ALL Employees table including managers and their direct reports';
```

```
COMMENT ON COLUMN employee.status IS  'valid codes are:      01, exempt; 02, non-exempt; 03, temp';
```

To show a comment, use the HELP COMMENT statement. For example, the comment on the status column can be shown by the statement:

```
HELP COMMENT COLUMN employee status;
```

To delete a comment, specify an empty string. For example, the comment on the status column can be deleted by this statement:

```
COMMENT ON COLUMN employee.status IS '';
```
