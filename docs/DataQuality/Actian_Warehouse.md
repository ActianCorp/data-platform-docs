---
title: "Actian Warehouse"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Actian_Warehouse.htm"
canonical_id: "actian-data-platform-actian-warehouse"
---

## Actian Warehouse

This topic describes connector properties and connection details for reading and writing data from/to an Actian Warehouse. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md):

    - See [Source Details for Actian Warehouse](../DataQuality/Actian_Warehouse.md) to [Define Source](../DataQuality/Define_Source.md).

    - See [Target Details for Actian Warehouse](../DataQuality/Actian_Warehouse.md) to [Define Targets](../DataQuality/Define_Targets.md).

When a new profile is created using the Actian Warehouse connector, users can select the desired warehouse instance from a pre-configured list hosted in Actian Data Platform.

!!! note "Note"

    The Actian Warehouse target connector has the following limitation: table row widths cannot exceed 255 KB.

- [Prerequisites](../DataQuality/Actian_Warehouse.md)
- [Source Details for Actian Warehouse](../DataQuality/Actian_Warehouse.md)

- [Target Details for Actian Warehouse](../DataQuality/Actian_Warehouse.md)
- [Supported Output Modes](../DataQuality/Actian_Warehouse.md)

- [Additional Information](../DataQuality/Actian_Warehouse.md)

Prerequisites

- You must have Actian Warehouse account access and credentials.
- The warehouse must be in a Running state in order to connect.

Source Details for Actian Warehouse

This topic provides information needed to create a new connection and specify the source table using the Actian Warehouse connector when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your source connection to Actian Warehouse will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

**IMPORTANT!**Creating an Actian Warehouse connection is not supported. However, you can use Actian Warehouse as a source and target connector when creating a profile and configure the connection information. See[Creating a Connection](../DataQuality/Creating_a_Connection.md).

Specify the following to define the source:

| Option | Description |
| --- | --- |
| Actian Warehouse | Select an Actian Warehouse. The warehouse must be in a Running state in order to connect. This property is mandatory.If the warehouse is not in a Running state, a popup message opens (at top right) which contains a Click here hyperlink. Click the link to start the warehouse. The warehouse status is shown in the Actian Warehouse field. States are:•Running - The warehouse is currently online.•Sleeping - The warehouse is currently offline.•Going to sleep - The warehouse is going offline.•Start Failed - An attempt to start the warehouse was unsuccessful and the warehouse is offline.•Starting - The warehouse is currently in the process of coming online.•Stop Failed - An attempt to stop the warehouse was unsuccessful.•Stopped - The warehouse is currently offline.•Delete Failed - An attempt to remove the warehouse was unsuccessful.•Deleting - The warehouse is currently in the process of being removed. |
| Connect to Actian Warehouse as current user | Enable this property to login to the selected warehouse using the credentials you used to login into the Actian Data Platform. Disable this property to login using alternate credentials. By default, this property is enabled.This property is useful when your Actian Data Platform credentials don’t grant access to a particular warehouse or table, and you have alternate credentials that do grant access to them.This property is mandatory.When this property is deselected, the User name and Password properties are mandatory:•User name - Specifies the user name for logging in to the Actian Warehouse.•Password - Specifies the password for logging in to the Actian Warehouse.For information about different types of users and how to add grant them permissions, see [Manage Users](../User/Manage_Users.md) and [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md). |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Select a table from which data will be read. This property is mandatory. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_50.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Target Details for Actian Warehouse

This topic describes information you must provide to write to a table in the Actian Warehouse, as well the options presented when defining the targets. Reference this information when you [Define Targets](../DataQuality/Define_Targets.md).

Note that there are two targets to be defined: the Pass Target (to write data that passes rule criteria) and the Fail Target (to write data that fails rule criteria).

Specify the following to define the Pass Target and the Fail Target:

| Option | Description |
| --- | --- |
| Select Warehouse | Select an Actian Warehouse. The warehouse must be in a Running state in order to connect. This property is mandatory.If the warehouse is not in a Running state, a popup message opens (at top right) which contains a Click here hyperlink. Click the link to start the warehouse. The warehouse status is shown in the Actian Warehouse field. States are:•Running - The warehouse is currently online.•Sleeping - The warehouse is currently offline.•Start Failed - An attempt to start the warehouse was unsuccessful and the warehouse is offline.•Starting - The warehouse is currently in the process of coming online.•Stop Failed - An attempt to stop the warehouse was unsuccessful.•Stopped - The warehouse is currently offline.•Delete Failed - An attempt to remove the warehouse was unsuccessful.•Deleting - The warehouse is currently in the process of being removed. |
| Connect to Actian Warehouse as current user | Enable this property to login to the selected warehouse using the credentials you used to login into the Actian Data Platform. Disable this property to login using alternate credentials. By default, this property is enabled.This property is useful when your Actian Data Platform credentials don’t grant access to a particular warehouse or table, and you have alternate credentials that do grant access to them.This property is mandatory.When the Connect to Actian Warehouse as current user property is deselected, the User name and Password properties are mandatory:•User name - Specifies the user name for logging in to the Actian Warehouse.•Password - Specifies the password for logging in to the Actian Warehouse.For information about different types of users and how to add grant them permissions, see [Manage Users](../User/Manage_Users.md) and [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md). |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Overwrite Existing Table | Select this option to store data in an existing Actian Warehouse table. All existing data in the table will be overwritten with new profile execution results.The Existing Table Name drop-down appears. Scroll through and select an existing table, or type in a text to filter table names that match the specified string.Preview the first 20 records - If the existing table contains data, click to verify that you’re connected to the correct table. The data for the selected table is displayed in the source data preview pane. Click ![](images/Design_51.png) and enter a string to search for a particular record. Click outside of the pane to close it.**Note:**Selecting an existing table option replaces the existing table. That is, the existing table is deleted and a new table with current schema is created. This may result in data loss. |
| Create New Table | Select this option to store data in a new table. The Create New Table field appears. Specify a new table name.Table names can contain only alphanumeric characters and must begin with an alphabetic character or an underscore (_). Names can contain (but cannot begin with) the following special characters: 0 through 9, #, @, and $. Names specified as delimited identifiers (in double quotes) can contain additional special characters. |
| Provide table access in Actian Query Editor | Select to grant table access to the dbadmingrp group. |

Supported Output Modes

Actian Warehouse connector supports the Replace output mode.

Additional Information

None
