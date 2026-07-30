---
title: "Cursors Versus Select Loops"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Cursors_Versus_Select_Loops.htm"
canonical_id: "actian-data-platform-cursors-versus-select-loops"
---

## Cursors Versus Select Loops

A select loop is a block of code associated with an embedded SELECT statement; the select loop processes the rows returned by the select. Select loops are typically used when the select returns more than one row.

The select loop is an enhancement of standard SQL. ANSI SQL does not allow more than one row to be retrieved by a SELECT statement. If multiple rows are to be retrieved, the ANSI standard requires the use of a cursor even if the rows are not updated.

Cursors enable an application to retrieve and manipulate individual rows without the restriction of the select loop. Within a select loop, statements cannot be issued that access the database. Use cursors in the following situations:

- When a program requires access to other tables while processing rows.
- When more than one table needs to be scanned simultaneously (parallel queries).

- When more than one table needs to be scanned in a nested fashion, for example, in a master-detail application.

The following two examples do the same thing. The first example uses a select loop and the second uses a cursor. Because there are no nested updates and only one result table is being processed, the select method is preferred.

```
//Select Loop Version
```

```
exec sql select ename, eno, sal    into :name, :empnum, :salary     from employee    order by ename;    exec sql begin;    print name, salary, empnum;    exec sql end;
```

```

```

```
//Cursor Versionexec sql declare c1 cursor for    select ename, eno, sal/* No INTO clause */    from employee    order by ename;    exec sql open c1;    exec sql whenever not found goto closec1;    loop while more rows    exec sql fetch c1 into :name, :salary, :empnum;    print name, salary, empnum;    end loop;    closec1:    exec sql close c1;
```
