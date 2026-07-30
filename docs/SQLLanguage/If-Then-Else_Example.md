---
title: "If-Then-Else Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "If-Then-Else_Example.htm"
canonical_id: "actian-data-platform-if-then-else-example"
---

## If-Then-Else Example

The following IF statement performs a delete or an insert and checks to make sure the statement succeeded:

```
IF (id > 0) AND (id <= maxid) THEN       DELETE FROM emp WHERE id = :id;       IF iierrornumber > 0 THEN              message 'Error deleting specified row';              return 1;       ELSEIF iirowcount = 0 THEN              message 'Specified row does not exist';              return 2;       ENDIF;ELSEIF (id < maxid) THEN       INSERT INTO emp VALUES (:name, :id, :status);       IF iierrornumber > 0 THEN              message 'Error inserting specified row';              return 3;       ENDIF;ELSE	message 'Invalid row specification';	return 4;ENDIF;
```
