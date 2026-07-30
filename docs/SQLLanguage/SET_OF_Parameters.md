---
title: "SET OF Parameters"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SET_OF_Parameters.htm"
canonical_id: "actian-data-platform-set-of-parameters"
---

## SET OF Parameters

A SET OF parameter is required when a global temporary table is being passed to the procedure. A SET OF parameter declaration consists of a SET OF parameter name and an accompanying elements list.

In the case of a procedure invoked by an [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md) statement with a GLOBAL TEMPORARY TABLE parameter, the SET OF elements correspond to the temporary table columns. If a global temporary table is used as an input parameter to a database procedure, no other parameters are allowed and the procedure cannot be row producing (syntax RESULT ROW). For more information, see [Temporary Table Parameter](../SQLLanguage/Temporary_Table_Parameter.md)[](../SQLLanguage/Temporary_Table_Parameter.md)under [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md).

In the case of a procedure invoked by a statement level rule, the SET OF element list consists of one entry for each actual parameter in the CREATE RULE EXECUTE PROCEDURE clause. The syntax of these entries is identical to that of normal (that is, non-SET OF) formal parameters. The type definitions must be compatible with (though not necessarily identical to) the corresponding actual parameters. The names must be the same, however, as this is how the equivalence between the actual parameters and the SET OF elements is determined.

Once a SET OF parameter is defined in a [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md) statement, it can be treated exactly like any base table or view from within the procedure. The SET OF elements are the columns of the table and the parameter name is the surrogate name of the table. The parameter name can be used as a table name in any SELECT, DELETE, UPDATE, or INSERT statement within the procedure.

For example, it can be used in an INSERT...SELECT... statement to return the multi-row result of a complex SELECT statement with a single procedure call, or it can be used in the FROM clause of an UPDATE to effect the update of many rows with a single procedure call.

For example:

```
CREATE PROCEDURE gttproc (gtt1 SET OF (coll INT, col2 FLOAT NOT NULL, col3 CHAR(8))) AS BEGIN....INSERT INTO TABLE SELECT * FROM gtt1;....END;
```

gtt1 is defined as a SET OF parameter to procedure gttproc and is used in the FROM clause of a SELECT statement in the body of the procedure.
