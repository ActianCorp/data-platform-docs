---
title: "Closing Cursors"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Closing_Cursors.htm"
canonical_id: "actian-data-platform-closing-cursors"
---

## Closing Cursors

To close a cursor, issue the CLOSE cursor statement:

```
EXEC SQL CLOSE cursor_name;
```

After the cursor is closed, no more processing can be performed with it unless another OPEN statement is issued. The same cursor can be opened and closed any number of times in a single program. A cursor must be closed before it can be reopened.
