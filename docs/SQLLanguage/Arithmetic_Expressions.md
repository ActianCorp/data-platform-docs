---
title: "Arithmetic Expressions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Arithmetic_Expressions.htm"
canonical_id: "actian-data-platform-arithmetic-expressions"
---

## Arithmetic Expressions

**Unary + and Unary -**

    - Value must be numeric or an error is returned (in both lax and strict modes)

    - The operator applies to each element of a sequence

**Binary +, -, *, /, %**

:   Requires singleton numeric operands. Any other operand, including sequences, generate errors (in both lax and strict modes).
