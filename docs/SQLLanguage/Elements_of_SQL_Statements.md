---
title: "Elements of SQL Statements"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Elements_of_SQL_Statements.htm"
canonical_id: "actian-data-platform-elements-of-sql-statements"
---

# Elements of SQL Statements

## SQL Operators

An operatoris a symbol that represents an action performed on one or more expressions.

There are three types of SQL operators:

- Arithmetic
- Comparison

- Logical

## Arithmetic Operators

Arithmetic operators are used to combine numeric expressions arithmetically to form other numeric expressions.

The arithmetic operators (in order of precedence) are as follows:

| Arithmetic Operator | Description |
| --- | --- |
| + and - | Positive, negative (unary) |
| ** | Exponentiation (binary) |
| * and / | Multiplication, division (binary) |
| + and - | Addition, subtraction (binary) |

Unary operators group from right to left, while binary operators group from left to right. Use the unary negative (-) to reverse the algebraic sign of a value.

To force a desired order of evaluation, use parentheses. For example:

```
(job.lowsal + 1000) * 12
```

is an expression in which the parentheses force the addition operator (+) to take precedence over the multiplication operator (*).

## Comparison Operators

Comparison operators compare two expressions. SQL includes the following comparison operators:

| Comparison Operator | Description |
| --- | --- |
| = | Equal to |
| <> | Not equal to |
| > | Greater than |
| >= | Greater than or equal to |
| < | Less than |
| <= | Less than or equal to |
| IS NOT DISTINCT FROM | Equal to, treating NULLs as equal |
| IS DISTINCT FROM | No equal to, treating NULLs as equal |

The <> operator can also be specified as != or ^=.

All comparison operators are of equal precedence.

The equal sign (=) also serves as the assignment operator in assignment operations.

More information:

[Comparison Predicate](../SQLLanguage/Predicates_in_SQL.md)

## Logical Operators

SQL has three logical operators, shown in order of precedence:

- NOT
- AND

- OR

Use parentheses to change the order of evaluation. For example, the following expression:

```
exprA OR exprB AND exprC
```

is evaluated as:

```
exprA OR (exprB AND exprC)
```

When parentheses are used as follows:

```
(exprA OR exprB) AND exprC
```

Actian Data Platform evaluates (exprA OR exprB) first, then uses the AND operator****for****the result with exprC.

Parentheses can also be used to change the default evaluation order of a series of expressions combined with the same logical operator. For example, the following expression:

```
exprA AND exprB AND exprC
```

is evaluated as:

```
(exprA AND exprB) AND exprC
```

To change this default left-to-right grouping, use parentheses as follows:

```
exprA AND (exprB AND exprC)
```

The parentheses direct the Actian Data Platform to use the AND operator for****exprB and exprC, then use the AND operator for that result with exprA.
