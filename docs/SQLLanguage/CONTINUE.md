---
title: "CONTINUE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CONTINUE.htm"
canonical_id: "actian-data-platform-continue"
---

## CONTINUE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc, TblProc

The CONTINUE statement starts the next iteration of a FOR, REPORT, or WHILE loop.

The CONTINUE statement has the following format:

```
CONTINUE [label] [WHEN boolean_expr]
```

The CONTINUE statement uses the label to indicate which level of nested loops to start the next iteration of. If no label is specified after CONTINUE, the innermost loop currently active is closed.

The following example illustrates the use of labels in nested FOR and WHILE loops:

```
label_1:    FOR select_1 DO
```

```
                statement_list_1
```

```
label_2:        WHILE condition_1 DO
```

```
                      statement_list_2
```

```
                      IF condition_2 THEN
```

```
                         CONTINUE label_1;
```

```
                      ELSE
```

```
                         CONTINUE label_2 WHEN condition_3;
```

```
                      ENDIF;
```

```
                      statement_list_3
```

```
                      CONTINUE WHEN condition_4;
```

```
                      statement_list_4
```

```
                      CONTINUE label_1 WHEN condition_5;
```

```
                      statement_list_5
```

```
                 ENDWHILE;
```

```
                 statement_list_6
```

```
                 IF condition_6 THEN
```

```
                      statement_list_7
```

```
                      CONTINUE;
```

```
                 ENDIF;
```

```
                 statement_list_8
```

```
            ENDFOR;
```

```
            statement_list_9
```

In the inner loop, if condition_2 is true, the inner loop is closed, and the next row for select_1 is obtained. If condition_2 is false, but condition_3 is true, control resumes at the WHILE statement. If condition_4 is true, then control resumes at the WHILE statement, or if condition_5 is true the inner loop is closed and the next row for select_1 is obtained.

### Permissions

This statement is available to all users.
