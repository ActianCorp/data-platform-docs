---
title: "Overview of SQL-Based Data Loading"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "OverviewSQLDataLoading.htm"
canonical_id: "actian-data-platform-overviewsqldataloading"
---

# Overview of SQL-Based Data Loading

This section is an overview containing information you need to know before using any of the following methods to load data from external tables in cloud storage using SQL:

- [Loading Delimited Text Data from Cloud Data Storage](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md)
- [Loading Parquet Data from Cloud Data Storage](../DataLoading/LoadingParquet.md)

- [Loading JSON Data from Cloud Data Storage](../DataLoading/LoadingJSONData.md)

To use the Actian SQL CLI for issuing SQL commands, see [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md).

The loading methods that Actian Data Platform supports are:

| Loading Method | Supported Clients | Performance | Supported Formats | Supported Object Stores |
| --- | --- | --- | --- | --- |
| COPY VWLOAD | •Actian SQL CLI•JDBC•ODBC | Fastest | Delimited text | •AWS S3•Azure Blob (General-purpose v2 accounts only)•Google Cloud•Gzipped delimited text |
| External Tables | •Actian SQL CLI•JDBC•ODBC | Fast | •Delimited text•Delimited text (gzipped)•JSON•Parquet | •AWS S3•Azure Blob (General-purpose v2 accounts only)•Google Cloud |

Here is an overview of each data loading method:

| Loading Method | Overview of Steps |
| --- | --- |
| COPY VWLOAD | 1.Set up cloud storage credentials.Follow the procedure for your cloud storage platform in [Set Up Access Credentials for Cloud Storage Accounts](../User/Set_Up_Access_Credentials_for_Cloud_Storage_Acco.md).2.Load data using the COPY VWLOAD statement.See [Loading Delimited Text Data Using COPY VWLOAD (SQL)](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md) and [COPY VWLOAD](../SQLLanguage/COPY_VWLOAD.md)). |
| External Tables | 1.Set up cloud storage credentials.Follow the procedure for your cloud storage platform in [Set Up Access Credentials for Cloud Storage Accounts](../User/Set_Up_Access_Credentials_for_Cloud_Storage_Acco.md).2.Specify your cloud storage credentials for your Actian warehouse.Follow the procedure for your cloud storage platform in [Grant Access to Warehouse or Database for External Tables Access](../User/Grant_Access_to_Warehouse_or_Database_for_Extern.md).3.Load data from external tables.Follow the procedure for your cloud storage platform in [Loading Delimited Text Data from External Tables (SQL)](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md). |

In addition to delimited text files, you can load Parquet and JSON data. See:

- [Loading Delimited Text Data from Cloud Data Storage](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md)
- [Loading Parquet Data from Cloud Data Storage](../DataLoading/LoadingParquet.md)

- [Loading JSON Data from Cloud Data Storage](../DataLoading/LoadingJSONData.md)

For more information, see [Grant Access to Warehouse or Database for External Tables Access](../User/Grant_Access_to_Warehouse_or_Database_for_Extern.md).
