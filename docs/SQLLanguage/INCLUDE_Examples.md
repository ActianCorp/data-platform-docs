---
title: "INCLUDE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "INCLUDE_Examples.htm"
canonical_id: "actian-data-platform-include-examples"
---

## INCLUDE Examples

1. Include the SQLCA in the program.

```
EXEC SQL INCLUDE SQLCA;
```

2. Include global variables.

```
EXEC SQL BEGIN DECLARE SECTION;           EXEC SQL INCLUDE 'global.var';     EXEC SQL END DECLARE SECTION;
```
