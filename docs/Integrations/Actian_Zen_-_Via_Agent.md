---
title: "Actian Zen - Via Agent"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Actian_Zen_-_Via_Agent.htm"
canonical_id: "actian-data-platform-actian-zen-via-agent"
---

## Actian Zen - Via Agent

!!! warning "Important"

    **IMPORTANT!**When using an Agent to run an integration using the Connect via Agent option, ensure that you download the integration-agent-3.3.0-47 version or later, as previous versions are not supported.

This topic describes how to connect via agent using the Actian Zen connector. This option is useful for reading data from an Actian Zen database that is located behind a firewall (hosted on-premise). This connector is available if Connect via Agent is enabled when creating a new connection or integration.

Use this information when [Creating Integrations](../Integrations/Creating_Integrations.md) or creating [Connections](../Integrations/Connections.md).

Prerequisites

- Download the Actian Integration Agent. See [Download an Agent](../Integrations/Download_an_Agent.md).
- Install the Actian Integration Agent on your machine. See [Install an Agent](../Integrations/Install_an_Agent.md).

- Register the Actian Integration Agent with Actian Data Platform. See [Register an Agent](../Integrations/Register_an_Agent.md).
- Actian Zen ODBC driver must be installed on the same machine and location that the Actian Integration Agent is installed.

Connection Details

Specify the following details to define a connection:

| Option | Description |
| --- | --- |
| Name | Specify a descriptive name for the connection and click Continue. This property is mandatory. |
| Agent | Select the Actian Integration Agent that is installed on your system and is registered to the logged in user. (The agent must be registered to the logged in user, otherwise it will not work.)This property is mandatory. |
| Server Host Name | Specifies the host name on which the Actian Zen database is hosted.This property is mandatory. |
| Database Name | Specifies the name of the database to connect to.This property is mandatory. |
| User Name | (Optional) Specifies the user name for the specified database. |
| Password | (Optional) Specifies the password for the specified database. |
| Use Unicode Driver to connect to Actian Zen | (Optional) Specifies whether a unicode driver must be used for connecting to Actian Zen.The default value is False. |
| Test | Click to verify your connection, then click Save.The new connection is listed on the Connections page and selected as the source connection (if you’re in the process of creating an integration). |

The connection appears in the list of connections on the Connections page.

If creating an integration specify the following details to define the source to be read:

!!! note "Note"

    The following options are visible when [Creating Integrations](../Integrations/Creating_Integrations.md) and not when creating [Connections](../Integrations/Connections.md).

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Specifies the table from which the data will be read. This is a mandatory property. |
| Encoding | Specify the encoding of the source data. The default value is OEM.For information about supported encodings, see https://docs.actian.com/dataconnect/12.3/#page/User/Unicode_Character_Encodings.htm. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/DesignWorkspace_116.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. |

The integration appears in the list of integrations on the Integration Designs page.
