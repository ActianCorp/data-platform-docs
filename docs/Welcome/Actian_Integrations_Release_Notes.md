---
title: "Actian Integrations Release Notes"
product: "Actian Data Platform"
guide: "Welcome"
source_file: "Actian_Integrations_Release_Notes.htm"
canonical_id: "actian-data-platform-actian-integrations-release-notes"
---

## Actian Integrations Release Notes

These Release Notes are for the initial release of Actian Integrations as a Service on the Actian Data Platform.

| Integrations as a Service on the Actian Data Platform Features | Release Date |
| --- | --- |
| •[Actian Ingres - Via Agent](../Integrations/Actian_Ingres_-_Via_Agent.md)•[Actian Vector - Via Agent](../Integrations/Actian_Vector_-_Via_Agent.md)•[Actian Zen - Via Agent](../Integrations/Actian_Zen_-_Via_Agent.md)•[HCL Informix - Via Agent](../Integrations/HCL_Informix_-_Via_Agent.md)•[HCL OneDB - Via Agent](../Integrations/HCL_OneDB_-_Via_Agent.md)•[JDBC - Via Agent](../Integrations/JDBC_-_Via_Agent.md) | December 13, 2024 |
| •[Creating Integrations](../Integrations/Creating_Integrations.md)•[Managing Integrations](../Integrations/Managing_Integrations.md)•[Managing Configurations](../Integrations/Managing_Configurations.md)•[Create Connections](../Integrations/Create_Connections.md)•[Managing Connections](../Integrations/Design.md)•[Services (REST/SOAP)](../Integrations/Services_(REST_2fSOAP).md)•[Source and Target Connections](../Integrations/Source_and_Target_Connections.md) | September 6, 2023 |

This release includes new connectors via an agent, which is useful when an entity is located behind a firewall (hosted on-premise). These connectors are available if Connect via Agent is enabled when creating a new connection or integration.

!!! note "Note"

    When using an Agent to run an integration using the Connect via Agent option, ensure that you download the integration-agent-3.3.0-47 version or later, as previous versions are not supported.

For more information, see [Creating Integrations](../Integrations/Creating_Integrations.md) or [Create Connections](../Integrations/Create_Connections.md).

This release adds a new Integration Workspace, which distinguishes design and management navigation. This workspace offers a design interface where users can create integrations and establish connections. It also adds REST and SOAP API support, to simplify the integration of data from virtually any application or data source. For more information, see [Overview of the Design Environment](../Integrations/Overview_of_the_Design_Environment.md)

You can use the management environment to see a comprehensive view of integration health and agent performance. From this area you can manage configurations, create templates, and closely monitor agents, especially in hybrid deployment scenarios. There is also a dedicated dashboard for Run History, to assist with troubleshooting integrations. For more information, see [Managing Integrations](../Integrations/Managing_Integrations.md).

You can perform data transformations using drag-and-drop predefined functions. These functions enable you to reshape your data using predefined blocks, eliminating the need for complex scripting when moving data from source to target. For more information, see [Expression Builder](../Integrations/Expression_Builder.md)

This release includes many new connectors, including SOAP and REST API connectors, which assist in creating quick connections to support your data integration. We also expand our out-of-the-box connectors, which facilitates faster and more convenient cloud-based service connectivity. For more information, see [Create Connections](../Integrations/Create_Connections.md).
