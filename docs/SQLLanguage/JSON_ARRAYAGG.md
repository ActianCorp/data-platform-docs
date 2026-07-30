---
title: "JSON_ARRAYAGG"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_ARRAYAGG.htm"
canonical_id: "actian-data-platform-json-arrayagg"
---

## JSON_ARRAYAGG

JSON_ARRAYAGG constructs a JSON array as an aggregation of values from table rows.

```
JSON_ARRAYAGG (
```

```
    value
```

```
    ORDER BY sort_list
```

```
    [NULL | ABSENT ON NULL]
```

```
    [RETURNING datatype]
```

```
)
```

**value**

:   Specifies a constant, table column, or expression to be aggregated.

**ORDER BY**

:   Causes the items in the aggregate to be ordered in the output array. If value is a JSON_OBJECT or JSON_ARRAY constructor, the ORDER BY columns can include columns used by the JSON_OBJECT or JSON_ARRAY queries.

**NULL ON NULL | ABSENT ON NULL**

:   Specifies how nulls are handled. NULL ON NULL inserts nulls as SQL nulls. ABSENT ON NULL omits null values. Default is ABSENT ON NULL.

**RETURNING datatype**

:   Specifies the data type of the result. Datatype can be any string data type. Default is varchar(4000).

Examples

The query:

```
SELECT JSON_ARRAYAGG (unit) FROM emp;
```

returns: `[`"`1A`"`,`"`2A`"`,`"`2A`"`,`"`2B`"`]`

```
SELECT JSON_OBJECT (
```

```
   'row':emp.row,
```

```
   'units':JSON_ARRAYAGG (
```

```
             JSON_OBJECTAGG (emp.name VALUE emp.unit ABSENT ON NULL))
```

```
)
```

```
FROM emp
```

```
GROUP BY emp.row
```

returns two rows:

```
{"row" : 1, "units" : [{"Frank":"1A", "Bob:"1B"}]}
```

```
{"row" : 2, "units" : [{"Steve":"2A"}]}
```

The query:

```
SELECT JSON_OBJECT (
```

```
   'row':emp.row,
```

```
   'units':JSON_ARRAYAGG (
```

```
            JSON_OBJECT (emp.name VALUE emp.unit ABSENT ON NULL) ORDER BY emp.unit DESC)
```

```
)
```

```
FROM emp
```

```
GROUP BY emp.row
```

returns two rows:

```
{"row" : 1, "units" : [{"Bob:"1B"},{"Frank":"1A"}]}
```

```
{"row" : 2, "units" : [{}, {"Steve":"2A"}]}
```
