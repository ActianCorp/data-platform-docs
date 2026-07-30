---
title: "Session Switching"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Session_Switching.htm"
canonical_id: "actian-data-platform-session-switching"
---

## Session Switching

To switch sessions using a numeric session identifier, use the SET_SQL(SESSION) statement. To switch sessions using the connection name, use the SET CONNECTION statement.

To determine the numeric session identifier for the current session, use the INQUIRE_SQL(SESSION) statement. To determine the connection name for the current session, use the INQUIRE_SQL(CONNECTION_NAME) statement.

Applications can switch sessions in the following circumstances:

- Within a transaction
- While cursors are open

- Within SQL block statements, such as a select loop

    The program code for the nested session must be inside a host language subroutine. If it is not, the SQL preprocessor issues an error.

- Within subroutines called by a WHENEVER statement
- Within the following types of routines:

    - Error handlers

    - Message handlers

    - Database event handlers

!!! note "Note"

    Sessions cannot be switched inside a database procedure.

After an application switches sessions, the error information obtained from the SQLCA or the INQUIRE_SQL statement is not updated until an SQL statement has completed in the new session.
