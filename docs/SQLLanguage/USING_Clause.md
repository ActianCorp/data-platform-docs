---
title: "USING Clause"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "USING_Clause.htm"
canonical_id: "actian-data-platform-using-clause"
---

## USING Clause

The USING clause directs the Actian Data Platform to use the variables pointed to by the sqlvar elements of the SQLDA (or other host language variables) when executing the statement.

The USING clause has the following syntax:

```
USING DESCRIPTOR descriptor_name
```

The keyword descriptor is optional in some statements that accept the USING clause.

The statements that accept the USING clause are:

- DESCRIBE
- EXECUTE

- EXECUTE IMMEDIATE
- EXECUTE PROCEDURE

- FETCH
- OPEN

- PREPARE
