---
title: "Null Indicator Arrays and Host Structures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Null_Indicator_Arrays_and_Host_Structures.htm"
canonical_id: "actian-data-platform-null-indicator-arrays-and-host-structures"
---

## Null Indicator Arrays and Host Structures

You can use host structures with the SELECT, FETCH, and INSERT statements wherever these statements allow host language variables to be used. An array of indicator variables can be used in conjunction with a host structure to detect whether a null has been assigned to an element of the host structure.

An indicator array is an array of 2-byte integers and is typically declared in the same declare section as its associated host language variable structure. Each element of the indicator array acts as an indicator variable to the correspondingly ordered member of the host structure.

The following example declares a host language variable structure, emprec, and an associated indicator array, empind.

```
emprec     ename        character(20),     eid          integer,     esal         float;
```

```
empind array(3)of short_integer;
```

The following example illustrates the use of a host structure and indicator array in an embedded statement:

```
exec sql select name, id, sal     into :emprec:empind     from employee     where number = 12;
```

In the preceding example, if the value of the employee id column is null, a value of -1 is assigned to the second element of the empind array.
