---
title: "Understanding JDBC Connectivity"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Understanding_JDBC_Connectivity.htm"
canonical_id: "actian-data-platform-understanding-jdbc-connectivity"
---

# Understanding JDBC Connectivity

## JDBC Components

The Actian Data Platform JDBC consists of the following components:

- The JDBC Driver
- The JDBC Information Utility

The Actian Data Platform JDBC Driver is subsequently referred to as simply the JDBC Driver.

## JDBC Driver

The JDBC Driver is a pure Java implementation of the JDBC 4.2 API released with Oracle Java Platform SE 8. The driver supports application, applet, and servlet access to Actian Data Platform data sources through the Data Access Server.

The JDBC Driver supports the following JDBC features.

JDBC 4.2 features:

- Long (eight-byte) row counts – method variants with 'Large' in method name.
- Method variants that utilize the SQLType class.

- LocalDate, LocalTime, LocalDateTime, OffsetTime, OffsetDateTime classes.
- TIME_WITH_TIMEZONE and TIMESTAMP_WITH_TIMEZONE. Actian Data Platform supports corresponding types; the driver prior to 4.2 identified these types as TIME and TIMESTAMP types. For backward compatibility, the driver continues to identify the Actian Data Platform types as TIME/TIMESTAMP and return Time/Timestamp objects. The new types are supported as aliases for TIME and TIMESTAMP.

JDBC 4.1 features:

- Connection.abort()
- Connection.getNetworkTimeout() and Connection.setNetworkTimeout()

- DatabaseMetaData.generatedKeyAlwaysReturned()
- Statement.isCloseOnCompletion() and Statement.closeOnCompletion()

- CallableStatement.getObject( int, Class<T> ) and CallableStatement.getObject( String, Class<T> )
- ResultSet.getObject( int, Class<T> ) and ResultSet.getObject( String, Class<T> )

JDBC 4.0 features:

- Auto-loading of the driver
- National Character Set Support

- Support for java.sql.Wrapper Interface

JDBC 3.0 features:

- Updatable ResultSets
- Scrollable ResultSets

- Transaction savepoints
- Named procedure parameters

- Auto-generated keys
- Parameter metadata

The JDBC Driver is delivered as a single Java archive file, named iijdbc.jar, located in the library directory (lib) of the Actian Data Platform instance. Depending on the Java environment used, access to the driver requires adding the Java archive to the CLASSPATH environment setting or as a resource in the appropriate utility. For browser/applet access, the Java archive must be copied to the Web Server directories.

## JDBC Information Utility--Load the JDBC Driver

The JDBC Information Utility, JdbcInfo, loads the JDBC driver and displays its internal release information.

The class files for the JdbcInfo utility are located in the library directory (lib) of the locally installed Actian Data Platform Client Runtime Package. You must set your CLASSPATH environment (see [Set CLASSPATH Environment](../Connectivity/Understanding_JDBC_Connectivity.md)) before using the JdbcInfo utility.

You can invoke the JdbcInfo utility from the command line with these parameters:

**java JdbcInfo**

:   Displays the internal driver release of the JDBC Driver.

**java JdbcInfo url**

:   Attempts to establish a JDBC connection to the target database using the specified URL. For more information on formatting the URL, see [DriverManager.getConnection() Method--Establish JDBC Driver Connection](../Connectivity/JDBC_Driver_Interface.md). If successful, it displays the JDBC Driver name and release that serviced the URL connection.

**java JdbcInfo host port**

:   Attempts to establish a low-level connection to the Data Access Server associated with host port. If successful, it displays the internal driver release of the JDBC Driver.

The utility also supports ‑h (help) parameter to display the command line options.

### Driver Archive Interface

Starting with driver version 4.3.0, the driver Java archive, iijdbc.jar, supports an executable interface with features similar to the JDBC Information Utility. The driver archive interface can be executed with either of the following command lines:

```
java -jar iijdbc.jar [options]
```

```
java com.ingres.jdbc.IngresMain [options]
```

The driver archive supports the same operations as JdbcInfo when executed with no arguments, a URL, or host/port pair. In addition, the driver archive provides options for displaying driver configuration properties:

```
java com.ingres.jdbc.IngresMain -p
```

:   Outputs the driver configuration properties loaded by the driver.

```
java com.ingres.jdbc.IngresMain -P
```

:   Outputs system properties and the driver configuration properties loaded by the driver.

!!! note "Note"

    When executing the driver archive using the -jar java option, the normal CLASSPATH logical is not used. This results in the driver not being able to load the default driver property file. Be sure to execute the driver using the IngresMain class when using the property display options.

### Set CLASSPATH Environment

Before using the JdbcInfo utility to load the JDBC driver, you must set the CLASSPATH Java environment variable to point to the class files for the driver.

To set your CLASSPATH environment

Issue the following command:

Windows:

```
set CLASSPATH = %II_SYSTEM%\ingres\lib\iijdbc.jar;.;%II_SYSTEM%\ingres\lib ]
```

Linux (C shell):

```
setenv CLASSPATH  $II_SYSTEM\ingres\lib\iijdbc.jar:.:$II_SYSTEM\ingres\lib ]
```
