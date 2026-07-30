---
title: "SELECT (Embedded)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SELECT_(Embedded).htm"
canonical_id: "actian-data-platform-select-embedded"
---

## SELECT (Embedded)

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The SELECT statement returns values from tables to host language variables in an embedded SQL program.

For more information about the various clauses of the SELECT statement, see [SELECT (Interactive)](../SQLLanguage/SELECT_(Interactive).md).

The SELECT (embedded) statement has the following format:

Non-cursor version:

```
EXEC SQL [REPEATED] SELECT [FIRST rowCount] [ALL | DISTINCT]              SELECT [FIRST rowCount] [ALL | DISTINCT]              INTO variable[:indicator_var] {, variable[:indicator_var]}              [FROM from_source {, from_source}              [WHERE search_condition]              [GROUP BY [ALL | DISTINCT] grouping element {,grouping element}]              [HAVING search_condition]]              [UNION  [ALL] full_select]              [ORDER BY ordering-expression [ASC | DESC]                             {, ordering-expression [ASC | DESC]}]              [OFFSET n]              [FETCH FIRST|NEXT n ROWS|ROW ONLY]              [WITH options][EXEC SQL BEGIN;              program code;EXEC SQL END;]
```

Cursor version (embedded in a DECLARE CURSOR statement):

```
SELECT [ALL|DISTINCT]        SELECT [FIRST rowCount] [ALL | DISTINCT]       [FROM from_source {, from_source}       [WHERE search_condition]       [GROUP BY [ALL | DISTINCT] grouping element {,grouping element}]       [HAVING search_condition]       [UNION [ALL] full_select]       [ORDER BY result_column [ASC|DESC]               {, result_column [ASC|DESC]}]       [FOR [DEFERRED | DIRECT]];       [WITH options]
```

where result_expression is:

```
expression | result_name = expression | expression AS result_name
```
