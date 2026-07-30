---
title: "Actian X"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Actian_X.htm"
canonical_id: "actian-data-platform-actian-x"
---

## Actian X

This topic describes Actian X connector properties and connection details for reading data from an Actian X database. This connector enables users to access a publicly accessible Actian X database (hosted in the cloud, not on-premise).

If you’re [Creating Integrations](../Integrations/Creating_Integrations.md) or [Connections](../Integrations/Connections.md), use this information to [Define Source](../Integrations/Define_Source.md).

- [Prerequisites](../Integrations/Actian_X.md)
- [Connection Details](../Integrations/Actian_X.md)

- [Source Details](../Integrations/Actian_X.md)
- [Jira](../Integrations/Jira.md)

Prerequisites

The connection to Actian X is made via JDBC, so users must ensure that their Actian X instance is reachable from the outside world, or add the following Actian Data Platform IP addresses to the allow-list of their own database host:

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
| Server Host Name | Specifies the URL or IP address of the server that hosts Actian X. This is a mandatory property. |
| Port | (Optional) Specifies the JDBC port number on which the JDBC connection can be established to the specified host/server. If the port number is not provided then the default port number is used. For example: II7. |
| Database Name | (Optional) Specifies the database name to connect to. |
| User Name | Specifies the user name for the specified database. This is a mandatory property. |
| Password | Specifies the password for the specified database. This is a mandatory property. |
| Additional Properties | (Optional) Specifies additional connection properties, in a comma separated format, that must be appended to the connection string. For example: rewriteBatchedStatements=true |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Table Name | Specifies the required table from which the data will be read. This is a mandatory property. |

Additional Information

None
