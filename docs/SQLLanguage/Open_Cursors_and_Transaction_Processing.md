---
title: "Open Cursors and Transaction Processing"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Open_Cursors_and_Transaction_Processing.htm"
canonical_id: "actian-data-platform-open-cursors-and-transaction-processing"
---

## Open Cursors and Transaction Processing

Cursors affect transaction processing as follows:

- Cursors cannot remain open across transactions. The COMMIT statement closes all open cursors, even if a CLOSE cursor statement was not issued.
- If an error occurs while a cursor is open, the Actian Data Platform can roll back the entire transaction and close the cursor.
