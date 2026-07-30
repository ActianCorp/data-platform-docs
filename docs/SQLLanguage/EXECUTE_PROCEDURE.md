---
title: "EXECUTE PROCEDURE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "EXECUTE_PROCEDURE.htm"
canonical_id: "actian-data-platform-execute-procedure"
---

## EXECUTE PROCEDURE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The EXECUTE PROCEDURE statement invokes a database procedure.

Database procedures can be executed from interactive SQL CLI, an embedded SQL program, or from another database procedure.

This statement can be executed dynamically or non-dynamically. When executing a database procedure, you typically provide values for the formal parameters specified in the definition of the procedure.

If an EXECUTE PROCEDURE statement includes a RESULT ROW clause, it can only be executed non-dynamically.

#### Syntax

The EXECUTE PROCEDURE statement has the following formats:

Non-dynamic version:

```
[EXEC SQL] EXECUTE PROCEDURE [schema.]proc_name              [([param_name=]param_spec {,[param_name=]param_spec})] |              [(parm = SESSION.global temporary table_name)]              [RESULT ROW (variable [:indicator_var]                                         {, variable[:indicator_var]})]              [INTO return_status]              [EXEC SQL BEGIN;program code;              EXEC SQL END;]
```

Dynamic version:

```
[EXEC SQL] EXECUTE PROCEDURE [schema.]proc_name              [USING [DESCRIPTOR] descriptor_name]              [INTO return_status]
```

**proc_name**

:   Specifies the name of the procedure, using a literal or a host string variable.

**global temporary table_name**

:   Is the name of a global temporary table already declared in the session in which the execute procedure is issued; it must be preceded by the SESSION qualifier.

**param_name=**

:   Is the name of the parameter. If using positional parameters, the parameter name is optional. See param_spec next.

**param_spec**

:   Is a literal value, a host language variable containing the value to be passed (**:**hostvar), or a host language variable passed by reference (BYREF(:host_variable)).

:   If using positional parameters (see [Positional Parameters Sample Syntax](../SQLLanguage/Positional_Parameters_Sample_Syntax.md)), each value must correspond to its matching ordinal location in the list of declared parameters.

!!! note "Note"

    Both positional and named parameters can be in a single parameter list, but all positional parameters must precede the first named parameter.
