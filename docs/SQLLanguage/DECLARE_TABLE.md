---
title: "DECLARE TABLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DECLARE_TABLE.htm"
canonical_id: "actian-data-platform-declare-table"
---

## DECLARE TABLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The DECLARE TABLE statement describes the characteristics of a database table.

The DECLARE TABLE statement has the following format:

```
EXEC SQL DECLARE [schema.]table_name TABLE           (column_name data_type [WITH NULL | NOT NULL [WITH DEFAULT]]          {, column_name data_type})
```

The DECLARE TABLE statement lists the columns and data types associated with a database table, for the purpose of program documentation. The DECLARE TABLE statement is a comment statement inside a variable declaration section and is not an executable statement. You cannot use host language variables in this statement.

The dclgen utility includes a DECLARE TABLE statement in the file it generates while creating a structure corresponding to a database table.

The embedded SQL preprocessor does not generate any code for the DECLARE TABLE statement. Therefore, in a language that does not allow empty control blocks (for example, COBOL, which does not allow empty IF blocks), the DECLARE TABLE statement must not be the only statement in the block.

#### Permissions

This statement is available to all users.

#### DECLARE TABLE Example

The following is a DECLARE TABLE statement example for a database table:

```
EXEC SQL DECLARE employee TABLE       (eno    INTEGER2 NOT NULL,       ename   CHAR(20) NOT NULL,       age     INTEGER1,       job     INTEGER2,       sal     FLOAT4,       dept    INTEGER2 NOT NULL);
```
