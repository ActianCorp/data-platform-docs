---
title: "JSON_OBJECT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_OBJECT.htm"
canonical_id: "actian-data-platform-json-object"
---

## JSON_OBJECT

The JSON_OBJECT constructor creates a JSON object from relational data.

```
JSON_OBJECT (   [JSON key and value [{,JSON key and value}...]   [NULL|ABSENT ON NULL]   [WITH|WITHOUT UNIQUE [KEYS]]   [RETURNING datatype])
```

where:

**JSON key and value**

:   Specifies the values in the table that you want to use for key and value in the key:value pair, using the following form:

```
[KEY] name VALUE value | name:value
```

:   The value used for name must be a string. A maximum of 100 key:value pairs is allowed. The KEY keyword is optional and has no affect on the returned object.

**NULL ON NULL | ABSENT ON NULL**

:   Specifies how nulls are handled. NULL ON NULL uses the string “null” if the input value is null. ABSENT ON NULL omits this key:value pair from the returned object. Default is NULL ON NULL.

**WITH UNIQUE [KEYS] | WITHOUT UNIQUE [KEYS]**

:   WITH UNIQUE returns an error if the object created by JSON_OBJECT has duplicate keys in its key:value pairs. For example, `{`"`Name`"`:`"`Frank`"`,`"`Name`"`:`"`Bob`"`}` generates an error.

:   WITHOUT UNIQUE does not enforce unique keys but does not require them. Default is WITHOUT UNIQUE.

**RETURNING datatype**

:   Specifies the data type of the result. Any string data type is permitted. Default is varchar(4000).

JSON_OBJECT is typically used in a select. For example:

Assume a table emp that contains the following rows:

```
+-------------+----------+-------+|row          |name      | unit  |+-------------+----------+-------+|            1|Frank     | 1A    ||            2|Steve     | 2A    ||            1|Bob       | 1B    ||            2|null      | 2B    |+-------------+----------+-------+
```

```
SELECT JSON_OBJECT (KEY 'id' VALUE emp.row,             KEY 'name' VALUE emp.name) FROM emp;
```

returns four JSON objects:

```
{"id": 1, "name": "Frank"}{"id": 2, "name": "Steve"}{"id": 1, "name": "Bob"}{"id": 2, "name": null}
```

If ABSENT ON NULL was specified in the above query, the row corresponding to unit 2B would be omitted and the result would only contain three rows.
