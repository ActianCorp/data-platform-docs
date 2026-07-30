---
title: "WHENEVER"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "WHENEVER.htm"
canonical_id: "actian-data-platform-whenever"
---

## WHENEVER

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL

The WHENEVER statement enables your application to handle error and exception conditions arising from embedded SQL database statements. The WHENEVER statement directs Actian Data Platform to perform a specified action when a specified condition occurs. The WHENEVER statement detects conditions by checking SQLCA variables, so an SQLCA must be included in your program before you issue the WHENEVER statement.

After a WHENEVER has been declared, it remains in effect until another WHENEVER is specified for the same condition. The WHENEVER statement has lexical (as opposed to logical) scope. For more information, see [Working with Transactions and Handling Errors](../SQLLanguage/Working_with_Transactions_and_Handling_Errors.md).

WHENEVER statements can be repeated for the same condition and can appear anywhere after the INCLUDE SQLCA statement.

The WHENEVER statement has the following format:

```
exec sql WHENEVER condition action;
```

**condition**

:   Defines the condition that triggers the action. The conditioncan be any of the following:

SQLWARNING

:   Indicates that the last embedded SQL database statement produced a warning condition. The sqlwarn0 variable of the SQLCA is set to W.

SQLERROR

:   Indicates that an error occurred as a result of the last embedded SQL database statement. The sqlcode of the SQLCA is set to a negative number.

SQLMESSAGE

:   Indicates that a message statement in a database procedure has executed. The sqlcode variable of the SQLCA is set to 700. If the database procedure is invoked by a rule, MESSAGE statements issued by the database procedure do not set sqlcode, and the sqlmessage condition does not occur.

NOT FOUND

:   Indicates that a SELECT, FETCH, UPDATE, DELETE, INSERT, CREATE INDEX, or CREATE AS...SELECT statement affected no rows. The sqlcode variable of the SQLCA is set to 100.

DBEVENT

:   Indicates that an event has been raised. The sqlcode variable of the SQLCA is set to 710. This condition occurs only for events that the application is registered to receive.

**action**

:   Specifies the action when the condition occurs. Valid actions include:

CONTINUE

:   No action is taken. The program continues with the next executable statement. If a fatal error occurs, an error message is printed and the program terminates.

STOP

:   Displays an error message and terminates. If the program is connected to a database when the condition occurs, the program disconnects from the database without committing pending updates. In response to an error or a message statement inside a database procedure, STOP terminates the database procedure. There is no way to determine which procedure statements have been executed when the database procedure is terminated in this way. The STOP action cannot be specified for the NOT FOUND condition.

GOTO label

:   Transfers control to the specified label (same as a host language go to statement). The label (or paragraph name in COBOL) must be specified using the rules of your host language. (The keyword GOTO can also be specified as GO TO). When specified as the response to an error or a message statement inside a database procedure, GOTO terminates the procedure when the action is performed. You cannot determine which database procedure statements have been executed when the procedure has been terminated in this way.

CALL procedure

:   Calls the specified procedure (in COBOL, performs the specified paragraph). The procedure must be specified according to the conventions of the host language. No arguments can be passed to the procedure. To direct the program to print any error or warning message and continues with the next statement, specify CALL SQLPRINT. (SQLPRINT is a provided procedure, not a user-written procedure.)

If the CALL action is taken in response to an error or a message statement inside a database procedure, another Actian Data Platform tool cannot be called. The called procedure cannot issue any database statements, because a database procedure continues to execute when a call action is specified. The called procedure can issue any forms statements that do not access the database. Do not issue form statements that access the database; for example, do not enter a display loop containing a SELECT statement, or issue the FORMINIT statement.

When the message statement is issued from a database procedure that executes as a result of a rule firing, Actian Data Platform displays the message text and continues program execution, even if a WHENEVER SQLMESSAGE statement is in effect. All messages are displayed and are not returned through the SQLCA.

If your program does not include an SQLCA (and therefore no WHENEVER statements), Actian Data Platform displays all errors. If your program includes an SQLCA, Actian Data Platform continues execution (and does not display errors) for all conditions for which you do not issue a WHENEVER statement.

To override the continue default and direct Actian Data Platform to display errors and messages, set II_EMBED_SET to SQLPRINT.

The program's condition is automatically checked after each embedded SQL database statement or each database procedure statement. If one of the conditions has become true, the action specified for that condition is taken. If the action is GOTO, the label must be within the scope of the statements affected by the WHENEVER statement at compile time.

An action specified for a condition affects all subsequent embedded SQL source statements until another WHENEVER is encountered for that condition.

The embedded SQL preprocessor does not generate any code for the WHENEVER statement. Therefore, in a language that does not allow empty control blocks (for example, COBOL does not allow empty IF blocks), the WHENEVER statement must not be the only statement in the block.

To avoid infinite loops, the first statement in an error handling routine must be a WHENEVER...CONTINUE that turns off error handling for the condition that caused the error. For example:

```
exec sql whenever sqlerror goto error_label;
```

```
exec sql create table worktable
```

```
        (workid integer2, workstats varchar(15));
```

```
        ...
```

```
process data;
```

```
         ...
```

```
error_label:
```

```
        exec sql whenever sqlerror continue;
```

```
        exec sql drop worktable;
```

```
        exec sql disconnect;
```

If the error handling block did not specify CONTINUE for condition SQLERROR and the DROP statement caused an error, at runtime the program loops infinitely between the DROP statement and the label, error_label.

## Embedded Usage

Host language variables cannot be used in an embedded WHENEVER statement.

## Permissions

This statement is available to all users.

## Locking

In general, the WHENEVER statement has no impact. However, if the specified action is stop, any locks held are dropped because this action terminates execution of the program.

## Related Statements

[CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md)[](../SQLLanguage/CREATE_PROCEDURE.md)

## WHENEVER Examples

The following examples describe how to enable your application to handle error and exception conditions arising from embedded SQL database statements.

1. During program development, print all errors and continue with next statement.

```
EXEC SQL WHENEVER SQLERROR CALL SQLPRINT;
```

2. During database cursor manipulation, close the cursor when no more rows are retrieved.

```
EXEC SQL OPEN cursor1;    EXEC SQL WHENEVER NOT FOUND GOTO close_cursor;    loop until whenever not found is true        EXEC SQL FETCH cursor1             INTO :var1, :var2;        print and process the results;    end loop;    close_cursor:        EXEC SQL WHENEVER NOT FOUND CONTINUE;        EXEC SQL CLOSE cursor1;
```

3. Stop program upon detecting an error or warning condition.

```
EXEC SQL WHENEVER SQLERROR STOP;    EXEC SQL WHENEVER SQLWARNING STOP;
```

4. Reset WHENEVER actions to default within an error handling block.

```
error_handle:        EXEC SQL WHENEVER SQLERROR CONTINUE;        EXEC SQL WHENEVER SQLWARNING CONTINUE;        EXEC SQL WHENEVER NOT FOUND CONTINUE;    ...    handle cleanup;    ...
```

5. Always confirm that the connect statement succeeded before continuing.

```
EXEC SQL WHENEVER SQLERROR STOP;    EXEC SQL CONNECT :dbname;    EXEC SQL WHENEVER SQLERROR CONTINUE;
```

6. Ignore all messages originating in a database procedure. This is useful when you want to suppress informational messages when providing a production application.

```
EXEC SQL WHENEVER SQLMESSAGE CONTINUE;    ...    EXEC SQL EXECUTE PROCEDURE proc1;
```
