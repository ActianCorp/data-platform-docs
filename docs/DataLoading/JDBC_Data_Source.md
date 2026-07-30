---
title: "JDBC Data Source"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "JDBC_Data_Source.htm"
canonical_id: "actian-data-platform-jdbc-data-source"
---

## JDBC Data Source

It is also possible to map tables from other databases using JDBC.

Syntax:

```
CREATE EXTERNAL TABLE ext_jdbc_hello_ingres
```

```
  (id INTEGER NOT NULL,
```

```
  txt VARCHAR(20)NOT NULL)
```

```
USING SPARK WITH REFERENCE='dummy',
```

```
FORMAT='jdbc',
```

```
OPTIONS=('url' = 'db_connection_url',
```

```
     'dbtable' = 'table_name',
```

```
     'user' = 'username',
```

```
     'password' = 'password')
```

!!! note "Note"

    The JDBC URL, the table name to access, and the user name and password are specified in the OPTIONS clause. The value specified WITH REFERENCE (dummy in this example) is not used, but the syntax requires a REFERENCE clause.

JDBC Data Source:

1. Create the external table for the Actian Data Platform data source:

```
CREATE EXTERNAL TABLE employee_ex_jdbc (
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
REFERENCE='dummy',
```

```
FORMAT='jdbc',
```

```
OPTIONS=('url' = 'jdbc:actian://usau-hcl-lnx01:V27/sparktest',
```

```
         'dbtable' = 't1',
```

```
         'user' = 'user1' ,
```

```
         'password' = 'pass123');
```

    In this example, we map the table t1 in database sparktest on node V2 on host usau-hcl-lnx01 to the external table employee_ex_jdbc and connect as user user1 using password pass123.

2. Create the native Actian Data Platform table:

```
CREATE TABLE employee_jdbc(
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
INSERT INTO employee_jdbc SELECT * FROM employee_ex_jdbc;
```

**WARNING!**The specified user credentials are visible for all users that can connect to the database.
