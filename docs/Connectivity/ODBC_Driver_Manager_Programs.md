---
title: "ODBC Driver Manager Programs"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "ODBC_Driver_Manager_Programs.htm"
canonical_id: "actian-data-platform-odbc-driver-manager-programs"
---

## ODBC Driver Manager Programs

The following are the installation requirements for the ODBC driver.

Windows:****Microsoft’s ODBC Driver Manager must be installed to use the ODBC driver (release 2.5 or above of the ODBC Driver Manager is acceptable). If the existing Windows installation has no ODBC Administrator or ODBC driver, these items can be downloaded as part of the Microsoft Data Access SDK (MDAC) from [http://www.microsoft.com](http://www.microsoft.com). ]

Linux:****The ODBC CLI is the preferred ODBC driver manager if no other ODBC drivers are required. No additional download is required.

If the ODBC application requires non-Ingres ODBC drivers, unixODBC Driver Manager can be installed to use the Actian Data Platform ODBC Driver. The unixODBC Driver Manager is often included with Linux installations or can be downloaded from [http://www.unixodbc.org](http://www.unixodbc.org). The download includes a Readme file with instructions for Linux. ]

### UnixODBC Implementation Considerations

The ODBC Driver can be used with the unixODBC Driver Manager on non-Windows platforms. Unlike the ODBC CLI, the unixODBC Driver Manager allows other ODBC drivers to be used in addition to the Actian Data Platform ODBC driver. To build the application, the include files sql.h and sqlext.h files in $II_SYSTEM/ingres/files can be used; alternatively, the include files sql.h, sqlext.h, sqltypes.h, and sqlucode.h provided with the unixODBC installation can be used.

UnixODBC data sources can be configured using the ODBC CLI. Unlike the CLI, the ODBCINI and ODBCSYSINI environment variables must be specified. For more information about ODBCINI and ODBCSYSINI in the unixODBC environment, see the unixODBC documentation.

Linux: Here is an example for building a unixODBC application on Linux:

```
cc -c myOdbcApp.c /I/disk1/unixODBC-2.2.12/include
```

```
ld -o myOdbcApp myOdbcApp.o -L/disk1/unixODBC-2.2.12/DriverManager -lodbc ]
```
