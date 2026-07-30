---
title: "FETCH Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "FETCH_Examples.htm"
canonical_id: "actian-data-platform-fetch-examples"
---

## FETCH Examples

1. Typical fetch, with associated cursor statements.

```
exec sql begin declare section;    name character_string(20);    age integer;exec sql end declare section;exec sql declare cursor1 cursor for    select ename, age    from employee    order by ename;...exec sql open cursor1 for readonly;loop until no more rows    exec sql fetch cursor1        into :name, :age;    print name, age;end loop;exec sql close cursor1;
```

    Assuming the structure:

```
Emprec    name character_string(20),    age integer;
```

    the fetch in the above example can be written as:

```
exec sql fetch cursor1    into :emprec;
```

    The preprocessor interprets that statement as though it had been written:

```
exec sql fetch cursor1    into :emprec.name, :emprec.age;
```

2. Fetch, using an indicator variable.

```
exec sql fetch cursor2 into :name, :salary:salary_ind;
```
