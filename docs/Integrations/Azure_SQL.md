---
title: "Azure SQL"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Azure_SQL.htm"
canonical_id: "actian-data-platform-azure-sql"
---

## Azure SQL

Microsoft Azure SQL adapter provides support for performing read, write and discovery operations on Microsoft Azure SQL database. Microsoft Azure SQL is a general-purpose relational database, running as a managed service on the Microsoft Azure cloud computing platform.

- [Prerequisites](../Integrations/Azure_SQL.md)
- [Connection Details](../Integrations/Azure_SQL.md)

- [Source Details](../Integrations/Azure_SQL.md)
- [Additional Information](../Integrations/Azure_SQL.md)

Prerequisites

You must have an Azure account and credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Server Name | Specifies the server’s name to connect. This is a mandatory property. |
| Port | Specifies the port to connect on the Server Name. The default value is 1433. This is a mandatory property. |
| Database | Specifies the name of the database. This is a mandatory property. |
| User | (Optional) Specifies the username for the connection or database login. |
| Password | (Optional) Specifies the password for the connection or database login. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Source | Specifies the data source object type. It has two possible values: Table (default) and Query. |
| Schema | (Optional) Specifies the schema name. |
| Table | Specifies the table or view name. This is a mandatory property. |
| Query | Specifies the SQL statement to select data from the source. This is a mandatory property. This field is enabled when Source field is selected to Query. |
| Row Limit | (Optional) Specifies the maximum number of records to return from the database. The value 0means all records are available. |
| Burst Size | (Optional) Specifies the number of records that the connector concatenates and returns as a single logical data unit per burst. The Value 0 instructs the connector to concatenate all available records and return them as a single unit of data. This property is enabled in burst mode. In integral mode the value 0 is always used. |

Additional Information

None
