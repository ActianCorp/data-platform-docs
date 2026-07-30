---
title: "WHERE Clause"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "WHERE_Clause.htm"
canonical_id: "actian-data-platform-where-clause"
---

## WHERE Clause

The WHERE clause specifies the search_conditions that rows of the table must satisfy in order to be updated.

## UPDATE Examples

Store order total information at the order level based on detail in the lineitem table.

```
UPDATE orders oSET o_totalprice =( SELECT SUM(l_extendedprice)   FROM lineitem l   WHERE l.l_orderkey = o.o_orderkey);
```
