---
title: "Edit Configuration Schedule"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Edit_Configuration_Schedule.htm"
canonical_id: "actian-data-platform-edit-configuration-schedule"
---

## Edit Configuration Schedule

To set a schedule for a configuration to run

1. Click Integrations, Manage, Configurations.

    The Configurations page lists the available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the name of the configuration you want to schedule.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click the edit icon that is displayed for the Scheduling field.

    The Edit Configuration Schedule page is displayed.

4. Select a frequency from the drop down menu:

    - On Demand – Unscheduled; the configuration must be run manually. See [Run a Configuration Manually](../Integrations/Run_a_Configuration_Manually.md).

    - Interval – Scheduled to run every x hours and x minutes.

    - Daily – Scheduled to run every x days at a specified time.

    - Weekly – Scheduled to run every week at a specified time on a specific day.

    - Monthly – Scheduled to run every month on a specific day every x months at a specified time.

    - Custom – Scheduled to run as per the specified schedule frequency.

    - Custom CRON Expression – Specify a cron expression using the Quartz Scheduler to schedule the job run. If necessary, please reference a [quick cron expression tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) provided by Quartz.

5. Enter the settings for the chosen schedule type.
6. Click Save Schedule.

    The scheduling is updated on the Configuration Details page.
