---
title: "DESCRIBE INPUT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DESCRIBE_INPUT.htm"
canonical_id: "actian-data-platform-describe-input"
---

## DESCRIBE INPUT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The DESCRIBE INPUT statement returns information about the input parameter markers of a prepared statement. (Input parameter markers are denoted by "?" in the prepared statement.)

When there is a direct correspondence to a table column, such as positional mapping or direct comparison, the type of the table column is returned. Otherwise, a best guess of the type based on local context (such as the nearest resolvable operand) is returned.

!!! note "Note"

    Best-guess types are typically returned as nullable. If no type guess is possible because of lack of context, a zero (illegal) type is returned, but the DESCRIBE INPUT operation succeeds.

Syntax

The DESCRIBE INPUT statement has the following format:

```
EXEC SQL DESCRIBE INPUT statement_name
```

```
    USING [SQL] DESCRIPTOR :descriptor_name
```

```
    [WITHOUT NESTING]
```

**statement_name**

:   Specifies a valid prepared statement. Specify the statement_name using a string literal or a host language string variable. If the statement is prepared but has no input parameters, the DESCRIBE INPUT succeeds and returns zero for the returned SQLDA's sqld field.

**descriptor_name**

:   Identifies the name of the receiving descriptor area, formatted as an SQLDA. The descriptor name can be SQLDA or any other valid object name defined by the program when the structure is allocated. Because the SQLDA is not declared in a declaration section, the preprocessor does not verify that descriptor_name represents an SQLDA structure. If descriptor_name does not represent an SQLDA structure, undefined errors occur at runtime.

**WITHOUT NESTING**

:   This optional noise phrase is included for Standards conformance. It has no effect on the operation of the statement.

The DESCRIBE INPUT statement cannot be issued until after the program allocates the SQLDA and sets the value of the SQLDA’s sqln field to the number of elements in the SQLDA’s sqlvar array. The results of the DESCRIBE INPUT statement are complete and valid only if the number of the statement parameter markers is less than or equal to the number of allocated sqlvar elements.
