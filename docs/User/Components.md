---
title: "Components"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Components.htm"
canonical_id: "actian-data-platform-components"
---

## Components

The Sparkforce platform integrates with the following components to provide a comprehensive data development environment:

| Component | Purpose |
| --- | --- |
| Apache Spark | A distributed data processing engine that exposes dataframe and SparkSQL APIs. |
| Spark | A thin RPC-client architecture designed to decouple client applications from the Spark cluster. |
| Actian Analytics Engine | A high-performance analytics engine integrated through the Spark Catalog API, but also accessible via JDBC/ODBC |
| MLflow | A tool for managing the machine learning lifecycle, including experiment tracking, model registries, and model serving. |
| Code Server | A browser-based VS Code IDE that includes preinstalled Python and PySpark libraries. |
| Data lake connectors | Preconfigured storage drivers supporting GCS, AWS, Azure, Iceberg, and Delta. |
| MLlib | Apache Spark's built-in machine learning library. |

!!! note "Note"

    All external connections to the platform are secured with Transport Layer Security (TLS) and authenticated by using JSON Web Token (JWT) bearer tokens.
