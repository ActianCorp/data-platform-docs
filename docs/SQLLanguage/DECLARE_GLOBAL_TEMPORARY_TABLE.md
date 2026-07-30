---
title: "DECLARE GLOBAL TEMPORARY TABLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DECLARE_GLOBAL_TEMPORARY_TABLE.htm"
canonical_id: "actian-data-platform-declare-global-temporary-table"
---

## DECLARE GLOBAL TEMPORARY TABLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DECLARE GLOBAL TEMPORARY TABLE statement creates a temporary table.

This statement has the following format:

```
DECLARE GLOBAL TEMPORARY TABLE [SESSION.]table_name          (column_name format {, column_name format})           [ON COMMIT PRESERVE ROWS]           [with_clause]
```

To create a temporary table by selecting data from another table:

```
DECLARE GLOBAL TEMPORARY TABLE [SESSION.]table_name          (column_name {, column_name})           AS [WITH common_table_expression] subselect          [ON COMMIT PRESERVE ROWS]           [with_clause]
```

**SESSION**

:   Allows the creation of permanent and temporary tables with the same name.

:   If the SESSION schema qualifier is used, then subsequent SQL statements that reference the table must use the SESSION qualifier. When using this syntax, the creation of permanent and temporary tables with the same name is allowed.

:   If the SESSION schema qualifier is not used, then subsequent SQL statements that reference the table can optionally omit the SESSION qualifier. This feature is useful when writing portable SQL. When using this syntax, the creation of permanent and temporary tables with the same name is not allowed.

:   A session table is local to the session, which means that two sessions can declare a global temporary table of the same name and they do not conflict with each other.

!!! note "Note"

    Syntaxes cannot be mixed in a single session. For example, if the table is declared with SESSION the first time, all declarations must use SESSION.

**table_name**

:   Defines the name of the temporary table.

**AS subselect**

:   Defines the subselect, as described in [SELECT (Interactive)](../SQLLanguage/SELECT_(Interactive).md).

**ON COMMIT PRESERVE ROWS**

:   Retains the contents of a temporary table when a COMMIT statement is issued.

**with_clause**

:   Specifies a list of valid WITH clause options, separated by a comma. Valid options are:

NORECOVERY

:   (Required for Ingres global temporary table.) Suspends logging for the temporary table.

:   (Optional for Actian Data Platform global temporary table.) If specified for a Actian Data Platform table, this option is ignored. Logging cannot be suspended for Actian Data Platform temporary tables.

[NO]MINMAX_SAMPLES

:   Creates or does not create a sampled min-max index. For more information, see [MINMAX_SAMPLES Option](../SQLLanguage/CREATE_TABLE.md).

## DECLARE GLOBAL TEMPORARY TABLE Examples

1. Use a subselect to create a temporary table containing the names and employee numbers of the highest-rated employees.

```
DECLARE GLOBAL TEMPORARY TABLE
```

```
     emps_to_promote
```

```
     AS SELECT emp_name, emp_no FROM employee
```

```
     WHERE emp_rating >= 9
```

```
     ON COMMIT PRESERVE ROWS
```

```
     WITH NORECOVERY;
```

2. Create a global temporary table and then insert the names in blocks where the rating is only a single value.

    The final select can be run many times as part of a large reporting SQL.

    When inserting a large number of records, the min-max indexing will work more efficiently if all of the rating values are in blocks. If the rating ranges 1 to 3 appear in all blocks, the scanner needs to select from all blocks; if all the values are the same in a block, the algebra required to return the required results is simple and quicker.

    Only the blocks at boundaries will have more than one rating value. Always consider that the load will be performed once and the data may be read many times. (This applies to real tables as well as temporary tables.) Always attempt to load data in the order of the most used retrieval criteria.

```
DECLARE GLOBAL TEMPORARY TABLE YYMD00(
```

```
   customer_id DECIMAL(18, 0),
```

```
   customer_name VARCHAR(20),
```

```
   customer_rating INTEGER1,
```

```
   YYDATAF FLOAT)
```

```
   ON COMMIT PRESERVE ROWS WITH NORECOVERY;
```

```
INSERT INTO YYMD00 SELECT emp_no, emp_name, 10, 2014 FROM employee WHERE emp_rating = 1;
```

```
INSERT INTO YYMD00 SELECT emp_no, emp_name, 20, 2014 FROM employee WHERE emp_rating = 2;
```

```
INSERT INTO YYMD00 SELECT emp_no, emp_name, 30, 2014 FROM employee WHERE emp_rating = 3;
```

```
SELECT customer_id, customer_name FROM YYMD00 WHERE customer_rating = 20;
```
