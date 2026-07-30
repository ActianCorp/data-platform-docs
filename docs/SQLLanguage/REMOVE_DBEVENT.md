---
title: "REMOVE DBEVENT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "REMOVE_DBEVENT.htm"
canonical_id: "actian-data-platform-remove-dbevent"
---

## REMOVE DBEVENT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The REMOVE DBEVENT statement removes a database event for which an application has previously registered.

The REMOVE DBEVENT statement has the following format:

```
[EXEC SQL] REMOVE DBEVENT [schema.]event_name;
```

#### Description

The REMOVE DBEVENT statement specifies that an application no longer intends to receive the specified database event.

If the database event has been raised before the application removes the registration, the database event remains queued to the application and is received when the application issues the [GET DBEVENT](../SQLLanguage/GET_DBEVENT.md) statement.

If the REMOVE DBEVENT statement is issued from within a transaction that is subsequently rolled back, the REMOVE DBEVENT statement is not rolled back. If an application issues the REMOVE DBEVENT statement for a database event for which it has not registered, Actian Data Platform returns an error.

#### Permissions

This statement is available to all users.

#### Related Statements

[REGISTER DBEVENT](../SQLLanguage/REGISTER_DBEVENT.md)

[CREATE DBEVENT](../SQLLanguage/CREATE_DBEVENT.md)

[GET DBEVENT](../SQLLanguage/GET_DBEVENT.md)

[INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)

[RAISE DBEVENT](../SQLLanguage/RAISE_DBEVENT.md)
