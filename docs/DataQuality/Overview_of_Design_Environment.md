---
title: "Overview of Design Environment"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Overview_of_Design_Environment.htm"
canonical_id: "actian-data-platform-overview-of-design-environment"
---

## Overview of Design Environment

Use the Design environment to establish a connection, create, test, schedule and execute data profiles, and view profile execution results.

To establish a connection, you can either choose from a list of connectors (see [Source and Target Connections](../DataQuality/Source_and_Target_Connections.md)), establish a new connection (see [Creating a Connection](../DataQuality/Creating_a_Connection.md)), or utilize an existing one (see [Define Source](../DataQuality/Define_Source.md)).

To create a data profile you create a source (see [Define Source](../DataQuality/Define_Source.md)), create data quality rules (see [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md)), and define a target (see [Define Targets](../DataQuality/Define_Targets.md)). Data isn’t persisted until the target tables are defined.

The data quality rules can be configured to enforce specific conditions or values. When a rule is applied to a specific field in a profile, the data in that field is evaluated against the condition or value within the rule. After processing is complete, each value from the source field is categorized as either valid or invalid. Valid data is written to the Pass target, while invalid data is written to the Fail target.

Profile rules can be added to a profile manually (see [Add Rule from Rule Set](../DataQuality/Add_Rule_from_Rule_Set.md)), or using the [Inspect & Recommend Rules](../DataQuality/Inspect___Recommend_Rules.md) option.

During profile design profiles can be executed manually (see [Run a Profile Manually](../DataQuality/Run_a_Profile_Manually.md)), or set to execute after any rule change (add, remove, edit, disable, or enable a rule in the profile). Consider executing a profile manually if the source dataset is large and requires a lot of processing time (see [Run a Profile Manually](../DataQuality/Run_a_Profile_Manually.md)). If the source dataset is smaller, consider enabling the [Run profile after every rule update](../DataQuality/Define_Rules_and_Analyze_Results.md) option so you can automatically get updated results and insights.

You can also test and adjust rules using a subset of your source data, or “[Sample Size](../DataQuality/Define_Rules_and_Analyze_Results.md)”. This can be helpful when your source dataset is large and you want to shorten processing time (see [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md)). Once the profile design has been tested and validated, the target tables can be defined in the Targets page. Profile execution from the Targets page will cause the profile rules to be executed against the entire dataset (rather than a Sample Size). The profile can be revised if desired (see [Edit a Profile](../DataQuality/Edit_a_Profile.md)).

Profile execution results, such as Pass/Fail count and execution duration time, are contained in jobs. Each time a profile is executed a job is created. Jobs cannot be edited. Aggregated job results for profiles are shown in the [Run History for all Profiles](../DataQuality/Run_History_for_all_Profiles.md) page. Job results for a single profile are shown in the Profile Details page (see [View Profile Details](../DataQuality/View_Profile_Details.md)).

Optionally, you can schedule a profile to execute at regular intervals. When a profile is scheduled to execute a configuration is automatically created for the profile. The configuration specifies when and where the profile executes. You then manage and edit the configuration associated with the profile (see [Managing Configurations](../DataQuality/Managing_Configurations.md)), and monitor execution results in the [Manage](../DataQuality/Manage.md) environment (see [Run History for all Configurations](../DataQuality/Run_History_for_all_Configurations.md) and [Run History for a Single Configuration](../DataQuality/Run_History_for_all_Configurations.md)). You can also interact with trend graphs which trace job results over a selected period in the [Manage, Overview Page](../DataQuality/Manage__Overview_Page.md).

!!! note "Note"

    Edits made to a profile after the configuration is created are not updated in the configuration. To update the configuration, recreate the profile.

Summary of what users can do in the Design environment:

- Create a connection. See [Creating a Connection](../DataQuality/Creating_a_Connection.md). See also:

    - [Source and Target Connections](../DataQuality/Source_and_Target_Connections.md)

    - [Define Source](../DataQuality/Define_Source.md)

- Create a data profile. See [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md). See also:

    - [Describe Data Profile](../DataQuality/Describe_Data_Profile.md)

    - [Define Source](../DataQuality/Define_Source.md)

    - [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md). See also:

        - [Add Rule from Rule Set](../DataQuality/Add_Rule_from_Rule_Set.md)

        - [Inspect & Recommend Rules](../DataQuality/Inspect___Recommend_Rules.md)

        - [View Source DataSet](../DataQuality/Define_Rules_and_Analyze_Results.md)

        - Set [Sample Size](../DataQuality/Define_Rules_and_Analyze_Results.md).

    - [Define Targets](../DataQuality/Define_Targets.md)

- Execute a profile. There are three ways to execute a profile. See:

    - [Run profile after every rule update](../DataQuality/Define_Rules_and_Analyze_Results.md)

    - [Run a Profile Manually](../DataQuality/Run_a_Profile_Manually.md)

    - [Define Targets](../DataQuality/Define_Targets.md) to execute from the Targets page.

- View job execution results. See [Run History for all Profiles](../DataQuality/Run_History_for_all_Profiles.md). See [View Profile Details](../DataQuality/View_Profile_Details.md) for a single profile.
- Edit a profile. See [Managing a Data Profile](../DataQuality/Managing_a_Data_Profile.md).

- Learn about Profiler Rules. See [Rule and Parameter Reference](../DataQuality/Rule_and_Parameter_Reference.md).

The [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) page (see below) opens by default in the Design environment. You can edit, schedule, duplicate, execute and delete profiles from this page.
