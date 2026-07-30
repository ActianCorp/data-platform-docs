---
title: "Data Loading Roadmap: Choosing a Data Loading Method"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "Data_Loading_Roadmap_3a_Choosing_a_Data_Loading_Me.htm"
canonical_id: "actian-data-platform-data-loading-roadmap-3a-choosing-a-data-loading-me"
---

# Data Loading Roadmap: Choosing a Data Loading Method

There are a number of ways you can load data from external sources into the Actian Data Platform. Depending on your data source and location, choose a data loading method and follow the link to the appropriate how-to information.

| Your Data Source or Format | Data Location | Data Loading Method | UI-based | Recommended for Large Data Sizes (> 1 GB) | See |
| --- | --- | --- | --- | --- | --- |
| Delimited text | Desktop | Data Load (Azure and Google Cloud only) | ![](images/GreenCheckmark.png) | Not recommended over 100MB | [Data Load](../DataLoading/Data_Load.md) |
| Cloud storage | SQL |  | ![](images/GreenCheckmark.png) | [Loading Delimited Text Data from Cloud Data Storage](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md) |
| Cloud storage:•AWS S3•Azure Blob Storage•Google Cloud | Batch data loading | ![](images/GreenCheckmark.png) |  | [Batch Data Loading](../DataLoading/BatchDataLoad.md) |
| •JSON•NoSQL | Cloud storage | SQL |  | ![](images/GreenCheckmark.png) | [Loading JSON Data from Cloud Data Storage](../DataLoading/LoadingJSONData.md) |
| •Parquet•Avro•CSV•HIVE•ORC•JDBC | Cloud storage | SQL |  | ![](images/GreenCheckmark.png) | •[Loading Parquet Data from Cloud Data Storage](../DataLoading/LoadingParquet.md)•[Examples of Defining External Tables and Loading Data](../DataLoading/Examples_of_Defining_External_Tables_and_Loading.md) |
| Web applications | •NetSuite•Salesforce•ServiceNow | Batch data loading | ![](images/GreenCheckmark.png) |  | [Batch Data Loading](../DataLoading/BatchDataLoad.md) |
| Databases | Actian Zen | Batch data loading | ![](images/GreenCheckmark.png) |  | [Batch Data Loading](../DataLoading/BatchDataLoad.md) |

You may also choose between the following data loading methods.

Loading delimited text file data using the Actian Data Platform automated data integrations

- [Data Load](../DataLoading/Data_Load.md) (Azure and Google Cloud only)
- [Batch Data Loading](../DataLoading/BatchDataLoad.md)

    - –Using Actian Library Templates for Loading Data to Avalanche

Loading data from external tables in cloud storage using SQL

- [Overview of SQL-Based Data Loading](../DataLoading/OverviewSQLDataLoading.md)
- [Loading Delimited Text Data from Cloud Data Storage](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md)

- [Loading Parquet Data from Cloud Data Storage](../DataLoading/LoadingParquet.md)
- [Loading JSON Data from Cloud Data Storage](../DataLoading/LoadingJSONData.md)
