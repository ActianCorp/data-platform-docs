---
title: "INCLUDE Statement"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "INCLUDE_Statement.htm"
canonical_id: "actian-data-platform-include-statement"
---

## INCLUDE Statement

The embedded SQL INCLUDE statement allows external files to be included in your source code. The syntax of the INCLUDE statement is:

```
EXEC SQL INCLUDE filename
```

This statement is commonly used to include an external file containing variable declarations.

For example, assuming you have a file called, myvars.dec, that contains a group of variable declarations, use the INCLUDE statement in the following manner:

```
exec sql begin declare section;exec sql include 'myvars.dec';exec sql end declare section;
```

This is the functional equivalent of listing all the declarations in the myvars.dec file in the declaration section itself.
