---
title: "Edit Profile Schedule"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Edit_Profile_Schedule.htm"
canonical_id: "actian-data-platform-edit-profile-schedule"
---

## Edit Profile Schedule

The first time a profile is scheduled to execute its associated configuration is created. Thereafter, if the profile is edited, its associated configuration is not updated. To update the configuration, the profile must be recreated and scheduled.

To set a run-schedule for a profile

1. Click the Data Quality link at the top of the page.

    The Data Profiles page (see [Data Profiles Page](../DataQuality/Data_Profiles_Page.md)) displays the available profiles.

2. Click the desired profile.

    The Profile Details page is displayed.

3. Click the edit icon that is displayed for the Scheduling field.

    The Edit Profile Schedule page is displayed.

4. Select a frequency from the drop down menu:

    - On Demand – Unscheduled; the configuration must be run manually. See [Run a Profile Manually](../DataQuality/Run_a_Profile_Manually.md).

    - Interval – Scheduled to run every x hours and x minutes.

    - Daily – Scheduled to run every x days at a specified time.

    - Weekly – Scheduled to run every week at a specified time on a specific day.

    - Monthly – Scheduled to run every month on a specific day every x months at a specified time.

    - Custom – Scheduled to run as per the specified schedule frequency.

    - Custom CRON Expression – Specify a cron expression using the Quartz Scheduler to schedule the job run. If necessary, please reference a [quick cron expression tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) provided by Quartz.

5. Enter the settings for the chosen schedule type.
6. Click Save Schedule.

    The scheduling is updated on the Profile Details page.
