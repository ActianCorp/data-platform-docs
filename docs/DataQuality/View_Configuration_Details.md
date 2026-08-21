---
title: "View Configuration Details"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "View_Configuration_Details.htm"
canonical_id: "actian-data-platform-view-configuration-details"
---

## View Configuration Details

The Configuration Details page displays information about a single configuration, and the last executed job. Use this page to edit a configuration.

!!! note "Note"

    The configuration must be in the Active state to run.

To view details about a configuration

1. Click Manage, Configurations.

    The Configurations page displays the available configurations.

2. Click the configuration of interest.

    The Configuration Details page displays information about the configuration. This page also provides details about the last executed job, such as the Job ID, its status, the execution start time, Total records processed, and Overall Pass/Fail summary. You can view and edit (where noted) the following information from this page (for details, see [Edit a Configuration](../DataQuality/Edit_a_Configuration.md)):

| Properties | Editable | Description |
| --- | --- | --- |
| ![](images/Manage_20.png) | No | Click to execute the configuration. |
| ![](images/Manage_21.png) | No | Click to delete the configuration. |
| Configuration | Yes | The configuration name. Hover over the configuration name and a pencil icon appears. Click the name or click the pencil icon to edit the configuration name. Click![](images/Manage_22.png)to save your changes. |
| Description | Yes | The description text. Hover over the description text and a pencil icon appears. Click the description text or click the pencil icon to edit the description. Click![](images/Manage_23.png)to save your changes. |
| Status | Yes | Toggle this property between Active and Inactive. You can run the configuration only if it is set to Active. |
| Run Location | No | Specifies where the configuration executes: in the Cloud or on-premise with an agent. |
| Job Timeout | Yes | Specifies the number of minutes the job has to finish executing before job execution times out. If the timeout is set to 0, the Job Timeout will be ignored. |
| Scheduling | Yes | This property displays the schedule for the configuration. Possible values are:<br>• On Demand – Unscheduled; the configuration must be run manually.<br>• Interval – Scheduled to run every x hours and x minutes.<br>• Daily – Scheduled to run every x days at a specified time.<br>• Weekly – Scheduled to run every week at a specified time on a specific day.<br>• Monthly – Scheduled to run every month on a specific day every x months at a specified time.<br>• Custom – Scheduled to run as per the specified schedule frequency.<br>• Custom CRON Expression – Specify a cron expression using the Quartz Scheduler to schedule the job run. If necessary, please reference a [quick cron expression tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) provided by Quartz. |
| Log Level | Yes | Specifies the types of messages that will be included in job log files. The default setting is INFO. Click the edit icon, then select one of the following:<br>• SEVERE – Logs errors that can cause the process execution to terminate if Break after first error is set.<br>• WARNING – Logs messages about data truncation in a field, field name changes, loss of precision, or other issues.<br>• INFO – (Default) Logs messages such as “Execution initialization...,” “Execution successful,” and whether the process execution was terminated.<br>• DEBUG – All messages generated as a result of a TraceOn action and some other messages are logged at this level. In this case, the record number, first five fields of each record, and all the events are recorded. Note that when this option is enabled performance loss can occur due to the amount of information being logged. |
| Owner | No | Displays the email address of the configuration owner. The default owner is the creator, but ownership can be transferred to another user. |
| Change Log | No | This property provides the created and modified dates for the configuration. |
