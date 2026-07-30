---
title: "GET DBEVENT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "GET_DBEVENT.htm"
canonical_id: "actian-data-platform-get-dbevent"
---

## GET DBEVENT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI

The GET DBEVENT statement gets an event previously defined by the [CREATE DBEVENT](../SQLLanguage/CREATE_DBEVENT.md) statement.

The GET DBEVENT statement receives database events for which an application is registered. The GET DBEVENT statement returns the next database event from the database event queue. To obtain database event information, issue the [INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md) statement.

#### Syntax

The GET DBEVENT statement has the following format:

```
EXEC SQL GET DBEVENT [WITH NOWAIT | WAIT [= wait_value]];
```

**WITH NOWAIT**

:   (Default) Checks the queue and returns immediately.

**WITH WAIT[=wait_value]**

:   Waits indefinitely for the next database event to arrive. If with wait = wait_valueis specified, GET DBEVENT returns when a database event arrives or whenwait_value seconds have passed, whichever occurs first. If GET DBEVENT times out before a database event arrives, no database event is returned.

:   Wait_value can be specified using an integer constant or integer host language variable.

:   The WITH WAIT option cannot be used within a select loop or a database procedure message processing routine called as the result of the WHENEVER SQLMESSAGE condition.

#### Permissions

This statement is available to all users.

#### Related Statements

[CREATE DBEVENT](../SQLLanguage/CREATE_DBEVENT.md)

[DROP DBEVENT](../SQLLanguage/DROP_DBEVENT.md)

[RAISE DBEVENT](../SQLLanguage/RAISE_DBEVENT.md)

[REGISTER DBEVENT](../SQLLanguage/REGISTER_DBEVENT.md)

[REMOVE DBEVENT](../SQLLanguage/REMOVE_DBEVENT.md)
