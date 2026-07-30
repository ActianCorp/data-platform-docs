---
title: "ALTER TABLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_TABLE.htm"
canonical_id: "actian-data-platform-alter-table"
---

## ALTER TABLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The ALTER TABLE statement can be used to:

- Add or remove a column.
- Add or remove a table-level constraint.

- Rename tables and columns. (For an alternative method of renaming tables, see [RENAME TABLE](../SQLLanguage/RENAME_TABLE.md).)

!!! note "Note"

    Adding or dropping a column is allowed only if there are no in-memory DML changes against the table. Use the MODIFY...TO COMBINE command to write the in-memory changes to disk.

This statement has the following format:

```
ALTER TABLE [schema.]table_name
```

```
   ADD [COLUMN] column_name format [default_clause] [null_clause]
```

```
       [MASKED [AS {BASIC | NULL | 0 | ' ' }] [column_constraint]
```

```
       [SET add_column_set_options]
```

```
   | ALTER [COLUMN] column_name format [default_clause] [null_clause]
```

```
       [MASKED [AS {BASIC | NULL | 0 | ' ' }] [column_constraint]
```

```
   | DROP [COLUMN] column_name RESTRICT
```

```
   | ADD [CONSTRAINT constraint_name] constraint_spec
```

```
   | DROP CONSTRAINT constraint_name RESTRICT
```

```
   | RENAME TO new_table_name
```

```
   | RENAME [COLUMN] old_column_name TO new_column_name
```

```
   | ADD MINMAX {column_name [{, column_name}] | ALL} [SET MINMAX_SAMPLES]
```

```
   | ALTER MINMAX ADD | DROP COLUMN column_name
```

```
   | DROP MINMAX
```

**table_name**

:   Specifies the name of the table to be altered.

**ADD [COLUMN] column_name format [default_clause] [null_clause] [MASKED [AS {BASIC | NULL | 0 | ' ' }] [column_constraint] [SET add_column_set_options]**

:   Adds a column. The column_name cannot already exist in the table.

:   The column is logically placed in the table definition after the last existing column. Only one column at a time can be added with the ALTER TABLE statement. The number of columns in the table and the row width cannot exceed the limits.

:   The format, default_clause, null_clause, and column_constraint have the same structure as for the CREATE TABLE statement, except that NOT NULL NOT DEFAULT is not allowed.

:   The SET add_column_set_options are:

[NO]MINMAX

:   SET [NO]MINMAX specifies whether the column should participate in a min-max index. If specified as MINMAX, the table must already have an existing min-max index. The default is MINMAX if the table has a min-max index, or NOMINMAX if not.

**Note:**If a column has a min-max index, the column_has_minmax column in the iicolumns catalog will have a value of Y (yes).

**ALTER [COLUMN] column_name format [default_clause] [null_clause] [MASKED [AS {BASIC | NULL | 0 | ' ' }] [column_constraint]**

:   Changes the characteristics of a column. For more information, see [ALTER TABLE...ALTER COLUMN Restrictions](../SQLLanguage/ALTER_TABLE...ALTER_COLUMN_Restrictions.md).

**DROP [COLUMN] column_name RESTRICT**

:   Drops a column. The column_name must exist in the specified table.Only one column can be dropped in a single ALTER TABLE statement.

**ADD [CONSTRAINT constraint_name] constraint_spec**

:   Adds a table-level constraint (see [Constraint Specifications](../SQLLanguage/ALTER_TABLE...ALTER_COLUMN_Restrictions.md)).

**DROP CONSTRAINT constraint_name RESTRICT**

:   Drops a table-level constraint.

:   **Notes:**

    - Unique and primary keys that are referenced by foreign keys cannot be dropped; the foreign key must be dropped first.

    - Foreign keys with indexes defined on them cannot be dropped; the index must be dropped first.

**RESTRICT Option**

:   The RESTRICT option does not drop the column or constraint if one or more objects exist that depend on it. For example:

    - A view with reference to the column in the base table

    - An index defined with this column

**RENAME TO new_table_name**

:   Renames a table. See [Rules and Restrictions on Renaming Tables](../SQLLanguage/ALTER_TABLE...ALTER_COLUMN_Restrictions.md).

**RENAME [COLUMN] old_column_name TO new_column_name**

:   Renames a table column. See [Rules and Restrictions on Renaming Columns](../SQLLanguage/ALTER_TABLE...ALTER_COLUMN_Restrictions.md).

**ADD MINMAX {column_name [{, column_name}] |ALL} [SET [NO]MINMAX_SAMPLES]**

:   Adds a min-max index on the specified columns. If the column list is specified as ALL, all columns are included in the new min-max index.

:   **Note:** The column_has_minmax column in the iicolumns system catalog indicates whether a column has a min-max index by the value Y (yes) or N (no).

:   Optionally, specifies whether the min-max index should be sampled. The default is NOMINMAX_SAMPLES. The MINMAX_SAMPLES setting becomes the new permanent minmax-samples property of the table. For more information, see [MINMAX_SAMPLES Option](../SQLLanguage/CREATE_TABLE.md).

!!! note "Note"

    You cannot alter an existing min-max index to be sampled or not-sampled; you must drop and re-add it.

**ALTER MINMAX ADD | DROP COLUMN column_name**

:   Adds or drops the specified column from the min-max index.

**DROP MINMAX**

:   Drops the min-max index from the table.
