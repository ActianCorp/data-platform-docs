---
title: "How the Transaction Processing System Handles Interrupts"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "How_the_Transaction_Processing_System_Handles_In.htm"
canonical_id: "actian-data-platform-how-the-transaction-processing-system-handles-in"
---

## How the Transaction Processing System Handles Interrupts

When an operator interrupt occurs on the currently executing transaction, the transaction processing system responds according to the operating system used:

Windows: The transaction processing system recognizes the interrupt signal, Ctrl+C. When the user enters a Ctrl+C through the SQL CLI during transaction processing, the DBMS interrupts the current statement and rolls back any partial results of that statement. Additional use of Ctrl+C is ignored (unless an additional statement is added to the transaction). The transaction remains open until terminated by a COMMIT or ROLLBACK statement. ]

Linux: The transaction processing system recognizes the interrupt signal Ctrl+C. When the user enters a Ctrl+C through the SQL CLI during transaction processing, the DBMS interrupts the current statement and rolls back any partial results of that statement. If there is no statement currently executing, Ctrl+C has no effect on the state of the transaction. ]
