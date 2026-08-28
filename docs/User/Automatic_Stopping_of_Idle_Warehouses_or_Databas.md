---
title: "Automatic Stopping of Idle Warehouses"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Automatic_Stopping_of_Idle_Warehouses_or_Databas.htm"
canonical_id: "actian-data-platform-automatic-stopping-of-idle-warehouses-or-databas"
---

## Automatic Stopping of Idle Warehouses

Every Actian warehouse created includes an idle stop feature that automatically stops idle warehouse to save costs. You can see the warehouse created date at the bottom of the [Warehouse Details](../User/Warehouse_Details.md) page.

You can set the idle stop time at warehouse creation from a minimum of 0 hours, 15 minutes to a maximum of 4 hours, 45 minutes. For more information, see [Create a Warehouse](../User/Create_a_Warehouse.md).

An idle warehouse is one that has no running queries. If you open a connection to the Actian warehouse but do nothing in that session, the Actian Data Platform will consider the warehouse as idle. If a warehouse remains idle for the amount of idle stop time that was set, the Actian Data Platform will automatically stop the warehouse. The automatic idle stop timer gets reset when there is a new connection or a new query is run.

If your warehouse has stopped and you want to restart it, see [Restart a Warehouse](../User/Restart_a_Warehouse.md).

To modify idle stop period for Google Cloud warehouses, see [Modify Idle Stop Period](../User/Modify_Idle_Stop_Period.md).
