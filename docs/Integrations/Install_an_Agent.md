---
title: "Install an Agent"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Install_an_Agent.htm"
canonical_id: "actian-data-platform-install-an-agent"
---

## Install an Agent

You can download the Agent installer from either the Agents and Devices page in Actian Data Platform or Actian ESD. See [Download an Agent](../Integrations/Download_an_Agent.md).

Prerequisites for Windows

- Windows

    - –Windows 10 Enterprise or later, Windows Server 2016 or later

    - –Windows user account with Run as Administrator privileges

- 64-bit processor, 2.90GHz
- 8 GB Installed memory (RAM)

To install the agent on a Windows machine

1. Right-click the downloaded installer file (integration-agent-xxx-win.exe) and select Run as administrator.

    If you have a previous version of the Agent installed, you will be prompted to uninstall it first. The uninstallation process will shut down running services and prepare for library updates; however, it will NOT remove or alter ProgramData (such as configuration files, logs, etc.). You can manually delete the IntegrationAgent folder from `C:\Program Files\Actian\` and `C:\ProgramData\Actian\` before proceeding with the new installation. You will also need to deregister the agent in Actian Data Platform (see [Deregister an Agent](../Integrations/Deregister_an_Agent.md)).

2. Click Next to start the wizard.
3. Accept the License Agreement.

4. Make changes to the installation path if needed and then click Install.
5. When the installation is complete, click Done.

!!! note "Note"

    You can uninstall the service by double-clicking the uninstaller.exe file, located in the agent package installation folder.

After installing the agent, you must register it. See [Register an Agent](../Integrations/Register_an_Agent.md).

Prerequisites for Linux

- Linux

    - –Red Hat Enterprise Linux 7.9 and 8 (64-bit U.S. English edition)

    - –GTK Version 3

    - –You need to install libnsl.so.1 separately on RHEL 8.1 or above versions.

    - –Linux user account with `sudo` privileges

- 64-bit processor, 2.90GHz
- 8 GB Installed memory (RAM)

- DataConnect v12 License file (typically *.slc)

To install the agent on a Linux machine

1. Copy the agent rpm to your machine.
2. Install the downloaded agent rpm executing the following command:

```
rpm -ihv worker-agent-<version>.noarch.rpm
```

    Then press y and then Enter to validate installation.

3. While you wait for the rpm to install, you may follow the agent log by executing the following command:

```
tail -f /etc/opt/actian/integration-agent/logs/integration-agent.log
```

!!! note "Note"

    You can uninstall the service by typing the agent rpm name with no file extension:
    `rpm -e worker-agent-<version>.noarch`

After installing the agent, you must register it. See [Register an Agent](../Integrations/Register_an_Agent.md).
