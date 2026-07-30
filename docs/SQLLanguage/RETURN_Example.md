---
title: "RETURN Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RETURN_Example.htm"
canonical_id: "actian-data-platform-return-example"
---

## RETURN Example

The following database procedure example, emp_sales_rank, returns rows containing the employee ID, total sales, and rank of sales amongst current salesmen:

```
CREATE PROCEDURE emp_sales_rank    RESULT ROW (INT, INT, MONEY) ASDECLARE    sales_tot  MONEY;    empid      INT;    sales_rank INT;BEGIN    sales_rank = 0;    FOR SELECT e.empid, sum(s.sales) AS sales_sum INTO :empid, :sales_tot        FROM employee e, sales s         WHERE e.job = 'sales' AND e.empid = s.empid         GROUP BY e.empid ORDER BY sales_sum DO      sales_rank = sales_rank + 1;      RETURN ROW(:sales_rank, :empid, :tot_sales);    ENDFOR;END
```
