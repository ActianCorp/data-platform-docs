---
title: "Schedule a Configuration"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Schedule_a_Configuration.htm"
canonical_id: "actian-data-platform-schedule-a-configuration"
---

## Schedule a Configuration

You can schedule a configuration to execute in the Configuration Details page.

To schedule a configuration

1. Click Manage, Configurations.

    The Configurations page displays the available configurations.

2. Click the configuration of interest.

    The Configuration Details page displays information about the selected configuration.

3. Click the edit icon next toScheduling.

    The Edit Configuration Schedule page is displayed.

4. Select a frequency from the drop down menu:

    - On Demand – Unscheduled; the configuration must be run manually.

    - Interval – Scheduled to run every x hours and x minutes.

    - Daily – Scheduled to run every x days at a specified time.

    - Weekly – Scheduled to run every week at a specified time on a specific day.

    - Monthly – Scheduled to run every month on a specific day every x months at a specified time.

    - Custom – Scheduled to run as per the specified schedule frequency.

    - Custom CRON Expression – Specify a cron expression using the Quartz Scheduler to schedule the job run. If necessary, please reference a [quick cron expression tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) provided by Quartz.

5. Enter the settings for the chosen schedule type.
6. Click Save Schedule.

    The scheduling is updated on the Configuration Details page.
