---
title: "DISCONNECT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DISCONNECT.htm"
canonical_id: "actian-data-platform-disconnect"
---

## DISCONNECT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The DISCONNECT statement terminates a session connected to a database. The disconnect statement implicitly closes any open cursors, and commits any pending updates.

The DISCONNECT statement has the following format:

```
EXEC SQL DISCONNECT [CURRENT] | connection_name |[SESSION session_identifier | ALL];
```

**CURRENT**

:   Terminates the current session.

**SESSION session_identifier**

:   Terminates the specified session, which is other than the current session in a multi-session application. To determine the numeric session identifier for the current session, use the INQUIRE_SQL(:session_id = SESSION) statement.

**connection_name**

:   Terminates the specified connection, which is other than the current session in a multi-session application. To determine the connection name for the current session, use the INQUIRE_SQL(:connection_name=connection_name) statement.

**ALL**

:   Disconnects all open sessions.

If an invalid session is specified, Actian Data Platform issues an error and does not disconnect the session.

#### Usage in OpenAPI, ODBC, JDBC, .NET

In OpenAPI, ODBC, JDBC, and .NET, Disconnect is supported through interface calls. For example, JDBC uses Connection.close() and OpenAPI uses IIapi_disconnect().

#### Permissions

This statement is available to all users.

#### Locking

When the DISCONNECT statement is issued, all locks held by the session are dropped.

#### Related Statements

[CONNECT](../SQLLanguage/CONNECT.md)

[SET](../SQLLanguage/SET.md)[](../SQLLanguage/SET.md)
