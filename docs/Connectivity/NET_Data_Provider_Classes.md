---
title: ".NET Data Provider Classes"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: ".NET_Data_Provider_Classes.htm"
canonical_id: "actian-data-platform-net-data-provider-classes"
---

## .NET Data Provider Classes

The .NET Data Provider is the runtime component that provides the interface between the .NET application and Ingres or Actian Data Platform.

The .NET Data Provider namespace (Ingres.Client) and its contents follow the same pattern as the Microsoft data providers.

All public static members are safe for multithreaded operations. To reduce unnecessary overhead, instance members are not guaranteed to be thread-safe. If a thread-safe operation on the instance is needed, wrap the operation in one of .NET’s System.Threading synchronization methods to protect the state of the critical section of code.

The base class and interface definition for each class is provided in C# and VB.NET syntax as shown below. However, .NET’s language interoperability feature allows any managed language to use the .NET Data Provider.

**C#:**Public sealed class IngresParameter : System.Data.Common.DbParameter, IDataParameter, IDbDataParameter, ICloneable

**VB.NET:**NotInheritable public class IngresParameter
 Inherits System.Data.Common.DbParameter
 Implements IDataParameter, IDbDataParameter, ICloneable

For more information on data provider classes, including information on other .NET language syntax and inherited methods and properties, see the Microsoft .NET Framework Developer’s Guide and Microsoft .NET Framework Class Library documentation.

## IngresCommand Class

The IngresCommand class represents a SQL command or a database procedure that executes against an Ingres or Enterprise Access database.

Parameter placeholders in the SQL command text are represented by a question mark (?).

Database procedures can be invoked by either setting CommandText=”myproc” and CommandType=CommandType.StoredProcedure, or by using the escape sequence format and setting CommandText=”{ call myproc }” and CommandType=CommandType.Text.

The .NET Data Provider does not currently support the following features:

- Multiple active results-sets
- Batched commands consisting of multiple Ingres SQL commands in one IngresCommand object

- Support for Ingres SQL command COPY TABLE
- Support for Ingres SQL command SAVEPOINT

- IngresCommand.ExecuteReader(CommandBehavior.SchemaOnly) is supported for SELECT commands only

### IngresCommand Class Declaration

The IngresCommand class declarations are:

**C#:**public sealed class IngresCommand : System.Data.Common.DbCommand, IDbCommand, IDisposable, ICloneable

**VB.NET:**NotInheritable Public Class IngresCommand
 Inherits System.Data.Common.DbCommand
 Implements IDbCommand, IDisposable, ICloneable

### IngresCommand Class Example

```
IngresCommand cmd = new IngresCommand(
```

```
“SELECT id, name FROM employee WHERE id = ?”);
```

### IngresCommand Class Properties

The IngresCommand class properties are:

| Property | Accessor | Description |
| --- | --- | --- |
| CommandText | get set | SQL statement string to execute or procedure name to call. |
| CommandTimeout | get set | The time, in seconds, for an attempted query to time-out if the query has not yet completed. Default is 0 seconds. |
| CommandType | get set | An enumeration describing how to interpret the CommandText property. Valid values are Text, TableDirect, or StoredProcedure. |
| Connection | get set | The IngresConnection object that is used to identify the connection to execute a command. For more information, see[IngresConnection Class](../Connectivity/NET_Data_Provider_Classes.md). |
| Parameters | get | The IngresParameterCollection for the parameters associated with the SQL query or database procedure. For more information, see [IngresParameterCollection Class](../Connectivity/NET_Data_Provider_Classes.md). |
| Transaction | get set | The IngresTransaction object in which the IngresCommand executes. This transaction object must be compatible with the transaction object that is associated with the Connection, (that is, the IngresTransaction must be the object (or a copy) returned by IngresConnection.BeginTransaction). |
| UpdateRowSource | get set | Defines how results are applied to a rowset by the DbDataAdapter.Update method. (Inherited from DbDataAdapter.) |

### IngresCommand Class Public Methods

The public methods for the IngresCommand class are:

| Method | Description |
| --- | --- |
| Cancel | Cancels the execution of the SQL command or database procedure. |
| CreateParameter | Creates a new instance of IngresParameter. For more information, see [IngresParameter Class](../Connectivity/NET_Data_Provider_Classes.md). |
| Dispose | Releases allocated resources of the IngresCommand and base Component. |
| ExecuteNonQuery | Executes a command that does not return results. Returns the number of rows affected by the update, delete, or insert SQL command. |
| ExecuteReader | Executes a command and builds an IngresDataReader. For more information, see [IngresDataReader Class](../Connectivity/NET_Data_Provider_Classes.md). |
| ExecuteScalar | Executes a command and returns the first column of the first row of the result set. |
| Prepare | Prepares the SQL statement to be executed later. |
| ResetCommandTimeout | Resets the CommandTimeout property to its default value of 30 seconds. |

### IngresCommand Class Constructors

The constructors for the IngresCommand class are:

| Constructor Overloads | Description |
| --- | --- |
| IngresCommand() | Instantiates a new instance of the IngresCommand class using default property values |
| IngresCommand(string) | Instantiates a new instance of the IngresCommand class using the defined SQL command or database procedure |
| IngresCommand(string, IngresConnection) | Instantiates a new instance of the IngresCommand class using the defined SQL command or database procedure and the connection to the Ingres, Actian Data Platform, or Enterprise Access database |
| IngresCommand(string, IngresConnection, IngresTransaction) | Instantiates a new instance of the IngresCommand class using the defined SQL command or database procedure, the connection to the Ingres, Actian Data Platform, or Enterprise Access database, and the IngresTransaction object |

## Sample Program Constructed with .NET Data Provider

To construct an application using the .NET Data Provider, the developer creates a series of objects from the data provider’s classes. The following is a simple C# program employing four data provider classes.

#### .NET 2.0 Programming Model

```
using System;
```

```
using System.Configuration;
```

```
using System.Data;
```

```
using System.Data.Common;
```

```
using System.IO;
```

```
using Ingres.Client;
```

```

```

```
class App
```

```
{
```

```
static public void Main()
```

```
{
```

```
ConnectionStringSettingsCollection connectionSettings =
```

```
        ConfigurationManager.ConnectionStrings;
```

```
if (connectionSettings.Count == 0)
```

```
        throw new InvalidOperationException(
```

```
         "No connection information specified in application configuration file.");
```

```
ConnectionStringSettings connectionSetting = connectionSettings[0];
```

```

```

```
string invariantName      = connectionSetting.ProviderName;
```

```
string myConnectionString = connectionSetting.ConnectionString;
```

```

```

```
DbProviderFactory factory = DbProviderFactories.GetFactory(invariantName);
```

```

```

```
DbConnection conn =
```

```
         factory.CreateConnection();
```

```
conn.ConnectionString = myConnectionString;
```

```

```

```
conn.Open();   // open the Ingres connection
```

```

```

```
string cmdtext =
```

```
        "select table_owner, table_name, " +
```

```
        " create_date from iitables " +
```

```
        " where table_type in ('T','V') and " +
```

```
        " table_name not like 'ii%' and" +
```

```
        " table_name not like 'II%'";
```

```
DbCommand cmd = conn.CreateCommand();
```

```
cmd.CommandText = cmdtext;
```

```

```

```
//          read the data using the DataReader method
```

```
DbDataReader   datareader = cmd.ExecuteReader();
```

```

```

```
//          write header labels
```

```
Console.WriteLine(datareader.GetName(0).PadRight(18) +
```

```
datareader.GetName(1).PadRight(34) +
```

```
datareader.GetName(2).PadRight(34));
```

```
int i = 0;
```

```
while (i++ < 10  &&  datareader.Read())
```

```
// read and write out a few data rows
```

```
{     // write out the three columns to the console
```

```
        Console.WriteLine(
```

```
        datareader.GetString(0).Substring(0,16).PadRight(18) +
```

```
        datareader.GetString(1).PadRight(34) +
```

```
                datareader.GetString(2));
```

```
}
```

```
datareader.Close();
```

```

```

```
DataSet  ds  = new DataSet("my_list_of_tables");
```

```
//          read the data using the DataAdapter method
```

```
DbDataAdapter adapter = factory.CreateDataAdapter();
```

```
DbCommand adapterCmd = conn.CreateCommand();
```

```
adapterCmd.CommandText = cmdtext;
```

```
adapter.SelectCommand = adapterCmd;
```

```
adapter.Fill(ds);  // fill the dataset
```

```

```

```
//          write the dataset to an XML file
```

```
ds.WriteXml("c:/temp/temp.xml");
```

```

```

```
conn.Close();   // close the connection
```

```
}  // end Main()
```

```
}  // end class App
```

#### .NET 1.1 Programming Model

```
using System;
```

```
using System.IO;
```

```
using System.Data;
```

```
using Ingres.Client;
```

```

```

```
class App
```

```
{
```

```
static public void Main()
```

```
{
```

```
string myConnectionString =
```

```
"Host=myserver.mycompany.com;" +
```

```
"User Id=myname;PWD=mypass;" +
```

```
"Database=mydatabase";
```

```
IngresConnection conn = new IngresConnection(
```

```
myConnectionString );
```

```
conn.Open();   // open the Ingres connection
```

```

```

```
string cmdtext = "select table_owner, table_name, " +
```

```
"create_date from iitables " +
```

```
" where table_type in ('T','V') and " +
```

```
" table_name not like 'ii%' and" +
```

```
" table_name not like 'II%'";
```

```
IngresCommand cmd = new IngresCommand(cmdtext, conn);
```

```

```

```
//          read the data using the DataReader method
```

```
IngresDataReader   datareader = cmd.ExecuteReader();
```

```

```

```
//          write header labels
```

```
Console.WriteLine(datareader.GetName(0).PadRight(18) +
```

```
datareader.GetName(1).PadRight(34) +
```

```
datareader.GetName(2).PadRight(34));
```

```
int i = 0;
```

```
while (i++ < 10  &&  datareader.Read())
```

```
// read and write out a few data rows
```

```
{     // write out the three columns to the console
```

```
        Console.WriteLine(
```

```
        datareader.GetString(0).Substring(0,16).PadRight(18) +
```

```
        datareader.GetString(1).PadRight(34) +
```

```
                datareader.GetString(2));
```

```
}
```

```
datareader.Close();
```

```
DataSet  ds  = new DataSet("my_list_of_tables");
```

```
//          read the data using the DataAdapter method
```

```
IngresDataAdapter adapter = new IngresDataAdapter();
```

```
adapter.SelectCommand = new IngresCommand(cmdtext, conn);
```

```
adapter.Fill(ds);  // fill the dataset
```

```

```

```
//          write the dataset to an XML file
```

```
ds.WriteXml("c:/temp/temp.xml");
```

```

```

```
conn.Close();   // close the connection
```

```
}  // end Main()
```

```
}  // end class App
```

## IngresCommandBuilder Class

The IngresCommandBuilder class automatically generates INSERT, DELETE, and UPDATE commands into an IngresDataAdapter object for a simple single-table SELECT query. These commands can be used to reconcile DataSet changes through the IngresDataAdapter associated with the Ingres or Actian Data Platform database.

### IngresCommandBuilder Class Declaration

The IngresCommandBuilder class can be declared as follows:

**C#:** public sealed class IngresCommandBuilder : DbCommandBuilder

**VB.NET:** NotInheritable Public Class IngresCommandBuilder
 Inherits DbCommandBuilder

### IngresCommandBuilder Class Properties

The IngresCommandBuilder class properties are:

| Property | Accessor | Description |
| --- | --- | --- |
| CatalogLocation | get set | Position of the catalog name in a qualified table name. |
| CatalogSeparator | get set | The string of characters that defines the separation between a catalog name and the table name. |
| ConflictOption | get set | Controls how to compare for update conflicts. |
| DataAdapter | get set | The IngresDataAdapter object that is associated with the CommandBuilder. The IngresDataAdapter contains the InsertCommand, DeleteCommand, and UpdateCommand objects that are automatically derived from the SelectCommand. |
| QuotePrefix | get set | The string of characters that are used as the starting delimiter of a quoted table or column name in an SQL statement. |
| QuoteSuffix | get set | The string of characters that are used as the ending delimiter of a quoted table or column name in an SQL statement. |
| SchemaSeparator | get set | The string of characters that defines the separation between a table name and column name. Always a period (.) |

### IngresCommandBuilder Class Methods

The public methods available to the IngresCommandBuilder class are:

| Method | Description |
| --- | --- |
| Derive Parameters | Retrieves the parameter metadata of the database procedure specified in the IngresCommand object and populates the IngresCommand.Parameters collection. |
| GetDeleteCommand | Gets the generated IngresCommand to perform DELETE operations on the table. |
| GetInsertCommand | Gets the generated IngresCommand to perform INSERT operations on the table. |
| GetUpdateCommand | Gets the generated IngresCommand to perform UPDATE operations on the table. |
| QuoteIdentifier | Wrap quotes around an identifier. |
| RefreshSchema | Refreshes the IngresCommandBuilder's copy of the metadata of a possibly changed SELECT statement in the IngresDataAdapter.SelectCommand object. |
| UnquoteIdentifier | Removes quotes from an identifier. |

### IngresCommandBuilder Class Constructors

The IngresCommandBuilder class has the following constructors:

| Constructor Overloads | Description |
| --- | --- |
| IngresCommandBuilder () | Instantiates a new instance of the IngresCommandBuilder class using default property values |
| IngresCommandBuilder (IngresDataAdapter) | Instantiates a new instance of the IngresCommandBuilder class using the specified IngresDataAdapter |

## IngresConnection Class

The IngresConnection class represents an open connection to an Ingres database. This class requires a connection string to connect to a target server and database.

!!! warning "Important"

    **IMPORTANT!**An application must Close( ) or Dispose( ) on the Connection object to return it to the connection pool for reuse by other applications.

### IngresConnection Class Declaration

The IngresConnection class declaration method signature is:

**C#:**public sealed class IngresConnection : System.Data.Common.DbConnection, IDbConnection, IDisposable

**VB.NET:**NotInheritable Public Class IngresConnection
 Inherits System.Data.Common.DbConnection
 Implements IDbConnection, IDisposable

### IngresConnection Class Example

```
IngresConnection conn = new IngresConnection(“Host=myserver.mycompany.com;Database=mydatabase;” +“User ID=myuid;Password=mypassword;”);conn.Open( );
```

### IngresConnection Class Properties

The IngresConnection class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| ConnectionString | get set | String that specifies the target server machine and database to connect to, the credentials of the user who is connecting, and the parameters that define connection pooling and security.Default is "".Consists of keyword=value pairs, separated by semicolons. Leading and trailing blanks around the keyword or value are ignored. Case and embedded blanks in the keyword are ignored. Case and embedded blanks in the value are retained. Can only be set if connection is closed. Resetting the connection string resets the ConnectionTimeOut and Database properties.For a list of valid keywords and their descriptions, see [Connection String Keywords](../Connectivity/NET_Data_Provider_Classes.md). |
| ConnectionTimeOut | get | The time, in seconds, for an attempted connection to abort if the connection cannot be established.Default is 15 seconds. |
| Database | get | The database name specified in the ConnectionString’s Database value.Default is "". |
| DataSource | get | The name of the target server. |
| ServerVersion | get | The server version number. May include additional descriptive information about the server. This property uses an IngresDataReader. For this reason, no other IngresDataReader can be active at the time that this property is first invoked. |
| State | get | The current state of the connection: ConnectionState.Closed or ConnectionState.Open. |

### IngresConnection Class Public Methods

The public methods for the IngresConnection class are:

| Method | Description |
| --- | --- |
| BeginTransaction | Begins a local transaction. The connection must be open before this method can be called. Nested or parallel transactions are not supported. Mutually exclusive with the EnlistDistributedTransaction method. |
| ChangeDatabase | Changes the database to be used for the connection. The connection must be closed before this method can be called. |
| Close | Closes the connection (rollback pending transaction) and returns the connection to the connection pool. |
| CreateCommand | Creates an IngresCommand object. |
| Dispose | Closes the connection and releases allocated resources. |
| EnlistDistributedTransaction | Enlists in an existing distributed transaction (ITransaction). Mutually exclusive with the BeginTransaction method. |
| EnlistTransaction | Enlists in an existing distributed transaction (System.Transactions.Transaction). Mutually exclusive with the BeginTransaction method. |
| GetSchema | Returns schema metadata from the Ingres catalog for the specified collection name. Valid collection names include:•MetaDataCollections•DataSourceInformation•DataTypes•Restrictions•ReservedWords•Tables•Views•Columns•Indexes•Procedures•ProcedureParameters |
| Open | Opens a database connection or uses one from the connection pool. |

### IngresConnection Class Events

The events generated by the IngresConnection are:

| Event | Description |
| --- | --- |
| InfoMessage | Generated when the database returns a warning or informational message. |
| StateChange | Generated when the State property changes from Closed to Open or from Open to Close. For a definition of State, see [IngresConnection Class Properties](../Connectivity/NET_Data_Provider_Classes.md). |

### IngresConnection Class Constructors

The constructors for the IngresConnection class are:

| Constructor Overloads | Description |
| --- | --- |
| IngresConnection() | Instantiates a new instance of the IngresConnection class using default property values |
| IngresConnection(string) | Instantiates a new instance of the IngresConnection class using the defined connection string |

### Connection String Keywords

Keywords for the ConnectionString property of the IngresConnection class are as follows.

Connection string keywords are case-insensitive. Certain keywords have synonyms. For example, keywords Server and Address are synonyms of Host. Spaces in values are retained. Values can be delimited by double quotes.

**BlankDate**

:   Specifies how an Ingresdate blank (empty) result value is to be returned to the application:

BlankDate=null

:   Returns a null value.

BlankDate=default

:   Returns the default (9999-12-31 23:59:59).

**BlankDate=datetime**

:   Returns a .NET DateTime value with the customized BlankDate value. This option lets you specify your own "magic" DateTime value to represent an Ingres blank date. The format of datetimemust be yyyy-mm-dd hh:mm:ss [GMT], and the value must be a valid .NET DateTime and Ingresdate value.

:   If the GMT specification is included, the returned .NET DateTime value is adjusted for the local time zone and returned as a .NET DateTime with DateTimeKind.Local property. For example:

:   "BlankDate=2099-12-31 12:00:00 GMT;" returns 2099-12-31 12:00:00 GMT converted to local time.

**Note:**Be careful if the application does an INSERT or UPDATE of the Ingresdate column. If the column is to contain a blank Ingresdate value, the application must map the DBNull or .NET DateTime value back to the Ingresdate column value of blank date. Applications that specify their own BlankDate “magic” values should be consistent with a value. Failure to INSERT or UPDATE these mapped values properly can lead to an inconsistent, confusing mix of blank dates and various “magic” date values in the database.

**Character Encoding**

:   Specifies the .NET character encoding name (for example, windows-1252) used for conversions between Unicode and character data types. This keyword allows an alternate .NET character encoding to be specified as an override, or a valid .NET character encoding to be used if the data provider is unable to map the Data Access Server’s installation character set. A code page name can also be specified in “cp” format (for example, “cp1252”).

**Compress**

:   Specifies whether network communication blocks are compressed between the data provider and server:

:   true – (Default) Enables compression. Connection fails if compression is not possible with the server.

:   false – No compression.

:   The keyword “compression” is a synonym for “compress.”

**Connection Lifetime or Connect Lifetime**

:   Specifies an interval, in seconds, that defines the lifetime of the connection. An inactive connection that has existed longer than the specified interval beyond when it was first opened is removed from the connection pool and is closed.

:   This parameter will increase the number of physical connections required over the life of the system, but allows the system administrator to release connections and system resources, or balance servers regardless of other pool parameters such as Min Pool Size.

:   Default: 0 (no checking)

!!! note "Note"

    Inactive connections waiting for work for more than 60 seconds are automatically removed from the pool unless the user specifies a Min Pool Size. Removing inactive connections releases system resources to other processes in both the client and server.

**Connection Timeout or Connect Timeout**

:   Specifies the time, in seconds, to wait for an attempted connection to time out if the connection has not completed. Default is 15.

**Cursor_mode**

:   Specifies the default cursor concurrency mode, which determines the concurrency of cursors that are not explicitly assigned in the command text (for example, FOR UPDATE or FOR READONLY). Options are:

:   readonly – (Default) Provides non-updatable cursors for best performance

:   update – Provides updatable cursors

:   dbms – The warehouse assigns the cursor concurrency mode.

**Database or DB**

:   Specifies the name of the database being connected to: db.

**Date_alias**

:   Specifies the alias for the DATE data type. This property is not used directly by the data provider but is sent to the DBMS and affects the processing of query text. Options are:

:   ansidate – Sets ANSIDATE as the alias (default if SendIngresDates is not set or is set to FALSE).

:   ingresdate – Sets INGRESDATE as the alias (default if SendIngresDates is set to TRUE).

**Date_format or Date_fmt**

:   Specifies the Ingres format for date literals. It corresponds to the Ingres environment variable II_DATE_FORMAT and is assigned the same values. This option is not used directly by the data provider, but is sent to the DBMS and affects the parsing of date literals in query text.

**Dbms_user**

:   Specifies the user name to be associated with the DBMS session. This name is equivalent to the Ingres -u flag, which can require administrator privileges.

**Dbms_password**

:   Specifies the DBMS password of the user, which is equivalent to the Ingres -P flag.

**Decimal_char**

:   Specifies the character that the warehouse will use to separate fractional and non-fractional parts of a number. It corresponds to the Ingres environment variable II_DECIMAL and is assigned the same values. This option is not used directly by the data provider, but is sent to the DBMS and affects the parsing and construction of numeric literals.

:   Decimal_char=',' specifies the comma (,) character.

:   Default: period (.) as in 12.34.

**Encrypt**

:   Specifies whether encryption is enabled for the connection:

:   false – (Default) Disables encryption.

:   true – Enables encryption. Connection fails if encryption is not possible with the server.

**Encryption AES Key Size**

:   Specifies the size of the AES key in bits. When client and server have different capabilities, the largest common key size will be used. Valid values are: 128, 192, or 256.

:   Default: 128

**Encryption RSA Key Scope**

:   Defines the scope where an RSA key is used. Options are:

:   process – (Default) Generates one RSA key in a process. Key is used for all connections originating from that process.

:   connection – Generates an RSA key for each connection. Key is used only for that connection.

**Encryption RSA Key Size**

:   Specifies the size of the RSA key in bits. Valid values are: 1024, 2048, 3072, 4096.

:   Default: 1024

**Enlist**

:   Specifies whether the IngresConnection in the transaction context is automatically enlisted if the creation thread is within a transaction context as established by System.EnterpriseServices.ServicedComponent.

:   Default: true

**Group ID**

:   Specifies the group identifier that has permissions for a group of users.

**Host or Server or Address**

:   Specifies the name of the target host server machine with the Data Access Server (DAS).

:   Multiple host names can be specified as a semicolon-separated list enclosed in parentheses with optional port lists:

```
Server=(hostname1[:port[,port]];hostname2[:port[,port]])
```

:   Example connection string:

```
Server=(myserver1;myserver2);db=mydatabase;
```

:   If a port ID is attached to a host name, any additional port IDs outside the list or specified in the PORT keyword are ignored. If a host name does not have an explicit port ID in the specification, then port IDs in the list that follows the PORT keyword are distributed to the hostname. For example:

```
Host=(myservera:II6;myserverb);Port=II8,II9;Database=mydb;
```

:   is equivalent to:

```
Host=(myservera:II6;myserverb):II8,II9;Database=mydb;
```

:   is equivalent to:

```
Host=(myservera:II6;myserverb:II8;myserverb:II9);Database=mydb;
```

:   To maintain performance, the connection string should specify a hostname and port that the DAS servers typically listen to.

:   Example: Assume that four DAS servers are started and listening on symbolic ports II7, II8, II9, and II10. The following IngresConnection.ConnectionString will connect a .NET application to the Ingres database using one of the four ports:

```
Host=myserver;Port=II7,II8,II9,II10;UserID=myuserid;Pwd=mypwd;Database=mydb;
```

:   or

```
Host=myserver:II7,II8,II9,II10;UserID=myuserid;Pwd=mypwd;Database=mydb;
```

**Identifier_Delimiter or IdentifierDelimiter or ID_Delimiter or IDDelimiter**

:   Specifies the character recognized by the data provider to delimit an identifier. Options are:

:   dquote – (Default) Recognizes only double-quotes.

:   bracket – Recognizes both double-quotes and brackets. This keyword is for use with products such as Microsoft SQL Server Analysis Services (SSAS), which generate bracket-delimited identifiers in their processing of SQL table and column references.

**Max Pool Size**

:   Specifies the maximum number of connections that can be in the pool.

:   Default: 100

**Min Pool Size**

:   Specifies the minimum number of connections that can be in the pool.

:   Default: 0

**Money_format or Money_fmt**

:   Specifies the Ingres format for money literals. It corresponds to the Ingres environment variable II_MONEY_FORMAT and is assigned the same values. This option is not used directly by the data provider, but is sent to the DBMS and affects the processing of query text.

**Money_precision or Money_prec**

:   Specifies the precision of money data values. It corresponds to the Ingres environment variable II_MONEY_PREC and is assigned the same values. This option is not used directly by the data provider, but is sent to the DBMS and affects the processing of money values.

**Password or PWD**

:   Specifies the password to the database. This value may be case-sensitive depending on the target server.

**Persist Security Info**

:   Specifies whether password information from the connection string is returned in a get of the ConnectionString property:

:   false – (Default) Does not return password information.

:   true – Returns password information.

**Pool Check Interval**

:   Specifies the interval, in seconds, at which inactive connections in the pool that are waiting for work are checked to test if the session is still responsive. Non-responsive connections are closed and removed from the pool.

:   A value that is too low generates needless query traffic to the warehouse. A value that is too high delays detection of non-responsive servers. An interval of 300 seconds may be a reasonable starting value.

:   Default: 0 (no checking)

**Pool Check Timeout**

:   Specifies the time, in seconds, for an inactive connection in the pool to wait on a non-responsive server before timing out and disconnecting. This keyword has no effect if Pool Check Interval is 0.

:   Default: 5

**Pooling**

:   Enables or disables connection pooling:

:   true – (Default) Enables connection pooling.

:   false – Disables connection pooling.

**Port**

:   Specifies the port number 27839.

**PrefetchBlocks**

:   Specifies the number of data blocks to be prefetched. By default, the rows that fit in one communication data block are prefetched. When this property is set, the prefetch block count is multiplied by the default prefetch row count to determine the number of rows to be prefetched. Depending on the row size and unused space in the rows, the number of blocks retrieved may be different.

:   Default: 1 (no override to default algorithm)

**Role ID**

:   Specifies the role identifier that has associated privileges for the role.

**Role Password or Role PWD**

:   Specifies the role password associated with the Role ID.

**SendIngresDates**

:   Specifies whether .NET DateTime parameter data is sent as INGRESDATE data type rather than as ANSI date and time data type. Options are:

:   false – Sends as ANSI date and time type. (Default if date_alias is not set or is set to ANSIDATE.)

:   true – Sends as INGRESDATE type. (Default if date_alias is set to INGRESDATE.)

:   For more information, see [SendIngresDates Connection Keyword](../Connectivity/NET_Data_Provider_Classes.md).

**Timezone or TZ**

:   Specifies the time zone associated with the client's location. Corresponds to the Ingres environment variable II_TIMEZONE_NAME and is assigned the same values. This information is not used directly by the data provider, but is sent to the DBMS and affects the processing of dates.

**User ID or UID**

:   Specifies the name of the authorized user connecting to the warehouse. This value may be case-sensitive depending on the target server.

**Vnode_usage**

:   Allows the .NET application to control the portions of the vnode information that are used to establish the connection to the remote warehouse through the Data Access Server. Options are:

:   connect – (Default) Uses only the vnode connection information.

:   login – Uses both the vnode connection and login information.

:   For more information, see [User ID Options for the Data Provider](../Connectivity/NET_Data_Provider_Classes.md).

### User ID Options for the Data Provider

When the .NET client application is running on the same machine as the Data Access Server (DAS), and DBMS authentication is not enabled, the .NET Data Provider does not require a user ID and password to establish a DBMS connection. The .NET client process user ID is used to establish the connection when a user ID and password are not provided.

If DBMS authentication is enabled and the user password is required, then the user ID and password must be provided even if the connection is to the same machine.

If the target database name specification includes a VNODE name specification, the VNODE login information is used to access the DBMS machine. Optionally, a user ID and password can be provided and is handled as described next.

When the DAS and warehouses are on different machines, a VNODE name is required in the target database specification of the form vnodename::dbname. The VNODE provides the connection and (optionally) login information needed to establish the DBMS connection.

The connection string keyword Vnode_usage determines how the VNODE is used to access the DBMS. Vnode_usage also determines the context (DAS or DBMS) in which the application user ID/password is used. If the target database specification does not contain a VNODE name, the Vnode_usage specification is ignored.

When Vnode_usage is set to CONNECT, only global VNODE connection information is used to establish the DBMS connection. The application-provided user ID and password are used in the DBMS context to access the DBMS machine.

When Vnode_usage is set to LOGIN, both connection and login VNODE information is used to access the DBMS machine. The application-provided User ID and Password are used in the DAS context, allowing access to private and global VNODEs on the DAS server.

The .NET Data Provider supports IPv6 addressing. IPv6 addresses should be enclosed in brackets [ ] because of the different address format—for example: [fe80::127:dff:fe7c:fecc].

If a hostname is associated with multiple IP addresses, the data provider sequentially tries to connect to each IP address in the AddressList returned by System.Net.Dns.GetHostEntry until it achieves a successful socket connection or until it reaches the end of the list. If the connection to the first address is down, the data provider attempts a connection to the next entry in the AddressList. Although performance will suffer as each Exception from a failed connection is caught, this re-attempt allows a secondary IP (backup) for a connection to a server.

### SendIngresDates Connection Keyword

The .NET Data Provider sends .NET DateTime parameter data to the Data Access Server (DAS) and the DBMS. The format of this DateTime parameter data sent by the provider depends on the level of support of the ANSI datetime data types.

In releases prior to Ingres 9.1 (also known as 2006 Release 2), the data is sent as a data type of INGRESDATE with a GMT timezone. Beginning with Ingres 9.1, the datetime data is sent with a data type of ANSI TIMESTAMP_WITH_TIMEZONE (TS_W_TZ) with a local datetime, local timezone, and microsecond data. This flexibility and adaptability to the capabilities of the DBMS is useful, but can have a side-effect when upgrading to new releases of Ingres.

When upgrading from a release of Ingres prior to 9.1, the behavior of the program can change under certain circumstances when datetime formerly sent as an INGRESDATE type is now sent as a TS_W_TZ type. Typically, no problem occurs because the TS_W_TZ data is converted as needed and any components of the data such as microseconds are discarded, depending on the target data type. In some cases, however, the change in data type can change the semantics of processing enough to become an issue.

For example, if datetime parameter data is sent to a query containing the the IFNULL( ? , ' ') function, the function may succeed or fail depending on the data type sent by the provider. If the provider sends the data as INGRESDATE type, then IFNULL(<ingresdate>, ' ' ) will execute correctly (returning the date or the empty string date if the parameter is null). Upon upgrade to Ingres 9.1 and later, the datetime parameter data is sent by the drivers as TIMESTAMP_WITH_TIMEZONE data type, and the IFNULL(<ts_w_tz>, ' ' ) will fail because the empty string date is not permitted in combination with ANSI TIMESTAMP_WITH_TIMEZONE.

The work-around for this problem is to wrap the INGRESDATE function around the parameter: IFNULL( INGRESDATE(?) , ' '). Changing every source reference in an application, however, may not be feasible.

Using the SendIngresDates=TRUE connection keyword tells the .NET Data Provider to send the datetime parameter data as INGRESDATE type and value (as if the server was pre-Ingres 9.1) to force the old behavior.

### IngresConnection.GetSchema Method

The IngresConnection.GetSchema method is used to return information on the schema of a database. The collection of metadata returned describes the tables, columns, and so on, that are defined in the database. The schema information is returned in the form of a .NET Framework DataTable.

GetSchema takes zero or more parameters. The first parameter is the collection name (for example: “Tables” or “Columns”). Optional restriction parameters in a String array ("restrictionValues") allow the returned metadata to be filtered to only those rows for a specified value, for example, only those columns for a specific table name. If GetSchema is invoked with no parameters or with a collection name of “MetaDataCollections” then a DataTable is returned that lists the collection names. Each row in the DataTable lists the collection name and number of restrictions supported for that collection.

The following collections are supported:

MetaDataCollection

| Column Name | Data Type | Description |
| --- | --- | --- |
| CollectionName | String | Collection name support by the data provider |
| NumberOfRestrictions | INT32 | Number of restrictions that can be specified for the collection by GetSchema |
| NumberOfIdentifierParts | INT32 | Number of parts in the database object name. |

DataSourceInformation

| Column Name | Data Type | Description |
| --- | --- | --- |
| CompositeIdentifierSeparatorPattern | String | Regular expression for matching composite name separator character |
| DataSourceProductName | String | Product name accessed by the data provider |
| DataSourceProductVersion | String | Product version accessed by the data provider |
| DataSourceProductVersionNormalized | String | Product version accessed by the data provider in a format that will be consistent for all versions of the data provider |
| GroupByBehavior | GroupByBehavior | The relationship between GROUP BY columns and non-aggregated columns of the SELECT statement |
| IdentifierPattern | String | Regular expression for matching an identifier |
| IdentifierCase | IdentifierCase | Indicates if nonquoted identifiers are case-sensitive |
| OrderByColumnsInSelect | Boolean | Specifies whether ORDER BY columns must be specified in the SELECT list. |
| ParameterMarkerFormat | String | Format string for matching a parameter marker |
| ParameterMarkerPattern | String | Regular expression for matching a parameter marker |
| ParameterNameMaxLength | INT32 | Maximum character length of a named parameter |
| ParameterNamePattern | String | Regular expression for matching a named parameter |
| QuotedIdentifierPattern | String | Regular expression for matching a quoted identifier |
| QuotedIdentifierCase | String | Indicats if quoted identifiers are case sensitive |
| StatementSeparatorPattern | String | Regular expression for matching a statement separator |
| StringLiteralPattern | String | Regular expression for matching a quoted string literal in an SQL statement |
| SupportedJoinOperators | SupportedJoinOperators | Specifies what SQL JOIN operators are supported |

DataTypes

| ColumnName | DataType | Description |
| --- | --- | --- |
| TypeName | String | Ingres data type name |
| ProviderDbType | INT32 | IngresType value to be used for a parameter data type |
| ColumnSize | INT64 | Length of the data type, if non-numeric |
| CreateFormat | String | Format string for creation of a column’s data type in a CREATE TABLE |
| CreateParameters | String | Length, precision, and/or scale parameters associated with the data type’s CreateFormat |
| DataType | String | Name of the .NET Framework data type associated with this data type |
| IsAutoIncrementable | Boolean | Indicates whether this data type may be auto-incrementing |
| IsBestMatch | Boolean | Indicates whether this data type is the best match for the .NET Framework specified by the DataType column |
| IsCaseSensitive | Boolean | Indicates whether the data type is a character data type and is case-sensitive |
| IsFixedLength | Boolean | Indicates whether the data type is of fixed length |
| IsFixedPrecisionScale | Boolean | Indicates whether the data type has a fixed precision and scale |
| IsNullable | Boolean | Indicates whether the data type is nullable |
| IsSearchable | Boolean | Indicates whether the data type can be used in a WHERE predicate with any operator other than LIKE |
| IsSearchableWithLike | Boolean | Indicates whether the data type can be used in a WHERE predicate with the LIKE operator |
| IsUnsigned | Boolean | Indicates whether the data type is unsigned |
| MaximumScale | INT16 | If the data type is numeric, the maximum number of digits to the right of the decimal point |
| MinimumScale | INT16 | If the data type is numeric, the minimum number of digits to the right of the decimal point |
| IsConcurrencyType | Boolean | Indicates whether the data type is updated when the row is changed and the column value is different. DBNull.Value if this capability is not supported. |
| IsLiteralSupported | Boolean | Indicates whether the data type can be expressed in a literal |
| LiteralPrefix | String | The prefix for a literal of this type |
| LiteralSuffix | String | The suffix for a literal of this type |

Restrictions

| ColumnName | DataType | Description |
| --- | --- | --- |
| CollectionName | String | Collection name |
| RestrictionName | String | Restriction name |
| RestrictionDefault | String | Ignored |
| RestrictionNumber | INT32 | The location (numbered from 1) within the restrictions collection where this restriction is associated with |

ReservedWords

| ColumnName | DataType | Description |
| --- | --- | --- |
| ReservedWord | String | Ingres specific reserved words |

Tables

| ColumnName | DataType | Description |
| --- | --- | --- |
| TABLE_CATALOG1 | String | Always DBNull.Value |
| TABLE_SCHEMA2 | String | Schema name (table owner name) |
| TABLE_NAME3 | String | Table name of user table |
| TABLE_TYPE | String | Always "TABLE" |

Views

| ColumnName | DataType | Description |
| --- | --- | --- |
| TABLE_CATALOG1 | String | Always DBNull.Value |
| TABLE_SCHEMA 2 | String | Schema name (view owner name) |
| TABLE_NAME3 | String | View name of user view |
| TABLE_TYPE | String | Always "VIEW" |

Columns

| ColumnName | DataType | Description |
| --- | --- | --- |
| TABLE_CATALOG1 | String | Always DBNull.Value |
| TABLE_SCHEMA2 | String | Schema name (table/view owner name) |
| TABLE_NAME3 | String | Table/view name of user table |
| COLUMN_NAME4 | String | Column name |
| ORDINAL_POSITION | Int16 | Position of the column within the set of the table’s columns, numbered from 1 |
| COLUMN_DEFAULT | String | Column’s default value |
| IS_NULLABLE | Boolean | Indicates whether the column is nullable |
| DATA_TYPE | String | Ingres data type name |
| CHARACTER_MAXIMUM  _LENGTH | INT32 | Maximum length in characters, if character or binary data type |
| CHARACTER_OCTET  _LENGTH | INT32 | Maximum length in bytes, if character or binary data type |
| NUMERIC_PRECISION | Byte | Precision length if an integer, float, real, decimal, datetime, or interval data type |
| NUMERIC_PRECISION  _RADIX | INT16 | Radix of the Precision |
| NUMERIC_SCALE | INT32 | Scale length |
| DATETIME_PRECISION | INT16 | Precision of ingresdate and ANSI Timestamp data types |

Indexes

| ColumnName | DataType | Description |
| --- | --- | --- |
| TABLE_CATALOG1 | String | Always DBNull.Value |
| TABLE_SCHEMA2 | String | Base table schema name  (table owner name) |
| TABLE_NAME3 | String | Base table name |
| NON_UNIQUE | INT16 | 1 if index is unique, else 0 |
| INDEX_QUALIFIER | String | Index owner name |
| INDEX_NAME4 | String | Index name |
| TYPE | INT16 | Index type (always ODBC index type SQL_INDEX_OTHER) |
| ORDINAL_POSITION | INT16 | Position of the column within the set of the index’s columns, numbered from 1 |
| COLUMN_NAME | String | Column name |
| ASC_OR_DSC | String | Collation. “A” for ascending, “D” for descending |

Procedures

| ColumnName | DataType | Description |
| --- | --- | --- |
| PROCEDURE_CATALOG1 | String | Always DBNull.Value |
| PROCEDURE_SCHEMA2 | String | Procedure schema (procedure owner name) |
| PROCEDURE_NAME3 | String | Procedure name |

ProcedureParameters

| ColumnName | DataType | Description |
| --- | --- | --- |
| PROCEDURE_CATALOG1 | String | Always DBNull.Value |
| PROCEDURE _SCHEMA2 | String | Schema name  (procedure owner name) |
| PROCEDURE _NAME3 | String | Procedure name |
| COLUMN_NAME4 | String | Procedure parameter name |
| ORDINAL_POSITION | INT16 | Position of the column within the set of the procedure’s parameters, numbered from 1 |
| COLUMN_DEFAULT | String | Parameter’s default value |
| IS_NULLABLE | Boolean | Indicates whether the parameter is nullable |
| DATA_TYPE | String | Ingres data type name |
| CHARACTER_MAXIMUM  _LENGTH | INT32 | Maximum length in characters, if character or binary data type |
| CHARACTER_OCTET  _LENGTH | INT32 | Maximum length in bytes, if character or binary data type |
| NUMERIC_PRECISION | Byte | Precision length if an integer, float, real, decimal, datetime, or interval data type |
| NUMERIC_PRECISION  _RADIX | INT16 | Radix of the precision |
| NUMERIC_SCALE | INT32 | Scale length |
| DATETIME_PRECISION | INT16 | Precision of ingresdate and ANSI Timestamp data types |
| INGRESTYPE | IngresType | .NET Data Provider data type |

1. Can be used as a restriction in the first entry of restrictionValues array.
2. Can be used as a restriction in the second entry of restrictionValues array.

3. Can be used as a restriction in the third entry of restrictionValues array.
4. Can be used as a restriction in the fourth entry of restrictionValues array.

### Enlistment in Distributed Transactions

The .NET Data Provider supports enlistment in distributed transactions through the MS Distributed Transaction Coordinator (MSDTC) and the XA two-phase commit protocol.

Developers should be aware of MSDTC performance with distributed transactions and the lag time in communicating with all voters of the two-phase commit protocol. For performance reasons, distributed transactions should be used carefully. While the enlistment in a distributed transaction is not slow, it is not as fast as an enlistment in a local transaction.

To use the EnlistTransaction and EnlistDistributedTransaction methods in the .NET Data Provider, the administrator of the Windows machine must enable XA transactions through Component Services.

### System.Transactions Programming Models

The .NET Framework System.Transactions namespace offers two programming models to the .NET application programmer to create a transaction. The .NET Data Provider supports both models:

- The explicit programming model allows the programmer to create, enlist into, and control the transaction manually.
- The implicit programming model allows .NET to automatically perform these operations. The implicit programming model is recommended as a best practice since there are fewer chances for programming errors and it frees the programmer from the details of managing enlistment in the System.Transactions.Transaction.

#### Implicit Automatic Enlistment using TransactionScope

The System.Transactions.TransactionScope class allows a .NET application to establish a transaction context. When a TransactionScope is instantiated, a current transaction context is established by .NET. Resource managers such as Ingres by default enlist in this ambient transaction. If an IngresConnection.Open() is issued by the application within the scope of this current transaction, and if the ConnectionString contains Enlist=yes (the default), then the IngresConnection automatically enlists the IngresConnection into the transaction.

Within the scope of the TransactionScope, the application calls the TransactionScope.Complete() method to indicate that the database unit of work should be committed. If the method is not called, the work is rolled back. When the TransactionScope is Disposed, updates to the Ingres database are committed or rolled back as directed by the .NET Transaction Manager. The Transaction Manager examines whether TransactionScope.Complete() method was called and issues the appropriate commit or rollback statements to Ingres.

!!! note "Note"

    When an Ingres connection is enlisted in the .NET transaction, the commit or rollback to Ingres to commit/rollback the database changes occur when the TransactionScope is disposed, not when the IngresConnection is closed or disposed. Even though a IngresConection.Close() method has been called and the IngresConection instance has been disposed, the Ingres session remains active until the .NET TransactionScope is disposed and the .NET Transaction Manager issues the commit/rollback to the Ingres session.

The .NET application programmer can prevent automatic enlistment of the IngresConnection in the transaction context if the IngresConnection.ConnectionString includes the Enlist=No keyword/value pair.

The advantage to coding a “using” statement and TransactionScope is that if any of the database operations throws an exception, flow of control jumps out of the "using (TransactionScope)" block and a rollback of the transaction automatically occurs. The ease of programming and reliability of rollback or commit within the TransactionScope makes this model of enlistment a better programming practice.

This example shows the enlistment of an Ingres database session in a distributed transaction managed by a using TransactionScope block. When the IngresConnection.Open( ) method is issued, the Ingres connection will enlist in the distributed transaction represented by the Transaction object within the TransactionScope. After the update, the TransactionScope is marked Complete(), and the updates to the Ingres database will be committed when the TransactionScope object is disposed.

```
static void TestEnlistTransactionImplicitSample(
```

```
      string connstring)
```

```
{
```

```
   using (TransactionScope scope = new TransactionScope())
```

```
   {
```

```

```

```
      using (IngresConnection conn1 =
```

```
         new IngresConnection(connstring))
```

```
      {
```

```
         conn1.Open();
```

```

```

```
         IngresCommand cmd = conn1.CreateCommand();
```

```
         cmd.CommandText =
```

```
            "update authors set au_id = '409-56-7008' " +
```

```
            "where au_id = '409-56-7008'";
```

```
         cmd.ExecuteNonQuery();
```

```

```

```
         scope.Complete();
```

```

```

```
      }  // end using (IngresConnection)
```

```
   }     // end using (TransactionScope)
```

```
}
```

#### Explicit Enlistment by EnlistTransaction() Method

A .NET application can disable automatic transaction enlistment and manually enlist the Ingres connection in the transaction if desired. The application programmer can prevent automatic enlistment of the IngresConnection in the current transaction context if the IngresConnection.ConnectionString includes the Enlist=no or Enlist=false keyword/value pair. Later, the application can manually enlist the Ingres connection in the transaction by calling the IngresConnection.EnlistTransaction method. The .NET Transaction Manager will issue a commit to the Ingres transaction if the .NET System.Transactions.Transaction is marked complete before the Transaction object is disposed, else the Ingres transaction will be rollbacked.

#### Actian Data Platform Enlistment in a .NET Transaction

Whether the enlistment is automatic or manual, when an Actian Data Platform connection is enlisted in a .NET transaction, the .NET Data Provider participates as a resource manager within the transaction. The data provider works with the Microsoft Distributed Transaction Coordinator (MSDTC), Actian Warehouse, and the Ingres XA Distributed Transaction Processing (DTP) subsystem to allow the warehouse connection to participate in the distributed transaction on Windows with other participants. The participants are polled in a vote to commit in a two-phase commit protocol (2PC). If the vote to commit is unanimous, all participants are directed to commit; otherwise, they are directed to roll back the database updates as an atomic unit of work.

## IngresConnectionStringBuilder Class

The IngresConnectionStringBuilder class provides a series of properties and methods to create syntactically correct connection string and to parse and rebuild existing connection strings.

### IngresConnectionStringBuilder Class Declaration

The IngresConnectionStringBuilder class can be declared as follows:

**C#:** public sealed class IngresConnectionStringBuilder : DbConnectionStringBuilder

**VB.NET:** NotInheritable Public Class IngresConnectionStringBuilder
 Inherits DbConnectionStringBuilder

### IngresConnectionStringBuilder Class Properties

The IngresConnectionStringBuilder class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| BrowsableConnectionString | get set | Indicates whether the ConnectionString Property is visible in Visual Studio designers. |
| BlankDate | get set | BlankDate=null specifies that an Ingres blank (empty) date result value is to be returned to the application as a null value. The default is to return an Ingres blank date as a DateTime value of "9999-12-31 23:59:59". |
| CharacterEncoding | get set | Specifies the .NET character encoding (for example, ISO-8859-1) used for conversions between Unicode and character data types. |
| Compress | get set | Specifies whether network communication blocks are compressed between the data provider and server. |
| ConnectTimeout | get set | The time, in seconds, to wait for an attempted connection to time out if the connection has not completed. Default is 15. |
| Count | get | The number of keys contained within the ConnectionString property. |
| CursorMode | get set | Specifies the default cursor concurrency mode, which determines the concurrency of cursors that have no explicitly assigned option in the command text. For example, FOR UPDATE or FOR READONLY. |
| Database | get set | Name of the Ingres or Actian Data Platform database being connected to. |
| DateAlias | get set | Specifies the alias data type for the DATE data type:ansidate – Sets ANSIDATE as the alias for DATEingresdate – Sets INGRESDATE is the alias for DATE |
| DateFormat | get set | Specifies the Ingres date format to be used by the Ingres server for date literals. Corresponds to the Ingres environment variable II_DATE_FORMAT and is assigned the same values. |
| DbmsUser | get set | The user name associated with the DBMS session. |
| DbmsPassword | get set | The DBMS password of the user. |
| DecimalChar | get set | Specifies the character that the Ingres DBMS Server is to use to separate fractional and non-fractional parts of a number—the comma (',') or the period ('.'). Default is the period. |
| Encrypt | get set | If set to true, encrypt the data between the data provider and server. Default is true. |
| EncryptionAESKeySize | get set | Size of the AES key in bits. Supported values are: 128, 192, and 256. Default is 128. |
| EncryptionRSAKeySize | get set | Size of the RSA key in bits. Supported values are: 1024, 2048, 3072, and 4096. Default is 1024 |
| EncryptionRSAKeyScope | get set | Defines the scope where an RSA key is used:process – (Default) One RSA key is generated in a process and used for all connections originating from that process.connection – An RSA key is generated for each connection and used only for that connection. |
| Enlist | get set | If set to true and if the creation thread is within a transaction context as established by System.EnterpriseServices.ServicedComponent, the IngresConnection is automatically enlisted into the transaction context. Default is true. |
| GroupID | get set | Group identifier that has permissions for a group of users. |
| IdentifierDelimiter | get set | The character recognized by the data provider to delimit an identifier:dquote – (Default) Recognizes only double-quotesbracket – Recognizes both double-quotes and brackets |
| Item | get set | The value associated with the key. This property is the C# indexer for the IngresConnectionStringBuilder class. |
| Keys | get | An ICollection of keys of type String in the IngresConnectionStringBuilder. |
| MaxPoolSize | get set | Maximum number of connections that can be in the connection pool. Default is 100. |
| MinPoolSize | get set | Minimum number of connections that can be in the connection pool. Default is 0. |
| MoneyFormat | get set | The Ingres money format to be used by the Ingres server for money literals. Corresponds to the Ingres environment variable II_MONEY_FORMAT and is assigned the same values. |
| MoneyPrecision | get set | The money precision to be used by the Ingres server for money literals. Corresponds to the Ingres environment variable II_MONEY_PREC and is assigned the same values. |
| Password | get set | The password to the Ingres database. |
| PersistSecurityInfo | get set | Indicates whether password information is returned in a get of the ConnectionString. |
| Pooling | get set | Enables or disables connection pooling. By default, connection pooling is enabled (true). |
| Port | get set | Port number on the target server machine that the Data Access Server is listening to. |
| PrefetchBlocks | get set | Prefetch blocking factor to override the default algorithm for computing the number of row blocks to fetch from a result-set. Default is 1 (no changes in default prefetch behavior). |
| RoleID | get set | Role identifier that has associated privileges for the role. |
| RolePassword | get set | Role password associated with the Role ID. |
| SendIngresDates | get set | Whether DateTime, Date, and Time values should be sent as INGRESDATE data type. Valid values are:false – (Default) Sends values as ANSI timestamp_with_timezone, ANSI date, ANSI time respectively.true – Sends values as INGRESDATE type.This option can be used for compatibility with semantic rules from older releases of Ingres |
| Server | get set | The Ingres or Actian Data Platform host server to connect to. |
| Timezone | get set | The Ingres or Actian Data Platform time zone associated with the user’s location. Used by the Ingres server only. Corresponds to the Ingres environment variable II_TIMEZONE_NAME and is assigned the same values. |
| UserID | get set | The name of the authorized user connecting to the warehouse. This value may be case-sensitive depending on the target server. |
| Values | get | An ICollection of values of type Object in the IngresConnectionStringBuilder. |
| VnodeUsage | get set | Allows the .NET application to control the portions of the vnode information that are used to establish the connection to the remote warehouse through the Ingres Data Access Server:connect – (Default) Uses only the vnode connection informationlogin – Uses both the vnode connection and login information |

### IngresConnectionStringBuilder Class Methods

The public methods available to the IngresConnectionStringBuilder class are:

| Method | Description |
| --- | --- |
| Add | Adds a key and value to the collection within IngresConnectionStringBuilder. |
| Clear | Clears all keys and values from IngresConnectionStringBuilder. Sets ConnectionString propery to “”. |
| ContainsKey | Returns true if IngresConnectionStringBuilder contains the specified key. |
| EquivalentTo | Returns true if keys and values are comparable to the specified IngresConnectionStringBuilder object. |
| Remove | Removes the entry with the specified key from IngresConnectionStringBuilder. |
| ToString | Returns the ConnectionString associated in the IngresConnectionStringBuilder. |
| TryGetValue | Returns a value corresponding to the specified key from the IngresConnectionStringBuilder. Returns false if the key was not found. |

### IngresConnectionStringBuilder Class Constructors

The IngresConnectionStringBuilder class has the following constructors:

| Constructor Overloads | Description |
| --- | --- |
| IngresConnectionStringBuilder () | Instantiates a new instance of the IngresConnectionStringBuilder class using default property values |
| IngresConnectionStringBuilder (string) | Instantiates a new instance of the IngresConnectionStringBuilder class using the specified connection string. |

## IngresDataReader Class

IngresDataReader provides a means of reading a forward-only stream of rows from a result-set created by a SELECT query or a row-producing database procedure.

When an IngresDataReader is open, the IngresConnection is busy and no other operations are allowed on the IngresConnection (other than IngresConnection.Close) until IngresDataReader.Close is issued. Created by the IngresCommand.ExecuteReader methods.

### IngresDataReader Class Declaration

The IngresDataReader can be declared as follows:

**C#:**public sealed class IngresDataReader : System.Data.Common.DbDataReader

**VB.NET:**NotInheritable Public Class IngresDataReader
 Inherits System.Data.Common.DbDataReader

### IngresDataReader Class Example

The following is an example implementation of the IngresDataReader class:

```
static void ReaderDemo(string connstring)
```

```
{
```

```
    IngresConnection conn = new IngresConnection(connstring);
```

```

```

```
    string strNumber;
```

```
    string strName;
```

```
    string strSSN;
```

```

```

```
    conn.Open();
```

```

```

```
    IngresCommand cmd = new IngresCommand(
```

```
        "select number, name, ssn  from personnel", conn);
```

```

```

```
    IngresDataReader reader = cmd.ExecuteReader();
```

```

```

```
    Console.Write(reader.GetName(0) + "\t");
```

```
    Console.Write(reader.GetName(1) + "\t");
```

```
    Console.Write(reader.GetName(2));
```

```
    Console.WriteLine();
```

```

```

```
    while (reader.Read())
```

```
    {
```

```
        strNumber= reader.IsDBNull(0)?
```

```
            "<none>":reader.GetInt32(0).ToString();
```

```
        strName  = reader.IsDBNull(1)?
```

```
            "<none>":reader.GetString(1);
```

```
        strSSN   = reader.IsDBNull(2)?
```

```
            "<none>":reader.GetString(2);
```

```

```

```
        Console.WriteLine(
```

```
        strNumber + "\t" + strName + "\t" + strSSN);
```

```
    }
```

```

```

```
    reader.Close();
```

```
    conn.Close();
```

```
}
```

### IngresDataReader Class Properties

The IngresDataReader class contains these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Depth | get | The depth of nesting for the current row. This data provider always returns a depth of zero to indicate no nesting of tables. |
| FieldCount | get | The number of columns in the current row. |
| HasRows | get | Returns true if the data reader contains one or more rows. Returns false if the data reader contains zero rows. |
| IsClosed | get | A true/false indicator as to whether the data reader is closed. |
| Item | get | Gets the column value in its native format for a given column name or column ordinal. This property is the C# indexer for the IngresDataReader class. |
| RecordsAffected | get | The number of rows updated, inserted, or deleted by execution of the SQL statement. -1 is returned for SELECT statements. |

### IngresDataReader Class Public Methods

The public methods available to the IngresDataReader class are:

| Method | Description |
| --- | --- |
| Close | Closes the IngresDataReader. |
| GetBoolean | Gets the column value as a Boolean. |
| GetByte | Gets the column value as an unsigned 8-bit Byte. |
| GetBytes | Gets the column value as a byte stream into a Byte array. |
| GetChar | Gets the column value as a Char. |
| GetChars | Gets the column value as a character stream into a Char array. |
| GetDataTypeName | Gets the column's data type name as known in Ingres. |
| GetDateTime | Gets the column value as a DateTime. |
| GetDecimal | Gets the column value as a Decimal. |
| GetDouble | Gets the column value as a double. |
| GetFieldType | Gets the column's .NET Type. |
| GetFloat | Gets the column value as a Float. |
| GetGuid | Gets the column value as a Guid. |
| GetInt16 | Gets the column value as a signed 16-bit integer. |
| GetInt32 | Gets the column value as a signed 32-bit integer. |
| GetInt64 | Gets the column value as a signed 64-bit integer. |
| GetName | Gets the column's name using a specified ordinal. |
| GetOrdinal | Gets the column's ordinal using a specified name. |
| GetSchemaTable | Returns a DataTable that describes the resultset column metadata. If ExecuteReader( CommandBehavior.KeyInfo ) was called, additional information about primary key columns, unique columns, and base names is retrieved from the database catalog and included in the returned DataTable. For column information returned, see [GetSchemaTable Columns Returned](../Connectivity/NET_Data_Provider_Classes.md). |
| GetString | Gets the column value as a string. |
| GetTimeSpan | Gets the column value as a TimeSpan. |
| GetValue | Gets the column value in its native format. |
| GetValues | Gets all of the column values into an Object array. |
| IsDBNull | Returns true/false indicating whether the column value is null. |
| NextResult | Advances the data reader to the next result set if present. |
| Read | Advances the data reader to the next row in the result set. |

!!! warning "Important"

    **IMPORTANT!**There are no conversions performed by the GetXXX methods. If the data is not of the correct type, an InvalidCastException is thrown.

Always call IsDBNull on a column if there is any chance of it being null before attempting to call one of the GetXXXaccessor to retrieve the data.

### GetSchemaTable Columns Returned

The GetSchemaTable describes the column metadata of the IngresDataReader.

!!! note "Note"

    The column information is not necessarily returned in the order shown.

| Column Information | Data Type | Description |
| --- | --- | --- |
| ColumnName | String | The name of the column, which reflects the renaming of the column in the command text (that is, the alias). |
| ColumnOrdinal | Int32 | The number of the column, beginning with 1. |
| ColumnSize | Int32 | Maximum possible length of a value in the column. |
| NumericPrecision | Int16 | This is the maximum precision of the column if the column is a numeric data type; otherwise the value is null. |
| NumericScale | Int16 | This is the number of decimal places in the column if the column is a numeric data type; otherwise the value is null. |
| DataType | Type | The .NET Framework data type of the column. |
| ProviderType | IngresType | The indicator of the column's data type |
| IsLong | Boolean | Set to true if the column contains a long varchar, long varbinary, or long nvarchar object; otherwise false. |
| AllowDBNull | Boolean | Set to true if the application can set the column to a null value or if the data provider cannot determine if the application can set the column to a null value. Set to false if it is known that the application is not permitted to set the column to a null. Note that a column value may be null even if the application is not permitted to set the null value. |
| IsReadOnly | Boolean | Set to true if it is known that the column cannot be modified; otherwise false. |
| IsRowVersion | Boolean | Set to true if column has a persistent row identifier that cannot be written to and serves only to identify the row. The .NET Data Provider always returns false. |
| IsUnique | Boolean | Set to true if no two rows in the table can have the same value in this column. Set to false if not unique or if uniqueness cannot be determined. Only set if ExecuteReader(CommandBehavior.KeyInfo) was called. |
| IsKey | Boolean | Set to true if this column is in the set of columns that, taken together, uniquely identify the row. Only set if ExecuteReader( CommandBehavior.KeyInfo) was called. |
| IsAutoIncrement | Boolean | Set to true if the column assigns values to new rows in fixed increments. The .NET Data Provider always returns false. |
| BaseCatalogName | String | The name of the database catalog that contains the column. This value is null if the catalog name cannot be determined. The .NET Data Provider always returns a null value. |
| BaseSchemaName | String | The name of the database schema that contains the column. This value is null if the schema name cannot be determined. Only set if ExecuteReader(CommandBehavior.KeyInfo) was called. |
| BaseTableName | String | The name of the database table or view that contains the column. This value is null if the table name cannot be determined. Only set if ExecuteReader(CommandBehavior.KeyInfo) was called. |
| BaseColumnName | String | The name of the column in the database. This value is null if the column name cannot be determined. Only set if ExecuteReader( CommandBehavior.KeyInfo ) was called. |

### Mapping of Ingres Native Types to .NET Types

The following table maps the native Ingres database types supported by the .NET Data Provider to their corresponding .NET type. It also maps the typed accessor that a .NET application uses for an Ingres native database type to be obtained as a .NET type.

| IngresType | Ingres Data Type | .NET Data Type | Accessor |
| --- | --- | --- | --- |
| Binary | byte | Byte[] | GetBytes() |
| Char | char | String | GetString() |
| DateTime | date | DateTime | GetDateTime() |
| Decimal | decimal | Decimal | GetDecimal() |
| Double | double precision  (float8) | Double | GetDouble() |
| SmallInt | smallint | Int16 | GetInt16() |
| TinyInt | integer1 | Byte | GetByte() |
| Int | integer | Int32 | GetInt32() |
| BigInt | bigint | Int64 | GetInt64() |
| LongVarBinary | long byte | Byte[] | GetBytes() |
| LongVarChar | long varchar | String | GetString() |
| LongNVarChar | long nvarchar | String | GetString() |
| Nchar | nchar | String | GetString() |
| NvarChar | nvarchar | String | GetString() |
| Real | real (float4) | Single | GetString() |
| VarBinary | byte varying | Byte[] | GetBytes() |
| VarChar | varchar | String | GetString() |
| IntervalYearToMonth | interval year to month | String | GetString() |
| IntervalDayToSecond | interval day to second | Timespan | GetTimeSpan() |

## IngresDataAdapter Class

The IngresDataAdapter class represents a set of SQL statements and a database connection that are used to fill a DataSet and, optionally, update the Ingres database. The IngresDataAdapter object acts as a bridge between a .NET DataSet and the Ingres database for retrieving and updating data.

### IngresDataAdapter Class Declaration

The declarations for the IngresDataAdapter class are:

**C#:**public sealed class IngresDataAdapter : DbDataAdapter, IDbDataAdapter, ICloneable

**VB.NET:**NotInheritable Public Class DataAdapter
 Inherits DbDataAdapter
 Implements IDbDataAdapter, ICloneable

### IngresDataAdapter Class Example

```
public DataSet CreateDataSet(
```

```
    string dsName, string connectionString, string commandText)
```

```
{
```

```
    IngresConnection connection =
```

```
        new IngresConnection(connectionString);
```

```
    IngresCommand command =
```

```
        new IngresCommand(commandText, connection);
```

```
    IngresDataAdapter adapter = new IngresDataAdapter(command);
```

```
    DataSet ds = new DataSet();
```

```
    adapter.Fill(ds, dsName);
```

```
    return ds;
```

```
}
```

### IngresDataAdapter Class Properties

The IngresDataAdapter class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| AcceptChangesDuringFill | get set | A true/false value indicating whether the DataRow.AcceptChanges method is called after the DataRow is added to the DataTable. Inherited from DataAdapter. Default is true. |
| ContinueUpdateOnError | get set | A true/false value indicating whether to generate an exception or to update the RowError property when an error occurs during an update to the row. Inherited from DataAdapter. Default is false. |
| DeleteCommand | get set | Command to be used (SQL statement or database procedure) to DELETE records from the database. |
| InsertCommand | get set | Command to be used (SQL statement or database procedure) to INSERT records into the database. |
| MissingMappingAction | get set | Action to be taken if incoming data does not have a matching table or column. Default is Passthrough. Inherited from DataAdapter. |
| MissingSchemaAction | get set | Action to be taken if an existing DataSet schema does not match incoming data. Inherited from DataAdapter. Default is Add. |
| SelectCommand | get set | Command to be used (SQL statement or database procedure) to SELECT records from the database. |
| TableMappings | get | The collection that provides the mapping between the returned records and the DataSet. Inherited from DataAdapter. Default is an empty collection. |
| UpdateBatchSize | get set | Enables or disables batch processing support (see [Batch Statement Execution](../Connectivity/NET_Data_Provider_Classes.md)) and specifies the number of commands that can be executed in a batch. Inherited from DbDataAdapter. Default is 1 (batch is disabled). |
| UpdateCommand | get set | Command to be used (SQL statement or database procedure) to UPDATE records in the database. |

### IngresDataAdapter Class Public Methods

The public methods available to the IngresDataAdapter Class are:

| Method | Description |
| --- | --- |
| Dispose | Releases allocated resources. |
| Fill | Adds or refreshes rows in the DataSet to match the values in the database. Inherited from DBDataAdapter. |
| FillSchema | Adds a DataTable to a DataSet and configures the schema to match that in the database. FillSchema does not add rows to a DataTable. Inherited from DBDataAdapter. |
| GetFillParameters | Gets an array of IDataParameter objects that contain the parameters set by the user when executing a SELECT statement. Inherited from DBDataAdapter. |
| Update | Calls the respective INSERT, UPDATE, or DELETE statements for each inserted, updated, or deleted row in the DataSet. Inherited from DBDataAdapter. |

### IngresDataAdapter Class Events

The events generated by the IngresDataAdapter class are:

| Event | Description |
| --- | --- |
| FillError | Raised when an error occurs during a Fill operation. Inherited from DBDataAdapter. |
| RowUpdating | Raised as an UPDATE, INSERT, or DELETE operation on a row (by a call to one of the Update methods) is about to start. |
| RowUpdated | Raised after an UPDATE, INSERT, or DELETE operation on a row (by a call to one of the Update methods) is complete. |

### IngresDataAdapter Class Constructors

The IngresDataAdapter class contains the following constructors:

| Constructor Overloads | Description |
| --- | --- |
| IngresDataAdapter() | Instantiates a new instance of the IngresDataAdapter class using default property values |
| IngresDataAdapter  (IngresCommand) | Instantiates a new instance of the IngresDataAdapter class using the defined IngresCommand as the SelectCommand. |
| IngresDataAdapter  (string, IngresConnection) | Instantiates a new instance of the IngresDataAdapter class using the defined command text for a new instance of IngresCommand for the SelectCommand, and the IngresConnection object |
| IngresDataAdapter  (string, string) | Instantiates a new instance of the IngresDataAdapter class using the defined command text for the SelectCommand and a connection string |

### Batch Statement Execution

The IngresDataAdapter class supports batch processing through the UpdateBatchSize property. This property directs the data adapter to gather several INSERT, UPDATE, and DELETE statements and their parameter sets from a DataSet or DataTable into a single block and send it to the server instead of processing one operation at a time.

The IngresDataAdapter is the Actian Data Platform implementation of the .NET DbDataAdapter class and can be used to manage the flow of Actian Data Platform data between the .NET application and the Actian Data Platform data source. The data adapter contains the SELECT command to fill a DataTable with DataRows and also contains the INSERT, UPDATE, and DELETE commands to update the database. As the application makes updates in the DataTable, the value and state change of each DataRow is recorded in the DataRow but the changes are not committed to the database until the application calls the data adapter's Update() method. When the method is called, the data adapter sweeps the DataRows of the DataTable. If the DataRow has a RowState of Added, Changed, or Deleted, the data adapter invokes the respective INSERT, UPDATE, or DELETE command.

The Microsoft .NET Framework allows a .NET application to specify that the updates be gathered into a batch by the DbDataAdapter for processing by the database. You can use the UpdateBatchSize property of the .NET DbDataAdapter to control the batch size. An UpdateBatchSize value of 1 (the default) disables batch processing—that is, each update is processed individually in a call to the database server. An UpdateBatchSize > 1 specifies the number of rows to be updated by the batch. If UpdateBatchSize is set to 0 then the batch size is left to the discretion of the data provider.

The value you choose for UpdateBatchSize depends on the application and its environment. The slower the channel between the client and server machines, the better the relative performance will be due to batch support. The benefit of .NET batch is that fewer I/Os result in reduced elapsed time. While some batch sizes will have a dramatic improvement in rows processed per second, increasingly larger batch sizes will reach a point of diminishing returns as the constant database processing time overshadows the decreasing I/O time. Experimentation in the client/server system will suggest a good value for UpdateBatchSize that balances I/Os, CPU, memory resources, .NET Garbage Collection (GC) timing, server resources to process the batch, and overall performance. A good starting value for UpdateBatchSize is 1000. A higher or lower value may be better for your environment.

The data adapter and UpdateBatchSize property can be used to bulk load a database table. A .NET DataTable is loaded with the new rows, the DataTable is associated with the IngresDataAdapter, the IngresDataAdapter.UpdateBatchSize is set to an efficient value > 1, and the IngresDataAdapter.Update() method invoked to drive a batch of rows to be INSERTed instead of one row at a time. Faster batched inserts can be achieved if the following conditions are met:

- Inserts must be into a base table (not an updatable view or index).
- The table should not have any rules or integrities (while they are allowed, they slow processing).

- The table must not be a gateway table (for example, an IMA table, security audit log file, or an Enterprise Access table).

## IngresError Class

The IngresError class represents error or warning information returned by the Ingres database.

### IngresError Class Declaration

The IngresError class can be declared as follows:

**C#:**[Serializable] public sealed class IngresError

**VB.NET:**NotInheritable Public Class IngresError

### IngresError Class Example

The following is an implementation of the IngresError class:

```
static void PrintErrorCollection(IngresErrorCollection errcol)
```

```
{
```

```
    foreach(IngresError err in errcol)
```

```
    {
```

```
        PrintError(err);
```

```
    }
```

```
    Console.WriteLine("");
```

```
}
```

```

```

```
static void PrintError(IngresError err)
```

```
{
```

```
    Console.Write(err.GetType().ToString() + ":\n");
```

```
    Console.Write("\t" + "Message         = " +
```

```
        (err.Message    !=null?
```

```
            err.Message.ToString()    :"<null>") + "\n");
```

```
    Console.Write("\t" + "Source = " +
```

```
        (err.Source!=null?err.Source.ToString():"<null>") + "\n");
```

```
    Console.Write("\t" + "ToString: " + err.ToString() + "\n");
```

```
    Console.Write("\t" + "Number       = " +
```

```
        (err.Number.ToString()) + "\n");
```

```
    Console.Write("\t" + "SQLState       = " +
```

```
        (err.SQLState  !=null?
```

```
            err.SQLState.ToString()  :"<null>") + "\n");
```

```
    Console.WriteLine("");
```

```
}
```

### IngresError Class Properties

The IngresError class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Message | get | A description of the error. |
| Number | get | The database-specific error integer information returned by the Ingres database. |
| Source | get | Name of the data provider that generated the error. Always “Ingres.” |
| SQLState | get | The standard five-character SQLSTATE code. |

### IngresError Class Public Methods

The public methods available to the IngresError class are:

| Method | Description |
| --- | --- |
| ToString | A description of the error in the form of “IngresError:error-message-text”. |

## IngresErrorCollection Class

The IngresErrorCollection class represents a collection of the IngresError objects returned by the Ingres database. Created by IngresException, an IngresErrorCollection collection always contains at least one instance of IngresError.

### IngresErrorCollection Class Declaration

The declarations for the IngresErrorCollection class are:

**C#:**[Serializable]
 public sealed class IngresErrorCollection : ICollection, IEnumerable

**VB.NET:**<Serializable>
 NotInheritable Public Class IngresError
 Inherits ICollection Implements IEnumerable

### IngresErrorCollection Class Example

The following is an example implementation of the IngresErrorCollection class:

```
static void PrintErrorCollection(IngresErrorCollection errcol)
```

```
{
```

```
    foreach(IngresError err in errcol)
```

```
    {
```

```
        PrintError(err);
```

```
    }
```

```
    Console.WriteLine("");
```

```
}
```

```

```

```
static void PrintError(IngresError err)
```

```
{
```

```
    Console.Write(err.GetType().ToString() + ":\n");
```

```

```

```
    Console.Write("\t" + "Message         = " +
```

```
        (err.Message    !=null?
```

```
            err.Message.ToString()    :"<null>") + "\n");
```

```
    Console.Write("\t" + "Source = " +
```

```
        (err.Source!=null?err.Source.ToString():"<null>") + "\n");
```

```
    Console.Write("\t" + "ToString: " + err.ToString() + "\n");
```

```
    Console.Write("\t" + "Number       = " +
```

```
        (err.Number.ToString()) + "\n");
```

```
    Console.Write("\t" + "SQLState       = " +
```

```
        (err.SQLState  !=null?
```

```
            err.SQLState.ToString()  :"<null>") + "\n");
```

```
    Console.WriteLine("");
```

```
}
```

### IngresErrorCollection Class Properties

The IngresErrorCollection class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Count | get | The number of errors in the collection. |
| Item | get | Gets the IngresError for a given ordinal. This property is the C# indexer for IngresErrorCollection class. |

### IngresErrorCollection Class Public Methods

The public methods available to the IngresErrorCollection class are:

| Method | Description |
| --- | --- |
| CopyTo | Copies the elements of IngresErrorCollection to an Array. |

## IngresException Class

The IngresException class represents the exception that is thrown when error information is returned by the Ingres database.

### IngresException Class Declaration

The IngresException is declared as follows:

**C#:**[Serializable]
 public sealed class IngresException : SystemException

**VB.NET:**<Serializable>
 NotInheritable Public Class IngresException
 Inherits SystemException

### IngresException Class Example

The following is an example implementation of the IngresException class:

```
static void PrintException(IngresException ex){
```

```
    Console.Write(ex.GetType().ToString() + ":\n");
```

```
    Console.Write("\t" + "Errors         = " +
```

```
        (ex.Errors    !=null?ex.Errors.ToString()    :
```

```
            "<null>") + "\n");
```

```
    Console.Write("\t" + "HelpLink       = " +
```

```
        (ex.HelpLink  !=null?ex.HelpLink.ToString()  :
```

```
            "<null>") + "\n");
```

```
    Console.Write("\t" + "InnerException = " +
```

```
                (ex.InnerException!=null?ex.InnerException.ToString():
```

```
            "<null>") + "\n");
```

```
    Console.Write("\t" + "Source = " +
```

```
        (ex.Source    !=null?ex.Source.ToString()    :
```

```
            "<null>") + "\n");
```

```
    Console.Write("\t" + "TargetSite = " +
```

```
                (ex.TargetSite!=null?ex.TargetSite.ToString():"<null>") + "\n");
```

```
    Console.WriteLine("");
```

```
}
```

### IngresException Class Properties

The IngresException class contains these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Errors | get | An ErrorCollection of one or more Error objects that give more detailed information on the exception generated by the provider. |
| InnerException | get | The nested Exception instance that caused the current exception. Inherited from Exception. |
| Message | get | A concatenation of all the messages in the Errors collection. |
| Source | get | Name of the data provider that generated the error. Always “Ingres.” |
| StackTrace | get | A string representation of the frames on the call stack at the time the current exception was thrown. |
| TargetSite | get | The method that threw the current exception. Inherited from Exception. |

### IngresException Class Public Methods

The public methods available to the IngresException class are:

| Method | Description |
| --- | --- |
| ToString | The description of the exception as a string. |

## IngresFactory Class

The IngresFactory class helps generate many of the other Ingres classes in an inter-operable data provider model. For each Ingres class that the factory wants to construct, simply call the Ingres constructor for that class and return the object instance.

### IngresFactory Class Declaration

The IngresFactory class can be declared as follows:

**C#:** public sealed class IngresFactory : DbProviderFactory

**VB.NET:** NotInheritable Public Class IngresFactory
 Inherits DbProviderFactory

### IngresFactory Class Public Fields

The IngresFactory class has the following public fields:

| Field | Description |
| --- | --- |
| Instance | The static field containing the single instance of IngresFactory. |

### IngresFactory Class Public Methods

The public methods available to the IngresFactory class are:

| Method | Description |
| --- | --- |
| CreateCommand | Creates an instance of IngresCommand using the factory. |
| CreateCommandBuilder | Creates an instance of IngresCommandBuilder using the factory. |
| CreateConnection | Creates an instance of IngresConnection using the factory. |
| CreateConnectionStringBuilder | Creates an instance of IngresConnectionStringBuilder using the factory. |
| CreateDataAdapter | Creates an instance of IngresDataAdapter using the factory. |
| CreateDataSourceEnumerator | Always returns null. |
| CreateParameter | Creates an instance of IngresParameter using the factory. |
| CreatePermission | Creates an instance of IngresPermission using the factory. |

## IngresInfoMessageEventArgs Class

The IngresInfoMessageEventArgs class provides the information on warnings from the database to the delegate method that handles the InfoMessage event.

### IngresInfoMessageEventArgs Class Declaration

The IngresInfoMessageEventArgs class is declared as follows:

**C#:**public sealed class IngresInfoMessageEventArgs : EventArgs

**VB.NET:**NotInheritable Public Class IngresInfoMessageEventArgs
 Inherits EventArgs

### IngresInfoMessageEventArgs Class Example

The following is an implementation of the IngresInfoMessageEventArgs class:

```
static void OnInfoMessage(
```

```
    Object sender, IngresInfoMessageEventArgs e)
```

```
{
```

```
    Console.WriteLine("OnInfoMessage event args: ("+
```

```
        "ErrorCode=" + e.Number +
```

```

```

```
        ", Errors=" + e.Errors +
```

```
        ", Message=\"" + e.Message + "\"" +
```

```
        ", Source=" + e.Source +")");
```

```
}
```

### IngresInfoMessageEventArgs Class Properties

The following are the properties of the IngresInfoMessageEventArgs class:

| Property | Accessor | Description |
| --- | --- | --- |
| Errors | get | An ErrorCollection of one or more Error objects that give more detailed information on the warnings generated by the provider. |
| Message | get | A concatenation of all the messages in the Errors collection. |
| Number | get | The database-specific warning integer information returned by the Ingres database. |
| Source | get | Name of the data provider that generated the error. Always “Ingres.” |

## IngresInfoMessageEventHandler Class

The IngresInfoMessageEventHandler delegate represents the delegate method that handles the InfoMessage event.

### IngresInfoMessageEventHandler Class Declaration

The IngresInfoMessageEventHandler class has the following message declaration:

**C#:**[Serializable]
 public delegate void IngresInfoMessageEventHandler
 (object sender, IngresInfoMessageEventArgs e)

**VB.NET:**<Serializable>
 Public Delegate Sub IngresInfoMessageEventHandler _
 (ByVal sender As Object, ByVal e As
 IngresInfoMessageEventArgs)

### IngresInfoMessageEventHandler Class Example

The following is an implementation of the IngresInfoMessageEventHandler class:

```
static void DoWork(string connstring)
```

```
{
```

```
    IngresConnection conn = new IngresConnection(connstring);
```

```
    conn.InfoMessage += new
```

```
    IngresInfoMessageEventHandler(OnInfoMessage);
```

```
<do additional work>
```

```
 }
```

```

```

```
static void OnInfoMessage(
```

```
    Object sender, IngresInfoMessageEventArgs e)
```

```
{
```

```
    Console.WriteLine("OnInfoMessage event args: ("+
```

```
        "ErrorCode=" + e.Number +
```

```

```

```
        ", Errors=" + e.Errors +
```

```
        ", Message=\"" + e.Message + "\"" +
```

```
        ", Source=" + e.Source +")");
```

```
}
```

## IngresMetaDataCollectionNames Class

The IngresMetaDataCollectionNames class presents information on metadata, such as tables, views, and columns. Each member of the class is a constant string suitable for use as collectionName argument for the IngresConnection.GetSchema method.

The collectionNames supported are:

- Columns
- Indexes

- ProcedureParameters
- Procedures

- Tables
- Views

### IngresMetaDataCollectionNames Class Declaration

The IngresMetaDataCollectionNames Class can be declared as follows:

**C#:** public static class IngresMetaDataCollectionNames

**VB.NET:** Public Shared Class IngresMetaDataCollectionNames

## IngresParameter Class

The IngresParameter class represents a parameter for an IngresCommand for each question mark (?) placeholder in the command and, optionally, its mapping to a DataSet column.

The IngresParameter constructor determines the data type of the parameter in the following ways:

- The constructor specifies an IngresType enumeration
- The constructor specifies a System.DbType enumeration

- Through the .NET Framework System.Type of the Value object if no specific data type is in the constructor

### Positional Parameters

The data provider supports the positional (unnamed) parameter marker placeholder syntax using the question mark character (?) similar to ODBC and JDBC. Parameter data is accessed from the IngresParameterCollection in the same relative order as the parameter markers in the SQL statement.

### Named Parameters

The data provider supports named parameters. A named parameter marker is constructed by an initial character of question mark (?), at-sign (@), or colon (:) followed by a name. The name is an alphanumeric identifier or an integer. Databases vary in the use of the initial character for a named parameter. While the Ingres recommended initial parameter marker character is the question mark, the .NET Data Provider supports all three characters.

If one parameter is named then all of the parameters must be named. If one parameter is unnamed (positional) then all of the parameters must be unnamed. For the sake of code readability, a mix of named parameters and unnamed parameters is not permitted.

For the sake of code readability, a mix of named parameters, each with a different initial parameter marker character in a single SQL statement is also not permitted.

Multiple occurrences of the same named parameter marker in the SQL statement is permitted.

Excess named parameters that are not referenced in the SQL statement are permitted in the IngresParameterCollection and are ignored.

The name comparison between the named parameter marker in the SQL statement and the named parameter in the IngresParameterCollection is not case sensitive.

### Named Parameters Example

The following is an example of using named parameters:

```
cmd = conn.CreateCommand();
```

```
cmd.CommandText =
```

```
      "insert into mytable  values ( ?key,  ?col1  ?col2  ?col3  )";
```

```
cmd.Parameters.AddWithValue("?key",  mykey);
```

```
cmd.Parameters.AddWithValue("?col3", mystring3);
```

```
cmd.Parameters.AddWithValue("?col1", mystring1);
```

```
cmd.Parameters.AddWithValue("?col2", mystring2);
```

```
cmd.ExecuteNonQuery();
```

```

```

```
cmd = conn.CreateCommand
```

```
cmd.CommandText =
```

```
      "insert into mytable  values ( @key,  @col1  @col2  @col3  )";
```

```
cmd.Parameters.AddWithValue("@key",  mykey);
```

```
cmd.Parameters.AddWithValue("@col3", mystring3);
```

```
cmd.Parameters.AddWithValue("@col1", mystring1);
```

```
cmd.Parameters.AddWithValue("@col2", mystring2);
```

```
cmd.ExecuteNonQuery();
```

```

```

```
cmd = conn.CreateCommand();
```

```
cmd.CommandText =
```

```
      "insert into mytable  values ( :key,  :col1  :col2  :col3  )";
```

```
cmd.Parameters.AddWithValue(":key",  mykey);
```

```
cmd.Parameters.AddWithValue(":col3", mystring3);
```

```
cmd.Parameters.AddWithValue(":col1", mystring1);
```

```
cmd.Parameters.AddWithValue(":col2", mystring2);
```

```
cmd.ExecuteNonQuery();
```

### IngresParameter Class Example

The following is an implementation of the IngresParameter class:

```
static string DemoParameterSSN(
```

```
    string connstring, int intNumber, string strSSN)
```

```
{
```

```
    IngresConnection conn = new IngresConnection(connstring);    string strName = null;    conn.Open();    IngresCommand cmd = new IngresCommand(
```

```
        "select name from demo_personnel where number = ? and ssn = ?",
```

```
        conn);    // add two parameters to the command's IngresParameterCollection
```

```
    cmd.Parameters.Add(new IngresParameter("Number", intNumber));
```

```
    IngresParameter parm =
```

```
        new IngresParameter("SSN", IngresType.VarChar);
```

```
    parm.Value = strSSN;
```

```
    cmd.Parameters.Add(parm);    IngresDataReader reader = cmd.ExecuteReader();    while (reader.Read())
```

```
    {
```

```
        if (reader.IsDBNull(0))
```

```
            break;
```

```
        strName  = reader.GetString(0);
```

```
    }    reader.Close();
```

```
    conn.Close();    return strName;
```

```
}
```

### IngresParameter Class Declaration

The class declaration for IngresParameter class is:

**C#:**public sealed class IngresParameter : System.Data.Common.DbParameter, IDataParameter, IDbDataParameter, ICloneable

**VB.NET:**NotInheritable Public Class IngresParameter
 Inherits System.Data.Common.DbParameter
 Implements IDataParameter, IDbDataParameter, ICloneable

### IngresParameter Class Properties

The properties for the IngresParameter are:

| Property | Accessor | Description |
| --- | --- | --- |
| DbType | get set | The type that the parameter must be converted to before being passed to the database server. Setting this parameter induces a setting of IngresType property.Default is DbType.String. |
| Direction | get set | Indicators whether the parameter has an input, input/output, output, or procedure return value. |
| IngresType | get set | The type that the parameter must be converted to before being passed to the database server. Setting this parameter induces a setting of DbType property.Default is IngresType.NvarChar if the database supports Unicode UCS-2; otherwise the default is IngresType.VarChar. |
| IsNullable | get set | Indicates whether the parameter accepts null values.  True = accepts null values. False = does not accept null values. |
| ParameterName | get set | The name of the parameter.Default is “”. |
| Precision | get set | Maximum number of digits for decimal parameters.Default is 0. |
| Scale | get set | Number of decimal places for decimal parameters.Default is 0. |
| Size | get set | Maximum size of binary and string data to be sent to the server.Default is inferred from the parameter value. |
| SourceColumn | get set | The name of the source column mapped to a DataSet.Default is “”. |
| SourceVersion | get set | The DataRowVersion used by an UpdateCommand during an Update operation for setting the parameter.Default is DataRowVersion.Current. |
| Value | get set | The value of the parameter.Default is null. |

!!! warning "Important"

    **IMPORTANT!**.NET strings are Unicode based. If the application is sending a Unicode string as a parameter to a database field that is ASCII char or varchar, the application can direct the data provider to coerce the Unicode string to an ASCII string on the client side by setting the parameter DbType property to DbType.AnsiString, or the IngresType property to IngresType.VarChar.

### IngresParameter Class Public Methods

The public methods available for the IngresParameter class are:

| Method | Description |
| --- | --- |
| ToString | The name of the parameter. |

### IngresParameter Class Constructors

The constructors available to the IngresParameter class are:

| Constructor Overloads | Description |
| --- | --- |
| IngresParameter() | Instantiates a new instance of the IngresParameter class using default property values |
| IngresParameter  (string, DbType) | Instantiates a new instance of the IngresParameter class using the defined parameter name and DbType. |
| IngresParameter  (string, IngresType) | Instantiates a new instance of the IngresParameter class using the defined parameter name and IngresType. |
| IngresParameter  (string, object) | Instantiates a new instance of the IngresParameter class using the defined parameter name and System.Object. The DbType and IngresType are inferred from the .NET Type of the object. |
| IngresParameter  (string, DbType, string) | Instantiates a new instance of the IngresParameter class using the defined parameter name, DbType, and source column name. |
| IngresParameter  (string, IngresType, string) | Instantiates a new instance of the IngresParameter class using the defined parameter name, IngresType, and source column name. |
| IngresParameter  (string, DbType, int) | Instantiates a new instance of the IngresParameter class using the defined parameter name, DbType, and column size. |
| IngresParameter  (string, IngresType, int) | Instantiates a new instance of the IngresParameter class using the defined parameter name, IngresType, and column size. |
| IngresParameter  (string, DbType, int, string) | Instantiates a new instance of the IngresParameter class using the defined parameter name, DbType, column size, and source column name. |
| IngresParameter  (string, IngresType, int, string) | Instantiates a new instance of the IngresParameter class using the defined parameter name, IngresType, column size, and source column name. |
| IngresParameter  (string, DbType, int, ParameterDirection, bool, byte, byte, string, DataRowVersion, object) | Instantiates a new instance of the IngresParameter class using the defined parameter name, DbType, column size, parameter direction, boolean indication of whether or not the field can be null, precision, scale, source column name, DataRowVersion describing the version of a System.Data.DataRow, and the value of the object. |
| IngresParameter  (string, IngresType, int, ParameterDirection, bool, byte, byte, string, DataRowVersion, object) | Instantiates a new instance of the IngresParameter class using the defined parameter name, IngresType, column size, parameter direction, boolean indication of whether or not the field can be null, precision, scale, source column name, DataRowVersion describing the version of a System.Data.DataRow, and the value of the object. |

## IngresParameterCollection Class

The IngresParameterCollection class represents a collection of all parameters for an IngresCommand object and their mapping to a DataSet object.

### IngresParameterCollection Class Declaration

The class declaration for IngresParameterCollection class is as follows:

**C#:**public sealed class IngresParameterCollection : System.Data.Common.DbParameterCollection, IDataParameterCollection, IList, ICollection, IEnumerable

**VB.NET:**NotInheritable Public Class IngresParameterCollection
 Inherits System.Data.Common.DbParameterCollection
 Implements IDataParameterCollection, IList, ICollection, IEnumerable

### IngresParameterCollection Class Example

For an example of adding parameters to an IngresParameterCollection, see [IngresParameter Class Example](../Connectivity/NET_Data_Provider_Classes.md).

### IngresParameterCollection Class Properties

The IngresParameterCollection has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Count | get | The number of parameters in the collection. |
| Item | get set | The IngresParameter object for a given ordinal or parameter name. This property is the C# indexer for IngresParameterCollection class. |

### IngresParameterCollection Class Public Methods

The public methods available to the IngresParameterCollection class are:

| Method | Description |
| --- | --- |
| Add | Adds an IngresParameter to the parameter collection. |
| AddRange | Adds an array of values or IngresParameters to the parameter collection |
| AddWithValue | Adds an IngresParameter with a name and value to the parameter collection. |
| Clear | Removes all items from the collection. |
| Contains | Indicates whether IngresParameter exists in the collection. True = does exist; False = does not exist. |
| CopyTo | Copies the elements of IngresParameterCollection to an Array. |
| IndexOf | Returns the index of the IngresParameter in the collection. |
| Insert | Inserts the IngresParameter into the collection. |
| Remove | Removes the IngresParameter from the collection. |
| RemoveAt | Removes an IngresParameter with a specified index or name from the collection. |

## IngresPermission Class

The IngresPermission class provides additional information that a user has a security level sufficient to access the Ingres database. At present, the class is not used by the .NET Data Provider. The class is included in the Ingres data provider to provide completeness for the Factory interoperability model. Instead, standard Ingres security and access control is used.

The IngresPermission class can be declared as follows:

**C#:** public sealed class IngresPermission : DBPermission

**VB.NET:** NotInheritable Public Class IngresPermission
 Inherits DBPermission

## IngresRowUpdatedEventArgs Class

The IngresRowUpdatedEventArgs class provides the information for the RowUpdated event of an IngresDataAdapter.

### IngresRowUpdatedEventArgs Class Declaration

The class declaration for IngresRowUpdateEventArgs is as follows:

**C#:**public sealed class IngresRowUpdatedEventArgs : RowUpdatedEventArgs

**VB.NET:**NotInheritable Public Class IngresRowUpdatedEventArgs
 Inherits RowUpdatedEventArgs

### IngresRowUpdatedEventArgs Class Properties

The IngresRowUpdatedEventArgs has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Command | get | The IngresCommand executed when DbDataAdapter.Update method is called. |
| Errors | get | The Exception containing any errors generated during the execution of the IngresCommand. Inherited from RowUpdatedEventArgs. |
| RecordsAffected | get | The number of rows updated, inserted, or deleted during the execution of the UPDATE, INSERT, or DELETE SQL statement. Inherited from RowUpdatedEventArgs. |
| Row | get | The System.Data.DataRow sent through the DbDataAdapter.Update. Inherited from RowUpdatedEventArgs. |
| StatementType | get | The type of SQL statement executed. Inherited from RowUpdatedEventArgs. |
| Status | get | The System.Data.UpdateStatus of the IngresCommand. Inherited from RowUpdatedEventArgs. |
| TableMapping | get | The DataTableMapping sent through a DbDataAdapter.Update. Inherited from RowUpdatedEventArgs. |

## IngresRowUpdatedEventHandler Class

The IngresRowUpdatedEventHandler delegate represents a delegate method that handles the RowUpdated event of an IngresDataAdapter.

### IngresRowUpdatedEventHandler Class Declaration

The IngresRowUpdateEventHandler class has the following declaration:

**C#:**[Serializable]
 public delegate void Ingres RowUpdated EventHandler
 ( object sender, IngresRowUpdated EventArgs e)

**VB.NET:**<Serializable>
 Public Delegate Sub Ingres RowUpdatedEventHandler _
 (ByVal sender As Object, ByVal e As
 IngresRowUpdatedEventArgs)

## IngresRowUpdatingEventArgs Class

The IngresRowUpdatingEventArgs class provides the information for the RowUpdating event of an IngresDataAdapter.

### IngresRowUpdatingEventArgs Class Declaration

The IngresRowUpdatingEventArgs class has the following declaration:

**C#:**public sealed class IngresRowUpdatingEventArgs : RowUpdatingEventArgs

**VB.NET:**NotInheritable Public Class Ingres RowUpdatingEventArgs
 Inherits RowUpdatingEventArgs

### IngresRowUpdatingEventArgs Class Properties

The IngresRowUpdatingEventArgs class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Command | get set | The IngresCommand executed when DbDataAdapter.Update method is called. |
| Errors | get | The Exception containing any errors generated during the execution of the IngresCommand. Inherited from RowUpdatedEventArgs. |
| RecordsAffected | get | The number of rows updated, inserted, or deleted during the execution of the UPDATE, INSERT, or DELETE SQL statement. Inherited from RowUpdatedEventArgs. |
| Row | get | The System.Data.DataRow sent through the DbDataAdapter.Update. Inherited from RowUpdatedEventArgs. |
| StatementType | get | The type of SQL statement executed. Inherited from RowUpdatedEventArgs. |
| Status | get | The System.Data.UpdateStatus of the IngresCommand. Inherited from RowUpdatedEventArgs. |
| TableMapping | get | The DataTableMapping sent through a DbDataAdapter.Update. Inherited from RowUpdatedEventArgs. |

## IngresRowUpdatingEventHandler Class

The IngresRowUpdatingEventHandler delegate represents a delegate method that handles the RowUpdating event of an IngresDataAdapter.

### IngresRowUpdatingEventHandler Class Declaration

The IngresRowUpdatingEventHandler class declaration is as follows:

**C#:**[Serializable]
 public delegate void IngresRowUpdatingEventHandler
 ( object sender, IngresRowUpdatingEventArgs e)

**VB.NET:**<Serializable>
 Public Delegate Sub Ingres RowUpdatingEventHandler _
 (ByVal sender As Object, ByVal e As IngresRowUpdatingEventArgs)

## IngresTransaction Class

The IngresTransaction class represents a local, non-distributed database transaction. Each connection is associated with a transaction. This object allows manual commit or rollback control over the pending local transaction.

Created by the BeginTransaction method in the IngresConnection object. After Commit() or Rollback has been issued against the transaction, the IngresTransaction object can not be reused and a new IngresTransaction object must be obtained from the IngresConnection.BeginTransaction method if another transaction is desired.

### IngresTransaction Class Declaration

The IngresTransaction class declaration is as follows:

**C#:**public sealed class IngresTransaction : System.Data.Common.DbTransaction

**VB.NET:**NotInheritable Public Class IngresTransaction
 Inherits System.Data.Common.DbTransaction

### IngresTransaction Class Example

The following is an implementation of the IngresTransaction class:

```
static void DemoTxn(string connstring)
```

```
{    IngresConnection conn = new IngresConnection(connstring);    ProviderTransaction txn;    conn.Open();    txn = conn.BeginTransaction();    IngresCommand cmd = new IngresCommand(        "update demo_personnel set name = 'Howard Lane' "+        "  where number = 200", conn, txn);    int numberOfRecordsAffected = cmd.ExecuteNonQuery();    Console.WriteLine(numberOfRecordsAffected.ToString() +        " records updated.");    txn.Commit();    conn.Close();}
```

### IngresTransaction Class Properties

The IngresTransaction class has these properties:

| Property | Accessor | Description |
| --- | --- | --- |
| Connection | get | The IngresConnection object that is associated with the transaction. Null if the transaction or connection is no longer valid. |
| IsolationLevel | get | The IsolationLevel for this transaction as set in the IngresConnection.BeginTransaction method. |

### IngresTransaction Class Methods

The IngresTransaction class contains the following methods:

| Method | Description |
| --- | --- |
| Commit | Commit the database changes. |
| Dispose | Release allocated resources. |
| Rollback | Roll back the database changes. |
