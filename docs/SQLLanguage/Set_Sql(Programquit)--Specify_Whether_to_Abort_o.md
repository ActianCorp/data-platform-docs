---
title: "Set_Sql(Programquit)--Specify Whether to Abort on Error"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Set_Sql(Programquit)--Specify_Whether_to_Abort_o.htm"
canonical_id: "actian-data-platform-set-sqlprogramquit-specify-whether-to-abort-o"
---

## Set_Sql(Programquit)--Specify Whether to Abort on Error

The SET_SQL(PROGRAMQUIT) statement specifies how an embedded SQL application handles the following types of errors:

- Attempt to execute a query when not connected to a database
- DBMS server failure

- Communications service failure

By default, when these types of errors occur, the DBMS issues an error but lets the program continue. To force an application to terminate when one of these errors occur, issue the following SET_SQL statement:

```
exec sql set_sql (programquit = 1);
```

If an application terminates as the result of one of the previously listed errors, the DBMS issues an error and rolls back open transactions and disconnects all open sessions. To disable terminating and restore the default behavior, specify PROGRAMQUIT = 0.

Errors affected by the PROGRAMQUIT setting belong to the generic error class GE_COMM_ERROR, which is returned to errorno as 37000, and to sqlcode (in the SQLCA) as -37000. An application can check for these errors and, when detected, must disconnect from the current session. After disconnecting from the current session, the application can attempt another connection, switch to another session (if using multiple sessions) or perform clean-up operations and quit.

PROGRAMQUIT can also be specified by using II_EMBED_SET.

To determine the current setting for this behavior, use the INQUIRE_SQL statement:

```
exec sql inquire_sql (int_variable = programquit);
```

This statement returns a 0 if PROGRAMQUIT is not set (execution continues despite these errors) or 1 if PROGRAMQUIT is set (the application exits after these errors).
