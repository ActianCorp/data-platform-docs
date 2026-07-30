---
title: "Variable Declaration"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Variable_Declaration.htm"
canonical_id: "actian-data-platform-variable-declaration"
---

## Variable Declaration

Host language variables must be declared to SQL before using them in any embedded SQL statements. Host language variables are declared to SQL in a declaration section that has the following syntax:

```
EXEC SQL BEGIN DECLARE SECTION;        host language variable declarationsEXEC SQL END DECLARE SECTION;
```

A program can contain multiple declaration sections. The preprocessor treats variables declared in each declaration section as global to the embedded SQL program from the point of declaration onward, even if the host language considers the declaration to be in local scope.

The variable declarations are identical to any variable declarations in the host language, however, the data types of the declared variables must belong to a subset of host language data types that embedded SQL understands.

The Actian Data Platform automatically handles the conversion between host language numeric types and SQL numeric types, as well as the conversion between host language character string types and SQL character string types. To convert data between numeric and character types, use one of the explicit conversion functions described in [Default Type Conversion](../SQLLanguage/SQL_Operations.md).

!!! note "Note"

    Host language variables that are not declared to SQL are not processed by the ESQL preprocessor and therefore can include data types that the preprocessor does not understand.
