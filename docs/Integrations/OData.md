---
title: "OData"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "OData.htm"
canonical_id: "actian-data-platform-odata"
---

## OData

The OData (Open Data Protocol) connector provides support for performing read and write operations on data sources that expose OData interface.

- [Prerequisites](../Integrations/OData.md)
- [Connection Details](../Integrations/OData.md)

- [Source Details](../Integrations/OData.md)
- [Additional Information](../Integrations/OData.md)

Prerequisites

None

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Root URL | Specifies the service root URL of the OData service. This is a mandatory property. |
| Base Headers | (Optional) Specifies the list of HTTP request headers in the format: key=value key=value...key=value. |
| Authentication Type | Specifies the type of authentication to use for accessing the OData service. This is a mandatory property. There are two types of authentications:<br>• None (default): No authentication is performed.<br>• Basic: Basic HTTP authentication with username and password is performed. |
| Username | Specifies the username value to use for basic authentication. This is a mandatory property. This property is enabled when Authentication Type is selected to Basic. |
| Password | Specifies the password value to use for basic authentication. This is a mandatory property. This property is enabled when Authentication Type is selected to Basic. |
| OData Version | (Optional) Specifies the version of OData to use for accessing the OData Service. There are two supported versions:<br>• V4 (default)<br>• V2 |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Entity Set | Specifies the entity set in the service on which to perform the data operation. This is a mandatory property. |
| Read Mode | Specifies the read mode of operation. This is a mandatory property. It has two possible values: Managed (default) and Raw. If Read Mode is set to Managed, it generates schema directly. |
| Headers | (Optional) Specifies the custom request headers. It includes the list of HTTP headers which is added to any headers specified in the base property for the connection. |
| Resource Path | (Optional) Specifies the addressing entries for resource path. |
| Format | (Optional) Specifies the media type format of the data. |
| Filter | (Optional) Specifies the filter expression to apply when fetching the data. |
| Top | (Optional) Specifies the limit for how many values to fetch. |
| Skip | (Optional) Specifies the number of values to skip from the beginning before fetching. |
| Order By | (Optional) Specifies an expression for determining what values are used to order the collection of entries. |
| Select | (Optional) Selects the required field or expression. |
| Select Source Tables | (Optional) Select which arrays of objects in the JSON data you wish to map to tables in the target. |

Additional Information

None
