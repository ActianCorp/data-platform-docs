---
title: "Open a Cursor"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Open_a_Cursor.htm"
canonical_id: "actian-data-platform-open-a-cursor"
---

## Open a Cursor

To open a cursor, use the OPEN statement:

```
EXEC SQL OPEN cursor_name [FOR READONLY];
```

Opening a cursor executes the associated SELECT statement. The rows returned by the SELECT statement are stored in a temporary result set. The cursor is positioned before the first row in the result table.

!!! note "Note"

    If a cursor is closed and reopened, the cursor is repositioned to the beginning of the result table, and does not resume the position it had before it was closed.
