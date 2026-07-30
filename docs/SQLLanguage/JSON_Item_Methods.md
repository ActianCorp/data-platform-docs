---
title: "JSON Item Methods"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "JSON_Item_Methods.htm"
canonical_id: "actian-data-platform-json-item-methods"
---

## JSON Item Methods

Item methods are postfix operators that operate on a JSON value and return a JSON item. When run against a sequence the method is applied to each item in the sequence.

Multiple item methods can be used. For example: `$.agestring.double().floor()`

!!! note "Note"

    All item methods except for type() and size() unwrap arrays in lax mode.

**Type()**

    - Returns a character string

    - Returns “null”, “Boolean”, “number”, “string”, “array”, or “object”

    - Does not unwrap arrays. Returns “array” even in lax mode.

    Example: `LAX $.* ? (@.TYPE() ==`"`number`"`)`

**Size()**

    - Returns an integer value

    - For an object or scalar, returns 1

    - For an array, returns the number of elements of the array

    - Does not unwrap arrays even in lax mode

    Example: `strict $.[1] ? (@.type() ==`"`array`"`&& @.size() > 1)`

**Numeric methods**

    - Ceiling(), floor(), abs() have the same functionality as the numeric functions in SQL.

    - Double() coerces a string or numeric into a numeric float.

**Keyvalue()**

    - Used to examine an object with unknown schema.

    - Returns a sequence of objects with three key-value pairs whose keys are name, value, and id. One object is returned for each key:value pair of the input object.

        - –Name and value will be the keys and values of the object.

        - –Id is an integer that is a unique identifier for the input SQL or JSON object.

    Assume a query runs the keyvalue() method on X objects and each object has Y key:value pairs. X*Y total objects are returned, and every “Y” object will have a unique ID that corresponds to the original object. The id allows reconstructing the original objects from the output of keyvalue().

    **Note:**The ids are only unique within the scope of the query that uses keyvalue(). The same objects can have different id numbers when run in separate queries.

    - In lax mode, the input is unwrapped, so keyvalue() on an array of X items returns a sequence of X items.

    - Id numbers are only unique for the query in which keyvalue() is called. They can be reused in other queries.

    Example: Given the object `{who:`"`Fred`"`, what: 64}`, keyvalue() returns:

```
{name: "who", value: "Fred", id: 9045},
```

```
{name: "what", value: 64, id: 9045}
```

    To find the value of all “names”, select `Keyvalue().name` which returns the sequence`(`"`who`"`,`"`what`"`).`

    Example: Given the sequence:

```
[{"Building":"Empire", "Unit":"3F"}, {"row":"A", "Seat":6}]
```

:   keyvalue() returns four objects:

```
{ name: "Building", value: "Empire", id: 1000 },
```

```
{ name: "Unit", value: "3F", id: 1000 },
```

```
{ name: "row", value: "A", id: 1001 },
```

```
{ name: "Seat", value: 6, id: 1001 }
```
