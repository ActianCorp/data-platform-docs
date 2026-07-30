---
title: "Warehouse Monitoring Services"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Warehouse_Monitoring_Services.htm"
canonical_id: "actian-data-platform-warehouse-monitoring-services"
---

## Warehouse Monitoring Services

These are the monitoring services:

- [Active Queries](../User/Active_Queries.md)
- [Cluster CPU Load](../User/Cluster_CPU_Load.md)

- [Connected Sessions](../User/Connected_Sessions.md)
- [Error Log](../User/Error_Log.md)

- [Execution Memory](../User/Execution_Memory.md)
- [Pending Disk Updates](../User/Pending_Disk_Updates.md)

- [Query Parallelism](../User/Query_Parallelism.md)
- [System Data Skew](../User/System_Data_Skew.md)

- [Table Data Skew](../User/Table_Data_Skew.md)
- [Warehouse Disk Usage](../User/Warehouse_Disk_Usage.md)

| Field | Description |
| --- | --- |
| Service | Displays the available services. Clicking on a link displays the service’s page. |
| Status | Displays the [Service Statuses](../User/Service_Statuses.md). |
| Last Checked | The clock time of the previous service check attempt. This time is always updated regardless of the returned status. |
| Attempt | Displays the number of the attempted service status checks/maximum number of attempts. 1/1 means an alert is raised as soon as a service check returns a status other than OK. 1/5 means an alert would not be raised unless 5 consecutive service checks returned a status other than OK and the first number would count the number of attempts, that is, it would read 1/5 then 2/5 until 5/5, when an alert is raised. |
| Status Information | Returns basic information checked for properly operational criteria, but also may contain additional details important to resolving potential problems as reported by Warning and Critical statuses. |
| Graph | Clicking the icon opens the service’s Graph tab. For more information, see [Graphing Service Information](../User/Graphing_Service_Information.md). |
