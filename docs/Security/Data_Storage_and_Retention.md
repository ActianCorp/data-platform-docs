---
title: "Data Storage and Retention"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Data_Storage_and_Retention.htm"
canonical_id: "actian-data-platform-data-storage-and-retention"
---

## Data Storage and Retention

The Actian Data Platform uses a write-once, one-block-per-blob data model. The data is stored as individual blocks, in cloud storage which guarantees at least 11 9s resiliency. See https://cloud.google.com/storage/docs/availability-durability for more details on storage availability.

!!! note "Note"

    We do not use dual or multi-region storage.

When data is written, the blocks are written out once and never update. Cloud storage uses an eventual consistency model, meaning blocks are not directly deleted. In this model, when data is deleted and/or updated, the corresponding blocks are marked for deletion and new blocks written. A separate garbage collection process asynchronously deletes the blocks marked for deletion based on a retention policy. The Actian Data Platform uses a default retention policy of 35 days, meaning any data deleted by user action will not physically be removed from cloud storage until at least 35 days after the user initiates the data deletion.

Additionally, cloud storage uses soft delete or blob versioning with a default retention policy of seven days. This means any data deleted as a result of software error or any other means can be restored for this additional period.

Warehouse deletion cloud storage buckets are retained for three days before being physically deleted.
