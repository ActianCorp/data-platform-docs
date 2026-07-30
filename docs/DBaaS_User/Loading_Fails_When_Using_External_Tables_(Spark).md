---
title: "Loading Fails When Using External Tables (Spark)"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Loading_Fails_When_Using_External_Tables_(Spark).htm"
canonical_id: "actian-data-platform-loading-fails-when-using-external-tables-spark"
---

## Loading Fails When Using External Tables (Spark)

This issue applies to both AWS AV-1 and Azure.

When you perform a CTAS operation to load data, such as:

```
create table ontime as select * from ontime_adl with partition=(hash on flightnum default partitions)
```

the following error is issued:

```
java.sql.SQLException: Error during communication with external table provider.
```

**Workaround**

Re-enter your Azure Storage or AWS S3 credentials, depending on which cloud platform you are using, and then retry the SQL statement. Alternatively, you can stop and restart the warehouse. For more information, see Stop a Warehouse and Restart a Warehouse.
