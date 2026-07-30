---
title: "Automatic Stopping of Idle Databases"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Automatic_Stopping_of_Idle_Databases.htm"
canonical_id: "actian-data-platform-automatic-stopping-of-idle-databases"
---

## Automatic Stopping of Idle Databases

Every database on the Actian Data Platform includes an idle stop feature that automatically stops an idle database to save costs. You can see the database created date at the bottom of the [Database Instance Details](../DBaaS_User/Database_Instance_Details.md) page.

You can set the idle stop time at database creation from a minimum of 0 hours, 15 minutes to a maximum of 4 hours, 45 minutes. For more information, see [Create a New Database Instance](../DBaaS_User/Create_a_New_Database_Instance.md).

An idle database is one that has no running queries. If you open a connection to the database but do nothing in that session, Actian Data Platform considers the database idle. If a database remains idle for the amount of idle stop time that was set, the database stops. The automatic idle stop timer gets reset when there is a new connection or a new query is run.

If your database has stopped and you want to restart it, see [Restart a Database](../DBaaS_User/Restart_a_Database_2.md).

To modify idle stop period for Google Cloud warehouses, see [Modify Idle Stop Period](../DBaaS_User/Modify_Idle_Stop_Period.md).
