---
title: "Creating Integrations"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Creating_Integrations.htm"
canonical_id: "actian-data-platform-creating-integrations"
---

## Creating Integrations

The Design environment provides for the creation and management of data integration designs. Data integrations enable the transformation and migration of data by visually mapping fields between a defined source and target.

Once an integration has been created, it can be run manually or scheduled for execution. When scheduled for execution it is deployed as a configuration (see [Managing Configurations](../Integrations/Managing_Configurations.md)) within the Manage environment (see [Manage](../Integrations/Manage.md)). All execution results and metadata related to the deployed configuration can be viewed and managed within the Design environment. To manage integrations, see [Managing Integrations](../Integrations/Managing_Integrations.md).

A new integration can be created by following the steps in our guided workflow. The steps include:

1. Describe – Name your integration.
2. Define Source – Provide the source connection details.

3. Define Target – Provide the target connection details.
4. Mapping – Map the source and target fields.

Navigation between pages of the guided workflow is possible by using the Back and Continue buttons at the bottom of the page. Navigating between pages will not clear data that has been entered by the user. When navigation to other pages is not possible, the button will fade in color and will not be active. You can exit the process anytime without saving any information by clicking Cancel.

To create a new integration

1. Click Integrations, Create Integration.

    The Create **Integration**page is displayed. It is a guided workflow that lets you create a simple integration by specifying the source and target connection details and mapping the fields.

2. Provide a name for the integration in the Integration Name field, then click Continue. The description field is optional.

    Integration names can contain alphanumeric characters and must begin with an alphanumeric character. Integration names can also contain but cannot begin with hyphen (-), underscore (_) and space.

3. Define the Source connection (see [Define Source](../Integrations/Define_Source.md)) and click Continue.

    The Define Target page is displayed.

4. Define the Target connection (see [Define Target](../Integrations/Define_Target.md)) and click Continue.

    The Source & Target Mapping page is displayed.

5. Map the Source and Target fields. See [Mapping](../Integrations/Mapping.md) and [Mapping Hierarchical Sources](../Integrations/Mapping_Hierarchical_Sources.md).
6. Perform one of the following actions:

| Actions | Description |
| --- | --- |
| Save & Close | Click this to save and close the Edit Integration page. Focus is directed back to the Integration Designs page from where you can search and list your newly created integration.Choose this option if you do not want to run the integration immediately. This is also useful if you have incomplete work and want to resume working later. You can run the integration later from the Integration Designs page. See [View Integration Details](../Integrations/View_Integration_Details.md). |
| Save & Schedule | Click this to save the integration and create a schedule for its execution.Choose this option to execute the integration based on a schedule. |
| Save & Run | Click this to save and run the integration.Choose this option if you want to execute the integration manually. When you use this option, no configuration (.jobConfig file) is generated. You can view the results from the Design, Run History page. See [View Integration Run History](../Integrations/View_Integration_Run_History.md). |

!!! warning "Important"

    **IMPORTANT!**When using an Agent to run an integration with Actian Warehouse as the target, make sure the IP address of the host machine where the Agent is installed is added to the Warehouse's allowed IP list. Without this, the integration will not run. See [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).
