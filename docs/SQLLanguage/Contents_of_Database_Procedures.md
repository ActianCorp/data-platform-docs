---
title: "Contents of Database Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Contents_of_Database_Procedures.htm"
canonical_id: "actian-data-platform-contents-of-database-procedures"
---

## Contents of Database Procedures

A database procedure can include the following entities:

- Local variable declarations
- Data manipulation statements such as SELECT or INSERT

- Control flow statements such as IF, FOR, and WHILE
- Status statements, such as MESSAGE, RETURN, RETURN ROW, and RAISE ERROR

The Actian Data Platform resolves all references to database objects in a database procedure at the time the procedure is created. For this reason, all referenced objects must exist at the time the procedure is created. If, at the time it is created, a procedure refers to a DBA-owned table, the procedure always uses that table, even if a user that owns a table with the same name executes the procedure.

!!! note "Note"

    Database local variables must be preceded by a colon when used in data manipulation statements.
