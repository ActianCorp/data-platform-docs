---
title: "PREPARE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "PREPARE.htm"
canonical_id: "actian-data-platform-prepare"
---

## PREPARE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The PREPARE statement prepares and names a dynamically constructed SQL statement for execution.

The PREPARE statement has the following format:

```
EXEC SQL PREPARE statement_name
```

```
              [INTO descriptor_name [USING NAMES]]
```

```
              FROM string_constant | string_variable;
```

The PREPARE statement encodes the dynamically constructed SQL statement string in the FROM clause and assigns it the specifiedstatement_name.

When the program subsequently executes the prepared statement, it uses the name to identify the statement, rather than the full statement string. Both the name and statement string can be represented by either a string constant or a host language variable. The maximum length of a statement name is 32 bytes. If the statement string is blank or empty, Actian Data Platform returns a runtime syntax error.

Within the statement string, replace constant expressions in WHERE clauses, INSERT VALUES clauses, and UPDATE SET clauses with question marks. When the statement executes, these question marks are replaced with specified values. Question marks cannot be used in place of table or column names or reserved words.

To illustrate, the following example prepares and executes a [DELETE](../SQLLanguage/DELETE.md) statement on a dynamically defined table:

```
statement_buffer = 'DELETE FROM ' + table_name +        ' WHERE code = ?';EXEC SQL PREPARE del_stmt FROM :statement_buffer;...EXEC SQL EXECUTE del_stmt USING :code;
```

The value in the variable, code, replaces the ? in the WHERE clause of the prepared DELETE statement.

Illustrating incorrect usage, the following example is not accurate because it includes a parameter specification in place of the table name:

```
EXEC SQL PREPARE bad_stmt	FROM 'delete from ? where code = ?';
```

Whenever an application executes a prepared statement that contains parameters specified with questions marks, the program must supply values for each question mark.

If the statement name identifies an existing prepared statement, the existing statement is destroyed and the new statement takes effect. This rule holds across the dynamic scope of the application. The statement name must not identify an existing statement name that is associated with an open cursor. The cursor must be closed before its statement name can be destroyed. Once prepared, the statement can be executed any number of times.

However, if a transaction is rolled back or committed, the prepared statement becomes invalid. If the prepared statement is to be executed only once, [EXECUTE IMMEDIATE](../SQLLanguage/EXECUTE_IMMEDIATE.md) must be used on the statement string. If the prepared statement is to be executed repeatedly, the prepare and execute sequence must be used.

The following statements cannot be prepared and executed dynamically:

- CONNECT
- CREATE PROCEDURE

- DECLARE
- DISCONNECT

- DROP PROCEDURE
- EXECUTE IMMEDIATE

- EXECUTE PROCEDURE
- EXECUTE

- GET DBEVENT
- INCLUDE

- INQUIRE_SQL
- PREPARE

- SET
- WHENEVER

In addition, the following types of statements cannot be prepared and dynamically executed:

- Dynamic SQL statements
- SQL statements (except SELECT) that include the keyword REPEATED

If the statement string is a SELECT statement, the select must not include an INTO clause. The SELECT statement string can include the different clauses of the cursor SELECT statement, such as the FOR UPDATE and ORDER BY clauses.

As with EXECUTE IMMEDIATE, the statement string must not include EXEC SQL, any host language terminators, or references to variable names. If your statement string includes embedded quotes, it is easiest to specify the string in a host language variable. If specifying a string that includes quotes as a string constant, remember that quoted characters within the statement string must follow the SQL string delimiting rules.

If your host language delimits strings with double quotes, the quoted characters within the statement string must be delimited by the SQL single quotes.

The INTO descriptor_name clause is equivalent to issuing the DESCRIBE statement after the statement is successfully prepared. For example, the following PREPARE statement:

```
EXEC SQL PREPARE prep_stmt	INTO SQLDA FROM :statement_buffer;
```

is equivalent to the following PREPARE and DESCRIBE statements:

```
EXEC SQL PREPARE prep_stmt FROM :statement_buffer;EXEC SQL DESCRIBE prep_stmt INTO SQLDA;
```

The INTO clause returns the same information as does the DESCRIBE statement. If the prepared statement is a SELECT, the descriptor contains the data types, lengths, and names of the result columns. If the statement is not a SELECT, the descriptor's sqld field contains a zero. For more information about the results of describing a statement, see [Embedded SQL](../SQLLanguage/Embedded_SQL.md) and [DESCRIBE](../SQLLanguage/DESCRIBE.md).

This statement must be terminated according to the rules of your host language.

#### Usage in OpenAPI, ODBC, JDBC, .NET

The applications should use the interface-specific mechanism, rather than sending PREPARE in the SQL.

#### Permissions

This statement is available to all users.

#### Related Statements

[DESCRIBE](../SQLLanguage/DESCRIBE.md)[](../SQLLanguage/DESCRIBE.md)

[EXECUTE](../SQLLanguage/EXECUTE.md)[](../SQLLanguage/EXECUTE.md)
