---
title: "MASK_COLUMN Function"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "MASK_COLUMN_Function.htm"
canonical_id: "actian-data-platform-mask-column-function"
---

## MASK_COLUMN Function

The MASK_COLUMN function unmasks the column or alters the way masked data is displayed. This special function can be used in views to allow the control of delegated access to masked data.

```
MASK_COLUMN(expr AS {BASIC | NULL | 0 | ' ' | UNMASK})
```

Examples:

Create a view that unmasks the minimum, maximum, and average salaries. Queries against the view will display the actual data, not mask it. Permit everyone to view the data.

```
CREATE VIEW employee_salary_stats AS SELECT
```

```
MIN(MASK_COLUMN(salary AS UNMASK)) min_salary,
```

```
MAX(MASK_COLUMN(salary AS UNMASK)) max_salary,
```

```
AVG(MASK_COLUMN(salary AS UNMASK)) average_salary FROM employee;
```

```
GRANT select ON employee_salary_stats TO public;
```

Create a view in which the values for minimum, maximum, and average salary are shown as asterisks, not actual values. Permit everyone to view the data.

```
CREATE VIEW employee_salary_stats AS SELECT
```

```
MIN(MASK_COLUMN(salary AS BASIC)) min_salary,
```

```
MAX(MASK_COLUMN(salary AS BASIC)) max_salary,
```

```
AVG(MASK_COLUMN(salary AS BASIC)) average_salary FROM employee;
```

```
GRANT select ON employee_salary_stats TO public;
```

## DBMSINFO Function

DBMSINFO is a SQL function that returns a string containing information about the current session. Use this function in the SQL CLI or in an embedded SQL application.

The DBMSINFO function is used in a SELECT statement like this:

```
SELECT DBMSINFO('request_name')
```

where 'request_name' is one of those described in [Request Names for DBMSINFO Function](../SQLLanguage/MASK_COLUMN_Function.md).

### Request Names for DBMSINFO Function

Valid request_names for the DBMSINFO function are:

**autocommit_state**

:   Returns 0 if autocommit is OFF, 1 if autocommit is ON, 2 if autocommit is READ.

**_bintim**

:   Returns the current time and date in an internal format, represented as the number of seconds since January 1, 1970 00:00:00 GMT.

**_bio_cnt**

:   Returns the number of I/Os to and from the front-end client (application) that created your session.

**cache_dynamic**

:   Returns Y if cache_dynamic is on; otherwise returns N.

**charset**

:   Returns the value of II_CHARSETxx, the character set setting for the installation.

**collation**

:   Returns the collation sequence defined for the database associated with the current session. This returns blanks if the database is using the collation sequence of the machine’s native character set, such as ASCII or EBCDIC.

**connect_time_limit**

:   Returns the session connect time limit or -1 if there is no connect time limit.

**create_table**

:   Returns Y if the session has create_table privileges in the database or N if the session does not.

**_cpu_ms**

:   Returns the CPU time for the session in milliseconds.

**current_priv_mask**

:   Returns the decimal number representing a mask of internal privilege bits currently enabled for the user.

**database**

:   Returns the database name.

**datatype_major_level**

:   Returns -2147483648 unless the user data types are in use.

**datatype_minor_level**

:   Returns 0 unless the user data types are in use.

**date_format**

:   Returns the current date format setting (set on II_DATE_FORMAT or by the SET statement).

**date_type_alias**

:   Returns the value of the date_alias parameter set at installation: default is ANSIDATE.

**dba**

:   Returns the user name of the database owner.

**db_admin**

:   Returns Y if the session has db_admin privileges, and N if the session does not have db_admin privileges.

**db_cluster_node**

:   Returns the machine you are connected to. Valid even if not clustered.

**db_count**

:   Returns the number of distinct databases opened.

**db_real_user_case**

:   Returns lower, upper, or mixed.

**dbms_bio**

:   Returns the cumulative non-disk I/O's performed by the server hosting session.

**dbms_cpu**

:   Returns the cumulative CPU time for the Actian Data Platform, in milliseconds, for all connected sessions.

**dbms_dio**

:   Returns the cumulative disk I/O's performed by the server hosting session.

**db_delimited_case**

:   Returns LOWER if delimited identifiers are translated to lower case, UPPER if delimited identifiers are translated to upper case, or MIXED if the case of delimited identifiers is not translated.

**db_name_case**

:   Returns LOWER if regular identifiers are translated to lower case or UPPER if regular identifiers are translated to upper case.

**db_privileges**

:   Returns a decimal integer which represents a bit mask of “Subject” privileges.

**db_tran_id**

:   Returns the 64 bit internal transaction ID as two decimal numbers.

**decimal_format**

:   Returns the current decimal format setting (set on II_DECIMAL or by the SET statement) for the session.

**_dio_cnt**

:   Returns the number of disk I/O requests for your session.

**_et_sec**

:   Returns the elapsed time since the start of your session, in seconds.

**flatten_aggregate**

:   Returns Y if the Actian Data Platform is configured to flatten queries involving aggregate subselects; otherwise, returns N. (Query flattening options are specified when the Actian Data Platform is started.)

**flatten_singleton**

:   Returns Y if the Actian Data Platform is configured to flatten queries involving singleton subselects; otherwise, returns N. (Query flattening options are specified when the Actian Data Platform is started.)

**group**

:   Returns the group identifier of the session or blanks if no group identifier is in effect.

**idle_time_limit**

:   Returns the session idle time limit or -1 if there is no idle time limit.

**ima_server**

:   Equivalent to IMA registration exp.gwf.gwm.glb.this_server, which returns the listen address of the attached server.

**ima_session**

:   Returns the internal session ID in decimal format.

**ima_vnode**

:   Equivalent to IMA registration exp.gwf.gwm.glb.def_vnode configuration value if set for the connected server. If not set, defaults to the local host name.

**initial_user**

:   Returns the user identifier in effect at the start of the session.

**language**

:   Returns the language used in the current session to display messages and prompts.

**lp64**

:   Returns Y if 64 bit pointers are in use, or N if 32 bit addresses are used.

**maxconnect**

:   Returns the current connect time limit, as set by the set maxconnect statement, or the initial value if no connect time limit has been set.

**maxcost**

:   Returns the value specified in the last set maxcost statement. If no previous set maxcost statement was issued or if set nomaxcost was specified last, this returns the same value as the request name query_io_limit.

**maxcpu**

:   Returns the value specified in the last set maxcpu statement. If no previous set maxcpu statement was issued or if set nomaxcpu was specified last, this returns the same value as the request name query_io_limit.

**maxidle**

:   Returns the current idle time limit, as set with the set maxidle statement, or the initial value if no idle time limit has been set.

**maxio**

:   Returns the value specified in the last set maxio statement. If no previous set maxio statement was issued or if set nomaxio was specified last, this returns the same value as the request name query_io_limit.

**maxquery**

:   Same as maxio.

**maxrow**

:   Returns the value specified in the last set maxrow statement. If no previous set maxrow statement was issued or if set nomaxrow was specified last, this returns the same value as the request name query_row_limit.

**maxpage**

:   Returns the value specified in the last set maxpage statement. If no previous set maxpage statement was issued or if set nomaxpage was specified last, this returns the same value as the request name query_io_limit.

**max_priv_mask**

:   Returns the decimal number representing a mask of internal privilege bits for which privileges the user might possess if all his/her privileges were enabled.

**max_tup_len**

:   Returns the maximum width for a tuple that does not span pages. This depends on max_page_size.

**money_format**

:   Returns the current money format setting (set on II_MONEY_FORMAT or by the SET statement).

**money_prec**

:   Returns the current money precision setting (set on II_MONEY_PREC or by the SET statement).

**on_error_state**

:   Returns the current setting for transaction error handling: rollback transaction or rollback statement. To set transaction error handling, use the set session with on_error statement.

**open_count**

:   Returns the number of times the database was opened.

**partition_spec_required**

:   Returns VECTOR if a partitioning specification is required on ; otherwise NONE.

**query_cost_limit**

:   Returns the session value for query_io_limit or -1 if no limit is defined for the session.

**query_cpu_limit**

:   Returns the session value for query_io_limit or -1 if no limit is defined for the session.

**query_flatten**

:   Returns Y if the query flattening is in effect or N if the query flattening is not in effect.

**query_io_limit**

:   Returns the session value for query_io_limit or -1 if no limit is defined for the session.

**query_language**

:   Returns sql or quel.

**query_page_limit**

:   Returns the session value for query_io_limit or -1 if no limit is defined for the session.

**query_row_limit**

:   Returns the session value for query_row_limit or -1 if no limit is defined for the session.

**role**

:   Returns the role identifier of the session or blanks if no role identifier is in effect.

**security_audit_log**

:   Returns the name of the current security auditing log file if it is enabled and the user has maintain_audit privileges, otherwise, remains blank.

**security_audit_state**

:   Returns the current Actian Data Platform security audit state. The following values are returned:

    (blank) – Security auditing is not available

    STOP – Security auditing is stopped

    SUSPEND – Security auditing is suspended

    ACTIVE – Security auditing is active

**security_priv**

:   Returns Y if the effective user has the security privilege or N if the effective user does not have the security privilege.

**select_syscat**

:   Returns Y if the session has select_syscat privilege or N if the session does not have select_syscat privilege.

**server_class**

:   Returns the server class for the session.

**session_id**

:   Returns the internal session identifier in hexadecimal.

**session_priority**

:   The current priority of the session or -1 if none

**session_schema**

:   Returns the current schema name for the session.

**session_user**

:   Returns the current effective user ID of the session.

**system_user**

:   Returns the system user ID.

**terminal**

:   Returns the terminal address.

**timeout_abort**

:   Returns Y or N, indicating that the database privilege GRANT TIMEOUT_ABORT is either enabled or disabled for the session.

**transaction_state**

:   Returns 1 if currently in a transaction and returns 0 if not currently in a transaction.

**ucollation**

:   Returns Unicode collation. The default is “udefault.”

**update_syscat**

:   Returns Y if the effective user is allowed to update system catalogs or N if the effective user is not allowed to update system catalogs.

**username**

:   Returns the name of the current user.

**_version**

:   Returns the Actian Data Platform runtime number.

**x100_host**

:   Returns the IP address of the node running the x100 server process.
