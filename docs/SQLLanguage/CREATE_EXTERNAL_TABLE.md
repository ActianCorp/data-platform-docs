---
title: "CREATE EXTERNAL TABLE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_EXTERNAL_TABLE.htm"
canonical_id: "actian-data-platform-create-external-table"
---

## CREATE EXTERNAL TABLE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE EXTERNAL TABLE statement maps the structure of a data file created outside of Actian Data Platform to the structure of a Actian Data Platform table. The data can then be queried from its original locations.

This statement has the following format:

```
CREATE EXTERNAL TABLE [IF NOT EXISTS] [schema.]table_name
```

```
(column_name data_type {,column_name data_type})
```

```
USING provider_name
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

**IF NOT EXISTS**

:   Creates the external table if it does not exist and returns without error if the table already exists.

**Caution!**The table definition of a pre-existing table may differ from that of the CREATE EXTERNAL TABLE IF NOT EXISTS statement.

**table_name**

:   Defines the name of the external table to be created.

**column_name data_type**

:   Specifies the column name and data type of each column. Each column specification must be separated with a comma.

**USING provider_name**

:   Specifies the name of the provider. The only valid provider is SPARK.

**WITH REFERENCE='reference'**

:   (Required) Specifies the reference to the external data source. This corresponds to the parameter passed to the load method of DataFrameReader or the save method of DataFrameWriter. It is typically a fully qualified path or identifier defined by the target. For example:

:   For database systems: the table name

**FORMAT='format'**

:   (Optional) Is a WITH clause option that specifies the format of the external data. Formats include:

    - avro

    - csv

    - hive

    - jdbc

    - json

    - orc

    - parquet

:   For other data sources, formatcorresponds to the class name that defines that external data source. For example, for Redshift it would be com.databricks.spark.redshift. This corresponds to the parameter passed to the format method of DataFrameReader/Writer.

:   When FORMAT is not specified, Actian Data Platform tries to recognize the format by looking at the file extension. For example, my_file.orc is treated as an ORC file.

:   For more information, see [Examples of Defining External Tables and Loading Data](../DataLoading/Examples_of_Defining_External_Tables_and_Loading.md) and [Loading JSON Data from External Tables (SQL)](../DataLoading/LoadingJSONData.md).

**OPTIONS**

:   (Optional) Is a WITH clause option that specifies user-defined options for the datasource read or written to. This corresponds to the options method of the DataFrameReader/Writer. For example, for CSV files you can pass any options supported by spark-csv. For additional options supported by various external data sources, see the DataFrameReader documentation at [https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html).

:   Useful options are:

'HEADER'='TRUE' | 'FALSE'

:   Indicates whether the data file contains a header row.

'DELIMITER'='character'

:   Indicates the character used in the data file as the record delimiter. Example: 'delimiter'='|'

'schema'='schema'

:   Specifies the table column definitions of the source using SparkSQL types. We recommend specifying this if the source file being loaded does not contain a header row. If not specified, Spark tries to infer the schema, which can degrade performance.

**Note:**The keyword schema is case-sensitive; it must be lowercase.

**'STAGING'='SparkSQL query string'**

:   Specifies a SparkSQL query ([https://spark.apache.org/docs/latest/sql-ref.html](https://spark.apache.org/docs/latest/sql-ref.html)) that creates an intermediate table in Spark for cleaning data or mapping the schema on top of the source data before the data is transferred into the Actian Data Platform. It has the form of SELECT...FROM THIS_TABLE, where THIS_TABLE is a designated keyword. The schema of the staging table must exactly match the schema of the external table. For details, see the staging table examples in [CREATE EXTERNAL TABLE Examples](../SQLLanguage/Predicate_Pushdown.md).

!!! note "Note"

    The feature is limited to the Spark-Vector Provider version 3 supporting Spark 3.1.1.

**'FILTER'='SparkSQL filter predicates string'**

:   Allows for specifying filter predicates on top of the data source in SparkSQL syntax ([https://spark.apache.org/docs/latest/sql-ref.html](https://spark.apache.org/docs/latest/sql-ref.html)). These filters are evaluated by Spark. Spark itself determines which filters can be pushed down to the data source depending on its implementation. For details, see how filter predicates are used in [CREATE EXTERNAL TABLE Examples](../SQLLanguage/Predicate_Pushdown.md).
