---
title: "JSON API Common Syntax"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_API_Common_Syntax.htm"
canonical_id: "actian-data-platform-json-api-common-syntax"
---

## JSON API Common Syntax

All JSON query functions need an input JSON value to process, a path specification that indicates what values of the JSON value to use (since the input value can be an object), and other optional parameters. Queries use the JSON API common syntax to specify these items.

The JSON API common syntax has the following format:

```
'json_context , json_path' [json_passing]
```

where:

**json_context**

:   Specifies the context item—the item to run the JSON path against. Typically, it is the database column containing the JSON objects.

**json_path**

:   Specifies a JSON path expression like the following example:

```
'LAX $.owner ? (@.assettag == $serial )' PASSING table1.sno AS "serial"'
```

:   The path expression consists of three sections:

1. The keyword LAX or STRICT to indicate the mode
2. A member accessor (starting with $) that represents the values to be returned from the JSON context item

3. A filter expression that begins with ? followed by a predicate expression in parentheses

    The filter expression causes the JSON path to return only those values that are qualified by the filter expression. It is like an SQL WHERE clause. In the filter expression, the special variable @ references the current JSON item in the sequence being examined.

    In the example above, @.assettag refers to $.owner.assettag.

    The path expression can also include a PASSING clause, described below.

**json_passing**

:   (Optional) The json_passing option is a method of using a constant or database column in the JSON path. The syntax is:

```
PASSING value AS identifier, [value AS identifier, ...]
```

:   Example:

```
PASSING t1.id AS "idno", t1.seat AS "seat"
```

:   In the JSON path, $idno is replaced with t1.id and $seat is replaced with t1.seat during query execution.

:   If a string column or constant uses FORMAT JSON AS in its passing clause, then the string is treated as a JSON object rather than a string. The JSON object (if a valid one) can have its key:values processed using standard member accessors. For example:

:   Assume a table employee with the following rows:

```
id      datacol - a varchar(100)
```

```
100     NULL
```

```
200     {"emptype":"contractor", "office":"home"}
```

```
300     {"emptype":"intern", "salary":"hourly"}
```

    The query:

```
SELECT id FROM employees e
```

```
    WHERE JSON_EXISTS (e.jsoncol, 'LAX $ ? ($J2.emptype == "intern")'
```

```
       PASSING e.jsoncol FORMAT JSON AS 'J2' )
```

:   returns one value: 300.

The JSON API common syntax is used in query functions to specify what values to return from JSON data stored in the database. For example:

```
SELECT c FROM t01 WHERE JSON_EXISTS (c, 'LAX $ ? (@.col.Name SIMILAR TO "d%"')
```

For more information on JSON query functions, see [JSON Query Functions](../SQLLanguage/JSON_Query_Functions.md).
