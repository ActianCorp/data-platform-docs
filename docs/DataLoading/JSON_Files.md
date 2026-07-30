---
title: "JSON Files"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "JSON_Files.htm"
canonical_id: "actian-data-platform-json-files"
---

## JSON Files

employee_test.json

```
{"name":"Michael", "salary":3000}
```

```
{"name":"Andy", "salary":4500}
```

```
{"name":"Justin", "salary":3500}
```

```
{"name":"Berta", "salary":4000}
```

```
{"name":"Raju", "salary":3000}
```

```
{"name":"Chandy", "salary":4500}
```

```
{"name":"Joey", "salary":3500}
```

```
{"name":"Mon", "salary":4000}
```

```
{"name":"Rachel", "salary":4000}
```

1. Create external table:

```
CREATE EXTERNAL TABLE employee_ex_json (
```

```
    name CHAR(25) NOT NULL,
```

```
    salary INTEGER NOT NULL
```

```
) USING SPARK WITH
```

```
REFERENCE='abfs://mycontainer@myaccount.dfs.core.windows.net/myblob/employee_test.json',
```

```
FORMAT = 'JSON';
```

**IMPORTANT!**Ensure that your external table column names match the names used for columns in your source data header row.

2. Create native Actian Data Platform table

```
CREATE TABLE employee_json(
```

```
    name CHAR(25) NOT NULL,
```

```
    salary INTEGER NOT NULL
```

```
) WITH STRUCTURE=X100;
```

3. Load the Actian Data Platform table with the INSERT command:

```
INSERT INTO employee_json SELECT * FROM employee_ex_json
```
