---
title: "Actian Ingres"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Actian_Ingres.htm"
canonical_id: "actian-data-platform-actian-ingres"
---

## Actian Ingres

This topic describes Actian Ingres connector properties and connection details for reading data from an Actian Ingres database. This connector enables users to access a publicly accessible Actian Ingres database (hosted in the cloud, not on-premise).

If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for Actian Ingres](../DataQuality/Actian_Ingres.md) to [Define Source](../DataQuality/Define_Source.md).

- [Prerequisites](../DataQuality/Actian_Ingres.md)
- [Source Details for Actian Ingres](../DataQuality/Actian_Ingres.md)

- [Additional Information](../DataQuality/Actian_Ingres.md)

Prerequisites

Add the following Actian Data Platform IP addresses to the allow-list of your database host:

- 35.170.36.127
- 34.198.71.203

- 35.171.66.189
- 3.215.150.162

- 35.174.183.2
- 52.226.47.196/30

For information about different types of users and how to add grant them permissions, see [Manage Users](../User/Manage_Users.md) and [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).

Source Details for Actian Ingres

This topic provides properties and details needed to create a new connection and specify the source table using the Actian Ingres connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to Actian Ingres will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Name | Enter a unique name for the connection and click Continue. |
| Server Host Name | Specifies the URL or IP address of the server that hosts Actian Ingres. This property is mandatory. |
| Port | (Optional) Specifies the JDBC port number on which the JDBC connection can be established to the specified host/server. If the port number is not provided then the default port number is used. For example: II7. |
| Database Name | (Optional) Specifies the database name to connect to. |
| User Name | Specifies the user name for the specified database. This property is mandatory. |
| Password | Specifies the password for the specified database. This property is mandatory. |
| Additional Properties | (Optional) Specifies additional connection properties, in a comma separated format, that must be appended to the connection string. For example: rewriteBatchedStatements=true |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source table to be read on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Select a table from which data will be read. This property is mandatory. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_52.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

None
