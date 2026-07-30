---
title: "MESSAGE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "MESSAGE.htm"
canonical_id: "actian-data-platform-message"
---

## MESSAGE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): DBProc

The MESSAGE statement returns message text and a message number from a database procedure to an application program. The message statement can only be issued from a database procedure.

The MESSAGE statement has the following format:

```
MESSAGE message_text | message_number | message_number message_text
```

```
              [WITH DESTINATION =([SESSION][, ERROR_LOG] [, AUDIT_LOG]]);
```

**message_text**

:   Specifies a string literal or a non-null host string variable.

:   Limits: The maximum length is 1500 bytes.

**message_number**

:   Specifies an integer literal or a non-null host integer variable.

:   Neither message_text nor message_number can be expressions. The values for these parameters do not correspond to Actian Data Platform error codes or messages; the message statement simply returns the specified values to the receiving application. If the message_number parameter is omitted, Actian Data Platform returns a value of 0.

**WITH DESTINATION**

:   Changes the default destination of the message, which is a window at the bottom of the screen. Alternate destinations are as follows:

ERROR_LOG

:   Directs the output of the message statement to the error log.

:   The message number and text is written to errlog.log with message identifier E_QE0300.

SESSION

:   Restores the default behavior.

:   To both log and return messages to the application, specify WITH DESTINATION = (SESSION, ERROR_LOG).

To specify an action to be performed when an application receives a message from a database procedure, use the WHENEVER SQLMESSAGE statement. For more information, see [WHENEVER](../SQLLanguage/WHENEVER.md).

#### Permissions

This statement is available to all users.

#### Related Statements

[CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md)[](../SQLLanguage/CREATE_PROCEDURE.md)

[INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)
