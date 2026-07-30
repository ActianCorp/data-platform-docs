---
title: "JDBC Driver Interface"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "JDBC_Driver_Interface.htm"
canonical_id: "actian-data-platform-jdbc-driver-interface"
---

## JDBC Driver Interface

This section details the JDBC Driver interface class files and their associated properties. It also includes instructions for loading and accessing the driver.

## JDBC Driver and Data Source Classes

The JDBC Driver and data source classes are located in the Java package, com.ingres.jdbc.

These packages are contained in the Java archive iijdbc.jar, which includes the following class files:

| Class | Implemented JDBC Interface |
| --- | --- |
| com.ingres.jdbc.IngresDriver | The Actian Data Platform implementation of the JDBC Driver interface (java.sql.Driver). |
| com.ingres.jdbc.IngresDataSource | The Actian Data Platform implementation of the JDBC DataSource interface (javax.sql.DataSource). |
| com.ingres.jdbc.IngresCPDataSource | The Actian Data Platform implementation of the JDBC ConnectionPoolDataSource interface (javax.sql.ConnectionPoolDataSource). |
| com.ingres.jdbc.IngresXADataSource | The Actian Data Platform implementation of the JDBC XADataSource interface (javax.sql.XADataSource). |

!!! note "Note"

    The original JDBC Driver and DataSources classes contained in the Java archive iijdbc.jar under the Java package path of “ca.ingres.jdbc” are moved to the package path of “com.ingres.jdbc”. The iijdbc.jar archive included with Ingres 9.0 also contains the original classes for backward compatibility. Starting with Ingres 10.0, the “ca.ingres.jdbc” package is no longer included in the iijdbc.jar archive. Existing references to “ca.ingres.jdbc” classes must be changed to “com.ingres.jdbc”.

### JDBC Driver Properties

Driver properties allow applications to establish connection parameters that are driver-dependent. JDBC Driver properties can be specified as follows:

- As connection URL attributes as a Java Properties parameter to a DriverManager.getConnection() method
- As Java system properties

- In a properties file

Attribute and property names are given below.

When specified as system properties or in a property file, the property key must be of the form:

```
ingres.jdbc.property.property_name
```

During Actian Data Platform Client Runtime package installation, the [JDBC Driver Properties Generator (iijdbcprop)](../Connectivity/JDBC_Driver_Interface.md) reads the Ingres configuration and generates the corresponding JDBC driver properties file, named iijdbc.properties.

A default properties file (typically iijdbc.properties) is loaded automatically by the JDBC Driver when the driver class is loaded. The file must reside in a location accessible by the class loader used to load the driver. In general, this requires that the properties file directory be included in the Java environment variable CLASSPATH.

An alternate properties file can also be specified using the system property ingres.jdbc.property_file. The directory path of the property file can be specified or the property file can be placed in a directory accessible as described above for the default properties file. Properties are searched in the following order: URL attributes, getConnection() property set, system properties, alternate properties file, and default properties file.

The JDBC Driver supports these properties:

| Property | Attribute | Description |
| --- | --- | --- |
| user | UID | The user ID on the target warehouse machine. See the description of the vnode_usage property in this table.This property can be used if the user has no DBMS user ID and password assigned (see dbms_user and dbms_password in this table). |
| password | PWD | The user’s operating system password. |
| role | ROLE | The desired role identifier. If a role password is required, include it with the role name as follows: name/password. |
| group | GRP | The user’s group identifier. |
| dbms_user | DBUSR | The user name associated with the DBMS session (Actian Data Platform -u flag, can require admin privileges). |
| dbms_password | DBPWD | The user’s DBMS password (Actian Data Platform -P flag). |
| compression | COMPRESS | Whether data is compressed over the network. Valid values are:off – Compression offon – (Default) Compression on |
| connect_pool | POOL | Server connection pool control. Valid values are:off – Requests a non-pooled connection when server pooling is enabledon – Requests a pooled connection when server pooling is optional.The default is to allow the DAS configuration to determine pooling. |
| select_loop | LOOP | Select loop vs. cursor queries. Valid values are:on – Uses select loops to retrieve query resultsoff – (Default) Uses cursorsFor more information, see [Cursors and Select Loops](../Connectivity/JDBC_Implementation_Considerations.md). |
| autocommit_mode | AUTO | Autocommit cursor handling mode. Valid values are:dbms – (Default) autocommit processing is done by the warehousesingle – DAS enforces single cursor operation during autocommitmulti–DAS simulates autocommit operations when more than one cursor is open.For more information, see [How Transactions Are Autocommitted](../Connectivity/JDBC_Implementation_Considerations.md). |
| cursor_mode | CURSOR | Default cursor concurrency mode, which determines the concurrency of cursors that have no concurrency explicitly assigned. Valid values are:dbms – Concurrency is determined by the warehouseupdate – Provides updateable cursorsreadonly – (Default) Provides non-updateable cursorsFurther details are provided in [Cursors and Result Set Characteristics](../Connectivity/JDBC_Implementation_Considerations.md). |
| vnode_usage | VNODE | Allows the JDBC application to control the portions of the vnode information that are used to establish the connection to the remote warehouse. Valid values are:connect – (Default) Only the vnode connection information is used to establish the connection.login – Both the vnode connection and login information are used to establish the connection.For more information, see [JDBC User Authentication](../Connectivity/JDBC_Implementation_Considerations.md). |
| encryption | ENCRYPT | Defines the default encryption mode used by client connections. Valid values are:on – Encryption is required and occurs unless no compatible encryption mechanism is available. Connection fails if encryption is not possible.off – (Default) Encryption is disabled. |
| char_encode | ENCODE | Specifies the Java character encoding used for conversions between Unicode and character data types. Generally, the character encoding is determined automatically by the driver from the DAS installation character set. This property allows an alternate character encoding to be specified (if desired) or a valid character encoding to be used when the driver is unable to map the server’s character set. |
| timezone | TZ | Specifies the time zone associated with the client’s location. Corresponds to the Actian Data Platform environment variable II_TIMEZONE_NAME and is assigned the same values. This property is not used directly by the driver but is sent to the DBMS and affects the processing of dates. |
| decimal_char | DECIMAL | Specifies the character to be used as the decimal point in numeric literals. Corresponds to the Actian Data Platform environment variable II_DECIMAL and is assigned the same values. This property is not used directly by the driver but is sent to the DBMS and affects the processing of query text. |
| date_alias | DATE | Specifies the data type of columns created using the alias keyword "date". Valid values are: "ansidate" or "ingresdate". Default value is "ansidate" if the property send_ingres_dates is set to false, otherwise it is "ingresdate". This property is not used directly by the driver but is sent to the DBMS and affects the processing of query text. |
| date_format | DATE_FMT | Specifies the Actian Data Platform format for date literals. Corresponds to the Actian Data Platform environment variable II_DATE_FORMAT and is assigned the same values. This property is not used directly by the driver, but is sent to the DBMS and affects the processing of query text. |
| money_format | MNY_FMT | Specifies the Actian Data Platform format for money literals. Corresponds to the Actian Data Platform environment variable II_MONEY_FORMAT and is assigned the same values. This property is not used directly by the driver but is sent to the DBMS and affects the processing of query text. |
| money_precision | MNY_PREC | Specifies the precision of money data values. Corresponds to the Actian Data Platform environment variable II_MONEY_PREC and is assigned the same values. This property is not used directly by the driver but is sent to the DBMS and affects the processing of money values. |
| send_ingres_dates | SEND_INGDATE | Specifies whether datetime values should be sent as INGRESDATE data type. Valid values are:false – Values sent as ANSI TIMESTAMP WITH TIMEZONE typetrue – Values sent as INGRESDATE typeDefault value is false if date_alias property is set to "ansidate"; otherwise it is true. Unlike date_format and date_alias, this property is internal to the driver, not sent to the DBMS, and affects the processing of query text. |
| send_integer_booleans | SEND_INTBOOL | Specifies if Boolean parameters are converted to tinyint values when sent to the DBMS. Valid values are:true – Boolean parameters are converted to tinyint valuesfalse – (Default) Boolean parameters are sent as Boolean values |
| identity_query | IDENTITY | Enables or disables the identity query. Valid values are:on – (Default) Identity query is issued if no table key or object key is received and other conditions permit. This setting provides the best behavior for applications that use only table or object keys or only identity columns.off – Identity query is not issued and identity values are not returned. This setting is appropriate if only table or object keys are used. |
| metadata_underscore | META_UNDER | Enables or disables the underscore character, ‘_’, as a pattern wildcard in DatabaseMetaData methods whose parameters are defined as patterns. Valid values are:true – (Default) Underscore character is treated as a wildcard in metadata patterns.false – Underscore is treated as a literal character in metadata patterns. |

Attributes can also be specified using the property name as the attribute name. Thus "UID=user1" and "user=user1" are semantically the same.

#### JDBC Driver Properties Generator (iijdbcprop)

The iijdbcprop utility automatically generates all supported JDBC properties. The utility runs automatically during installation but can be run at any time.

This utility provides the following benefits:

- Automatically generates all JDBC properties that match related Actian Data Platform environment variables, such as II_TIMEZONE_NAME, II_DECIMAL, II_DATE_FORMAT, II_MONEY_FORMAT and II_MONEY_PREC. These properties can keep the JDBC Driver behavior synchronized with an Ingres or Actian Data Platform installation, since the JDBC Driver does not have access to the Ingres or Actian Data Platform environment variables and is often deployed on a machine separate from Ingres or Actian Data Platform.
- Reduces typing errors when entering JDBC properties by hand. All available JDBC properties are generated, but properties not in the Actian Data Platform configuration files are commented out.

The iijdbcprop command writes the iijdbc.properties file into the directory:

Linux: $II_SYSTEM/ingres/files ]

Windows: %II_SYSTEM%\ingres\files ]

During loading of the JDBC Driver by the class loader, the directory containing the iijdbc.properties file must be specified in the Java environment variable CLASSPATH.

**Example Entries**—For example, to turn on tracing in the driver, uncomment the desired trace entries in the iijdbc.properties file by removing the leading # sign, and then provide appropriate values for them as shown here.

On Linux, the following entries in iijdbc.properties file will produce a JDBC Driver trace file under the /tmp directory called jdbc_driver.log, provided the $II_SYSTEM/ingres/files directory is in the CLASSPATH.

```
ingres.jdbc.trace.log=/tmp/jdbc_driver.log
```

```
ingres.jdbc.trace.drv=5
```

```
ingres.jdbc.trace.msg=3
```

### Data Source Properties

A data source configuration is a collection of information that identifies the target database to which the driver connects. The Data Source classes support the following data source properties and associated getter/setter methods.

| DS Property | Description |
| --- | --- |
| description | Description of the data source |
| serverName | Server host name or network address (required).Multiple hosts and associated ports can be specified using the following syntax:`host:port{,port}{;host:port{,port}}`TCP/IPv6 addresses (colon-hexadecimal format) must be enclosed in square brackets, for example: [::1]. If a single host name or address is provided with no port, the associated port must be provided using the portName or portNumber properties. If a port (or ports) is provided in this property, then the portName and portNumber properties should not be set. |
| portName | Symbolic port ID. Multiple ports can be provided, separated by commas. A port ID must be provided in the serverName, portName, or portNumber properties. |
| portNumber | Numeric port ID. A port ID must be provided either in the serverName, portName, or portNumber properties. |
| databaseName | Database name (required) |
| user | User’s ID. (A user ID is required when the DAS is not on the same machine as the JDBC client; otherwise this property is optional.) |
| password | User's password. (A password is required when the DAS is not on the same machine as the JDBC client; otherwise this property is optional.) |
| roleName | DBMS role identifier |
| groupName | DBMS group identifier |
| dbmsUser | User ID for the DBMS session (-u flag) |
| dbmsPassword | User's DBMS password |
| compression | Data compression: off or on |
| connectionPool | Use pooled connection: 'off' or 'on' |
| autocommitMode | Autocommit cursor handling: 'dbms', 'single', 'multi' |
| selectLoop | Select loop processing: 'off', or 'on' |
| cursorMode | Default cursor concurrency: 'dbms', 'update', 'readonly' |
| vnodeUsage | Vnode usage for warehouse access: 'login', 'connect' |
| charEncode | Java character encoding |
| timeZone | IANA or Ingres timezone |
| decimalChar | Actian Data Platform decimal character |
| dateAlias | Actian Data Platform date alias |
| dateFormat | Actian Data Platform date format |
| encryption | Data encryption: off or on |
| moneyFormat | Actian Data Platform money format |
| moneyPrecision | Actian Data Platform money precision |
| sendIngresDates | Send datetime values as ingresdate data type: 'true' or 'false' |
| sendIntegerBooleans | Send Boolean parameters as tinyint values: 'true' or 'false' |
| IdentityQuery | Issue identity query for identity columns: 'on' or 'off' |
| metadataUnderscore | Treat underscore character as metadata pattern wildcard: 'true' or 'false' |

The data source properties marked as “required” correspond to parameters contained in a connection URL. For a description of these parameters, see [DriverManager.getConnection() Method--Establish JDBC Driver Connection](../Connectivity/JDBC_Driver_Interface.md). The remaining Data Source properties correspond to the driver properties defined in JDBC Driver Properties.

### Additional Data Source Properties

In addition to the DataSource class properties, the ConnectionPoolDataSource and XADataSource classes support these properties and associated getter/setter methods:

| DS Property | Description |
| --- | --- |
| initialPoolSize | Initial connection pool size |
| minPoolSize | Minimum connection pool size |
| maxPoolSize | Maximum connection pool size |
| maxIdleTime | Maximum time in connection pool |
| propertyCycle | Wait time for checking the connection pool |

### System Properties

The following system properties can be used to configure the driver:

**ingres.jdbc.property_file**

:   Path and filename containing configuration system properties. Default is iijdbc.properties (must reside in CLASSPATH directory).

**ingres.jdbc.property.<property name>**

:   Driver connection properties. Defaults are property dependent.

**ingres.jdbc.batch.enabled**

:   Specifies whether batch statement processing is enabled. If set to true, batch statements will be executed together in a batch. If set to false (or if batch processing is not supported by the DBMS), batch statements will be executed individually. Default is true.

**ingres.jdbc.date.empty**

:   Replacement value, in standard JDBC datetime format YYYY-MM-DD hh:mm:ss, for Actian Data Platform empty dates. Can also be set to null to have empty dates returned as null values. For default behavior, set to default or empty, as described in [Datetime Columns and Values](../Connectivity/JDBC_Implementation_Considerations.md).

**ingres.jdbc.dbms.trace.log**

:   Path and filename of the DBMS trace log. Default is no trace log.

**ingres.jdbc.encryption.aes.key.size**

:   Size of the AES key in bits. Valid values are: 128, 192, 256 (limited by Java encryption provider capabilities). When client and server have different capabilities, the largest common key size will be used. Default is 128.

**ingres.jdbc.encryption.rsa.key.size**

:   Size of RSA key in bits. Valid values are: 1024, 2048, 3072, 4096. Default is 1024.

**ingres.jdbc.encryption.rsa.key.scope**

:   Defines the scope where an RSA key is used:

process

:   (Default) One RSA key is generated in a process and used for all connections originating from that process.

connection

:   An RSA key is generated for each connection and used only for that connection.

**ingres.jdbc.lob.cache.enabled**

:   Enable/disable caching Large Objects (true/false). Default is false.

**ingres.jdbc.lob.cache.segment_size**

:   Number of bytes/characters per segment in LOB cache. Default is 8192.

**ingres.jdbc.lob.locators.enabled**

:   Enable/disable Locators for Large Objects if supported by DBMS (true/false). Default is true.

**ingres.jdbc.lob.locators.autocommit.enabled**

:   Enable/disable Locators for Large Objects during autocommit (true/false). LOB Locators must also be generally enabled. Default is false.

**ingres.jdbc.lob.locators.select_loop.enabled**

:   Enable/disable Locators for Large Objects during select loops (true/false). LOB Locators must also be generally enabled. Default is false.

**ingres.jdbc.lob.locators.stream.enabled**

:   Enable or disable streaming access of Large Objects using locators. When enabled, access methods such as Clob.getCharacterStream() issue a single request to the DBMS to retrieve LOB data. No other requests can be made on the associated connection until all result data has been retrieved. When disabled, access methods issue individual requests for sequential blocks of LOB data, permitting other requests to be made on the associated connection while LOB data is being retrieved. Default is true.

**ingres.jdbc.metadata.pattern.underscore.enabled**

:   Enable or disable the underscore character, ‘_’, as a metadata pattern wildcard (true/false). Default is true.

**ingres.jdbc.prefetch.blocks**

:   The number of data blocks to be prefetched. By default, the rows that will fit in one communication data block are prefetched. When this property is set, the prefetch block count is multiplied by the default prefetch row count to determine the number of rows to be prefetched. Depending on the row size and unused space in the rows, the number of blocks retrieved may be different.

**ingres.jdbc.scroll.enabled**

:   Enable or disable scrollable result sets (true/false). If disabled, all result sets will be forward-only and an SQLWARNING will be generated if a scrollable result set is requested. Default is true.

**ingres.jdbc.sql.comment.doubledash.enabled**

:   Enable or disable removal of double dash ('--') comments in SQL text (true/false). Default is true.

**ingres.jdbc.trace.log**

:   Path and filename of the driver trace log. Default is no trace log.

**ingres.jdbc.trace.drv**

:   Driver trace level. Default is 0 (no tracing).

**ingres.jdbc.trace.ds**

:   DataSource trace level. Default is 0 (no tracing).

**ingres.jdbc.trace.msg**

:   Messaging system trace level. Default is 0 (no tracing).

**ingres.jdbc.trace.msg.tl**

:   Transport layer trace level. Default is 0 (no tracing).

**ingres.jdbc.trace.msg.nl**

:   Network layer trace level. Default is 0 (no tracing).

**ingres.jdbc.trace.timestamp**

:   Include timestamps in traces (true/false). Default is false.

### How the Driver Is Loaded

The JDBC Driver can be loaded by an application or applet by using one of these methods:

- Adding the driver class, com.ingres.jdbc.IngresDriver, to the JDBC DriverManager system property "jdbc.drivers"
- Adding the following Java statement to the application/applet prior to attempting to establish a connection using the JDBC Driver:

```
Class.forName( "com.ingres.jdbc.IngresDriver" ).newInstance();
```

Depending on the Java environment, calling the forName() method can be sufficient to load and initialize the JDBC Driver classes. Some environments, most notably older releases of Microsoft Internet Explorer, require the instantiation of a JDBC Driver object to fully initialize the driver.

While only one method is needed, both methods can be used without conflict.

### DriverManager.getConnection() Method--Establish JDBC Driver Connection

A JDBC Driver connection can be established using a DriverManager.getConnection() method with a URL in the following format:

- For JDBC Driver prior to 4.3.7:

```
jdbc:ingres://host:port{,port}{;host:port{,port}}/db{;attr=value}
```

- For JDBC Driver 4.3.7 or later:

```
jdbc:actian://host:port{,port}{;host:port{,port}}/db{;attr=value}
```

where:

**host**

:   Specifies the network name or address of the host on which the target Data Access Server (DAS) is running. TCP/IPv6 addresses (colon-hexadecimal format) must be enclosed in square brackets, for example: [::1]. Multiple hosts with associated ports must be separated by semi-colons.

**port**

:   Specifies the network port 27839.

**db**

:   Specifies the target database, db.

**attr=value**

:   (Optional) Specifies the attribute name and value pair. Multiple attribute pairs are separated by a semi-colon.

:   Attributes represent driver properties that are implementation-specific and can be used to configure the new connection. For details, see [JDBC Driver Properties](../Connectivity/JDBC_Driver_Interface.md).

!!! note "Note"

    A user ID and password are required when making remote connections. They can be included as parameters to the getConnection() method as driver properties or as URL attributes.

### Access to a Remote Instance

You can connect to remote databases using either a vnode or dynamic vnode.

!!! note "Note"

    Connections to Actian Data Platform typically use a dynamic vnode.
