---
title: "Register an Agent"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Register_an_Agent.htm"
canonical_id: "actian-data-platform-register-an-agent"
---

## Register an Agent

After you [Download an Agent](../Integrations/Download_an_Agent.md) and [Install an Agent](../Integrations/Install_an_Agent.md), you must register it. However, only the connectors listed when the Connect via Agent option is enabled on the Create Connections page can be used with the agent. See [Connections](../Integrations/Connections.md).

!!! note "Note"

    There may be additional license requirement to use connectors via agents.

To register an agent

1. At the end of the agent installation process, if installed locally, open `http://localhost:6001/home`. If installed on a network server, open `http://[agent hostname]:6001/home`.
2. Choose one of the following options to register the agent:

    - Register as a Platform user: Enter your platform credentials in the username and password fields and click Register (or press Enter).

    - Register using Community Id: Clicking this button opens a page where you can enter your Actian Community credentials (username and password).

    - Register using Google Cloud: Clicking this button opens the Google Sign in page where you can enter your Google credentials .

    The agent is registered and is listed under Registered Agents on the Integrations, Manage, Agents and Devices page (see [View Registered Agents](../Integrations/View_Registered_Agents.md)) the next time you log in.

!!! note "Note"

    You can open `http://localhost:6001/home` at any time to confirm the status of the Agent on the installed machine.

If you encounter issues, try the following:

- Make sure the agent has been activated. See [Activate/Deactivate an Agent](../Integrations/Activate_2fDeactivate_an_Agent.md).
- If the issue doesn’t resolve, open Windows Services and ensure that the Integration Agent service is running. Try restarting the Integration Agent service and see if the issue is fixed.

See Also

- [View Registered Agents](../Integrations/View_Registered_Agents.md)
- [Ping an Agent](../Integrations/Ping_an_Agent.md)
