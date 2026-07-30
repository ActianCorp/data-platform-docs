---
title: "Variable Usage"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Variable_Usage.htm"
canonical_id: "actian-data-platform-variable-usage"
---

## Variable Usage

After host language variables are declared, use them in your embedded statements. In embedded SQL statements, host language variables must be preceded by a colon, for example:

```
exec sql select ename, sal     into :name, :salary     from employee     where eno = :empnum;
```

The INTO clause contains two host language variables, name and salary, and the WHERE clause contains one, empnum.

A host language variable can have the same name as a database object, such as a column. The preceding colon distinguishes the variable from an object of the same name.

If no value is returned (for example, no rows qualified in a query), the contents of the variable are not modified.
