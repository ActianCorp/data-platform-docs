---
title: "Booleans and Boolean Operators"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Booleans_and_Boolean_Operators.htm"
canonical_id: "actian-data-platform-booleans-and-boolean-operators"
---

## Booleans and Boolean Operators

Unlike SQL, JSON has three Boolean states: TRUE, FALSE, and JSON UNKNOWN. JSON UNKNOWN is generally a result of an error (for example, invalid data type comparison).

!!! note "Note"

    You cannot simply test for a true or false condition, which is the natural inclination for Boolean. For example, to compare @.age for all rows against the number 18, you cannot simply test for ‘@.age <= 18’ and ‘@.age > 18’; you must account for rows where ‘(@.age > 18)’ is unknown.

TRUE and FALSE Boolean conditions are tested using ==. Unlike SQL, Booleans cannot be tested “standalone.”

    Example: Assume `@.skilled` is a Boolean value.

    `? (@.skilled == TRUE)` is a valid statement.

    `? (@.skilled)` is an invalid statement.

UNKNOWN Boolean conditions are testing using the IS UNKNOWN operator.

    Examples

    : `? (@.skilled IS UNKNOWN)`is a valid statement.

    `? (@.skilled == unknown)` is an invalid statement.

&&, ||, and ! are the AND, OR, and NOT operators and work against Boolean operands.

If the initial tested operand is enough to return a result, the other operand does not need to be evaluated. (For example, if operand 1 is FALSE and the operator is &&, then operand 2 can be ignored.)

&& truth table:

|  | TRUE | FALSE | UNKNOWN |
| --- | --- | --- | --- |
| TRUE | TRUE | FALSE | UNKNOWN |
| FALSE | FALSE | FALSE | FALSE |
| UNKNOWN | UNKNOWN | FALSE | UNKNOWN |

!!! note "Note"

    Operators can be checked in any order, so `FALSE &&``error` may still return an error.

|| truth table:

|  | TRUE | FALSE | UNKNOWN |
| --- | --- | --- | --- |
| TRUE | TRUE | TRUE | TRUE |
| FALSE | TRUE | FALSE | UNKNOWN |
| UNKNOWN | TRUE | UNKNOWN | UNKNOWN |

! truth table:

!TRUE is FALSE

!FALSE is TRUE

!UNKNOWN is UNKNOWN
