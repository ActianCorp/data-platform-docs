---
title: "Workflow Terms"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Workflow_Terms.htm"
canonical_id: "actian-data-platform-workflow-terms"
---

## Workflow Terms

Three terms are important to understand: integration, configuration, and job. Each term reflects a different integration state as you design, execute, and manage it.

## Integration

When you build and test an integration, it resides in the [Design](../Integrations/Design.md) environment. The Design environment provides for the creation and management of data integration designs. See [Creating Integrations](../Integrations/Creating_Integrations.md).

Data integrations enable the transformation and migration of data by visually mapping fields between a defined source and target.

If you need an integration that is very similar to an existing integration, consider duplicating the existing integration and revising it, rather than creating one from scratch. See [Duplicate Integration](../Integrations/Duplicate_Integration.md).

When you decide to save and schedule the integration, an associated configurationis deployed in the [Manage](../Integrations/Manage.md) environment. You then modify and execute the configuration, and monitor performance in the Manage environment.

## Configuration

Configurations reside in the [Manage](../Integrations/Manage.md) environment. The Manage environment provides for viewing and managing execution results, and metadata related to the deployed configuration. See [Managing Configurations](../Integrations/Managing_Configurations.md).

Configurations contain properties which specify how and when an integration will be executed. Properties for scheduling, logging levels, run location, job timeout, and configuration status can found by exploring the Configuration Details page. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

If you need a configuration that is very similar to an existing configuration, consider duplicating the existing configuration and revising it, rather than creating one from scratch.

Each time you run a configuration, an associated jobis generated.

## Job

Jobs are reports about the run results of the configurations you execute. For example, whether the run was successful, the run duration, and log file data. Jobs are not editable. You can view jobs in the Design, Run History page, and in the Manage, Run History page. See [View Configuration Jobs](../Integrations/View_Configuration_Jobs.md).

!!! note "Note"

    The Integrations console utilizes a RESTful interface. You can use the REST API for Integration Manager to change configuration options and automate the execution of your configurations.

See [Design](../Integrations/Design.md) and [Manage](../Integrations/Manage.md) for more information about tools and options in each environment.
