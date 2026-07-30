---
title: "Create a New Database Instance"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Create_a_New_Database_Instance.htm"
canonical_id: "actian-data-platform-create-a-new-database-instance"
---

## Create a New Database Instance

Before you start loading or querying your data, you must create a database. To create an Actian Data Platform database instance, you must specify its size in terms of Actian units (AUs). For more information, see [Actian Units](../User/Concepts_to_Understand.md).

To create a new Actian Data Platform database instance

1. On the Avalanche Database Instances Console, click the Create Database Instance button.

    The Create a New Database Instance dialog is displayed.

2. Name the database.
3. Select the cloud environment for the database.

    If you are a Google-only user or platform user, your only choice will be Google Cloud.

4. Choose a region (geographical location) where the database will be created.

    AWS: You must select the same AWS region where your S3 source data bucket is located. Loading data from an S3 bucket region different from the warehouse location is not supported and will result in an error during the loading process. ]

5. Select a database size (number of Actian units).

    For more information, see [Concepts to Understand](../User/Concepts_to_Understand.md).

6. Ensure that your current IP address and the Actian Data Platform data integration services IP addresses are selected.

    Actian Data Platform data integration IPs are addresses for the Integration workers and engines that run integration jobs (see [Batch Data Loading](../DataLoading/BatchDataLoad.md)). Enabling these IP addresses allows these machines to run integration [You can find information to set up and run your data integrations in Creating Integrations and Managing Integrations.](../DataLoading/BatchDataLoad.md), which target an Actian database. If the IPs are not allowed, integration jobs configured to connect to your database will fail unless the IPs are added.

7. (Optional) Enter one or more Allow Listed application IP addresses (machine addresses allowed to connect to the Actian database) with or without [CIDR (Classless Inter-Domain Routing) blocks](https://searchnetworking.techtarget.com/definition/CIDR):

    CIDR blocks 24–30 are accepted. 31 is not accepted, and 32 is the same as the IP address itself. Enter in the form XXX.XXX.XXX.XXX/##.

    a. Enter an IP address in the IP Address(es) field.

    You may enter multiple IP addresses by separating them with a comma.

    b. (Optional) Provide a text label for the IP address, for example, “QA Test Machine.”

    c. Click the ![](images/PlusButtonBlue.png) button or press Enter.

    The IP address(es) are added.

    d. Continue to add more IP addresses, if needed. Delete added IPs by clicking the X button for an IP:

![](images/MyLocalMachineIP.png)

!!! note "Note"

    To modify the list of Allow List IPs after database creation, see [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).

8. Set an idle stop period.

    This is an amount of time after which the database will stop running if there is no query activity—from 0 hours, 15 minutes to 4 hours, 45 minutes. This saves on AU costs. For more information, see [Warehouse or Database Cost and Actian Units](../User/Concepts_to_Understand.md).

    Idle stop cannot be disabled in a non-production environment. For more information, see [Automatic Stopping of Idle Warehouses or Databases](../User/Automatic_Stopping_of_Idle_Warehouses_or_Databas.md).

    Google Cloud: To modify the idle stop period after the database is created, see [Modify Idle Stop Period](../User/Modify_Idle_Stop_Period.md). ]

9. Click Create Database.

    New accounts are assigned a default maximum quota of Actian units. This quota differs, depending on how you got access to the Actian service. The number of units that contributes toward this quota is calculated by summing them across all your databases. Stopped databases also contribute toward this quota. You can request a quota increase by posting in the Actian Data Platform Community forum.

    The Database Instances console page is redisplayed, and notifications are shown. The database creates a new entry on the page.

!!! note "Note"

    For Google Cloud, it takes about 5 minutes to create a database.
