---
title: "Scale a Database"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "ScaleDatabase.htm"
canonical_id: "actian-data-platform-scaledatabase"
---

# Scale a Database

To schedule the scaling of a warehouse, see [Schedule a Database](../DBaaS_User/Schedule_a_Database.md).

After creating a warehouse, you can scale the number of AUs up or down to resize the warehouse.

!!! note "Note"

    You can scale up to any allowable amount, but you can only scale down to the initial allotment of AUs. For example, if your installation was initially alloted 2AUs, you can scale up to 4 AUs, but you cannot scale down below 2 AUs.

Scaling up can improve query performance, enables the warehouse to handle increasing workloads (more users, more data), and improves data loading. Scaling up, however, does not require existing data to be reloaded or reorganized to get performance from the additional compute to the warehouse.

A warehouse must be running to scale it.

!!! note "Note"

    Any scaling, up or down, restarts the warehouse. During scaling, the warehouse/database will be unavailable and any active users’ work will be affected. We recommend scaling during off hours.

To scale an Avalanche warehouse

1. On the Avalanche Warehouses page, click the name of the warehouse you want to scale. It must be in the Running state (see Restart a Warehouse or Restart a Database).

    The Warehouse Details page is displayed.

2. On the Compute row, click Scale.

    The Compute dialog opens.

3. Click the number of AUs you want to scale to.
4. Click Save and confirm the scaling.

    The warehouse enters the Scaling state, and the Compute field reflects the new number of AUs.

After scaling is completed, the warehouse enters the Running state.
