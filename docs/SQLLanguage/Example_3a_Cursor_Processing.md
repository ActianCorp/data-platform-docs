---
title: "Example: Cursor Processing"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Example_3a_Cursor_Processing.htm"
canonical_id: "actian-data-platform-example-3a-cursor-processing"
---

## Example: Cursor Processing

The following is an example of cursor processing:

```
exec sql include sqlca;exec sql begin declare section;     name          character_string(15);     salary        float;exec sql end declare section;exec sql whenever sqlerror stop;exec sql connect personnel;exec sql declare c1 cursor for          select ename, sal          from employee;exec sql open c1;exec sql whenever not found goto closec1;loop while more rows/* The WHENEVER NOT FOUND statement causes     the loop to be broken as soon as a row     is not fetched. */exec sql fetch c1 into :name, :salary;print name, salary;end loop;closec1:exec sql close c1;exec sql disconnect;
```
