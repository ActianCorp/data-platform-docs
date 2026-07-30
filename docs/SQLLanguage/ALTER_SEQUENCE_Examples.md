---
title: "ALTER SEQUENCE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_SEQUENCE_Examples.htm"
canonical_id: "actian-data-platform-alter-sequence-examples"
---

## ALTER SEQUENCE Examples

Change sequence settings that were specified when the sequence was created:

1. Change the start value so that sequence “XYZ” starts at sequence item 10.

```
ALTER SEQUENCE XYZ RESTART WITH 10
```

2. Change the increment value of sequence “XYZ” to 20.

```
ALTER SEQUENCE XYZ INCREMENT BY 20
```
