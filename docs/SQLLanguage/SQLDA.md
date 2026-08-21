---
title: "SQLDA"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQLDA.htm"
canonical_id: "actian-data-platform-sqlda"
---

## SQLDA

The descriptor area, called the SQLDA (SQL Descriptor Area), is a host language structure used by dynamic SQL. Dynamic SQL uses the SQLDA to store information about each result column of the SELECT statement and to store descriptive information about program variables. Use the SQLDA when executing a DESCRIBE statement, a PREPARE statement, an EXECUTE statement, or EXECUTE IMMEDIATE statement.

### Structure of the SQLDA

Typically, storage for the SQLDA structure is allocated at runtime. If a program allows several dynamically defined cursors to be opened at one time, the program can allocate several SQLDA structures, one for each SELECT statement, and assign each structure a different name.

Each host language has different considerations for the SQLDA structure.

The layout of the SQLDA is shown in the following table:

| SQLDA Structure | Description |
| --- | --- |
| sqldaid | 8-byte character array assigned the blank-padded value SQLDA. |
| sqldabc | 4-byte integer assigned the size of the SQLDA. |
| sqln | 2-byte integer indicating the number of allocated sqlvar elements. This value must be set by the program before describing a statement, form, or table field. The value must be greater than or equal to zero. |
| sqld | 2-byte integer indicating the number of result columns associated with the DESCRIBE statement. This number specifies how many of the allocated sqlvar elements were used to describe the statement. If sqld is greater than sqln, the program must reallocate the SQLDA to provide more storage buffers and reissue the DESCRIBE statement.To use the SQLDA to place values in a table, the program must set sqld to the correct number before the SQLDA is used in a statement.When describing a dynamic SQL statement, if the value in sqld is zero, the described statement is not a SELECT statement. |
| sqlvar | A sqln-size array composed of the following elements:<br>• **sqltype** – 2-byte integer indicating the length data type of the column, variable, or field.<br>• **sqllen** – 2-byte integer indicating the length of the column, variable, or field.<br>• **sqldata** – Pointer.<br>• **sqlind** – Pointer to indicator variable associated with the host language variable. Your program must also allocate the memory to which this variable points.<br>• **sqlname** – The result column name (when a SELECT statement is described). |

### Including the SQLDA in a Program

To define the SQLDA, your application must issue the following INCLUDE statement:

```
EXEC SQL INCLUDE SQLDA;
```

Do not place this statement in a declaration section.

In most host languages, this statement incorporates a set of type definitions that can be used to define the SQLDA structure; in some host languages it declares the structure. If the structure is declared directly (instead of using the INCLUDE statement), any name can be specified for the structure.

More than one SQLDA-type structure is allowed in a program. A dynamic FRS describe statement and a dynamic SQL statement can use the same SQLDA structure if the described form fields or table field columns have the same names, lengths, and data types as the columns of the database table specified in the dynamic SQL statement.

### DESCRIBE Statement and SQLDA

The DESCRIBE statement loads descriptive information about a prepared SQL statement, a form, or the table field of a form into the SQLDA structure. There are three versions of this statement, one for each type of object (statement, form, table field) that can be described.

Dynamic SQL uses the DESCRIBE statement to return information about the result columns of a SELECT statement. Describing a select tells the program the data types, lengths, and names of the columns retrieved by the select. If statements that are not SELECT statements are described, a 0 is returned in the sqld field, indicating that the statement was not a SELECT statement. For a complete discussion of how to use describe in a dynamic SQL application, see [Prepare and Describe SELECT Statements](../SQLLanguage/Execute_a_Dynamic_SELECT_Statement.md).

### Data Type Codes

The DESCRIBE statement returns a code indicating the data type of a field or column. This code is returned in sqltype, one of the fields in an sqlvar element.

The following table lists the data type codes. If a type code is negative, the column, variable, or field described by the sqlvar element is nullable.

| Data Type Name | Data Type Code | Nullable |
| --- | --- | --- |
| char | 20 | No |
|  | -20 | Yes |
| ansidate | 3 | No |
|  | -3 | Yes |
| decimal | 10 | No |
|  | -10 | Yes |
| float | 31 | No |
|  | -31 | Yes |
| integer | 30 | No |
|  | -30 | Yes |
| money | 5 | No |
|  | -5 | Yes |
| varchar | 21 | No |
|  | -21 | Yes |
