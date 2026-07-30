---
title: "Data Types Mapping"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Data_Types_Mapping.htm"
canonical_id: "actian-data-platform-data-types-mapping"
---

## Data Types Mapping

The .NET Data Provider defines its own enumeration of supported data types in addition to the standard System.Data.DbType enumeration.

The following table shows the mapping of the .NET Data Provider's data types to its .NET data type counterparts. For information on the typed accessors that a .NET application uses for an Ingres native database type to be obtained as a .NET type, see [IngresDataReader Class](../Connectivity/NET_Data_Provider_Classes.md).

| IngresType | Ingres  Data Type | Description | .NET Data Type |
| --- | --- | --- | --- |
| Binary | byte | Fixed length stream of binary data | Byte[ ] |
| Boolean | boolean | Boolean values of true and false | Boolean |
| Char | char | Fixed length stream of character data | String |
| Date | ansidate | Date data | DateTime |
| Time | time | Time data | DateTime |
| DateTime | timestamp | Date and time data | DateTime |
| IngresDate | ingresdate | Ingres format date | DateTime |
| IntervalYearToMonth | interval year to month | Interval year to month | String |
| IntervalDayToSecond | interval day to second | Interval day to second | TimeSpan |
| Decimal | decimal | Exact numeric data | Decimal |
| Double | double precision (float8) | Approximate numeric data | Double |
| SmallInt | smallint | Signed 16-bit integer data | Int16 |
| TinyInt | integer1 | Signed 8-bit integer data | SByte |
| Int | integer | Signed 32-bit integer data | Int32 |
| BigInt | bigint | Signed 64-bit integer data | Int64 |
| LongVarBinary | long byte | Binary large object | Byte[ ] |
| LongVarChar | long varchar | Character large object | String |
| LongNVarChar | long nvarchar | Unicode large object | String |
| NChar | nchar | Fixed length stream of Unicode data | String |
| NVarChar | nvarchar | Variable length stream of Unicode data | String |
| Real | real (float4) | Approximate numeric data | Single |
| VarBinary | byte varying | Variable length stream of binary data | Byte[ ] |
| VarChar | varchar | Variable length stream of character data | String |

**Notes:**

- DateTime literals within SQL CommandText must be specified in the form of {d 'yyyy-mm-dd'} for dates and {ts 'yyyy-mm-dd hh-mm-ss'} for timestamps. However, it is preferable to pass .NET DateTime parameters rather than literals for these values.
- For Ingres servers, DateTime parameters are converted to UTC values before being sent to the Ingres servers. DateTime values retrieved from Ingres servers are converted from UTC values to Local values. For non-Ingres servers, DateTime values are passed between the data provider and servers unchanged.

- IngresType.DateTime parameter data is sent by the data provider depending on the level of support of the ANSI datetime data types. You can override the default behavior by specifying the IngresType.IngresDate data type for the parameter data rather than IngresType.DateTime. IngresType.IngresDate parameter data type forces the data provider to send the datetime parameter data as INGRESDATE type and value. For more information, see [SendIngresDates Connection Keyword](../Connectivity/NET_Data_Provider_Classes.md).

## DbType Mapping

.NET’s System.Data.DbType for a parameter is mapped to the IngresType data type as follows:

| DbType | IngresType |
| --- | --- |
| AnsiString | VarChar |
| AnsiStringFixedLength | Char |
| Binary | VarBinary |
| Boolean | Boolean |
| Byte | Binary, if supported by the database; otherwise, Char |
| Currency | Decimal |
| Date | DateTime |
| DateTime | DateTime |
| Decimal | Decimal |
| Double | Double |
| Guid | Not supported |
| Int16 | SmallInt |
| Int32 | Int |
| Int64 | Decimal |
| Object | Not supported |
| SByte | TinyInt, if supported by the database; otherwise, SmallInt |
| Single | Real |
| String | NVarChar , if supported by the database; otherwise, VarChar |
| StringFixedLength | NChar, if supported by the database; otherwise, Char |
| Time | DateTime |
| UInt16 | Int |
| UInt32 | Decimal |
| UInt64 | Decimal |
| VarNumeric | Decimal |

## Coercion of Unicode Strings

.NET strings are Unicode based. If the application is sending a Unicode string as a parameter to a database field that is ASCII char or varchar, the application can direct the data provider to coerce the Unicode string to an ASCII string on the client side by setting the IngresParameter’s DbType property to DbType.AnsiString or the IngresType property to IngresType.VarChar.

The following is an example of coercing a Unicode string:

```
IngresCommand cmd = new IngresCommand(
```

```
    "select name from personnel where ssn = ?",    conn);IngresParameter parm =    new IngresParameter("SSN", IngresType.VarChar);parm.Value = strSSN;cmd.Parameters.Add(parm);
```
