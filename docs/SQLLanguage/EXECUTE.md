---
title: "EXECUTE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "EXECUTE.htm"
canonical_id: "actian-data-platform-execute"
---

## EXECUTE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): ESQL, OpenAPI, ODBC, JDBC, .NET

The EXECUTE statement executes a previously prepared dynamic SQL statement.

The EXECUTE statement has the following format:

```
exec sql EXECUTE statement_name               [USING variable {, variable} | USING DESCRIPTOR descriptor_name];
```

**statement_name**

:   Identifies a valid object name specified using a regular or delimited identifier or a host language variable. It must identify a valid prepared statement.

:   If the statement identified bystatement_name is invalid, Actian Data Platform issues an error and terminates the EXECUTE statement. (A prepared statement is invalid if a transaction was committed or rolled back after the statement was prepared or if an error occurred while preparing the named statement.) Similarly, if the statement name refers to a cursor update or delete whose associated cursor is no longer open, Actian Data Platform issues an error. For more information, see [UPDATE](../SQLLanguage/UPDATE.md)[](../SQLLanguage/UPDATE.md)and [DELETE](../SQLLanguage/DELETE.md).

**USING variable**

:   Must be used if question marks (?) are used in the prepared statement as placeholders for parameters to be specified at runtime. If the number and data types of the expressions specified by question marks in the prepared statement are known, use the USING variable_list alternative. The number of the variables listed must correspond to the number of question marks in the prepared statement, and each must be type-compatible with its usage in the prepared statement.

**USING DESCRIPTOR descriptor_name**

:   Must be used if the number and data types of the parameters in the prepared statement are not known until runtime.

The EXECUTE statement executes the prepared statement specified by statement_name. EXECUTE can be used to execute any statement that can be prepared, except the SELECT statement.

!!! note "Note"

    To execute a prepared SELECT statement, use the [EXECUTE IMMEDIATE](../SQLLanguage/EXECUTE_IMMEDIATE.md) statement.

The following example prepares a statement containing one question mark from a buffer and executes it using a host language variable:

```
statement_buffer =
```

```
         'delete from ' + table_name +
```

```
                  ' where code = ?';
```

```
exec sql prepare del_stmt from :statement_buffer;
```

```
...
```

```

```

```
exec sql execute del_stmt using :code;
```

The value in the variable, code, replaces the '?' in the WHERE clause of the prepared DELETE statement.

If the number and data types of the parameters in the prepared statement are not known until runtime, the USING DESCRIPTOR alternative must be used. In this alternative, the descriptor_name identifies an SQLDA, a host language structure that must be allocated prior to its use. The SQLDA includes the sqlvar array. Each element of sqlvar is used to describe and point to a host language variable. The EXECUTE statement uses the values placed in the variables pointed to by the sqlvar elements to execute the prepared statement.

When the SQLDA is used for input, as it is in this case, your application program must set the sqlvar array element type, length, and data area for each portion of the prepared statement that is specified by question marks prior to executing the statement. Your application program can use one of the following methods to supply that information:

- When preparing the statement, the program can request all type and length information from the interactive user.
- Before preparing the statement, the program can scan the statement string, and build a SELECT statement out of the clauses that include parameters. The program can prepare and describe this SELECT statement to collect data type information to be used on input.

- If another application development tool is being used to build the dynamic statements (such as an 4GL frame or a VIFRED form), the data type information included in those objects can be used to build the descriptor. An example of this method is shown in the examples.

In addition, the program must also correctly set the sqld field in the SQLDA structure.

The variables used by the USING clause can be associated with indicator variables if indicator variables are permitted with the same statement in the non-dynamic case.

For example, because indicator variables are permitted in the INSERT statement VALUES clause, the following dynamically defined INSERT statement can include indicator variables (name_ind and age_ind) in the EXECUTE statement:

```
statement_buffer = 'insert into employee (name, age) values (?, ?)';exec sql prepare s1 from :statement_buffer;exec sql execute s1 using :name:name_ind, :age:age_ind;
```

However, a host structure variable cannot be used in the USING clause, even if the named statement refers to a statement that allows a host structure variable when issued non-dynamically.

This statement must be terminated according to the rules of the host language.

#### Usage in OpenAPI, ODBC, JDBC, .NET

In OpenAPI, ODBC, JDBC, and .NET, the applications must use the interface-specific mechanism for executing a prepared statement, rather than sending an EXECUTE statement.

#### Permissions

This statement is available to all users.

#### Locking

The locking behavior of the EXECUTE statement depends on the statement that is executed.

#### Related Statements

[DESCRIBE](../SQLLanguage/DESCRIBE.md)[](../SQLLanguage/DESCRIBE.md)

[PREPARE](../SQLLanguage/PREPARE.md)[](../SQLLanguage/PREPARE.md)
