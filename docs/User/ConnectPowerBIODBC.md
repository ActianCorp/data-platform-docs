---
title: "Connect to Power BI with ODBC"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "ConnectPowerBIODBC.htm"
canonical_id: "actian-data-platform-connectpowerbiodbc"
---

# Connect to Power BI with ODBC

After your Actian warehouse is created and running, you may connect to it from Power BI Desktop.

!!! note "Note"

    When loading large amounts of data, you may face network disconnects or network-related errors. You must keep your TCP connection alive by increasing the TCP keepalive length. For more information, see [Network Disconnects Due to Perceived Inactivity](../User/Network_Disconnects_Due_to_Perceived_Inactivity.md).

Before you can connect to your warehouse from Power BI, you must install the Actian Data Platform ODBC driver. Follow the instructions in [Avalanche Client Runtime Package](../User/Access_Warehouse_or_Database_Connection_Informat.md).

Video: [How to Connect Power BI to an Actian warehouse](https://vimeo.com/actian/review/405821811/372a3fa0eb)

To connect Power BI to your Actian warehouse

1. Start Power BI Desktop.
2. In the Actian Data Platform, add your IP address to your warehouse’s allow list of trusted IPs.

    For more information, see [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).

3. On the Actian Data Platform [Warehouse Details](../User/Warehouse_Details.md) page, click the Connections tab.

    For more information, see [Connection Tools](../User/Connection_Tools.md).

4. Select Power BI from the Connect to Actian warehouse dropdown.
5. Copy the Connection String to the clipboard.

6. In Power BI, click Get Data, Other, ODBC. Then click the Connect button.

    The From ODBC dialog is displayed.

7. From the Data source name (DSN) dropdown, select (None).
8. Expand the Advanced options.

9. Paste the connection string from the Actian Data Platform to the Power BI Connection string field.
10. Click OK.

    The ODBC driver dialog opens.

11. In the Power BI Password field, enter the Actian warehouse Connection Password.

    For more information, see:

    - For AWS AV-1 and Azure: [Set the dbuser Connection Password](../User/Set_the_dbuser_Connection_Password.md).

    - For Google Cloud and AWS AV-2: [Add Native Users](../User/Add_Native_Users.md).

12. Click the Connect button.

    The Actian warehouse connection entry is listed in the Power BI Navigator pane.

13. Verify that data from your Actian warehouse is reaching Power BI: Open the sample schema and click a table name.

    Airline data should be displayed.
