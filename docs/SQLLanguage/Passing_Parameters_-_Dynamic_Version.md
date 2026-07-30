---
title: "Passing Parameters - Dynamic Version"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Passing_Parameters_-_Dynamic_Version.htm"
canonical_id: "actian-data-platform-passing-parameters-dynamic-version"
---

## Passing Parameters - Dynamic Version

In the dynamic version of the EXECUTE PROCEDURE statement, the descriptor_name specified in the USING clause identifies an SQL Descriptor Area (SQLDA), a host language structure allocated at runtime.

Prior to issuing the EXECUTE PROCEDURE statement, the program must place the parameter names in the sqlname fields of the SQLDA sqlvar elements and the values assigned to the parameters must be placed in the host language variables pointed to by the sqldata fields. When the statement is executed, the USING clause ensures those parameter names and values to be used.

Parameter names and values follow the same rules for use and behavior when specified dynamically as those specified non-dynamically. For example, because positional referencing is not allowed when you issue the statement non-dynamically, when you use the dynamic version, any sqlvar element representing a parameter must have entries for both its sqlname and sqldata fields. Also, the names must match those in the definition of the procedure and the data types of the values must be compatible with the parameter to which they are assigned.

Any parameter in the definition of the procedure that is not assigned an explicit value when the procedure is executed is assigned a null or default value. If the parameter is not nullable and does not have a default, an error is issued.

For example, for the CREATE statement

```
create procedure p (i integer not null,        d date, c varchar(100)) as ...
```

the following associated EXECUTE PROCEDURE statement implicitly assigns a null to parameter d.

```
exec sql execute procedure p (i = 123,         c = 'String');
```

When executing a procedure dynamically, set the SQLDA sqld field to the number of parameters that you are passing to the procedure. The sqld value tells Actian Data Platform how many sqlvar elements the statement is using (how many parameters are specified). If the sqld element of the SQLDA is set to 0 when you dynamically execute a procedure, it indicates that no parameters are being specified, and if there are parameters in the formal definition of the procedure, these are assigned null or default values when the procedure executes. If the procedure parameter is not nullable and does not have a default, an error is issued.

A parameter cannot be specified in the EXECUTE PROCEDURE statement that was not specified in the [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md) statement.

Return_status is an integer variable that receives the return status from the procedure. If areturn_status is not specified in the database procedure, or the return statement is not executed in the procedure, 0 is returned to the calling application.

!!! note "Note"

    The INTO clause cannot be used in interactive SQL.

The statement must be terminated according to the rules of the host language.
