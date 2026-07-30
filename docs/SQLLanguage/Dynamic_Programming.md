---
title: "Dynamic Programming"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Dynamic_Programming.htm"
canonical_id: "actian-data-platform-dynamic-programming"
---

## Dynamic Programming

Dynamic programming allows your applications to specify program elements (including queries, SQL statements, and form names) at runtime. In applications where table or column names are not known until runtime, or where queries must be based on the runtime environment of the application, hard-coded SQL statements are not sufficient.

To support applications such as these, use dynamic SQL. Using dynamic SQL, you can:

- Execute a statement that is stored in a buffer (using the EXECUTE IMMEDIATE statement).
- Encode a statement stored in a buffer and execute it multiple times (using the PREPARE and EXECUTE statements).

- Obtain information about a table at runtime (using the PREPARE and DESCRIBE statements).

!!! note "Note"

    Dynamic FRS allows an application to transfer data between the form and the database using information specified at runtime.
