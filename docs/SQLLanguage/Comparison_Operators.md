---
title: "Comparison Operators"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Comparison_Operators.htm"
canonical_id: "actian-data-platform-comparison-operators"
---

## Comparison Operators

Note the following when using comparison operators:

- Two JSON items are comparable if one of them is a JSON null and the other is a JSON scalar, or if both are an identical scalar type (string, numeric, or Boolean). Arrays and JSON objects cannot be directly compared, although lax mode unwinds arrays and turns them into sequences.
- Equality operators have the same precedence as inequality operators.

- Comparisons require identical data types (no automatic casting).
- JSON NULLS are not greater than or less than anything.

- JSON NULLS are not equal to SQL nulls when compared directly using PASSING clause variables. The JSON NULL is considered a unique data type and is therefore not equal to null values of other data types (a null integer, for example).
- Comparisons allow sequences as operands. Every item in each sequence is compared against every item in the other sequence. When comparing sequences, the following rules apply:

    - –If a comparison results in a JSON UNKNOWN (for example, incomparable operands), then the comparison immediately returns JSON UNKNOWN as the final result.

    - –In lax mode, if a pair of operands returns a TRUE comparison, then the result is TRUE. This occurs even if there is an invalid “UNKNOWN” comparison that has not been detected yet. If all pairs of operands are compared and return FALSE, then the result is FALSE.

    - –In strict mode, every combination of operands is compared to check for JSON UNKNOWNs. If any comparison returns JSON UNKNOWN, then the result is JSON UNKNOWN. If all the comparisons return FALSE, then the result is FALSE. If all the comparisons return TRUE or FALSE and one or more return TRUE, then the result is TRUE.

- Operators can be checked in any order, so `FALSE &&``error` may still return an error.
