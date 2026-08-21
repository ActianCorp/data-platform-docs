---
title: "Overview Page"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Overview_Page.htm"
canonical_id: "actian-data-platform-overview-page"
---

## Overview Page

The Overview page provides a dashboard of data visualization charts you can use to monitor the general health and performance of your integrations, configurations and agents. This page also includes [Recent Integrations](../Integrations/Overview_Page.md), which provides a list of your configurations and tools to manage them.

| Charts | Description |
| --- | --- |
| ![](images/allIntegrationsCard.png) | The ALL RECENT JOBS chart traces jobs that executed for the selected number of jobs (Last 50 jobs, Last 100 jobs or Last 200 jobs). Mouse over the chart to see the number of jobs executed on a particular date. |
| ![](images/failedSyncResultsCard.png) | The RECENT FAILED JOBS chart traces jobs that failed to execute for the selected number of jobs (Last 50 jobs, Last 100 jobs or Last 200 jobs). Mouse over the chart to see the number of jobs that failed on a particular date. |
| ![](images/agentHealthCard.png) | The AGENT HEALTH chart represents the health status of agents a user has installed. In the adjacent figure, the user has four agents installed. Mouse over the chart to see the number of agents per status indicated.Agent status can be:<br>• Healthy: (Green) The agent is connected and ready to receive jobs.<br>• Warning*: (Yellow) The Agent has not reported its status in over 3 hours and may require attention.<br>• Error*: (Red) The Agent has not reported its status in over 6 hours.<br>• Updating: (Turquoise) The Agent is currently processing an Update Command, such as Update Worker or Update Engine.<br>• Offline*: (Grey) The Agent is offline or the local service is stopped. This status is typically reported just prior to a shutdown.<br>• Expired: (Dark Grey) The Agent has expired.*You can verify whether the agent is running, and also start the agent service, by opening Windows Services. |
| ![](images/syncResultsStatusCard.png) | The SYNC RESULTS STATUS chart represents run results status for configuration jobs executed during the selected time period (30, 60 or 90 days).Sync result status can be:<br>• Finished: Job has successfully completed. A log file is available (or soon will be).<br>• Running: Job is currently executing on a worker.<br>• Canceled: Job was canceled prior to being acquired by a worker (during the Waiting or Queued state). No log file will be produced.<br>• Error: Job encountered an exception during execution. Depending on configuration and artifact design, the job may or may not have completed. A log file is available (or soon will be).<br>• Queued: Job has been queued for execution by the next available worker.<br>• Failed: Job failed or was manually stopped by user command or exception at some point during initialization or execution. A log file may or may not be available. |

You can also perform the following actions:

- Click ![](images/RuntimeWorkspace_2.png) to download the chart in SVG or PNG format, or download the data in CSV format (which you can open in Excel). Drag and drop charts to reorder.
- Click ![](images/RuntimeWorkspace_3.png), Settings to change or reorder the charts shown in Dashboard Settings.

- Click ![](images/RuntimeWorkspace_4.png), Remove to remove a chart.
- Add charts from the Available charts list by clicking ![](images/RuntimeWorkspace_5.png). Drag and drop charts to reorder. Settings are persisted the next time you log in.

Recent Integrations

The Recent Integrations list provides a list of all your configurations and management tools.

You can:

- Click ![](images/RuntimeWorkspace_6.png) to import a configuration. This option opens the Import Configuration page where you can select an existing file from your local system, or select a file from the Integrations File repository. Accepted file formats are .djar, .rtc, .process, .ip.xml, and .tf.xml.
- Click ![](images/RuntimeWorkspace_7.png) next to a configuration, and then select Run, View Configuration, View Log, or Delete.

- Click ![](images/RuntimeWorkspace_8.png) to filter the configuration list by Failed, Finished, Queued, Error, Running, Canceled, or Sequenced.
