---
title: "Backup and Recovery Policy"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Backup_and_Recovery_Policy.htm"
canonical_id: "actian-data-platform-backup-and-recovery-policy"
---

## Backup and Recovery Policy

Full backups run automatically once a week on a per-warehouse basis. This is an on-line process and takes a consistent snapshot of the warehouse to serve as an initial point of recovery. You can also schedule your own backups, if desired. See [Modify Maintenance Window Starting Times](../User/Modify_Maintenance_Window_Starting_Times.md).

Additionally, incremental backups are taken about every 15 minutes. Incremental backups are processed at the transaction level to ensure consistency. By default, we retain 5 weekly backups, which when combined with the incremental backups allows a warehouse to be restored to any complete incremental backup point within a rolling 35 day window.

Recovery can be initiated at any time by the user but must be done so by raising a support ticket. They can either be performed in place or targeted to a newly created warehouse
