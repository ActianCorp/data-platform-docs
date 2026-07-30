---
title: "Salesforce"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Salesforce.htm"
canonical_id: "actian-data-platform-salesforce"
---

## Salesforce

The Salesforce connector allows users to connect to a specific Salesforce entity, or table, as a source within an integration. The integration facilitates visually mapping the source fields to the target fields, data type transformation, and (optional) data manipulation using the [Expression Builder](../Integrations/Expression_Builder.md).

- [Prerequisites](../Integrations/Salesforce.md)
- [Connection Details](../Integrations/Salesforce.md)

- [Source Details](../Integrations/Salesforce.md)
- [Additional Information](../Integrations/Salesforce.md)

Prerequisites

You must have Salesforce account access and credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| User | Specifies the user name for connecting to Salesforce. This is a mandatory property. |
| Password | Specifies the password for connecting to Salesforce. This is a mandatory property. |
| Salesforce Token | Specifies the token provided by your administrator. This is a mandatory property. |
| Use Sandbox | Points to a sandbox instance of Salesforce for testing. Allows a user to easily switch between a sandbox server and a production server.Turn this property ON if you want to connect to Salesforce in the sandbox environment. This property is toggled OFF by default.For more information, refer to the sandbox-related topics within Salesforce documentation. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Table Name | Specifies the required table from which the data will be read. This is a mandatory property. |

Additional Information

None
