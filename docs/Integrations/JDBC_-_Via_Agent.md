---
title: "JDBC - Via Agent"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "JDBC_-_Via_Agent.htm"
canonical_id: "actian-data-platform-jdbc-via-agent"
---

## JDBC - Via Agent

!!! warning "Important"

    **IMPORTANT!**When using an Agent to run an integration using the Connect via Agent option, ensure that you download the integration-agent-3.3.0-47 version or later, as previous versions are not supported.

This topic describes how to connect via agent using the JDBC connector. This option is useful for reading data from a database that supports connectivity using JDBC. Connecting via agent is useful when a database is located behind a firewall (hosted on-premise). This connector is available if Connect via Agent is enabled when creating a new connection or integration.

Use this information when [Creating Integrations](../Integrations/Creating_Integrations.md) or creating [Connections](../Integrations/Connections.md).

Prerequisites

- Download the Actian Integration Agent. See [Download an Agent](../Integrations/Download_an_Agent.md).
- Install the Actian Integration Agent on your machine. See [Install an Agent](../Integrations/Install_an_Agent.md).

- Register the Actian Integration Agent with Actian Data Platform. See [Register an Agent](../Integrations/Register_an_Agent.md).
- The JDBC driver jar of the database you intend to connect to should be available/obtained from the database provider/distributor and this driver jar file should be present on the same machine where Actian Integration Agent is installed.

Connection Details

Specify the following details to define a connection:

| Option | Description |
| --- | --- |
| Name | Specify a descriptive name for the connection and click Continue. This property is mandatory. |
| Agent | Select the Actian Integration Agent that is installed on your system and is registered to the logged in user. (The agent must be registered to the logged in user, otherwise it will not work.)This property is mandatory. |
| JDBC URL | Specifies the complete JDBC URL for the database that is recognized by the driver.This property is mandatory. |
| User Name | (Optional) Specifies the user name for the specified database. |
| Password | (Optional) Specifies the password for the specified database. |
| Additional Properties | (Optional) Specifies additional connection properties, in a comma separated format, which must be appended to the connection string. For example: rewriteBatchedStatements=trueProperties which are not specified in the key=value format will be ignored. |
| Driver Jar Location | Specifies the path of the driver .jar file from which to load the JDBC driver. This path can be a folder on your file system that contains the driver jar file or the full path to the .jar file. It is recommended to provide the name of the .jar file with the full path. The path provided should be accessible by the logged in user who installed and is using the agent. Otherwise the “No suitable driver found” error is returned.This property is mandatory. |
| Driver Class | Specifies the fully qualified Java class name of the JDBC driver.This property is mandatory. |
| Test | Click to verify your connection, then click Save.The new connection is listed on the Connections page and selected as the source connection (if you’re in the process of creating an integration). |

The connection appears in the list of connections on the Connections page.

If creating an integration specify the following details to define the source to be read:

!!! note "Note"

    The following options are visible when [Creating Integrations](../Integrations/Creating_Integrations.md) and not when creating [Connections](../Integrations/Connections.md).

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Table Name | Specifies the table from which the data will be read. This is a mandatory property. |
| Batch Size | (Optional) Specifies the number of source records the connector caches before processing them. The default value is 2000.**Tip...**When a large number of records are to be transformed, setting Batch Size to a higher value can help improve the speed of the job execution (provided that ample system resources, such as memory/RAM, are available to the machine where the agent is installed.) |
| Fetch Size | (Optional) Specifies the number of rows to retrieve from the database per server request. The default value is 1000. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/DesignWorkspace_119.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. |

The integration appears in the list of integrations on the Integration Designs page.
