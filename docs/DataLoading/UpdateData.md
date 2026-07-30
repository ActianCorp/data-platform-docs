---
title: "Updating Data"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "UpdateData.htm"
canonical_id: "actian-data-platform-updatedata"
---

# Updating Data

## Methods for Updating Data

Data can be inserted, updated, and deleted using these methods:

- As a batch or bulk operation using SQL statements or the vwload command
- As a bulk operation using the MODIFY...TO COMBINE statement

- Using tools that generate the commands and SQL statements to load the data

Updating data in Actian Data Platform tables can be done as either a batch or bulk operation.

Batch operations go to the PDTs (memory) by default. Bulk operations are written to the table files on disk by default.

Bulk operations have higher performance and lower memory footprint (data goes directly to disk), but concurrent transactions with bulk operations on the same table are not allowed. The later transaction to commit will conflict and need to be rolled back. When concurrency is needed, you can use SET INSERTMODE ROW to make the operations that by default execute in bulk mode execute in batch mode. See [Allowing Concurrent Inserts](../DataLoading/UpdateData.md).

By default, SQL statements and the VWLOAD command map to batch and bulk DML operations as follows:

- INSERT is a batch operation that quickly adds a small number of records.
- DELETE is a batch operation that quickly deletes a small number of records.

- UPDATE is a batch operation that quickly modifies a small number of records.
- CREATE TABLE AS SELECT is a bulk operation that adds many records.

- INSERT...SELECT is a bulk operation that adds many records.

    INSERT...SELECT is a batch operation if executed on a non-empty table with a clustered index.

- A batch INSERT through an ODBC, JDBC, or .Net based application is a bulk operation that adds many records.

    A batch INSERT is a batch operation if executed on a non-empty table with a clustered index.

- COPY FROM is a bulk operation that adds many records.

    COPY FROM is a batch operation if executed on a non-empty table with a clustered index.

- vwload is a bulk operation that adds many records.

    vwload is a batch operation if executed on a non-empty indexed table.

    vwload is a batch operation if --rowmode (-R) parameter is used.

In scenarios where both batch and bulk updates are valid, you can choose the method of operation by specifying:

- SET INSERTMODE BULK for bulk
- SET INSERTMODE ROW for batch

COPY FROM, INSERT...SELECT, and vwload are batch operations if executed on a non-empty table with a clustered index. For these operations to be bulk, the target table with the clustered index must meet all these conditions:

1. The table is empty.
2. There have been no batch updates performed on this table since the last MODIFY...TO COMBINE call for the table.

!!! note "Note"

    The table can be seen as empty, but there can still be batch updates stored for it in memory. This can happen if a user issues, for example, an INSERT or COPY command followed by a DELETE.

3. If the index is based on a foreign key, there can be no batch updates on the referenced table.

The following table summarizes the various update methods and their behavior depending on the target table:

| Operation | Raw Table | Table with Clustered Index when Empty | Table with Clustered Index when Not Empty |
| --- | --- | --- | --- |
| COPY FROM | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch |
| CREATE TABLE AS SELECT | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Not applicable | Not applicable |
| DELETE | Batch | Batch | Batch |
| INSERT | Batch by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch |
| INSERT...SELECT | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch |
| Batch INSERT through an ODBC, JDBC, or .NET interface | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch |
| MERGE...WHEN NOT MATCHED INSERT | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch |
| Spark SQL through the Spark-Actian Data Platform Connector | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Bulk by default;Batch with INSERTMODE ROW;Bulk with INSERTMODE BULK | Batch |
| UPDATE | Batch | Batch | Batch |
| vwload | Bulk (Batch with ‑R) | Bulk (Batch with ‑R) | Batch |

An alternative method of updating data is combining tables.

## Transfer Data from a Traditional Ingres Table

Data can be transferred in either direction between traditional Ingres tables and Actian Data Platform tables using either INSERT...SELECT or CREATE TABLE AS SELECT.

To transfer data from traditional Ingres using INSERT...SELECT

1. Create a destination table with VECTORWISE storage type:

```
CREATE TABLE dst (i INTEGER)
```

2. Issue INSERT...SELECT into that table:

```
INSERT INTO dst SELECT * FROM src
```

To transfer data from traditional Ingres using CREATE TABLE AS SELECT

Use a statement like the following:

```
CREATE TABLE dst AS SELECT FROM src
```

To create an Ingres table based on a table in the Actian Data Platform

If the default setting is to create an Actian Data Platform table, use a statement like the following:

```
CREATE TABLE dst_ing AS SELECT FROM src_vw WITH STRUCTURE = HEAP
```

!!! note "Note"

    You must be licensed to use HEAP tables in the Actian Data Platform.

Because DML operations can be costly in terms of memory resources if the batch update mode is used, an alternative way to apply data updates is to use the MODIFY...TO COMBINE statement. This process merges the updates buffered in memory, and at the same time provides a way for performing bulk DML operations on any form of a table.

Examples:

1. `DELETE FROM tab WHERE x > y`

    can be implemented with these statements:

```
CREATE TABLE deletions AS
```

```
  SELECT key FROM tab WHERE x > y;
```

```
MODIFY tab EXCEPT deletions TO COMBINE;
```

```
DROP TABLE deletions;
```

2. `UPDATE tab SET x = x + 1 WHERE x > y`

    can be implemented with these statements:

```
CREATE TABLE updates AS
```

```
  SELECT key, CAST(x + 1 AS int) AS x, y WHERE x > y;
```

```
MODIFY tab EXCEPT updates UNION updates TO COMBINE
```

```
DROP TABLE updates;
```

3. `DELETE FROM tab`

    can be implemented with this statement:

```
MODIFY tab EXCEPT tab TO COMBINE
```

**Notes:**

- Table “tab” has a primary key on the “key” column.
- The MODIFY...TO COMBINE statement works only if the column types and names of the new table match those of the original table. The example assumes that column x is type INT. When creating the updates table, the expression is casted so that it matches the type of the column in the original table. The expression “x+1” is remapped to the original column name (“AS x”).

You can use similar solutions for other DML operations.

For more information about this command, see [MODIFY...TO COMBINE Statement--Merge and Update Data](../DataLoading/UpdateData.md).

During batch operations the Actian Data Platform automatically propagates the changes buffered in memory to the disk-resident table. Because such propagation can be costly in terms of time and resources, it is best to avoid frequent propagation to large tables by using one of the following approaches:

- Consider disabling automatic propagation by setting [system] update_propagation = false.
- For large tables with frequent inserts, consider using RAW storage format.

- For tables with a clustered index, keep the volume of data changed below what will easily fit in RAM.

!!! note "Note"

    The data changes buffered in memory are not compressed.

- If a clustered index must be used for query performance, stage batches of inserts and deletes in one or more separate tables and use the [MODIFY...TO COMBINE Statement--Merge and Update Data](../DataLoading/UpdateData.md) to add them to the table.
- Enforce propagation at a convenient moment, as described in [MODIFY...TO COMBINE Statement--Merge and Update Data](../DataLoading/UpdateData.md).

For large updates, we recommend using a bulk insert (for example, COPY or vwload) to initially load the data into staging tables, and then using explicit MODIFY...TO COMBINE statements.

The syntax of the MODIFY...TO COMBINE statement is as follows:

```
MODIFY [schema.]tablename [[UNION ut] [EXCEPT et] ...] TO COMBINE
```

This statement tells the system that all tuples from except tables must be deleted from the base table, and then all tuples from union tables must be added to that table. This statement generates a new copy of the base table.

For detailed usage notes, see [MODIFY...TO COMBINE Statement](../SQLLanguage/MODIFY.md) in the SQL Language Guide.

## Propagate In-memory Updates to Disk

During batch operations the Actian Data Platform automatically propagates the changes buffered in memory to the disk-resident table.

To do this manually, use the [MODIFY...TO COMBINE Statement](../SQLLanguage/MODIFY.md). Doing so frees this memory.

Use the following SQL statement:

```
MODIFY table_name TO COMBINE
```

The most efficient way to load data into the Actian Data Platform is to use bulk append:

- vwload utility
- COPY INTO

- Batch INSERT through an ODBC, JDBC, or .NET based application

Bulk append into a non-empty table is only available for tables in RAW format (that is, without a clustered index). The performance cost of this method is roughly proportional to the volume of data appended.

When planning an append strategy, consider the granularity of appends. To maximize efficiency, each append should use multiple disk blocks. Smaller appends work fine and the Actian Data Platform will first fill up blocks at the end of the table, but larger appends will further optimize on-disk storage.

For small-cardinality data modifications, you can use the standard INSERT/DELETE/UPDATE commands, which work on all table types.

For large-cardinality deletions and updates, and for appends to a table with a clustered index, you should use:

- The explicit MODIFY...TO COMBINE method (see [Combining Tables](../DataLoading/UpdateData.md)), where you first create staging tables that contain deletions and updates, and then merge these into your tables in bulk fashion
- Batch INSERT through an ODBC, JDBC, or .NET based application

The performance cost of the MODIFY...TO COMBINE method can be significant because it is roughly proportional to the total volume of data in the table, so it should be used only when modifying a significant percentage of a table. The benefit of this approach is that it allows large modifications, results in lower memory consumption, and provides higher processing performance after the update.

Data is “inserted” into an Actian warehouse table by either an insert or an append. An insert goes to the PDTs, which reside in memory. An append is written directly to the table files on disk. (PDTs eventually are written to disk through update propagation.)

The default behavior is: Single row inserts go through the PDTs (insert), INSERT AS SELECT goes directly to disk (append).

If you need to do concurrent INSERT AS SELECTs into the same table, you must set the insert mode to ROW. The insert mode can be changed at the session level by using the [SET](../SQLLanguage/SET.md) INSERTMODE statement.

At the session level, if you do not use SET INSERTMODE ROW, then by default, a second commit will fail with the following error:

```
E_VW1120 Error committing transaction: conflict appending to table - concurrent append or update.
```

When you SET INSERTMODE to ROW in both sessions, however, the second commit will succeed.

The insert mode can also be set to BULK, which means data is appended directly to disk, which does not allow concurrent inserts. If you have two sessions and at least one of them has the insert mode set to BULK, then an error will occur.

!!! note "Note"

    The insert mode also applies to the MERGE operation.
