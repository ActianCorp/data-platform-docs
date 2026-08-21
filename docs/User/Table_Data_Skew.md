---
title: "Table Data Skew"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Table_Data_Skew.htm"
canonical_id: "actian-data-platform-table-data-skew"
---

## Table Data Skew

```
tableDataSkew -w <count> -c <count>
```

Displays counts of database tables with data skew. The warning (-w) and critical (-c) thresholds are applied to the table skew percentage; if that percentage is higher than the critical threshold, a critical alert is raised. If the percentage is higher than the warning threshold, a warning alert is raised. For more information, see [Service Statuses](../User/Service_Statuses.md).

```
1 critical tables and 0 warning tables
```

The detail section displays individual table data skew details:

| Detail | Description |
| --- | --- |
| Partitions | Partition count for the specific table |
| Total Blocks | Sum of data blocks for all partitions |
| Partition Blocks | • Min – Block count for smallest partition<br>• Median – Partition median block count<br>• Max – Block count for largest partition |
| Data Skew | Data skew percentage |
| Table | Table name using <owner>.<table> notation |

```
                Total                Partition Blocks          Data
```

```
Partitions      Blocks         Min       Median         Max    Skew  Table
```

```

```

```
     8           6,275           0          227       2,683  342.2%  actian.lineitem
```

Data Skew is calculated as partition blocks max / partition blocks average.
