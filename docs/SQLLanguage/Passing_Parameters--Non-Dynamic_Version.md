---
title: "Passing Parameters--Non-Dynamic Version"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Passing_Parameters--Non-Dynamic_Version.htm"
canonical_id: "actian-data-platform-passing-parameters-non-dynamic-version"
---

## Passing Parameters--Non-Dynamic Version

In the non-dynamic version of the EXECUTE PROCEDURE statement, parameters can be passed byvalue or by reference.

**By value** - To pass a parameter by value, use this syntax:

```
param_name = value
```

When passing parameters by value, the database procedure receives a copy of the value. Values can be specified using:

- Numeric or string literals
- SQL constants (such as TODAY or USER)

- Host language variables
- Arithmetic expressions

The data type of the value assigned to a parameter must be compatible with the data type of the corresponding parameter in the procedure definition. Specify date data using quoted character string values, and money using character strings or numbers. If the data types are not compatible, an error is issued and the procedure not executed.

**By reference** – To pass a parameter by reference, use this syntax:

```
param_name = BYREF(:host_variable)
```

When passing parameters by reference, the database procedure can change the contents of the variable. Any changes made by the database procedure are visible to the calling program. Parameters cannot be passed by reference in interactive SQL.

Each param_name must match one of the parameter names in the parameter list of the definition of the procedure.Param_name must be a valid object name, and can be specified using a quoted or unquoted string or a host language variable.
