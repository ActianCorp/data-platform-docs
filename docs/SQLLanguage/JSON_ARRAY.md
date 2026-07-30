---
title: "JSON_ARRAY"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_ARRAY.htm"
canonical_id: "actian-data-platform-json-array"
---

## JSON_ARRAY

JSON_ARRAY constructs a JSON array from a list of data.

```
JSON_ARRAY (
```

```
    [value [{,value}...]]
```

```
    [NULL|ABSENT ON NULL]
```

```
    [RETURNING datatype]
```

```
)
```

**value**

:   Specifies one or more constants, table columns, or expressions. Only 100 values can be used in a single JSON_ARRAY statement.

**NULL ON NULL | ABSENT ON NULL**

:   Specifies how nulls are handled. NULL ON NULL inserts nulls as SQL nulls. ABSENT ON NULL omits null values. Default is ABSENT ON NULL.

**RETURNING datatype**

:   Specifies the data type of the result. Datatype can be any string data type. Default is varchar(4000).

Example:

```
SELECT JSON_ARRAY ('test', emp.unit, emp.name) FROM emp WHERE "row" = 1
```

returns:

```
["test"”, "1A", "Frank"]
```

```
["test", "1B", "Steve"]
```
