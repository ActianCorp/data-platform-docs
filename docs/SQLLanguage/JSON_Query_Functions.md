---
title: "JSON Query Functions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Query_Functions.htm"
canonical_id: "actian-data-platform-json-query-functions"
---

## JSON Query Functions

JSON functions perform queries against JSON objects.

**IS JSON**

:   Validates a string and returns TRUE if the string is a valid JSON value.

```
value IS [NOT] JSON
```

```
    type
```

```
    [WITH | WITHOUT UNIQUE [KEYS]]
```

    value is any valid string constant, column, or expression.

    type is one of VALUE, ARRAY, OBJECT, or SCALAR. A type of VALUE means any valid value (ARRAY, OBJECT, or SCALAR). If not specified, type defaults to OBJECT.

    IS NOT JSON returns TRUE if the input value does not match the specified type.

    IS JSON returns TRUE if the input value matches the specified type.

    WITH UNIQUE KEYS causes JSON objects to return TRUE for IS JSON OBJECT or FALSE for IS NOT JSON OBJECT only if the objects have unique keys.

    WITHOUT UNIQUE KEYS allows objects to return TRUE for IS JSON OBJECT or FALSE for IS NOT JSON OBJECT regardless of whether the object has unique keys.

    Default is WITHOUT UNIQUE KEYS.

**JSON_EXISTS**

:   Returns TRUE if one or more keys specified by the JSON API common syntax (as described in [JSON API Common Syntax](../SQLLanguage/JSON_API_Common_Syntax.md)) are found.

```
JSON_EXISTS (
```

```
json_api_common_syntax
```

```
[json_exists_error_behavior ON ERROR]
```

```
)
```

```

```

:   The ON ERROR clause indicates the value returned if the common syntax returns an error (for example, item not existing in strict mode). Valid values for json_exists_error_behavior are TRUE, FALSE, or ERROR. Default is FALSE ON ERROR. If the context of json_api_common_syntax is NULL, the return value is FALSE.

:   Example: Assume a table “shapes” with a column “document” containing:

```
{"type": "Feature", "name": "JSON"}
```

    The query `JSON_EXISTS (shapes.document, '$.type')`returns TRUE.

**JSON_VALUE**

:   Returns a JSON scalar for value specified by a JSON API common syntax.

:   JSON_VALUE expects that the path expression will return exactly one value. Returning more than one value is an error.

```
JSON_VALUE (     json_api_common_syntax     [RETURNING datatype]     [ERROR | NULL | DEFAULT value_expression ON EMPTY]     [ERROR | NULL | DEFAULT value_expression ON ERROR])
```

```

```

:   If the context item of json_api_common_syntax is NULL, JSON_VALUE returns a null of the RETURNING data type.

:   The RETURNING clause specifies the data type for the return value. It can be a string, numeric, or Boolean. The default is a varchar(4000).

:   The ON EMPTY clause specifies what to do if json_api_common_syntax returns 0 items. The default is NULL ON EMPTY. DEFAULT value_expression means: Evaluate the expression value, cast the result to the target data type, and return the result.

:   The ON ERROR clause specifies how to handle errors returned during processing of the statement. The default is NULL ON ERROR.

:   **Notes**:

        - When using JSON_VALUE in a constraint, be sure to not return nulls if you use a comparison operator like = or !=, since a null will always return FALSE for both.

        - Comparisons: The constraint must include an IS NULL clause or avoid using NULL for ON EMPTY or ON ERROR.

**JSON_QUERY**

:   Returns a JSON array or JSON object for values specified by the JSON API common syntax.

:   JSON_QUERY returns an error if a JSON scalar is returned unless the WITH WRAPPER option is specified.

:   JSON_VALUE should be used for returning scalars.

```
JSON_QUERY (     json_api_common_syntax     RETURNING datatype     [WITHOUT [ARRAY] WRAPPER]     [WITH [CONDITIONAL | UNCONDITIONAL] [ARRAY] WRAPPER]     [ERROR | NULL | EMPTY ARRAY | EMPTY OBJECT ON EMPTY]     [ERROR | NULL | EMPTY ARRAY | EMPTY OBJECT ON ERROR])
```

    If the context of json_api_common_syntax is NULL, JSON_QUERY returns NULL.

    WITH WRAPPER means the sequence of values returned by json_api_common_syntax can be inserted into an array. If this occurs, the return value is the array of values. If UNCONDITIONAL, the array wrapping is always done. If CONDITIONAL, the array wrapping is not done if the sequence consists of only one value and the value is an array or JSON object. The default for WITH WRAPPER is UNCONDITIONAL.

    WITHOUT WRAPPER, the default behavior, does not attempt to wrap values. If the return sequence is not an array or JSON object an error is returned.

    Example: Assuming a value of `{col1:[1], col2:"test"}`, the following shows results of selecting this value using the following queries and path specifications:

|  | $.col1 | $.col2 |
| --- | --- | --- |
| JSON_VALUE | error | test |
| JSON_QUERY WITHOUT ARRAY | [1] | error |
| JSON_QUERY WITH UNCONDITIONAL ARRAY | [[1]] | [“test”] |
| JSON_QUERY WITH CONDITIONAL ARRAY | [ 1 ] | [“test”] |

:   ON EMPTY specifies the desired behavior if json_api_common_syntax returns 0 items. Default is NULL ON EMPTY.

:   ON ERROR handles errors that occur during processing of the query. An error can be triggered due to returning a non-array/object WITHOUT WRAPPER. Default is NULL ON ERROR.

:   For both the ON EMPTY and ON ERROR clauses, EMPTY ARRAY means JSON_QUERY returns [ ], which is an array with 0 items. EMPTY OBJECT means JSON_QUERY returns { }, which is an object with 0 items.

    The ON EMPTY clause cannot be used with the WITH ARRAY WRAPPER clause. (It is not needed regardless because it will wrap an empty sequence to an array with 0 items.)

    The RETURNING clause specifies a string data type for the return value of the function. The default is varchar(4000).

    **Notes:**

    - When using JSON_QUERY in a constraint, be sure to not return nulls if you use a comparison operator like = or !=, because a null will always return FALSE for both.

    - Comparisons: The constraint must include an IS NULL clause or avoid using NULL for ON EMPTY or ON ERROR.
