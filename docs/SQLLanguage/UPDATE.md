---
title: "UPDATE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "UPDATE.htm"
canonical_id: "actian-data-platform-update"
---

## UPDATE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The UPDATE statement updates column values in a table.

This statement has the following formats:

Interactive version:

```
UPDATE [schema.]tablename [corr_name]
```

```
              [FROM from_source {, from_source}]
```

```
              SET [corr_name.]column_name = expression{,
```

```
                  [corr_name.]column_name = expression}
```

```
              [WHERE search_condition];
```

Embedded non-cursor version:

```
EXEC SQL [REPEATED] UPDATE [schema.]tablename [corr_name]{ ,
```

```
              [FROM from_source {, from_source}]
```

```
              SET [corr_name.]column_name = expression{,
```

```
                  [corr_name.]column_name = expression}
```

```
              [WHERE search_condition];
```

The UPDATE statement replaces the values of the specified columns by the values of the specified expressions for all rows of the table that satisfy the search_condition in the WHERE clause.

If a row update violates an integrity constraint on the table, the update is not performed. table_name specifies the table for which the constraint is defined. A correlation name(corr_name)can be specified for the table for use in the search_condition. For a definition of correlation names and discussion of their use, see [Introducing SQL](../SQLLanguage/Introducing_SQL.md).

The expressions in the SET clause can use constants or column values from the table being updated or from any tables listed in the FROM clause. They also can be a scalar subquery (a SELECT statement that returns 0 or 1 rows and has a single entry in the select list).

If a column name specifies a numeric column, its associated expression must evaluate to a numeric value. Similarly, if a column name represents a character type, its associated expression must evaluate to a character type.

The result of a correlated aggregate cannot be assigned to a column. For example, the following UPDATE statement is invalid:

```
UPDATE mytable FROM yourtable
```

```
      SET mytable.mycolumn = MAX(yourtable.yourcolumn);
```

To assign a null to a nullable column, use the null constant.
