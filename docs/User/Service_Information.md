---
title: "Service Information"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Service_Information.htm"
canonical_id: "actian-data-platform-service-information"
---

## Service Information

These are the fields on each service page.

| Field | Description |
| --- | --- |
| Status | Current operational status of a service check. Can be OK, Warning, Critical, Pending, and Unknown. See [Service Statuses](../User/Service_Statuses.md). |
| Status Information | Each service check not only returns basic information checked for properly operational criteria, but also contains additional details important to resolving potential problems as reported by Warning and Critical statuses. |
| Last Check Time | The clock time of the previous service check attempt. This time is always updated regardless of the returned status. It is possible this time can be older than expected if there are maintenance windows and similar situations were service checks are delayed. |
| Next Scheduled Check | The clock time of the next scheduled attempt to check on a service status. If services are not in an OK state, the monitoring system uses a heuristic to determine the next check time, which may be longer than normal if a service is not responding with an acceptable status. In that case the next check may be a longer time interval than normally found with services in an OK state. |
| Last State Change | This is a clock time that the service check made a transition between the various statuses. It can be useful to determine if a service has been in an OK state for a long time or how long a service has been in a Warning or Critical state. |
| In Scheduled Downtime? | If this information field is “Yes,” then the service check is being ignored because the system is undergoing some type of maintenance procedure. Service checks are typically disabled during maintenance windows. |
| Last Update | The time information about the service check was modified. This is more than just a last check time, as Operations may have acknowledged a Warning or Critical status or the system may have entered a maintenance window. |
