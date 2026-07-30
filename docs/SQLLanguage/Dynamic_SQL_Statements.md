---
title: "Dynamic SQL Statements"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Dynamic_SQL_Statements.htm"
canonical_id: "actian-data-platform-dynamic-sql-statements"
---

## Dynamic SQL Statements

Dynamic SQL has the following statements that are used exclusively in a dynamic program:

- EXECUTE IMMEDIATE
- PREPARE and EXECUTE

- DESCRIBE

In addition, all statements that support cursors (DECLARE, OPEN, FETCH, UPDATE, DELETE) have dynamic versions to support dynamically executed SELECT statements.

This section is an overview of the four statements used in dynamic programs. Detailed discussions on using these statements to execute dynamic statements can be found in[Execute a Dynamic Non-select Statement](../SQLLanguage/Execute_a_Dynamic_Non-select_Statement.md) and [Execute a Dynamic SELECT Statement](../SQLLanguage/Execute_a_Dynamic_SELECT_Statement.md). For information about the dynamic versions of the cursor statements, see [Data Manipulation with Cursors](../SQLLanguage/Data_Manipulation_with_Cursors.md). In addition, information about the dynamic version of the EXECUTE PROCEDURE statement is found in [EXECUTE PROCEDURE](../SQLLanguage/EXECUTE_PROCEDURE.md).

### EXECUTE IMMEDIATE Statement

The EXECUTE IMMEDIATE statement executes an SQL statement specified as a string literal or using a host language variable. This statement is most useful when the program intends to execute a statement only once, or when using a select loop with a dynamic SELECT statement.

Use the EXECUTE IMMEDIATE statement to execute all SQL statements except for the following statements:

- CALL
- CLOSE

- CONNECT
- DECLARE

- DESCRIBE
- DISCONNECT

- EXECUTE PROCEDURE
- EXECUTE

- FETCH
- GET DBEVENT

- INCLUDE
- INQUIRE_SQL

- OPEN
- PREPARE

- SET_SQL
- WHENEVER

The syntax of EXECUTE IMMEDIATE is:

```
EXEC SQL EXECUTE IMMEDIATE statement_string       [INTO variable {, variable} | USING [DESCRIPTOR] descriptor_name         [EXEC SQK BEGIN;               program_code          EXEC SQL END;]];
```

The contents of the statement_string must not include the keywords EXEC SQL or a statement terminator. The optional INTO/USING clause and BEGIN/END statement block can only be used when executing a dynamic SELECT statement.

### PREPARE and EXECUTE Statements

The PREPARE statement tells the Actian Data Platform to encode the dynamically built statement and assign it the specified name. After a statement is prepared, the program can execute the statement one or more times within a transaction by issuing the EXECUTE statement and specifying the statement name. This method improves performance if your program must execute the same statement many times in a transaction. When a transaction is committed, all statements that were prepared during the transaction are discarded.

The following SQL statements cannot be prepared:

- CALL
- CLOSE

- CONNECT
- DECLARE

- DISCONNECT
- EXECUTE IMMEDIATE

- EXECUTE FETCH
- GET DBEVENT

- INCLUDE
- INQUIRE_SQL

- OPEN
- PREPARE

- SET
- SET_SQL

- WHENEVER

The syntax of the PREPARE statement is:

```
EXEC SQL PREPARE statement_name        [INTO descriptor_name|USING DESCRIPTOR descriptor_name]        FROM host_string_variable | string_literal;
```

The statement_name can be a string literal or variable. The contents of the host string variable or the string literal cannot include EXEC SQL or the statement terminator.

If the INTO clause is included in the PREPARE statement, the PREPARE statement also describes the statement string into the specified descriptor area and it is not necessary to describe the statement string separately.

The syntax of the EXECUTE statement is:

```
EXEC SQL EXECUTE statement_name        [USING host_variable {, host_variable}         | USING DESCRIPTOR descriptor_name];
```

A prepared statement can be fully specified, or some portions can be specified by question marks (?); these elements must be filled in (by the USING clause) when the statement is executed. For more information see [PREPARE](../SQLLanguage/PREPARE.md).

### DESCRIBE Statement

The DESCRIBE statement describes a prepared SQL statement into a program descriptor (SQLDA), which allows the program to interact with the dynamic statement as though it was hard coded in the program. This statement is used primarily with dynamic SELECT statements.

The syntax for the DESCRIBE statement is as follows:

```
EXEC SQL DESCRIBE statement_name INTO|USING descriptor_name;
```

For more information about the describe statement, see [DESCRIBE Statement and SQLDA](../SQLLanguage/SQLDA.md) and [Prepare and Describe SELECT Statements](../SQLLanguage/Execute_a_Dynamic_SELECT_Statement.md).
