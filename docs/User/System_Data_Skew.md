---
title: "System Data Skew"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "System_Data_Skew.htm"
canonical_id: "actian-data-platform-system-data-skew"
---

## System Data Skew

```
systemDataSkew -w <count> -c <count>
```

Displays total database blocks used along with per-node minimum, median, and maximum data skew. The warning (-w) and critical (-c) thresholds are applied to the highest per node data skew, and if that percentage is higher than the critical threshold, a critical alert is raised. If the percentage is higher than the warning threshold, a warning alert is raised. For more information, see [Service Statuses](../User/Service_Statuses.md).

```
total blocks: 25,795 data skew min/median/max: -26.8% / 3.4% / 13.3%
```

Skew percentage is calculated by dividing the node block average by the per-node block count; a negative percentage indicates a node block count lower than the per-node average.

The detail section displays the block size and the per-node minimum, median, and maximum block counts.

```
block size/count: 1.00M / 25,795 node min/median/max: 4,886 / 6,674.00 / 7,561
```

In the previous example, the database block size is 1 MB and the database occupies 25,795 blocks of data. Per-node minimum block count is 4,886, median is 6,674, and maximum is 7,561.

Data skew occurs when tables are partitioned using columns with relatively low cardinality or uneven data distribution. See [Table Data Skew](../User/Table_Data_Skew.md) to identify individual tables with poor data distribution.
