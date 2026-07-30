---
title: "JSON Scalars"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Scalars.htm"
canonical_id: "actian-data-platform-json-scalars"
---

## JSON Scalars

A JSON scalar can be a string, number, null, or Boolean.

Strings must be double quoted.

JavaScript escape rules for strings apply: a single quote (') in a double quoted string is represented as two consecutive single quotes. Example: `"six o'' clock"`

A backslash can be used to escape nested quotes. Any or all characters can be represented by using the string "\u" followed by four hexadecimal digits representing the UTF-16 surrogate pairs for representing Unicode characters. Examples:

`"They said \"correct\""`

`"Fran\u00e7ois"` for “François”

Floats can be entered in exponential format. Example: 1.23E08

A JSON null is different from an Actian null value. A JSON null is considered a unique value of its own data type and is equal to another JSON null.

The comparison (NULL == NULL) returns TRUE. Actian nulls used in JSON expressions are converted to JSON nulls.

A JSON Boolean is TRUE or FALSE.
