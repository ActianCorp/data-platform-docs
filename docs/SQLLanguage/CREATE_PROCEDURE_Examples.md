---
title: "CREATE PROCEDURE Examples"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_PROCEDURE_Examples.htm"
canonical_id: "actian-data-platform-create-procedure-examples"
---

## CREATE PROCEDURE Examples

1. This database procedure, mark_emp, accepts an employee ID number and a label string as input. The employee matching that ID is labeled and an indication is returned.

```
CREATE PROCEDURE mark_emp    (id INTEGER NOT NULL, label VARCHAR(100)) ASBEGIN    UPDATE employee    SET COMMENT = :label    WHERE id = :id;    IF iirowcount = 1 THEN    MESSAGE 'Employee was marked';    COMMIT;    RETURN 1;    ELSE    MESSAGE'Employee was not marked - record error';    ROLLBACK;    RETURN 0;    ENDIF;END;
```

2. This database procedure, add_n_rows, accepts as input a label, a base number, and a number of rows. It inserts the specified number of rows into the table blocks, starting from the base number. If an error occurs, the procedure terminates, and the current row number is returned.

```
CREATE PROCEDURE add_n_rows    (base INTEGER NOT NULL, n INTEGER,     label VARCHAR(100)) ASDECLARE    limit INTEGER;    err INTEGER;BEGIN    limit = base + n;    err = 0;    WHILE (base < limit) AND (err = 0) DO    INSERT INTO blocks VALUES (:label, :base);    IF iierrornumber > 0 THEN        err = 1;    ELSE        base = base + 1;    ENDIF;    ENDWHILE;    RETURN :base;END;
```

3. The following example illustrates the use of global temporary tables as procedure parameters. The database procedure, gttproc, accepts as input a surrogate table name; gtt1 is defined as a SET OF parameter to the gttproc procedure and is used in the FROM clause of a SELECT statement in the body of the procedure.

```
CREATE PROCEDURE gttproc    (gtt1 SET OF (col1 INT, col2 FLOAT NOT NULL, col3 CHAR(8))) ASBEGIN...    INSERT INTO table1    SELECT * FROM gtt1;...END;
```

4. The following example illustrates the use of parameter modes to effect the return of the customer name and zipcode column values for a given customer number to the calling procedure.

```
CREATE PROCEDURE getnamezip (IN custno INT NOT NULL, OUT custname, OUT custzip) AS BEGIN...    SELECT c_name, c_zip INTO :custname, :custzip FROM customer WHERE c_id = :custno;...END;
```

5. This database procedure, avgsal_by_dept, returns rows containing the department name, average salary in the department, and count of employees in the department. The columns of the result row are assigned the names dept_name, avg_sal and emp_count so that the procedure can also be referenced as a table procedure in a SELECT statement. Any unexpected error from the SELECT statement in the procedure terminates the loop:

```
CREATE PROCEDURE avgsal_by_dept       RESULT ROW avgsal(dept_name CHAR(15), avg_sal FLOAT, emp_count INT) AS
```

```
DECLARE       deptname CHAR(15);       avgsal   FLOAT;       empcount INT;       err      INT;BEGIN       err = 0;       FOR SELECT d.dept, avg(e.salary), count(*) INTO :deptname, :avgsal, :empcount       FROM department d, employee e        WHERE e.deptid = d.deptid       GROUP BY d.deptid do       IF iierrornumber > 0 THEN       err = 1;       endloop;       endif;       RETURN ROW(:deptname, :avgsal, :empcount);       ENDFOR;RETURN :err;END;
```
