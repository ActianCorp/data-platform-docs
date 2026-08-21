---
title: "Actian Vector - Via Agent"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Actian_Vector_-_Via_Agent.htm"
canonical_id: "actian-data-platform-actian-vector-via-agent"
---

## Actian Vector - Via Agent

!!! warning "Important"

    **IMPORTANT!**When using an Agent to run an integration using the Connect via Agent option, ensure that you download the integration-agent-3.3.0-47 version or later, as previous versions are not supported.

Connecting with Actian Vector via agent is useful when an Actian Vector database is located behind a firewall (hosted on-premise). This connector is available if Connect via Agent is enabled when creating a new connection or integration.

Use this information when [Creating Integrations](../Integrations/Creating_Integrations.md) or creating [Connections](../Integrations/Connections.md).

Actian Vector also supports connecting in the cloud which is useful when an Actian Vector database is publicly accessible. For information, see [Actian Vector](../Integrations/Actian_Vector.md).

Prerequisites

- Download the Actian Integration Agent. See [Download an Agent](../Integrations/Download_an_Agent.md).
- Install the Actian Integration Agent on your machine. See [Install an Agent](../Integrations/Install_an_Agent.md).

- Register the Actian Integration Agent with Actian Data Platform. See [Register an Agent](../Integrations/Register_an_Agent.md).
- Actian Client Runtime or Vector ODBC driver must be installed on the same machine and location that the Actian Integration Agent is installed.

Connection Details

Specify the following details to define a connection:

| Option | Description |
| --- | --- |
| Name | Specify a descriptive name for the connection and click Continue. This property is mandatory. |
| Agent | Select the Actian Integration Agent that is installed on your system and is registered to the logged in user. (The agent must be registered to the logged in user, otherwise it will not work.)This property is mandatory. |
| Connect Using | Select one of the following:<br>• DSN (Data Source Name) - Specifies to connect using the ODBC DSN that is configured on the installed Actian Integration Agent. The following properties are mandatory with this selection: Data Source Name, User Name and Password.<br>• Driver - Specifies the name of the driver to use to connect to the database. If no driver is specified, then the default driver is used. The following properties are mandatory with this selection: Server Host Name, User Name and Password (values for the Driver Name, Port, Database Name and Additional Properties are optional and if these are not specified the default values are used). |
| Data Source Name | Specifies the name of the DSN to use to connect to the database. The DSN name must be an accurate System DSN name. User DSNs will not work.This property is visible when DSN (Data Source Name) is selected for Connect Using. |
| User Name | Specifies the user name for the specified database. This property is mandatory. |
| Password | Specifies the password for the specified database. This property is mandatory. |
| Driver Name | (Optional) Specifies the name of the driver to use to connect to the database. If no driver is specified the default driver is used. |
| Server Host Name | Specifies the host name on which the Actian Vector database is hosted.This property is mandatory if Driver is selected for Connect Using. |
| Port | (Optional) Specifies the port number on the on the host that the ODBC DSN that connects to.This property is visible when Driver is selected for Connect Using. |
| Database Name | (Optional) Specifies the name of the ODBC DSN that is configured on the installed Actian Integration Agent to connect to.This property is visible when Driver is selected for Connect Using. |
| Additional Properties | (Optional) Specifies additional connection properties in a comma separated format which must be appended to the connection string. For example: SERVERTYPE=VECTOR;DATEALIAS=ansidateProperties which are not specified in the key=value format will be ignored.This property is visible when Driver is selected for Connect Using. |
| Test | Click to verify your connection, then click Save.The new connection is listed on the Connections page and selected as the source connection (if you’re in the process of creating an integration). |

The connection appears in the list of connections on the Connections page.

If creating an integration specify the following details to define the source to be read:

!!! note "Note"

    The following options are visible when [Creating Integrations](../Integrations/Creating_Integrations.md) and not when creating [Connections](../Integrations/Connections.md).

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Specifies the table from which the data will be read. This is a mandatory property. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/DesignWorkspace_115.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. |
