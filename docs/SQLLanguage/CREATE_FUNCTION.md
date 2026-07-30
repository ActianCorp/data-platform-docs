---
title: "CREATE FUNCTION"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_FUNCTION.htm"
canonical_id: "actian-data-platform-create-function"
---

## CREATE FUNCTION

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE FUNCTION statement creates a user-defined function (UDF).

!!! note "Note"

    SQL and JavaScript UDFs are a development release. Please work with Actian Support before using such UDFs in a production environment.

    The CREATE FUNCTION statement has the following format:

```
[EXEC SQL] [CREATE | CREATE OR REPLACE] FUNCTION func_name
```

```
   [([IN] param_name [=] param_type [WITH | NOT DEFAULT] [WITH | NOT NULL]
```

```
   {, [IN] param_name [=] param_type [WITH | NOT DEFAULT] [WITH | NOT NULL]})]
```

```
   RETURN (result_type) = | AS
```

```
[
```

```
   [declare_section] BEGIN statement {; statement}[;] RETURN expression[;] END
```

```

```

```
   |
```

```
   LANGUAGE language_name language_specific_attribute = value
```

```
    {,lang_specific_attribute = value}
```

```
]
```

**CREATE OR REPLACE**

:   Recreates the function if it already exists and preserves the object ID and any existing dependent objects.

!!! note "Note"

    You can create SQL UDFs only with the [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md), except for simple functions that require no DECLARE section for local variables.

**func_name**

:   Defines the name of the function. This must be a valid object name. Function names are case insensitive and cannot be delimited.

**IN**

:   Declares the parameter as an input only parameter. IN is the only supported mode.

**param_name**

:   Defines the name of a function parameter. This must be a valid object name.

**param_type**

:   Specifies the data type of the associated parameter. The data type can be any legal SQL data type, and the WITH | NOT NULL clause can be part of the specification.

**result_type**

:   Specifies the data type of the intended [RETURN](../SQLLanguage/RETURN.md) statement. The data type can be any legal SQL data type.

**declare_section**

:   (SQL language only) Describes a list of local variables for use in the function. For more information, see [DECLARE](../SQLLanguage/DECLARE.md).

**statement**

:   (SQL language only) Defines local variable assignments, simple SELECT assign statements, and RETURN statement. Non-scalar SELECT expressions and control flow instructions like FOR or WHILE cannot be used.

**LANGUAGE=language_name**

:   Specifies the implementation language. Valid values are:

**JAVASCRIPT**(or **JS**) – JavaScript

**PYTHON** (or **PY**) – Python

**SQL** – SQL

:   To define an SQL UDF, use the DECLARE-BEGIN-END SQL syntax.

**lang_specific_attribute=value**

:   An attribute defining a characteristic from the table. Valid values are:

| Attribute | Language Support | Value |
| --- | --- | --- |
| COMMUTATIVE | All | TRUE or FALSEWhether the dyadic can be called with its parameters swapped. For example: ADD(a,b)<=>ADD(b,a) |
| INGEXECINGRESEXEC | All | TRUE or FALSEWhether the function can be executed on Ingres data |
| INJECTIVE | All | TRUE or FALSEWhether the function preserves one-to-one mapping. |
| SOURCE | JavaScript,Python | A text string specifying the body of the function |
| VARFI | All | TRUE or FALSEWhether the attribute must be evaluated every time and not be constant folded |
| VWEXECX100EXEC | All | TRUE or FALSEWhether the function can be executed on X100 data |

#### Description

The CREATE FUNCTION statement creates a user-defined function (UDF). The function is executed in the chosen language by the Actian Data Platform.

Function names can be overloaded and are differentiated by the data types of the parameters. For choosing which overloaded function instance to execute, data type size is generally ignored. For creating functions, however, the size of integers and floating-point numbers and the scale and precision of decimals are treated as distinct. For all other data types, size is ignored. Thus, functions fn(int) and fn(smallint) are treated as distinct but fn(varchar(10)) and fn(varchar(20)) are treated as the same.

#### Parameter Modes

Parameters to a user-defined function are INPUT only. Though the parameter value may be updated in the body of the function, the changed value is not passed back to the calling application, rule, or procedure.

#### Nullability and Default Values for Parameters

User-defined functions can be called from embedded SQL applications or from interactive SQL. The caller supplies values for function parameters. The WITH DEFAULT, NOT DEFAULT, WITH NULL, and NOT NULL clauses can be used to specify whether parameters have default values and whether they are nullable.

These clauses have the following meanings for function parameters:

**WITH DEFAULT**

:   The caller does not have to specify a value for the parameter. If the parameter is nullable, its default value is null. If the parameter is not nullable, its default value is 0 (for numeric data types) or blanks (for character data types).

**NOT DEFAULT**

:   The caller must specify a value for the parameter. If no value is specified, Actian Data Platform issues an error.

**WITH NULL**

:   The parameter can be null.

**NOT NULL**

:   The parameter cannot be null.

The combined effects of these clauses are as follows:

| Parameter | Description |
| --- | --- |
| WITH NULL | The parameter can be null. If no value is provided, Actian Data Platform passes a null. |
| NOT NULL WITH DEFAULT | The parameter does not accept nulls. If no value is provided, Actian Data Platform passes 0 for numeric and money columns, or an empty string for character and date columns. |
| NOT NULL NOT DEFAULT or NOT NULL | The parameter is mandatory and does not accept nulls. |
| WITH NULL WITH DEFAULT | Not allowed. |
| WITH NULL NOT DEFAULT | Not allowed. |
| WITH DEFAULT | Not allowed without NOT NULL clause. |
| NOT DEFAULT | Not allowed without NOT NULL clause. |

#### Permissions

To use CREATE FUNCTION, you must have permission to access the tables and views specified in queries issued by the function.

#### Embedded Usage

The embedded CREATE FUNCTION statement is identical to its interactive version, with the following exceptions and additions for the SQL language:

- Braces { } cannot be used in place of the BEGIN and END clauses.
- All statements in the function must be separated by semicolons. The statement terminator after the final END clause follows the syntax of the host language.

- The CREATE FUNCTION statement cannot contain any references to host language variables.
- The rules for the continuation of statements over multiple lines follow the embedded SQL host language rules. String literals, continued over multiple lines, also follow the host language rules.

- Comments in a procedure body follow the comment rules of the host language.

The SQL syntax of the CREATE FUNCTION statement is validated at runtime, not by the preprocessor.

#### Related Statements

DROP FUNCTION

DECLARE
