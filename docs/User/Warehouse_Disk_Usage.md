---
title: "Warehouse Disk Usage"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Warehouse_Disk_Usage.htm"
canonical_id: "actian-data-platform-warehouse-disk-usage"
---

## Warehouse Disk Usage

Measures storage used for these metrics:

| Metric | Type of Storage | Description |
| --- | --- | --- |
| data | Database tables/indexes storage used | Space consumed by database tables and indexes |
| WAL | Write-ahead log storage, current and backups | Space consumed by the current WAL file and retained backup WAL files |
| backup | Full and incremental backup storage | Backup files are managed by the system and require no user intervention. Backup storage is space consumed by database backups, both full and incremental. Space consumed is a function of database size, backup frequency, and number of retained backups. |
| work | Temporary workfile storage | Space consumed by temporary work files generated during normal query execution |

The Actian Data Platform uses cloud provider blob storage, which is virtually unlimited. As a result, there are no alarm thresholds on storage used.

The service check displays storage used by each component in the appropriate units:

```
storage used: data 151.97GB, WAL 2.02GB, backup 0.00b, work 105.00b
```

The detail section displays data size in the appropriate units as well as database block count and block size. Space consumed is a product of blocks and block size.

```
data: 151.97GB blocks: 77810 block_size: 2.00MB
```
