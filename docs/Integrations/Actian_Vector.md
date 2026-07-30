---
title: "Actian Vector"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Actian_Vector.htm"
canonical_id: "actian-data-platform-actian-vector"
---

## Actian Vector

This topic describes Actian Vector connector properties and connection details for reading data from an Actian Vector database. This connector enables users to access a publicly accessible Actian Vector database (hosted in the cloud, not on-premise).

If you’re [Creating Integrations](../Integrations/Creating_Integrations.md) or [Connections](../Integrations/Connections.md), use this information to [Define Source](../Integrations/Define_Source.md).

Actian Vector also supports connecting via agent. This option is useful when an Actian Vector database is located behind a firewall (hosted on-premise). For information, see [Actian Vector - Via Agent](../Integrations/Actian_Vector_-_Via_Agent.md).

- [Prerequisites](../Integrations/Actian_Vector.md)
- [Connection Details](../Integrations/Actian_Vector.md)

- [Source Details](../Integrations/Actian_Vector.md)
- [Additional Information](../Integrations/Actian_Vector.md)

- [Actian Vector - Via Agent](../Integrations/Actian_Vector_-_Via_Agent.md)

Prerequisites

The connection to Actian Vector is made via JDBC, so users must ensure that their Actian Vector instance is publicly accessible, or add the following Actian Data Platform IP addresses to the allow-list of their own database host:

- 35.170.36.127
- 34.198.71.203

- 35.171.66.189
- 3.215.150.162

- 35.174.183.2
- 52.226.47.196/30

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Server Host Name | Specifies the URL or IP address of the server that hosts Actian Vector. This is a mandatory property. |
| Port | (Optional) Specifies the JDBC port number on which the JDBC connection can be established to the specified host/server. If the port number is not provided then the default port number is used. For example: II7. |
| Database Name | (Optional) Specifies the database name to connect to. |
| User Name | Specifies the user name for the specified database. This is a mandatory property. |
| Password | Specifies the password for the specified database. This is a mandatory property. |
| Additional Properties | (Optional) Specifies additional connection properties, in a comma separated format, that must be appended to the connection string. For example: rewriteBatchedStatements=true |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Table | Specifies the required table from which the data will be read. This is a mandatory property. |

Additional Information

None
