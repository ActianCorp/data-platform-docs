---
title: "Error Handling for Embedded SELECT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Error_Handling_for_Embedded_SELECT.htm"
canonical_id: "actian-data-platform-error-handling-for-embedded-select"
---

## Error Handling for Embedded SELECT

If the SELECT statement retrieves no rows, the SQLCA variable sqlcode is set to 100. The number of rows returned from the database is in the SQLCA variable sqlerrd(3). In a select loop, if the ENDSELECT statement was issued, sqlerrd(3) contains the number of rows retrieved before ENDSELECT was issued.
