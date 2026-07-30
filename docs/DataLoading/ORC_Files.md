---
title: "ORC Files"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "ORC_Files.htm"
canonical_id: "actian-data-platform-orc-files"
---

## ORC Files

userdata.orc:

The ORC file does not have a header.

Column details:

```
column#   column_name           hive_datatype
```

```
==============================================
```

```
1         registration_dttm     timestamp
```

```
2         id                    int
```

```
3         first_name            string
```

```
4         last_name             string
```

```
5         email                 string
```

```
6         gender                string
```

```
7         ip_address            string
```

```
8         cc                    string
```

```
9         country               string
```

```
10        birthdate             string
```

```
11        salary                double
```

```
12        title                 string
```

1. Create external table with header=false option:

```
CREATE EXTERNAL TABLE orc_ex_test (
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
REFERENCE='s3a://<bucket>/userdata*',
```

```
FORMAT='orc',
```

```
OPTIONS=('header' = 'false','schema'='registration_dttm TIMESTAMP, id INT, first_name STRING, last_name STRING, email STRING, gender STRING, ip_address STRING, cc STRING, country STRING, birthdate STRING, salary DOUBLE, title STRING');
```

2. Create the native Actian Data Platform table:

```
CREATE TABLE orc_test(
```

```
    registration_dttm    TIMESTAMP,
```

```
    id                   INTEGER,
```

```
    first_name           VARCHAR(50),
```

```
    last_name            VARCHAR(50),
```

```
    email                VARCHAR(50),
```

```
    gender               VARCHAR(50),
```

```
    ip_address           VARCHAR(50),
```

```
    cc                   VARCHAR(50),
```

```
    country              VARCHAR(50),
```

```
    birthdate            VARCHAR(50),
```

```
    salary               FLOAT8,
```

```
    title                VARCHAR(50)
```

```
) WITH STRUCTURE=X100;
```

3. Load the Actian Data Platform table with the INSERT command

```
INSERT INTO orc_test SELECT * FROM orc_ex_test;
```
