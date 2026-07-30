---
title: "Actian Warehouse"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Actian_Warehouse.htm"
canonical_id: "actian-data-platform-actian-warehouse"
---

## Actian Warehouse

This topic describes Actian Warehouse connector properties and connection details for reading data from an Actian Warehouse. Actian Warehouse connector can also be used as a target connector.

!!! note "Note"

    The Actian Warehouse target connector has the following limitation: table row widths cannot exceed 255 KB.

- [Prerequisites](../Integrations/Actian_Warehouse.md)
- [Connection Details](../Integrations/Actian_Warehouse.md)

- [Source Details](../Integrations/Actian_Warehouse.md)
- [Additional Information](../Integrations/Actian_Warehouse.md)

Prerequisites

You must have an Actian warehouse account access and credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Select Actian Warehouse | Specifies the Actian warehouse that you want to connect to. If the selected warehouse is not running, you must start it. This is a mandatory property. |
| Connect to Actian Warehouse as current user | Specifies to login/access the warehouse with your logged in Actian Data Platform user account (SSO user).Deselect and specify the required username and password to login. By default, this property is selected. This is a mandatory property.For details about different types of users and how to add a new SSO user, see: [Manage Users](../User/Manage_Users_2.md).**Note:**The specified user must have the required permission to access the warehouse. |
| User name | Specifies the user name of the native user that has access to the Actian Warehouse. For details about how to add a new native user, see: [Manage Users](../User/Manage_Users_2.md).When the Connect to Actian Warehouse as current user property is deselected, the User name and Password properties are mandatory to establish a connection to Actian Warehouse. |
| Password | Specifies the password of the native user that has access to the Actian Warehouse. For details about how to add a new native user, see: [Manage Users](../User/Manage_Users_2.md).When the Connect to Actian Warehouse as current user property is deselected, the User name and Password properties are mandatory to establish a connection to Actian Warehouse. |

Source Details

Specify the following details to identify the source:

| Property | Description |
| --- | --- |
| Table Name | Specifies the required table from which the data will be read. This is a mandatory property. |

Additional Information

None
