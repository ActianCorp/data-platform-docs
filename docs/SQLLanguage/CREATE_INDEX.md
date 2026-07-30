---
title: "CREATE INDEX"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_INDEX.htm"
canonical_id: "actian-data-platform-create-index"
---

## CREATE INDEX

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE INDEX statement creates an index on an existing table.

!!! note "Note"

    Vertical (column-level) partitioning is not supported for indexes.

This statement has the following format:

```
CREATE INDEX [schema.]index_name ON
```

```
   [schema.]table_name (column_name {, column_name})
```

```
   [WITH-clause]
```

**index_name**

:   Defines the name of the index. It must be a valid object name.

**table_name**

:   Specifies the table on which the index is to be created.

**column_name**

:   Specifies a list of columns from the table to be included in the index.

**WITH-clause**

:   (Optional) Specifies WITH clause options:

WITH STRUCTURE=

:   Specifies the index structure:

VECTORWISE_IX

:   (Default) Creates a primary (clustered) index. Only one primary index per table is allowed.

**Note:**Secondary indexes are not supported.

## When to Use Indexing

Actian Data Platform does not rely on explicitly created indexes to achieve good performance. Most reporting and data analysis workloads do not benefit from indexed tables.

Workloads that may benefit from indexed data include:

- Highly selective filter queries on large tables
- Single row UPDATE or DELETE statements

Actian Data Platform supports primary clustered indexes. You may know this type of index as an index-organized table.

The CREATE INDEX statement by default creates a clustered index on a table that defines the physical organization of the data in storage.

The index columns define the sort order of the data in that table.

Only one clustered index can be created per table.

Creating such an index on a foreign key attribute will try to introduce a join index for the foreign key relationship by sorting the table according to the sort order of the referenced table with the matching primary key. If such a join index creation is not possible, for example, for non-matching partitioning strategies of the primary and foreign key tables, Actian Data Platform will fall back to creating a single table index of the referencing table as described previously.

Join indexes require some finesse, but if you have one dominating foreign key join, they may be worthwhile.

A clustered index will result in faster data access for queries that filter on the indexed column(s) or columns with a strong correlation to the index columns. Min-max indexes, which are created on all columns by default, provide access optimization not in addition to but as a combination of both methods.

Clustered indexes also affect query execution plans. The sorting operation on a table after an index column requested by an ORDER BY statement may be improved, benefiting from the preexisting sorting. A GROUP BY index_column statement may be accelerated using optimized operators; because of the sorting, the group is already in sequence.

A more efficient (sort) merge join may be chosen over a hash join plan when both tables have compatible clustered indexes. The (sort) merge join uses less memory than the hash join and is more efficient when data is already sorted by a clustered index.

Creating a clustered index on a table introduces considerations for update operations and can increase the memory usage to load and update data. The default target for inserted data will always be the in-memory delta structures (PDTs), and regularly reoccurring propagation to disk will be needed, either by automated or by manually triggered processes. For more information see [Data Loading Overview](../DataLoading/DataLoadingOverview.md).

Actian Data Platform does not support secondary indexes.

## Considerations for Creating a Primary Clustered Index

A clustered index (also known as a primary index) is a table organized as an index.

Use a primary index only if the table is predominantly accessed through the indexed columns. If the table is often filtered or joined only on non-indexed columns, the index will likely slow down rather than improve query performance.

Restrictions include:

- Create a primary index after creating the table.
- Only one primary index is allowed per table.

- An initial bulk load into the table is directly and efficiently written to disk. Subsequent updates are always loaded into memory first, unless the COMBINE operation (see [MODIFY...TO COMBINE Statement](../SQLLanguage/MODIFY.md)) is used.

## CREATE INDEX Examples

1. Create a primary index named l_idx on the l_shipdate column of the lineitem table:

```
CREATE INDEX l_idx ON lineitem(l_shipdate);
```

    This is identical to the following, which explicitly specifies the optional WITH clause and default option:

```
CREATE INDEX l_idx ON lineitem(l_shipdate) WITH STRUCTURE=VECTORWISE_IX;
```

2. Create a two-column primary index named idx_simple_parquet3_col1_col2 on the columns col1 and col2 of the simple_parquet3 table:

```
CREATE INDEX idx_simple_parquet3_col1_col2 on simple_parquet3 (col1, col2);
```
