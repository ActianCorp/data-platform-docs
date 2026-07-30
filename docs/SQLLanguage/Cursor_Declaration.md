---
title: "Cursor Declaration"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Cursor_Declaration.htm"
canonical_id: "actian-data-platform-cursor-declaration"
---

## Cursor Declaration

Before using a cursor in an application, the cursor must be declared. The syntax for declaring a cursor is:

```
EXEC SQL DECLARE cursor_name CURSOR FOR
```

```
     select_statement;
```

The DECLARE CURSOR statement assigns a name to the cursor and associates the cursor with a SELECT statement to be used to retrieve data. A cursor is always associated with a SELECT statement. The select is executed when the cursor is opened. The cursor_name can be specified using a string literal or a host language string variable. The cursor name cannot exceed 32 bytes and can be assigned dynamically. For more information, see [Summary of Cursor Positioning](../SQLLanguage/Summary_of_Cursor_Positioning.md).
