---
title: "Multiple Sessions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Multiple_Sessions.htm"
canonical_id: "actian-data-platform-multiple-sessions"
---

## Multiple Sessions

To open a session, issue the CONNECT statement. To identify individual sessions in a multiple-session application, assign a connection name or numeric session identifier when issuing the CONNECT statement.

You can create multiple sessions that connect to the same database. For each connection, specify different runtime options, including the effective user.

The current session is established when an application connects to a database (by issuing the CONNECT statement) or switches sessions (using the SET CONNECTION or SET_SQL(SESSION) statements). If an error occurs when a program attempts to connect to a database, there is no current session in effect. Before the program can issue any queries, it must establish the current session by (successfully) connecting to a database or switching to a previously established session.
