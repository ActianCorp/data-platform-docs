---
title: "Salesforce"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Salesforce.htm"
canonical_id: "actian-data-platform-salesforce"
---

## Salesforce

This topic describes Salesforce connector properties and connection details for reading data from a Salesforce entity or table. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for Salesforce](../DataQuality/Salesforce.md) to [Define Source](../DataQuality/Define_Source.md).

- [Prerequisites](../DataQuality/Salesforce.md)
- [Source Details for Salesforce](../DataQuality/Salesforce.md)

- [Additional Information](../DataQuality/Salesforce.md)

Prerequisites

You must have Salesforce account access and credentials.

Source Details for Salesforce

This topic provides properties and details needed to create a new connection and specify the source table using the Salesforce connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to Salesforce will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Name | Enter a unique name for the connection and click Continue. |
| User | Specifies the user name for connecting to Salesforce. This property is mandatory. |
| Password | Specifies the password for connecting to Salesforce. This property is mandatory. |
| Salesforce Token | Specifies the token provided by your administrator. This property is mandatory. |
| Use Sandbox | Specifies whether to point to a sandbox instance of Salesforce for testing. Allows a user to easily switch between a sandbox server and a production server.Turn this property ON if you want to connect to Salesforce in the sandbox environment. This property is OFF by default.For more information, refer to the sandbox-related topics within Salesforce documentation. |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Select a table from which data will be read. This property is mandatory. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_60.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

None
