---
title: "Data Manipulation with Cursors"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Data_Manipulation_with_Cursors.htm"
canonical_id: "actian-data-platform-data-manipulation-with-cursors"
---

## Data Manipulation with Cursors

Cursors enable embedded SQL programs to process, one at a time, the result rows returned by a SELECT statement. After a cursor has been opened, it can be advanced through the result rows. When the cursor is positioned to a row, the data in the row can be transferred to host language variables and processed according to the requirements of the application. The row to which the cursor is positioned is referred to as the current row.

A typical cursor application uses SQL statements to perform the following steps:

1. Declare a cursor that selects a set of rows for processing.
2. Open the cursor, thereby selecting the data.

3. Fetch each row from the result set and move the data from the row into host language variables.
4. Close the cursor and terminate processing.

!!! note "Note"

    Actian Data Platform cursors operate as a single indivisible statement, and other queries cannot be issued while the cursor is open.
