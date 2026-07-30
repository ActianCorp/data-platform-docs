---
title: "FROM Clause"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "FROM_Clause.htm"
canonical_id: "actian-data-platform-from-clause"
---

## FROM Clause

The FROM clause in the UPDATE statement specifies the source tables and views from which data is to be read. The specified tables and views must exist at the time the query is issued. The from_source parameter can be:

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

- A derived table specified using the following syntax:

```
(select_stmt) corr_name [(column_list)]
```

    where select_stmt is a SELECT statement with no ORDER BY clause, corr_name is a mandatory correlation name, and column_list is an optional list of override names for the columns in the SELECT list of the select_list.

A maximum of 126 tables can be specified in a query, including the tables in the FROM list, tables in subselects, and tables and views resulting from the expansion of the definitions of any views included in the query.
