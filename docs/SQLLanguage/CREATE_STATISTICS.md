---
title: "CREATE STATISTICS"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_STATISTICS.htm"
canonical_id: "actian-data-platform-create-statistics"
---

## CREATE STATISTICS

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL

The CREATE STATISTICS statement creates statistics and histograms on specified tables and columns. It has the same effect as optimizedb, but allows applications to manipulate statistics from within a transaction.

This statement allows histograms to be constructed on global temporary tables, providing much better optimization of subsequent queries that reference the temporary tables.

To drop statistics, use the DROP STATISTICS statement.

This statement has the following format:

```
CREATE {STATISTICS | STATS} FOR table [(column list)] [{, table [(column list)]} [WITH option list]
```

**FOR table (column list)**

:   Specifies the table and optionally columns to create statistics for. The following can be specified instead of a table and column list:

FOR ALL TABLES

:   Creates statistics for all tables in a database.

FOR ALL userTABLES

:   Creates statistics for all tables owned by the specified user ID.

**WITH option list**

:   Specifies options for creating statistics, as any of the following:

NOSAMPLE

:   Requests no sampling. All rows from the table are read to create the histograms. It has the same effect as the optimizedb -zns flag.

SAMPLE = n

:   Specifies the percentage (n) of rows to be sampled in creating the histograms.

:   Limits: 0 through 100

:   Default: If this option is not specified, tables with more than two million rows are sampled to reduce the number of rows processed to one million. For example, if there are five million rows, a 20% sample is used.

MAXCELLS = n

:   Specifies the maximum number of cells (n) to create in the histograms.

:   Limits: 32000

:   Default: 1000

COLUMN COMPARE

:   Requests the building of column comparison statistics for compatible pairs of columns in each table.

COLUMN GROUP

:   Requests the building of column grouping statistics. These statistics should improve the estimates of some cardinalities that are subject to column correlation. COLUMN GROUP can be specified only with explicit table names and only with column lists with two, three, or four column names. The FOR ALL syntax is not supported for column groups.

ENCRYPTED

:   Allows statistics to be generated for encrypted columns. Without the ENCRYPTED option, CREATE STATISTICS skips encrypted or masked columns or issues an error if they are explicitly named.

**Caution!**The existence of column statistics exposes a small sampling of the column data through the iihistogram catalog. Database administrators should weigh this partial exposure against possible performance gains when encrypted columns are involved in WHERE or ON clause predicates. Having to use the ENCRYPTED option is designed to prevent accidental exposure of sensitive data.

## CREATE STATISTICS Permissions

CREATE STATISTICS FOR ALL TABLES requires DB_ADMIN or equivalent privileges.

CREATE STATISTICS FOR ALL ownerTABLES requires that the effective user be owner, or that the session have DB_ADMIN or equivalent privileges.

CREATE STATISTICS FOR tablename, ... requires that the user own the table, or the session have DB_ADMIN or equivalent privileges, or the user be granted the MODIFY privilege for the table. If any table in the list fails the permission check, the entire statement fails.

Similar permissions are required for [DROP STATISTICS](../SQLLanguage/DROP_STATISTICS.md).

!!! note "Note"

    “DB_ADMIN or equivalent” means that the user must be the DBA (owner) of the database, or has been granted the DB_ADMIN database privilege for the database or installation, or is defined as a SECURITY user.

## CREATE STATISTICS Example

1. Generate statistics for all columns in tables a and b and columns x, y, and z in table c:

```
CREATE STATISTICS FOR a, b, c(x, y, z);
```

2. Generate statistics for columns p and q of the global temporary table ttab. Subsequent queries that reference the temporary table will be compiled with those statistics:

```
CREATE STATISTICS FOR session.ttab(p, q);
```
