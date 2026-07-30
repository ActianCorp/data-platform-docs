---
title: "CREATE SEQUENCE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_SEQUENCE_Examples.htm"
canonical_id: "actian-data-platform-create-sequence-examples"
---

## CREATE SEQUENCE Examples

1. Define the start value for sequence “XYZ” as 10.

```
CREATE SEQUENCE XYZ START WITH 10
```

2. Define the increment value for sequence “XYZ” as 10 and the number of cached values as 500.

```
CREATE SEQUENCE XYZ INCREMENT BY 10 CACHE 500
```

3. Define a sequence with 32-bit integer capacity.

```
CREATE SEQUENCE seq1 AS INTEGER
```

4. Define a sequence with a 64-bit integer capacity (depending on declared sequence attributes).

```
CREATE SEQUENCE biggerseq1 AS BIGINT
```
