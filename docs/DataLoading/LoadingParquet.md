---
title: "Loading Parquet Data from Cloud Data Storage"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "LoadingParquet.htm"
canonical_id: "actian-data-platform-loadingparquet"
---

# Loading Parquet Data from Cloud Data Storage

!!! note "Note"

    Before using this method, be sure to read [Overview of SQL-Based Data Loading](../DataLoading/OverviewSQLDataLoading.md).

You can load Parquet data using the following loading method: [Loading Parquet Data from External Tables (SQL)](../DataLoading/LoadingParquet.md).

The cloud object stores that are currently supported are AWS S3, Azure Blob Storage, and Google Cloud.

To use the Actian SQL CLI for issuing SQL commands, see [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md).

External tables use Apache Spark underneath to reference and load external data into the Actian warehouse. This in turn has been wrapped in a native Actian Data Platform SQL command to aid ease of use.

## Loading Parquet Data from Google Cloud Storage

Shown below is an example of how to load Parquet data stored on Google Cloud storage using external tables.

Example: Loading Parquet Data from Google Cloud Storage

```
DROP TABLE IF EXISTS pemdata_gs;
```

```
CREATE EXTERNAL TABLE pemdata_gs (
```

```
    timeperiod VARCHAR(20),
```

```
    flow1 VARCHAR(20),
```

```
    flow2 VARCHAR(20),
```

```
    occupancy1 VARCHAR(20),
```

```
    speed1 VARCHAR(20)
```

```
) using spark
```

```
WITH
```

```
    reference='gs://avpemdata/part*.parquet',
```

```
    format='parquet';
```

```

```

```
DROP TABLE IF EXISTS pemdata;
```

```
CREATE TABLE pemdata (
```

```
    timeperiod TIMESTAMP,
```

```
    flow1 VARCHAR(20),
```

```
    flow2 VARCHAR(20),
```

```
    occupancy1 VARCHAR(20),
```

```
    speed1 VARCHAR(20)
```

```
);
```

```

```

```
INSERT INTO pemdata SELECT * FROM pemdata_gs;
```

## Loading Parquet Data from Azure Blob Storage

Shown below is an example of how to load Parquet data stored on Azure Blob storage using external tables.

Example: Loading Parquet data from Azure Blob Storage

```
DROP TABLE IF EXISTS pemdata_adl;
```

```
CREATE EXTERNAL TABLE pemdata_adl (
```

```
    timeperiod VARCHAR(20),
```

```
    flow1 VARCHAR(20),
```

```
    flow2 VARCHAR(20),
```

```
    occupancy1 VARCHAR(20),
```

```
    speed1 VARCHAR(20)
```

```
) using spark
```

```
WITH
```

```
    reference='abfs://parquetdata@mydata.dfs.core.windows.net//part*.parquet',
```

```
    format='parquet';
```

```

```

```
DROP TABLE IF EXISTS pemdata;
```

```
CREATE TABLE pemdata (
```

```
    timeperiod TIMESTAMP,
```

```
    flow1 VACHAR(20),
```

```
    flow2 VARCHAR(20),
```

```
    occupancy1 VARCHAR(20),
```

```
    speed1 VARCHAR(20)
```

```
);
```

```

```

```
INSERT INTO pemdata SELECT * FROM pemdata_adl;
```

Notes:

1. Before doing the insert into or load operation to create the native Actian Data Platform table, it is important that you can view the data in the external table using a SELECT * FROM <external table>.

    Typically you will have a mismatched data type or column name, so it is important to narrow down the offending column or columns.

    This is achieved by doing SELECT <column1>, <column2> FROM <external table>, and adding more columns as you go.

    You can use this method to find the offending column or columns and fix accordingly.

2. This time, instead of doing a CTAS operation we did an insert because we wanted our native Actian Data Platform table to use a timestamp for the timeperiod column.

    So, we referenced the column timeperiod as a varchar(20) data type from the external table side and a timestamp datatype from the Actian Data Platform table side.

    The insert then handles the mapping appropriately.

## Loading Parquet Data from AWS S3 Storage

Shown below is an example of how to load Parquet data stored on AWS S3 storage using external tables.

Example: Loading Parquet Data from AWS S3

```
DROP TABLE IF EXISTS pemdata_s3;
```

```
CREATE EXTERNAL TABLE pemdata_s3 (
```

```
    timeperiod VARCHAR(20),
```

```
    flow1 VARCHAR(20),
```

```
    flow2 VARCHAR(20),
```

```
    occupancy1 VARCHAR(20),
```

```
    speed1 VARCHAR(20)
```

```
) using spark
```

```
WITH
```

```
    reference='s3a://avpemdata/part*.parquet',
```

```
    format='parquet';
```

```

```

```
DROP TABLE IF EXISTS pemdata;
```

```
CREATE TABLE pemdata (
```

```
    timeperiod TIMESTAMP,
```

```
    flow1 VARCHAR(20),
```

```
    flow2 VARCHAR(20),
```

```
    occupancy1 VARCHAR(20),
```

```
    speed1 VARCHAR(20)
```

```
);
```

```

```

```
INSERT INTO pemdata SELECT * FROM pemdata_s3;
```
