---
title: "REPEAT - ENDREPEAT"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "REPEAT_-_ENDREPEAT.htm"
canonical_id: "actian-data-platform-repeat-endrepeat"
---

## REPEAT - ENDREPEAT

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The REPEAT-ENDREPEAT statement repeats a series of statements until a specified condition is true.

The REPEAT-ENDREPEAT statement has the following format:

```
[label:]         REPEAT
```

```
                    statement; {statement;}
```

```
                    UNTIL boolean_expr ENDREPEAT;
```

The REPEAT - ENDREPEAT statement defines a program loop. This statement can only be used inside a database procedure.

The Boolean expression (boolean_expr) must evaluate to true or false. A Boolean expression can include comparison operators (=, >, and so on) and these logical operators:

- AND
- OR

- NOT

The statement list can include any series of legal database procedure statements, including another WHILE or REPEAT statement.

The series of statements between REPEAT and UNTIL will always execute once. Then as long as the condition represented by the Boolean expression remains false, the statements will continue to be executed. The condition is tested only at the end of each loop. If values change inside the body of the loop so as to make the condition true, execution continues for the current iteration of the loop, unless an ENDLOOP statement is encountered.

The ENDLOOP statement terminates a REPEAT loop. When ENDLOOP is encountered, the loop is immediately closed, and execution continues with the first statement following ENDREPEAT. For example:

```
REPEAT         statement_list_1        IF condition_1 THEN                ENDLOOP;        ENDIF;        statement_list_2UNTIL condition_2 ENDREPEAT;
```

In this case, if condition_1is true, statement_list_2is not executed in that pass through the loop, and the entire loop is closed. Execution resumes at the statement following the ENDREPEAT statement.

A REPEAT statement can be labeled. The label enables the ENDLOOP statement to break out of a nested series of REPEAT statements to a specified level. The label precedes REPEAT and is specified by a unique alphanumeric identifier followed by a colon, as in the following:

```
A: REPEAT...
```

The label must be a legal object name. For more information, see [Introducing SQL](../SQLLanguage/Introducing_SQL.md). The ENDLOOP statement uses the label to indicate which level of nesting to break out of. If no label is specified after ENDLOOP, only the innermost loop currently active is closed.

The following example illustrates the use of labels in nested REPEAT statements:

```
label_1;            REPEAT
```

```
                     statement_list_1
```

```
label_2:                   REPEAT
```

```
                             statement_list_2
```

```
                             IF condition_1 THEN
```

```
                                    ENDLOOP label_1;
```

```
                             ELSEIF condition_2 THEN
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
                     UNTIL condition_3 ENDREPEAT;
```

```
                     statement_list_4
```

```
             UNTIL condition_4 ENDREPEAT;
```

In this example, there are two possible breaks out of the inner loop. If condition_1is true, both loops are closed, and control resumes at the statement following the outer loop. If condition_1is false but condition_2is true, the inner loop is exited and control resumes at statement_list_4.

If an error occurs during the evaluation of a REPEAT statement, the database procedure terminates and control returns to the calling application.

#### Permissions

To use [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md), you must have permission to access the tables and views specified in queries issued by the procedure. If the procedure uses database events owned by other users, you must have the required permissions (RAISE and REGISTER) on the database events. If the procedure executes database procedures owned by other users, you must have EXECUTE permission for those procedures.

If permissions are changed after the procedure is created and the creator of the procedure no longer has permissions to access the tables and views, a runtime error results when the procedure is executed.

The GRANT statement can be used to assign the [NO]CREATE_PROCEDURE privilege to specific users, groups, and roles.
