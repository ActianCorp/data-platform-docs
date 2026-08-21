---
title: "View Integration Run History"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "View_Integration_Run_History.htm"
canonical_id: "actian-data-platform-view-integration-run-history"
---

## View Integration Run History

The Run History page displays the execution history for each DataConnect, DataFlow or Link Integration that has been run.

To display the run history

Click Integrations, Run History. The Run History page is displayed with a list of execution history.

The default page size is set to 25. Page size and navigation controls are located at the bottom of the page. If your integration is not listed on the first page, use the search box to locate it.

The upper portion of the page features a bar chart which presents the summary status of all executed jobs.![](images/DesignWorkspace_42.png)

The lower portion of the page presents a sortable list of all executed jobs with the following information:

| Column Name | Description |
| --- | --- |
| Start Time | The date and time the job was started.The time displayed here is specific to your time zone. |
| Integration | Name of the integration. Clicking on the integration name displays the Integration Details page (see [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md)). If the run history is not based on a integration, “Not Set” is displayed. |
| Owner | Displays the first two characters of the Job owner (creator) name. Clicking on the initials displays the username of the owner. |
| Status | Status of the job:<br>• Waiting – Job has been created but needs additional information or a trigger event prior to being queued for execution.<br>• Queued – Job has been queued for execution by the next available worker.<br>• Canceled – Job was canceled prior to being acquired by a worker (during the Waiting or Queued state). No log file will be produced.<br>• Initializing – Job has been acquired by a worker and is being prepared for execution.<br>• Running – Job is currently executing on a worker.<br>• Finished – Job has successfully completed. A log file is available (or soon will be).<br>• Error – Job encountered an exception during execution. Depending on integration and artifact design, the job may or may not have completed. A log file is available (or soon will be).<br>• Failed – Job failed or was manually stopped by user command or exception at some point during initialization or execution. A log file may or may not be available. |
| Duration | Execution time. |
| Server | Where the job was executed. |
| Log | Click ![](images/DesignWorkspace_43.png) for a specific record in the Run History table. The Run History page is displayed from where you can view and download the log file. See [Download Log File](../Integrations/Download_Log_File.md). |
