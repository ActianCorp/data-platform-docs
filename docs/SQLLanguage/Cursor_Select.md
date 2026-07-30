---
title: "Cursor Select"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Cursor_Select.htm"
canonical_id: "actian-data-platform-cursor-select"
---

## Cursor Select

The cursor SELECT statement is specified as part of a DECLARE CURSOR statement. Within the DECLARE CURSOR statement, the SELECT statement is not preceded by EXEC SQL. The cursor SELECT statement specifies the data to be retrieved by the cursor. When executed, the DECLARE CURSOR statement does not perform the retrieval; the retrieval occurs when the cursor is opened.

The cursor select can return multiple rows, because the cursor provides the means to process and update retrieved rows one at a time. The correlation of expressions to host language variables takes place with the FETCH statement, so the cursor select does not include an INTO clause. The rules for the remaining clauses are the same as in the non-cursor select.

More information:

[Data Manipulation with Cursors](../SQLLanguage/Data_Manipulation_with_Cursors.md)

[DECLARE CURSOR](../SQLLanguage/DECLARE_CURSOR.md)
