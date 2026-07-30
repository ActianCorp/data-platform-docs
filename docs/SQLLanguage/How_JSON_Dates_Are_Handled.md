---
title: "How JSON Dates Are Handled"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_JSON_Dates_Are_Handled.htm"
canonical_id: "actian-data-platform-how-json-dates-are-handled"
---

## How JSON Dates Are Handled

All datetime data is converted to string.

The string output format is UTC (Z) based for a TIMESTAMP WITH any time zone:
YYYY-MM-DDThh:mm:ss.s[s[s[s[s[s]]]]Z

The output format for a TIMESTAMP WITHOUT TIME ZONE omits the Z:
YYYY-MM-DDThh:mm:ss.s[s[s[s[s[s]]]]

For example, running JSON_OBJECT() on an ingresdate column produces the following output:

```
+-----------------------------------------------------------------+
```

```
|json                                                             |
```

```
+-----------------------------------------------------------------+
```

```
|{"ingresdate col":"2018-12-14T20:56:48Z"}                        |
```

```
|{"ingresdate col":"5 hrs"}                                       |
```

```
|{"ingresdate col":"5 hrs"}                                       |
```

```
|{"ingresdate col":"1 days"}                                      |
```

```
|{"ingresdate col":"2540 days"}                                   |
```

```
|{"ingresdate col":"5 hrs"}                                       |
```

```
|{"ingresdate col":"5 hrs"}                                       |
```

```
+-----------------------------------------------------------------|
```
