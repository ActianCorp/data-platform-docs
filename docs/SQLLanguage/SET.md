---
title: "SET"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SET.htm"
canonical_id: "actian-data-platform-set"
---

## SET

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The SET statement specifies a runtime option for the current session. The selected option remains in effect until the session is terminated or the option is changed using another SET statement.

This statement has the following format:

```
SET [ACTUAL | ESTIMATED] MAXROW n
```

```
SET AUTOCOMMIT ON | OFF | READ
```

```
SET [NO]BATCH_COPY_OPTIM
```

```
SET [NO]CACHE_DYNAMIC
```

```
SET CONNECTION connection_name |NONE
```

```
SET DATE_FORMAT [value]
```

```
SET DECIMAL [value]
```

```
SET FLOAT_FORMAT 'format'
```

```
SET INSERTMODE DEFAULT | ROW | BULK
```

```
SET JOINOP NOTIMEOUT | TIMEOUT | TIMEOUT nnn
```

```
SET JOINOP TIMEOUTABORT nnn
```

```
SET JOINOP [NO]GREEDY
```

```
SET MAXROWSTEP n
```

```
SET MONEY_FORMAT [value]
```

```
SET MONEY_PREC [value]
```

```
SET [NO]OJFLATTEN
```

```
SET [NO]OPTIMIZEONLY
```

```
SET NOPARTITION_PARTS | PARTITION_PARTS n
```

```
SET NOPARTITION_SCHEME | PARTITION_SCHEME {AUTO | NONE | HASH}
```

```
SET [NO]PRINTQRY
```

```
SET [NO]QEP [CONCISE | SEGMENTED]
```

```
SET RANDOM_SEED [value]
```

```
SET RESULT_STRUCTURE VECTORWISE | VECTORWISE_ROW | HEAP
```

```
SET [NO]REUSE
```

```
SET [NO]SCHEMA
```

```
SET SESSION AUTHORIZATION username | USER | CURRENT_USER
```

```
                   SESSION_USER | SYSTEM_USER | INITIAL_USER
```

```
SET SESSION [NO]CACHE_DYNAMIC
```

```
SET SESSION READ ONLY | READ WRITESET SESSION WITH
```

```
             DESCRIPTION | NODESCRIPTION
```

```
             ON_ERROR = ROLLBACK STATEMENT | TRANSACTION
```

```
             ON_USER_ERROR = ROLLBACK TRANSACTION | NOROLLBACK
```

```
               | DESCRIPTION ='session_description'
```

```
               | NODESCRIPTION
```

```
               | PRIORITY = INITIAL | MINIMUM | MAXIMUM | priority
```

```
SET [NO]STATISTICS tablename
```

```
SET TRANSACTION READ ONLY | READ WRITE
```

```
SET [NO]UNION_FLATTENING
```

## SET Options

**SET [ACTUAL | ESTIMATED] MAXROW n**

:   Limits the number of actual or estimated rows returned in a query to n. ESTIMATED is the default and does not need to be specified.

**SET AUTOCOMMIT ON|OFF|READ**

:   SET AUTOCOMMIT ON treats each query as a single-query transaction.

:   SET AUTOCOMMIT OFF, the default, means an explicit COMMIT or ROLLBACK statement or terminating the session is required to terminate a transaction.

:   SET AUTOCOMMIT READ autocommits a transaction that was started in read-only mode.

:   Transactions are started read only when no transaction is currently started, and:

    - The SET [SESSION or TRANSACTION] READ ONLY statement is in effect, or:

    - The AUTOCOMMIT state is ON or READ, and one of the following query types is issued:

        - –A SELECT statement (including SELECT loop in Embedded SQL)

        - –A COPY INTO statement

        - –A CREATE or DROP STATISTICS statement*

        - –An OPEN cursor statement, whether FOR READONLY or not, if the cursor query references Actian Data Platform tables

:   It is possible to treat Actian Data Platform cursors as read-only statements because Actian Data Platform cursors are not updatable and cannot nest; they are similar to Ingres SELECT loops.

:   Since many ODBC and JDBC programs use cursors for querying, and since autocommit ON is the default for ODBC and JDBC, then SET AUTOCOMMIT READ will alleviate some out-of-memory conditions caused by uncommitted transactions; a long SELECT cursor query will run read-only for its entirety without having to wait for the commit.

:   If AUTOCOMMIT READ is in effect and an updating statement is issued, a multi-statement transaction will be started. You must explicitly end such a transaction with COMMIT or ROLLBACK.

:   SET AUTOCOMMIT READ can be helpful for Actian Data Platform query sessions. In Actian Data Platform, all transactions must be committed as soon as possible to prevent unnecessary memory usage.

:   The SET AUTOCOMMIT statement cannot be issued in an open transaction. In ODBC and JDBC, autocommit is ON by default.

**SET [NO]BATCH_COPY_OPTIM**

:   Enables or disables copy optimization when executing batched inserts. This statement overrides the default set on Actian Data Platform BATCH_COPY_OPTIM configuration parameter.

**SET [NO]CACHE_DYNAMIC**

:   Enables or disables the caching of query plans for cursors defined with dynamic SELECT statements. It overrides the server level setting defined by the CACHE_DYNAMIC configuration parameter. To check the current setting, use SELECT DBMSINFO ('CACHE_DYNAMIC'). The SET [NO]CACHE_DYNAMIC setting persists until Actian Data Platform is shut down. See also SET SESSION [NO]CACHE_DYNAMIC.

**SET CONNECTION connection_name | NONE**

:   Switches the current session to a connection previously established using the CONNECT statement. SET CONNECTION NONE results in no current session.

:   Valid in Embedded SQL only.

**SET DATE_FORMAT [value]**

:   Specifies the format for date values. This option corresponds to the Actian Data Platform environment variable II_DATE_FORMAT and is assigned the same values. If set, DATE_FORMAT replaces the currently configured format with an alternate format. The default setting is US.

**SET DECIMAL [value]**

:   Specifies the character to be used as the decimal point in numeric literals. This option corresponds to the Actian Data Platform environment variable II_DECIMAL and is assigned the same values. Valid characters are the period (.) (as in 12.34) and the comma (,) (as in 12,34). The default is the period.

**SET FLOAT_FORMAT 'format'**

:   Sets floating point output to the specified format. Allows a portable copydb operation to automatically generate SET statements to use the specified format (for example: -f4F79.38 and -f8F79.38) so floating point values do not lose precision if an appropriate floating point output format is not specified on the command line.

**SET INSERTMODE DEFAULT | ROW | BULK**

:   Specifies the mode to use for inserts and merges. This statement can be used to force appends to go through the PDTs, to allow concurrent inserts. Modes are as follows:

DEFAULT

:   Uses default behavior: Single row inserts go through the PDT, INSERT...AS SELECT does not.

ROW

:   Inserts through the PDT (allows concurrent inserts)

BULK

:   Appends directly to disk (does not allow concurrent inserts)

**SET JOINOP NOTIMEOUT | TIMEOUT | TIMEOUT nnn**

:   Changes the timeout point of the query optimizer. When the query optimizer is checking query execution plans, it stops when it believes that the best plan that it has found takes less time to execute than the amount of time already spent searching for a plan or when it has evaluated all possible query plans, whichever is reached first.

:   SET JOINOP TIMEOUT nnntells the query optimizer to stop looking for query execution plans after the specified number of milliseconds and to use the best plan found to that point.

:   If 0 is specified, the timeout occurs when the optimizer finds that the best plan found so far will take less time to execute than the amount of time already spent evaluating plans (the default).

:   SET JOINOP NOTIMEOUT tells the optimizer to search ALL possible query plans. SET JOINOP TIMEOUT restores the default TIMEOUT.

:   This option has no effect if the GREEDY option is in effect.

**SET JOINOP TIMEOUTABORT nnn**

:   Specifies the time in milliseconds after which the optimizer stops considering query plans and uses the best plan found to that point. If no plan is found within the specified time, an error is generated.

:   If 0 (the default) is specified, the timeout is disabled.

:   Like SET JOINOP TIMEOUT nnn, SET JOINOP TIMEOUTABORT nnninstructs the optimizer to time out after nnnmilliseconds of processing.

:   The TIMEOUTABORT option, however, also applies to the time prior to obtaining the first query plan. If the time expires and no plan is found, the query is terminated with an error. If at least one plan is found, the best plan is used and the query is executed.

:   Contrast this with SET JOINOP TIMEOUT nnn, where the time can expire only after the first plan is found.

:   As with SET JOINOP TIMEOUT, the default value of 0 for SET JOINOP TIMEOUTABORT effectively disables this feature.

:   If both TIMEOUT and TIMEOUTABORT have been assigned non-zero values, the following rules apply:

    - If TIMEOUT is greater than or equal to TIMEOUTABORT, this is equivalent to TIMEOUT being set to 0, that is, its value is ignored and the TIMEOUTABORT mechanism is in effect.

    - If TIMEOUTABORT is greater than TIMEOUT, then both timing strategies are in effect.

    - If the TIMEOUT time expires, the search for a better plan stops if any plan is found.

    - Otherwise, optimization continues until either a plan is found or the TIMEOUTABORT timer expires.

:   As with SET JOINOP TIMEOUT nnn, this new timing feature does not affect the default SET JOINOP TIMEOUT behavior, which is to time out when as much time has been used for optimization as the estimated execution time of the best plan found so far.

**SET JOINOP [NO]GREEDY**

:   Enables or disables the complex query enumeration heuristic of the query optimizer. The greedy heuristic enables the optimizer to produce a query plan much faster than with its default technique of exhaustive searching for query execution plans when the query references a large number of tables. When SET JOINOP GREEDY is specified, the SET JOINOP TIMEOUT statement has no effect.

**SET MAXROWSTEP n**

:   Specifies the number of rows that an individual query step cannot exceed before the query is canceled.

**SET MONEY_FORMAT [value]**

:   Specifies the format for monetary output. This option corresponds to the Actian Data Platform environment variable II_MONEY_FORMAT and is assigned the same values. The default is L:$. The symbol to the left of the colon indicates the location of the currency symbol—L for a leading currency symbol or a T for a trailing currency symbol. The symbol to the right of the colon is the currency symbol you want displayed. Currency symbols can contain up to four physical characters. If no currency symbol is required, set the value to NONE (case insensitive). For example:

| Definition | Result |
| --- | --- |
| `L:$` | `$100` |
| `T:DM` | `100DM` |
| `T:F` | `100F` |

**SET MONEY_PREC [value]**

:   Specifies the number of decimal places to be displayed for money values. This option corresponds to the Actian Data Platform environment variable II_MONEY_PREC and is assigned the same values. Valid values are 0, 1, and 2. The default is 2 (for decimal currency).

**SET [NO]OJFLATTEN**

:   Tells the query optimizer to use (SET OJFLATTEN) or not to use (SET NOOJFLATTEN) the transformation that converts a NOT EXISTS/NOT IN subselect to an outer join with the containing query. The default is SET OJFLATTEN.

**SET [NO]OPTIMIZEONLY**

:   Specifies whether query execution should halt after the completion of query optimization. Use SET OPTIMIZEONLY with SET QEP when there is a requirement to view query execution plans without executing a query.

**SET PARTITION_SCHEME {AUTO | NONE | HASH}SET NOPARTITION_SCHEME**

:   Automatically assigns a partition scheme when an X100 table is created during a CREATE TABLE statement. Valid values are:

NONE

:   No partitioning.

HASH

:   Hash partitioning on the first column of the table.

AUTO

:   Automatic partitioning.

:   SET PARTITION_SCHEME overrides the default setting for the session. SET NOPARITION_SCHEME removes the session setting and uses the system default.

**SET PARTITION_PARTS n SET NOPARTITION_PARTS**

:   Sets the number of partitions that should be created when a default partitioning scheme is used. SET PARTITION_PARTS overrides the default setting for the session. SET NOPARTITION_PARTS removes the session setting and uses the system default.

**SET [NO]PRINTQRY**

:   Displays or does not display each query and its parameters as it is passed to Actian Data Platform for processing.

**SET [NO]QEP [CONCISE | SEGMENTED]**

:   Displays or does not display a graphical representation of the query execution plan (QEP) chosen for the query by the optimizer. SET QEP CONCISE displays the QEP in a format that is suitable for parsing by a program. SET QEP SEGMENTED displays QEP as a series of segments that are easier to read when parsing complex SQL statements.

**SET RANDOM_SEED [value]**

:   Sets the beginning value for the random functions. The global seed value is used until you issue SET RANDOM_SEED, which changes the value of the local seed. Once changed, the local seed is used for the entire session. If you are using the global seed value, the seed is changed whenever a random function executes. This means that other users issuing random calls enhance the “randomness” of the returned value. The seed value can be any integer. If you omit the value, the value is a multiple of the process ID and the number of seconds since 1/1/1970.

**SET RESULT_STRUCTURE**

:   Forces WITH STRUCTURE=VECTORWISE, VECTORWISE_ROW, or HEAP on all CREATE TABLE, CREATE TABLE AS SELECT, and DECLARE GLOBAL TEMPORARY TABLE statements for the session.

**SET [NO]REUSE**

:   Disables the “reuse” heuristic of the query optimizer.

**SET [NO]SCHEMA**

:   The SET SCHEMA schema_name statement sets the schema for the session. If schema is not the same as the current user then all further unqualified object references are treated as if the schema value had been explicitly provided as a qualification.

:   For example, SET SCHEMA john applies “john.” to all unqualified object references. So SELECT * FROM mytab becomes SELECT * FROM from john.mytab.

:   The current schema_name can be retrieved using:

```
SELECT DBMSINFO('SESSION_SCHEMA')
```

:   SET SCHEMA (with no parameters) or SET NOSCHEMA resets schema_name to the current session user.

:   SET SCHEMA is ignored for all system catalogs.

**SET SESSION AUTHORIZATION**

:   Lets a user with security administrator and operator privilege or who is the DBA of the database to set the effective user for the current session. The statement must be issued before a transaction commences and the settings apply until that session is completed. The SET SESSION AUTHORIZATION options are as follows:

username

:   The user name specified

USER | CURRENT USER | SESSION USER

:   The current user of the session (Actian Data Platform user)

SYSTEM_USER

:   The operating system user who started the session

INITIAL_USER

:   The Actian Data Platform user ID that started the session

**SET SESSION [NO]CACHE_DYNAMIC**

:   Enables or disables the caching of query plans for cursors defined with dynamic SELECT statements. It overrides the server level setting defined by the CACHE_DYNAMIC configuration parameter. To check the current setting, use SELECT DBMSINFO ('CACHE_DYNAMIC'). See also SET [NO]CACHE_DYNAMIC.

**SET SESSION READ ONLY | READ WRITE**

:   Controls the access mode for the current session. The SET SESSION statement must be issued before a transaction commences and the settings apply until that session is completed.

:   SET SESSION READ ONLY means that insert, update, delete, copy, and DDL operations are disallowed, and an SQLSTATE of 25000 (invalid session state) is returned. Temporary tables are the exception and are always writable. When a READ ONLY session is begun, it registers itself with the logging system. Use it for applications that can be read only most of the time.

:   SET SESSION READ ONLY prevents the session from being part of conflict resolution. Not being part of conflict resolution means that transactions executed as READ ONLY do not cause committed transaction memory to be used.

:   SET SESSION may be overridden with SET TRANSACTION.

**SET SESSION WITH DESCRIPTION | NODESCRIPTION**

:   Tracks tools and users that are logging into the database. For example:

```
 SET SESSION WITH DESCRIPTION = 'BI="PowerBI";UID="Jason";TYPE="Adhoc";FQ="Monthly"'
```

**SET SESSION WITH ON_ERROR**

:   Specifies how transaction errors are handled in the current session.

:   ROLLBACK TRANSACTION rolls back the current transaction if an error occurs. ROLLBACK rolls back only the current statement. This is the default.

:   To determine the current status of transaction error handling, issue the SELECT DBMSINFO('ON_ERROR_STATE') statement.

:   ROLLBACK TRANSACTION reduces logging overhead and can help performance. The performance gain is offset by the fact that, if an error occurs, the entire transaction is rolled back. The following errors always roll back the current transaction regardless of the current transaction error-handling setting:

    - Deadlock

    - Forced termination

    - Lock quota exceeded

:   To determine if a transaction was terminated as the result of a database statement error, issue the SELECT DBMSINFO('TRANSACTION_STATE') statement. If the error terminated the transaction, this statement returns 0, indicating that the application is currently not in a transaction.

!!! note "Note"

    SQL syntax errors (including most messages beginning with E_US) do not cause a rollback. Only errors that occur during execution of the SQL statement cause a rollback.

**SET SESSION WITH ON_USER_ERROR**

:   Specifies how user errors are handled in the current session. ROLLBACK TRANSACTION rolls back the effects of the entire transaction if a user error occurs. To revert back to default behavior, specify NOROLLBACK.

**SET [NO]STATISTICS tablename**

:   Tells the query optimizer to use or ignore any statistics found in IIHISTOGRAMS or IISTATISTICS for the specified table. The default is for the query optimizer to use statistics.

:   SET [NO]STATISTICS permanently modifies the table definition and affects queries in future sessions, so its use is restricted to the table owner and DBA.

**SET TRANSACTION READ ONLY | READ WRITE**

:   The SET TRANSACTION statement is used to override the SET SESSION setting. SET TRANSACTION must be issued before a transaction commences and the settings last only until that transaction is completed.

:   The access mode options are as follows:

READ ONLY

:   When a transaction access mode of READ ONLY is specified, insert, update, delete, copy, and DDL operations are disallowed, and an SQLSTATE of 25000 (invalid session state) is returned. Temporary tables are the exception and are always writable.

:   When a READ ONLY transaction is begun, it registers itself with the logging system and is allowed to proceed.

READ WRITE

:   When you need to write to the database, use SET TRANSACTION READ WRITE for that transaction.

!!! note "Note"

    The access mode of a transaction has no effect on the locking mode of the transaction.

**SET STRING_TRUNCATION IGNORE | WARN | FAIL**

:   Sets error handling mode for string truncation errors. Such an error occurs if an attempt is made to insert a string into a table column that is too short to contain the value. Valid values are:

IGNORE

:   Truncates and inserts the string without issuing an error message.

WARN

:   Truncates and inserts the string and issues a warning message.

**Note:**X100 operations treat WARN as FAIL.

FAIL

:   (Default) Aborts the statement and issues an error message. The FAIL option is supported only for singleton INSERTs and COPY. It is supported only in cases where the literal string value can be validated, so it is not supported for CREATE TABLE AS SELECT, INSERT...SELECT, nor for updates where the string value originates from an expression from another table.

**SET [NO]UNION_FLATTENING**

:   Turns union flattening on or off for the session.

:   Union flattening is an optimization technique used to increase the potential for compiling efficient query plans. If a query involves joining the result of a union view (or derived table or common table element) to other tables or views, the query optimizer will expand the union view to produce a query that is the union of each SELECT in the union view joined to the other tables. For example, if a view is defined as “create view uv as select * from u1 union all select * from u2”, and a query is executed as “select * from uv, a, b where uv.x = a.y and a.p = b.q”, the optimizer will transform it to “select * from u1, a, b where u1.x = a.y and a.p = b.q union all select * from u2, a, b where u2.x = a.y and a.p = b.q”.

:   Default: OFF
