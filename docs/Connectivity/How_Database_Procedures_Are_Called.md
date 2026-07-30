---
title: "How Database Procedures Are Called"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "How_Database_Procedures_Are_Called.htm"
canonical_id: "actian-data-platform-how-database-procedures-are-called"
---

## How Database Procedures Are Called

The .NET Data Provider supports calling Ingres database procedures. Input, output, and return values can be passed to and from the execution of the procedure on the warehouse.

The .NET application can call database procedures in either of two programming styles.

The first technique simply sets the IngresCommand.CommandText property to the name of the database procedure, sets the IngresCommand.CommandType to CommandType.StoredProcedure, optionally sets IngresCommand.Parameters with a collection of parameters, and executes the command.

The second technique uses the “{call …}” escape sequence syntax that is commonly used in the ODBC and JDBC APIs. The syntax supported is:

```
{ [ ? = ]  CALL [schemaname.]procedurename [( [parameters, ...])]      parameters := param  | param,   parameters
```

```
      param      := [parametername =]  [value]
```

```
      value      :=  ?  |  literal   |  SESSION.tablename
```

```
      literal    := numeric_literal  |  string_literal  |  hex_string
```

Zero or more parameters can be passed to the procedure. In its IngresParameter.Direction property, a parameter can have a ParameterDirection of Input, InputOutput, Output, or ReturnValue.

Ingres Global Temporary Table (GTT) procedure parameters are specified by providing a parameter value in the form of SESSION.tablename. In this parameter, tablename is the name of the GTT, and the keyword SESSION. identifies the parameter as a GTT parameter.

When using the CALL syntax, parameters can be named or unnamed. Named parameters specify a parametername= qualifier and can be specified in any order in the CALL syntax. Unnamed (or positional) parameters must be specified in the same order in the CALL syntax as the parameters defined in the CREATE PROCEDURE declaration. Having a mix of named and unnamed parameters in the CALL statement is not permitted.

When connecting to an Ingres 9.x or earlier DBMS Server, the use of named procedure parameters is encouraged. (Using named parameters improves performance by eliminating a query of the database catalog to assign names to the parameters based on the declared order of the procedure parameters.) When connecting to an Ingres 10 or later DBMS Server, named procedure parameters are not required.

Ingres database procedures permit the use of the transaction statements COMMIT and ROLLBACK. The use of these statements, however, is highly discouraged due to the potential for conflict in the transaction processing state between the .NET client and warehouse sides of the session. Including these statements in a procedure called by the data provider can result in the unintentional commit or rollback of work done prior to procedure execution. It is also possible that a change in transaction state during procedure execution can be misinterpreted as a transaction abort. For these reasons, applications must make sure that no transaction is active prior to executing a database procedure that contains COMMIT or ROLLBACK statements.

## Row Producing Procedures

The result-set from Ingres row-producing database procedures can be read by the .NET Data Provider like any other result set.

If the database procedure was defined as:

```
create procedure myrowproc
```

```
   result row(char(32)) as
```

```
      declare tabname char(32);
```

```
begin
```

```
   for select table_name into :tabname from iitables
```

```
   do
```

```
      return row(:tabname);
```

```
   endfor;
```

```
end;
```

The application code fragment to read the result set might be:

```
IngresCommand cmd = new IngresCommand(
```

```
   "myrowproc", conn);
```

```
cmd.CommandType = CommandType.StoredProcedure;
```

```
IDataReader reader = cmd.ExecuteReader();while (reader.Read())
```

```
{
```

```
   Console.Write(reader.GetString(0));
```

```
}Console.WriteLine();
```

```
reader.Close();
```
