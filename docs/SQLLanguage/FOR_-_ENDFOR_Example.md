---
title: "FOR - ENDFOR Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "FOR_-_ENDFOR_Example.htm"
canonical_id: "actian-data-platform-for-endfor-example"
---

## FOR - ENDFOR Example

The following database procedure, avgsal_by_dept, returns rows containing the department name, average salary in the department, and count of employees in the department. Any unexpected error from the SELECT statement terminates the loop:

```
create procedure avgsal_by_dept       result row (char(15), float, int) asdeclare       deptname char(15);       avgsal   float;       empcount int;       err      int;begin       err = 0;       for select d.dept, avg(e.salary), count(*) into :deptname, :avgsal, :empcount       from department d, employee e        where e.deptid = d.deptid       group by d.deptid do       if iierrornumber > 0 then       err = 1;       endloop;       endif;       return row(:deptname, :avgsal, :empcount);       endfor;return :err;end”
```
