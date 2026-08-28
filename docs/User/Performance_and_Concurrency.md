---
title: "Performance and Concurrency"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Performance_and_Concurrency.htm"
canonical_id: "actian-data-platform-performance-and-concurrency"
---

## Performance and Concurrency

Actian Analytics Engine is the underlying database engine that powers the Actian Data Platform, enabling it to operate on hundreds of tuples of data. Massively Parallel Processing (MPP) architecture provides the coordinated processing of a single task by multiple processors communicating with each other using a messaging interface. This means that you can scale out to hundreds of nodes and petabytes of data. But the Actian Data Platform uses advanced columnar storage, which implements compression by data type, leading to 4–6x improved compression and a reduced data footprint.

To keep your data costs down, compute and storage are separated in the Actian Data Platform, so you pay only for what you use. For more information, see [Warehouse Cost and Actian Units](../User/Concepts_to_Understand.md).

Actian Data Platform performs analytical queries as the data warehouse is being updated without any performance degradation. The service is built for high volume of concurrent users, allowing up to 64 concurrent users.
