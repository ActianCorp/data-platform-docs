---
title: "Apache Spark and Spark Connect"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Apache_Spark_and_Spark_Connect.htm"
canonical_id: "actian-data-platform-apache-spark-and-spark-connect"
---

## Apache Spark and Spark Connect

Apache Spark serves as the distributed computing backbone of the Sparkforce platform. It is an open-source, distributed data-processing framework designed for speed and ease of use. Spark provides a unified engine for batch processing, stream processing, SQL queries, machine learning, and graph analysis. Under its lazy execution model, transformations on data frames are not executed immediately; instead, Spark constructs a directed acyclic graph (DAG) of operations and optimizes the execution plan before running it. For more information, see the [Spark documentation](https://spark.apache.org/docs/4.0.1/).

The Sparkforce platform uses a decoupled, lightweight, gRPC-based client to shift heavy data processing to the cluster, delivering scalable, cost-efficient performance suitable for diverse deployments, including mobile applications.

## Reading and Writing Data

Sparkforce includes preconfigured storage drivers for AWS, Azure, and GSC. Supported file formats include CSV, JSON, Parquet, ORC, Avro, and XML. The platform supports Apache Iceberg and Delta open table formats with full data definition language (DDL) operations through the Spark frontend. You can also access Iceberg and Delta tables through Analytics Engine external tables for read and append operations.

## Accelerating Data Lake Access with Actian Analytics Engine

Sparkforce implements the Spark Catalog API, ensuring Actian Analytics Engine tables appear as first-class Spark tables. The warehouse database is preconfigured and accessible directly through the catalog name analytics_engine.

For example:

```
SELECT * FROM analytics_engine.lineitem.
```

## Metering and Billing

Each Spark job is metered individually based on its own resource configuration and runtime duration. Consumption is calculated from the resources requested by the executor pods assigned to that job, rather than actual instantaneous usage. This per-job metering approach gives administrators accurate cost attribution at the job level and encourages you to provision only the resources that each workload requires.
