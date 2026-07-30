---
title: "PARQUET Files"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "PARQUET_Files.htm"
canonical_id: "actian-data-platform-parquet-files"
---

## PARQUET Files

userdata.parquet:

This is a file containing data in PARQUET format. The file has a header.

Column details:

```
column#	 column_name	hive_datatype
```

```
===============================================
```

```
1         registration_dttm       timestamp
```

```
2         id                      int
```

```
3         first_name              string
```

```
4         last_name               string
```

```
5         email                   string
```

```
6         gender                  string
```

```
7         ip_address              string
```

```
8         cc                      string
```

```
9         country                 string
```

```
10        birthdate               string
```

```
11        salary                  double
```

```
12        title                   string
```

1. Create the external table:

```
CREATE EXTERNAL TABLE parquet_ex_test (
```

```
     registration_dttm     TIMESTAMP,
```

```
     id                    INTEGER,
```

```
     first_name            VARCHAR(50),
```

```
     last_name             VARCHAR(50),
```

```
     email                 VARCHAR(50),
```

```
     gender                VARCHAR(50),
```

```
     ip_address            VARCHAR(50),
```

```
     cc                    VARCHAR(50),
```

```
     country               VARCHAR(50),
```

```
     birthdate             VARCHAR(50),
```

```
     salary                DECIMAL(18,2),
```

```
     title                 VARCHAR(50)
```

```
) USING SPARK WITH
```

```
REFERENCE='abfs://loadtest@avalanchetest.dfs.core.windows.net/userdata.parquet',
```

```
FORMAT = 'parquet';
```

2. Create the native Actian Data Platform table:

```
CREATE TABLE parquet_test(
```

```
     registration_dttm     TIMESTAMP,
```

```
     id                    INTEGER,
```

```
     first_name            VARCHAR(50),
```

```
     last_name             VARCHAR(50),
```

```
     email                 VARCHAR(50),
```

```
     gender                VARCHAR(50),
```

```
     ip_address            VARCHAR(50),
```

```
     cc                    VARCHAR(50),
```

```
     country               VARCHAR(50),
```

```
     birthdate             VARCHAR(50),
```

```
     salary                DECIMAL(18,2),
```

```
     title                 VARCHAR(50)
```

```
) WITH STRUCTURE=X100;
```

3. Load the Actian Data Platform table with the INSERT command

```
INSERT INTO parquet_test SELECT * FROM parquet_ex_test
```

!!! note "Note"

    If the file does not have a header, include schema in OPTIONS, as shown in the external table to load an ORC file.
