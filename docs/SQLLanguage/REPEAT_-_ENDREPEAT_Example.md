---
title: "REPEAT - ENDREPEAT Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "REPEAT_-_ENDREPEAT_Example.htm"
canonical_id: "actian-data-platform-repeat-endrepeat-example"
---

## REPEAT - ENDREPEAT Example

In the following REPEAT - ENDREPEAT statement example, this database procedure, delete_n_rows, accepts as input a base number and a number of rows. The specified rows are deleted from the table “tab,” starting from the base number. Because this is a repeat loop, one row will always be deleted. If it is possible for no rows to be identified, the pre-testing WHILE - ENDWHILE loop should be used instead. If an error occurs, the loop terminates:

```
CREATE PROCEDURE delete_n_rows
```

```
      (base INTEGER, n INTEGER) AS
```

```
DECLARE
```

```
      limit INTEGER;
```

```
      err INTEGER NOT NULL;
```

```
BEGIN
```

```
      limit = base + n;
```

```
      err = 0;
```

```
      REPEAT
```

```
            DELETE FROM tab WHERE val = :base;
```

```
            IF iierrornumber > 0 THEN
```

```
                  err = 1;
```

```
                  ENDLOOP;
```

```
            ENDIF;
```

```
            base = base + 1;
```

```
      UNTIL (base >= limit) ENDREPEAT;
```

```
      RETURN :err;
```

```
END
```
