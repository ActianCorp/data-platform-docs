---
title: "ENDLOOP"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ENDLOOP.htm"
canonical_id: "actian-data-platform-endloop"
---

## ENDLOOP

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc, TblProc

The ENDLOOP statement terminates a FOR, REPORT or WHILE loop.

The ENDLOOP statement has the following format:

```
ENDLOOP [label] [WHEN boolean_expr]
```

The ENDLOOP statement uses the label to indicate which level of nested loops to break out of. If no label is specified after ENDLOOP, the innermost loop currently active is closed.

EXIT or LEAVE are synonyms for ENDLOOP.

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
                            ENDLOOP label_1;
```

```
                      ELSE
```

```
                            ENDLOOP label_2 WHEN condition_3;
```

```
                      ENDIF;
```

```
                      statement_list_3
```

```
                      ENDLOOP WHEN condition_4;
```

```
                      statement_list_4
```

```
                      ENDLOOP label_1 WHEN condition_5;
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
                      ENDLOOP;
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

In this example, there are four possible breaks out of the inner loop. If condition_2 is true, both loops are closed, and control resumes at statement_list_9. If condition_2 is false, but condition_3 is true, the inner loop is exited and control resumes at statement_list_6. If condition_4 is true, then the inner loop is exited, or if condition_5 is true both loops are closed.

#### Permissions

This statement is available to all users.
