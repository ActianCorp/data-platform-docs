---
title: "DROP FUNCTION"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_FUNCTION.htm"
canonical_id: "actian-data-platform-drop-function"
---

## DROP FUNCTION

The DROP FUNCTION statement removes a user-defined function (UDF) from the database. The function is removed from Actian Data Platform as appropriate.

If the function is overloaded by another UDF, the instance of UDF to be dropped must be indicated by specifying the parameters and function name; otherwise, if unambiguous, use the unqualified DROP FUNCTION func_name syntax.

The DROP FUNCTION statement has the following format:

```
DROP FUNCTION [IF EXISTS] func_name
```

```
    [([IN] param_name [=] param_type [WITH | NOT DEFAULT] [WITH | NOT NULL]
```

```
    {, [IN] param_name [=] param_type [WITH | NOT DEFAULT] [WITH | NOT NULL]})]
```

```
    [RETURN (result_type)] [LANGUAGE language]
```

**IF EXISTS**

:   Suppresses error reporting for the specified object if the object does not exist and the user matches the schema.

**func_name**

:   Defines the name of the function to be removed.

**param_name**

:   Specifies the name of a function parameter, which is required to distinguish the instance of the UDF when the UDF is overloaded. The WITH | NOT NULL clause can be part of the specification.

**param_type**

:   Specifies the data type of the associated parameter. The WITH | NOT NULL clause can be part of the specification.

**RETURN result_type**

:   The data type of the RETURN statement. The RETURN clause is not mandatory because the data type is not used to distinguish the instance of the UDF to be dropped.

**language_name**

:   The implementation language. Valid values are: PYTHON, JS, SQL.

#### Permissions

You must be the owner of the function.

#### Related Statements

[CREATE FUNCTION](../SQLLanguage/CREATE_FUNCTION.md)
