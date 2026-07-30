---
title: "Overview of Manage Environment"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Overview_of_Manage_Environment.htm"
canonical_id: "actian-data-platform-overview-of-manage-environment"
---

## Overview of Manage Environment

After you create and schedule a profile in the Design environment, use the Manage environment to edit, manage and execute its associated configuration, and to also monitor, investigate, and gain insight from job execution results.

When creating a profile in the Design environment, a configuration is automatically created when you (optionally) schedule the profile to execute. You then manage and edit the configuration associated with the profile in the Manage environment (see [Managing Configurations](../DataQuality/Managing_Configurations.md)).

The configuration specifies when and where the profile will be executed. A profile has only one associated configuration. Configurations can be edited (see [Edit a Configuration](../DataQuality/Edit_a_Configuration.md)).

!!! note "Note"

    If you edit the profile associated with a configuration you must recreate and schedule the profile to create a new configuration.

Each time a configuration executes a job is created. The job contains execution Pass/Fail results, and has several states. For example, Running, Queued (which indicates that the job is scheduled to execute), and Finished (see [Job Detail](../DataQuality/Run_History_for_all_Configurations.md)). A configuration, and a profile have many associated jobs. Jobs cannot be edited.

Aggregated job results (for both configurations and profiles) are shown from various perspectives in [Run History](../DataQuality/Run_History_2.md) displays. These displays are useful for gaining insight into whether execution results are improving, worsening, or remaining the same:

    - View configurations as a whole (see [Run History for all Configurations](../DataQuality/Run_History_for_all_Configurations.md)).

    - View a single configuration, rule or field (see [Run History for a Single Configuration](../DataQuality/Run_History_for_all_Configurations.md)).

    - View profiles as a whole (see [Run History for all Profiles](../DataQuality/Run_History_for_all_Profiles.md)).

    - View a single profile (see [View Profile Details](../DataQuality/Run_History_for_all_Profiles.md)).

The [Manage, Overview Page](../DataQuality/Manage__Overview_Page.md) (see below) opens by default in the Manage environment. Consider using this page as a dashboard for managing configurations, and also to investigate particular job results at a more granular perspective.

Summary of what users can do in the Manage environment:

- Edit, execute, schedule, and delete a configuration, and edit certain properties. See [Managing Configurations](../DataQuality/Managing_Configurations.md).
- View run history for all executed configurations. See [Run History for all Configurations](../DataQuality/Run_History_for_all_Configurations.md).

- View run history for a single configuration. See [Run History for a Single Configuration](../DataQuality/Run_History_for_all_Configurations.md).
- View execution results per job, rule or field. See [View Job Details](../DataQuality/Run_History_for_all_Profiles.md).

- View or download job log file. See [Download Log File](../DataQuality/Run_History_for_all_Configurations.md).
