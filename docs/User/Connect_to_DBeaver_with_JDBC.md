---
title: "Connect to DBeaver with JDBC"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Connect_to_DBeaver_with_JDBC.htm"
canonical_id: "actian-data-platform-connect-to-dbeaver-with-jdbc"
---

# Connect to DBeaver with JDBC

After your Actian warehouse is created and running, you may connect to it from various applications. These applications could deal with loading data, performing ad-hoc querying, using BI tools for reporting, loading data into a Spark warehouse or into a Data Science workbench.

For the examples in this section, we use the community edition of DBeaver Universal Database Tool, available for download from [https://dbeaver.io/](https://dbeaver.io/).

!!! note "Note"

    When loading large amounts of data, you may face network disconnects or network-related errors. You must keep your TCP connection alive by increasing the TCP keepalive length. For more information, see [Network Disconnects Due to Perceived Inactivity](../User/Network_Disconnects_Due_to_Perceived_Inactivity.md).

Before you can connect to your warehouse, you must install the Actian JDBC package. Follow the instructions in [Actian JDBC Driver](../User/Actian_JDBC_Driver.md).
