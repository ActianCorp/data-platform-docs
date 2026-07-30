---
title: "DECLARE Example"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DECLARE_Example.htm"
canonical_id: "actian-data-platform-declare-example"
---

## DECLARE Example

The following example demonstrates some declarations and uses of local variables:

```
CREATE PROCEDURE variables (vmny MONEY NOT NULL) AS       DECLARE       vi4    INTEGER NOT NULL;       vf8    FLOAT;       vc11   CHAR(11) NOT NULL;       vdt    DATE;       BEGIN       vi4 = 1234;       vf8 = null;       vc11 = '26-jun-1957';       vdt = date(:vc11);       vc11 = :vmny;--data type conversion error       vmny = :vf8;--null to non-null conversion              error       RETURN :vi4;END;
```
