---
title: "EXECUTE PROCEDURE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "EXECUTE_PROCEDURE_Examples.htm"
canonical_id: "actian-data-platform-execute-procedure-examples"
---

## EXECUTE PROCEDURE Examples

The following EXECUTE PROCEDURE examples assume the following [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md) statement has been successfully executed:

```
EXEC SQL CREATE PROCEDURE p          (i INTEGER NOT NULL,          d DATE,          c VARCHAR(100)) AS ...
```

1. The following example uses a host language variable, a null constant, and an empty string.

```
EXEC SQL EXECUTE PROCEDURE p     (i=:ivar, d=null, c='')    INTO :retstat;
```

2. The following example assumes the c parameter is null and uses a null indicator for the d parameter.

```
EXEC SQL EXECUTE PROCEDURE p     (i=:ivar, d=:dvar:ind)    INTO :retstat;
```

3. The following example demonstrates the use of the WHENEVER statement for intercepting errors and messages from a database procedure.

```
EXEC SQL WHENEVER SQLERROR GOTO err_exit;EXEC SQL WHENEVER SQLMESSAGE CALL SQLPRINT;EXEC SQL EXECUTE PROCEDURE p INTO :retstat;...err_exit:EXEC SQL INQUIRE_SQL (:errbug = errortext);
```

4. The following example demonstrates a dynamically-executed EXECUTE PROCEDURE statement. The example creates and executes the dynamic equivalent of the following statement.

```
EXEC SQL EXECUTE PROCEDURE enter_person	(age = :i4_var, comment = :c100_var:indicator);
```

    **Dynamic version:**

```
EXEC SQL INCLUDE sqlda;allocate an SQLDA with 10 elements;sqlda.sqln = 10;sqlda.sqld = 2;/* 20-byte character for procedure name */proc_name = 'enter_person';/* 4-byte integer to put into parameter "age" */sqlda.sqlvar(1).sqltype = int;sqlda.sqlvar(1).sqllen = 4;sqlda.sqlvar(1).sqldata = address(i4_var)sqlda.sqlvar(1).sqlind = null;sqlda.sqlvar(1).sqlname ='age';/* 100-byte nullable character to put into the** parameter "comment" */sqlda.sqlvar(2).sqltype = char;sqlda.sqlvar(2).sqllen = 100;sqlda.sqlvar(2).sqldata = address(c100_var);sqlda.sqlvar(2).sqlind = address(indicator);sqlda.sqlvar(2).sqlname = 'comment';EXEC SQL EXECUTE PROCEDURE :proc_name    USING DESCRIPTOR sqlda;
```

5. Call a database procedure, passing parameters by reference. This enables the procedure to return the number of employees that received bonuses and the total amount of bonuses conferred.

```
EXEC SQL EXECUTE PROCEDURE grant_bonuses    (ecount = BYREF(:number_processed),      btotal = BYREF(:bonus_total));
```
