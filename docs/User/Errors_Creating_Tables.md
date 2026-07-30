---
title: "Errors Creating Tables"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Errors_Creating_Tables.htm"
canonical_id: "actian-data-platform-errors-creating-tables"
---

## Errors Creating Tables

Creating and querying the following table results in an error. This table:

```
create external table customer_orig_ext(
```

```
    customer_id integer ,
```

```
    account_num integer,
```

```
    lname varchar(30),
```

```
    fname varchar(30),
```

```
    mi varchar(30),
```

```
    address1 varchar(30),
```

```
    address2 varchar(30),
```

```
    address3 varchar(30),
```

```
    address4 varchar(30),
```

```
    city varchar(30),
```

```
    state varchar(2),
```

```
    zipcode varchar(5),
```

```
    country varchar(30),
```

```
    region_id integer ,
```

```
    phone1 varchar(30),
```

```
    phone2 varchar(30),
```

```
    birthdate varchar(30) ,
```

```
    marital_status varchar(30),
```

```
    yearly_income varchar(30),
```

```
    gender varchar(1),
```

```
    total_children integer,
```

```
    num_children_at_home integer,
```

```
    education varchar(30),
```

```
    date_accnt_opened varchar(30) ,
```

```
    member_card varchar(30) ,
```

```
    occupation varchar(30) ,
```

```
    houseowner varchar(30) ,
```

```
    num_cars_owned integer,
```

```
    fullname varchar(60)
```

```
)using spark WITH reference='gs://prrbucket/customer_orig.csv', format='csv',options=('header'='false', 'quote'='"', 'nullValue'='null', 'sep'=',');
```

```

```

```

```

```
select * from customer_orig_ext;
```

results in this error:

```
[Actian][Ingres ODBC Driver][Ingres]External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`customer_id`' given input columns: [src_39._c11, src_39._c0, src_39._c25, src_39._c22, src_39._c4, src_39._c19, src_39._c8, src_39._c24, src_39._c21, src_39._c9, src_39._c14, src_39._c27, src_39._c2, src_39._c18, src_39._c20, src_39._c15, src_39._c10, src_39._c7, src_39._c3, src_39._c13, src_39._c12, src_39._c23, src_39._c6, src_39._c26, src_39._c5, src_39._c1, src_39._c28, src_39._c16, src_39._c17]; line 1 pos 48; 'InsertIntoTable 'UnresolvedRelation `customer_orig_ext_40`, false, false +- 'Project ['customer_id, 'account_num, 'lname, 'fname, 'mi, 'address1, 'address2, 'address3, 'address4, 'city, 'state, 'zipcode, 'country, 'region_id, 'phone1, 'phone2, 'birthdate, 'marital_status, 'yearly_income, 'gender, 'total_children, 'num_children_at_home, 'education, 'date_accnt_opened, ... 5 more fields] +- SubqueryAlias `src_39` +- Relation[_c0#2019,_c1#2020,_c2#2021,_c3#2022,_c4#2023,_c5#2024,_c6#2025,_c7#2026,_c8#2027,_c9#2028,_c10#2029,_c11#2030,_'.
```

Reason and correction:

You need to specify the schema option to define the underlying file to Spark:

```
'schema'='customer_id int, account_num int, lname string, ...
```
