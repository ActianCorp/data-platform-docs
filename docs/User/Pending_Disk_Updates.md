---
title: "Pending Disk Updates"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Pending_Disk_Updates.htm"
canonical_id: "actian-data-platform-pending-disk-updates"
---

## Pending Disk Updates

```
pdtUsage -w <percent> -c <percent>
```

Displays details about pending disk updates. The warning (-w) and critical (-c) thresholds are applied to the percentage of update memory used; if that percentage is higher than the critical threshold, a critical alert is raised. If the percentage is higher than the warning threshold, a warning alert is raised. For more information, see [Service Statuses](../User/Service_Statuses.md).

| Detail | Description |
| --- | --- |
| memory used | Query working memory consumed by pending disk updates |
| memory limit | Maximum memory allowed for all pending disk updates |
| memory % | Percentage of maximum currently in use |
| row insert | Count of row inserts in pending memory |
| row update | Count of row updates in pending memory |
| row delete | Count of row deletes in pending memory |

```
memory used/limit/%: 16.40M / 6.00G / 0.27% row insert/update/delete 0 / 68,265 / 100
```

The detail section identifies update memory usage by database table:

| Detail | Description |
| --- | --- |
| Memory | Pending update memory consumed by the table |
| Table | Table name using <owner>.<table> notation |

```
Memory Table
```

```

```

```
  14.25M actian.partsupp
```

```

```

```
   2.14M actian.customer
```

```

```

```
   2.71K actian.c_test
```
