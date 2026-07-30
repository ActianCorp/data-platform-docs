---
title: "Edit Integration Schedule"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Edit_Integration_Schedule.htm"
canonical_id: "actian-data-platform-edit-integration-schedule"
---

## Edit Integration Schedule

To edit an integration schedule

1. Click the Integrations link at the top of the page.

    The Integration Designs page displays the available integrations.

2. Click the desired Integration.

    The Integration details page is displayed.

3. Click the ![](images/DesignWorkspace_39.png) icon that is displayed for the Scheduling field.

    The Integration Schedule page is displayed.

4. Select a frequency from the drop down menu:

    - On Demand – Unscheduled; the integration must be run manually.

    - Interval – Scheduled to run every x hours and x minutes.

    - Daily – Scheduled to run every x days at a specified time.

    - Weekly – Scheduled to run every week at a specified time on a specific day.

    - Monthly – Scheduled to run every month on a specific day every x months at a specified time.

    - Custom – Scheduled to run as per the specified schedule frequency.

    - Custom CRON Expression – Specify a cron expression using the Quartz Scheduler to schedule the job run. If necessary, please reference a [quick cron expression tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) provided by Quartz.

5. Enter the settings for the chosen schedule type.
6. Click Save Schedule.
