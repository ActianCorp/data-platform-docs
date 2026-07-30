---
title: "Database Monitoring Services"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Database_Monitoring_Services.htm"
canonical_id: "actian-data-platform-database-monitoring-services"
---

## Database Monitoring Services

These are the monitoring services:

- [Error Log](../DBaaS_User/Error_Log.md)
- [DBMS Processes](../DBaaS_User/DBMS_Processes.md) -> Needs doc writeup

- [Lock Waits](../DBaaS_User/Lock_Waits.md) -> Needs doc writeup
- [Transaction Log](../DBaaS_User/Transaction_Log.md) -> Needs doc writeup

- [OS Disk Usage](../DBaaS_User/OS_Disk_Usage.md)
- [OS Load Average](../DBaaS_User/OS_Load_Average.md) -> Needs doc writeup

- [OS Memory](../DBaaS_User/OS_Memory.md) -> Needs doc writeup
- [Active Queries KEEP?](../DBaaS_User/Active_Queries_KEEP_3f.md) ??

- [Connected Sessions KEEP?](../DBaaS_User/Connected_Sessions_KEEP_3f.md) ??
- | Field | Description |
| --- | --- |
| Service | Displays the available services. Clicking on a link displays the service’s page. |
| Status | Displays the [Check a Service](../DBaaS_User/Check_a_Service.md). |
| Last Checked | The clock time of the previous service check attempt. This time is always updated regardless of the returned status. |
| Attempt | Displays the number of the attempted service status checks/maximum number of attempts. 1/1 means an alert is raised as soon as a service check returns a status other than OK. 1/5 means an alert would not be raised unless 5 consecutive service checks returned a status other than OK and the first number would count the number of attempts, that is, it would read 1/5 then 2/5 until 5/5, when an alert is raised. |
| Status Information | Returns basic information checked for properly operational criteria, but also may contain additional details important to resolving potential problems as reported by Warning and Critical statuses. |
| Graph | Clicking the icon opens the service’s Graph tab. |
