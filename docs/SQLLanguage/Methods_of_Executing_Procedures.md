---
title: "Methods of Executing Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Methods_of_Executing_Procedures.htm"
canonical_id: "actian-data-platform-methods-of-executing-procedures"
---

## Methods of Executing Procedures

Database procedures can be executed in the following ways:

- By using the EXECUTE PROCEDURE statement in an embedded SQL application.

    This statement executes a specified procedure and passes parameter values to the procedure. To specify different parameter lists at runtime, use the dynamic version of the EXECUTE PROCEDURE statement. To execute a procedure owned by a user other than the effective user of the session, specify the procedure name using the schema.procedure_name syntax.

- From interactive SQL, from within another database procedure, or by using the dynamic SQL EXECUTE IMMEDIATE statement.

!!! note "Note"

    These methods cannot execute row-producing procedures.

    A procedure cannot be executed using the dynamic SQL PREPARE and EXECUTE statements.

- By using the OpenAPI IIapi_query() function.

For more information about executing a database procedure, see [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md).

All referenced objects must exist at the time the procedure is executed. Between the time of creation and the time of execution, objects such as tables and columns can be modified, reordered, or dropped and recreated without affecting the procedure definition. However, if an object is redefined in a way that invalidates the procedure definition, drop and recreate the procedure.
