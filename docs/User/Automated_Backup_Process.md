---
title: "Automated Backup Process"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Automated_Backup_Process.htm"
canonical_id: "actian-data-platform-automated-backup-process"
---

## Automated Backup Process

Once created, all production warehouses are backed up automatically following this process:

1. After being provisioned, a full offline backup is run.
2. Full backups are run weekly on Sundays at 1:00 a.m. UTC.

    - The five most recent backups are retained, then the oldest is deleted when a new one is created.

3. Incremental backups are taken periodically.
4. If a user deletes a warehouse, all backups associated with the warehouse are deleted after 3 days.

To request that a backup be restored, contact Actian Support.

!!! note "Note"

    Restoring a backup will not change the warehouse version.
