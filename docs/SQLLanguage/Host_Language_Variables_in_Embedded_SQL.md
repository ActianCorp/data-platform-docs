---
title: "Host Language Variables in Embedded SQL"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Host_Language_Variables_in_Embedded_SQL.htm"
canonical_id: "actian-data-platform-host-language-variables-in-embedded-sql"
---

## Host Language Variables in Embedded SQL

Embedded SQL allows the use of host language variables for many elements of embedded SQL statements. Host language variables can be used to transfer data between the database and the program or to specify the search condition in a WHERE clause.

In embedded SQL statements, host language variables can be used to specify the following elements:

- Database expressions. Variables can generally be used wherever expressions are allowed in embedded SQL statements, such as in target lists and predicates. Variables must denote constant values and cannot represent names of database columns or include any operators.
- Objects of the INTO clause of the SELECT and FETCH statements. The INTO clause is how values retrieved from the database are transferred to host language variables.

- Miscellaneous statement arguments. Many embedded SQL statement arguments can be specified using host language variables. For more information, see [SQL Statements](../SQLLanguage/SQL_Statements.md).

A host language variable can be a simple variable or a structure. All host language variables must be declared to embedded SQL before using them in embedded SQL statements.
