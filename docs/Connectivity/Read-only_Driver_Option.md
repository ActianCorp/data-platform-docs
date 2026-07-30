---
title: "Read-only Driver Option"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Read-only_Driver_Option.htm"
canonical_id: "actian-data-platform-read-only-driver-option"
---

## Read-only Driver Option

To support the release of a non-configurable read-only driver into production environments, the ODBC driver can optionally be installed as a read-only driver. This driver allows SQL statements such as SELECT, and EXECUTE PROCEDURE, but does not allow update statements (for example, INSERT, DELETE, UPDATE, CREATE, and so on).

Both ODBC drivers (read-only and read/update) are installed during the [Actian Client Runtime Package](../User/Actian_Client_Runtime_Package.md) installation. Selecting the driver type happens during configuration of an ODBC data source. For more information, see [Configure a Data Source (Windows)](../Connectivity/Configure_a_Data_Source_(Windows).md) and [Configure a Data Source (Linux)](../Connectivity/Configure_a_Data_Source_(Linux).md).
