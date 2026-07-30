---
title: "Connect to Looker with JDBC"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "ConnectLookerJDBC.htm"
canonical_id: "actian-data-platform-connectlookerjdbc"
---

# Connect to Looker with JDBC

After your Actian warehouse is created and running, you may connect to it from Looker.

!!! note "Note"

    When loading large amounts of data, you may face network disconnects or network-related errors. You must keep your TCP connection alive by increasing the TCP keepalive length. For more information, see [Network Disconnects Due to Perceived Inactivity](../User/Network_Disconnects_Due_to_Perceived_Inactivity.md).

Before you can connect to your warehouse from Looker, you must install the Actian JDBC package. Follow the instructions in [Actian JDBC Driver](../User/Actian_JDBC_Driver.md).

Video: [How to Connect Looker to an Actian warehouse](https://academy.actian.com/connect-looker-to-an-avalanche-cloud-data-warehouse-free-trial).

To connect Looker to your Actian warehouse

1. Start Looker and display the dashboard.
2. In the Actian Data Platform, add your IP address and the Looker endpoint IP address to your warehouse’s allow list of trusted IPs.

    For more information, see [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).

3. On the Actian Data Platform [Warehouse Details](../User/Warehouse_Details.md) page, click the Connections tab.

    For more information, see [Connection Tools](../User/Connection_Tools.md).

4. Select Looker from the Connect to Actian warehouse dropdown.
5. From the Looker dashboard, click the Admin menu, Database, Connections.

6. Click the New Connection button.

    The Connection Settings page is displayed.

7. Enter a name for the connection, for example, “Actian warehouse.”
8. Copy the following information from the Actian Data Platform Looker Connections page to the corresponding fields on the Looker Connections Settings page:

    - Dialect

    - Host

    - Database

    - Username

9. In the Looker Connections Settings Password field, enter the Actian warehouse Connection Password.

    For more information, see:

    - For AWS AV-1 and Azure: [Set the dbuser Connection Password](../User/Set_the_dbuser_Connection_Password.md).

    - For Google Cloud and AWS AV-2: [Add Native Users](../User/Add_Native_Users.md).

10. At the bottom of the Looker Connections Settings page, click the Test These Settings button.

    If the connection fails, make sure the Actian warehouse is running and double-check the information entered in the connection fields. Then test again until a successful connection is made.

11. Click the Add Connection button.

    The new connection is added to Looker’s list of available connections.

12. Open the connection and test whether it returns data from your Actian warehouse.
