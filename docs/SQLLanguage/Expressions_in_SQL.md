---
title: "Expressions in SQL"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Expressions_in_SQL.htm"
canonical_id: "actian-data-platform-expressions-in-sql"
---

## Expressions in SQL

Expressions are composed of various operators and operands that evaluate to a single value or a set of values. Some expressions do not use operators; for example, a column name is an expression. Expressions are used in many contexts, such as specifying values to be retrieved (in a SELECT clause) or compared (in a WHERE clause).

In the following example, empname and empage are expressions representing the column values to be retrieved, salary is an expression representing a column value to be compared, and 75000 is an integer literal expression.

```
SELECT empname, empage FROM employee
```

```
        WHERE salary > 75000
```

Expressions that contain aggregate functions can appear only in SELECT lists and HAVING clauses unless they are within a nested SELECT clause. Aggregate functions cannot be nested.

An expression can be enclosed in parentheses without affecting its value.

A row value expression is a list of expressions, separated by commas and enclosed in parentheses. Row value expressions can be used with most comparison predicates and allow for row result comparisons. For example, this WHERE clause:

```
WHERE empname ='Jones' AND empage = 36 AND salary = 45000
```

can be written using a row value comparison as follows:

```
WHERE (empname, empage, salary)=('Jones', 36, 45000)
```

To test if there is at least one row in employees that has a 36 year old Jones can be achieved with either of the following examples, first written with an EXISTS predicate and then with a row value comparison:

```
WHERE EXISTS(SELECT 1 FROM employee WHERE empname='Jones' AND empage=36)
```

```
WHERE ('Jones', 36) IN (SELECT empname, empage FROM employee)
```

## CASE Expressions

Case expressions provide a decoding capability that allows one expression to be transformed into another. Case expressions can appear anywhere that other forms of expressions can be used.

There are two forms of case expressions:

- Simple
- Searched

Syntax for a simple case expression is as follows:

```
CASE expr WHEN expr1 THEN expr2 WHEN expr3 THEN expr4... [ELSE exprn] END
```

The initial case expression is compared in turn to the expressions in each WHEN clause. The result of the case is the expression from the THEN clause corresponding to the first WHEN clause whose expression is equal to the case expression. If none of the WHEN expressions match the case expression, the result is the value of the expression from the ELSE clause. If there is no ELSE clause, the result is the null value.

Syntax for the searched case expression is as follows:

```
CASE WHEN search_conditon1 THEN expr1 WHEN search_expression2 THEN expr2...[ELSE exprn] END
```

The search conditions of each WHEN clause are evaluated in turn. The result of the case is the expression from the THEN clause corresponding to the first WHEN clause whose search condition evaluates to true. If none of the WHEN clause search conditions evaluate as true, the result is the value of the expression from the ELSE clause. If there is no ELSE clause, the result is the null value.

### DECODE Function

DECODE performs the same function as the simple case expression.

**DECODE**

```
DECODE(source_value, match_value1, decode_value1, match_value2, decode_value2,..., match_valuen, decode_valuen [, else_value])
```

:   Operand type and Result type: All data types, but the types of source_value,match_value1, match_value2, … must be union compatible, and the types of decode_value1, decode_value2, …, else_value must also be union compatible.

:   Compares source_value successively to match_value1, match_value2, …, match_valuen. The result is the decode_valuei of the first matching match_valuei. If none of the match_valuei have the same value as source_value, the result of the function is else_value.

:   Examples:

1. Decode the value state_code. If state_code is 'ak', then return 'Alaska'; if state_code is 'al', then return 'Alabama'; and so on; otherwise return “unknown”.

```
DECODE(state_code, 'ak', 'Alaska',
```

```
                   'al', 'Alabama',
```

```
                            . . . ,
```

```
                   'wy', 'Wyoming',
```

```
                   'unknown') AS state_name;
```

2. Decode the value sex:

```
SELECT name, DECODE(sex, 'm', 'male', 'f', 'female', 'unknown') FROM person;
```

### IF, NULLIF, and COALESCE Functions

IF, NULLIF, and COALESCE are derivative functions of the case expression and can be defined in terms of the case expression.

**IF**

:   Returns the second parameter if the first evaluates as true; otherwise it returns any third, if present. The first expression must be a predicate.

:   It can be represented as follows:

```
IF(expr1, expr2)
```

:   is the same as:

```
CASE WHEN expr1 THEN expr2 ELSE NULL END
```

:   and

```
IF(expr1, expr2, expr3)
```

:   is the same as:

```
CASE WHEN expr1 THEN expr2 ELSE expr3 END
```

:   Example: `IF (a = 1, b IS FALSE)`

**NULLIF**

:   Returns the null value if its two parameters are equal; otherwise it returns the first parameter value. It can be represented as follows:

```
NULLIF(expr1, expr2)
```

:   is the same as:

```
CASE WHEN expr1 = expr2 THEN NULL ELSE expr1 END
```

**COALESCE**

:   Returns the first non-null value of an arbitrary list of parameters. It can be represented as follows:

```
COALESCE(expr1, expr2)
```

:   is the same as:

```
CASE WHEN expr1 IS NOT NULL THEN expr1 ELSE expr2 END
```

:   and

```
COALESCE(expr1, expr2, ..., exprn)
```

:   is the same as:

```
CASE WHEN expr1 IS NOT NULL THEN expr1
```

```
                     ELSE COALESCE(expr2, ..., exprn)
```

### GREATEST, GREATER, LEAST, LESSER Functions

**GREATEST**

```
GREATEST(v1,v2...vN)
```

:   Operand type: Any

:   Result type: Any

:   Returns greatest of values in v1 through vN. Return type is based on that of the first parameter with a size or precision suitable to represent each of the parameters. If all of the values v1 through vN are NULL then returns NULL.

**GREATER**

```
GREATER(v1,v2…vN)
```

:   Operand type: Any

:   Result type: Any

:   Returns greatest of values in v1 through vN. Return type is based on that of the first parameter with a size or precision suitable to represent each of the parameters. If any of the values v1 through vN are NULL then returns NULL.

**LEAST**

```
LEAST(v1,v2...vN)
```

:   Operand type: Any

:   Result type: Any

:   Returns least of values v1 through vN. Return type is based on that of the first parameter with a size or precision suitable to represent each of the parameters. If all of the values v1 through vN are NULL then returns NULL.

**LESSER**

```
LESSER(v1,v2...vN)
```

:   Operand type: Any

:   Result type: Any

:   Returns least of values v1 through vN. Return type is based on that of the first parameter with a size or precision suitable to represent each of the parameters. If any of the values v1 through vN are NULL, then it returns NULL.

## CAST Expressions

An alternative to using CASE and DECODE for conversions is the CAST expression. Cast expressions coerce the source expression into the indicated data type. They can appear anywhere that other forms of expression can.

They are specified as follows:

```
CAST (expr AS datatype)
```

where expr is the source value expression and datatypeis any supported data type.

Example:

```
SELECT CAST(CURRENT_TIME AS TIME(9) WITH TIME ZONE);
```
