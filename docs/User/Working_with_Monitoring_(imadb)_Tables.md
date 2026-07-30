---
title: "Working with Monitoring (imadb) Tables"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Working_with_Monitoring_(imadb)_Tables.htm"
canonical_id: "actian-data-platform-working-with-monitoring-imadb-tables"
---

## Working with Monitoring (imadb) Tables

For users to work with imadb tables, they must be assigned the [IMA_SEC_READ Privilege](../Security/Assigning_Privileges_and_Granting_Permissions.md).

Access to IMA (Ingres Management Architecture) tables enables users to view various real-time monitoring information. Only users who are assigned the useradmin profile have the privilege to read IMA tables. Any user may be assigned this profile; however, the profile also gives them user management privileges. At warehouse creation, the warehouse owner is automatically added to the useradmin profile and as a result will have read access to IMA tables.

**ima_dbms_server_status**

:   Provides usage and performance measurements about DBMS server status such as server, selects processed, current connections, listen state, shutdown state, server state, last activity start, and last activity finish

**ima_gca_connections**

:   Lists the current GCA connections (all active connections to DBMS server)

**ima_locklists**

:   Lists locks, their status and session ID, and server process ID they belong to

**ima_locks**

:   Displays all the transactional resource locks held by the DBMS

**ima_log_transactions**

:   Shows a log of transactions in the system, active and inactive

**ima_resources**

:   Lists the resources the locks are for

**ima_server_sessions**

:   Lists connected DBMS server sessions for both users and the system

**ima_server_sessions_query**

:   Provides the previous (last) query that was executed for a session. Combine with ima_server_sessions for complete information.

**ima_server_sessions_extra**

:   Provides additional information for each session, such as session ID, session start time, session state, wait reason, and current CPU consumption. This does not include X100-specific CPU use.

## Restrictions on IMA Use

These are current restrictions within IMA:

- The IMA supports full SQL but with the following restrictions:

    - –There is no locking or lock ownership of IMA underlying objects.

    - –There are no transactions for updates for IMA objects.

    - –Updates take immediate action and cannot be rolled back.

    - –All reads are “dirty.” This means that querying the same object may return different values because the data underlying the record could have changed.

    - –Rule triggering is unreliable. Rules are not triggered when the value of an object changes in a way unknown through SQL. This occurs to IMA-related data as the installation operates. Thus, while updates that are performed through SQL can trigger rules, rule integrity cannot be guaranteed for IMA data.

- The group of defined objects supplied with the imadb database is subject to change in subsequent releases.
- A cluster installation is visible to IMA as the installations on each node within a domain.

## Query Examples on IMA Tables

Notes:

- Selecting from IMA tables requires the IMA_SEC_READ privilege; otherwise 0 rows are returned.
- Each example assumes it is being run in a new session.

What are user sessions doing?

The following SQL shows what user sessions are currently doing

```
select
```

```
       *
```

```
from
```

```
       ima_server_sessions
```

```
where db_owner != '';
```

Who is waiting for a lock?

The following query shows which sessions are waiting for locks:

```
select distinct
```

```
       resource_id,
```

```
       lock_id,
```

```
       lock_state,
```

```
       ima_locklists.locklist_id,
```

```
       locklist_server_pid,
```

```
       locklist_session_id,
```

```
       effective_user,
```

```
       db_name,
```

```
       session_terminal,
```

```
       session_query
```

```
from
```

```
       ima_locks,
```

```
       ima_locklists,
```

```
       ima_server_sessions
```

```
where lock_state != 'GR'
```

```
and ima_locks.locklist_id = ima_locklists.locklist_id
```

```
and ima_locklists.locklist_server_pid = ima_server_sessions.server_pid
```

```
and ima_locklists.locklist_session_id = ima_server_sessions.session_id;
```

Who is holding a lock that other sessions need?

The following query shows which sessions are holding locks where other sessions are waiting:

```
select distinct
```

```
       resource_id,
```

```
       lock_id,
```

```
       lock_state,
```

```
       ima_locklists.locklist_id,
```

```
       locklist_server_pid,
```

```
       locklist_session_id,
```

```
       effective_user,
```

```
       db_name,
```

```
       session_terminal
```

```
       from
```

```
       ima_locks,
```

```
       ima_locklists,
```

```
       ima_server_sessions
```

```
where resource_id in
```

```
       (
```

```
       select distinct
```

```
              ima_locks.resource_id
```

```
       from
```

```
              ima_locks
```

```
       where lock_state != 'GR'
```

```
       )
```

```
and lock_state != 'WT'
```

```
and ima_locks.locklist_id = ima_locklists.locklist_id
```

```
and ima_locklists.locklist_server_pid = ima_server_sessions.server_pid
```

```
and ima_locklists.locklist_session_id = ima_server_sessions.session_id;
```

When did a query start?

You can find out when a query started and how long it has been running.

Notes:

- This is start of execution, not parsing or optimization.
- The start time is in seconds since 1-Jan-1900 00:00:00, known as a UNIX EPOCH value.

- The time is not zeroed when the query ends.

To find out how long a query has been running, here is a sample SQL statement that shows you the longest running query in the system:

```
select server, db_name, session_query, (bigint((current_timestamp - timestamp_with_tz('1970-01-01 00:00:00+00:00'))/interval '1' second) -  query_start_secs) as elapsedsecs
```

```
from ima_server_sessions
```

```
where db_name not in ('', 'imadb')\g
```

If a query is finished, it will still show in the list. In this case you can join another table and ignore queries in BIO state:

```
select db_name, session_query, (bigint((current_timestamp - timestamp_with_tz('1970-01-01 00:00:00+00:00'))/interval '1' second) -  query_start_secs) as elapsedsecs
```

```
from ima_server_sessions s,ima_server_sessions_extra e
```

```
where s.session_id = e.session_id and s.effective_user != ''
```

```
    and (e.session_state != 'CS_EVENT_WAIT' or e.session_wait_reason != 'BIOR')
```

```
    and db_name not in ('', 'imadb')
```

The previous query will show you all queries that are actually running as opposed to those already run, finished, and waiting for user input (\q and so on).
