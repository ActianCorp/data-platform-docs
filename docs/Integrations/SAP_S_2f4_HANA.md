---
title: "SAP S/4 HANA"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "SAP_S_2f4_HANA.htm"
canonical_id: "actian-data-platform-sap-s-2f4-hana"
---

## SAP S/4 HANA

The SAP S/4 HANA connector provides support for executing SAP S/4 HANA Cloud APIs using OData V2 or OData V4 interfaces.

The following features are supported by the SAP S/4 HANA connector:

- Provides support for connecting to a compliant SAP S/4 HANA Cloud service, discovering entity sets exposed by the services and importing entity definitions in the form of native JSON schemas.
- The connector supports fetching entities in two modes:

    - Managed mode: Fetches entities where the entity data complies with the imported schemas.

    - Raw Mode: Fetches entities where SAP S/4 HANA Cloud service is accessed directly, and the exchanged data is not constrained and validated by the adapter-provided schema.

!!! note "Note"

    The SAP S/4 HANA adapter extends the OData connector .

- [Prerequisites](../Integrations/SAP_S_2f4_HANA.md)
- [Connection Details](../Integrations/SAP_S_2f4_HANA.md)

- [Source Details](../Integrations/SAP_S_2f4_HANA.md)
- [Additional Information](../Integrations/SAP_S_2f4_HANA.md)

Prerequisites

None

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Root URL | Specifies the service root URL of the OData service. This is a mandatory property. |
| Base Headers | (Optional) Specifies the list of HTTP request headers in the format: key=value key=value...key=value. |
| Authentication Type | Specifies the type of authentication to use for accessing the OData service. This is a mandatory property. There are two types of authentications:•API Key(default): API Key is used.•Basic: Basic HTTP authentication with username and password is performed. |
| API Key | Specifies the API key value to use for authentication. This is a mandatory property. This property is enabled when Authentication Type is set to API key. |
| Username | Specifies the username value to use for basic authentication. This is a mandatory property. This property is enabled when Authentication Type is set to Basic. |
| Password | Specifies the password value to use for basic authentication. This is a mandatory property. This property is enabled when Authentication Type is set to Basic. |
| OData Version | (Optional) Specifies the version of OData to use for accessing the OData Service. There are two supported versions:•V4 (default)•V2 |

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

SAP S/4 HANA APIs on SAP.com require an API Key for authorization.

The SAP S/4 HANA connector provides an authentication type of API Key that uses this value. This property is available through the command -AK or -APIKEY. It may be helpful to define a Configuration Variable called SAPAPIKEY containing your key. You can then have multiple connections that referencing %SAPAPIKEY%while your key is stored in just one place.
