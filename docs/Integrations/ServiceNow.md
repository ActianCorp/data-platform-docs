---
title: "ServiceNow"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "ServiceNow.htm"
canonical_id: "actian-data-platform-servicenow"
---

## ServiceNow

The ServiceNow connector allows users to connect to a specific ServiceNow entity, or table, as a source within an integration. The integration facilitates visually mapping the source fields to the target fields, data type transformation, and (optional) data manipulation using the [Expression Builder](../Integrations/Expression_Builder.md).

- [Prerequisites](../Integrations/ServiceNow.md)
- [Connection Details](../Integrations/ServiceNow.md)

- [Source Details](../Integrations/ServiceNow.md)
- [Additional Information](../Integrations/ServiceNow.md)

Prerequisites

You must have ServiceNow account access and credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| ServiceNow Instance URL | Specifies the URL of the ServiceNow instance. For example, https://myorg.service-now.com/This is a mandatory property. |
| ServiceNow Username | Specifies the user name for connecting to the ServiceNow instance. This is a mandatory property. |
| ServiceNow Password | Specifies the password for connecting to the ServiceNow instance. This is a mandatory property. |

Source Details

Specify the following details to identify the source:

| Property | Description |
| --- | --- |
| Encoded Query String | (Optional) Specifies the ServiceNow URL-friendly query string which defines the criteria to filter the returned records. For more information, see the following link:[https://docs.servicenow.com/bundle/london-platform-user-interface/page/use/using-lists/concept/c_EncodedQueryStrings.html.](https://docs.servicenow.com/bundle/london-platform-user-interface/page/use/using-lists/concept/c_EncodedQueryStrings.html) |
| Table Name | Specifies the required table from which the data will be read.This is a mandatory property. |
| Use Display Values | Specifies whether to return string display values or raw data types and values. When this property is set to **True**, it returns string display values for all fields. If it is set to **False**, it returns the raw data types and values for all fields, including GUIDs of records in external tables.Default value is **True**.This is a mandatory property.**Note:**ServiceNow data will not be retrieved for Journal Input type fields (like comments and comments_and_work_notes in the incident table) when the Use Display Values property is set to False. The entries for these fields are stored in a separate table (sys_journal_field). Retrieving the data for these fields would require performing separate queries for each field of the type Journal Input which would have a significant performance impact on queries. The best way to include the contents of Journal Input fields is to set the source connector’s Use Display Values property to True. If that is not possible, then the map must be designed to perform the separate queries manually in events to set the values. |

Additional Information

None
