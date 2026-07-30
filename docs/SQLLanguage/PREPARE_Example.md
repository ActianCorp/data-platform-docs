---
title: "PREPARE Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "PREPARE_Example.htm"
canonical_id: "actian-data-platform-prepare-example"
---

## PREPARE Example

A two-column table, whose name is defined dynamically but whose columns are called high and low, is manipulated within an application, and statements to delete, update and select the values are prepared.

```
get table_name from a set of names;statement_buffer = 'DELETE FROM ' + table_name +    ' WHERE high = ? AND low = ?';EXEC SQL PREPARE del_stmt FROM :statement_buffer;statement_buffer = 'INSERT INTO ' + table_name +    ' VALUES (?, ?)';EXEC SQL PREPARE ins_stmt FROM :statement_buffer;statement_buffer = 'SELECT * FROM ' + table_name    + ' WHERE low ?';EXEC SQL PREPARE sel_stmt FROM :statement_buffer;...EXEC SQL EXECUTE del_stmt USING :high, :low;...EXEC SQL EXECUTE ins_stmt USING :high, :low;...EXEC SQL DECLARE sel_csr CURSOR FOR sel_stmt;EXEC SQL OPEN sel_csr USING :high, :low;loop while more rows    EXEC SQL FETCH sel_csr INTO :high1, :low1;    ...end loop;
```
