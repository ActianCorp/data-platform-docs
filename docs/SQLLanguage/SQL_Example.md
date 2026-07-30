---
title: "SQL Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_Example.htm"
canonical_id: "actian-data-platform-sql-example"
---

## SQL Example

To get all the tables of a schema, sample in this case, you could use this code:

```
\trim SELECT
```

```
    'select '+x'27',
```

```
    table_name as "table name",
```

```
    x'27'+', count(*) from sample.',
```

```
    table_name as tablename
```

```
FROM information_schema.tables where table_schema = 'sample'
```

```
FETCH FIRST 1 ROW ONLY;
```

```
SELECT
```

```
    'union all',
```

```
    'select '+x'27',
```

```
    table_name as "table name",
```

```
    x'27'+', count(*) from sample.',
```

```
    table_name as tablename
```

```
FROM information_schema.tables where table_schema = 'sample'
```

```
OFFSET 1;
```

```
\g
```

You could put this in a script to enhance it further: call the script giving the SQL connectivity string to the respective warehouse and optionally the schema name. Output is in comma-separated format ready to be loaded anywhere.

```
#!/bin/bash
```

```
set -e
```

```
#DBCONNECT=@av-mc07gf2l3329.avstage.actiandatacloud.com,tcp_ip,27832[dbuser,password]::db
```

```
DBCONNECT=$1
```

```
SCHEMA=$2
```

```
: ${SCHEMA:=sample}
```

The desired generated SQL query result from the first SQL call looks like this:

```
select 'ontime', count(*) from sample.ontime\g
```

Awk appends the \g to the generated query (something not possible in SQL).

The second SQL call executes that generated query.

The first SELECT statement is optional. It is the header for the comma-separated output:

```
sql -S ${DBCONNECT} <<-EOF | awk '\{print}END\{print "\\g"}' | sql -S ${DBCONNECT} \trim SELECT
```

```
    'select '+x'27'+' table_name'+x'27',
```

```
    ','+x'27'+','+x'27'+',',
```

```
    x'27'+'        rows'+x'27'+';';
```

```
SELECT
```

```
    'select '+x'27',
```

```
    table_name as "table name",
```

```
    x'27'+'as table,'+x'27'+','+x'27',
```

```
    ', count(*) as rows from '+x'22'+'${SCHEMA}'+x'22'+'.',
```

```
    table_name as tablename
```

```
FROM information_schema.tables where table_schema = '${SCHEMA}'
```

```
FETCH FIRST 1 ROW ONLY;
```

```
SELECT
```

```
    'union all',
```

```
    'select '+x'27',
```

```
    table_name as "table name",
```

```
    x'27'+'as table,'+x'27'+','+x'27',
```

```
    ', count(*) from '+x'22'+'${SCHEMA}'+x'22'+'.',
```

```
    table_name as tablename
```

```
FROM information_schema.tables where table_schema = '${SCHEMA}'
```

```
OFFSET 1;
```

```
\g
```

```
EOF
```
