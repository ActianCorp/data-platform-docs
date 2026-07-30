---
title: "Query Parallelism"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Query_Parallelism.htm"
canonical_id: "actian-data-platform-query-parallelism"
---

## Query Parallelism

```
queryParallelism -w <count> -c <count>
```

Displays configured maximum parallelism level, count of queries started during the previous minute, and mean threads per query.

The warning (-w) and critical (-c) thresholds are applied to the query with the lowest parallelism level; if that level is below the warning threshold, then a warning alert is raised. If the level is below the critical threshold, a critical alert is raised. Note that critical threshold value should be less than the warning value. For more information, see [Service Statuses](../User/Service_Statuses.md).

```
max parallelism: 32 queries: 349 mean threads: 26.8
```

The detail section displays statistics for queries started during each of the preceding 5 minutes, most current first. The table consists of 8 buckets ranging from 1 to the maximum configured parallelism level, and the value is a count of queries started with that number of threads. In the following example, for the third minute of the current hour:

214 queries were started with 29–32 threads per query in boldface
15 queries were started with 21–24 threads per query

89 queries were started with 17–20 threads per query
31 queries were started with 13–16 threads per query

```
                                   Parallelism
```

```

```

```
Minute    1-4      5-8      9-12    13-16    17-20    21-24    25-28    29-32
```

```

```

```
   03        0        0        0       31       89       15        0      214
```

```

```

```
   02        0        0        0       32       82       29        0      209
```

```

```

```
   01        0        0        9       20       83       18        0      243
```

```

```

```
   00        0        0        0       34       63       32        0      225
```

```

```

```
   59        0        0        1       13      100       12        0      229
```

At query start time the scheduler determines parallelism level by looking at the number of currently executing queries and number of threads per query. If those values are relatively low, then the current query is likely to execute at or near max parallelism level. As those values increase, new queries will execute at lower and lower parallelism levels. A heavily loaded environment will tend to have most queries executing at the lower ranges of parallelism.
