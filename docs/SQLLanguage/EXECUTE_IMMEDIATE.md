---
title: "EXECUTE IMMEDIATE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "EXECUTE_IMMEDIATE.htm"
canonical_id: "actian-data-platform-execute-immediate"
---

## EXECUTE IMMEDIATE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The EXECUTE IMMEDIATE statement executes an SQL statement specified as a string literal or in a host language variable.

The EXECUTE IMMEDIATE statement has the following format:

```
EXEC SQL EXECUTE IMMEDIATE statement_string
```

```
              [INTO variable {, variable} | USING [DESCRIPTOR] descriptor_name
```

```
              [EXEC SQL BEGIN;
```

```
                            program_code
```

```
               EXEC SQL END;]]
```

The EXECUTE IMMEDIATE statement executes a dynamically built statement string. Unlike the PREPARE and EXECUTE sequence, this statement does not name or encode the statement and cannot supply parameters.

The EXECUTE IMMEDIATE statement is equivalent to the following statements:

```
exec sql prepare statement_name       from :statement_buffer;exec sql execute statement_name;'Forget' the statement_name;
```

The EXECUTE IMMEDIATE can be used:

- If a dynamic statement needs to be executed just once in your program
- When a dynamic SELECT statement is to be executed and the result rows are to be processed with a select loop

- In DROP statements, where the name of the object to be dropped is not known at the time the program is compiled

If the statement string is to be executed repeatedly and it is not a SELECT statement, use the [PREPARE](../SQLLanguage/PREPARE.md) and [EXECUTE](../SQLLanguage/EXECUTE.md) statements instead. For more information about the alternatives available for executing dynamic statements, see [Embedded SQL](../SQLLanguage/Embedded_SQL.md).

The EXECUTE IMMEDIATE statement must be terminated according to the rules of the host language. If the statement string is blank or empty, Actian Data Platform returns a runtime syntax error.

The following SQL statements cannot be executed using EXECUTE IMMEDIATE:

- CLOSE
- CONNECT

- DECLARE
- DISCONNECT

- FETCH
- GET DBEVENT

- HELP
- INCLUDE

- INQUIRE_SQL
- OPEN

- SET_SQL
- WHENEVER

- Other dynamic SQL statements

The statement string must not include EXEC SQL, any host language terminators, or references to variable names. If your statement string includes embedded quotes, it is easiest to specify the string in a host language variable. If a string that includes quotes as a string constant is to be specified, remember that quoted characters within the statement string must follow the SQL string delimiting rules.

If your host language delimits strings with double quotes, the quoted characters within the statement string must be delimited by the SQL single quotes.

If the statement string is a cursor update or cursor delete, the declaration of the named cursor must appear in the same file as the EXECUTE IMMEDIATE statement executing the statement string.

The INTO or USING clause can only be used when the statement string is a SELECT statement. The INTO clause specifies variables to store the values returned by a SELECT. Use this option when the program knows the data types and lengths of the result columns before the SELECT executes. The data type of the variables must be compatible with the associated result columns.

If the program does not know the types and lengths of the result columns until runtime, specify the USING clause. The USING clause specifies an SQL Descriptor Area (SQLDA), a host language structure having, among other fields, an array of sqlvar elements. Each sqlvar element describes and points to a host language variable. When specifying the USING clause, the result column values are placed in the variables to which the sqlvar elements point.

If the USING clause is to be used, the program can first prepare and describe the SELECT statement. This process returns data type, name, and length information about the result columns to the SQLDA. Your program can use that information to allocate the necessary variables before executing the select.

If the SELECT statement returns more than one row, include the BEGIN and END statement block. This block defines a select loop. Actian Data Platform processes each row that the select returns using the program code that you specify in the select loop. The program code inside the loop must not include any other database statements, except the ENDSELECT statement. If the select returns multiple rows and a select loop is not supplied, the application receives only the first row and an error to indicate that others were returned but unseen.

#### Usage in OpenAPI, ODBC, JDBC, .NET

In OpenAPI, ODBC, JDBC, and .NET, the EXECUTE IMMEDIATE statement is equivalent to executing an SQL statement in a string variable without preparing the statement first, so the functionality is supported while the syntax is not.

#### Permissions

This statement is available to all users.

#### Locking

The locking behavior of the EXECUTE IMMEDIATE statement depends on which statement is executed.

#### Related Statements

[EXECUTE](../SQLLanguage/EXECUTE.md)[](../SQLLanguage/EXECUTE.md)

[PREPARE](../SQLLanguage/PREPARE.md)
