---
title: "RETURN ROW Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RETURN_ROW_Example.htm"
canonical_id: "actian-data-platform-return-row-example"
---

## RETURN ROW Example

The following is a RETURN ROW example:

```
CREATE PROCEDURE rowproc ... AS    ... RESULT ROW (CHAR(8), INT, FLOAT) ...  BEGIN    ...    FOR SELECT department, COUNT(*), AVG(salary) INTO :a, :b, :c FROM personnel         GROUP BY deptname DO    ...   RETURN ROW (:a, :b, :c);    ENDFOR;     ...  END;
```
