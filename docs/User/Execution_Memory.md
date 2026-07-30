---
title: "Execution Memory"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Execution_Memory.htm"
canonical_id: "actian-data-platform-execution-memory"
---

## Execution Memory

```
queryMemory -w x -c y
```

At startup time, Actian Data Platform is configured with a query execution memory pool that is a percentage of the available host memory. This memory pool is shared by all currently executing queries, with each query allocating execution memory as needed.

The execution memory pool may be insufficient if the average allocation is consistently near the configured limit. In this situation, execution queries may be spilling working memory to disk or possibly aborting. Aborted queries will be logged by the error message service check. This metric measures execution memory usage by the currently executing queries.

```
execution memory min/avg/max/limit: 571.00MB / 726.00MB / 946.00MB / 24.00GB
```

The detail section displays this information:

| Detail | Description |
| --- | --- |
| Status | Status of the service |
| Status Information | See the following metrics for details |
| Last Check Time | Date and time the status was checked |
| Next Scheduled Check | Date and time of the next status check |
| Last State Change | Date and time when the status last changed |
| In Schedule Downtime? | Displays whether the warehouse is currently in scheduled downtime |
| Last Update | Date and time when the service was last updated |

Displayed metrics:

| min | minimum memory allocation in the most recent sample interval |
| --- | --- |
| avg | average memory allocation in the most recent sample interval |
| max | maximum memory allocation is the most recent sample interval |
| limit | size of query execution memory pool |

The associated graph charts the above metrics over time.
