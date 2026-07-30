---
title: "Statement Terminators"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Statement_Terminators.htm"
canonical_id: "actian-data-platform-statement-terminators"
---

## Statement Terminators

Statement terminators separate one SQL statement from another.

In interactive SQL, the statement terminator is the semicolon (;). Terminate statements with a semicolon when entering two or more SQL statements before issuing the go command (**\g**) or issuing another SQL CLI command.

In the following example, semicolons terminate the first and second statements. The third statement does not need to be terminated with a semicolon, because it is the final statement.

```
SELECT * FROM addrlst;SELECT * FROM emp     WHERE fname = 'john';SELECT * FROM emp     WHERE mgrname = 'dempsey'\g
```

If only one statement is entered, the statement terminator is not required. For example, the following single statement does not require a semicolon:

```
SELECT * FROM addrlst\g
```
