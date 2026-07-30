---
title: "JDBC Implementation Considerations"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "JDBC_Implementation_Considerations.htm"
canonical_id: "actian-data-platform-jdbc-implementation-considerations"
---

## JDBC Implementation Considerations

To implement Java applications in the Actian Data Platform environment, you should be aware of these programming considerations and guidelines.

## JDBC User Authentication

When the Java client is running on the same machine as the Data Access Server (DAS), and DBMS authentication is not enabled, the JDBC Driver does not require a user ID and password to establish a DBMS connection. The Java client process user ID is used to establish the connection when a user ID and password are not provided.

If DBMS authentication is enabled and the user password is required, then the user ID and password must be provided even if the connection is to the same machine.

If the target database specification includes a VNODE, the VNODE login information is used to access the DBMS machine. Optionally, a userID/password can be provided and is handled as described next.

When the Java client and DAS are on different machines, a user ID and password are required to establish a connection to the DBMS. If the DAS and warehouse are running in the same Actian Data Platform instance (no VNODE in target database specification), the userID/password is used to validate access to the DAS/DBMS machine.

When the DAS and warehouses are on different machines, a VNODE is required in the target database specification. The VNODE provides the connection and (optionally) login information needed to establish the DBMS connection.

The driver property vnode_usage determines how the VNODE is used to access the DBMS. The vnode_usage property also determines the context (DAS or DBMS) in which the application userID/password is used. VNODE usage without a userID/password is described above. If the target database specification does not contain a VNODE, the vnode_usage property is ignored.

When vnode_usage is set to 'connect', only global VNODE connection information is used to establish the DBMS connection. The application-provided user ID and password are used in the DBMS context to access the DBMS machine.

When vnode_usage is set to 'login', both connection and login VNODE information is used to access the DBMS machine. The application-provided user ID and password are used in the DAS context, allowing access to private and global VNODEs.

## How Transactions Are Autocommitted

Application developers must be aware that the warehouse imposes severe limits on the operations that can be performed when autocommit is enabled (the JDBC default transaction mode) and a cursor is opened. In general, only one cursor at a time can be open during autocommit, and only cursor-related operations (cursor delete, cursor update) can be performed. Violating this restriction results in an exception being thrown with the message text:

```
No MST is currently in progress, cannot declare another cursor
```

Cursors are opened by the Statement and PreparedStatement executeQuery() methods and remain open until the associated ResultSet is closed. The driver closes a cursor automatically when the end of the result set is reached, but applications must not rely on this behavior. JDBC applications can avoid many problems by calling the close() method of each JDBC object when the object is no longer needed.

### autocommit_mode Connection Property--Set Autocommit Processing Mode

The JDBC Driver provides alternative autocommit processing modes that help overcome the restriction of autocommitting transactions or handle problems that applications have with closing result sets.

The autocommit processing modes can be selected by setting the connection property autocommit_mode to one of the following values. For additional information, see [JDBC Driver Properties](../Connectivity/JDBC_Driver_Interface.md).

| Value | Mode | Description |
| --- | --- | --- |
| dbms | DBMS (default) | Autocommit processing is done by the warehouse and is subject to the restrictions mentioned above. |
| single | Single-cursor | The DAS allows only a single cursor to be open during autocommit. If a query or non-cursor operation is requested while a cursor is open, the server closes the open cursor. Any future attempts to access the cursor fails with an unknown cursor exception. This mode is useful for applications that fail to close result sets, but does not perform other queries or non-cursor related operations while the result set is being used. |
| multi | Multi-cursor | Autocommit processing is done by the warehouse when no cursors are open. The DAS disables autocommit and begins a standard transaction when a cursor is opened. Because autocommit processing is disabled, multiple cursors can be open at the same time and non-cursor operations are permitted.When a cursor is closed, and no other cursor is open, the DAS commits the standard transaction and re-enables autocommit in the DBMS. This mode overcomes the restrictions imposed by the DBMS during autocommit, but requires the application to be very careful in closing result sets. Because the DAS does not commit the transaction until all cursors are closed, a cursor left open inadvertently eventually runs into log-file full problems and transaction aborts. |

## Cursors and Result Set Characteristics

Ingres cursors and JDBC result sets both have an associated type specifying that the object is scrollable or forward-only. The JDBC Driver by default opens cursors as forward-only.

A scrollable cursor can be opened by specifying a JDBC result set type of ResultSet.TYPE_SCROLL_INSENSITIVE or ResultSet.TYPE_SCROLL_SENSITIVE when creating the associated statement. Ingres read-only (static) scrollable cursors are insensitive to changes, while updatable (keyset) scrollable cursors are sensitive to changes. Either type can be specified for both read-only and updatable cursors. If the incorrect type is used, the JDBC driver will produce a result set with the correct type and generate a JDBC warning indicating that the result set type was changed.

Ingres cursors and JDBC result sets both have an associated concurrency characteristic specifying that the object is readonly or updatable. The JDBC Driver automatically provides an updatable ResultSet when the associated cursor is updatable. The JDBC readonly/update mode characteristics are used by the Ingres Driver to control the mode of the resulting cursor.

For an updatable cursor, row updates and deletes can be performed using the updatable ResultSet interface or by using a separate JDBC Statement to issue positioned update and delete statements on the cursor. The cursor name needed to issue a positioned update or delete statement can be assigned using the Statement method setCursorName() or obtained by using the ResultSet method getCursorName().

Cursor concurrency can be specified using the FOR READONLY or FOR UPDATE clause in the SELECT statement. The JDBC Driver supports the JDBC syntax SELECT FOR UPDATE (and also SELECT FOR READONLY) and translates this to the correct Actian Data Platform syntax.

A cursor is opened as readonly if one of the following is true (listed in descending precedence):

- The SELECT statement contains the FOR READONLY clause.
- The associated statement was created using a Connection method that specified the concurrency as ResultSet.CONCUR_READ_ONLY.

- The connection is readonly (Connection.setReadOnly( true )).
- The connection property cursor_mode is set to 'readonly' (the default setting).

- The connection property cursor_mode is set to 'dbms' and the warehouse determines that the cursor cannot be updated.

A cursor is opened as updatable if one of the following is true (listed in descending precedence):

- The SELECT statement contains the FOR UPDATE clause.
- The associated statement was created using a Connection method that specified the concurrency as ResultSet.CONCUR_UPDATABLE and the warehouse determines that the cursor can be updated.

- No other readonly condition is true and the warehouse determines that the cursor can be updated.

!!! note "Note"

    The JDBC Driver does not attempt to force the cursor to be updatable even when the application requests a concurrency of ResultSet.CONCUR_UPDATABLE when creating the associated statement or the connection property cursor_mode is set to ‘update’. In these cases, the cursor will be updatable if the warehouse determines that an updatable cursor is possible, otherwise the cursor will be readonly. The JDBC specification requires "graceful degradation" with a warning rather than throwing an exception when a requested concurrency cannot be provided.

### Turn Off Bi-directional Updatable Scrollable Cursors

You can use a configuration setting to turn off bi-directional updatable scrollable cursors. All result-sets will be forward-only.

To turn off bi-directional updatable scrollable cursors

Use this command:

```
java -Dingres.jdbc.scroll.enabled=false App
```

Or use this alternative method:

1. Put the following line in a property file:

```
ingres.jdbc.scroll.enabled=false
```

2. Specify the property file on the command line:

```
java -Dingres.jdbc.property_file=file App
```

## Cursors and Select Loops

By default, the JDBC Driver uses a cursor to issue SQL select queries. Cursors permit other SQL operations, such as deletes or updates, to be performed while the cursor is open. (Operations can be restricted during autocommit, as described in [How Transactions Are Autocommitted](../Connectivity/JDBC_Implementation_Considerations.md).

Cursors also permit multiple queries to be active at the same time. These capabilities are possible because only a limited number of result rows (frequently only a single row) are returned by the warehouse for each cursor fetch request. The low ratio of driver requests to returned rows results in lower performance compared to other access methods.

The JDBC Driver uses cursor prefetch capabilities whenever possible. Updatable cursors only return a single row for each fetch request. READONLY cursors return a fixed number of rows on each fetch request. For details, see [Cursors and Result Set Characteristics](../Connectivity/JDBC_Implementation_Considerations.md). By default, the JDBC Driver obtains as many rows as fit in one communications block on each fetch request.

Depending on row size, this can greatly increase data access efficiency. The application can also specify the number of rows to be retrieved for READONLY cursors by using the setFetchSize() method.

The JDBC Driver also permits the JDBC application to use a data access method called a select loop. In a select loop request, the warehouse returns all the result rows in a single data stream to the driver. Because select loops use the connection while the result set is open, no other operation or query can be performed until the result set is closed.

The statement cancel() method can be used to interrupt a select loop data stream when a result set needs to be closed before the last row is processed. Because the warehouse does not wait for fetch requests from the driver, this access method is the most efficient available.

Select loops are enabled in the JDBC Driver by setting the driver connection property select_loop to a value of 'on.' For more information, see [JDBC Driver Properties](../Connectivity/JDBC_Driver_Interface.md).

With select loops enabled, the driver avoids using cursors for SELECT queries unless explicitly indicated by the application. An application can request a cursor be used for a query by assigning a cursor name to the statement (setCursorName() method) or by using the JDBC syntax 'SELECT FOR UPDATE ...' to request an updatable cursor.

## Batch Statement Execution

To take advantage of the batch query execution capability of the Ingres DBMS or Actian Data Platform DBMS, you can use the addBatch and executeBatch methods supported by the JDBC Driver.

Batched statements that use repeated dynamic INSERT statements (for example, through Java-based Extract Transfer and Load tools) are specially optimized to improve performance.

If you want to force individual statement execution, use the ingres.jdbc.batch.enabled system property (see [System Properties](../Connectivity/JDBC_Driver_Interface.md)) to disable batch query execution. If the DBMS does not support batch processing, the JDBC Driver detects it and automatically executes the statements individually.

We recommend not using autocommit with batch execution. If batch execution is used with autocommit, and you cancel the batch execution, it is impossible to tell which statements were committed.

You can improve performance of batch statement processing by following these guidelines:

- If you have large batches of inserts, we recommend that you use prepared statements. Using prepared INSERT statements with large batches (of more than 100) can significantly improve performance.
- If you are using prepared statements for batch, we recommend that you make your batches as large as possible. Larger batch sizes can make a significant difference with insert performance—even 2 or 3 times faster. In fact, when using prepared INSERT statements, the larger the batch, the better the performance. Batch sizes up to 100,000 have been noted to significantly improve performance.

- If you must use small batches (of less than 100), then you should avoid using prepared statements. The DBMS optimization works well only for large batches; for small batches, you can achieve better performance by batching non-prepared inserts.

Faster inserts also can be achieved if the following conditions are met:

- Inserts must be into a base table (not a view or index).
- The table must not have any rules or integrities defined on it.

- The table must not be a gateway table (for example, an IMA table or an Enterprise Access table).
- The inserts must be batched.

- The batched statements must be an execution of a prepared dynamic insert where the dynamic parameters exactly match the values being inserted.

### Batch Statement Execution Example

Here is a Java code segment that shows batched inserts using prepared statements:

```
PreparedStatement prep = conn.prepareStatement( "insert into emp( id, name ) values( ?, ? )" );
```

```

```

```

```

```
prep.setInt( 1, 1001 );
```

```

```

```
prep.setString( 2, "Adam Anderson" );
```

```

```

```
prep.addBatch();
```

```

```

```

```

```
...
```

```

```

```

```

```
prep.setInt( 1, 1099 );
```

```

```

```
prep.setInt( 2, "Barry Bradley" );
```

```

```

```
prep.addBatch();
```

```

```

```

```

```

```

```
int results[] = prep.executeBatch()
```

## Database Procedures

Database procedures are supported through the JDBC CallableStatement interface. The JDBC Driver supports the following database procedure syntax.

!!! note "Note"

    Items enclosed in brackets are optional.

| Database Procedure | Syntax |
| --- | --- |
| JDBC/ODBC CALL escape | `{[? =] CALL [schema.]name[( parameters )]}` |
| Ingres EXECUTE PROCEDURE | `EXECUTE PROCEDURE [schema.]name[( parameters )] [INTO ?]` |
| Ingres CALLPROC | `CALLPROC [schema.]name[( parameters )] [INTO ?]` |

For all of these statements, the JDBC Driver supports a combined parameter syntax supporting features of the ODBC positional parameter syntax and the Ingres named parameter syntax:

```
parameters := param | param, parameters
```

```
param := [name =] [value]
```

```
value := ? | literal | SESSION.table_name
```

```
literal := numeric_literal | string_literal | hex_string
```

### Named and Unnamed Parameters

Parameters can be named or unnamed, but mixing of named and unnamed parameters is not allowed. Dynamic parameters can also be named using CallableStatement methods introduced with JDBC 3.0. Literals can only be named using the syntax provided above. All Ingres database procedure parameters are named.

When connecting to an Ingres 9.x or earlier warehouse, the use of named procedure parameters is encouraged. (Using named parameters improves performance by eliminating a query of the database catalog to assign names to the parameters based on the declared order of the procedure parameters.) When connecting to an Ingres 10 or later warehouse, named procedure parameters are not required.

The JDBC Driver provides support for parameter default values by allowing parameter values to be omitted. This support is intended primarily for ODBC positional parameters. For Ingres named parameters, default values can be used simply by omitting the parameter entirely.

### Additional Parameter Considerations

Ingres supports the parameter attributes IN, OUT, and INOUT when creating database procedures. When invoking a database procedure, the JDBC Driver marks a parameter as IN when an input value is set using a CallableStatement.setXXX() method. Registering a parameter for output using a CallableStatement registerOutParameter() method will mark the parameter as OUT. Setting a value and registering for output will mark a parameter as INOUT. All dynamic parameters must have an input value assigned and/or be registered for output prior to executing the procedure.

Ingres database procedure parameters can also be passed by value or reference when not explicitly marked with IN, OUT, or INOUT attributes. The JDBC Driver treats parameters passed by value as IN parameters, and parameters passed by reference (BYREF) as INOUT parameters. If an input value is not provided for a parameter registered for output, the driver sends a NULL value of the output type registered for that parameter.

Ingres Global Temporary Table procedure parameters are specified by providing a parameter value in the form session.table_name. In this parameter, table_name is the name of the Global Temporary Table, and 'session.' identifies the parameter as a Global Temporary Table parameter.

### Executing Procedures

The CallableStatement methods executeQuery() and execute() can be used to execute a row-producing procedure. The methods executeUpdate() and execute() can be used for non-row-producing procedures. Ingres does not permit output parameters with procedures that return rows.

Procedure return values, output parameter values and rows returned by row-producing procedures are accessed by standard JDBC methods and interfaces. The CallableStatement getXXX() methods are used to retrieve procedure return and output parameter values. Rows returned by a procedure are accessed using the ResultSet returned by the CallableStatement getResultSet() method.

Ingres database procedures permit the use of the transaction statements COMMIT and ROLLBACK, however, the use of these statements is highly discouraged!

Using these statements in a procedure executed by the JDBC Driver can result in the unintentional commitment or rollback of work done prior to procedure execution. It is also possible that a change in transaction state during procedure execution can be interpreted as a transaction abort. For these reasons, applications must make sure that no transaction is active prior to executing a database procedure that contains COMMIT or ROLLBACK statements.

## Datetime Columns and Values

The Ingres DBMS uses the time zone and date format of the client to perform various types of processing of date values. By default, the JDBC Driver uses the Java/JDBC conventions for dates by setting the client time zone to GMT and the date format to match that specified by JDBC. When using these settings, the JDBC Driver manipulates datetime values to match the requirements of both the DBMS and JDBC.

Because the DBMS does not have the actual client time zone, the following restrictions exist:

- Ingres date literal formats are not supported. JDBC specifies the format for date, time, and timestamp literals using the following escape clause syntax:

**Literal**/**Syntax**

- These escape clauses must be used to include date, time, and timestamp literals in SQL text. Applications can use other datetime formats by using the classes java.sql.Date, java.sql.Time, java.sql.Timestamp, and java.util.date with an appropriately configured date formatter (java.text.DateFormat).
- Ingres specific date processing, such as intervals and date functions, causes problems associated with the difference between GMT and the actual client time zone and must be avoided.

The JDBC Driver allows the Ingres time zone and date format to be passed to the DBMS. For more information, see [JDBC Driver Properties](../Connectivity/JDBC_Driver_Interface.md). When these property values are provided, all Ingres date processing is supported in addition to the JDBC functionality listed above.

!!! note "Note"

    The Ingres time zone provided must correspond to the Java client default time zone. Using an arbitrary time zone results in time values that differ by the relative time zone offsets.

The JDBC Driver supports Ingres empty dates ('') by returning the JDBC datetime epoch values ('1970-01-01','00:00:00') for methods getDate(), getTime() and getTimestamp() and a zero-length string for getString(). In addition, a DataTruncation warning is created by the driver when an empty date is returned by any of these methods. An application checks for the warning by calling the getWarnings() method after calling one of the previously mentioned methods. An Ingres empty date is different than a NULL value, and cannot be detected using the wasNull() method.

A DataTruncation warning is also created for Ingres date-only values (no time component) for the same conditions described for empty dates. While an Ingres date-only value is comparable to a JDBC DATE value, Ingres date columns are described as being JDBC TIMESTAMP types and date-only values are technically a truncation of that type.

The driver can also be configured to return an alternate value for Ingres empty dates. The system property ingres.jdbc.date.empty can be set to a standard JDBC format datetime value to be returned in place of empty date values. This property can also be set to null to have empty dates treated as null values. A setting of default or empty results in the behavior described above. Input parameter values are also compared to the empty date alternate value when configured to send ingresdate values. An input parameter that matches the configured alternate empty date value results in an empty ingresdate, rather than alternate value, sent to the DBMS. Since null parameters are converted to empty ingresdate values if the system property is configured to null, the null setting should not be used if actual null values need to be inserted into the database.

Ingres interval values are not supported by the methods getDate(), getTime(), and getTimestamp(). An exception is thrown if an Ingres date column containing an interval value is accessed using these methods. Ingres interval values can be retrieved using the getString() method. Because the output of getString() for an interval value is not in a standard JDBC datetime format, the JDBC Driver creates a warning that can be checked by calling the getWarnings() method following the call to getString().

## National Character Set Columns

When using character parameters for a PreparedStatement, the data type sent by the driver is determined by the JDBC methods used to assign the parameter value, and the data types supported by the target database.

The JDBC parameter methods and resulting Ingres parameter data type for both standard and National Character Set databases are:

| Method | Standard Data Type | NCS Database Data Type |
| --- | --- | --- |
| setString() | varchar | nvarchar |
| setAsciiStream() | long varchar | long nvarchar |
| setUnicodeStream() | long varchar | long nvarchar |
| setCharacterStream() | long varchar | long nvarchar |
| setObject( char[] ) | char | nchar |
| setObject(String) | varchar | nvarchar |
| setObject(Reader) | long varchar | long nvarchar |
| setObject(obj,CHAR) | char | nchar |
| setObject(obj,VARCHAR) | varchar | nvarchar |
| setObject(obj,LONGVARCHAR) | long varchar | long nvarchar |
| setObject(char[],OTHER) | char | char |
| setObject(String,OTHER) | varchar | varchar |
| setObject(Reader,OTHER) | long varchar | long varchar |

!!! note "Note"

    The driver’s use of National Character Set parameters can be overridden using the JDBC SQL type of OTHER in the setObject() method.

## Using Data Compression

Compression is enabled on JDBC connections if not explicitly disabled.

If the server does not support compression, connection succeeds without compression. If compression is explicitly requested (connection attribute “compress=on”), then connection will fail if server does not support compression.

Compression can be explicitly disabled with connection attribute “compress=off.”

Compression occurs between the JDBC client and Data Access Server (DAS), and between the GCC client and the GCC server, so compression should be enabled on the network link as follows:

- If the DAS is local to the client and a vnode is used to reach the server then enable compression in the vnode.
- If the DAS is in the server installation then compression is on by default in JDBC.

- For pure Ingres Net clients, enable compression in the vnode.

An error is returned if compression cannot be enabled.
