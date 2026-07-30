---
title: "Service Statuses"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Service_Statuses.htm"
canonical_id: "actian-data-platform-service-statuses"
---

## Service Statuses

The following are the statuses for the services. When a warehouse is first started, statuses other than OK may be displayed until the warehouse is fully running.

| Status | Description |
| --- | --- |
| Pending | A service check has not yet run and there is no information currently available on the status of the service check. However, the service check is active and scheduled to be checked shortly. See “Next Scheduled Check” in [Service Information](../User/Service_Information.md) for more precise scheduling information. |
| OK | The service check has up-to-date information, and the status meets or exceeds the criteria to be considered as acceptable operation. The criteria for each service check is unique to that check. |
| Warning | A service check detected a problem that is not yet serious but should be addressed in a timely fashion. It is possible that a Warning check will become critical if not addressed. |
| Critical | A service check has reported that a problem exists that is likely to affect production operation or has already caused some type of outage or loss of service. Service checks with this status should be addressed immediately. |
| Unknown | A service check was attempted; however, some other type of issue or limitation has prevented useful information from being processed. Usually an Unknown status will be accompanied by another service being in a Warning or Critical status. |
