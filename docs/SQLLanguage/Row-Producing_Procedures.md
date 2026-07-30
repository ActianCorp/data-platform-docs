---
title: "Row-Producing Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Row-Producing_Procedures.htm"
canonical_id: "actian-data-platform-row-producing-procedures"
---

## Row-Producing Procedures

A row-producing procedure is a database procedure that can return zero or more rows to its caller.

### Format of a Row-Producing Procedure

The RESULT ROW clause in the procedure definition defines the format of a row-producing procedure. The RETURN ROW statement specifies the value returned in each “column” of a result row. The value can be a local variable or parameter of the procedure, or any expression involving constants, local variables, and parameters. The local variables must contain data retrieved in the procedure by a SELECT statement. Multiple result rows must be returned to the caller using the For-loop that retrieves data from a SELECT statement.

### How a Row-Producing Procedure Is Called

Row-producing procedures can only be called directly from an embedded SQL host program (not using dynamic SQL, a terminal monitor, or by nesting a call in another database procedure). The host program, however, must include a Begin/End block to process the rows as they are returned from the procedure. This block functions much the same as the “select block” used with embedded SELECT statements.

A row-producing procedure cannot execute another procedure.

### Row-Producing Procedure Example

```
CREATE PROCEDURE emp_sales_rank
```

```
   RESULT ROW (INT, INT, MONEY)
```

```
AS
```

```
DECLARE
```

```
   sales_tot   MONEY;
```

```
   empid       INT;
```

```
   sales_rank  INT;
```

```
BEGIN
```

```
   sales_rank = 0;
```

```
   FOR
```

```
        SELECT e.empid,
```

```
               sum(s.sales) as sales_sum
```

```
        INTO   :empid,
```

```
               :sales_tot
```

```
        FROM    employee e,
```

```
                sales s
```

```
        WHERE   e.job   = 'sales'
```

```
        AND     e.empid = s.empid
```

```
        GROUP BY e.empid
```

```
        ORDER BY sales_sum DESC
```

```
        DO
```

```
                sales_rank = sales_rank + 1;
```

```
                RETURN ROW (:sales_rank, :empid, :tot_sales);
```

```
   ENDFOR;
```

```
END;
```

```

```

```

```

```

```

```
EXEC SQL BEGIN DECLARE;
```

```
     int       empid;
```

```
     int       sales_rank;
```

```
     float     sales_tot;
```

```
     ...
```

```
EXEC SQL END DECLARE;
```

```
     ...
```

```
EXEC SQL EXECUTE PROCEDURE emp_sales_rank
```

```
         RESULT ROW (:sales_rank, :empid, :tot_sales);
```

```
EXEC SQL BEGIN;
```

```
     ...
```

```
EXEC SQL END;
```

```
     ...
```
