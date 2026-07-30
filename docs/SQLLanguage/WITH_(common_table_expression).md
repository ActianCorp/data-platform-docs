---
title: "WITH (common_table_expression)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "WITH_(common_table_expression).htm"
canonical_id: "actian-data-platform-with-common-table-expression"
---

## WITH (common_table_expression)

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

A Common Table Expression (CTE) is a temporary named result set, derived from a simple query and defined within the execution scope of a SELECT or INSERT statement. It is similar to a derived table or inline view.

CTEs can appear in the following contexts:

- SELECT
- CREATE TABLE…AS SELECT

- DECLARE GLOBAL TEMPORARY TABLE…AS SELECT
- INSERT INTO…SELECT

- CREATE VIEW

For more information and examples, see [Common Table Expressions (CTEs)](../SQLLanguage/Common_Table_Expressions_(CTEs).md).

## Guidelines for Using CTEs

A CTE is introduced into a query using the WITH clause preceding the outermost SELECT keyword. It can be used in combination with query statements or with INSERT, CREATE TABLE, DEFINE GLOBAL TEMPORARY TABLE, and CREATE VIEW.

The CTE can be a list of named subquery expressions separated by commas, each being able to reference ordinary tables and views but also able to refer to WITH elements in the same query that precede its definition. A CTE cannot refer to another in the same query that is defined later in the query.

The ability for a CTE to reference itself as in a recursive manner is not supported.

CTE definitions do not have an INTO clause or ORDER BY but can otherwise contain general subquery syntax including UNION and DISTINCT.

## WITH (common_table_expression) Syntax

A common table expression has the following format:

```
[ WITH { common_table_expression },... ]
```

where the common_table_expressionformat is:

```
expr_name [ ( { column_name },... ) ] AS ( CTE_query_def )
```

**expr_name**

:   Is an identifier for the common table expression. The expr_name must be unique among other common table expression names defined in the same WITH common_table_expressionclause, but expr_name can be the same as the name of a base table or view. Any reference to expr_name in the query uses the common table expression and not the base object.

**column_name**

:   Specifies a column name in the common table expression. Duplicate names within a single CTE definition are not allowed. The number of column names specified must match the number of columns in the result set of the CTE_query_def. The list of column names is optional only if distinct names for all resulting columns are supplied in the query expression.

**CTE_query_def**

:   Specifies a SELECT statement whose result set populates the common table expression. The SELECT statement for CTE_query_def must meet the same requirements as for creating a view, except a CTE cannot define another CTE.

:   If more than one CTE_query_def is defined, the queries must be joined by either UNION or UNION ALL.

## WITH (common_table_expression) Embedded Usage

When used with the REPEATED keyword, the WITH clause is placed after REPEATED and before the SELECT keyword.

## WITH (common_table_expression) Examples

See [Examples of Using CTEs: The Person and Relative Tables](../SQLLanguage/Common_Table_Expressions_(CTEs).md).
