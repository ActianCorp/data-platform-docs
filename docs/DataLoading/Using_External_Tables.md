---
title: "Using External Tables"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "Using_External_Tables.htm"
canonical_id: "actian-data-platform-using-external-tables"
---

# Using External Tables

## Introduction to External Tables

The external tables feature lets you read from and write to data sources stored outside of the Actian Data Platform. The data source must be one that Apache Spark is able to read from and write to, such as files stored in formats like Parquet, ORC, JSON, or tables in external database systems.

The syntax CREATE EXTERNAL TABLE creates an Actian Data Platform table that points at existing data files in locations outside of the platform. This feature eliminates the need to import the data into a new table when the data files are already in a known location, in the desired file format.

After the data file structure is mapped to an Actian Data Platform format using the CREATE EXTERNAL TABLE statement, you can:

- Select, join, or sort external table data
- Create views for external tables

- Insert data into external tables
- Import and store the data into an Actian database

The data is queried from its original locations and the Actian Data Platform leaves the data files in place when you drop the table.

The following statements cannot be performed against external tables:

- MODIFY
- CREATE INDEX

The Actian Data Platform leverages Apache Spark’s extensive connectivity for external tables functionality.

The platform receives queries operating on external tables from the user, rewrites them into JSON requests for external data. These requests are translated into Spark jobs, which are launched. These jobs typically issue queries (to SparkSQL) like “INSERT INTO avalanche_table SELECT * FROM external_resource” for reading external data or “INSERT INTO external_resource SELECT * FROM avalanche_table” for writing to external systems. Finally, these jobs push and pull data in and out of the platform.

Inserts into external table are allowed.

The syntax for defining an external table is as follows:

```
CREATE EXTERNAL TABLE table_name (column_name data_type {,column_name data_type})
```

```
USING SPARK
```

```
WITH REFERENCE='reference'
```

```
[,FORMAT='format']
```

```
[,OPTIONS=('key'=value {,'key'='value'})]
```

For more information, see [CREATE EXTERNAL TABLE](../SQLLanguage/CREATE_EXTERNAL_TABLE.md) in the SQL Language Guide.

After external tables are defined with the CREATE EXTERNAL TABLE syntax, they behave like regular platform tables. You can issue queries such as the following:

```
SELECT * FROM test_table_csv
```

```
INSERT INTO my_table_orc SELECT some_column FROM other_table
```

For more information about exporting data, see [Exporting and Importing Data](../DataLoading/ExportingImportingData.md).

By default, the Actian Data Platform supports only Spark-integrated data sources (such as JDBC, JSON, Parquet) and CSV data sources.

The external tables feature has the following limitations:

- WARNING!The options retained in the CREATE EXTERNAL TABLE definition are not secure; they can be shown in clear text in tracing and logging. We recommend that no sensitive information be used in the OPTIONS portion of the definition. This has implications for JDBC data sources.
- Spark runs under the user that is the owner of the Actian warehouse. This means that only data sources for which that user has permissions to access (read or write) can be used in the Actian warehouse.

- Operations not supported on external tables are usually reported with explicit errors. Unsupported operations include the following:

    - –Creating keys (of any type) and creating indexes (of any type) are not supported because they cannot be enforced (that is, they can be violated by the actions of an external entity)

    - –Adding and dropping columns

    - –Updates and deletes

Note the following when using external tables:

- For writing to external tables, the mode is SaveMode.Append. Some data sources do not support this mode. For example, you cannot write to existing CSV files because spark-csv does not support this mode.
- CREATE EXTERNAL TABLE does not validate the supplied values for REFERENCE, FORMAT, or OPTIONS until the external table is used. So, the following use case will result in an error if the target does not yet exist:

```
CREATE EXTERNAL TABLE test_table(col INT NOT NULL) USING SPARK
```

```
WITH REFERENCE='abfs://tpch@pjwstuff.dfs.core.windows.net/region.csv';
```

```
SELECT * FROM test_table; \g
```

```
Executing . . .
```

```

```

```
E_VW1213 External table provider reported an error 'java.io.IOException:
```

```
   No input paths specified in job'.
```

    However, as soon as the Actian Data Platform user inserts some data, the external table is created at its original location (for example, files are written to ABFS) and a subsequent SELECT statement will succeed:

```
INSERT INTO test_table VALUES (1);
```

```
SELECT * FROM test_table; \g
```

```
Executing . . .
```

```

```

```
(1 row)
```

```

```

```
┌─────────────┐
```

```
│col          │
```

```
├─────────────┤
```

```
│ 1           │
```

```
└─────────────┘
```

```
(1 row)
```
