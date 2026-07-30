---
title: "Predicates in SQL"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Predicates_in_SQL.htm"
canonical_id: "actian-data-platform-predicates-in-sql"
---

## Predicates in SQL

Predicates are keywords that specify a relationship between two expressions.

## Comparison Predicate

The syntax for comparison predicates is as follows:

```
expression_1 comparison_operator expression_2
```

In a comparison predicate, expression2 can be a subquery. If expression2 is a subquery and does not return any rows, the comparison predicate evaluates to false. For information about subqueries, see [Subqueries in the WHERE Clause](../SQLLanguage/Subqueries.md). For more information about comparison operators, see Comparison Operators.

## Pattern-matching Predicates

Pattern-matching predicates (the LIKE family of predicates) are used to search for a specified pattern in text, an expression, or column. These predicates include:

- LIKE
- BEGINNING, ENDING, CONTAINING

The specific predicate to use depends on how complex the pattern needs to be. All predicates in the LIKE family have the same SQL syntax, operate on the same data types, and can control the case-sensitivity of the matching.

The LIKE family of predicates performs pattern matching for the character data types (char, varchar) and Unicode data types (nchar, nvarchar).

!!! note "Note"

    Actian Data Platform supports constant LIKE patterns only.

The LIKE family of predicates has the following syntax:

```
expression [NOT] [LIKE|BEGINNING|CONTAINING|ENDING] pattern            [WITH CASE | WITHOUT CASE]            [ESCAPE escape_character]
```

where

**expression**

:   Is a column name or a string expression

**pattern**

:   Specifies the pattern to be matched. The pattern is typically a string literal but can be an arbitrary string expression.

:   The patterns supported depends upon the specific predicate used.

**WITH CASE | WITHOUT CASE**

:   Indicates whether to match the case of the pattern. This option can be used before, after, or instead of the ESCAPE clause.

:   Default: If not specified, the collation type of the expression is used, typically WITH CASE.

**ESCAPE escape_character**

:   Specifies the character to use to escape another character or to enable a character's special meaning in a pattern.

### LIKE Predicate

Use LIKE in a WHERE clause to search for a specified pattern in a column.

LIKE performs pattern matching for the character and Unicode data types.

The LIKE predicate has the following syntax:

```
expression [NOT] LIKE pattern [WITH CASE | WITHOUT CASE]            [WITH DIACRITICAL | WITHOUT DIACRITICAL]           [ESCAPE escape_character]
```

where

**expression**

:   Is a column name or an expression containing string functions

**pattern**

:   Specifies the pattern to be matched. The pattern is typically a string literal but can be an arbitrary string expression.

:   The pattern-matching (wild card) characters are as follows:

% (percent sign)

:   Denotes 0 or more characters

_ (underscore)

:   Denotes a single character

\|

:   Denotes the alternation operator

**WITH CASE | WITHOUT CASE**

:   Indicates whether to match the case of the pattern. This option can be used before, after, or instead of the ESCAPE clause.

:   Default: WITH CASE

**WITH DIACRITICAL | WITHOUT DIACRITICAL**

:   Indicates whether to ignore diacritical marks. For example, Latin little “e” will match Latin little “e” with acute if the WITHOUT DIACRITICAL is specified.

:   Default: WITH DIACRITICAL

**ESCAPE escape_character**

:   Specifies an escape character, which suppresses any special meaning for the character following it, allowing the character to be entered literally. The following characters can be escaped:

    - The pattern-matching characters % and _.

    - The escape character itself. To enter the escape character literally, type it twice.

    - The | character, which can be used to specify alternate patterns to match.

LIKE does not ignore the trailing blanks present with a char or nchar data type. If you are matching a char value (that is padded with blanks when it is inserted) or if the value has trailing blanks that were entered by the user, include these trailing blanks in your pattern. For example, if searching a char(10) column for rows that contain the name harold, specify the trailing blanks in the pattern to be matched:

```
name like 'harold    '
```

Four blanks are added to the pattern after the name to include the trailing blanks.

Because blanks are not significant when performing comparisons of c data types, the LIKE predicate returns a correct result whether or not trailing blanks are included in the pattern.

**LIKE Examples**

The following examples illustrate some uses of the pattern-matching capabilities of the LIKE predicate.

To match any string starting with a:

```
name LIKE 'a%'
```

To match any two characters followed by 25%:

```
name LIKE '__25\%' ESCAPE '\'
```

To match a string starting with a backslash. Because there is no ESCAPE clause, the backslash is taken literally:

```
name LIKE '\%'
```

To match a string starting with a backslash and ending with a percent:

```
name LIKE '\\%\%' ESCAPE '\'
```

To detect names that start with S and end with h, disregarding any leading or trailing spaces:

```
SQUEEZE(name) LIKE 'S%h'
```

To detect a single quote, repeat the quote:

```
name LIKE ''''
```

To search for multiple patterns, use escaped | as a delimiter. For example, the following will match if string_1 contains ABC, 123, or xyz:

```
string_1 LIKE '%ABC%@|%123%@|%xyz%' ESCAPE '@'
```

### BEGINNING, CONTAINING, and ENDING Predicates

Use BEGINNING, CONTAINING, or ENDING in a WHERE clause to search for a specified pattern in a column.

These predicates have the following syntax:

```
expression [NOT] BEGINNING | CONTAINING | ENDING pattern            [WITH CASE | WITHOUT CASE] [ESCAPE escape_character]
```

where

**expression**

:   Is a column name or an expression containing string functions.

**BEGINNING**

:   Matches if the pattern string is found at the beginning of the text.

**CONTAINING**

:   Matches if the pattern string is found within the text.

**ENDING**

:   Matches if the pattern string is found at the end of the text.

**pattern**

:   Specifies the pattern to be matched. The pattern must be a string literal.

## BETWEEN Predicate

The following table explains the operators BETWEEN and NOT BETWEEN:

| Operator | Meaning |
| --- | --- |
| y BETWEEN [ASYMMETRIC] xAND z | x < = y and y < = z |
| y NOT BETWEEN [ASYMMETRIC] x AND z | not (y between x and z) |
| y BETWEEN SYMMETRIC xAND z | (x < = y and y < = z) or (z < = y and y < = x) |
| y NOT BETWEEN SYMMETRIC x AND z | not (y between symmetric x and z) |

x, y, and z are expressions, and can include subqueries.

## IN Predicate

The following table explains the operators IN and NOT IN:

| Operator | Meaning |
| --- | --- |
| y IN (x, ..., z) | The IN predicate returns true if y is equal to one of the values in the list (x, ..., z).(x, ..., z) represents a list of expressions, each of which must evaluate to a single value. If there is only one expression in the list, the parentheses are optional. None of the expressions (y, x, or z) can be subqueries. |
| y NOT IN (x, ..., z) | Returns true if y is not equal to any of the values in the list (x, ..., z).(x, ..., z) is a list of expressions, each of which must evaluate to a single value. If there is only one expression in the list, the parentheses are optional. None of the expressions (y, x, or z) can be subqueries. |
| y IN (subquery) | Returns true if y is equal to one of the values returned by thesubquery. The subquery must be parenthesized and can reference only one column in its SELECT clause. |
| y NOT IN (subquery) | Returns true if y is not equal to any of the values returned by thesubquery. The subquery must be specified in parentheses and can reference only one column in its SELECT clause. |

## Any-or-All Predicate

The any-or-all predicate takes the following form:

any-or-all-operator (subquery)

The subquery must have exactly one element in the target list of its outermost subselect (so that it evaluates to a set of single values rather than a set of rows). The any-or-all operator must be one of the following:

| =ANY  <>ANY  <ANY  <=ANY  >ANY  >=ANY | =ALL  <>ALL  <ALL  <=ALL  >ALL  >=ALL |
| --- | --- |

The != (instead of <>) can also be used to specify not equal. Include a space between the comparison operator and the keyword ANY or ALL.

A predicate that includes the ANY operator is true if the specified comparison is true for at least one value y in the set of values returned by the subquery. If the subquery returns no rows, the ANY comparison is false.

A predicate that includes the ALL operator is true if the specified comparison is true for all values y in the set of values returned by the subquery. If the subquery returns no rows, the ALL comparison is true.

The operator =ANY is equivalent to the operator IN. For example:

```
SELECT enameFROM employeeWHERE dept = ANY       (SELECT dno       FROM dept       WHERE floor = 3);
```

can be rewritten as:

```
SELECT enameFROM employeeWHERE dept IN       (SELECT dno       FROM dept       WHERE floor = 3);
```

The operator SOME is a synonym for operator ANY. For example:

```
SELECT nameFROM employeeWHERE dept = SOME       (SELECT dno       FROM dept       WHERE floor = 3);
```

## EXISTS Predicate

The EXISTS predicate takes the following form:

```
[NOT] EXISTS (subquery)
```

It evaluates to true if the set returned by the subquery is not empty. For example:

```
SELECT enameFROM employeeWHERE EXISTS        (SELECT *       FROM dept       	WHERE dno = employee.dept       AND floor = 3);
```

It is typical, but not required, for the subquery argument to EXISTS to be of the form SELECT *.

## IS NULL Predicate

Use IS NULL to determine whether an expression is null, because you cannot test for null by using the = comparison operator. When applied to row value expressions, all elements must test the same.

The IS NULL predicate takes the following form:

```
IS [NOT] NULL
```

For example:

```
x IS NULL
```

is true if x is a null.

IS UNKNOWN is a synonym for IS NULL when the expression is of the BOOLEAN type.

## IS INTEGER Predicate

Use IS INTEGER to determine if a particular result can be assigned to a column of the given data type. It is especially useful for cleaning data or validating data input. When applied to row value expressions, all elements must test the same.

The IS INTEGER predicate takes the following form:

```
IS [NOT] INTEGER
```

For example:

```
x IS INTEGER
```

is true if x is integer in form. If x is a string, then this will be true if the value is a number where any fractional digits are zero and the signed result can be stored in an int8. Any leading or trailing white space is ignored. If x is a DECIMAL or a FLOAT value, then this predicate is true if the value can be stored in an int8 column and any fractional digits are zero.

If all values in a column pass this predicate, then the whole column can be coerced into a int8 column.

The following predicates are all true:

```
' +12345 ' IS INTEGER
```

```
'1.000000' IS INTEGER
```

```
1.0e10 IS INTEGER
```

```
DECIMAL('1234567890123456789012345', 25,0) IS NOT INTEGER
```

```
'number' IS NOT INTEGER
```

```
'123 456' IS NOT INTEGER
```

## IS DECIMAL Predicate

Use IS DECIMAL to determine if a particular result can be assigned to a column of the given data type. It is especially useful for cleaning data or validating data input. When applied to row value expressions, all elements must test the same.

The IS DECIMAL predicate takes the following form:

```
IS [NOT] DECIMAL
```

For example:

```
x IS DECIMAL
```

is true if x is decimal in form. If x is a string, then this is true if the value is a number that can be stored as a decimal data type with no loss of accuracy. Any leading or trailing white space is ignored. If x is a FLOAT value then this predicate is true only if the number can be stored in a decimal column without loss of precision of overflow.

The following predicates are all true:

```
' +12345 ' IS DECIMAL
```

```
'1.000000' IS DECIMAL
```

```
1.0e10 IS DECIMAL
```

```
DECIMAL('1234567890123456789012345', 25,0) IS DECIMAL
```

```
'number' IS NOT DECIMAL
```

```
'123 456' IS NOT DECIMAL
```

```
'1.0e40' IS NOT DECIMAL
```

If all values in a column pass this predicate, then the whole column can be coerced into a decimal column.

## IS FLOAT Predicate

Use IS FLOAT to determine if a particular result can be assigned to a column of the given data type. It is especially useful for cleaning data or validating data input. When applied to row value expressions, all elements must test the same.

The IS FLOAT predicate takes the following form:

```
IS [NOT] FLOAT
```

For example:

```
x IS FLOAT
```

is true if x is float in form. If x is a string, then this is true if the value is a number that can be stored as a float data type. All integers and decimals can be represented as float but there may be some loss of accuracy. Any leading or trailing white space is ignored.

If all values in a column pass this predicate then the whole column can be coerced into a float column.

The following predicates are all true:

```
' +12345 ' IS FLOAT
```

```
'1.000000' IS FLOAT
```

```
1.0e10 IS FLOAT
```

```
DECIMAL('1234567890123456789012345', 25,0) IS FLOAT
```

```
'number' IS NOT FLOAT
```

```
'123 456' IS NOT FLOAT
```

```
'1.0e4000' IS NOT FLOAT
```

## IS TRUE, IS FALSE, IS UNKNOWN Predicates

The IS Boolean operator behaves according to the following truth table:

| IS | TRUE | FALSE | UNKNOWN |
| --- | --- | --- | --- |
| True | True | False | False |
| False | False | True | False |
| Unknown | False | False | True |

That is:

- IS TRUE is true for a BOOLEAN TRUE.
- IS FALSE is true for a BOOLEAN FALSE.

- IS UNKNOWN is true for an unknown (NULL) value.
- Every other comparison is false.

When applied to row value expressions, all elements must test the same.
