---
title: "CONNECT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CONNECT.htm"
canonical_id: "actian-data-platform-connect"
---

## CONNECT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The CONNECT statement connects the application to a database and, optionally, to a distributed transaction.

This statement has the following format:

```
EXEC SQL CONNECT dbname              [AS connection_name]              [SESSION session_number]              [IDENTIFIED BY username]              [DBMS_PASSWORD = dbms_password]              [OPTIONS = flag {, flag}]              [WITH HIGHDXID = value, LOWDXID = value]
```

**dbname**

:   Specifies the database to which the session connects. Dbnamecan be a quoted or unquoted string literal or a host string variable. If the name includes any name extensions (such as a system or node name), string literals must be quoted.

**AS connection_name**

:   Specifies an alphanumeric identifier to be associated with the session. The connection name must be a string of up to 128 characters that identifies the session. If the AS connection_name clause and the SESSION clause are omitted, the default connection name is the specified database name.

:   Connection_name must be specified using a quoted string literal or a host language variable.

**SESSION session_number**

:   Specifies a numeric identifier to be associated with the session. The session number must be a positive integer literal or variable, and must be unique among existing session numbers in the application.

**IDENTIFIED BY username**

:   Specifies the user identifier under which this session runs. Username can be specified using a quoted or unquoted string literal or string variable.

**DBMS_PASSWORD=dbms_password**

:   Specifies the valid password either as string constant or a string program variable. This parameter allows the application to specify the password at connection time if required.

**OPTIONS=flag**

:   Specifies runtime options for the connection. Valid flags are those accepted by the sql command. Flags specific to the SQL CLI are not valid. The maximum number of flags is 12.

:   Common flags are:

-uusername

:   Specifies the effective user for the session.

-Ggroupid

:   Specifies a group identifier.

-Rroleid

:   Specifies a role identifier for the session. If the role ID has a password, use the format:

```
'-Rroleid/password '
```

+user[=username[,password]]

:   Passes username and password as the DBMS_authentication user and password. If +user is specified, the database name must not include [user,password] syntax. If username is omitted, the name of the logged-in OS user is used. If no password is specified, the user is prompted to enter a password. The syntax ‑user[=username[,password]] is also valid.

:   The flags can be specified using quoted or unquoted character string literals or string variables.

**value**

:   Highdxid specifies the high-order 4 bytes of a distributed transaction ID. Lowdxid specifies the low-order 4 bytes of a distributed transaction ID. These options are used for two-phase commit of distributed transactions.

CONNECT Example

Connect to a remote database called inventory. Authenticate as user fred. Prompt for fred’s password:

```
EXEC SQL CONNECT -USER=fred @MYLAPTOP,II::inventory;
```
