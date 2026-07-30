---
title: "Messages from Database Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Messages_from_Database_Procedures.htm"
canonical_id: "actian-data-platform-messages-from-database-procedures"
---

## Messages from Database Procedures

Database procedures use the SQL MESSAGE statement to return messages to users and applications. (The SQL MESSAGE statement is not the same as the forms MESSAGE statement.) Messages from database procedures can be trapped using the WHENEVER SQLMESSAGE statement or the SET_SQL(MESSAGEHANDLER) statement.

Messages from database procedures can return to your application before the database procedure has finished executing. For this reason, any message-handling routine must not execute any database statements in the current session. To issue database statements from a message-handling routine, switch sessions or open another session; if your message-handling routine switches sessions, it must switch back to the original session before returning from the message-handling routine.

### Message Handling Using the WHENEVER Statement

If your application does not include an SQLCA, messages from database procedures are displayed on the terminal. If your application includes an SQLCA, use the WHENEVER statement to trap and handle messages from database procedures. If your application includes an SQLCA, messages are displayed only if your application issues the WHENEVER SQLMESSAGE CALL SQLPRINT statement.

The WHENEVER statement handles all messages returned from directly executed database procedures.

Messages issued by database procedures return message text and a message number to the calling application, and set sqlcode to +700.

!!! note "Note"

    If a database procedure issues a MESSAGE statement and subsequently raises an error, the WHENEVER SQLMESSAGE does not trap the message. To trap all messages, use a message handler routine.

### Message Handling Using User-Defined Handler Routines

To define a message handler routine, use the SET_SQL MESSAGEHANDLER statement. Routines defined this way can trap all messages returned by procedures, whereas the WHENEVER statement traps only the last message.

To enable or disable a message-handling routine, your application must issue the following SET_SQL statement:

```
EXEC SQL SET_SQL(MESSAGEHANDLER = message_routine | 0)
```

To enable message handling, specify message_routine as a pointer to your message-handling routine or function. To disable message handling, specify 0.

In addition to issuing the SET_SQL statement shown above, create the message-handling routine and link it with your embedded SQL application.
