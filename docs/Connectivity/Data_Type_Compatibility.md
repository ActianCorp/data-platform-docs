---
title: "Data Type Compatibility"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Data_Type_Compatibility.htm"
canonical_id: "actian-data-platform-data-type-compatibility"
---

## Data Type Compatibility

With the exception of the data types listed in [Unsupported JDBC Features](../Connectivity/Unsupported_JDBC_Features.md), the JDBC Driver supports conversion of Actian Data Platform data values into Java/JDBC values as required by the JDBC specification.

Because Actian Data Platform does not support all the JDBC data types, the following conventions are used when sending Java/JDBC parameters to the DBMS:

**NULL**

:   Generally, NULL values sent to the DBMS are associated with the data type provided in the setNULL() or setObject() method call or the data type implied by the setXXX() method call. A generic or typeless NULL value can be sent to the DBMS using one of the following method calls:

```
setNull( idx, Types.NULL )  setObject( idx, null ) setObject( idx, null, Types.NULL )
```

**BOOLEAN**

:   Boolean values are sent to the DBMS as single byte integers with the value 0 or 1.

**BIGINT**

:   Long values are sent to the DBMS as DECIMAL (if supported by the DBMS) or DOUBLE values when BIGINT is not supported by the DBMS.

**DECIMAL**

:   BigDecimal values are sent as DOUBLE values when DECIMAL is not supported by the DBMS. Avoid using the BigDecimal constructor that takes a parameter of type double. This constructor can produce decimal values that exceed the scale/precision supported by Actian Data Platform.

**DATE**

:   For earlier versions of Ingres and Enterprise Access gateways in which ANSI datetime data types are not supported, Ingres supports a single date data type, which is used for DATE, TIME, and TIMESTAMP values. Ingres dates do support date without time values and this form is used for JDBC DATE values.

**TIME**

:   For earlier versions of Ingres and Enterprise Access gateways in which ANSI datetime data types are not supported, Ingres supports a single date data type that is used for DATE, TIME, and TIMESTAMP values. Ingres dates do not support date without time values. The JDBC Driver adds the JDBC date epoch 1970-01-01 to JDBC TIME values. The Ingres DBMS adds the current date to time-only values.

**CHAR**

:   Zero length CHAR values are sent as VARCHAR values. For conventions associated with NCS enabled databases, see [National Character Set Columns](../Connectivity/JDBC_Implementation_Considerations.md). For information on automatic conversion to LONGVARCHAR, see the end of this section.

**VARCHAR**

:   For conventions associated with NCS enabled databases, see [National Character Set Columns](../Connectivity/JDBC_Implementation_Considerations.md). For information on automatic conversion to LONGVARCHAR, see the end of this section.

**LONGVARCHAR**

:   The LONGVARCHAR type is used by the driver to represent Character and NCS Large Object values passed to the driver as data streams. For conventions associated with NCS enabled databases, see [National Character Set Columns](../Connectivity/JDBC_Implementation_Considerations.md).

**BINARY**

    Zero length BINARY values are sent as VARBINARY values.

**LONGVARBINARY**

:   The LONGVARBINARY type is used by the driver to represent Binary Large Object values passed to the driver as data streams.

In addition to the JDBC types listed above, the following conventions are used when certain Java data values are provided to the setObject() method:

**byte[]**

:   Byte arrays are sent by default as VARBINARY values.

**char[]**

:   While not required by JDBC, character arrays are supported by the JDBC Driver and are sent by default as CHAR values. For conventions associated with NCS enabled databases, see [National Character Set Columns](../Connectivity/JDBC_Implementation_Considerations.md). For information on automatic conversion to LONGVARCHAR, see the end of this section.

**String**

:   Strings are sent by default as VARCHAR values. For conventions associated with NCS enabled databases, see [National Character Set Columns](../Connectivity/JDBC_Implementation_Considerations.md). For information on automatic conversion to LONGVARCHAR, see the end of this section.

**InputStream**

:   While not required by JDBC, InputStream objects are supported by the JDBC Driver and are sent by default as LONGVARBINARY values.

**Reader**

:   While not required by JDBC, Reader objects are supported by the JDBC Driver and are sent by default as LONGVARCHAR values. For conventions associated with NCS enabled databases, see [National Character Set Columns](../Connectivity/JDBC_Implementation_Considerations.md).

    JDBC requires BINARY, VARBINARY, CHAR, and VARCHAR parameter values to be converted to LONGVARBINARY/LONGVARCHAR when their length exceeds some DBMS dependent maximum.

    The default maximum used by the JDBC Driver is 2000 bytes. This default maximum value can be incorrect for an Ingres database that has been configured with non-default page sizes and for EDBC or Enterprise Access gateways.

    The JDBC Driver uses the following entries in the iidbcapabilities system catalog to determine at runtime the appropriate size limits:

```
SQL_MAX_BYTE_COLUMN_LENSQL_MAX_VBYT_COLUMN_LENSQL_MAX_CHAR_COLUMN_LENSQL_MAX_VCHR_COLUMN_LEN
```

Not all releases of the Ingres DBMS, Actian Data Platform DBMS, EDBC, and Enterprise Access gateways have these entries in their iidbcapabilities system catalogs. These entries can be entered manually to provide accurate size information for the driver. Depending on the DBMS involved, special permissions are required to update the system catalog.
