---
title: "Create a New Database Instance"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Create_a_New_Database_Instance.htm"
canonical_id: "actian-data-platform-create-a-new-database-instance"
---

## Create a New Database Instance

Before you start loading or querying your data, you must create a database instance. To create an Actian database instance, you must specify its size in terms of Actian units (AUs). For more information, see [Actian Units](../DBaaS_User/Concepts_to_Understand.md).

!!! note "Note"

    By default, Actian warehouses are created using an Actian-managed encryption key for data at rest encryption.If you want to use your customer-managed external key management service for data encryption, you must set up key management before creating any warehouses. See [Set Up Key Management Service for Data Encryption](../DBaaS_User/Set_Up_Key_Management_Service_for_Data_Encryptio.md).

To create a new Actian database instance

1. On the [Actian Data Platform Database Instances Console](../DBaaS_User/Actian_Data_Platform_Database_Instances_Console.md), click the + New Databasebutton.

    The Create Database Instance dialog is displays.

2. Name the database instance.
3. Select the cloud environment for the database instance.

    If you are a Google-only user or platform user, your only choice will be Google Cloud.

4. Choose a region (geographical location) where the database instance is located.

    AWS: You must select the same AWS region where your S3 source data bucket is located. Loading data from an S3 bucket region different from the warehouse location is not supported and will result in an error during the loading process. ]

5. Select a database AU size (number of Actian units).

The AUs field is a universal measure of compute capacity (RAM and CPU) on the platform. The number of AUs determines the base configuration for an Ingres database instance via the cache_guideline parameter in cbf/config.dat as shown below. You can scale this up and down at any time via the user console.

- 1 AU = small/dev test = 128 max sessions
- 2 AU = medium= 256 max sessions

- 4 AU = medium/large = 512 max sessions
- 8 AU = huge = 1024 max sessions

6. Set an idle stop period.

    This is an amount of time after which the database will stop running if there is no query activity—from 0 hours, 15 minutes to 4 hours, 45 minutes. This saves on AU costs. For more information, see [Database Cost and Actian Units](../DBaaS_User/Concepts_to_Understand.md).

    Idle stop cannot be disabled in a non-production environment. For more information, see [Automatic Stopping of Idle Databases](../DBaaS_User/Automatic_Stopping_of_Idle_Databases.md).

    Google Cloud: To modify the idle stop period after the database is created, see [Modify Idle Stop Period](../DBaaS_User/Modify_Idle_Stop_Period.md). ]

7. Click Continue.
8. In the Create IP Allow List dialog, your current IP address and the Actian data integration services IP addresses are selected.

!!! note "Note"

    Actian data integration IPs are addresses for the Integration workers and engines that run integration jobs (see [Batch Data Loading](../DataLoading/BatchDataLoad.md)). Enabling these IP addresses allows these machines to run integrations. If the IPs are not allowed, integration jobs configured to connect to your database will fail unless the IPs are added.

9. (Optional) Enter one or more Allow Listed application IP addresses (machine addresses allowed to connect to the Actian database) with or without [CIDR (Classless Inter-Domain Routing) blocks](https://searchnetworking.techtarget.com/definition/CIDR):

    CIDR blocks 24–30 are accepted. 31 is not accepted, and 32 is the same as the IP address itself. Enter in the form XXX.XXX.XXX.XXX/##.

    a. Enter an IP address in the IP Address(es) field.

    You may enter multiple IP addresses by separating them with a comma.

    b. (Optional) Provide a text label for the IP address, for example, “QA Test Machine.”

    c. Click the ![](images/PlusButtonBlue.png) button or press Enter.

    The IP address(es) are added.

    d. Continue to add more IP addresses, if needed. Delete added IPs by clicking the X button for an IP:

!!! note "Note"

    To modify the list of Allow List IPs after database creation, see Update Allow List IP Addresses.

10. (Optional) The Import Ingres configuration files dialog enables you to specify local configurations to use on the Actian Data Platform to provide an on-premise equivalence needed for applications. You can include one or more of the following files from your existing installation:

    - config.dat

    - protect.dat (necessary with config.dat)

    - symbol.tbl

    Settings in these files override default settings, such as page sizes, caches, facility memory settings, and character sets.

11. Click Continue.
12. Enter the name of the database you want in the instance.

13. Click Create Database Instance.

    It takes about 5-10 minutes to create the instance and database.
