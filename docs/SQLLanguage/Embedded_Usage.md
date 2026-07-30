---
title: "Embedded Usage"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Embedded_Usage.htm"
canonical_id: "actian-data-platform-embedded-usage"
---

## Embedded Usage

The embedded [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md) statement is identical to its interactive version, with the following exceptions and additions:

- Braces { } cannot be used in place of the BEGIN and END clauses.
- All statements in the procedure must be separated by semicolons. The statement terminator after the final END clause follows the syntax of the host language.

- The CREATE PROCEDURE statement cannot contain any references to host language variables.
- The rules for the continuation of statements over multiple lines follow the embedded SQL host language rules. String literals, continued over multiple lines, also follow the host language rules.

- Comments in a procedure body follow the comment rules of the host language.
- The [INCLUDE](../SQLLanguage/INCLUDE.md) statement cannot be issued inside a database procedure. However, an include file can contain an entire CREATE PROCEDURE statement.

The SQL syntax of the CREATE PROCEDURE statement is validated at runtime, not by the preprocessor.
