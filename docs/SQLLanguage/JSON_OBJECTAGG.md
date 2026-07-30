---
title: "JSON_OBJECTAGG"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_OBJECTAGG.htm"
canonical_id: "actian-data-platform-json-objectagg"
---

## JSON_OBJECTAGG

JSON_OBJECTAGG returns a JSON object where the key:value pairs of the object are an aggregate based on rows of a table.

```
JSON_OBJECTAGG (
```

```
   [JSON key and value [{,JSON key and value}...]
```

```
   [NULL|ABSENT ON NULL]
```

```
   [WITH|WITHOUT UNIQUE [KEYS]]
```

```
   [RETURNING datatype]
```

```
)
```

where the arguments have the same meaning as described in [JSON_OBJECT](../SQLLanguage/JSON_OBJECT.md).

Example:

```
SELECT JSON_OBJECTAGG (name VALUE row ABSENT ON NULL) FROM emp;
```

returns the JSON object `{`"`Frank`"`:1,`"`Steve`"`:2,`"`Bob`"`:1}`.

```
SELECT JSON_OBJECTAGG (name VALUE row NULL ON NULL) FROM emp;
```

generates an error because the last name is NULL, which is invalid.

JSON_OBJECTAGG can be used in GROUP BY clauses.

```
SELECT emp.row,
```

```
JSON_OBJECTAGG (name VALUE emp.unit ABSENT ON NULL) AS units
```

```
FROM emp GROUP BY emp.row
```

returns:

```
Row   units
```

```
1     {"Frank":"1A","Bob":"1B"}
```

```
2     {"Steve":"2A"}
```
