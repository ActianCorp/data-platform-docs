---
title: "CREATE SCHEMA Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_SCHEMA_Example.htm"
canonical_id: "actian-data-platform-create-schema-example"
---

## CREATE SCHEMA Example

Create a schema for the accounting user:

```
CREATE SCHEMA AUTHORIZATION accounting       CREATE TABLE employees (lname CHAR(30) NOT NULL,              fname CHAR(30) NOT NULL,              salary MONEY,              dname CHAR(10)                      REFERENCES dept(deptname),              PRIMARY KEY (lname, fname))       CREATE TABLE dept(deptname CHAR(10) NOT NULL UNIQUE,       location CHAR(15),       budget MONEY,       expenses MONEY DEFAULT 0)       CREATE VIEW mgr(mlname, mfname, mdname) AS         SELECT lname, fname, deptname FROM employees,dept           WHERE dname = deptname       GRANT REFERENCES(lname, fname)          ON TABLE employees TO harry;
```
