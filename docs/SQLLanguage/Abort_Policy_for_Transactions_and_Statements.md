---
title: "Abort Policy for Transactions and Statements"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Abort_Policy_for_Transactions_and_Statements.htm"
canonical_id: "actian-data-platform-abort-policy-for-transactions-and-statements"
---

## Abort Policy for Transactions and Statements

Transactions and statements can be terminated (rolled back) by any of the following entities:

- An application
- The DBMS

Applications can terminate transactions or statements as a result of the following conditions:

- ROLLBACK statement
- An update conflict detected at commit time

The DBMS terminates statements and transactions as a result of the following conditions:

- Error while executing a database statement
- An update conflict detected at commit time

### Conflicts Detected at Commit Time

If two separate sessions update the same row (for example, update vw set a = 4 where a = 3), both updates are successful, but only the transaction from the first session commits successfully. The second session that tries to commit the update to the **same** row sees the error: E_VW1126 Error committing transaction: updates conflict with updates in another transaction.

### How to Direct the DBMS to Roll Back an Entire Transaction or Statement

To direct the DBMS to roll back an entire transaction (or a single statement), use the SET SESSION WITH ON ERROR = ROLLBACK STATEMENT | TRANSACTION statement.
