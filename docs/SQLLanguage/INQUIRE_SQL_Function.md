---
title: "INQUIRE_SQL Function"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "INQUIRE_SQL_Function.htm"
canonical_id: "actian-data-platform-inquire-sql-function"
---

## INQUIRE_SQL Function

The INQUIRE_SQL function returns information about the status of the last SQL database statement issued by an application.

The INQUIRE_SQL function can provide the following information on the occurrence of an error:

- Return the error number and the complete error text.
- Retrieve the message number and text from a message statement that was executed inside a database procedure.

- Determine if your session is returning local or generic errors, if a transaction is open, or what session is currently active (useful in multiple-session applications).

The INQUIRE_SQL function does not return status information about forms statements. To obtain information about the results of forms statements, use the INQUIRE_FRS statement.

For a complete list and description of available status information, see [INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md).
