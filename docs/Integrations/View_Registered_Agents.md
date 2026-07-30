---
title: "View Registered Agents"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "View_Registered_Agents.htm"
canonical_id: "actian-data-platform-view-registered-agents"
---

## View Registered Agents

Use the Agents & Devices page to manage, and monitor the health of your registered agents.

To view an agent you must first [Download an Agent](../Integrations/Download_an_Agent.md), [Install an Agent](../Integrations/Install_an_Agent.md), and [Register an Agent](../Integrations/Register_an_Agent.md).

To view installed and registered agents

Click Integrations, Manage, Agents & Devices to view the Agents and Devices page.

- To search for specific text within the Agents list, click the ![](images/SearchIcon.png) icon and enter the text you want to search on. Agent names that match the text you enter automatically display.
- To sort listed agents, click the Hostname, Last Check-in, Version, or Status column header. The agents are sorted based on the column header you click.

- To reduce or enlarge the Agents list or jump to earlier or later pages of the listing, click the appropriate control on the toolbar at the end of the list:

![](images/RuntimeWorkspace_119.png)

| Column Name | Description |
| --- | --- |
| Hostname | Hostname of the agent owner. Clicking on the column header sorts the list of agents in ascending or descending alphabetical order. |
| Owner | Displays the first two characters of the agent owner name. Clicking on owner icon displays the username of the owner. |
| IPV4 | Public IP address of the agent (the owner’s local machine). |
| Last Check-in | Time the agent last sent a message back to the cloud. Clicking on the column header sorts the list of agents in ascending or descending alphabetical order. |
| Version | Version number of the installed agent. Clicking on the column header sorts the list of agents in ascending or descending alphabetical order. |
| Status | Displays the current status of the agent. Clicking on the column header sorts the list of agents in ascending or descending alphabetical order.•Healthy – The agent is connected and ready to receive jobs.•Updating – The Agent is currently processing an Update Command, such as Update Worker or Update Engine.•Warning* – The Agent has not reported its status in over 3 hours and may require attention.•Error* – The Agent has not reported its status in over 6 hours.•Offline* – The Agent is offline or the local service is stopped. This status is typically reported just prior to a shutdown.*You can verify whether the agent is running, and also start the agent service, by opening Windows Services. |
| Active | Displays whether the agent is active or inactive. For more information, see [Activate/Deactivate an Agent](../Integrations/Activate_2fDeactivate_an_Agent.md). |
| ![](images/cogwheelIcon.png) | You can perform the following actions:•Ping - Clicking ![](images/RuntimeWorkspace_120.png) sends a message to the agent which responds with a check-in message.•Clicking ![](images/RuntimeWorkspace_121.png) opens the dropdown to perform the following actions:–Request Log – Updates the Agent.log file, stored in the IntegrationAgent\logs folder. See [Request Log](../Integrations/Request_Log.md).–View Log – Opens the Agent.log log file in the Agent Log page. See [View Log](../Integrations/View_Log.md).–Update Settings – Resets the connection configuration information in the current cloud settings. See [Update an Agent](../Integrations/Update_an_Agent.md).–Update License – Updates to the newest license file that is installed locally. See [Update an Agent](../Integrations/Update_an_Agent.md).–Update Worker – Updates to the latest version of the agent. See [Update an Agent](../Integrations/Update_an_Agent.md).–Update Engine – Updates to the latest version of Actian Data Platform. See [Update an Agent](../Integrations/Update_an_Agent.md).–Activate/Deactivate – Sets the agent to the Active or Inactive state. See [Activate/Deactivate an Agent](../Integrations/Activate_2fDeactivate_an_Agent.md).–Deregister – Disconnects and removes the agent from the Agents and Devices page. For system uninstallation details, see the end of the Windows or Linux installation instructions in [Install an Agent](../Integrations/Install_an_Agent.md). |
