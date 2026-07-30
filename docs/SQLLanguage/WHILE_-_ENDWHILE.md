---
title: "WHILE - ENDWHILE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "WHILE_-_ENDWHILE.htm"
canonical_id: "actian-data-platform-while-endwhile"
---

## WHILE - ENDWHILE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The WHILE - ENDWHILE statement repeats a series of statements while a specified condition is true.

The WHILE - ENDWHILE statement has the following format:

```
[label:]      WHILE boolean_expr DO
```

```
                            statement; {statement;}
```

```
                   ENDWHILE;
```

The WHILE - ENDWHILE statement defines a program loop. This statement can only be used inside a database procedure.

The Boolean expression (boolean_expr) must evaluate to true or false. A Boolean expression can include comparison operators (' =',' >', and so on) and these logical operators:

- AND
- OR

- NOT

The statement list can include any series of legal database procedure statements, including another WHILE statement.

As long as the condition represented by the Boolean expression remains true, the series of statements between DO and ENDWHILE is executed. The condition is tested only at the start of each loop. If values change inside the body of the loop so as to make the condition false, execution continues for the current iteration of the loop, unless an ENDLOOP statement is encountered.

The ENDLOOP statement terminates a WHILE loop. When ENDLOOP is encountered, the loop is immediately closed, and execution continues with the first statement following ENDWHILE. For example:

```
WHILE condition_1 DO        statement_list_1        IF condition_2 THEN                endloop;        ENDIF;        statement_list_2ENDWHILE;
```

In this case, if condition_2 is true, statement_list_2 is not executed in that pass through the loop, and the entire loop is closed. Execution resumes at the statement following the ENDWHILE statement.

A WHILE statement can be labeled. The label enables the ENDLOOP statement to break out of a nested series of WHILE statements to a specified level. The label precedes WHILE and is specified by a unique alphanumeric identifier followed by a colon, as in the following:

```
A: WHILE...
```

The label must be a legal object name. For more information, see [Introducing SQL](../SQLLanguage/Introducing_SQL.md). The ENDLOOP statement uses the label to indicate which level of nesting to break out of. If no label is specified after ENDLOOP, only the innermost loop currently active is closed.

The following example illustrates the use of labels in nested WHILE statements:

```
label_1:            WHILE condition_1 DO
```

```
                     statement_list_1
```

```
label_2:                   WHILE condition_2 DO
```

```
                             statement_list_2
```

```
                             IF condition_3 THEN
```

```
                                    ENDLOOP label_1;
```

```
                             ELSEIF condition_4 THEN
```

```
                                    ENDLOOP label_2;
```

```
                             ENDIF;
```

```
                             statement_list_3
```

```
                     ENDWHILE;
```

```
                     statement_list_4
```

```
             ENDWHILE;
```

In this example, there are two possible breaks out of the inner loop. If condition_3 is true, both loops are closed, and control resumes at the statement following the outer loop. If condition_3 is false but condition_4 is true, the inner loop is exited and control resumes at statement_list_4.

If an error occurs during the evaluation of a WHILE statement, the database procedure terminates and control returns to the calling application.

## WHILE - ENDWHILE Permissions

You must have CREATE_PROCEDURE privilege.

## WHILE - ENDWHILE Example

In the following WHILE - ENDWHILE statement example, this database procedure, delete_n_rows, accepts as input a base number and a number of rows. The specified rows are deleted from the table “tab,” starting from the base number. If an error occurs, the loop terminates:

```
create procedure delete_n_rows      (base integer, n integer) asdeclarelimit integer;      err integer;begin      limit = base + n;      err = 0;      while (base < limit) do            delete from tab where val = :base;            if iierrornumber > 0 then                  err = 1;                  endloop;            endif;            base = base + 1;      endwhile;      return :err;end
```
