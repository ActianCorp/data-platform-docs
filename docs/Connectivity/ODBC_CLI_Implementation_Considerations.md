---
title: "ODBC CLI Implementation Considerations"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "ODBC_CLI_Implementation_Considerations.htm"
canonical_id: "actian-data-platform-odbc-cli-implementation-considerations"
---

## ODBC CLI Implementation Considerations

The ODBC CLI includes two include files for compiling applications:

- sql.h
- sqlext.h

These files can be found at $II_SYSTEM/ingres/files.

Other standard ODBC includes libraries, such as sqlucode.h or sqltypes.h, are already included within the ODBC CLI version of sql.h and sqlext.h.

Linux:****The ODBC CLI is installed as the shared library libiiodbc.ext. Depending on the Linux implementation, the library extension (ext) varies. The library resides in $II_SYSTEM/ingres/lib.

Here is an example for building an ODBC CLI application on Linux:

```
cc -c myOdbcApp.c -I$II_SYSTEM/ingres/files
```

```
ld -o myOdbcApp myOdbcApp.o -L$II_SYSTEM/ingres/lib -liiodbc.1
```

]

## Optional Data Source Definitions

The use of odbcinst.ini, odbc.ini or the ODBC configuration registry is optional for the ODBC CLI. An application can invoke SQLDriverConnect() and specify a connection string that omits an ODBC Data Source (DSN) specification.

If the connection string has sufficient information to connect to the database, the location and name of the ODBC driver library are automatically determined. The use of the iiodbcadmin utility (Linux) or Microsoft ODBC Administrator (Windows) is optional.
