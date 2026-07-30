---
title: "Connected Sessions KEEP?"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Connected_Sessions_KEEP_3f.htm"
canonical_id: "actian-data-platform-connected-sessions-keep-3f"
---

## Connected Sessions KEEP?

```
connectedSessions -w <count> -c <count>
```

Displays a count of currently connected sessions.

The warning (-w) and critical (-c) thresholds are applied to the connect count; if connect count exceeds the critical threshold, a critical alert is raised. If connect count exceeds the warning threshold, a warning alert is raised. For more information, see Service Statuses.

```
Session count: 4
```

The detail section displays individual connection attributes:

| Detail | Description |
| --- | --- |
| Session ID | Internal sessions identifier |
| Elapsed Time | Connect time duration |
| Queries Executed | Count of queries executed by the session |
| Execution Time | Accumulated execution time for all queries executed by the session |
| Comm Server | Type of client connection (JDBC/.Net or ODBC/CLI) |
| Db user | Database username for the session |
| Client user@host | Client login username and client host name |
| Query Start | Start time for the currently executing query |

```
                     Elapsed   Queries    Execution       Comm
```

```
    Session ID         Time    Executed      Time        Server  Db user / Client user@host
```

```

```

```
    7F8E125D3640     0:37:58     1,104    10:52.914   JDBC/.Net  actian / user1@atchison11.tongy.local
```

```

```

```
Query Start: 15:43:59
```

```

```

```
Fetch ~Q cursor for
```

```

```

```
SELECT n_name, sum(l_extendedprice *(1 - l_discount)) AS revenue
```

```

```

```
FROM customer, orders, lineitem, supplier, nation, region
```

```

```

```
WHERE c_custkey = o_custkey AND l_orderkey = o_orderkey AND l_suppkey = s_suppkey AND c_nationkey =  . . .
```

The currently executing query may be abbreviated for display purposes. If that is the case, the line will end with “. . .”.
