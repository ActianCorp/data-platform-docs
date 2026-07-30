---
title: "CSV Files"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "CSV_Files.htm"
canonical_id: "actian-data-platform-csv-files"
---

## CSV Files

The following examples illustrate:

- Creating external tables for data files in CSV format residing on Amazon S3
- Two scenarios for working with CSV files: one with and one without a header row

- Loading the data into an Actian Data Platform table after the external table is created

### Small Data Set

A small dataset is usually represented by data of fewer than 150 GB (uncompressed). Small dimension tables usually fit into this category.

For this example, we have a file nation.csv residing on Amazon S3, where the data looks like the following.

#### Data file with a header row

```
n_nationkey|n_name|n_regionkey
```

```
0|ALGERIA|0
```

```
1|ARGENTINA|1
```

```
2|BRAZIL|1
```

```
3|CANADA|1
```

```
4|EGYPT|4
```

To create the external table for a file with a header row:

1. Create the external table:

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
   n_regionkey INTEGER NOT NULL,
```

```
   n_comment VARCHAR(152) NOT NULL
```

```
) USING SPARK WITH
```

```
REFERENCE='s3a://<bucket>/nation.tbl*',FORMAT='csv',OPTIONS=('header'='true',
```

```
'delimiter'='|');
```

**IMPORTANT!**Ensure that your external table column names match the names used for columns in your source data header row.

    You can now manipulate the data using standard SQL against the external table.

To load the data into the Actian Data Platform:

2. Create the native Actian Data Platform table:

```
CREATE TABLE nation (
```

```
   n_nationkey INTEGER NOT NULL,
```

```
   n_name CHAR(25) NOT NULL,
```

```
   INTEGER NOT NULL,
```

```
   n_comment VARCHAR(152) NOT NULL
```

```
) WITH NOPARTITION;
```

3. Load the table with an INSERT command:

```
INSERT INTO nation SELECT * FROM nation_s3;
```

    This statement reads the data from the external table nation_s3, which points to the data on an S3 bucket and inserts it into the native Actian Data Platform table “nation”.

After the data is loaded, we recommend that you run the CREATE STATISTICS command on the Actian Data Platform table: `CREATE STATISTICS FOR nation;`

#### Data file without a header row

In this example, the file does not have a header row.

```
0|ALGERIA|0
```

```
1|ARGENTINA|1
```

```
2|BRAZIL|1
```

```
3|CANADA|1
```

```
4|EGYPT|4
```

If the CSV file does not have a header, you must set “header=false” in your external table declaration and explicitly specify the CSV schema:

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
) USING SPARK WITH REFERENCE='s3a://<bucket>/nation.csv',FORMAT='csv',OPTIONS=('header'=false,'delimiter'='|','schema'='n_nationkey INT NOT NULL, n_name STRING NOT NULL, n_regionkey INT NOT NULL');
```

!!! note "Note"

    The column names in the schema must match the column names of the external table. The Spark data type specified in the schema must be compatible with the Actian Data Platform data type for the matching column. For Actian Data Platform to Spark data type mapping, see [Actian Data Platform to Spark Data Type Mapping](../DataLoading/AvalancheSparkMapping.md).

The Steps 2 and 3 remain the same as before.

!!! note "Note"

    If your data is split across multiple files, such as nation.csv.1, nation.csv.2, and so on, you can use a wildcard expression (nation.csv.*) to select multiple files or folders in your external table SQL declaration.

After the data is loaded, we recommend that you run the CREATE STATISTICS command on the Actian Data Platform table: `CREATE STATISTICS FOR nation;`

### Large Data Set

If your data is larger than 150 GB (uncompressed), which is usually the case with fact tables, and you want to load the data into the Actian Data Platform, then you must specify a partitioning clause and a partitioning key when creating the native Actian Data Platform table.

We will walk through two scenarios for working with CSV files: one with and one without a header row.

#### Data with a header row

To illustrate this case, we use the example of a manufacturing parts table CSV file residing on Amazon S3, where the data looks like this:

```
p_partkey|p_name|p_mfgr|p_brand|p_type|p_size|p_container|p_retailprice
```

```
1|goldenrod lace spring peru powder|Manufacturer#1|Brand#13|PROMO BURNISHED COPPER|7|JUMBO PKG|901.00
```

```
2|blush rosy metallic lemon navajo|Manufacturer#1|Brand#13|LARGE BRUSHED BRASS|1|LG CASE|902.00
```

```
3|dark green antique puff wheat|Manufacturer#4|Brand#42|STANDARD POLISHED BRASS|21|WRAP CASE|903.00
```

```
4|chocolate metallic smoke ghost drab|Manufacturer#3|Brand#34|SMALL PLATED BRASS|14|MED DRUM|904.00
```

```
5|forest blush chiffon thistle chocolate|Manufacturer#3|Brand#32|STANDARD POLISHED TIN|15|SM PKG|905.00
```

```
6|white ivory azure firebrick black|Manufacturer#2|Brand#24|PROMO PLATED STEEL|4|MED BAG|906.00
```

```
7|blue blanched tan indian olive|Manufacturer#1|Brand#11|SMALL PLATED COPPER|45|SM BAG|907.00
```

```
8|ivory khaki cream midnight rosy|Manufacturer#4|Brand#44|PROMO BURNISHED TIN|41|LG DRUM|908.00
```

Let us assume that the data is split across multiple CSV files: part.csv.1, part.csv.2, and so on.

To create the external table for data with a header row:

1. Create the external table:

```
CREATE EXTERNAL TABLE part_s3 (
```

```
   p_partkey INTEGER NOT NULL,
```

```
   p_name VARCHAR(55) NOT NULL,
```

```
   p_mfgr CHAR(25) NOT NULL,
```

```
   p_brand CHAR(10) NOT NULL,
```

```
   p_type VARCHAR(25) NOT NULL,
```

```
   p_size INTEGER NOT NULL,
```

```
   p_container CHAR(10) NOT NULL,
```

```
   p_retailprice DECIMAL(18,2) NOT NULL,
```

```
   p_comment VARCHAR(23) NOT NULL
```

```
) USING SPARK WITH
```

```
REFERENCE='s3a://<bucket>/part.tbl*',FORMAT='csv',OPTIONS=('header'='true','delimiter'='|');
```

!!! warning "Important"

    **IMPORTANT!**Ensure that your external table column names match the names used for columns in your source data header row.

    You can now manipulate the data using standard SQL against the external table.

To load the data into the Actian Data Platform:

2. Create the native Actian Data Platform table.

    Because the data is large, we want to distribute (partition) it for optimal performance.

    The Actian Data Platform supports a hash distribution scheme and requires a partition key to be specified. For more information about partitioning and choosing a partitioning key, see [Partitioned Tables](../SQLLanguage/CREATE_TABLE.md) in the SQL Language Guide.

    In this case, we will use p_partKey for hash distribution, and the CREATE TABLE statement for table part will look like:

```
CREATE TABLE part (column_specification {, column_specification }) WITH PARTITION =(HASH ON p_partkey DEFAULT PARTITIONS);
```

    We recommend using default partitions and not specifying a partition number. Using default partitions automatically chooses an ideal value based on your warehouse size.

```
CREATE TABLE part (
```

```
   p_partkey INTEGER NOT NULL,
```

```
   p_name VARCHAR(55) NOT NULL,
```

```
   p_mfgr CHAR(25) NOT NULL,
```

```
   p_brand CHAR(10) NOT NULL,
```

```
   p_type VARCHAR(25) NOT NULL,
```

```
   p_size INTEGER NOT NULL,
```

```
   p_container CHAR(10) NOT NULL,
```

```
   p_retailprice DECIMAL(18,2) NOT NULL,
```

```
   p_comment VARCHAR(23) NOT NULL
```

```
) WITH PARTITION=(HASH ON p_partkey DEFAULT PARTITIONS);
```

3. Load the table with an INSERT command:

```
INSERT INTO part SELECT * FROM part_s3;
```

    This statement reads the data from the external table part_s3, which points to the data on an S3 bucket and inserts it into the native Actian Data Platform table part.

    This will load the part data into the database and, depending on the data size and the cluster size, could take a few minutes to a few hours.

After the data is loaded, we recommend that you run the CREATE STATISTICS command on the Actian Data Platform table: `CREATE STATISTICS FOR part;`

#### Data without a header row

This example uses the same scenario as above, but without a header row.

```
1|goldenrod lace spring peru powder|Manufacturer#1|Brand#13|PROMO BURNISHED COPPER|7|JUMBO PKG|901.00
```

```
2|blush rosy metallic lemon navajo|Manufacturer#1|Brand#13|LARGE BRUSHED BRASS|1|LG CASE|902.00
```

```
3|dark green antique puff wheat|Manufacturer#4|Brand#42|STANDARD POLISHED BRASS|21|WRAP CASE|903.00
```

```
4|chocolate metallic smoke ghost drab|Manufacturer#3|Brand#34|SMALL PLATED BRASS|14|MED DRUM|904.00
```

```
5|forest blush chiffon thistle chocolate|Manufacturer#3|Brand#32|STANDARD POLISHED TIN|15|SM PKG|905.00
```

```
6|white ivory azure firebrick black|Manufacturer#2|Brand#24|PROMO PLATED STEEL|4|MED BAG|906.00
```

```
7|blue blanched tan indian olive|Manufacturer#1|Brand#11|SMALL PLATED COPPER|45|SM BAG|907.00
```

```
8|ivory khaki cream midnight rosy|Manufacturer#4|Brand#44|PROMO BURNISHED TIN|41|LG DRUM|908.00
```

Since there is no header row, we need to set 'header'='false' and explicitly specify a schema in the options.

To create the external table for data without a header row:

1. Create the external table:

```
CREATE EXTERNAL TABLE part_s3 (
```

```
   p_partkey INTEGER NOT NULL,
```

```
   p_name VARCHAR(55) NOT NULL,
```

```
   p_mfgr CHAR(25) NOT NULL,
```

```
   p_brand CHAR(10) NOT NULL,
```

```
   p_type VARCHAR(25) NOT NULL,
```

```
   p_size INTEGER NOT NULL,
```

```
   p_container CHAR(10) NOT NULL,
```

```
   p_retailprice DECIMAL(18,2) NOT NULL,
```

```
   p_comment VARCHAR(23) NOT NULL
```

```
) USING SPARK WITH REFERENCE='s3a://<bucket>/part.tbl*',FORMAT='csv',OPTIONS=('header'='false','delimiter'='|','schema'='p_partkey int NOT NULL, p_name string NOT NULL, p_mfgr string NOT NULL, p_brand string NOT NULL, p_type string NOT NULL, p_size int NOT NULL, p_container string NOT NULL, p_retailprice double NOT NULL, p_comment string NOT NULL');
```

!!! note "Note"

    The column names in the schema must match the column names of the external table. The Spark data type specified in the schema must be compatible with the Actian Data Platform data type for the matching column. See [Actian Data Platform to Spark Data Type Mapping](../DataLoading/AvalancheSparkMapping.md).

    You can now manipulate the data using standard SQL against the external table.

To load the data into the Actian Data Platform:

2. Create the native Actian Data Platform table:

```
CREATE TABLE part (
```

```
   p_partkey INTEGER NOT NULL,
```

```
   p_name VARCHAR(55) NOT NULL,
```

```
   p_mfgr CHAR(25) NOT NULL,
```

```
   p_brand CHAR(10) NOT NULL,
```

```
   p_type VARCHAR(25) NOT NULL,
```

```
   p_size INTEGER NOT NULL,
```

```
   p_container CHAR(10) NOT NULL,
```

```
   p_retailprice DECIMAL(18,2) NOT NULL,
```

```
   p_comment VARCHAR(23) NOT NULL
```

```
) WITH PARTITION=(HASH ON p_partkey DEFAULT PARTITIONS);
```

3. Load the table with an INSERT command:

```
INSERT INTO part SELECT * FROM part_s3;
```

    This statement reads the data from the external table part_s3, which points to the data on an S3 bucket and inserts it into the native Actian Data Platform table part.

    This will load the part data into the database and, depending on the data size and the cluster size, could take a few minutes to a few hours.

After the data is loaded, we recommend that you run the CREATE STATISTICS command on the Actian Data Platform table: `CREATE STATISTICS FOR part;`
