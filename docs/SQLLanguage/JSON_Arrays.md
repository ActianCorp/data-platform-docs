---
title: "JSON Arrays"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Arrays.htm"
canonical_id: "actian-data-platform-json-arrays"
---

## JSON Arrays

A JSON array is a comma-separated list of JSON values surrounded by square brackets.

The values in an array can have different data types.

Array values are referenced by specifying an array name followed by a list of array indexes in square brackets.

An array index is used to reference an array value/element. Rules for array indexes are as follows:

- Array indexes can be single numbers. Floats are rounded down.
- The first element of an array is at index 0.

- "last" represents the last element of the array; "last-1", "last-2" are also permitted.
- The keyword “to” is used to represent a range. If `X to Y` is used where X is greater than Y, it is an error in strict mode and returns no elements in lax mode. (For more information on modes, see [Lax and Strict Modes](../SQLLanguage/Lax_and_Strict_Modes.md).)

- An asterisk (*) returns all elements of the array.
- Out of range indexes are ignored in lax mode and are errors in strict mode.

- In lax mode, scalars can be treated as one-element arrays.

Examples:

Let A1 be the array `[0, 1.0, 2, "three", {"number":4}, [5,6]]`

- A1[0] = 0
- A1[last] = [5,6]

- A1[1 to last-2] = 1.0, 2, “three”
- A1 [*] = 0, 1.0, 2, “three”, {“Number”:4}, [5,6]

The following are errors for strict mode and return the shown result for lax mode:

- A1[2.1, 10, 0 to 1, 2] = 2, 0, 1.0, 2 (in that order)
- A1 [*].Number = 4

- A1 [*][1] = 6
- A1 [*][0] = 0, 1.0, 2, “three”, {“Number”:4}, 5

- A1 [-1 to 1] = 0, 1.0
