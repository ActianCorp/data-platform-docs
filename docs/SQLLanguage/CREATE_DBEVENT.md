---
title: "CREATE DBEVENT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_DBEVENT.htm"
canonical_id: "actian-data-platform-create-dbevent"
---

## CREATE DBEVENT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE DBEVENT statement defines a database event.

## Syntax

The CREATE DBEVENT statement has the following format:

```
[EXEC SQL] CREATE DBEVENT [schema.]event_name
```

**event_name**

:   Identifies the event. The event_name must be a valid object name.

## Description

The CREATE DBEVENT statement creates the specified database event. Database events enable an application to pass status information to other applications.

Database events can be registered or raised by any session, provided that the owner has granted the required permission (raise or register) to the session’s user, group, or role identifier, or to public. Only the user, group, or role that created a database event can drop that database event.

## Usage in OpenAPI, ODBC, JDBC, .NET

In ODBC, JDBC, and .NET, events can be created in query statements, but other interfaces must be used to catch the event being created.

## Permissions

This statement is available to all users.

## Related Statements

DROP DBEVENT

GRANT (privilege)

RAISE DBEVENT

REGISTER DBEVENT

REMOVE DBEVENT
