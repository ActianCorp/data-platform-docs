---
title: "Loading JSON Data from Cloud Data Storage"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "LoadingJSONData.htm"
canonical_id: "actian-data-platform-loadingjsondata"
---

# Loading JSON Data from Cloud Data Storage

!!! note "Note"

    Before using this method, be sure to read [Overview of SQL-Based Data Loading](../DataLoading/OverviewSQLDataLoading.md).

You can load JSON data using the following loading method: [Loading JSON Data from External Tables (SQL)](../DataLoading/LoadingJSONData.md).

The cloud object stores that are currently supported are AWS S3, Azure Blob Storage, and Google Cloud.

To use the Actian SQL CLI for issuing SQL commands, see [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md).

External tables use Apache Spark underneath to reference and load external data into the Actian warehouse. This in turn has been wrapped in a native Actian Data Platform SQL command to aid ease of use.

## Loading JSON Data from Google Cloud Storage

Shown below is an example of how to load JSON data stored on Google Cloud Storage using external tables.

Example: JSON file

```
[
```

```
    {
```

```
        "sepalLength": 5.1,
```

```
        "sepalWidth": 3.5,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.9,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.7,
```

```
        "sepalWidth": 3.2,
```

```
        "petalLength": 1.3,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.6,
```

```
        "sepalWidth": 3.1,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.0,
```

```
        "sepalWidth": 3.6,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.4,
```

```
        "sepalWidth": 3.9,
```

```
        "petalLength": 1.7,
```

```
        "petalWidth": 0.4,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.6,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.3,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.0,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.4,
```

```
        "sepalWidth": 2.9,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.9,
```

```
        "sepalWidth": 3.1,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.4,
```

```
        "sepalWidth": 3.7,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.8,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.6,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.8,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.3,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.1,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.8,
```

```
        "sepalWidth": 4.0,
```

```
        "petalLength": 1.2,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.7,
```

```
        "sepalWidth": 4.4,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.4,
```

```
        "species": "setosa"
```

```
    }
```

```
]
```

Example: Loading JSON Data from Google Cloud Storage

```
DROP TABLE IF EXISTS irisdata_external;
```

```
CREATE EXTERNAL TABLE irisdata_external (
```

```
    sepalLength FLOAT,
```

```
    sepalWidth FLOAT,
```

```
    petalLength FLOAT,
```

```
    petalWidth FLOAT,
```

```
    species VARCHAR(20)) using spark
```

```
WITH
```

```
    reference='gs://avirisdata/iris.json',
```

```
    format='json',
```

```
    options=('multiLine'='true');
```

```

```

```
CREATE TABLE irisdata AS SELECT * FROM irisdata_external;
```

## Loading JSON Data from Azure Blob Storage

Shown below is an example of how to load JSON data stored on Azure Blob storage using external tables.

Example: JSON file

```
[
```

```
    {
```

```
        "sepalLength": 5.1,
```

```
        "sepalWidth": 3.5,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.9,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.7,
```

```
        "sepalWidth": 3.2,
```

```
        "petalLength": 1.3,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.6,
```

```
        "sepalWidth": 3.1,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.0,
```

```
        "sepalWidth": 3.6,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.4,
```

```
        "sepalWidth": 3.9,
```

```
        "petalLength": 1.7,
```

```
        "petalWidth": 0.4,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.6,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.3,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.0,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.4,
```

```
        "sepalWidth": 2.9,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.9,
```

```
        "sepalWidth": 3.1,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.4,
```

```
        "sepalWidth": 3.7,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.8,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.6,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.8,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.3,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.1,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.8,
```

```
        "sepalWidth": 4.0,
```

```
        "petalLength": 1.2,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.7,
```

```
        "sepalWidth": 4.4,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.4,
```

```
        "species": "setosa"
```

```
    }
```

```
]
```

Example: Loading JSON data from Azure Blob Storage

```
DROP TABLE IF EXIST irisdata_external;
```

```
CREATE EXTERNAL TABLE irisdata_external (
```

```
    sepalLength FLOAT,
```

```
    sepalWidth FLOAT,
```

```
    petalLength FLOAT,
```

```
    petalWidth FLOAT,
```

```
    species VARCHAR(20)) using spark
```

```
WITH
```

```
    reference='abfs://arisdata@mydata.dfs.core.windows.net/iris.json',
```

```
    format='json',
```

```
    options=('multiLine'='true');
```

```

```

```
CREATE TABLE irisdata AS SELECT * FROM irisdata_external;
```

Notes:

1. Before doing the CTAS (Create Table As Select) or load operation, ensure you can do a SELECT * FROM that external table.

    If this does not work, narrow down the offending column or columns in incremental steps by doing SELECT <column1>, <column2> FROM <external table>, and adding more columns as you go to find the offending column or columns.

2. To see the available JSON options:

    [https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html#csv-json.collection.Seq-](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html#csv-json.collection.Seq-)

## Loading JSON Data from AWS S3 Storage

Shown below is an example of how to load JSON data stored on AWS S3 storage using external tables.

Example: JSON file

```
[
```

```
    {
```

```
        "sepalLength": 5.1,
```

```
        "sepalWidth": 3.5,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.9,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.7,
```

```
        "sepalWidth": 3.2,
```

```
        "petalLength": 1.3,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.6,
```

```
        "sepalWidth": 3.1,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.0,
```

```
        "sepalWidth": 3.6,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.4,
```

```
        "sepalWidth": 3.9,
```

```
        "petalLength": 1.7,
```

```
        "petalWidth": 0.4,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.6,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.3,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.0,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.4,
```

```
        "sepalWidth": 2.9,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.9,
```

```
        "sepalWidth": 3.1,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.4,
```

```
        "sepalWidth": 3.7,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.8,
```

```
        "sepalWidth": 3.4,
```

```
        "petalLength": 1.6,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.8,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.4,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 4.3,
```

```
        "sepalWidth": 3.0,
```

```
        "petalLength": 1.1,
```

```
        "petalWidth": 0.1,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.8,
```

```
        "sepalWidth": 4.0,
```

```
        "petalLength": 1.2,
```

```
        "petalWidth": 0.2,
```

```
        "species": "setosa"
```

```
    },
```

```
    {
```

```
        "sepalLength": 5.7,
```

```
        "sepalWidth": 4.4,
```

```
        "petalLength": 1.5,
```

```
        "petalWidth": 0.4,
```

```
        "species": "setosa"
```

```
    }
```

```
]
```

Example: Loading JSON Data from AWS S3

```
DROP TABLE IF EXISTS irisdata_external;
```

```
CREATE EXTERNAL TABLE irisdata_external (
```

```
    sepalLength FLOAT,
```

```
    sepalWidth FLOAT,
```

```
    petalLength FLOAT,
```

```
    petalWidth FLOAT,
```

```
    species VARCHAR(20)) using spark
```

```
WITH
```

```
    reference='s3a://avirisdata/iris.json',
```

```
    format='json',
```

```
    options=('multiLine'='true');
```

```

```

```
CREATE TABLE irisdata AS SELECT * FROM irisdata_external;
```
