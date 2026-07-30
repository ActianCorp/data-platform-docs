---
title: "REGISTER DBEVENT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "REGISTER_DBEVENT.htm"
canonical_id: "actian-data-platform-register-dbevent"
---

## REGISTER DBEVENT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The REGISTER DBEVENT statement enables a session to specify the database events it intends to receive.

A session receives only the database events for which it has registered. To remove a registration, use the REMOVE statement. After registering for a database event, the session receives the database event using the GET DBEVENT statement.

A session can register for events owned by the session's effective user or for which register privilege has been granted. If an attempt is made to register for a nonexistent event, for an event for which register privilege has not been granted, or twice for the same event, Actian Data Platform issues an error.

If the schema parameter is omitted, Actian Data Platform first checks the events owned by the current user. If the specified event is not found, Actian Data Platform checks the events owned by the DBA.

If the REGISTER DBEVENT statement is issued from within a transaction that is subsequently rolled back, the registration remains in effect.

#### Syntax

The REGISTER DBEVENT statement has the following format:

```
[EXEC SQL] REGISTER DBEVENT [schema.]event_name;
```

#### Permissions

To register for an event you do not own, you must specify the schema parameter, and must have REGISTER privilege for the database event. To assign REGISTER privilege, use the GRANT statement.

## Related Statements

[CREATE DBEVENT](../SQLLanguage/CREATE_DBEVENT.md)

[GET DBEVENT](../SQLLanguage/GET_DBEVENT.md)

[INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)

[RAISE DBEVENT](../SQLLanguage/RAISE_DBEVENT.md)

[REMOVE DBEVENT](../SQLLanguage/REMOVE_DBEVENT.md)
