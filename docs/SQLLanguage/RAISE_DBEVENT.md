---
title: "RAISE DBEVENT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RAISE_DBEVENT.htm"
canonical_id: "actian-data-platform-raise-dbevent"
---

## RAISE DBEVENT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, DBProc, OpenAPI, ODBC, JDBC, .NET

The RAISE DBEVENT statement enables an application to notify other applications of its status.

#### Syntax

The RAISE DBEVENT statement has the following format:

```
[EXEC SQL] RAISE DBEVENT [schema.]event_name [event_text]
```

```
               [WITH [NO]SHARE];
```

**event_name**

:   Specifies an existing database event name.

#### Description

The RAISE DBEVENT statement enables a session to communicate status information to other sessions that are registered to receive event_name.

If schema is omitted, Actian Data Platform checks first for the specified database event owned by the effective user of the session. If the current effective user does not own the database event, Actian Data Platform seeks the specified database event in the database events owned by the DBA.

Use the optional event_text parameter to pass a (maximum 256 character) string to receiving applications; to obtain the text, receiving applications must use the [INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)(DBEVENTTEXT) statement.

To restrict database event notification to the session that raised the database event, specify WITH NOSHARE. To notify all registered sessions, specify WITH SHARE or omit this clause. The default is SHARE.

If a database event is raised from within a transaction and the transaction is subsequently rolled back, the database event notification is not rolled back.

#### Permissions

To raise a database event you do not own, specify the schema parameter and have RAISE privilege for the database event. To assign RAISE privilege to another user, use the GRANT statement.

#### Related Statements

[CREATE DBEVENT](../SQLLanguage/CREATE_DBEVENT.md)

[GET DBEVENT](../SQLLanguage/GET_DBEVENT.md)

[INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)

[REGISTER DBEVENT](../SQLLanguage/REGISTER_DBEVENT.md)

[REMOVE DBEVENT](../SQLLanguage/REMOVE_DBEVENT.md)
