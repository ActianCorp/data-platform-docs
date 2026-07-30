---
title: "Connect to Tableau with ODBC"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "ConnectTableauODBC.htm"
canonical_id: "actian-data-platform-connecttableauodbc"
---

# Connect to Tableau with ODBC

After your Actian warehouse is created and running, you may connect to it from Tableau Desktop.

!!! note "Note"

    When loading large amounts of data, you may face network disconnects or network-related errors. You must keep your TCP connection alive by increasing the TCP keepalive length. For more information, see [Network Disconnects Due to Perceived Inactivity](../User/Network_Disconnects_Due_to_Perceived_Inactivity.md).

Before you can connect to your warehouse from Tableau, you must install the Actian Data Platform ODBC driver. Follow the instructions in [Avalanche Client Runtime Package](../User/Access_Warehouse_or_Database_Connection_Informat.md).

Video: [How to Connect Tableau to an Actian warehouse](https://vimeo.com/actian/review/408811007/259d8df521)

To connect Tableau to your Actian warehouse

1. Start Tableau Desktop.
2. In the Actian Data Platform, add your IP address to your warehouse’s allow list of trusted IPs.

    For more information, see [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).

3. On the Actian Data Platform [Warehouse Details](../User/Warehouse_Details.md) page, click the Connections tab.

    For more information, see [Connection Tools](../User/Connection_Tools.md).

4. Select Tableau from the Connect to Actian warehouse dropdown.
5. Copy the Virtual Node value to the clipboard.

6. In Tableau, from the Connect pane on the left, under the To a Server section, click Actian Vector.

    The Actian Vector dialog opens.

7. Past the virtual node value from the clipboard.
8. Copy the Database value from the Actian Data Platform and paste it in Tableau.

9. Enter the Username dbuser and the Actian Data Platform Connection Password.

    For more information, see:

    - For AWS AV-1 and Azure: [Set the dbuser Connection Password](../User/Set_the_dbuser_Connection_Password.md).

    - For Google Cloud and AWS AV-2: [Add Native Users](../User/Add_Native_Users.md).

10. Click the Sign In button.

    The connection is added to the left pane in Tableau.

11. Verify that data from your Actian warehouse is reaching Tableau:

    a. Click the Select Schema dropdown and choose the sample schema.

    Tables are listed.

    b. Drag one of the table entries onto the Tableau canvas on the right side of the window.

    Airline data should be displayed.
