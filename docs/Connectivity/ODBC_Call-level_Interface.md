---
title: "ODBC Call-level Interface"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "ODBC_Call-level_Interface.htm"
canonical_id: "actian-data-platform-odbc-call-level-interface"
---

## ODBC Call-level Interface

The ODBC Call-level Interface (ODBC CLI) provides access to the ODBC application environment without the need to use third-party software. It is installed when you install the ODBC Driver.

The ODBC CLI performs these functions:

- Optionally determines driver characteristics from ODBC configuration files
- Loads and unloads the ODBC driver into and from application memory

- Maps the driver manager API to the driver API
- Performs basic error checking

- Provides thread safety
- Provides ODBC tracing

- Provides function templates, type definitions, and constant definitions for ODBC applications
- Provides connection pooling, which allows connections to be shared in ODBC applications

!!! note "Note"

    The ODBC CLI is not a generic ODBC driver manager. While it does provide functions similar to other ODBC driver managers, it is designed specifically to support ODBC-based application access. It does not support ODBC drivers provided by third-party vendors.

The ODBC CLI is available on all supported platforms except Windows. The iiodbcadmin utility configures ODBC Data Source Definitions for the CLI. For more information, see [Configure a Data Source (Linux)](../Connectivity/Configure_a_Data_Source_(Linux).md).
