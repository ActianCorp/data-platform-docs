---
title: "Positional Parameters Sample Syntax"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Positional_Parameters_Sample_Syntax.htm"
canonical_id: "actian-data-platform-positional-parameters-sample-syntax"
---

## Positional Parameters Sample Syntax

Here are two samples of procedure invocation with and without positional parameters.

The first example shows a mixture of positional parameters and named parameters:

```
EXECUTE PROCEDURE proc1 (25, 'abc', :a, p8 = 19, p11 = 22);
```

The third parameter value is a host variable. All positional parameters must precede all named parameters in a parameter list.

The second example shows a syntax fragment from a query containing the invocation of a table procedure:

```
...FROM table1, view3, rpp2('pqr', 'xyz', table1.col4), ...
```

All parameters in this query are specified using positional notation and the third value is a reference to a column from another FROM clause entry.
