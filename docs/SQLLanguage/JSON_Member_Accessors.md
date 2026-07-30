---
title: "JSON Member Accessors"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Member_Accessors.htm"
canonical_id: "actian-data-platform-json-member-accessors"
---

## JSON Member Accessors

A member accessor specifies the JSON object keys whose values are to be returned.

A $ represents the entire object and is optionally followed by a list of key names separated with a period. Key names can be delimited with double quotes. The double quotes are required if the key name has a special character.

A list of key names uses a parent-child relationship.

$.key1.key2.key3 means the base object ($) contains a key named “key1”.

The value of “key1” should be an object that contains the key “key2”.

The value of “key2” should be an object that contains the key “key3”.

If any of the above is not true, then $.key1.key2.key3 will return an error in strict mode or an empty sequence in lax mode.

A * can be used to return all objects from an object or array.

Given the following JSON object:

```
{   "type": "Feature",     "geom": { "type": "Polygon",        "coord": [[0, 0], [0,10], [10, 10], [10, 0], [0,0]]      } }
```

The following table gives examples of JSON member accessors followed by the result value.

| Member Accessor | Result |
| --- | --- |
| $ | `{ "type": "Feature", "geom": { "type": "Polygon", "coord": [[0, 0], [0,10], [10, 10], [10, 0], [0,0]] }}` |
| $.geom | `{"type": "Polygon", "coord": [[0, 0], [0,10], [10, 10], [10, 0], [0,0]] }` |
| $.geom.coord | `[[0, 0], [0,10], [10, 10], [10, 0], [0,0]]` |
| $.geom.coord[0] | `[0, 0]` |
| $.geom.coord[0].* | `0,0`**Note:** This is a sequence of two values |

In lax mode the following behaviors apply:

- If an operation requires an array but the operand is not an array, then the operand is converted to a one-item array before performing the operation.
- If an array is referenced without specifying the array element, then [*] is assumed.

    If $.grid is an array of objects containing the key “point”, ‘lax $.grid.point’ is equivalent to ‘strict $.grid[*].point’.

- If an operator requires something other than an array, but the operand is an array, then the array of X elements is converted to a sequence containing the same X elements. The operator is then performed on the newly created sequence.
- Arrays of size 1 can be treated as scalars. For example, `[`"`This`"`]` is the same as "`This`" and vice versa. $[0] returns a value for a scalar in lax mode.

- Any reference to a nonexistent key causes an empty sequence to be returned.

Doing any of the above in strict mode returns an error.
