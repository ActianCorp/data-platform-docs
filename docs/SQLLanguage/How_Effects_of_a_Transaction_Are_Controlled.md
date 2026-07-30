---
title: "How Effects of a Transaction Are Controlled"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_Effects_of_a_Transaction_Are_Controlled.htm"
canonical_id: "actian-data-platform-how-effects-of-a-transaction-are-controlled"
---

## How Effects of a Transaction Are Controlled

The COMMIT and ROLLBACK statements allow control of the effects of a transaction on the database as follows:

- The COMMIT statement makes the changes permanent.
- The ROLLBACK statement undoes the changes made by the transaction.

When a COMMIT statement is issued:

- The DBMS makes all changes resulting from the transaction permanent and terminates the transaction.
- When a ROLLBACK statement is issued, the DBMS undoes any database changes made by the transaction and terminates the transaction.
