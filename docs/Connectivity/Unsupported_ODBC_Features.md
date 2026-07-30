---
title: "Unsupported ODBC Features"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Unsupported_ODBC_Features.htm"
canonical_id: "actian-data-platform-unsupported-odbc-features"
---

## Unsupported ODBC Features

The ODBC driver does not currently support the following features:

- Executing functions asynchronously
- Translation DLL (Actian Data Platform handles this requirement through the II_CHARSETxx environment variable.)

- The GUID (Globally Unique Identifier) data type, which is specific to Microsoft Access databases.
- Installer DLL

    On Windows, the Microsoft installer DLL can be used to install the ODBC Driver, if required. The ODBC Driver can be installed from the Actian Data Platform Runtime installer.

    On non-Windows platforms, the odbcinst utility uses the ODBC Configuration API to configure driver information.

- SQLBulkOperations()
