---
title: "MODIFY"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "MODIFY.htm"
canonical_id: "actian-data-platform-modify"
---

## MODIFY

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The MODIFY statement changes the properties of a table or index.

This statement has the following format:

```
MODIFY [schema.]tablename TO modify-action [WITH PASSPHRASE = encryption passphrase [NEW_PASSPHRASE = new encryption passphrase]]
```

When modify-action is COMBINE, the format is:

```
MODIFY [schema.]tablename [[UNION ut] [EXCEPT et] ...] TO COMBINE
```

When modify-action is RECONSTRUCT, the format is:

```
MODIFY [schema.]tablename TO RECONSTRUCT [WITH PARTITION=dimension | NOPARTITION]
```

**tablename**

:   Specifies the name of the table. The user must own the table or have MODIFY permission for the table.

**modify-action**

:   Specifies how the table should be modified. The modify-action can be any one of the following keywords:

COMBINE

:   Merges updates buffered in memory and performs bulk DML operations on any form of a table. It writes the data from all completed, cached, INSERT/UPDATE/DELETE statements against a table that reside in memory to disk and optimizes the table layout on disk.

:   MODIFY tablenameUNION utEXCEPT etTO COMBINE is the equivalent of deprecated command CALL VECTORWISE(COMBINE 'tablename+ut-et').

:   The user must have at least SELECT permission for the union and except tables.

:   Using COMBINE is the most efficient way to perform updates and deletes to a sizable percentage of the data in a table. However, depending on the volume of outstanding changes on a table and whether a table is indexed, COMBINE can be a lengthy operation.

:   For more information, see [MODIFY...TO COMBINE Statement](../SQLLanguage/MODIFY.md).

RECONSTRUCT

:   Rewrites all data of the table. All in-memory updates are merged to disk and empty disk space is reclaimed.

:   The RECONSTRUCT operation can repartition the table using the WITH PARTITION clause or remove partitioning using the WITH NOPARTITION clause.

:   For more information, see [MODIFY...TO RECONSTRUCT Statement](../SQLLanguage/MODIFY.md).

TRUNCATED

:   Deletes all data from a table and its indexes.

:   This statement deletes all rows and releases the file space back to the operating system. MODIFY...TO TRUNCATED takes an exclusive lock on the table so concurrent operations against the table being modified must wait until the operation is completed and the lock is released when the transaction is committed or rolled back.

:   The MODIFY...TO TRUNCATED operation fails under the following conditions:

        - If removing all rows will result in a foreign-key constraint violation

        - If a concurrent DML or truncate operation on the same table commits in the meantime

        - If a background update-propagation operation on the same table commits in the meantime

        - If the table is referenced by another table's foreign key, and a concurrent DML operation on the referencing table commits in the meantime

ENCRYPT

:   Enables or disables access to an encrypted table by supplying or retracting the passphrase for the table. Must be used with the WITH PASSPHRASE clause

**WITH PASSPHRASE = encryption passphrase [NEW_PASSPHRASE = new encryption passphrase]**

:   PASSPHRASE specifies an encryption passphrase used to access a table with one or more encrypted columns. The passphrase must match the latest one defined for the table. WITH PASSPHRASE must be used with the ENCRYPT modify action.

:   NEW_PASSPHRASE lets you change the passphrase. (The passphrase is initially defined on the CREATE TABLE statement.) It must be preceded by the WITH PASSPHRASE clause. The passphrase must be at least eight characters, can contain spaces, and must be enclosed in single quotes.

:   After the new passphrase is defined using NEW_PASSPHRASE, access to the encrypted table is disabled until an additional MODIFY … ENCRYPT WITH PASSPHRASE statement is issued, which verifies that the new passphrase was typed correctly.

:   If the second command succeeds you can then issue a COMMIT, confident that you have changed the passphrase correctly. If this series of MODIFY … ENCRYPT … NEW_PASSPHRASE and MODIFY … ENCRYPT commands fails because of a password mismatch, you can retry the second MODIFY (if you mistyped the passphrase) or ROLLBACK the passphrase change attempt to the old passphrase and try again.

## MODIFY...TO COMBINE Statement

The MODIFY...TO COMBINE statement merges updates buffered in memory and lets you perform bulk DML operations on any form of a table.

For large updates, we recommend using initially loading the data into staging tables, and then using explicit MODIFY...TO COMBINE statements.

The MODIFY...TO COMBINE command has the following format:

```
MODIFY [schema.]tablename [[UNION ut] [EXCEPT et] ...] TO COMBINE
```

This statement tells the system that all tuples from except tables (et) must be deleted from the base table, and then all tuples from union tables (ut) must be added to that table. This statement generates a new copy of the base table.

The order of union and except tables does not matter—all deletions are performed before insertions.

Usage Notes:

- In the worst case, the MODIFY...TO COMBINE statement may need to rewrite the entire table. As a result, the amount of space required to store the table roughly doubles temporarily. Take the required additional storage space into account when sizing your system.

    If the base table contains a Primary Key, the except tables must contain attributes with names that match all attributes of this Primary Key. These attributes do not need to be declared as a Primary Key in the except table; however, they need to be NOT NULL (as Primary Key enforces NOT NULL on the involved base table attributes).

    If the base table does not contain a Primary Key, the format of the except table must match exactly the format of the base table, because the entire record is used to identify the tuple to be deleted.

!!! note "Note"

    Performance of deletions using this method is significantly worse than when using a schema with a Primary Key.

- Union tables must match the columns of the base table: the names, orders and types (including NULLability) of columns should be identical. The union tables do not need to contain any primary and foreign-key constraints (see below).
- The order of parameters does not matter: all deletions are applied before all insertions.

- COMBINE can also be used to quickly delete all tuples from a given table by issuing, for example:

```
MODIFY a EXCEPT a TO COMBINE
```

    The system detects that this is, in effect, a table truncation, so performs a fast operation.

- You can replace all data in a given table with other data. For example:

```
MODIFY a EXCEPT a UNION b TO COMBINE
```

    replaces all tuples in 'a' with tuples from 'b' with a fast operation involving a table truncation and bulk load.

- MODIFY...TO COMBINE is a DDL command, and as a result, no other concurrent updates should be run. Other updates can be run but only the first transaction to commit will succeed.
- This statement can return all standard errors reported by DML operations, for example, constraint violations.

- Using the same table as the base table and the union table (for example: MODIFY a UNION a TO COMBINE) is illegal.
- The MODIFY...TO COMBINE process also applies batch (“small”) updates buffered in memory to the new copy of a table—a process known as propagation. You can enforce propagation as follows:

```
MODIFY a TO COMBINE
```

    After statement execution is completed, the memory used by the buffered updates is freed.

- The MODIFY...TO COMBINE statement lets you perform large deletes. For example:

```
CREATE TABLE deletions AS SELECT key FROM basetable WHERE orderdate < '2010-01-01';
```

```
MODIFY basetable EXCEPT deletion TO COMBINE;
```

```
DROP TABLE deletions;
```

- The constraints and indexes in the staging tables (union and except tables) are irrelevant for the merging process.

    It is possible to have a non-indexed table and combine it (both as union table and as except table) into an indexed table. Similarly, if the base table has a primary key or a foreign key, the staging tables do not have to have the same primary key defined (if the except tables contain columns matching the primary key in the base table and union tables match the column structure of the base table). If the staging tables are not used for querying, we highly recommend that they do not contain constraints (foreign or primary keys) or indexes, to improve their performance in loading data.

- The nullability of the columns in the union tables and except tables must match the base table.
- The MODIFY...TO COMBINE statement works on Actian Data Platform tables only but including temporary tables.

- Typically, MODIFY...TO COMBINE does not rewrite the entire table. For insertions, the data usually is written to the end of the table. For deletes, minmax indexes are rebuilt and empty blocks are discarded, which avoids I/O degradation caused by read queries scanning empty or partially empty blocks.

    If you want the entire table to be rewritten you can either use the MODIFY…TO RECONSTRUCT statement or set [system] full_rewrite_on_combine to true in your configuration file.

!!! note "Note"

    When using the MODIFY...TO COMBINE statement on a table with an identity column unexpected results, such as duplicate values, may occur. When records are inserted using MODIFY...TO COMBINE rather than the SQL INSERT, the values in the identify column in the Actian Data Platform table will not be synchronized with the identity values stored in the system catalogs.

### MODIFY...TO COMBINE Examples

1. Insert into table “tab” data from the staging table “tab_insertions”:

```
MODIFY tab UNION tab_insertions TO COMBINE
```

2. Replace all data in table1 with data from table2:

```
MODIFY table1 EXCEPT table1 UNION table2 TO COMBINE
```

3. Keep track of changes in the current product range by creating an intermediate change table:

```
DROP IF EXISTS product_master;
```

```
CREATE TABLE product_master (id_pm INTEGER, name_pm VARCHAR(30), intro_pm DATE);
```

```
DROP IF EXISTS product_current;
```

```
CREATE TABLE product_current (id_pc INTEGER, name_pc VARCHAR(30));
```

```
DROP IF EXISTS change_p;
```

```
CREATE TABLE change_p (id_pm INTEGER, name_pm VARCHAR(30), intro_pm DATE);
```

```
INSERT INTO product_current VALUES (1, 'Orange Juice'), (2, 'Grape Juice'),(3, 'Grapefruit Juice'),(4, 'Apple Juice'),(5, 'Cranberry Juice'),(6, 'Strawberry Juice'),(7, 'Mango Juice');
```

```
SELECT * FROM product_current;
```

```
INSERT INTO change_p SELECT pc.id_pc AS id_pm, name_pc AS name_pm,  DATE'2011-10-14' AS intro_pm
```

```
FROM product_current pc WHERE id_pc NOT IN (SELECT id_pm FROM product_master);
```

```
COMMIT;MODIFY product_master EXCEPT change_p UNION change_p TO COMBINE;
```

```
SELECT * FROM product_master;
```

```
COMMIT;INSERT INTO product_current VALUES (8, 'Gooseberry Juice');
```

```
UPDATE product_current SET name_pc = 'Carrot Juice' WHERE id_pc = 1;
```

```
COMMIT;SELECT * FROM product_current;MODIFY change_p EXCEPT change_p TO COMBINE;INSERT INTO change_p select pc.*,  CURRENT_DATE FROM product_current pc
```

```
WHERE id_pc NOT IN (SELECT id_pm FROM product_master WHERE name_pc = name_pm);
```

```
COMMIT;SELECT * FROM change_p;MODIFY product_master EXCEPT change_p UNION change_p TO COMBINE;SELECT * FROM product_master;
```

## MODIFY...TO RECONSTRUCT Statement

The MODIFY...TO RECONSTRUCT statement rewrites all data of a table and optionally repartitions a table or removes partitioning from a table.

This command has the following format:

```
MODIFY tablename TO RECONSTRUCT [WITH PARTITION=dimension | NOPARTITION]
```

where dimension is that described in [Partitioning Syntax](../SQLLanguage/CREATE_TABLE.md). For example:

```
MODIFY tablename TO RECONSTRUCT WITH PARTITION=(HASH ON column 2 PARTITIONS)
```

!!! note "Note"

    MODIFY...TO RECONSTRUCT consumes much time and disk space.

### MODIFY...TO RECONSTRUCT Examples

1. Apply updates to the sales_dimen table by rewriting the entire table:

```
MODIFY sales_dimen TO RECONSTRUCT
```

!!! note "Note"

    To conserve time and disk space, consider using MODIFY...TO COMBINE instead, which typically does not rewrite the entire table.

2. Repartition a table using the default partitioning count:

```
MODIFY sales_fact TO RECONSTRUCT WITH PARTITION=(HASH ON product_code DEFAULT PARTITIONS)
```

## MODIFY Examples

1. Update table “tab” with data from the staging table “tab_insertions”:

```
MODIFY tab UNION tab_insertions TO COMBINE;
```

2. Replace all data in table1 with data from table2:

```
MODIFY table1 UNION table2 EXCEPT table1 TO COMBINE;
```

3. Add two staging tables to a base table:

```
MODIFY base UNION stage1 UNION stage2 TO COMBINE;
```

4. Delete all rows in the sales_fact table and release the space:

```
MODIFY sales_fact TO TRUNCATED;
```

5. Modify the table to disable encryption and decryption (which prevents all table access).

```
MODIFY secrets TO ENCRYPT WITH PASSPHRASE='';
```

6. Modify the encrypted table to re-enable access.

```
MODIFY secrets TO ENCRYPT WITH PASSPHRASE='to encrypt or not encrypt, that is the question';
```

7. Modify the encrypted table’s passphrase, and immediate verify and commit the new passphrase.

```
MODIFY secrets TO ENCRYPT WITH PASSPHRASE='to encrypt or not encrypt, that is the question', NEW_PASSPHRASE='now is the passphrase of our discontent changed'; MODIFY secrets TO ENCRYPT WITH PASSPHRASE='now is the passphrase of our discontent changed'; COMMIT;
```

8. Change the distribution scheme to AUTOMATIC for the “tab” table:

```
MODIFY tab TO RECONSTRUCT WITH PARTITION=(AUTOMATIC 4 PARTITIONS);
```
