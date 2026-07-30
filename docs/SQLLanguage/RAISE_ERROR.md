---
title: "RAISE ERROR"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "RAISE_ERROR.htm"
canonical_id: "actian-data-platform-raise-error"
---

## RAISE ERROR

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The RAISE ERROR statement notifies Actian Data Platform and the application that a database procedure has encountered an error. The RAISE ERROR statement can only be issued inside a database procedure. This statement is particularly useful when using a rule and its associated database procedure to apply an integrity constraint.

When this statement is issued, Actian Data Platform responds as if the database procedure has encountered an error. If the procedure was invoked by a rule, Actian Data Platform rolls back any changes made to the database by the original user statement and any made by the database procedure and issues an error to the application. If the RAISE ERROR statement is issued in a procedure that is executed directly by the EXECUTE PROCEDURE statement, the error is processed in the same manner as are other errors in a database procedure. (For more information, see Database Procedures.)

When executing a RAISE ERROR statement with associated errortext, both the errornumber anderrortext are returned to the application. However, only the errortext is displayed. In embedded SQL and 4GL applications, this can be changed by using INQUIRE_SQL to retrieve the error number and text (DBMSERROR and ERRORTEXT). Additionally, in embedded SQL, use the WHENEVER statement with the SQLERROR condition to inhibit the automatic display of the errortext and provide an alternate error handling mechanism.

The errornumber is, by default, returned to SQLCA variable SQLERRD(1) and to DBMSERROR, which is accessible using INQUIRE_SQL. The generic error number corresponding to a raise error is 41300. This number is returned, by default, to ERRORNO, which is accessible using INQUIRE_SQL, and to SQLCODE, another SQLCA variable. The number in SQLCODE is negative (-41300).

If you have specified that local errors are returned to ERRORNO and SQLCODE (by issuing the SQT_SQL(DBMSERROR) statement), the locations described above for the errornumber and its generic error number are reversed also. In such cases, it is not necessary to provide a negative number for the errornumber; Actian Data Platform automatically negates the number when it places the number in SQLCODE. For a complete discussion of local and generic error numbers, see [Working with Transactions and Handling Errors](../SQLLanguage/Working_with_Transactions_and_Handling_Errors.md).

To direct the output of the RAISE ERROR statement to the error log, specify WITH DESTINATION=(ERROR_LOG). The error number and text are written to the errlog.log file with message identifier E_QE0300. To direct output to the session (the default behavior), specify WITH DESTINATION=(SESSION). To both log an error and return it to an application, specify WITH DESTINATION=(SESSION, ERROR_LOG).

To direct the output of the RAISE ERROR statement directly to the audit log, specify WITH DESTINATION=(AUDIT_LOG). Any such messages are regarded as security audit events. The description indicates the source of the event (for example: MESSAGE, RAISE ERROR). The message text and error number are available in the detail information for the event.

Syntax

The Raise Error statement has the following format:

```
RAISE ERROR errornumber [errortext]              [WITH DESTINATION = ([SESSION] [, ERROR_LOG] [, AUDIT_LOG])];
```

**errornumber**

:   Can be an integer constant, a local variable, or a parameter in the invoked database procedure. If it is a local variable, it must be either a non-nullable integer or smallint type.

**errortext**

:   Is an optional text string that describes the error associated with errornumber. It can be a string constant, a local string variable, or a parameter in the invoked database procedure. Iferrortextis not specified, interactive applications such as QBF display a default error message.

:   Limits: The maximum length is 1500 bytes.

#### Permissions

You must have CREATE_PROCEDURE privilege.

#### Related Statements

[EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md)[](../SQLLanguage/EXECUTE_PROCEDURE.md)

[INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)[](../SQLLanguage/INQUIRE_SQL.md)

[MESSAGE](../SQLLanguage/MESSAGE.md)[](../SQLLanguage/MESSAGE.md)

## RAISE ERROR Example

The following example enforces a relationship (or integrity constraint) between an employee and a manager. When an employee is entered into the database, a check is performed to enforce the existence of the manager of the employee. If the manager is not found, the Raise Error statement returns a message to the user and rolls back the changes made to the database by the statement that fired the rule.

```
CREATE PROCEDURE validate_manager        (mname VARCHAR(30)) ASDECLARE       msg VARCHAR(80) NOT NULL;       check_val INTEGER;BEGIN       SELECT COUNT(*) INTO :check_val FROM manager               WHERE name = :mname;       IF check_val = 0 THEN              msg = 'Error 99999: Manager "' + :mname +                     '" not found.';RAISE ERROR 99999 :msg;ENDIF;END;CREATE RULE check_emp AFTER INSERT INTO employeeEXECUTE PROCEDURE validate_manager        (mname = new.manager);
```
