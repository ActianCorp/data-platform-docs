---
title: "MERGE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "MERGE.htm"
canonical_id: "actian-data-platform-merge"
---

## MERGE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The MERGE statement allows data to be inserted or updated if the data matches a specified condition.

The MERGE operation updates a table using data from a source, which can be a table, view, or subselect. Rows in the target that match the source can be deleted or updated as specified. Rows that do not exist in the target can be inserted.

MERGE is a way of combining multiple operations rather than using multiple [INSERT](../SQLLanguage/INSERT.md), [UPDATE](../SQLLanguage/UPDATE.md), and [DELETE](../SQLLanguage/DELETE.md) statements.

Updating the same row of the target table multiple times in the same MERGE statement is not allowed.

This statement has the following format:

```
MERGE INTO target-table [[AS] corr-name] USING table-ref ON join-condition clause-list
```

where clause-list is:

```
WHEN MATCHED [AND condition]
```

```
             {UPDATE SET col = expr,... | DELETE}
```

```
         WHEN NOT MATCHED [AND condition]
```

```
             INSERT [(col-list)] VALUES (expr-list)
```

**target-table**

:   Specifies the name of the table into which the data is being updated or inserted. The target table must be a base table, not a view.

**corr-name**

:   Specifies a correlation name for the target table. It can be used in the join-condition, optional clause conditions, and any UPDATE clause SET value expressions.

**table-ref**

:   Specifies the source of the data to be updated or inserted. The source can be a table, view, or the result of a subselect.

**join-condition**

:   Specifies how candidate rows are formed from the target-table and the table-reference. The MERGE statement fragment:

```
INTO target-table USING table-reference ON join-condition
```

:   operates as if it were the following SELECT FROM-clause fragment:

```
FROM target-table RIGHT JOIN table-reference ON join-condition
```

:   The results of the (right outer) join are the candidate rows that are processed by the clause-list that follows.

:   The candidate row conceptually includes all columns of the table-reference plus all columns of the target-table. The target-table columns may be NULL if no target-table row joined that table-reference row; this is the usual rule for outer joins.

**clause-list**

    Specifies an ordered list of WHEN-clauses that describe if and how each candidate row is applied to the target table. Clause-list can be a series of any of the following:

    - `WHEN MATCHED [AND condition] THEN DELETE`

    - `WHEN MATCHED [AND condition] THEN UPDATE SET target-column = value,...`

    - `WHEN NOT MATCHED [AND condition] THEN INSERT VALUES (value,...)`

:   The values in an UPDATE SET clause can come from any tables listed including the target-table, including constants.

:   The values in an INSERT VALUES clause can come from the table-reference, including constants, but not the target-table.

:   A subquery is not allowed in a when-clause.

:   A WHEN MATCHED clause is executed if a target-table row joined to form the candidate row being processed.

:   A WHEN NOT MATCHED clause is executed if no target-table row joined while forming the candidate row.

:   WHEN MATCHED and WHEN NOT MATCHED clauses can be specified in any order, but the first clause applicable to a candidate row is the one executed by that row.

:   For any given result row, only the first applicable when-clause is run. If no clause matches, the candidate row is discarded, having no effect on the target table.

:   A mix of conditional and unconditional clauses can be used, but some combinations may not make sense. For example, it is legal to have more WHEN MATCHED clauses following an unconditional WHEN MATCHED clause, but those following clauses cannot have an effect, and so are ignored.

The join cannot produce more than one row per target row, or else an error is issued.

## MERGE Examples

1. Add transaction incremental balances to a master account table. If an account is not in the master table yet, it is added.

```
CREATE TABLE master_table (
```

```
    acct_no INTEGER NOT NULL,
```

```
    balance FLOAT4);
```

```
INSERT INTO master_table VALUES (1,23.9),(3,18.5);
```

```
CREATE TABLE trx (
```

```
    acct_no INTEGER NOT NULL,
```

```
    balance FLOAT4);
```

```

```

```
INSERT INTO trx values (2,23.9),(3,29.8);
```

```

```

```
MERGE INTO master_table t USING trx x ON t.acct_no = x.acct_no
```

```
WHEN MATCHED THEN UPDATE SET balance = t.balance + x.balance
```

```
WHEN NOT MATCHED THEN INSERT VALUES (x.acct_no, x.balance);
```

2. In the previous example, if there are multiple transaction table rows for a new account, multiple master rows get inserted for the same acct_no. This happens because all MATCHED / NOT MATCHED decisions are made before any updates, inserts, or deletes occur.

    If there may be multiple new-account transaction rows, a better way to do this merge is:

```
DELETE FROM trx;
```

```
INSERT INTO trx values (5,33.9),(4,2.63), (1,99.9);
```

```

```

```
MERGE INTO master_table t
```

```
USING (SELECT acct_no, sum(balance) AS balance FROM trx GROUP BY acct_no) x ON t.acct_no = x.acct_no
```

```
WHEN MATCHED THEN UPDATE SET balance = t.balance + x.balance
```

```
WHEN NOT MATCHED THEN INSERT VALUES (x.acct_no, x.balance);
```

    This MERGE processes each transaction acct_no exactly once.

3. This example is the same as the previous one, except that we now assume that a NULL balance in the transaction table means that this account is to be deleted (or never recorded, if it is a new account).

```
DELETE FROM trx;
```

```
INSERT INTO trx values (5,33.9),(4,2.63), (3,NULL);
```

```

```

```
MERGE INTO master_table t
```

```
USING (SELECT acct_no,
```

```
    MAX(CASE WHEN balance IS NULL THEN 1 ELSE 0 END) as delete_flag,
```

```
    SUM(balance) AS balance
```

```
    FROM trx GROUP BY acct_no) x
```

```
ON t.acct_no = x.acct_no
```

```
WHEN MATCHED AND delete_flag = 1 THEN DELETE
```

```
WHEN MATCHED THEN UPDATE SET balance = t.balance + x.balance
```

```
WHEN NOT MATCHED AND delete_flag <>1 THEN INSERT VALUES (x.acct_no, x.balance);
```

    The second WHEN MATCHED clause could have been written with a condition "AND delete_flag <> 1" without changing the semantics of the MERGE statement. (The statement is easier to understand without the unnecessary condition.)

4. Example:

```
MERGE INTO t USING s ON (t.i = s.i)
```

```
-- branch 1
```

```
WHEN MATCHED AND (s.op = 1) THEN UPDATE SET t.j = t.j + s.j
```

```
-- branch 2
```

```
WHEN NOT MATCHED AND (s.op = 2) THEN INSERT VALUES (s.i, 2 * s.j)
```

```
-- branch 3
```

```
WHEN MATCHED AND (s.op = 3) THEN DELETE
```

```
-- branch 4
```

```
WHEN MATCHED THEN UPDATE SET t.j = t.j - 4 * s.j
```

```
-- branch 5
```

```
WHEN NOT MATCHED THEN INSERT VALUES (s.i, 5 * s.j)
```
