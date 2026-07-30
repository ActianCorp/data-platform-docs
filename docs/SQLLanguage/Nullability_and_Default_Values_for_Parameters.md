---
title: "Nullability and Default Values for Parameters"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Nullability_and_Default_Values_for_Parameters.htm"
canonical_id: "actian-data-platform-nullability-and-default-values-for-parameters"
---

## Nullability and Default Values for Parameters

Database procedures can be called from embedded SQL applications or from interactive SQL. The caller supplies values for procedure parameters. The WITH DEFAULT, NOT DEFAULT, WITH NULL, and NOT NULL clauses can be used to specify whether parameters have default values and whether they are nullable.

These clauses have the following meanings for database procedure parameters:

**WITH DEFAULT**

:   The caller does not have to specify a value for the parameter. If the parameter is nullable, its default value is null. If the parameter is not nullable, its default value is 0 (for numeric data types) or blanks (for character data types).

**NOT DEFAULT**

:   The caller must specify a value for the parameter. If no value is specified, the Actian Data Platform issues an error.

**WITH NULL**

:   The parameter can be null.

**NOT NULL**

:   The parameter cannot be null.

The combined effects of these clauses are as follows:

| Parameter | Description |
| --- | --- |
| WITH NULL | The parameter can be null. If no value is provided, Actian Data Platform passes a null. |
| NOT NULL WITH DEFAULT | The parameter does not accept nulls. If no value is provided, Actian Data Platform passes 0 for numeric and money columns, or an empty string for character and date columns. |
| NOT NULL NOT DEFAULT orNOT NULL | The parameter is mandatory and does not accept nulls. |
| WITH NULL WITH DEFAULT | Not allowed. |
| WITH NULL NOT DEFAULT | Not allowed. |
| WITH DEFAULT | Not allowed without NOT NULL clause. |
| NOT DEFAULT | Not allowed without NOT NULL clause. |
