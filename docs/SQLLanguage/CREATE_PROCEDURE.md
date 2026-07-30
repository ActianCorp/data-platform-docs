---
title: "CREATE PROCEDURE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_PROCEDURE.htm"
canonical_id: "actian-data-platform-create-procedure"
---

## CREATE PROCEDURE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE PROCEDURE statement creates a database procedure.

The CREATE PROCEDURE statement has the following format:

```
[EXEC SQL] [CREATE | CREATE OR REPLACE] PROCEDURE [schema.]proc_name
```

```
            [[(set_param_name [=] SET OF]
```

```
            ([param_mode] param_name [=] param_type
```

```
                    [WITH | NOT DEFAULT] [WITH | NOT NULL]
```

```
            {, [param_mode] param_name [=] param_type
```

```
                    [WITH | NOT DEFAULT] [WITH | NOT NULL]})[)]]
```

```
            [RESULT ROW [result_row_name] ([result_column_name]
```

```
            (result_type [WITH | NOT DEFAULT] [WITH | NOT NULL]
```

```
            {,  result_type [WITH | NOT DEFAULT] [WITH | NOT NULL]}) =|AS
```

```
            [declare_section]
```

```
BEGIN
```

```
            statement {; statement}[;]
```

```
END
```

**CREATE OR REPLACE**

:   Recreates the procedure if it already exists, and preserves the object ID and any existing dependent objects.

**proc name**

:   Defines the name of the procedure. This must be a valid object name.

**set_param_name**

:   Defines the name of the SET OF parameter. This must be a valid object name. The SET OF parameters are referenced like base tables in the body of the procedure.

**param_name**

:   Defines the name of a procedure parameter. This must be a valid object name. Parameters can be passed by value or by reference.

**param_mode**

:   Assigns one of the following modes to the procedure parameter:

IN

:   Declares the parameter as an input only parameter.

OUT

:   Declares the parameter as an output only parameter.

INOUT

:   Declares the parameter as one that passes a value into the procedure and returns it, possibly modified, to the calling program.

**param_type**

:   Specifies the data type of the associated parameter. The data type can be any legal SQL data type, and the WITH | NOT NULL clause can be part of the specification.

**declare_section**

:   A list of local variables for use in the procedure. For more information, see [DECLARE](../SQLLanguage/DECLARE.md).

**statement**

:   Local variable assignments and any of the statements listed in the text of the CREATE PROCEDURE description.

**result_row_name**

:   Assigns a name to the result row.

!!! note "Note"

    A result row name is required when result columns are to be named. A result row can be unnamed if none of the columns are to be named.

**result_column_name**

:   Assigns a name to a result column. This name can then be used in a query.

**result_type**

:   The data type of the associated entry in a RETURN ROW statement. The data type can be any legal SQL data type, and the WITH | NOT NULL clause can be part of the specification. For more information, see [RETURN ROW](../SQLLanguage/RETURN_ROW.md).

!!! note "Note"

    If II_DECIMAL is set to comma, you must follow any comma required in SQL syntax (such as a list of table columns or SQL functions with several parameters) by a space. For example:

```
SELECT col1, IFNULL(col2, 0), LEFT(col4, 22) FROM version;
```
