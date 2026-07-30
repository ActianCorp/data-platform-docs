---
title: "Oracle CRM on Demand"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Oracle_CRM_on_Demand.htm"
canonical_id: "actian-data-platform-oracle-crm-on-demand"
---

## Oracle CRM on Demand

The Oracle CRM on Demand connector allows users to connect to a specific Oracle CRM on Demand entity, or table, as a source within an integration. The integration facilitates visually mapping the source fields to the target fields, data type transformation, and (optional) data manipulation using the [Expression Builder](../Integrations/Expression_Builder.md).

- [Prerequisites](../Integrations/Oracle_CRM_on_Demand.md)
- [Connection Details](../Integrations/Oracle_CRM_on_Demand.md)

- [Source Details](../Integrations/Oracle_CRM_on_Demand.md)
- [Additional Information](../Integrations/Oracle_CRM_on_Demand.md)

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

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Server | Specifies the name of the Oracle CRM server to connect to. This is a mandatory property. |
| User | Specifies the user name for connecting to Oracle CRM. This is a mandatory property. |
| Password | Specifies the password for connecting to Oracle CRM. This is a mandatory property. |

Source Details

Specify the following details to identify the source:

| Property | Description |
| --- | --- |
| Table Name | Specifies the required table from which the data will be read. This is a mandatory property. |

Additional Information

None
