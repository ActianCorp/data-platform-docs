---
title: "Active Queries KEEP?"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Active_Queries_KEEP_3f.htm"
canonical_id: "actian-data-platform-active-queries-keep-3f"
---

## Active Queries KEEP?

Displays a count of currently executing queries and the average execution threads per query.

The warning (-w) and critical (-c) thresholds are applied to the active query count; if active query count exceeds the critical threshold, a critical alert is raised. If active query count exceeds the warning threshold, a warning alert is raised. For more information, see Service Statuses.

```
active count: 2 average threads: 26.00
```

The detail section displays query execution statistics for the preceding 1 minute, 5 minutes, and 15 minutes. Queries is a count of queries that finished executing in the specified time frame. Execution Time is the minimum, median, and average per-query execution time for that collection of queries. Parallelism is the minimum, median, and maximum execution threads per query.

```
Time                       Execution Time              Parallelism
```

```

```

```
Frame  Queries       Min        Median       Max     Min Median  Max
```

```

```

```
   1       125    0:00.012    0:00.021    0:00.062    13   32.0   32
```

```

```

```
   5       469    0:00.015    0:00.021    0:00.246    10   32.0   32
```

```

```

```
  15     1,021    0:00.015    0:00.023    0:16.269    10   32.0   32
```

As a general rule, lightly loaded environments will have median parallelism relatively close to the maximum. As the overall load increases the gap between median and max will increase as well.
