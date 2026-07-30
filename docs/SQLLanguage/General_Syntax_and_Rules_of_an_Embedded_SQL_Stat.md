---
title: "General Syntax and Rules of an Embedded SQL Statement"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "General_Syntax_and_Rules_of_an_Embedded_SQL_Stat.htm"
canonical_id: "actian-data-platform-general-syntax-and-rules-of-an-embedded-sql-stat"
---

## General Syntax and Rules of an Embedded SQL Statement

An embedded SQL statement has the following format:

```
[margin] EXEC SQL SQL_statement [terminator]
```

When creating embedded SQL (ESQL) programs, remember the following points:

- The margin, consisting of spaces or tabs, is the margin that the host language compiler requires before the regular host code. Not all languages require margins.
- The keywords EXEC SQL must precede the SQL statement. EXEC SQL indicates to the embedded SQL preprocessor that the statement is an embedded SQL statement.

- The terminator, which indicates the end of the statement, is specific to the host language. Different host languages require different terminators and some, such as Fortran, do not require any.
- Embedded SQL statements can be continued across multiple lines according to the host language’s rules for line continuation.

- A label can precede an embedded statement if a host language statement in the same place can be preceded by a label. Nothing can be placed between the label and the EXEC SQL keywords.
- Host language comments must follow the rules for the host language.

Some host languages allow the placement of a line number in the margin.
