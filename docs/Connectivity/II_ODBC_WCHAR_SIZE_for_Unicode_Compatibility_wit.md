---
title: "II_ODBC_WCHAR_SIZE for Unicode Compatibility with unixODBC or DataDirect"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "II_ODBC_WCHAR_SIZE_for_Unicode_Compatibility_wit.htm"
canonical_id: "actian-data-platform-ii-odbc-wchar-size-for-unicode-compatibility-wit"
---

## II_ODBC_WCHAR_SIZE for Unicode Compatibility with unixODBC or DataDirect

The ODBC environment variable II_ODBC_WCHAR_SIZE overrides the default byte size of Unicode characters for the ODBC Driver.

Applications that use unixODBC on Linux can define Unicode characters with a different byte size than the ODBC Driver does. Depending on the environment, the unixODBC Driver Manager can define Unicode characters with a size of two bytes, but the ODBC Driver can define Unicode characters as four bytes. For these cases, enter this command at the command prompt:

```
ingsetenv II_ODBC_WCHAR_SIZE 2
```

This specification forces the ODBC Driver to treat Unicode characters as two bytes instead of four.

Applications that use DataDirect define Unicode characters with only one byte, but the ODBC Driver defines Unicode characters as two or four bytes. DataDirect environments use only UTF-8 encoding. To make the ODBC Driver compatible with DataDirect, execute these commands from the command prompt:

```
ingsetenv II_ODBC_WCHAR_SIZE 1
```

```
ingsetenv II_CHARSETxx UTF8
```

where the xx is the instance ID.

!!! note "Note"

    The installation must be stopped and restarted for the II_CHARSETxx setting to take effect.

II_ODBC_WCHAR_SIZE can also be set in the config.dat file. For example, issue the following command to specify the setting for the machine myhost:

```
iisetres ii.myHost.odbc.wchar_size 1
```

or:

```
iisetres ii.myHost.odbc.wchar_size 2
```
