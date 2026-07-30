---
title: "Give Your Actian Warehouse Access to Azure Cloud Storage"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Give_Your_Actian_Warehouse_Access_to_Azure_Cloud.htm"
canonical_id: "actian-data-platform-give-your-actian-warehouse-access-to-azure-cloud"
---

## Give Your Actian Warehouse Access to Azure Cloud Storage

The Actian Data Platform authenticates through Azure Active Directory to read and ingest data from an Azure Blob storage account. You need to create a service principal client ID and provide its credentials to allow the Actian Data Platform access to the data. For more information, see [Set Up Microsoft Azure Access](../User/Set_Up_Microsoft_Azure_Access.md).

!!! note "Note"

    This section applies only when loading data from external tables. It is not necessary when loading using [Loading Delimited Text Data Using COPY VWLOAD (SQL)](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md).

To add client and tenant IDs to your Actian warehouse

1. From the Actian warehouse list, click the name of the warehouse whose credentials you want to set.

    The [Warehouse Details](../User/Warehouse_Details.md) page is displayed.

2. On the External Table Access row, click Set Storage Account Authentication.

    The External Table Access dialog appears.

3. Enter the following values:

    - Application (client) ID of the app (see [Step 2: Obtain the Application ID and the Directory ID](../User/Set_Up_Microsoft_Azure_Access.md))

    - Directory (tenant) ID of the app (see [Step 2: Obtain the Application ID and the Directory ID](../User/Set_Up_Microsoft_Azure_Access.md))

    - Client secret of the app (see [Step 4: Generate a Client Secret for the Application](../User/Set_Up_Microsoft_Azure_Access.md))

4. Click Save.

After setting external table credentials, they should be applied to the warehouse within a minute.

Your warehouse can now access your Azure data in the cloud, and you may now run queries against the data source using the [Query Editor](../User/Part_QueryEditor.md).
