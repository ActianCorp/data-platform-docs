---
title: "JDBC Tracing"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "JDBC_Tracing.htm"
canonical_id: "actian-data-platform-jdbc-tracing"
---

## JDBC Tracing

The JDBC Driver supports both DriverManager and DataSource tracing as documented in the JDBC 3.0 API specification. Trace information consists of JDBC API method entry and exit points with corresponding parameter and return values.

Enable internal JDBC Driver tracing by defining system properties on the java command line (-D flag) or by including the properties in the driver properties file.

DBMS trace messages are written to the internal trace log and can be directed to a separate trace log specified by a driver property.

These properties are supported:

| Property | Value | Description |
| --- | --- | --- |
| ingres.jdbc.trace.log | log | Path and file name of the JDBC Driver trace log |
| ingres.jdbc.trace.drv | 0–5 | Tracing level for the JDBC Driver |
| ingres.jdbc.trace.ds | 0–5 | Tracing level for the Ingres JDBC DataSources |
| ingres.jdbc.trace.msg | 0–5 | Tracing level for Messaging I/O |
| ingres.jdbc.trace.msg.tl | 0–5 | Tracing level for Transport Layer I/O |
| ingres.jdbc.trace.msg.nl | 0–5 | Tracing level for Network Layer I/O |
| ingres.jdbc.trace.timestamp | true | Include timestamp in trace log |
| ingres.jdbc.dbms.trace.log | log | Path and file name of the DBMS trace log |
| edbc.trace.log | log | Path and file name of the EDBC JDBC Driver trace log |
| edbc.trace.id | level | Tracing level for the EDBC JDBC Driver |
| edbc.trace.timestamp | true | Include timestamp in EDBC trace log |

Internal tracing is also enabled by the application using these JDBC Driver methods:

| Method | Parameters | Description |
| --- | --- | --- |
| setTraceLog(String) | log | Log file path and name |
| setTraceLevel(int) | level | Tracing level for ID 'drv' |
| setTraceLevel(String,int) | id, level | Trace ID and numeric tracing level |

Internal driver tracing permits separate tracing level settings for these trace IDs (id):

| Trace ID | Description |
| --- | --- |
| drv | General driver tracing |
| ds | Data source tracing |
| msg | General messaging IO tracing |
| msg.tl | IO tracing: transport layer |
| msg.nl | IO tracing: network layer |

## Tracing Levels

The tracing level determines the type of information that is logged. The following levels are currently defined:

1 – Errors and exceptions
2 – High level method invocation

3 – High level method details
4 – Low level method invocation

5 – Low level method details

## JDBC Driver Tracing Using Java Logging Package

JDBC Driver trace output can be configured to be logged using the Java Logging package (java.util.logging). The JDBC Driver uses the following Java logger objects to output driver trace messages:

**ingres.jdbc.trace.log**

:   Logger used to enable driver trace output via Java Logging and the logger used to output the driver traces. An explicit tracing level must be configured for this logger to enable trace output. Traces are written to this logger at the INFO level, so a logging level of INFO is sufficient to enable Java Logging output.

**ingres.jdbc.trace.drvingres.jdbc.trace.dsingres.jdbc.trace.msgingres.jdbc.trace.msg.tlingres.jdbc.trace.msg.nl**

:   Loggers used to configure the trace level for each of the associated components. Each logger must have an explicit tracing level assigned to enable trace output of the associated component. The Java Logging levels correspond to JDBC Driver trace levels as follows:

| Log Level | Trace Level |
| --- | --- |
| OFF | 0 (none) |
| INFO | 1 |
| FINE | 2 |
| FINER | 3 |
| FINEST | 4 |
| ALL | 5 |

If the system property ingres.jdbc.trace.log is defined, then driver tracing is written to the indicated log file and Java Logging is not used for trace output. If the system property ingres.jdbc.trace.log is not defined, then the Java Logger ingres.jdbc.trace.log is used if it is explicitly configured with a logging level of at least INFO.

Tracing levels are determined by the logging levels of the loggers associated with the various driver components. The tracing level determines which trace outputs are written to the logging system. Logging output is written to the ingres.jdbc.trace.log logger at the INFO level regardless of the configured tracing levels.

### DBMS Tracing Using Java Logging Package

DBMS trace output can be configured to be logged using the Java Logging package (java.util.logging). The JDBC Driver uses the following Java logger objects to output DBMS trace messages:

**ingres.jdbc.dbms.trace.log**

:   Logger used to enable DBMS trace output through Java Logging and the logger used to output the DBMS traces. An explicit tracing level must be configured for this logger to enable trace output. Traces are written to this logger at the INFO level, so a logging level of INFO is sufficient to enable Java Logging output.

If the system property ingres.jdbc.dbms.trace.log is defined, then DBMS tracing is written to the indicated log file and Java Logging is not used for trace output. If the system property ingres.jdbc.dbms.trace.log is not defined, then the Java Logger ingres.jdbc.dbms.trace.log is used if it is explicitly configured with a logging level of at least INFO. Logging output is written to the ingres.jdbc.dbms.trace.log at the INFO level.

### Example Logging Configuration

A simple logging configuration file to enable JDBC Driver and DBMS logging can use the following settings:

```
ingres.jdbc.trace.log.handlers = java.util.logging.ConsoleHandler
```

```
ingres.jdbc.trace.log.level = INFO
```

```
ingres.jdbc.trace.drv.level = FINER
```

```
ingres.jdbc.dbms.trace.log.handlers = java.util.logging.ConsoleHandler
```

```
ingres.jdbc.dbms.trace.log.level = INFO
```

If the settings shown above are placed in a file, logging.properties, then the following command line can be used to run a Java program, App, with driver tracing enabled at level 3, DBMS tracing enabled, and output sent to the Java system console:

```
java -Djava.util.logging.config.file=logging.properties App
```
