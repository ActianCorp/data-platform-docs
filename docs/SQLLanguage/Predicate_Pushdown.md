---
title: "Predicate Pushdown"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Predicate_Pushdown.htm"
canonical_id: "actian-data-platform-predicate-pushdown"
---

## Predicate Pushdown

Actian Data Platform to Spark

If a SQL query is issued to an EXTERNAL TABLE using Spark, predicates from the WHERE clause may already be evaluated by Spark, reducing the number of tuples sent. However, currently this works only under the following circumstances:

- It is implemented for all column data types except “time with time zone” and “timestamp with timezone.”
- Supported predicates are: <, <=, =, >=, and >. Using “like” is currently unsupported. Only predicates that can be translated into a column value range are supported.

- For logical connections of simple predicates:

    - –AND is supported on a single column and across columns

    - –OR is supported only on a single column

    - –IN is supported

    Where the whole complex predicate contains a single OR spanning different columns, nothing is pushed down to Spark. In this case, Spark transfers all tuples to the Actian Data Platform, and the filtering is done solely on the Actian Data Platform side.

Predicate pushdown is considered only from Actian Data Platform to Spark. The predicate evaluation on the Spark side is determined by the Spark framework. How far Spark and its internal optimizer push down predicates (how close to the source) depends on the specific file format and the Spark version. For example, in Spark 2, Parquet files may already be filtered during parsing, but this is not possible for CSV files. Filtering during CSV file parsing is supported in Spark 3.

Spark to Data Source

Predicate pushdown is considered only from Actian Data Platform to Spark. On the Spark side, predicate pushdown to the data source is determined by the optimizer framework of Spark. It depends on the specific file format, the data source implementation, and the Spark version. For example, in Spark 2, Parquet files may already be filtered during parsing, but this is not possible for CSV files. Filtering during CSV file parsing is supported in Spark 3.

## CREATE EXTERNAL TABLE Examples

!!! note "Note"

    The column names in the Actian Data Platform external table must match the column names in the reference source.

1. Define an external table for a CSV data source residing in Amazon S3:

```
CREATE EXTERNAL TABLE ext_csv (col1 INT4 NOT NULL, col2 VARCHAR(20) NOT NULL)
```

```
USING SPARK
```

```
WITH REFERENCE='s3a://<bucket>/file.csv'
```

```
 OPTIONS=('DELIMITER' = '|', 'HEADER' = 'TRUE','SCHEMA'='col1 INT4 NOT NULL, col2 VARCHAR(20) NOT NULL');
```

    **Notes:**

    - If the CSV file does not have a header, the name of the columns in the external table must match those in spark-csv, that is, C0, C1, .... If the option 'HEADER' = 'TRUE' is not specified and the Actian Data Platform external table definition has different names, you will get an error like:

```
E_VW1213 External table provider reported an error
```

```
'org.apache.spark.sql.AnalysisException: cannot resolve 'a' given input columns C0, C1; line 1 pos 38'.
```

    - If external table columns are defined as NOT NULL, the table schema must be specified with NOT NULL in the SCHEMA option, even if header is set to true. This is because if Spark SQL implicitly determines the schema information from, for example, a CSV file, the nullability of columns typically defaults to true.

2. Define an external table for a CSV data source residing in Amazon S3. The CSV data does not have a header row:

```
CREATE EXTERNAL TABLE nation_s3 (
```

```
   n_nationkey INTEGER NOT NULL,
```

```
   n_name CHAR(25) NOT NULL,
```

```
   n_regionkey INTEGER NOT NULL
```

```
) USING SPARK WITH REFERENCE='s3a://<bucket>/nation.csv',FORMAT='csv',
```

```
OPTIONS=('HEADER'='FALSE','DELIMITER'='|','SCHEMA'='n_nationkey INT NOT NULL, n_name STRING NOT NULL, n_regionkey INT NOT NULL');
```

!!! note "Note"

    The column names in the schema must match the column names of the external table. The Spark data type specified in the schema must be compatible with the Actian Data Platform data type for the matching column. See [Actian Data Platform to Spark Data Type Mapping](../DataLoading/AvalancheSparkMapping.md).

3. Define an external table for an ORC data source from Azure:

```
CREATE EXTERNAL TABLE my_table_orc(a INT8 NOT NULL)
```

```
USING SPARK WITH REFERENCE='abfs://loadtest@avalanchetest.dfs.core.windows.net/my_table.orc';
```

4. Define an external table for an AVRO data source from Azure:

```
CREATE EXTERNAL TABLE tweets
```

```
(username VARCHAR(20),
```

```
tweet VARCHAR(100),
```

```
timestamp VARCHAR(50))
```

```
USING SPARK
```

```
WITH REFERENCE='abfs://loadtest@avalanchetest.dfs.core.windows.net/twitter.avro',
```

```
FORMAT='com.databricks.spark.avro'
```

5. Define an external table for a JSON data source:

    Example JSON file:

```
[{
```

```
     "symbol": "MSFT",
```

```
     "company": "Microsoft Corporation",
```

```
     "stock_tstamp": "2020-01-31T21:00:00+00:00",
```

```
     "price": 170.777,
```

```
     "volume": 36142690,
```

```
     "sector": "TECH"
```

```
},
```

```
{
```

```
     "symbol": "AAPL",
```

```
     "company": "Apple Inc.",
```

```
     "stock_tstamp": "2020-01-31T21:00:00+00:00",
```

```
     "price": 309.51,
```

```
     "volume": 49897096,
```

```
     "sector": "TECH"
```

```
},
```

```
{
```

```
     "symbol": "GOOG",
```

```
     "company": "Alphabet Inc.",
```

```
     "stock_tstamp": "2020-01-31T21:00:00+00:00",
```

```
     "price": 1434.23,
```

```
     "volume": 2417214,
```

```
     "sector": "TECH"
```

```
},
```

```
{
```

```
     "symbol": "AMZN",
```

```
     "company": "Amazon.com, Inc.",
```

```
     "stock_tstamp": "2020-01-31T21:00:00+00:00",
```

```
     "price": 2008.72,
```

```
     "volume": 15567283,
```

```
     "sector": "TECH"
```

```
}]
```

    Example SQL to create an external table to reference that JSON file stored on an Azure ADL:

```
CREATE EXTERNAL TABLE techstocks (
```

```
     symbol VARCHAR(4),
```

```
     company VARCHAR(20),
```

```
     stock_tstamp TIMESTAMP,
```

```
     price FLOAT,
```

```
     volume INTEGER,
```

```
     sector CHAR(5)
```

```
) USING SPARK WITH REFERENCE='abfs://stockquotes@eastusstockdata.dfs.core.windows.net/tech1.json',
```

```
     FORMAT='json',
```

```
     OPTIONS=(
```

```
     'multiline'='true',
```

```
     'SCHEMA'= 'symbol string, company string, stock_tstamp string, price double, volume integer, sector string');
```

!!! note "Note"

    In JSON, dates are not dates but strings. See [https://weblog.west-wind.com/posts/2014/jan/06/javascript-json-date-parsing-and-real-dates](https://weblog.west-wind.com/posts/2014/jan/06/javascript-json-date-parsing-and-real-dates).

6. Define an external table for a CSV data source residing in Google Cloud Storage. The CSV data has no header row:

```
CREATE EXTERNAL TABLE stations (    n_stationkey INTEGER NOT NULL,     n_stationname CHAR(25) NOT NULL,     n_locationkey INTEGER NOT NULL) USING SPARK WITH REFERENCE='gs://<path>/stations.csv',FORMAT='csv',OPTIONS=('HEADER'='FALSE','DELIMITER'='|','SCHEMA'='n_stationkey INT NOT NULL, n_stationname STRING NOT NULL, n_locationkey INT NOT NULL');
```

!!! note "Note"

    The column names in the schema must match the column names of the external table. The Spark data type specified in the schema must be compatible with the Actian Data Platform data type for the matching column. See [Actian Data Platform to Spark Data Type Mapping](../DataLoading/AvalancheSparkMapping.md).

7. Remove all rows where text column contains NULL character. The filtering is done completely on the Spark side with possible predicate pushdown to the data source:

```
CREATE EXTERNAL TABLE filter_test(id INT, text VARCHAR(20))
```

```
USING SPARK WITH REFERENCE='test.csv',
```

```
FORMAT='csv',
```

```
OPTIONS=(
```

```
'header'='false',
```

```
'schema'='id Integer, text String',
```

```
'filter'='text NOT LIKE "%\\u0000%"'
```

```
);
```

8. Create an external table test_ext referencing a table test in another Actian warehouse:

```
CREATE EXTERNAL TABLE test_ext(id Int, text VARCHAR(20))
```

```
USING SPARK WITH REFERENCE='dummy',
```

```
FORMAT='vector',
```

```
OPTIONS=(
```

```
'host'='localhost',
```

```
'port'='VW7',
```

```
'database'='testdb',
```

```
'table'='test',
```

```
'user'='actian',
```

```
'password'='actian',
```

```
'staging'='select id, replace(text, "e", "i") as text from THIS_TABLE',
```

```
);
```

    Staging SparkSQL creates an intermediate table that does string replacement. THIS_TABLE is a designated keyword.

9. Map schema by simply unnesting a nested parquet file:

```
CREATE EXTERNAL TABLE unnested(id INT, name VARCHAR(20), surname VARCHAR(20))
```

```
USING SPARK WITH REFERENCE='nested.parquet',
```

```
FORMAT='parquet',
```

```
OPTIONS=(
```

```
   'SCHEMA'='id integer, fullname struct(name string, surname string)',
```

```
   'STAGING'='select id, fullname.name as name, fullname.surname as surname from THIS_TABLE'
```

```
);
```

    SCHEMA describes the nested schema of the referenced parquet file. STAGING maps the source schema onto the schema of the external table.

    Notes:

    - The schema of the staging table must match the schema of the external table.

    - In the staging table expression, you can use all functions provided by SparkSQL ([https://spark.apache.org/docs/3.1.1/api/sql/index.html](https://spark.apache.org/docs/3.1.1/api/sql/index.html)). However, using NOT, AND, or OR in a WHERE clause could raise an exception if Spark decides for predicate pushdown, because the Spark-Vector Provider does not currently support pushdown of those predicates.

    - This feature is available for Spark Provider 3 only.
