---
title: "Maintenance and Compliance"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Maintenance_and_Compliance.htm"
canonical_id: "actian-data-platform-maintenance-and-compliance"
---

## Maintenance and Compliance

Actian Data Platform is hosted in AWS, Google Cloud, and Azure data centers that are ISO 27001 certified. These cloud data centers provide a high level of physical security, including biometric access and 24/7 surveillance.

You can specify a geographical region for the creation of a warehouse. See [Create a New Warehouse](../User/Create_a_New_Warehouse.md).

Database-level log events are available within the warehouse. Security events and metadata are logged at the management plane level (see [The Actian Data Platform Virtual Private Cloud (VPC) Architecture](../Security/The_Actian_Data_Platform_Virtual_Private_Cloud_(.md)). These logs are provided upon request to support auditing requirements. No customer data is logged to the management plane and no passwords are logged anywhere. The management plane is maintained with rolling up-to-date patching and software.

The warehouse service instances are regularly patched within the maintenance window. The Actian Data Platform console is scanned with a PCI-approved scanning vendor (ASV). Additionally, the web UI is scanned for web application vulnerabilities and resolved quickly. The environment is monitored 24x7 by a global operations team. Current performance and uptime metrics are available at the [Actian Data Platform Customer Portal](https://communities.actian.com/s/) and through RSS feed.
