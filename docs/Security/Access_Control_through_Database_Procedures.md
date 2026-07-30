---
title: "Access Control through Database Procedures"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Access_Control_through_Database_Procedures.htm"
canonical_id: "actian-data-platform-access-control-through-database-procedures"
---

## Access Control through Database Procedures

Database procedures provide the DBA with greater control over database access.

The DBA can grant permission to execute a database procedure even if the user has no direct access to the underlying tables referenced in the procedure. With EXECUTE permissions, the DBA can give users limited, specific access to tables without needing to give the users full query grants (such as SELECT) on the tables. In this way, the DBA controls exactly what operations a user can perform on a database.

For example, both tables used in the previous example can be inaccessible to users except through the procedure. The DBA grants EXECUTE permission, as in the following example, to allow users in the acctg group to access the tables for this procedure only:

```
GRANT EXECUTE ON PROCEDURE move_emp TO acctg
```

When the procedure is invoked, the executing application passes a single integer parameter.

For example, the following statement calls the move_emp procedure for the employee ID 56742:

```
EXEC SQL EXECUTE PROCEDURE move_emp (id = 56742);
```
