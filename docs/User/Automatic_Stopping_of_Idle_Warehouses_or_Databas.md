---
title: "Automatic Stopping of Idle Warehouses or Databases"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Automatic_Stopping_of_Idle_Warehouses_or_Databas.htm"
canonical_id: "actian-data-platform-automatic-stopping-of-idle-warehouses-or-databas"
---

## Automatic Stopping of Idle Warehouses or Databases

Every Actian warehouse/database created includes an idle stop feature that automatically stops idle warehouse/database to save costs. You can see the warehouse/database created date at the bottom of the [Warehouse Details](../User/Warehouse_Details.md) or [Database Instance Details](../User/Database_Instance_Details.md) page.

You can set the idle stop time at warehouse/database creation from a minimum of 0 hours, 15 minutes to a maximum of 4 hours, 45 minutes. For more information, see [Create a Warehouse](../User/Create_a_Warehouse.md) or [Create a New Database Instance](../User/Create_a_New_Database_Instance.md).

An idle warehouse/database is one that has no running queries. If you open a connection to the Actian warehouse/database but do nothing in that session, the Actian Data Platform will consider the warehouse/database as idle. If a warehouse/database remains idle for the amount of idle stop time that was set, the Actian Data Platform will automatically stop the warehouse/database. The automatic idle stop timer gets reset when there is a new connection or a new query is run.

If your warehouse/database has stopped and you want to restart it, see [Restart a Warehouse](../User/Restart_a_Warehouse.md).

To modify idle stop period for Google Cloud warehouses, see [Modify Idle Stop Period](../User/Modify_Idle_Stop_Period.md).
