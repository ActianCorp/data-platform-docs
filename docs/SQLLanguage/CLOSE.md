---
title: "CLOSE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CLOSE.htm"
canonical_id: "actian-data-platform-close"
---

## CLOSE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The CLOSE statement closes an open cursor.

The CLOSE statement has the following format:

```
EXEC SQL CLOSE cursor_name
```

**cursor_name**

:   Specifies the cursor name using a quoted or unquoted string literal or a host language string variable. If cursor_name is a reserved word, it must be specified in quotes.

The cursor_name must have been previously defined in your source file by a [DECLARE CURSOR](../SQLLanguage/DECLARE_CURSOR.md) statement. Once closed, the cursor cannot be used for further processing unless reopened with a second [OPEN](../SQLLanguage/OPEN.md) statement. A [COMMIT](../SQLLanguage/COMMIT.md), [ROLLBACK](../SQLLanguage/ROLLBACK.md), or [DISCONNECT](../SQLLanguage/DISCONNECT.md) statement closes all open cursors.

A string constant or host language variable can be used to specify the cursor name.

#### Embedded Usage

In an embedded [CLOSE](../SQLLanguage/CLOSE.md) statement, a string constant or host language variable can be used to specify the cursor name.

#### Usage in OpenAPI, ODBC, JDBC, .NET

In OpenAPI, ODBC, JDBC, and .NET, [CLOSE](../SQLLanguage/CLOSE.md) cannot be directly issued on a cursor name, but can take handles or objects that perform the same task.

#### Permissions

This statement is available to all users.

#### Locking

In the [CLOSE](../SQLLanguage/CLOSE.md) statement, closing a cursor does not release the locks held by the cursor. (The locks are released when the transaction is completed.)

#### Related Statements

[DECLARE CURSOR](../SQLLanguage/DECLARE_CURSOR.md)[](../SQLLanguage/DECLARE_CURSOR.md)

[FETCH](../SQLLanguage/FETCH.md)[](../SQLLanguage/FETCH.md)

[OPEN](../SQLLanguage/OPEN.md)[](../SQLLanguage/OPEN.md)
