---
title: "How Transactions Work"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_Transactions_Work.htm"
canonical_id: "actian-data-platform-how-transactions-work"
---

## How Transactions Work

A transaction can be performed by the SQL user, the program, or in some instances, by the Actian Data Platform itself.

The transaction performs the following actions:

- The transaction begins with the first SQL statement following a CONNECT, COMMIT, or ROLLBACK statement.
- The transaction continues until there is an explicit COMMIT or ROLLBACK statement, or until the session terminates. (Terminating the session or disconnecting from the database issues an implicit COMMIT statement.)
