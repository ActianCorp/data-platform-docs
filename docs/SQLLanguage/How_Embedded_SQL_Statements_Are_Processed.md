---
title: "How Embedded SQL Statements Are Processed"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_Embedded_SQL_Statements_Are_Processed.htm"
canonical_id: "actian-data-platform-how-embedded-sql-statements-are-processed"
---

## How Embedded SQL Statements Are Processed

Embedded SQL statements are processed by an embedded SQL (ESQL) preprocessor, which converts the ESQL statements into host language source code statements. The resulting statements are calls to a runtime library that provides the interface to Actian Data Platform (host language statements are not altered by the ESQL preprocessor). After the program has been preprocessed, it must be compiled and linked according to the requirements of the host language.
