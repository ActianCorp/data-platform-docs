---
title: "Variable Structures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Variable_Structures.htm"
canonical_id: "actian-data-platform-variable-structures"
---

## Variable Structures

To simplify data transfer in and out of database tables, embedded SQL allows the usage of variable structures in the SELECT, FETCH, UPDATE, and INSERT statements. Structures must be specified according to the rules of the host language and must be declared in an embedded SQL declare section. For structures to be used in SELECT, INSERT, and UPDATE statements, the number, data type, and order of the structure elements must correspond to the number, data type, and order of the table columns in the statement.

For example, if you have a database table, employee, with the columns, ename (char(20)) and eno (integer), you can declare the following variable structure:

```
emprec,     ename character_string(20),     eno integer;
```

and issue the following SELECT statement:

```
exec sql select *     into :emprec.ename, :emprec.eno     from employee     where eno = 23;
```

It is also legal to specify only the structure name in the statement. If this is done, each variable structure must correspond to the table specified in the statement. The number, data type, and order of the structure elements must correspond to the number, data type, and order of the table columns in the statement.

```
exec sql select *     into :emprec     from employee     where eno = 23;
```

The embedded SQL preprocessor expands the structure name into the names of the individual members. Placing a structure name in the INTO clause has the same effect as enumerating all members of the structure in the order in which they were declared.

A structure can also be used to insert values in the database table. For example:

```
exec sql insert into employee (ename,eno)     values (:emprec);
```
