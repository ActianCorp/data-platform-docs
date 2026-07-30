---
title: "JSON Objects"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Objects.htm"
canonical_id: "actian-data-platform-json-objects"
---

## JSON Objects

A JSON object is a comma separated list of key:value pairs surrounded by braces {}.

A key must be a double-quoted string. A value can be any JSON value including a JSON object or JSON array. It cannot be blank.

Whitespace is ignored in a JSON object string except for whitespace within the double quotes of a string.

Example:

```
{  "type": "Feature",     "geometry": {           "type": "Point",          "coordinates": [0, 90] },           "properties": { "name": "North Pole" }      }}
```

Keys in a JSON object do not have to be unique. During key retrieval, however, only the first value is returned.

In addition, JSON objects are considered an unordered set of key:value pairs, so subsequent key retrievals may return the “other” duplicate key.

You can create a JSON object from table data using the JSON_OBJECT constructor, as described in [JSON_OBJECT](../SQLLanguage/JSON_OBJECT.md).
