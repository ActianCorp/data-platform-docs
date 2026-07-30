---
title: "SELECT (embedded) Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SELECT_(embedded)_Examples.htm"
canonical_id: "actian-data-platform-select-embedded-examples"
---

## SELECT (embedded) Examples

The following examples illustrate the non-cursor SELECT statement:

1. Retrieve the name and salary of an employee. Drop locks by committing the following transaction.

```
EXEC SQL SELECT ename, sal    INTO :namevar, :salvar    FROM employee    WHERE eno = :numvar;EXEC SQL COMMIT;
```

2. Select all columns in a row into a host language variable structure. (The emprec structure has members that correspond in name and type to columns of the employee table.)

```
EXEC SQL SELECT *    INTO :emprec    FROM employee    WHERE eno = 23;
```

3. Select a constant into a variable.

```
EXEC SQL SELECT 'Name: ', ename    INTO :title, :ename    FROM employee    WHERE eno >= 148 AND age = :age;
```

4. Select the row in the employee table whose number and name correspond to the variables, numvar and namevar. The columns are selected into a host structure called emprec. Because this statement is issued many times (in a subprogram, perhaps), it is formulated as a repeat query.

```
EXEC SQL REPEATED SELECT *     INTO :emprec    FROM employee    WHERE eno = :numvar AND ename = :namevar;
```

5. Example of a select loop: insert new employees, and select all employees and generate a report. If an error occurs during the process, end the retrieval and back out the changes. No database statements are allowed inside the select loop (BEGIN-END block).

```
error = 0;
```

```
EXEC SQL INSERT INTO employee
```

```
    SELECT * FROM newhires;
```

```
EXEC SQL SELECT eno, ename, eage, esal, dname
```

```
        INTO :eno, :ename, :eage, :esal, :dname
```

```
    FROM employee e, dept d
```

```
    WHERE e.edept = d.deptno
```

```
    GROUP BY ename, dname
```

```
EXEC SQL BEGIN;
```

```
    generate report of information;
```

```
    if error condition then
```

```
        error = 1;
```

```
        EXEC SQL ENDSELECT;
```

```
    end if;
```

```
EXEC SQL END;
```

```
/*
```

```
** Control transferred here by completing the
```

```
** retrieval or because the endselect statement
```

```
** was issued.
```

```
*/
```

```
if error = 1
```

```
    print 'Error encountered after row',
```

```
        sqlca.sqlerrd(3);
```

```
    EXEC SQL ROLLBACK;
```

```
else
```

```
    print 'Successful addition and reporting';
```

```
    EXEC SQL COMMIT;
```

```
end if;
```

6. The following SELECT statement uses a string variable to substitute for the complete search condition. The variable search_condition is constructed from an interactive forms application in query mode, and during the select loop the employees who satisfy the qualification are displayed.

```
run forms in query mode;construct search_condition of employees;EXEC SQL SELECT  *    INTO :emprec    FROM employee    WHERE :search_condition;EXEC SQL BEGIN;    load emprec into a table field;EXEC SQL END;display table field for browsing;
```

7. This example illustrates session switching inside a select loop. The main program processes sales orders and calls the new_customer subroutine for every new customer.

    The main program:

```
...EXEC SQL INCLUDE SQLCA;EXEC SQL BEGIN DECLARE SECTION;/* Include output of dclgen for declaration of record order_rec */EXEC SQL INCLUDE 'decls';EXEC SQL END DECLARE SECTION;EXEC SQL CONNECT customers session 1;EXEC SQL CONNECT sales session 2;...EXEC SQL SELECT * INTO :order_rec FROM orders;EXEC SQL BEGIN;
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
    process order;EXEC SQL END;...EXEC SQL DISCONNECT;
```

    The subroutine, new_customer, which is from the select loop, contains the session switch:

```
subroutine new_customer(record order_rec)begin;EXEC SQL SET_SQL(session = 1);    EXEC SQL INSERT INTO accounts         VALUES (:order_rec);process any errors;EXEC SQL SET_SQL(session = 2);/* Reset status information before resuming select loop */sqlca.sqlcode = 0;    sqlca.sqlwarn.sqlwarn0 = ' ';end subroutine;
```
