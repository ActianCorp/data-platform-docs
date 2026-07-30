---
title: "Readonly Cursors"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Readonly_Cursors.htm"
canonical_id: "actian-data-platform-readonly-cursors"
---

## Readonly Cursors

Readonly cursors specify that the data does not intend to be updated. Cursors on Actian Data Platform SELECT statements are always READONLY.

To improve performance, the Actian Data Platform pre-fetches (buffers) rows for readonly cursors. Use the SET_SQL(prefetchrows) statement to disable prefetching or to specify the number of rows to prefetch. To determine the number of rows that is prefetched for a readonly cursor, open the cursor, issue the INQUIRE_SQL(prefetchrows) statement.

By default the Actian Data Platform calculates the number of rows it can prefetch, taking into consideration the size of the row being fetched and the dimensions of internal buffers. If, using SET_SQL(prefetchrows), a value larger than the maximum number of rows the Actian Data Platform can prefetch is specified, prefetchrows is reset to its calculated maximum.
