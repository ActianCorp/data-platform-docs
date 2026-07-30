---
title: "SET AUTOCOMMIT ON--Commit Individual Statement"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SET_AUTOCOMMIT_ON--Commit_Individual_Statement.htm"
canonical_id: "actian-data-platform-set-autocommit-on-commit-individual-statement"
---

## SET AUTOCOMMIT ON--Commit Individual Statement

A transaction begins with the first statement after connection to the database or the first statement following a commit or rollback (including rollbacks performed by the DBMS). Subsequent statements are part of the transaction until a commit or rollback is executed. By default, an explicit commit or rollback must be issued to close a transaction.

To direct the DBMS to commit each database statement individually, use the SET AUTOCOMMIT ON statement. This statement cannot be issued in an open transaction. When autocommit is set on, a commit occurs automatically after every statement, except PREPARE and DESCRIBE. If autocommit is on and a cursor is opened, the DBMS does not issue a commit until the CLOSE cursor statement is executed, because cursors are logically a single statement. A ROLLBACK statement can be issued when a cursor is open.

To restore the default behavior (and enable multi-statement transactions), issue the SET AUTOCOMMIT OFF statement.

### How to Determine if You Are in a Transaction

To determine whether you are in a transaction, use the INQUIRE_SQL (see [INQUIRE_SQL](../SQLLanguage/INQUIRE_SQL.md)) statement.

To find out if autocommit is on or off, use the DBMSINFO function (see page [DBMSINFO Function--Return Information About the Current Session](../SQLLanguage/DBMSINFO_Function--Return_Information_About_the.md)).
