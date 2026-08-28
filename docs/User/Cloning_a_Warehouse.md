---
title: "Cloning a Warehouse"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Cloning_a_Warehouse.htm"
canonical_id: "actian-data-platform-cloning-a-warehouse"
---

## Cloning a Warehouse

Cloning an Actian warehouse has the same implications as creating a new warehouse. You must specify the size of the warehouse in terms of Actian units (AUs). For more information, see [Actian Units](../User/Concepts_to_Understand.md).

!!! note "Note"

    Cloning a warehouse includes only the data from last backup.

To clone an Actian warehouse

1. On the Actian Data Platform Warehouses Console, choose a warehouse to clone, and either click the three buttons to the right of the warehouse, and choose Clone from the menu or click Create Clone from the Warehouse Details dialog.
2. Name the warehouse.

3. Select a warehouse size (number of Actian units).

    For more information, see [Concepts to Understand](../User/Concepts_to_Understand.md).

!!! note "Note"

    Include warehouse Schedules in the Clone is checked by default, which means the cloned warehouse will include any scheduled start, stop, or scaling events from the source warehouse. Make sure this is unchecked if you do not want these events associated with your cloned warehouse.

4. Set an Idle Action.

    You can choose Idle Stop or Idle Sleep. Both specify an amount of time after which the warehouse will stop running or sleep if there is no query activity within the specified idle time. This saves on AU costs.

    If you select Idle Stop, you must manually start or restart the warehouse. If you select Idle Sleep, the warehouse resumes as soon as a query is launched on the warehouse.

    For more information, see [Warehouse Cost and Actian Units](../User/Concepts_to_Understand.md).

    Idle stop cannot be disabled in a non-production environment. For more information, see [Automatic Stopping of Idle Warehouses](../User/Automatic_Stopping_of_Idle_Warehouses_or_Databas.md).

5. Ensure that your current IP address and the Actian Data Platform data integration services IP addresses are selected.

    Actian Data Platform data integration IPs are addresses for the Integration workers and engines that run integration jobs (see [Batch Data Loading](../DataLoading/BatchDataLoad.md)). Enabling these IP addresses allows these machines to run integration [You can find information to set up and run your data integrations in Creating Integrations and Managing Integrations.](../DataLoading/BatchDataLoad.md), which target an Actian warehouse. If the IPs are not allowed, integration jobs configured to connect to your warehouse will fail unless the IPs are added.

6. (Optional) Enter one or more Allow Listed application IP addresses (machine addresses allowed to connect to the Actian warehouse) with or without [CIDR (Classless Inter-Domain Routing) blocks](https://searchnetworking.techtarget.com/definition/CIDR):

    CIDR blocks 24–30 are accepted. 31 is not accepted, and 32 is the same as the IP address itself. Enter in the form XXX.XXX.XXX.XXX/##.

    a. Enter an IP address in the IP Address(es) field.

    You may enter multiple IP addresses by separating them with a comma.

    b. (Optional) Provide a text label for the IP address, for example, “QA Test Machine.”

    c. Click the ![](images/PlusButtonBlue.png) button or press Enter.

    The IP address(es) are added.

    d. Continue to add more IP addresses, if needed. Delete added IPs by clicking the X button for an IP:

![](images/MyLocalMachineIP.png)

!!! note "Note"

    To modify the list of Allow List IPs after warehouse creation, see [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).

    Google Cloud: To modify the idle stop period after the warehouse is created, see [Modify Idle Stop Period](../User/Modify_Idle_Stop_Period.md). ]

7. Click Finish.

    New accounts are assigned a default maximum quota of Actian units. This quota differs, depending on how you got access to the Actian service. The number of units that contributes toward this quota is calculated by summing them across all your warehouses. Stopped warehouses also contribute toward this quota. You can request a quota increase by posting in the Actian Data Platform Community forum.

    The Warehouses console page is redisplayed, and notifications are shown. The warehouse creates a new entry on the page.
