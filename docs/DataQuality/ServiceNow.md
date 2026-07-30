---
title: "ServiceNow"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "ServiceNow.htm"
canonical_id: "actian-data-platform-servicenow"
---

## ServiceNow

This topic describes ServiceNow connector properties and connection details for reading data from a ServiceNow entity or table. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for ServiceNow](../DataQuality/ServiceNow.md) to [Define Source](../DataQuality/Define_Source.md).

- [Prerequisites](../DataQuality/ServiceNow.md)
- [Source Details for ServiceNow](../DataQuality/ServiceNow.md)

- [Additional Information](../DataQuality/ServiceNow.md)

Prerequisites

You must have ServiceNow account access and credentials.

Source Details for ServiceNow

This topic provides properties and details needed to create a new connection and specify the source table using the ServiceNow connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to ServiceNow will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Name | Enter a unique name for the connection and click Continue. |
| ServiceNow Instance | Specifies the URL of the ServiceNow instance. For example, https://myorg.service-now.com/This property is mandatory. |
| User | Specifies the user name for connecting to the ServiceNow instance. This property is mandatory. |
| Password | Specifies the password for connecting to the ServiceNow instance. This property is mandatory. |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Select a table from which data will be read. This property is mandatory. |
| Encoded Query String | (Optional) Specifies the ServiceNow URL-friendly query string which defines the criteria to filter the returned records. For more information, see the following link:[https://docs.servicenow.com/bundle/london-platform-user-interface/page/use/using-lists/concept/c_EncodedQueryStrings.html.](https://docs.servicenow.com/bundle/london-platform-user-interface/page/use/using-lists/concept/c_EncodedQueryStrings.html) |
| Use Display Values | Specifies whether to return string display values or raw data types and values. When this property is set to **True**, it returns string display values for all fields. If it is set to **False**, it returns the raw data types and values for all fields, including GUIDs of records in external tables.Default value is **True**.This property is mandatory.**Note:**ServiceNow data will not be retrieved for Journal Input type fields (like comments and comments_and_work_notes in the incident table) when the Use Display Values property is set to False. The entries for these fields are stored in a separate table (sys_journal_field). Retrieving the data for these fields would require performing separate queries for each field of the type Journal Input which would have a significant performance impact on queries. The best way to include the contents of Journal Input fields is to set the source connector’s Use Display Values property to True. If that is not possible, then the map must be designed to perform the separate queries manually in events to set the values. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_61.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

None
