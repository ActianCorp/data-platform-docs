---
title: "Oracle CRM on Demand"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Oracle_CRM_on_Demand.htm"
canonical_id: "actian-data-platform-oracle-crm-on-demand"
---

## Oracle CRM on Demand

This topic describes Oracle CRM on Demand connector properties and connection details for reading data from an Oracle CRM on Demand entity or table. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for Oracle CRM on Demand](../DataQuality/Oracle_CRM_on_Demand.md) to [Define Source](../DataQuality/Define_Source.md).

- [Prerequisites](../DataQuality/Oracle_CRM_on_Demand.md)
- [Source Details for Oracle CRM on Demand](../DataQuality/Oracle_CRM_on_Demand.md)

- [Additional Information](../DataQuality/Oracle_CRM_on_Demand.md)

Prerequisites

You must do the following:

1. Obtain the Oracle CRM On Demand Server URL, User ID, and Password.
2. Log in to Oracle CRM On Demand.

3. Enable REST API support in Oracle CRM On Demand. To do this:

    a. Click **Admin** > **User Management** **and** **Access Controls** > **Role Management**.

    b. Click **Edit**for the Administrator role, then from **Role Management Wizard** for the Administrator, click the **Step 4 Privileges** tab.

    c. Enable the **Integration: Restful Services** category.

4. Enable access rights to manipulate objects and child objects in Oracle CRM On Demand. To do this:

    a. Click **Admin** > **User Management and** **Access Controls** > **Access Profiles**.

    b. In the **Access Profiles** window, click **Edit for the Full Profile**.

    c. Click the **Step 2 Specify Access Levels** tab.

    d. Change the access level for each record type you with to interact with.

Source Details for Oracle CRM on Demand

This topic provides properties and details needed to create a new connection and specify the source table using the Oracle CRM on Demand connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to Oracle CRM on Demand will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Name | Enter a unique name for the connection and click Continue. |
| Server | Specifies the name of the Oracle CRM server to connect to. This property is mandatory. |
| User | Specifies the user name for connecting to Oracle CRM. This property is mandatory. |
| Password | Specifies the password for connecting to Oracle CRM. This property is mandatory. |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Select a table from which data will be read. This property is mandatory. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_59.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

None
