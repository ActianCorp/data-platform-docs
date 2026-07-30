---
title: "DESCRIBE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DESCRIBE.htm"
canonical_id: "actian-data-platform-describe"
---

## DESCRIBE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The DESCRIBE statement retrieves information about the result of a prepared dynamic SQL statement.

The DESCRIBE statement has the following format:

```
EXEC SQL DESCRIBE statement_name  INTO|USING [:]descriptor_name [USING NAMES];
```

**statement_name**

:   Specifies a valid prepared statement. Specify the statement_name using a string literal or a host language string variable. If an error occurs when the specified statement is prepared, the statement is not valid. If a [COMMIT](../SQLLanguage/COMMIT.md) or [ROLLBACK](../SQLLanguage/ROLLBACK.md) statement is executed after the statement is prepared and before it is executed, the statement is discarded and cannot be described or executed.

**descriptor name**

:   Identifies an SQLDA. The descriptor name can be SQLDA or any other valid object name defined by the program when the structure is allocated. Because the SQLDA is not declared in a declaration section, the preprocessor does not verify that descriptor_name represents an SQLDA structure. If descriptor_name does not represent an SQLDA structure, undefined errors occur at runtime.

:   Descriptor_name can be preceded by a colon (:).

**USING NAMES**

:   Returns the names of result columns in the descriptor if the described statement is a SELECT statement. (The USING NAMES clause is optional and has no effect on the results of the DESCRIBE statement.)

#### Description

The DESCRIBE statement returns the data type, length, and name of the result columns of the prepared select. If the prepared statement is not a SELECT, describe returns a zero in the SQLDA sqld field.

The DESCRIBE statement cannot be issued until after the program allocates the SQLDA and sets the value of the SQLDA's sqln field to the number of elements in the SQLDA’s sqlvar array. The results of the DESCRIBE statement are complete and valid only if the number of the result columns (from the SELECT) is less than or equal to the number of allocated sqlvar elements. (The maximum number of result columns that can be returned is 1024.)

The [PREPARE](../SQLLanguage/PREPARE.md) statement can also be used with the INTO clause to retrieve the same descriptive information provided by describe.

#### Usage in OpenAPI, ODBC, JDBC, .NET

The OpenAPI, ODBC, JDBC, and .NET interfaces cannot send a Describe statement to the DBMS. Each has its own mechanism for obtaining this information from the database. For example, JDBC uses ResultSet.getMetaData and OpenAPI uses IIapi_getDescriptor().

#### Permissions

This statement is available to all users.

#### Related Statements

[DESCRIBE INPUT](../SQLLanguage/DESCRIBE_INPUT.md)[](../SQLLanguage/DESCRIBE_INPUT.md)

[EXECUTE](../SQLLanguage/EXECUTE.md)[](../SQLLanguage/EXECUTE.md)

[PREPARE](../SQLLanguage/PREPARE.md)[](../SQLLanguage/PREPARE.md)
