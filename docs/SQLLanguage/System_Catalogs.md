---
title: "System Catalogs"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "System_Catalogs.htm"
canonical_id: "actian-data-platform-system-catalogs"
---

# System Catalogs

## Standard Catalog Interface

Actian Data Platform has a set of internal system catalog tables that store information (for example, metadata) required for operation. The System Catalog Interface (SCI) is a set of views on top of these system catalog tables, and a set of tables that can be queried through SQL statements and therefore used in applications to access (but not update) information about the database.

If you are developing applications that need to query the system catalogs, you must use the Standard Catalog Interface, so that your applications will be upwardly compatible.

All database users can read the Standard Catalog Interface catalogs, but only a privileged user can update them.

To display the underlying view, use the SQL statement HELP VIEW. To display the format of catalogs, use the SQL statement HELP (see [Example of HELP VIEW and HELP Statements](../SQLLanguage/Example_of_HELP_VIEW_and_HELP_Statements.md)). (HELP commands are valid in interactive SQL but not in the Query Editor.)

The length of character fields, as listed in the length column, is a maximum length; the actual length of the field may be installation dependent. The values are left-justified and the columns are non-nullable.

Unless otherwise stated, dates are displayed as 25-byte character strings with the following format:

```
yyyy_mm_dd hh:mm:ss GMT
```

When developing applications that access SCI, storage should be allocated based on the length shown in the Data Type column in the descriptions below.
