---
title: "DECLARE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DECLARE.htm"
canonical_id: "actian-data-platform-declare"
---

## DECLARE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The DECLARE statement describes a list of local variables for use in a database procedure.

This statement is used only in a database procedure definition to declare a list of local variables for use in the procedure. If this statement is to be used, place it before the BEGIN clause of the database procedure definition.

Nullable variables are initialized to null. Non-nullable variables are initialized to the default value according to data type: character data types are initialized to blank, and numeric data types are initialized to zero. Any non-nullable variables declared without an explicit default value are initialized to the default value.

The following table lists the effects of the null and default specifications on the default value of a column.

| Nullability Option | Default Option | Results |
| --- | --- | --- |
| WITH NULL | (none specified) | The variable can be null; default value is null. |
| NOT NULL | (none specified) | The default is 0 or blank (according to data type). |
| (none specified) | WITH DEFAULT | Not valid without a NULL clause. |
| (none specified) | NOT DEFAULT | Not valid without a NULL clause. |
| WITH NULL | WITH DEFAULT | Not valid. |
| WITH NULL | NOT DEFAULT | Not valid. |
| NOT NULL | WITH DEFAULT | The variable defaults to 0 or blank, according to its data type. |
| NOT NULL | NOT DEFAULT | The variable defaults to 0 or blank, according to its data type. |

#### Syntax

The DECLARE statement has the following format:

```
   DECLARE    var_name {, var_name} [=] var_type              [NOT NULL [WITH | NOT DEFAULT] | WITH NULL];              {var_name {, var_name} [=] var_type              [NOT NULL [WITH | NOT DEFAULT] | WITH NULL];}
```

**var_name**

:   Specifies the name of the local variable. A variable name must be unique within the procedure; it cannot match the name of any other procedure variable or parameter.

**var_type**

:   Is the data type of the variable. A local variable can be any data type.

#### Permissions

This statement is available to all users.

#### Related Statements

CREATE PROCEDURE

PREPARE
