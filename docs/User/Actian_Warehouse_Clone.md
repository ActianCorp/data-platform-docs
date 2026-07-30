---
title: "Actian Warehouse Clone"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Actian_Warehouse_Clone.htm"
canonical_id: "actian-data-platform-actian-warehouse-clone"
---

# Actian Warehouse Clone

An Actian warehouse clone is a copy of the warehouse, including the data. The clone of the warehouse is fully rewrite-accessible and behaves as any other warehouse, post-creation. Actions on the clone do not have any impact on the source warehouse.

!!! note "Note"

    Only GCP and AWS warehouses are supported at this time. You can clone warehouses that are at version 630.0.27 (or later) or 620.1.43 (or later).

Benefits of the clone feature include:

- Backup: Can serve as an immediate backup for disaster recovery, large data transformations, or migration scenarios.
- Data Sharing: You can share the entire dataset with a partner or a different department without giving them access to the primary warehouse.

- Performance Testing: Customers can clone the entire warehouse to perform stress tests and other performance tests without affecting the production environment.
- Training Environments: New team members can train on a cloned warehouse, so they do not disrupt the primary warehouse.

- Audit and Compliance: Keeping a full snapshot of the warehouse at different points in time can help with auditing and regulatory compliance.

Note: Clones are only possible in the same account. Users will not be able to clone a warehouse from a different tenant even if they have the warehouse ID.
