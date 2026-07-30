---
title: "ENDSELECT Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ENDSELECT_Example.htm"
canonical_id: "actian-data-platform-endselect-example"
---

## ENDSELECT Example

Break out of a select loop on a data loading error:

```
exec sql select ename, eno into :ename, :eno         from employee;exec sql begin;        load ename, eno into data set;        if error then        print 'Error loading ', ename, eno;        exec sql endselect;        end ifexec sql end;/* endselect transfers control to here */
```
