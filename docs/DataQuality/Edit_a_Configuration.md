---
title: "Edit a Configuration"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Edit_a_Configuration.htm"
canonical_id: "actian-data-platform-edit-a-configuration"
---

## Edit a Configuration

This section describes how to edit a configuration in the Configuration Details page.

To edit configuration details

1. Click Manage, Configurations.

    The Configurations page displays the available configurations.

2. Click the configuration name that you want to edit.

    The Configuration Details page is displayed.

3. You can view and edit (where noted) the following information from this page:

| Properties | Editable | Description |
| --- | --- | --- |
| ![](images/Manage_25.png) | No | Click to execute the configuration. |
| ![](images/Manage_26.png) | No | Click to delete the configuration. |
| Configuration (name) | Yes | The configuration name. Hover over the configuration name and a pencil icon appears. Click the name or click the pencil icon to edit the name. Click![](images/Manage_27.png)to save your changes. |
| Description | Yes | The description text. Hover over the description text and a pencil icon appears. Click the description text or click the pencil icon to edit the description. Click![](images/Manage_28.png)to save your changes. |
| Status | Yes | Toggle this property between Active and Inactive. You can run the configuration only if it is set to Active. |
| Run Location | No | Specifies where the configuration executes: in the Cloud or on-premise with an agent. |
| Job Timeout | Yes | Specifies the number of minutes the job has to finish executing before job execution times out. If the timeout is set to 0, the Job Timeout will be ignored. |
| Scheduling | Yes | Specifies when the configuration executes. Click the edit icon, select a scheduling option for the configuration, and enter the settings for the selected option. Options are:•On Demand – Unscheduled; the configuration must be run manually.•Interval – Scheduled to run every x hours and x minutes.•Daily – Scheduled to run every x days at a specified time.•Weekly – Scheduled to run every week at a specified time on a specific day.•Monthly – Scheduled to run every month on a specific day every x months at a specified time.•Custom – Scheduled to run as per the specified schedule frequency.•Custom CRON Expression – Specify a cron expression using the Quartz Scheduler to schedule the job run. If necessary, please reference a [quick cron expression tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) provided by Quartz. |
| Log Level | Yes | Specifies the types of messages that will be included in job log files. The default setting is INFO. Click the edit icon, then select one of the following:•SEVERE – Logs errors that can cause the process execution to terminate if Break after first error is set.•WARNING – Logs messages about data truncation in a field, field name changes, loss of precision, or other issues.•INFO – (Default) Logs messages such as “Execution initialization...,” “Execution successful,” and whether the process execution was terminated.•DEBUG – All messages generated as a result of a TraceOn action and some other messages are logged at this level. In this case, the record number, first five fields of each record, and all the events are recorded. Note that when this option is enabled performance loss can occur due to the amount of information being logged. |
| Owner | No | Displays the email address of the configuration owner. The default owner is the configuration creator. |
| Change Log | No | Displays the created date and last modified date for the configuration. |
