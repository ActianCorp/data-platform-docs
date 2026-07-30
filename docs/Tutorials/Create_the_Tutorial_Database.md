---
title: "Create the Tutorial Database"
product: "Actian Data Platform"
guide: "Tutorials"
source_file: "Create_the_Tutorial_Database.htm"
canonical_id: "actian-data-platform-create-the-tutorial-database"
---

## Create the Tutorial Database

Before you start loading or querying your data, you must create a database.

To create a new Actian database

1. On the [Actian Data Platform Database Instances Console](../Tutorials/Actian_Data_Platform_Database_Instances_Console.md), click the Create Warehouse button.

    The Create a New Warehouse dialog is displayed.

2. Name the warehouse **Tutorial**.
3. Select the cloud environment for the warehouse.

4. Choose a region (geographical location) where the warehouse will be created.

    AWS: If you are using AWS, you must select the same AWS region where your S3 source data bucket is located. Loading data from an S3 bucket region different from the warehouse location is not supported and will result in an error during the loading process. ]

5. Select a warehouse size (number of Actian units): **2 AUs**.
6. Enter one or more Allow Listed application IP addresses (machine addresses allowed to connect to the Actian warehouse).

    a. Enter your local IP address in the IP Address(es) field.

    You may enter multiple IP addresses by separating them with a comma.

    b. (Optional) Provide a text label for the IP address, for example, “My Local Machine.”

    c. Click the ![](images/PlusButtonBlue.png) button or press Enter.

    The IP address(es) are added.

7. Set an idle stop period.

    This is an amount of time after which the warehouse will stop running if there is no query activity—from 1 hour to 4 hours, 45 minutes. This saves on AU costs.

8. Click Create Warehouse.

    The Warehouses console page is redisplayed, and notifications are shown. The warehouse creates a new entry on the page.

!!! note "Note"

    For AWS and Azure, it takes 20 minutes or longer to create a warehouse, depending on its size.

| Next Step![](images/getting_started_green_arrow.png) | Go to [Actian Data Platform Database Instances Console](../Tutorials/Actian_Data_Platform_Database_Instances_Console.md). |
| --- | --- |
