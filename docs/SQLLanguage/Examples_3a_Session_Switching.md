---
title: "Examples: Session Switching"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Examples_3a_Session_Switching.htm"
canonical_id: "actian-data-platform-examples-3a-session-switching"
---

## Examples: Session Switching

The following examples illustrate session switching inside a select loop and the resetting of status fields. The main program processes sales orders and calls the subroutine new_customer for every new customer. This example illustrates the use of numeric session identifiers.

The following is an example of the main program:

```
exec sql include sqlca;
```

```
exec sql begin declare section;
```

```
/* Include output of dclgen for declaration of
```

```
** record order_rec */
```

```
     exec sql include 'decls';
```

```
exec sql end declare section;
```

```
exec sql connect customers session 1;
```

```
exec sql connect sales session 2;
```

```
...
```

```
exec sql select * into :order_rec from orders;
```

```
exec sql begin;
```

```
     if (order_rec.new_customer = 1) then
```

```
          call new_customer(order_rec);
```

```
     endif
```

```
     process order;
```

```
exec sql end;
```

```
...
```

```
exec sql disconnect;
```

```
exec sql set_sql(session = 1);
```

```
exec sql disconnect;
```

The following is an example of subroutine new_customer from the select loop, containing the session switch:

```
subroutine new_customer(record order_rec)
```

```
begin;
```

```
     exec sql set_sql(session = 1);
```

```
     exec sql insert into accounts values
```

```
          (:order_rec);
```

```
     process any errors;
```

```
     exec sql set_sql(session = 2);
```

```
     sqlca.sqlcode = 0;
```

```
     sqlca.sqlwarn.sqlwarn0 = ' ';
```

```
end subroutine;
```
