---
title: "Column Masking Example"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Column_Masking_Example.htm"
canonical_id: "actian-data-platform-column-masking-example"
---

## Column Masking Example

This example implements partial masking of data in a view. Such masking is often used for displaying credit card numbers. A privileged user creates the view, which unprivileged users (that is, without the UNMASK privilege) can then safely use because the credit card number is partially masked.

```
CREATE TABLE masking_table (int_masked INTEGER8 MASKED NOT NULL);INSERT INTO masking_table VALUES
```

```
(4556288950166430),
```

```
(4929591048738619),
```

```
(4929933452574454),
```

```
(4929571480910157),
```

```
(4557432740524776);
```

Issued by a privileged user:

```
CREATE VIEW masking_view ASSELECT DISTINCT CONCAT (
```

```
    MASK_COLUMN (SUBSTR (varchar (int_masked), 1, 4) AS BASIC), ' ',
```

```
    MASK_COLUMN (SUBSTR (varchar (int_masked), 5, 4) AS BASIC), ' ',
```

```
    MASK_COLUMN (SUBSTR (varchar (int_masked), 9, 4) AS BASIC), ' ',
```

```
    MASK_COLUMN (SUBSTR (varchar (int_masked), 13, 4) AS UNMASK)
```

```
    ) AS "partial cc"
```

```
FROM masking_table;SELECT * FROM masking_view ORDER BY 1;+-------------------+
```

```
|partial cc         |
```

```
+-------------------+
```

```
|4556 2889 5016 6430|
```

```
|4557 4327 4052 4776|
```

```
|4929 5714 8091 0157|
```

```
|4929 5910 4873 8619|
```

```
|4929 9334 5257 4454|
```

```
+-------------------+
```

Issued by an unprivileged user:

```
SELECT * FROM masking_view ORDER BY 1;+-------------------+
```

```
|partial cc         |
```

```
+-------------------+
```

```
|**** **** **** 0157|
```

```
|**** **** **** 4454|
```

```
|**** **** **** 4776|
```

```
|**** **** **** 6430|
```

```
|**** **** **** 8619|
```

```
+-------------------+
```
