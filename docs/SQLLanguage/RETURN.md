---
title: "RETURN"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RETURN.htm"
canonical_id: "actian-data-platform-return"
---

## RETURN

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc, UDF

The RETURN statement terminates a currently executing database procedure or user-defined function and gives control back to the calling application, and, optionally, returns a value. The RETURN statement can only be used inside a database procedure or a user-defined function. (The calling application resumes execution at the statement following [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md), in the case of a database procedure.)

The RETURN statement has the following format:

```
RETURN [return_status];
```

The optional return_status returns a value to the calling application when the RETURN statement executes. Return_status must be a non-null integer constant, variable, or parameter whose data type is comparable with the data type of the variable to which its value is assigned. If the return_status is not specified or if a return statement is not executed, the procedure returns 0 to the calling application.

The INTO clause of the EXECUTE PROCEDURE statement allows the calling application to retrieve the return_status once the procedure has finished executing.

#### Permissions

This statement is available to all users.
