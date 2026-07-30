---
title: "Access Warehouse or Database Connection Information"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Access_Warehouse_or_Database_Connection_Informat.htm"
canonical_id: "actian-data-platform-access-warehouse-or-database-connection-informat"
---

# Access Warehouse or Database Connection Information

After your Actian warehouse or database is created and running (see Create a Warehouse and Restart a Warehouse or [Create a Database Instance](../DBaaS_User/Create_a_Database_Instance.md) and Restart a Database), you may connect to it from external applications. These applications could deal with loading data, performing ad-hoc querying, using BI tools for reporting, loading data into a Spark warehouse or into a Data Science workbench. You may use any tool or application that is ODBC- JDBC-, or .NET-compliant.

You can access connection information for various third-party tools through the Connection tab on the Warehouse Details or [Database Instance Details](../DBaaS_User/Database_Instance_Details.md) page. The dropdown menu on the Connections tab displays the various warehouse/database connection strings for JDBC, ODBC, as well as the tools listed in [Connection Tools](../DBaaS_User/Connection_Tools.md).

!!! note "Note"

    While a warehouse or database is being created, this information will not be available immediately. We recommend that you use this time to download and set up your client; follow the link for your application in [Connection Tools](../DBaaS_User/Connection_Tools.md).

Connection strings will work only from machines with an Allow List IP address. For more information, see Update Allow List IP Addresses.
