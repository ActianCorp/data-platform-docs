---
title: "How Parameters Are Passed in Database Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_Parameters_Are_Passed_in_Database_Procedures.htm"
canonical_id: "actian-data-platform-how-parameters-are-passed-in-database-procedures"
---

## How Parameters Are Passed in Database Procedures

By default, the EXECUTE PROCEDURE statement passes parameters to a database procedure by value. To pass a value by reference, use the BYREF option. If a parameter is passed by reference, the called database procedure can change the contents of the variable, and the change is visible to the calling program.

In addition to the BYREF option for passing parameters from an invoking application, parameters can be passed in one of three declared modes: IN, OUT, and INOUT. IN is the default parameter mode and is equivalent to the by value mode described above. It cannot return values to the calling procedure or application. The OUT and INOUT modes allow the passing of possibly modified parameter values back to the calling database procedure or triggering operation, for example, allowing the application to modify a column value in a row before it is inserted or updated.

Example:

```
CREATE PROCEDURE getnamezip (IN custno int NOT NULL, OUT custname, OUT custzip)
```

```
AS
```

```
DECLARE
```

```

```

```
p_errnum        INTEGER NOT NULL NOT DEFAULT;
```

```
p_rowcount      INTEGER NOT NULL NOT DEFAULT;
```

```

```

```
BEGIN
```

```

```

```
        ...
```

```
        SELECT  c_name,
```

```
                c_zip
```

```
        INTO    :custname,
```

```
                :custzip
```

```
        FROM    customer
```

```
        WHERE   c_id = :custno;
```

```
        ...
```

```

```

```
END;
```

```

```

```

```

```
EXECUTE PROCEDURE getnamezip (custno   = :w_custno,
```

```
                                custname = :w_custname,
```

```
                                custzip  = :w_custzip);
```
