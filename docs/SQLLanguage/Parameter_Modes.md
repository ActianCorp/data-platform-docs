---
title: "Parameter Modes"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Parameter_Modes.htm"
canonical_id: "actian-data-platform-parameter-modes"
---

## Parameter Modes

By default, parameters to a database procedure are INPUT only. Though the parameter value may be updated in the body of the procedure, the changed value is not passed back to the calling application, rule, or procedure. The BYREF designation used in a calling application can be used to force the return of the modified parameter value. For more information on BYREF, see [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md).

For database procedures called from other database procedures or by the firing of a rule, the INOUT and OUT modes can be coded in a parameter declaration to return the modified value of the parameter back to the caller of the procedure. This allows results to be passed from one procedure to another and column values to be changed by BEFORE rules defined on a particular table.
