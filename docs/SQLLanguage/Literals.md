---
title: "Literals"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Literals.htm"
canonical_id: "actian-data-platform-literals"
---

## Literals

A literal is an explicit representation of a value. There are four types of literals:

- String
- Numeric

- Date and time
- Boolean

## String Literals

String literals are specified by one or more characters enclosed in single quotes. The default data type for string literals is VARCHAR, but a string literal can be assigned to any character data type or to money or date data type without using a data type conversion function.

To compare a string literal with a non-character data type, you must either cast the string literal to the non-character data type or cast the non-character data type to the string literal type. Failure to do so causes unexpected results if the non-character data type contains the ‘NULL (0) value.

### Hexadecimal Representation

To specify a non-printing character in the SQL CLI, use a hex (hexadecimal) constant.

Hex constants are specified by an X followed by a single-quoted string composed of (an even number of) alphanumeric characters. For example, the following represents the ASCII string ABC<carriage return>:

```
X'4142430D'
```

```
A = X'41', B = X'42', C = X'43', and carriage return = X'OD'.
```

An alternative is to use a prefix of 0x. That is, 0xstring composed of (an even number of) alphanumeric characters:

```
0x4142430D
```

```
A = 0x41, B = 0x42', C = 0x43, and carriage return = 0xOD.
```

!!! note "Note"

    Tables of structure VECTORWISE and VECTORWISE_ROW do not support the BYTE data type. A string literal can be used to hold BYTE values but be careful when using functions that may result in embedded NULL (\000) being placed in a string because all values after the first NULL will be permanently lost. The values 'A\000BCD' will be stored as 'A'.

### Quotes within Strings

To include a single quote inside a string literal, it must be doubled. For example:

```
'The following letter is quoted: ''A''.'
```

which is evaluated as:

```
The following letter is quoted: 'A'.
```

### Unicode Literals

A Unicode string literal in SQL is identified by prefixing the string either with U& or with the letter N. The characters present in the string will be converted to Unicode code points and the data type of the resulting literal will be NVARCHAR.

Unicode code points can also be embedded in the literal using their numeric form. Being able to encode code points numerically allows the literal to contain characters that may have no representation in the character set of the SQL CLI. Characters from the Basic Multilingual Plane can be embedded using the escape character \ followed by the four hexadecimal digits of its value. The code points from the remaining Supplementary Planes all use six hexadecimal digits and are escaped with +. For example:

```
U&'Hello\202Fworld+029E71'
```

In this string, Hello is converted to the equivalent Unicode code points, the hex digits 202F represent code point U+202F (the narrow non-breaking space), world is converted to the equivalent Unicode code points, and the hex digits 029E71 represent code point U+29E71 (the Chinese ideograph chù from Plane 2). The resulting literal is the concatenation of the converted Unicode components.

## Numeric Literals

Numeric literals specify numeric values. There are three types of numeric literals:

- Integer
- Decimal

- Floating point

A numeric literal can be assigned to any of the numeric data types or the money data type without using an explicit conversion function. The literal is automatically converted to the appropriate data type, if necessary.

By default, the period (.) is displayed to indicate the decimal point. This default can be changed by setting II_DECIMAL.

!!! note "Note"

    If II_DECIMAL is set to comma, you must follow any comma required in SQL syntax (such as a list of table columns or SQL functions with several parameters) by a space. For example:

```
SELECT col1, IFNULL(col2, 0), LEFT(col4, 22) FROM version;
```

### Integer Literals

Integer literals are specified by a sequence of digits and an optional sign, in the following format:

```
[+|-] digit {digit} [e digit]
```

Integer literals are represented internally as a SMALLINT, INTEGER, or BIGINT depending on the value of the literal. A literal in the range -32,768 to +32,767 is represented as a SMALLINT. A literal in the range ‑2,147,483,648 to +2,147,483,647 but outside the range of a SMALLINT is represented as an INTEGER. A literal in the range ‑9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 is represented as a BIGINT. Values that exceed the range of integers are represented as decimals.

You can specify integers using a simplified scientific notation, similar to the way floating point values are specified. To specify an exponent, follow the integer value with the letter, e, and the value of the exponent. This notation is useful for specifying large values. For example, to specify 100,000 use the exponential notation as follows:

```
1e5
```

### Decimal Literals

Decimal literals are specified as signed or unsigned numbers of 1 to 38 digits that include a decimal point. The precision of a decimal number is the total number of digits, including leading and trailing zeros. The scale of a decimal literal is the total number of digits to the right of the decimal point, including trailing zeros.

Decimal literals that exceed 38 digits are treated as floating point values.

Examples of decimal literals are:

```
3.
```

```
-10.
```

```
1234567890.12345
```

```
001.100
```

### Floating Point Literals

A floating point literal must be specified using scientific notation. The format is:

```
[+|-] {digit} [.{digit}] e|E [+|-] {digit}
```

For example:

```
2.3e-02
```

At least one digit must be specified either before or after the decimal point.

## Date and Time Literals

Date and time literals specify ANSI compliant date/time values. There are four types of date and time literals:

- Date
- Time

- Timestamp
- Interval

Date and time literals can be assigned to the corresponding date and time data type without using an explicit conversion function. The value is coded as a quoted string, but is automatically converted to the appropriate internal value.

### Date Literals

Literals of the ANSI date type have the following format:

```
DATE 'date_value'
```

**date_value**

:   Defines a date in the format yyyy-mm-dd.

!!! note "Note"

    The II_DATE_FORMAT setting has no impact on the processing of date literals.

Examples:

```
DATE '2012-05-29'
```

```
DATE '1998-10-08'
```

```
DATE '2000-11-29'
```

### Time Literals

Literals of the ANSI time type have the following format:

```
TIME 'time_value'
```

**time_value**

:   Defines a time value in the format hh:mm:ss, optionally followed by .fff (fractions of seconds) and also optionally followed by ±hh:mm, the time zone offset.

Examples:

```
TIME '11:11:00'
```

```
TIME '18:05:23.425364'
```

```
TIME '5:23:00-5:00'
```

```
TIME '18:05:23.4253+08:00'
```

| Time Format | Example | Description |
| --- | --- | --- |
| TIME WITHOUT TIME ZONE | `TIME '11:11:00'` | A time value with no decimal precision |
| TIME WITHOUT TIME ZONE(6) | `TIME '18:05:23.425364'` | A time value with six places of decimal precision |
| TIME WITH TIME ZONE | `TIME '05:23:00-5:00'` | A time with time zone value with no decimal precision |
| TIME WITH TIME ZONE(4) | `TIME '18:05:23.4253+08:00'` | A time with time zone value with four places of decimal precision |

### Timestamp Literals

Literals of the ANSI timestamp type have the following format:

```
TIMESTAMP 'timestamp_value'
```

**timestamp_value**

:   Consists of a date value and a time value separated by a single space. The time value can contain optional fractions of seconds, time zone offset, or both.

Examples:

```
TIMESTAMP '2012-05-29 10:30:00.000-04:00'
```

```
TIMESTAMP '1918-11-11 11:11:00'
```

### Interval Literals

Literals of the ANSI interval type have the following format:

```
INTERVAL '[sign]interval_value' interval_qualifier
```

**sign**

:   Indicates a positive (+) or negative (-). The default is +.

**interval_value**

:   Consists of:

:   A year to month interval value in the format: year-mm (for example: '25-7') or

:   A day to second interval value in the format: dddd... hh:mm:ss[.fffffffff] (for example: '15 5:10:27.4325')

**interval_qualifier**

:   Qualifies the interval as a year to month or a day to second. The interval_qualifier has the following format:

```
leading field [TO trailing field]
```

    Valid values for leading field and trailing field in order of precedence are:

YEAR

MONTH

DAY

HOUR

MINUTE

SECOND [(p)].

    The leading field cannot have lower precedence than the trailing field.

    The precision value on the SECOND field indicates the number of digits allowed in the fractional part of that field.

Examples:

```
INTERVAL '5-7' year to month
```

```
INTERVAL '-0-11' year to month
```

```
INTERVAL '+24 12:10:5.1234' day to second
```

```
INTERVAL '124' year
```

```
INTERVAL '12' month
```

```
INTERVAL '18' day
```

```
INTERVAL '10' hour
```

```
INTERVAL '34' minute
```

```
INTERVAL '20.23456789' second (9)
```

```
INTERVAL '8-11' year to month
```

```
INTERVAL '12 10' day to hour
```

```
INTERVAL '12 10:20' day to minute
```

```
INTERVAL '121 10:15:23.123456' day to second(6)
```

## Boolean Literals

The SQL literals FALSE and TRUE can be used in expressions, including on the right side of an assignment. Boolean values or expressions can be tested against those literals using the IS operator. For example:

```
WHERE boolean_value IS TRUE
```

For input, the literals FALSE and TRUE are accepted, without case sensitivity.

More information:

[IS TRUE, IS FALSE, IS UNKNOWN Predicates](../SQLLanguage/Predicates_in_SQL.md)
