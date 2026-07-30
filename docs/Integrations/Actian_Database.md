---
title: "Actian Database"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Actian_Database.htm"
canonical_id: "actian-data-platform-actian-database"
---

## Actian Database

This topic describes Actian Database connector properties and connection details for reading data from an Actian Database.

When you create a new integration using the Actian Database connector as a source, a pre-configured list of Actian Database instances become available to choose from. Actian Database instances are hosted in Actian Data Platform.

- [Prerequisites](../Integrations/Actian_Database.md)
- [Connection Details](../Integrations/Actian_Database.md)

- [Source Details](../Integrations/Actian_Database.md)
- [Additional Information](../Integrations/Actian_Database.md)

Prerequisites

You must have Actian Warehouse account access and credentials.

If you access the database with your logged in account, your SSO user must have access to Actian Database, or you can connect to it using native user credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Select Actian Database | Specifies the Actian Database instance that you want to connect to. If the selected database is not running, go to Database Instances and start the database. This is a mandatory property. |
| Connect to Actian Warehouse as current user | Specifies to login/access the database with your logged in Actian Data Platform user account (SSO user). By default, this property is selected. This is a mandatory property.Deselect and specify the required username and password to login.For details about different types of users and how to add a new SSO user, see: [Manage Users](../User/Manage_Users_2.md).**Note:**The specified user must have the required permission to access the database instance. |
| User name | When the Connect to Actian Warehouse as current user property is deselected, the User name and Password properties are mandatory to establish a connection to an Actian Database instance. Provide the username of the native user that has access to the Actian Database instance.For details about how to add a new native user, see: [Manage Users](../User/Manage_Users_2.md). |
| Password | When the Connect to Actian Warehouse as current user property is deselected, the User name and Password properties are mandatory to establish a connection to an Actian Database instance. Provide the password of the native user that has access to the Actian Database instance.For details about how to add a new native user, see: [Manage Users](../User/Manage_Users_2.md). |

Source Details

Specify the following details to identify the source:

| Property | Description |
| --- | --- |
| Table Name | Specifies the required table from which the data will be read. This is a mandatory property. |

Additional Information

None
