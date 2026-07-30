---
title: "SQL Operations"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_Operations.htm"
canonical_id: "actian-data-platform-sql-operations"
---

## SQL Operations

The basic SQL operations include:

- String concatenation operations
- Assignment operations

- Arithmetic operations

## String Concatenation Operations

To concatenate strings, use either the operator **+** or **||**.

For example:

```
'This ' + 'is ' + 'a ' + 'test.'
```

gives the value:

```
'This is a test.'
```

Likewise:

```
'Hello ' || 'World'
```

gives the value:

```
'Hello World'
```

Also, the concat function can be used to concatenate strings. For more information, see [String Functions](../SQLLanguage/SQL_Functions.md).

## Assignment Operations

An assignment operation places a value in a column or variable. Assignment operations occur during the execution of INSERT, UPDATE, ...AS SELECT, and embedded SELECT statements.

The data types of the assigned value and the receiving column or variable must either be the same or comparable.

- If the data types are not the same, comparable data types are converted.
- If the data types are not comparable, convert the assignment value into a type that is the same or comparable with the receiving column or variable.

For information about the type conversion functions, see [Default Type Conversion](../SQLLanguage/SQL_Operations.md).

### Character String Assignments

All character types are comparable with one another and with integer, decimal, and float types. Any character string can be assigned to any column or variable of character data type. A character string can also be assigned to a column or variable of integer, decimal, or float type, as long as the content of the string is a valid numeric value. The result of the assignment depends on the types of the assignment string and the receiving column or variable.

| Assigned String | Receiving Column or Variable | Description |
| --- | --- | --- |
| Fixed-length (c or char) | Fixed-length | **Note:**The assigned string is truncated or padded with spaces if the receiving column or variable is not the same length as the fixed length string. If the assigned string is truncated to fit into a host variable, a warning condition is indicated in SQLWARN. For a discussion of the SQLWARN indicators, see SQL Communications Area (SQLCA). |
| Fixed-length | Variable-length (varchar, long varchar, or text) | The trailing spaces are trimmed. If the receiving column or variable is shorter than the fixed length string, the fixed length string is truncated from the right side. If the assignment was to a variable, a warning condition is indicated in SQLWARN. For a discussion of the SQLWARN indicators, see SQL Communications Area (SQLCA).**Note:**If a long varchar value over is assigned to another character data type, the result is truncated at the maximum row size configured but not exceeding 32,000 (16,000 in a UTF8 instance). |
| Variable-length (varchar, long varchar, or text) | Fixed-length | The assigned string is truncated or padded with spaces if the receiving column or variable is not the same length as the variable length string.If a long varchar value over is assigned to another character data type, the result is truncated at the maximum row size configured but not exceeding 32,000 (16,000 in a UTF8 instance). |
| Variable-length | Variable-length | The variable length string is truncated if the receiving column or variable is not long enough. |

### String Truncation

If an attempt is made to insert a string value into a table column that is too short to contain the value, the Actian Data Platform terminates the statement and issues an error message.

String truncation can occur as a result of the following statements:

- COPY
- CREATE TABLE...SELECT

- INSERT
- UPDATE

To change error handling behavior for string truncation, use one of these methods:

- Specify the -STRING_TRUNCATION=option flag on the CONNECT statement, specified when a session connects to a database.
- Specify the -STRING_TRUNCATION=option flag on the command line for the Actian Data Platform operating system commands that accept SQL option flags.

- Specify the config.string_truncation configuration parameter in config.dat using the iisetres command.

This flag can also be specified on the command line for the Actian Data Platform operating system commands that accept SQL option flags.

For more information about the -string_truncation flag, see [sql Command Options and Flags](../SQLLanguage/sql_Command_Options_and_Flags.md).

### Numeric Assignments

All numeric types are compatible with one another and with character types. Money is compatible with all of the numeric and string data types.

Numeric assignments follow these rules:

- The Actian Data Platform can truncate leading zeros, or all or part of the fractional part of a number if necessary. If truncation of the non-fractional part of a value (other than leading zeros) is necessary, an overflow error results. These errors are reported only if numeric overflow error handling is set to warn or fail.
- If the receiving column or variable specifies more digits to the right of the decimal point than is present in the assignment value, the assignment value is padded with trailing zeros.

- When a float, float4, decimal, or money value is assigned to an integer column or variable, the fractional part is truncated.
- When a decimal value with a scale greater than two is assigned to a money column or variable, the fractional value is rounded.

- Character data is subject to numeric syntax checks if assigned in a numeric or money context.

### Date and Time Assignments

The ANSI date and time data types are compatible between themselves and string columns.

The values of all date and time types can be assigned to string columns. The result is a display version of each value. String values can also be assigned to date and time columns, as long as the string values correspond to the acceptable input format for the particular date and time type.

!!! note "Note"

    When a date and time value is retrieved from a database, it is always presented to the user in the appropriate display format in a string variable.

### Null Value Assignments

A null can be assigned to a column of any data type if the column was defined as a nullable column. A null can also be assigned to a host language variable if there is an indicator variable associated with the host variable.

To ensure that a null is not assigned to a column, use the IFNULL function.

## Arithmetic Operations

An arithmetic operation combines two or more numeric expressions using the arithmetic operators (see [Arithmetic Operators](../SQLLanguage/Elements_of_SQL_Statements.md)) to form a resulting numeric expression.

Before an arithmetic operation is performed, the participating expressions are converted to identical data types. After the arithmetic operation is performed, the resulting expression also has that storage format.

### Default Type Conversion

When two numeric expressions are combined, the data types of the expressions are converted to be identical; this conversion determines the data type of the result. The expression having the data type of lower precedence is converted to the data type of higher precedence.

The order of precedence among the numeric data types, in highest-to-lowest order, is as follows:

- MONEY
- FLOAT4

- FLOAT
- DECIMAL

- INTEGER8 (BIGINT)
- INTEGER4 (INTEGER)

- INTEGER2 (SMALLINT)
- INTEGER1 (TINYINT)

For example, in an operation that combines an integer and a floating point number, the integer is converted to a floating point number before the operation is performed. If the operands are two integers of different sizes, the smaller is converted to the size of the larger.

For example, for the expression:

```
(job.lowsal + 1000) * 12
```

the first operator (+) combines a float4 expression (job.lowsal) with a smallint constant (1000). The result is float4. The second operator (*) combines the float4 expression with a smallint constant (12), resulting in a float4 expression.

The following table lists the data types that result from combining numeric data types in expressions:

|  | integer1 | integer2 | integer4 | integer8 | decimal* | float8 | float4 | money |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer1 | integer8 | integer8 | integer8 | integer8 | decimal6 | float8 | float4 | money |
| integer2 | integer8 | integer8 | integer8 | integer8 | decimal6 | float8 | float4 | money |
| integer4 | integer8 | integer8 | integer8 | integer8 | decimal12 | float8 | float4 | money |
| integer8 | integer8 | integer8 | integer8 | integer8 | decimal20 | float8 | float4 | money |
| decimal* | decimal6 | decimal6 | decimal12 | decimal20 | decimal6 | float8 | float4 | money |
| float8 | float8 | float8 | float8 | float8 | float8 | float8 | float4 | money |
| float4 | float4 | float4 | float4 | float4 | float4 | float4 | float4 | money |
| money | money | money | money | money | money | money | money | money |
|  | *decimal(n) – The result size depends on the size of the decimal. The result size shown is for adding decimal(1) to the other value, for example: decimal(1) + int2(1). |

To convert one data type to another, use data type conversion functions (see [Conversion Functions](../SQLLanguage/SQL_Functions.md)).

### Arithmetic Operations on Decimal Data Types

Actian Data Platform uses the Standard decimal handling rules (decimal_rule in config.dat is set to Standard rather than Classic).

In expressions that combine decimal values and return decimal results, the precision (total number of digits) and scale (number of digits to the right of the decimal point) of the Standard result can be determined, as shown in the following table:

| Operation | Result Precision | Result Scale |
| --- | --- | --- |
| **Addition and subtraction** | Largest number of fractional digits plus largest number of non-fractional digits + 1 | Largest number of fractional digits |
| **Multiplication** | Total of input precisions | Total of input scales |
| **Division** | Dividend non-fractional digits, plus divisor scale, plus result scale | Dividend scale, plus divisor precision, plus one; but at least 10 |

If the result precision is larger than 38, the result scale is reduced by the amount of the precision excess, and the result precision is set to 38. The result scale is not reduced below 4 if the input scales are 4 or more; if both input scales are less then 4, the result scale is not reduced to less than the larger.

For example, in the following decimal addition operation:

```
1.234 + 567.89
```

the scale and precision of the result is calculated as follows:

Precision = 7, calculated as 3 (largest number of fractional digits) + 3 (largest number of non-fractional digits) + 1 = 7.

Scale = 3. The first operand has the largest number of digits to the right of the decimal point.

Result: 0569.124

If exponentiation is performed on a decimal value, the resulting data type is float.

#### Comparison of Decimal Handling Settings

Decimal arithmetic is handled according to the setting on the decimal_rule parameter in config.dat--either Classic or Standard.

The following examples compare Classic and Standard decimal handling. Given the input precision and scale, the result precision and scale for Classic and Standard settings are shown.

| Input Precision and Scale | Classic Result | Standard Result |
| --- | --- | --- |
| (38,10) + (38,5) | (38,10) | (38,5) |
| (14,3) * (14,3) * (14,3) * (4,1) | (38,10) | (38,3) |
| (38,20) * (38,20) | (38,38) | (38,4) |
| (5,1) / (3,1) | (38,33) | (15,10) |
| (14,4) / (12,2) | (38,26) | (29,17) |

The Classic rules follow the SQL Standard specifications for result scale, even when the precision has to be limited to the maximum of 38. The effect is that in a complex expression, the result scale tends to be large, which reduces the number of available non-fractional digits and makes numeric overflow more likely.

The Standard rules reduce both precision and scale when precision gets too large, which favors non-fractional digits at the expense of fractional digits and makes numeric overflow less likely.

### Date and Time Arithmetic

The following arithmetic is supported for date and time data types.

!!! note "Note"

    “Absolute type” is a non-interval form.

Operators that return absolute date forms:

| absolute type | - | interval type | = | absolute type |
| --- | --- | --- | --- | --- |
| absolute type | + | interval type | = | absolute type |
| interval type | + | absolute type | = | absolute type |

The result will be the same as the absolute term.

Operators used with intervals:

| - interval type | = | interval type |  |  |
| --- | --- | --- | --- | --- |
| + interval type | = | interval type |  |  |
| absolute type | - | absolute type | = | interval type |
| interval type | + | interval type | = | interval type |
| interval type | - | interval type | = | interval type |
| interval type | * | numeric-expression | = | interval type |
| numeric-expression | * | interval type | = | interval type |
| interval type | / | numeric-expression | = | interval type |
| interval type | / | interval type | = | numeric-expression |

The combining rules are:

- ANSI absolute types must match to take their difference.
- You cannot combine YEAR TO MONTH and DAY TO SECOND intervals.

### ANSI Date and Time Comparisons

ANSI date and time values can be compared only to values of the same type. When the time zone setting of a time or timestamp value does not match that of its comparand, time or timestamp values WITH TIME ZONE or WITH LOCAL TIME ZONE are considered to be stored in GMT and can be compared directly. If one comparand is time or timestamp WITH TIME ZONE or WITH LOCAL TIME ZONE and the other comparand is WITHOUT TIME ZONE, the value of the WITHOUT TIME ZONE comparand is assumed to be in local time of the session default time zone. It is converted to GMT based on that assumption and the comparison proceeds.

### Operator Coercion Rules

The implicit coercion rules for operators are as follows:

1. Generally, where a numeric type is required, a string type can be supplied. If the character data turns out not to be numeric in form, a conversion error will occur.
2. Generally, where a string type is required, a numeric type can be supplied. This is the case for all integers, decimal, and all floats.

3. When an operator combines two values of the same data class, string or number, then the following precedence, shown from highest to lowest, is followed:

NCHAR

NVARCHAR

MONEY

CHAR

VARCHAR

FLOAT

DECIMAL

INT

4. The exception to Rule 3 is the “+” operator, which is an arithmetic operator as well as a concatenation operator for strings. The two modes coexist, but if a number is added to a string, then the result type is a number.
5. Mixed type comparisons between character and numeric data are virtually coerced into Numeric String data before being compared.
