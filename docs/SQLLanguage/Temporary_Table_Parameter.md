---
title: "Temporary Table Parameter"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Temporary_Table_Parameter.htm"
canonical_id: "actian-data-platform-temporary-table-parameter"
---

## Temporary Table Parameter

The temporary table must have been declared prior to procedure execution. However, it does not have to be populated (because the procedure itself can place rows into the table). Upon invocation of the procedure, Actian Data Platform binds the executing procedure unambiguously to the global temporary table instance of the invoking session. This permits any number of users, each with their own temporary table instance, to execute the procedure concurrently.

Example:

```
execute procedure gttproc (parm1 = session.mygtt1);
```

This statement invokes the procedure gttproc, passing the global temporary table session.mygtt1 as its parameter. (The name used for the actual parameter is inconsequential.)

### Limitations of Temporary Table Parameter

When a global temporary table is passed as a procedure parameter, it must be the only parameter in both the calling and called parameter list (that is, in both the EXECUTE PROCEDURE and CREATE PROCEDURE statements).

The columns of the temporary table declaration and the elements in the set of parameter definition must exactly match in degree (number), name, type, and nullability. A check is performed during the execute procedure compile to assure that this constraint is met.

Temporary table parameters cannot be used in nested procedure calls. Global temporary tables cannot be declared within a procedure; hence no locally created temporary table can be passed in an EXECUTE PROCEDURE statement nested in another procedure. Likewise, a set of parameter cannot be specified in a nested EXECUTE PROCEDURE statement.
