---
title: "INQUIRE_SQL"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "INQUIRE_SQL.htm"
canonical_id: "actian-data-platform-inquire-sql"
---

## INQUIRE_SQL

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The INQUIRE_SQL statement provides an application program with a variety of runtime information.

#### Syntax

The INQUIRE_SQL statement has the following format:

```
EXEC SQL INQUIRE_SQL (:variable = object {, variable = object});
```

**variable**

:   Specifies the name of a program variable.

**object**

:   Specifies a valid INQUIRE_SQL object name, as follows:

| Object | Data Type | Description |
| --- | --- | --- |
| dbeventname | Character | The name of the event (assigned using the CREATE DBEVENT statement). The receiving variable must be large enough for the full event name; if the receiving variable is too small, the event name is truncated to fit. |
| dbeventowner | Character | The creator of the event. |
| dbeventdatabase | Character | The database in which the event was raised. |
| dbeventtime | Date | The date and time at which the event was raised. |
| dbeventtext | Character | The text (if any) specified as the event_text parameter when the event was raised. The receiving value must be a 256-character string; if the receiving variable is too small, the text is truncated to fit. |
| dbmserror | Integer | Returns the number of the error caused by the last query. This number corresponds to the value of sqlerrd(1), the first element of the sqlerrd array in the SQLCA. To specify whether a local or generic error is returned, use the SET_SQL(ERRORTYPE) statement. |
| column_name | Character | Valid only in a data handler routine that retrieves data (with a SELECT or FETCH statement); returns the name of the column for which the data handler was invoked. The receiving variable must be a minimum of 32 bytes; if the host language uses null-terminated strings, an additional byte is required. |
| columntype | Integer | Valid only in a data handler routine that retrieves data (with a SELECT or FETCH statement); returns an integer indicating the data type of the column for which the data handler was invoked. |
| connection_name | Character | Returns the connection name for the current session. |
| connection_target | Character | Returns the node and database to which the current session is connected; for example, 'bignode::mydatabase'. |
| endquery | Integer | Returns 1 if the previous fetch statement was issued after the last row of the cursor, 0 if the last fetch statement returned a valid row. This is identical to the NOT FOUND condition (value 100) of the SQLCA variable sqlcode, which can be checked after a fetch statement is issued. If endquery returns '1', the variables assigned values from the fetch are left unchanged. |
| errorno | Integer | Returns the error number of the last query as a positive integer. The error number is cleared before each embedded SQL statement. ERRORNO is meaningful only immediately after the statement in question. This error number is the same as the positive value returned in the SQLCA variable sqlcode, except in two cases:A single query generates multiple different errors, in which case the sqlcode identifies the first error number, and the ERRORNO object identifies the last error.After switching sessions. In this case, sqlcode reflects the results of the last statement executed before switching sessions, while ERRORNO reflects the results of the last statement executed in the current session.If a statement executes with no errors or if a positive number is returned in sqlcode (for example, +100 to indicate no rows affected), the error number is set to 0. |
| errortext | Character | Returns the error text of the last query. The error text is only valid immediately after the database statement in question. The error text that is returned is the complete error message of the last error. This message can have been truncated when it was deposited into the SQLCA variable sqlerrm. The message includes the error number and a trailing end-of-line character. A character string result variable of size 256 must be sufficient to retrieve all error messages. If the result variable is shorter than the error message, the message is truncated. If there is no error message, a blank message is returned. |
| errortype | Character | Returns 'genericerror' if generic errors are returned to ERRORNO and sqlcode, or 'dbmserror' if local warehouse errors are returned to ERRORNO and sqlcode. |
| messagenumber | Integer | Returns the number of the last message statement executed inside a database procedure. If there was no message statement, a zero is returned. The message number is defined by the database procedure programmer. |
| messagetext | Character | Returns the message text of the last message statement executed inside a database procedure. If there is no text, a blank is returned. If the result variable is shorter than the message text, the message is truncated. The message text is defined by the database procedure programmer. |
| object_key | Character | Returns the logical object key added by the last INSERT statement, or -1 (in the indicator variable) if no logical key was assigned. |
| prefetchrows | Integer | Returns the number of rows Actian Data Platform buffers when fetching data using readonly cursors. This value is reset every time a readonly cursor is opened. If your application is using this feature, be sure to set the value before opening a readonly cursor. |
| programquit | Integer | Returns 1 if the programquit option is enabled (using SET_SQL(PROGRAMQUIT). If programquit is enabled, the following errors cause embedded SQL applications to terminate:•Issuing a query when not connected to a database•Failure of Actian Data Platform•Failure of communications services•Returns 0 if applications continue after encountering such errors. |
| querytext | Character | Returns the text of the last query issued; valid only if this feature is enabled. To enable or disable the saving of query text, use the SET_SQL(SAVEQUERY=1\|0) statement.A maximum of 1024 characters is returned; if the query is longer, it is truncated to 1024 characters. If the receiving variable is smaller than the query text being returned, the text is truncated to fit.If a null indicator variable is specified with the receiving host language variable, the indicator variable is set to -1 if query text cannot be returned, 0 if query text is returned successfully. Query text cannot be returned if (1) savequery is disabled, (2) no query has been issued in the current session, or (3) the INQUIRE_SQL statement is issued outside of a connected session. |
| rowcount | Integer | Returns the number of rows affected by the last query. The following statements affect rows: INSERT, DELETE, UPDATE, SELECT, FETCH, MODIFY, CREATE INDEX, and CREATE TABLE AS SELECT. If any of these statements runs successfully, the value returned for rowcount is the same as the value of the SQLCA variable sqlerrd(3). If these statements generate errors, or if statements other than these are run, the value of ROWCOUNT is negative and the value of sqlerrd(3) is zero.Exception: for MODIFY TO TRUNCATED, INQUIRE_SQL(ROWCOUNT) always returns 0. |
| savequery | Integer | Returns 1 if query text saving is enabled, 0 if disabled. |
| session | Integer | Returns the session identifier of the current database session. If the application is not using multiple sessions or there is no current session, session 0 is returned. |
| table_key | Character | Returns the logical table key added by the last INSERT statement, or -1 (in the indicator variable) if no logical key was assigned. |
| transaction | Integer | Returns a value of 1 if there is a transaction open. |

All character values are returned in lower case. If no event is queued, an empty or blank string is returned (depending on your host language conventions).

#### Description

The INQUIRE_SQL statement enables an embedded SQL program to retrieve a variety of runtime information, such as:

- Information about the last executed database statement
- The message number and text from a message statement executed by a database procedure

- Status information, such as the current session ID, the type of error (local or generic) being returned to the application, and whether a transaction is currently open
- Information about the last event removed from the event queue

- The value of the last single logical key inserted into the database by the application
- Provides an application program with a variety of runtime information.

The INQUIRE_SQL statement does not execute queries; the information INQUIRE_SQL returns to the program reflects the results of the last query that was executed. For this reason, the INQUIRE_SQL statement must be issued after the database statement about which information is desired, and before another database statement is executed (and resets the values returned by INQUIRE_SQL).

To retrieve error or message information about database procedure statements, issue the INQUIRE_SQL statement inside an error or message handler called by the WHENEVER SQLERROR or WHENEVER SQLMESSAGE statement.

Some of the information returned by INQUIRE_SQL is also available in the SQLCA. For example, the error number returned by the object errorno is also available in the SQLCA sqlcode field.

Similarly, when an error occurs, the error text can be retrieved using INQUIRE_SQL with the ERRORTEXT object or it can be retrieved from the SQLCA sqlerrm variable. ERRORTEXT provides the complete text of the error message, which is often truncated in sqlerrm.

This statement must be terminated according to the rules of your host language.

#### Permissions

This statement is available to all users.

## INQUIRE_SQL Example

Execute some database statements, and handle errors by displaying the message and terminating the transaction.

```
exec sql whenever sqlerror goto err_handle;exec sql select name, sal    into :name, :sal    from employee    where eno = :eno;if name = 'Badman' then    exec sql delete from employee         where eno = :eno;else if name = 'Goodman' then    exec sql update employee set sal = sal + 3000         where eno = :eno;end if;exec sql commit;...err_handle:exec sql whenever sqlerror continue;exec sql inquire_sql (:err_msg = errortext);print 'Avalanche error: ', sqlca.sqlcode;print err_msg;exec sql rollback;
```
