---
title: "DROP STATISTICS"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_STATISTICS.htm"
canonical_id: "actian-data-platform-drop-statistics"
---

## DROP STATISTICS

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL

The DROP STATISTICS statement deletes histograms created by [CREATE STATISTICS](../SQLLanguage/CREATE_STATISTICS.md).

This statement has the following format:

```
DROP {STATISTICS | STATS} FOR table [(column list)] [{, table [(column list)]} [WITH opt [,opt]]
```

**FOR table (column list)**

:   Specifies the table and optionally columns to drop statistics for. The following can be specified instead of a table and column list:

FOR ALL TABLES

:   Drops statistics for all tables in a database.

FOR userTABLES

:   Drops statistics for all tables owned by the specified user ID.

**WITH opt [,opt]**

:   Drops COLUMN COMPARE or COLUMN GROUP statistics (which are created using the same options on CREATE STATISTICS), or both, in addition to dropping the column's value histogram statistics. Values for optare:

COLUMN COMPARE

:   Drops column comparison statistics

COLUMN GROUP

:   Drops column group statistics

:   If no WITH-option is given, no column comparison or column group statistics are dropped.

:   If one WITH-option is given, all specified statistics that involve any of the columns listed in the DROP column list are dropped.

:   If no DROP column list is given, the implication is all columns, so all specified statistics for the table are dropped.

:   To drop all statistics for a table—value histogram, column comparison, and column group statistics—use WITH COLUMN COMPARE, COLUMN GROUP.

## DROP STATISTICS Examples

1. Delete the statistics created for all columns in tables a and b and columns x, y, and z in table c:

```
DROP STATISTICS FOR a, b, c(x, y, z);
```

2. Delete all column group statistics that involve the columns x, y, z in table c:

```
DROP STATISTICS FOR c(x, y, z) WITH COLUMN GROUP;
```

3. Delete all statistics for table a:

```
DROP STATISTICS FOR a WITH COLUMN COMPARE, COLUMN GROUP
```
