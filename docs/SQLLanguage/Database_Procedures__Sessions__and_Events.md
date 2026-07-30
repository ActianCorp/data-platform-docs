---
title: "Database Procedures, Sessions, and Events"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Database_Procedures__Sessions__and_Events.htm"
canonical_id: "actian-data-platform-database-procedures-sessions-and-events"
---

# Database Procedures, Sessions, and Events

## How Database Procedures Are Created, Invoked, and Executed

A database procedure is a named routine composed of SQL statements stored in a database.

Database procedures are created using the CREATE PROCEDURE statement and dropped using the DROP PROCEDURE statement.

Database procedures can be called or invoked in the following ways:

- From an embedded SQL program
- From interactive SQL

- From a 4GL program

A database procedure query execution plan is created at the time the procedure is created. If objects named in the procedure are modified in a way that invalidates the query execution plan, the Actian Data Platform recreates the query execution plan the next time the procedure is invoked.
