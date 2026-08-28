---
title: "Scale a Warehouse"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "ScaleWarehouse.htm"
canonical_id: "actian-data-platform-scalewarehouse"
---

# Scale a Warehouse

To schedule the scaling of a warehouse, see [Schedule a Warehouse](../User/Schedule_a_Warehouse.md).

After creating a warehouse, you can scale the number of AUs up or down to resize the warehouse.

!!! note "Note"

    You can scale up to any allowable amount, but you can only scale down to the initial allotment of AUs. For example, if your installation was initially alloted 2AUs, you can scale up to 4 AUs, but you cannot scale down below 2 AUs.

The workload size (S, M, L) comes with a preset AU range for each warehouse. Determine which workload size is best for your needs, and specify the AUs within the preset AU range. You can then scale the AU size to any size within the valid range of your workload size without a restart.

Scaling up can improve query performance, enables the warehouse to handle increasing workloads (more users, more data), and improves data loading. Scaling up, however, does not require existing data to be reloaded or reorganized to get performance from the additional compute to the warehouse.

Dynamic scaling enables warehouses to scale up or down in size without a restart. This enables you to adjust resources available to a warehouse without interrupting workloads. This feature is only available in a 620.x or above warehouse. Any existing 610.x-based warehouses need to upgrade to enable this new feature.

Dynamic scaling features include:

- Dynamic scaling takes less time to complete then an off-line scaling
- In progress queries and transactions must complete before the dynamic scaling operation starts

- New queries cannot start until the scaling completes
- After scaling completes, existing sessions reconnect

Note: Upgrading your warehouse to enable dynamic scaling requires a support ticket. New warehouses use 620.x warehouses by default.

A warehouse must be running to scale it.

!!! note "Note"

    If you are running a 610.x-based warehouse, any scaling, up or down, takes the warehouse off-line and restarts the warehouse. During an off-line scaling, the warehouse will be unavailable and any active users’ work will be affected. If you are doing an off-line scaling, we recommend scaling during off hours.

To scale an Actian warehouse

1. On the Actian Warehouses page, click the name of the warehouse you want to scale. It must be in the Running state (see [Restart a Warehouse](../User/Restart_a_Warehouse.md)).

    The [Warehouse Details](../User/Warehouse_Details.md) page is displayed.

2. On the Compute row, click Scale.

    The Compute dialog opens.

3. Click the number of AUs you want to scale to.
4. Click Save and confirm the scaling.

    The warehouse enters the Scaling state, and the Compute field reflects the new number of AUs.

After scaling is completed, the warehouse enters the Running state.
