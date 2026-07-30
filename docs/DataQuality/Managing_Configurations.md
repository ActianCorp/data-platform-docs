---
title: "Managing Configurations"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Managing_Configurations.htm"
canonical_id: "actian-data-platform-managing-configurations"
---

## Managing Configurations

A configuration is a set of properties that specify when, where, and how a profile executes. When a profile is scheduled to execute, a configuration is automatically created for the profile.

!!! note "Note"

    If you edit the profile associated with a configuration you must recreate and schedule the profile to create a new configuration.

Profiles are scheduled to execute in the Design environment. The schedule can be revised in the Manage Environment.

!!! note "Note"

    A configuration is not created when a profile is executed within the Design environment.

When a configuration executes, the associated profile executes. When execution is completed, runtime metrics for all configurations are available for review in [Run History](../DataQuality/Run_History_2.md). To view runtime metrics for a single configuration, see [Run History for a Single Configuration](../DataQuality/Run_History_for_all_Configurations.md).

All your configurations are displayed on the Configurations page. You can open the Configurations page by clicking Manage, Configurations. For complete details about this page, see [Search Configurations](../DataQuality/Search_Configurations.md).

The following actions can be performed on this page:

- [Search Configurations](../DataQuality/Search_Configurations.md)
- [View Configuration Details](../DataQuality/View_Configuration_Details.md)

- [Schedule a Configuration](../DataQuality/Schedule_a_Configuration.md)
- [Run a Configuration](../DataQuality/Run_a_Configuration.md)

- [Edit a Configuration](../DataQuality/Edit_a_Configuration.md)
- [Delete a Configuration](../DataQuality/Delete_a_Configuration.md)

To view configuration execution results, see [Run History for a Single Configuration](../DataQuality/Run_History_for_all_Configurations.md).
