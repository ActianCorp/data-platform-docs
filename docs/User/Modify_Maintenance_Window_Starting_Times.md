---
title: "Modify Maintenance Window Starting Times"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Modify_Maintenance_Window_Starting_Times.htm"
canonical_id: "actian-data-platform-modify-maintenance-window-starting-times"
---

## Modify Maintenance Window Starting Times

Warehouse or database administrators may modify the time when maintenance activities, such as updates and backups, occur.

When available, updates run first, which should take only a few minutes. A running warehouse stops while updates apply and then returns to its previous state after the update period. The weekly backup initiates after updates complete. A running warehouse may continue to run while the backup proceeds.

To modify the Maintenance Window start time:

1. On the Warehouses page, click the warehouse whose maintenance window you want to change.

    The [Warehouse Details](../User/Warehouse_Details.md) page displays.

2. In the Maintenance Window row, click Update.

    The Maintenance Window row dialog opens.

3. Set the day and time for the maintenance to begin each week.
4. Click Save.

    The Maintenance Window updates to the new day and time.
