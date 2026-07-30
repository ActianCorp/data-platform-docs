---
title: "FOR - ENDFOR"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "FOR_-_ENDFOR.htm"
canonical_id: "actian-data-platform-for-endfor"
---

## FOR - ENDFOR

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The FOR - ENDFOR statements repeat a series of statements while a specified condition is true.

The FOR - ENDFOR statement has the following format:

```
[label:] FOR select_stmt DO              statement; {statement;}              ENDFOR;
```

The FOR - ENDFOR statement define a program loop driven by the rows retrieved by the select_stmt. These statements can only be used inside a database procedure. The SELECT statement must have an INTO clause so that it can return result values into local variables in the procedure. The statement list can include any series of legal database procedure statements, including another for statement. The statement list is executed once for each row returned by the SELECT statement. After the last row from the result set of the SELECT statement is processed through the statement list, the for loop is terminated and execution continues with the first statement following the ENDFOR.

The ENDLOOP statement also terminates a FOR loop. When ENDLOOP is encountered, the loop is immediately closed, the remaining rows in the result set of the SELECT statement (if any) are discarded, and execution continues with the first statement following ENDFOR. For example,

```
        FOR select_1 DO
```

```
        statement_list_1
```

```
        IF condition_1 THEN
```

```
        ENDLOOP;
```

```
        ENDIF;
```

```
        statement_list_2;
```

```
ENDFOR;
```

In this case, statement_list_1and statement_list_2 are executed once for each row returned byselect_1. As soon as condition_1 is true, statement_list_2is not executed in that pass through the loop, select_1 is closed and the entire loop is terminated.”

A FOR statement can be labeled. The label enables the [ENDLOOP](../SQLLanguage/ENDLOOP.md) statement to break out of a nested series of FOR statements to a specified level. The label precedes FOR and is specified by a unique alphanumeric identifier followed by a colon, as in the following:

```
A: for...
```

The label must be a legal object name. The ENDLOOP statement uses the label to indicate which level of nesting to break out of. If no label is specified after ENDLOOP, only the innermost loop currently active is closed.

The following example illustrates the use of labels in nested FOR statements:

```
label_1:        FOR select_1 DO                     statement_list_1label_2:            FOR select_2 DO                            statement_list_2                            IF condition_1 THEN                                ENDLOOP label_1;                            ELSEIF condition_2 THEN                                ENDLOOP label_2;                            ENDIF;                            statement_list_3                    ENDFOR;                    statement_list_4                ENDFOR;
```

In this example, there are two possible breaks out of the inner loop. If condition_1 is true, both loops are closed, and control resumes at the statement following the outer loop. If condition_1 is false but condition_2 is true, the inner loop is exited and control resumes at statement_list_4.

If an error occurs during the evaluation of a FOR statement, the database procedure terminates and control returns to the calling application.

#### Permissions

You must have CREATE_PROCEDURE privilege.
