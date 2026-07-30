---
title: "JSON Predicates"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Predicates.htm"
canonical_id: "actian-data-platform-json-predicates"
---

## JSON Predicates

JSON predicates work against a sequence as follows:

- In lax mode, arrays are unwrapped.
- The predicate is evaluated for all values of the input sequence.

- The return sequence is the set of values for which the predicate is true.
- If the input sequence contains three items, but only two pass the filter qualifications, then the output sequence will contain those two values.

A predicate can return true, false, or a JSON unknown (a predicate error).

An example of a predicate returning unknown: `(@.hours > 9)` if @.hours is a string scalar.

The following JSON predicates are available:

- EXISTS
- Comparison operators

- SIMILAR TO
- STARTS WITH

- IS UNKNOWN

### EXISTS

The EXISTS predicate tests for the existence of a key. Specifically, it tests whether a member accessor returns at least one JSON value. It can be used to probe for a member before accessing it. EXISTS is especially useful for preventing errors in STRICT mode.

Example:

```
STRICT $ ? (EXISTS (@.name)).name
```

This JSON path returns an empty sequence if the base object does not contain the key “name”.

### Comparison Operators

The following comparison operators are supported:

| Comparison Operator | Description |
| --- | --- |
| == | Equal to |
| != or <> | Not equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

### SIMILAR TO

The SIMILAR TO predicate tests if a string matches a pattern. The syntax is identical to SQL’s SIMILAR TO except it supports only _ and %. In the JSON standard, the standard escape character is the backslash (\); therefore, unlike SQL’s SIMILAR TO, the escape “\\” clause is assumed and cannot be specified or changed.

Example:

```
SELECT c FROM t01 WHERE JSON_EXISTS (c, 'LAX $ ? (@.col.Name SIMILAR TO "d%")
```

### STARTS WITH

The STARTS WITH predicate tests for an initial substring.

`A STARTS WITH B` returns true if string A starts with string B (that is, if string B is a prefix of string A).

No wildcards are allowed in either operand. To use wildcards, the SIMILAR TO predicate must be used.

If the second operand of STARTS WITH is a sequence, then TRUE is returned if the first operand starts with any value within the second operand’s sequence.

### IS UNKNOWN

The IS UNKNOWN predicate tests for JSON unknown results. It lets you find invalid rows by testing a result to see if it returned a JSON unknown (which is typically an error).

Example:

```
SELECT id
```

```
FROM employees
```

```
WHERE JSON_EXISTS (datacol,
```

```
'LAX $ ? ( (@.age > 18) IS UNKNOWN')
```

This query returns all rows where (@.age > 18) returns an JSON unknown rather than true or false. In this case, most likely @.age is a non-numeric value.
