---
title: "DELETE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DELETE.htm"
canonical_id: "actian-data-platform-delete"
---

## DELETE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The DELETE statement deletes rows from the specified table that satisfy the search_conditionin the WHERE clause. If the WHERE clause is omitted, the statement deletes all rows in the table. The result is a valid but empty table.

This statement has the following formats:

Interactive version:

```
DELETE FROM [schema.]table_name [corr_name]        [WHERE search_condition];
```

Embedded non-cursor version:

```
[REPEATED] DELETE FROM [schema.]table_name [corr_name]           [WHERE search_condition];
```

**table_name**

:   Specifies the name of the table from which rows are to be deleted.

**corr_name**

:   Specifies a correlation name for the table for use in the search_condition.

## DELETE Examples

1. Delete from the sales_fact table where the year is last year:

```
CREATE TABLE sales_fact (
```

```
    sales_date ANSIDATE,
```

```
    value INTEGER2,
```

```
    quantity FLOAT8);
```

```
INSERT INTO sales_fact VALUES ('2013-02-28', 120, 23.8),('2014-04-30', 1, 3.8),('2012-08-14', 30, 44.0),('2013-11-01', 1, 19.4),('2012-10-12', 3, 14.4);
```

```
DELETE FROM sales_fact WHERE year(sales_date) = year(CURRENT_DATE);
```

    One row will be deleted.

2. Delete all rows from sales_fact:

```
DELETE FROM sales_fact;
```
