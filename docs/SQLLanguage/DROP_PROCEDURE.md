---
title: "DROP PROCEDURE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_PROCEDURE.htm"
canonical_id: "actian-data-platform-drop-procedure"
---

## DROP PROCEDURE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP PROCEDURE statement removes a database procedure definition from the database. Sessions that are executing the procedure can complete before the procedure's query plan is removed from memory.

If a procedure that is executed from another procedure is removed, the calling procedure is retained but marked dormant, and cannot be executed until the called procedure is restored.

**Notes:**

- DROP PROCEDURE cannot be prepared.
- Dropping a table procedure will cause dependent views to be dropped. To avoid the loss of dependent views when redefining a database procedure, use the syntax CREATE OR REPLACE PROCEDURE.

The DROP PROCEDURE statement has the following format:

```
[EXEC SQL] DROP PROCEDURE [IF EXISTS] proc_name;
```

**IF EXISTS**

:   Suppresses error reporting for the specified object if the object does not exist and the user matches the schema.

**proc_name**

:   Specifies the name of the procedure to be removed.

#### Embedded Usage

In an embedded DROP PROCEDURE statement, a host language variable cannot be used to represent proc_name.

#### Permissions

You must be the owner of the database procedure.

#### Related Statements

[CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md)[](../SQLLanguage/CREATE_PROCEDURE.md)

[EXECUTE](../SQLLanguage/EXECUTE.md)[](../SQLLanguage/EXECUTE.md)

[GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md)[](../SQLLanguage/GRANT_(privilege).md)

## DROP PROCEDURE Example

Remove the procedure named salupdt:

```
DROP PROCEDURE salupdt;
```
