---
title: "Automated Database Backup Process"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Automated_Database_Backup_Process.htm"
canonical_id: "actian-data-platform-automated-database-backup-process"
---

## Automated Database Backup Process

Once created, all production warehouses are backed up automatically following this process:

1. After being provisioned, a full offline backup is run and journaling is enabled.

!!! note "Note"

    The journaling process runs every 10 minutes. Therefore, Actian Support can restore a warehouse back to a 10-minute time window.

2. Full checkpoint backups are run weekly on Sundays at 1:00 a.m. UTC.

    - If the warehouse is on, a full online checkpoint is run.

    - If the warehouse is off, the warehouse is started, the checkpoint is run, and the warehouse is stopped.

3. Checkpoint backups are retained for 35 days and then deleted on day 36. (Up to 5 checkpoints are retained.) All warehouse journals older than 35 days old are also deleted.
4. If a user deletes a warehouse, all backups associated with the warehouse are deleted after 3 days.

To request that a backup be restored, contact Actian Support.
