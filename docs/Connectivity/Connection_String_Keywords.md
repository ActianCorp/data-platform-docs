---
title: "Connection String Keywords"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Connection_String_Keywords.htm"
canonical_id: "actian-data-platform-connection-string-keywords"
---

## Connection String Keywords

If your application requires a connection string to connect to a data source, you must specify the data source name. Optionally, you can specify attribute=value pairs to override certain data source and vnode definitions. The ODBC function SQLDriverConnect() or SQLDriverConnectW() is required for connection strings.

The connection string has the form:

```
DSN=data_source_name[;attribute=value[;attribute=value]...]
```

Alternatively, you can bypass data source definitions entirely if you include sufficient information in the connection string. The minimum attributes in this case are the SERVER, SERVERTYPE, and DATABASE attribute=value pairs.

Connection strings that bypass the DSN definition have the form:

```
CONNECTSTR=SERVER=server_name; SERVERTYPE=server_type; DATABASE=database;[attribute=value]...]
```

The following table provides the keywords for each connection string attribute.

| Keyword | Attribute Value Description |
| --- | --- |
| DSN | Data source name. |
| DRIVER | Driver description as returned by SQLDrivers(). |
| UID | User ID to override vnode definition. |
| PWD | Password to override vnode definition. If specified, UID must also be specified. |
| DBMS_PWD | Database password. Database passwords are defined by the [CREATE USER](../SQLLanguage/CREATE_USER.md) statement.Although supported as a connection string attribute, DBMS_PWD is not supported as a DSN configuration attribute. |
| SERVER | Vnode name. |
| SERVERTYPE | Server type (for example, INGRES, IDMS, or DB2). |
| DATABASE | Database name as defined on the server. |
| DB | A synonym for DATABASE. |
| ROLENAME | Role name to override vnode definition. |
| ROLEPWD | Role password to override vnode definition. |
| GROUP | Group identifier for the session. Equivalent to the -G flag of the Ingres command-line flags. |
| BLANKDATE | =NULL  Indicates that the driver must return empty string DATE values as NULL. |
| DATEALIAS | Specifies the data type of columns created using the alias keyword DATE. Valid values are: ANSIDATE or INGRESDATE. The attribute can be left unset. Default value is unset.This setting overrides the date_alias setting in config.dat. If left unset, the date_alias setting in config.dat is used. If neither the ODBC nor config.dat specify a date alias, the default is INGRESDATE. |
| SENDDATETIMEASINGRESDATE | Specifies whether to send datetime values as INGRESDATE data type. Valid values are:false – Send values as ANSI TIMESTAMP WITH TIMEZONE typetrue – Send values as INGRESDATE typeunset – Implicitly send ANSIDATE or INGRESDATE, depending on the DATEALIAS property: If DATEALIAS property is set to ANSIDATE, uses a value of false; otherwise uses a value of true. Unlike DATEALIAS, this property affects the way parameter data is handled. |
| DATE1582 | =NULL  Indicates that the driver must return values of ‘1582-01-01’ as NULL. |
| DATE | Same as DATE1582 keyword. |
| SELECTLOOPS | =N  Indicates that Cursor Loops must be used. |
| CATCONNECT | =Y  Indicates that a second separate Ingres session must be used for catalog functions (SQLTables, and so on). |
| NUMERIC_ OVERFLOW | =IGNORE  Indicates that no error is issued if an arithmetic error of numeric overflow, underflow, or divide by zero occur.  Equivalent to “-numeric_overflow=ignore” command line flag. |
| CATSCHEMANULL | =Y  Returns NULL for schema names from ODBC catalog functions. |
| CONVERTINT8TOINT4 | =Y  Coerces eight-byte (i8) integer values from the DBMS to four-byte (i4). |
| ALLOWUPDATE | =Y  Allows updates on sessions set to read-only. |
| DEFAULTTOCHAR | =Y  Treats Unicode strings as “standard” (multi-byte) strings. |
| MULTIBYTEFILLCHAR | =cDisplays the specified character (c) for each character that fails to convert from Unicode. This option is for applications that display Unicode data as multi-byte.This attribute can be specified if no ODBC DSN is defined or to override the "Fill character for failed Unicode/multibyte conversions" setting in the ODBC DSN. |
| DISABLEUNDERSCORE | =Y  Disables underscore wildcard search characters in catalog function. |
| IDENTIFIERDELIMITER | =BRACKETAllows brackets [ ] (and double quotes, the default) as identifier delimiters. |
