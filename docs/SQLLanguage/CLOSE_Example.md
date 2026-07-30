---
title: "CLOSE Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CLOSE_Example.htm"
canonical_id: "actian-data-platform-close-example"
---

## CLOSE Example

The following example illustrates cursor processing from cursor declaration to closing:

```
EXEC SQL DECLARE c1 CURSOR FOR SELECT ename, jobidFROM employeeWHERE jobid = 1000;...EXEC OPEN c1;LOOP UNTIL NO MORE ROWS;EXEC SQL FETCH c1      INTO :name, :jobid;PRINT NAME, jobid;END LOOP;EXEC SQL CLOSE c1;
```
