---
title: "DROP DBEVENT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_DBEVENT.htm"
canonical_id: "actian-data-platform-drop-dbevent"
---

## DROP DBEVENT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP DBEVENT statement drops the specified database event.

#### Syntax

The DROP DBEVENT statement has the following format:

```
[EXEC SQL] DROP DBEVENT [schema.]event_name;
```

## Permissions

You must be the owner of a database event. If applications are currently registered to receive the database event, the registrations are not dropped. If the database event was raised prior to being dropped, the database event notifications remain queued, and applications can receive them using the GET DBEVENT statement.

## Related Statements

[CREATE DBEVENT](../SQLLanguage/CREATE_DBEVENT.md)

[GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md)

[RAISE DBEVENT](../SQLLanguage/RAISE_DBEVENT.md)

[REGISTER DBEVENT](../SQLLanguage/REGISTER_DBEVENT.md)

[REMOVE DBEVENT](../SQLLanguage/REMOVE_DBEVENT.md)

## DROP DBEVENT Example

Delete the drill_hot dbevent:

```
DROP DBEVENT drill_hot;
```
