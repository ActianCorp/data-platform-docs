---
title: "Actian Data Platform Standard Catalogs"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Actian_Data_Platform_Standard_Catalogs.htm"
canonical_id: "actian-data-platform-actian-data-platform-standard-catalogs"
---

## Actian Data Platform Standard Catalogs

Actian Data Platform contains the following standard catalogs:

| iiaccess | iialt_columns | iiaudittables |
| --- | --- | --- |
| iicolumns | iiconstraint_indexes | iiconstraints |
| iidb_comments | iidb_subcomments | iidbcapabilities |
| iidbconstants | iidistcols | iidistschemes |
| iievents | iifile_info | iihistograms |
| iiindex_columns | iiindexes | iiingres_tables |
| iiintegrities | iikeys | iikey_columns |
| iilog_help | iilpartitions | iimulti_locations |
| iipermits | iiphysical_tables | iiprocedures |
| iiproc_access | iiproc_params | iirange |
| iiref_constraints | iiproc_rescols | iirules |
| iisecurity_alarms | iiregistrations | iisequences |
| iistats | iisession_privileges | iitables |
| iiviews | iisynonyms |  |

### iiaccess Catalog

The iiaccess catalog holds information about permissions on tables, views, and indexes.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | Name of the table, view, or index |
| table_owner | char(32) | Owner of the table, view, or index |
| table_type | char(1) | T – Base table  V – View  I – Index |
| system_use | char(1) | S – System catalog object  U – User object  G – Generated |
| permit_user | char(32) | Name of grantee or empty string |
| permit_type | char(49) | Privilege granted |

### iialt_columns Catalog

All columns defined as part of an alternate key have an entry in iialt_columns.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table |
| table_owner | char(32) | The name of the table owner |
| key_id | integer | The number of the alternate key for this table |
| column_name | char(256) | The name of the column |
| key_sequence | smallint | Sequence of column in the key, numbered from 1 |

### iiaudittables Catalog

The iiaudittables catalog provides a list of registered security audit log files for the database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the virtual security audit table |
| table_owner | char(32) | The name of the table owner as determined by the register table statement |
| audit_log | char(256) | The full file name specification of the underlying security audit log |
| register_date | char(25) | The date and time the audit table was registered |

### iicolumns Catalog

For each queriable object in the iitables catalog, there are one or more entries in the iicolumns catalog. Each row in iicolumns contains the information on a column of the object. Iicolumns is used by Actian Data Platform tools and user programs to perform dictionary operations and dynamic queries.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table. |
| table_owner | char(32) | The owner of the table. |
| column_name | char(256) | The name of the column |
| column_datatype | char(32) | The data type of the column |
| column_length | integer | The length of the column. Displays the precision for decimal data, zero for money and date |
| column_scale | integer | Displays the scale for decimal data type, zero for all other data types |
| column_collid | smallint | The column's collation ID. Valid values are:-1 The default  1 for unicode  2 for unicode_case_insensitive  3 for sql_character |
| column_nulls | char(1) | Y if the column can contain null values, N if the column cannot contain null values |
| column_defaults | char(1) | Y if the column has a default value when a row is inserted, N if not |
| column_sequence | integer | The position of the column based on the DDL for the object, starting at 1.For example, the first column in a CREATE statement displays 1 in this column. |
| key_sequence | integer | The order, numbered from 1, of this column in the primary key for a table. 0 if this column is not part of the primary key |
| sort_direction | char(1) | A for ascending; used when key_sequence is greater than 0 |
| column_ingdatatype | integer | Contains the internal numeric representation of the column's external data type.If the value is positive, the column is not nullable.  If the value is negative, the column is nullable.If the installation has user-defined data types (UDTs), this column contains the data type that the UDT is converted to when returned.The data types and their corresponding values are: |
|  |  | INTEGER | 30/-30 |
|  |  | FLOAT | 31/-31 |
|  |  | C | 32/-32 |
|  |  | TEXT | 37/-37 |
|  |  | INGRESDATE* | 3/-3 |
|  |  | DECIMAL | 10/-10 |
|  |  | MONEY | 5/-5 |
|  |  | CHAR | 20/-20 |
|  |  | VARCHAR | 21/-21 |
|  |  | LONG VARCHAR | 22/-22 |
|  |  | BYTE | 23/-23 |
|  |  | LONG BYTE | 25/-25 |
|  |  | TABLE_KEY | 12/-12 |
|  |  | OBJECT_KEY | 11/-11 |
|  |  | ANSIDATE | 4/-4 |
|  |  | TIME WITHOUT TIMEZONE | 6/-6 |
|  |  | TIME WITH TIMEZONE | 7/-7 |
|  |  | TIME | 8/-8 |
|  |  | TIMESTAMP WITHOUT TIMEZONE | 9/-9 |
|  |  | TIMESTAMP WITH TIMEZONE | 18/-18 |
|  |  | TIMESTAMP | 19/-19 |
|  |  | INTERVAL YEAR TO MONTH | 33/-33 |
|  |  | INTERVAL DAY TO SECOND | 34/-34 |
|  |  | BOOLEAN | 38/-38 |
|  |  | *Returned to applications as a string. |
| column_internal_  datatype | char(32) | The internal data type of the datatype column.If the installation has user-defined data types, this column contains the user-specified name. |
| column_internal_  length | integer | The internal length of the column.  0 if the data type is date or moneyDoes not include the null indicator byte for nullable columns or the 2-byte length specifier for varchar and text columns |
| column_internal_  ingtype | smallint | The numeric representation of the internal data type.See column_ingdatatype for a list of valid values.If the installation has user-defined data types, this column contains the user-specified data type number. |
| column_system_  maintained | char(1) | Y if system-maintained  N if not system-maintained |
| column_updateable | char(1) | Y if the column can be updated  N if the column cannot be updated  Blank if unknown |
| column_has_default | char(1) | Y if the column is defined with a default value,  N if the column is defined as not default,  U if the column is defined without a default  Blank if unknown |
| column_default_val | varchar(1501) | The value of the default if the column has one  Null if the default is not specified, NOT DEFAULT, or not knownIt contains surrounding and embedded quotes for character defaults, per ISO Entry SQL92 semantics. |
| security_audit_key | char(1) | Y if column is a security audit key  N if column is not a security audit key |
| column_always_ident | char(1) | Y if column is declared as GENERATED ALWAYS AS IDENTITY, N if not |
| column_bydefault_ident | char(1) | Y if column is declared as GENERATED BY DEFAULT AS IDENTITY, N if not |
| column_encrypted | char(1) | Y if the column is encrypted, N if not |
| column_encrypt_width | integer | The width of an encrypted column, including the data itself and encryption overhead. |
| column_encrypt_salt | char(1) | Y if salt (extra initialization bits) is included in the encryption, N if not. The default is Y for encrypted columns. |
| column_encrypt_crc | char(1) | Y if a data validation hash is included for encryption; for Ingres 10.0 this is always Y for encrypted columns. |
| column_has_mask | char(1) | Y if column data is masked, N if not |
| column_mask_value | varchar(1501) | The value of the column mask. |
| column_has_minmax | char(1) | Y if column has a min-max index, N if not |
| column_location | varchar(32) | The location of the column. |

### iiconstraint_indexes Catalog

The iiconstraint_indexes catalog contains information about constraint indexes.

| Column Name | Data Type | Description |
| --- | --- | --- |
| constraint_name | char(256) | The name of the constraint |
| schema_name | char(32) | The name of the schema |
| index_name | char(256) | The name of the index |

### iiconstraints Catalog

The iiconstraints catalog contains constraint information.

| Column Name | Data Type | Description |
| --- | --- | --- |
| constraint_name | char(256) | The name of the constraint |
| schema_name | char(32) | The name of the schema |
| table_name | char(256) | The name of the table |
| constraint_type | char(1) | The type of constraint:  U if Unique  P if Primary  C if Check  R if References  Blank |
| create_date | char(25) | The date the constraint was created |
| text_sequence | integer8 | The sequence number, from 1, for the text_segment |
| text_segment | varchar(240) | The text of the constraint definition |
| system_use | char(1) | U if the object is a user object  G if generated by the system for the user. A status of G is used for constraints or views with check option. |

### iidb_comments Catalog

The iidb_comments catalog contains table comments.

| Column Name | Data Type | Description |
| --- | --- | --- |
| object_name | char(256) | The name of the table, view or index |
| object_owner | char(32) | The owner of the table, view or index |
| object_type | char(1) | Always T |
| short_remark | char(60) | The text of the short remark  Blank if none |
| text_sequence | integer8 | Always 1; the sequence number of the long_remark |
| long_remark | varchar  (1600) | The text of the long remark  If none, a zero-length string |

### iidb_subcomments Catalog

The iidb_subcomments catalog contains column comments.

| Column Name | Data Type | Description |
| --- | --- | --- |
| object_name | char(256) | The name of the table, view or index |
| object_owner | char(32) | The owner of the table, view or index |
| subobject_name | char(256) | The name of the column |
| subobject_type | char(1) | Always C |
| short_remark | char(60) | The text of the short remark  Blank if none |
| text_sequence | integer8 | Always 1; the sequence number of the long_remark. |
| long_remark | varchar(1600) | The text of the long remark  If none, a zero-length string |

### iidbcapabilities Catalog

The iidbcapabilities catalog contains information about the capabilities provided by the DBMS.

| Column Name | Data Type | Description |
| --- | --- | --- |
| cap_capability | char(32) | Contains one of the values listed in the capability column of the table below. |
| cap_value | char(32) | The contents of this field depend on the capability; see the Value column in the table below. |

The cap_capability column contains one or more of the following values:

| Capability | Value |
| --- | --- |
| COMMON/SQL_LEVEL | Deprecated. Use OPEN/SQL_LEVEL |
| DB_DELIMITED_CASE | The case of delimited identifiers:LOWER for lowercase (Actian Data Platform setting)  MIXED for mixed case (ISO Entry SQL92 setting)If MIXED, an identifier must be enclosed in double quotes to maintain its original case; otherwise, it is converted to uppercase. |
| DB_NAME_CASE | The case of regular identifiers:LOWER for lowercase (Actian Data Platform setting)  UPPER for uppercase (ISO Entry SQL92 setting) |
| DB_REAL_USER_CASE | The case of user names as retrieved by the operating system.LOWER for lowercase (Actian Data Platform setting)  MIXED for mixed case  UPPER for uppercase |
| DBMS_TYPE | The type of DBMS the application is communicating with. Valid values are the same as those accepted by the WITH DBMS = clause.Examples:  INGRES (default)  INGRES_VECTORWISE  STAR  RMS |
| DISTRIBUTED | Y if the database is distributed  N if database is local |
| ESCAPE | Y if DBMS supports the ESCAPE clause of the LIKE predicate in the WHERE clause  N if ESCAPE is not supported |
| INGRES | Y if the DBMS supports all aspects of Release 6 and Ingres (the default)  N if not |
| INGRES/SQL_LEVEL | Version of SQL supported by the DBMSExamples:01020 Ingres 10.2  01100 Ingres 11.0  01110 Ingres 11.1  00000 DBMS does not support SQL |
| INGRES/QUEL_LEVEL | Version of QUEL supported by the DBMS |
| INGRES_RULES | Y if rules supported  N if rules not supported |
| INGRES_UDT | Y if user-defined data types supported  N if user-defined data types not supported |
| INGRES_AUTH_GROUP | Y if group identifiers supported  N if group identifiers not supported |
| INGRES_AUTH_ROLE | Y if role identifiers supported  N if role identifiers not supported |
| INGRES_LOGICAL_KEY | Y if logical keys supported  N if logical keys not supported |
| MAX_COLUMNS | Maximum number of columns allowed in a table. |
| MIXEDCASE_NAMES | Y if case is significant in object names.  N if ABC, Abc, and abc are all equivalent object names. |
| NATIONAL_CHARACTER_SET | Y if Unicode supported  N if Unicode not supported |
| OPEN_SQL_DATES | Absent if OpenSQL date data type is implicitly supported when accessing a standard DBMS server. |
| OPEN/SQL_LEVEL | Version of OpenSQL supported by the DBMSExamples:00860 Ingres 2.6  00902 Ingres r3  00904 Ingres 9.0**Note:**Use this name instead of the deprecated COMMON/SQL_LEVEL. |
| OWNER_NAME | schema.table format is supported with optional quotes.  The default is QUOTED. |
| PHYSICAL_SOURCE | T indicates that iitables contains physical table information.  P (a deprecated setting) indicates that only iiphysical_tables contains the physical table information.  T is the default and only current usage. |
| QUEL_LEVEL | Text version of QUEL support level. Example: II11.0.0 |
| SAVEPOINTS | Y if savepoints behave exactly as in Actian Data Platform (default)  N if not |
| SLAVE2PC | Indicates if the DBMS supports 2-phase commit slave protocol:Y for Release 6.3 and above  N for Star  If not present, Y is assumed. |
| SQL_MAX_NCHAR_COLUMN_LEN | Maximum number of characters for an NCHAR column |
| SQL_MAX_NVCHR_COLUMN_LEN | Maximum number of characters for an NVARCHAR column |
| SQL_LEVEL | Text version of SQL support level. |
| STANDARD_CATALOG_LEVEL | Release of the standard catalog interface supported by this database.Examples:  01000  01100  01110 |
| UNIQUE_KEY_REQ | Y if the database service requires that some or all tables have a unique key.  N or not present if the database service allows tables without unique keys. |
| SQL_MAX_BYTE_COLUMN_LEN | Maximum number of characters for a BYTE column |
| SQL_MAX_BYTE_LITERAL_LEN | Maximum number of characters for a BYTE LITERAL column |
| SQL_MAX_CHAR_COLUMN_LEN | Maximum number of characters for a CHAR column |
| SQL_MAX_CHAR_LITERAL_LEN | Maximum number of characters for a CHAR LITERAL column |
| SQL_MAX_COLUMN_NAME_LEN | Maximum number of characters for a column name |
| SQL_MAX_DECIMAL_PRECISION | Maximum decimal precision |
| SQL_MAX_PROCEDURE_NAME_LEN | Maximum number of characters for a procedure name |
| SQL_MAX_ROW_LEN | Maximum length of a row |
| SQL_MAX_SCHEMA_NAME_LEN | Maximum number of characters for a schema name |
| SQL_MAX_STATEMENTS | Maximum number of SQL statementsIf 0 unlimited |
| SQL_MAX_TABLE_NAME_LEN | Maximum number of characters for a table name |
| SQL_MAX_USER_NAME_LEN | Maximum number of characters for a user name - 32 |
| SQL_MAX_VBYT_COLUMN_LEN | Maximum number of characters for a VARBYTE column - 32000 |
| SQL_MAX_VCHR_COLUMN_LEN | Maximum number of characters for a VARCHAR column - 32000 |

### iidbconstants Catalog

The iidbconstants catalog contains values required by the Actian Data Platform tools.

| Column Name | Data Type | Description |
| --- | --- | --- |
| user_name | c(32) | The name of the current user |
| dba_name | c(32) | The name of the database owner |
| system_owner | varchar(32) | The name of the catalog owner ($ingres) |

### iidistcols Catalog

The iidistcols catalog describes the columns that generate partitioning values for a partitioned table. Each partitioned table has one row per partitioning column per dimension in iidistcols. (Dimensions that do not use a value-based partitioning scheme do not appear in iidistcols.)

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the partitioned table |
| table_owner | char(32) | The owner of the table |
| dimension | smallint | The dimension being described, counting from 1 |
| column_name | char(256) | The name of the partitioning column |
| column_sequence | smallint | The sequence of this column in this dimension's partitioning value, counting from 1 |
| column_datatype | char(32) | The data type of the column. |

### iidistschemes Catalog

The iidistschemes catalog describes the partitioning scheme of a partitioned table. Each partitioned table has one row per partitioning dimension in iidistschemes.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the partitioned table |
| table_owner | char(32) | The owner of the table |
| dimension | smallint | The dimension being described, counting from 1 |
| partitioning_columns | smallint | The number of columns that make up the partitioning value for a value-based partitioning rule |
| logical_partitions | smallint | The number of logical partitions in this dimension |
| partitioning_rule | varchar(9) | The partitioning rule:  AUTOMATIC  HASH |

### iievents Catalog

The iievents catalog provides information about database events.

| Column Name | Data Type | Description |
| --- | --- | --- |
| event_name | char(32) | The name of the event |
| event_owner | char(32) | The owner of the event |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text_segment | varchar(240) | The dbevent text definition |
| security_label | char(8) | Empty stringThis column is deprecated. |

### iihistograms Catalog

The iihistograms table contains histogram information.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The table for the histogram |
| table_owner | char(32) | The name of the owner |
| column_name | char(256) | The name of the column |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text_segment | char(228) | The encoded histogram data created by optimizedb |

### iiindex_columns Catalog

For indexes, any columns that are defined as part of the primary index key has an entry in iiindex_columns. For a full list of all columns in the index, use the iicolumns catalog.

| Column Name | Data Type | Description |
| --- | --- | --- |
| index_name | char(256) | The index containing column_name |
| index_owner | char(32) | The name of the index owner |
| column_name | char(256) | The name of the column |
| key_sequence | smallint | Sequence of column in the key, numbered from 1 |
| sort_direction | char(1) | Defaults to A for ascending |

### iiingres_tables Catalog

The iiingres_table catalog presents information about tables, views, and indexes in a different format than iitables.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table |
| table_owner | char(32) | The owner of the table |
| expire_date | char(25) | How long to save this table  A value of 1970_01_01 00:00:00 GMT indicates table never expires. |
| table_integrities | char(1) | Y if integrities exist on this table  N if not |
| table_permits | char(1) | Y if permits exist on this table  N if not |
| all_to_all | char(1) | Y if any user can perform any operation on this table  N if not |
| ret_to_all | char(1) | Y if any user can retrieve data from this table |
| row_width | integer | Maximum width of tuple in bytes |
| is_journalled | char(1) | N if not journaled  Y if journaled.  C if journaled started/stopped after next checkpoint |
| view_base | char(1) | Deprecated. Value set to N. |
| modify_date | char(25) | Date of last modify performed on the table  If never modified, the table creation date |
| table_ifillpct | smallint | Fill factor for B-tree index pages  Otherwise unused |
| table_dfillpct | smallint | Fill factor for data pages if table does not have HEAP structure |
| table_lfillpct | smallint | Fill factor for B-tree leaf pages |
| table_minpages | integer | Minimum number of hash buckets to use if modifying to HASH structure |
| table_maxpages | integer | Maximum number of hash buckets to use if modifying to HASH structure |
| location_name | char(32) | Name of first location for data files |
| table_reltid | integer | Reltid from iirelation |
| table_reltidx | integer | Reltidx from iirelation |

### iiintegrities Catalog

The iiintegrities catalog contains one or more entries for each integrity defined on a table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table |
| table_owner | char(32) | The owner of the table |
| create_date | char(25) | The creation date of the integrity |
| integrity_number | smallint | The number of the integrity |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text_segment | varchar(240) | The text of the integrity definition |

### iikeys Catalog

The iikeys catalog contains information about keys used in internal indexes to support unique constraints and referential integrities.

| Column Name | Data Type | Description |
| --- | --- | --- |
| constraint_name | char(256) | The name of the constraint |
| schema_name | char(32) | The name of the schema |
| table_name | char(256) | The name of the table |
| column_name | char(256) | The name of the column |
| key_position | smallint | A number indicating the key position |

### iikey_columns Catalog

The iikey_columns catalog presents information about the key columns for indexes and base tables not using a heap structure.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table key is on |
| table_owner | char(32) | The owner of the table |
| column_name | char(256) | Name of key component column |
| key_sequence | smallint | Position of column in key. 1 being the most significant component |
| sort_direction | varchar(1) | A: Ascending sort. (Currently only ascending indexes are supported.) |

### iilog_help Catalog

The iilog_help catalog presents information about table/view/index attributes (columns) in an alternate format to iicolumns.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | Name of the object column is part of |
| table_owner | char(32) | The owner of the object |
| create_date | char(25) | Date object was created |
| table_type | char(8) | T if attribute is part of a table  V if attribute is part of a view  I if attribute is part of an index |
| table_subtype | char(1) | Always N |
| table_version | char(5) | II9.0 for current release of product |
| system_use | char(1) | S if part of a system catalog  U if part of a user object |
| column_name | char(256) | Name of attribute. |
| column_datatype | char(32) | Long name of data type for this column |
| column_length | integer | Size in bytes of data |
| column_nulls | char(1) | N if not nullable  Y if column supports nulls |
| column_defaults | char(1) | N if no default for this column  Y if a default value exists for this column |
| column_sequence | smallint | Position of this column in table |
| key_sequence | smallint | Position in key for this table or zero |

### iilpartitions Catalog

The iilpartitions catalog describes each logical partition, and the partitioning values or range associated with that partition. Each logical partition of a partitioned table has at least one row in iilpartitions. Specifically, there is one row per column component for each partitioning value and for each logical partition in each dimension of the partitioned table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the partitioned table |
| table_owner | char(32) | The owner of the table |
| dimension | smallint | The dimension being described, counting from 1 |
| logical_partseq | smallint | The logical partition sequence number in its dimension, counting from 1 |
| partition_name | char(256) | The name of the partition  If no name is assigned in the partition definition, a name of the form iipartNN is used, where NN is a sequence number. |
| value_sequence | smallint | The partitioning value being described:RANGE then incremental from 1  LIST then incremental from 1  AUTOMATIC then one entry with a zero value_sequence  HASH then one entry with a zero value_sequence |
| column_sequence | smallint | The column component in the partitioning value:RANGE then incremental from 1  LIST then incremental from 1  AUTOMATIC then one entry with a zero column_sequence  HASH then one entry with a zero column_sequence |
| operator | varchar(7) | If the partitioning is based on:RANGE then <, <=, =, >=, >  LIST then =, DEFAULT  AUTOMATIC then blank  HASH then blank |
| value | varchar (1500) | If the partitioning is based on:RANGE then column value  LIST then column value (if DEFAULT, then meaningless)  AUTOMATIC then NULL  HASH then NULL |

Here is an example of using iilpartitions to view the partitioning values for a table:

```
select dimension,
```

```
       logical_partseq
```

```
       value_sequence
```

```
       column_sequence
```

```
       operator varchar(value,30)
```

```
from iilpartitions
```

```
where table_name = 'partitioned_table'
```

```
and table_owner = 'thedba'
```

```
order by dimension, logical_partseq, value_sequence, column_sequence;
```

### iimulti_locations Catalog

For tables located on multiple volumes, this table contains an entry for each additional location on which a table resides. The first location for a table can be found in the iitables catalog.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table |
| table_owner | char(32) | The owner of the table |
| loc_sequence | smallint | The sequence of this location in the list of locations specified in the modify command. Numbered from 1. |
| location_name | char(32) | The name of the location |

### iipermits Catalog

The iipermits catalog contains one or more entries for each permit defined against a table, view, or procedure.

| Column Name | Data Type | Description |
| --- | --- | --- |
| object_name | char(256) | The name of the table, view, or procedure |
| object_owner | char(32) | The owner of the table, view, or procedure |
| permit_grantor | char(32) | The name of the user granting the permit |
| object_type | char(1) | The type of the object:T if a table  P if a database procedure  E if an event  V if a view |
| create_date | char(25) | The creation date of the permit |
| permit_user | char(32) | The user name to which this permit applies |
| permit_depth | smallint | Indicates relative ordering distance of the permit holder from the object owner, as established in the grant with grant option statements |
| permit_number | smallint | The number of this permit |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text-segment | varchar(240) | The text of the permission definition |

### iiprocedures Catalog

The iiprocedures catalog contains one or more entries for each database procedure defined on a database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| procedure_name | char(256) | The name of the procedure |
| procedure_owner | char(32) | The owner of the procedure |
| create_date | char(25) | The creation date of the procedure |
| proc_subtype | varchar(1) | N if native |
| text_sequence | integer8 | The sequence number from 1 for the test_segment |
| text_segment | varchar(240) | The text of the procedure definition |
| system_use | char(1) | U if the object is a user object  G if generated by the system for the user |
| security_label | char(8) | An empty stringThis column is deprecated. |
| row_proc | char(1) | Y if the procedure is row producing  N if the procedure is not row producing |

### iiproc_access Catalog

The iiproc_access catalog contains information about database procedures.

| Column Name | Data Type | Description |
| --- | --- | --- |
| object_name | char(256) | Name of database procedure |
| object_owner | char(32) | Owner of database procedure |
| permit_grantor | char(32) | Grantor of privilege to this procedure |
| object_type | char(1) | Always P (database procedure) |
| create_date | char(25) | Procedure creation date |
| permit_user | char(32) | Name of the grantee |
| permit_depth | smallint | Depth of dependencies this procedure permission depends on |
| permit_number | smallint | Reserved for future usage |
| text_sequence | integer8 | Sequence number from 1 for the text segment |
| text_segment | varchar(240) | The text of the procedure definition |

### iiproc_params Catalog

The iiproc_params catalog contains information about procedure parameters.

| Column Name | Data Type | Description |
| --- | --- | --- |
| procedure_name | char(256) | Name of database procedure |
| procedure_owner | char(32) | Owner of database procedure |
| param_name | char(256) | Name of parameter |
| param_sequence | smallint | Which argument this parameter corresponds to (1 = first) |
| param_datatype | char(32) | Data type of parameter |
| param_datatype_code | smallint | Numeric representation of datatype.  See column_ing_datatype in iicolumns for these values. |
| param_length | integer | The column length  Displays the precision for decimal data type, zero for money and date |
| param_scale | integer | Displays the scale for decimal data type, zero for all other data types |
| param_nulls | char(1) | Y if this parameter is NULLable |
| param_defaults | char(1) | Y if this parameter has a default value |
| param_default_val | varchar(1501) | Default value used if default parameter provided |
| param_input | char(1) | Y if the corresponding procedure parameter is declared as IN in the database procedure definition |
| param_output | char(1) | Y if the corresponding procedure parameter is declared as OUT |
| param_inout | char(1) | Y if the corresponding procedure parameter is declared as INOUT |

### iiproc_rescols Catalog

The iiproc_rescols catalog is a standard interface catalog with information about the parameters and result columns of an Actian Data Platform database procedure. It has one row for each parameter, the same as the rows of iiproc_params. It also contains one row for each result column of a row producing procedure.

| Column Name | Data Type | Description |
| --- | --- | --- |
| procedure_name | char(256) | The name of the procedure |
| procedure_owner | char(32) | The owner of the procedure |
| rescol_name | char(256) | The name of the parameter/result column |
| rescol_sequence | smallint | Ordinal position of parameter or result column in procedure declaration |
| rescol_datatype | char(32) | Datatype of parameter/result column |
| rescol_datatype_code | smallint | Numeric representation of datatype |
| rescol_length | integer | Length of parameter/result column |
| rescol_scale | integer | The second number in a two-part user length specification; for type name (len1, len2) it is len2 |
| rescol_nulls | char(1) | Y indicates this parameter is null |
| rescol_param | char(1) | Y indicates this is a parameter  N indicates this is a result column |
| rescol_defaults | char(1) | Y indicates this parameter has a default value |
| rescol_default_val | varchar(1501) | Default value used if default parameter provided |

### iirange Catalog

The iirange catalog contains the range values for an rtree index.

| Column Name | Data Type | Description |
| --- | --- | --- |
| rng_baseid | integer | Identifier for the base table |
| rng_indexid | integer | Identifier for the rtree index table |
| rng_ll1 | float8 | Lower-left coordinate of range box for the first dimension |
| rng_ll2 | float8 | Lower-left coordinate of range box for the second dimension |
| rng_ll3 | float8 | Lower-left coordinate of range box for the third dimension. This column is currently not in use. |
| rng_ll4 | float8 | Lower-left coordinate of range box for the forth dimension. This column is currently not in use. |
| rng_ur1 | float8 | Upper-right coordinate of range box for the first dimension |
| rng_ur2 | float8 | Upper-right coordinate of range box for the second dimension |
| rng_ur3 | float8 | Upper-right coordinate of range box for the third dimension. This column is currently not in use. |
| rng_ur4 | float8 | Upper-right coordinate of range box for the forth dimension. This column is currently not in use. |
| rng_dimension | smallint | Dimension of range box  Currently, the value is 2. |
| rng_hilbertsize | smallint | The size of the hilbert function for the range |
| rng_rangedt | smallint | The data type of the range box, either box or ibox |
| rng_rangetype | char(1) | The data type of the range box's coordinates:I if integer  F if float |

### iiref_constraints Catalog

The iiref_constraints catalog contains information about referential constraints.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ref_constraint_name | char(256) | The name of the referential constraint |
| ref_schema_name | char(32) | The name of the schema on which the referential constraint applies |
| ref_table_name | char(256) | The name of the table on which the referential constraint applies |
| unique_constraint_name | char(256) | The name of the unique constraint |
| unique_schema_name | char(32) | The name of the schema on which the unique constraint applies |
| unique_table_name | char(256) | The name of the table on which the unique constraint applies |

### iiregistrations Catalog

The iiregistrations catalog contains the text of register statements used by Star.

| Column Name | Data Type | Description |
| --- | --- | --- |
| object_name | char(256) | The name of the registered table, view, or index |
| object_owner | char(32) | The name of the owner of the table, view, or index |
| object_dml | char(1) | The language used in the registration statement  S if SQL  Q if QUEL |
| object_type | char(2) | Object type:T if object is a table  V if a view  I if an index |
| object_subtype | char(1) | Describes the type of table or view created by the register statement:  L if this is a link for Star |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text_segment | varchar  (240) | The text of the register statement |

### iirules Catalog

The iirules catalog contains one row for each rule defined in a database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| rule_name | char(256) | The name of the rule |
| rule_owner | char(32) | The name of the person who defined the rule |
| table_name | char(256) | The name of the table that the rule was defined against |
| text_sequence | integer8 | The sequence number for the text segment |
| text_segment | varchar(240) | The text of the rule definition |
| system_use | char(1) | U if the object is a user object  G if generated by the system for the user; used for constraints or views with check option |

### iisecurity_alarms Catalog

The iisecurity_alarms catalog contains information about the security alarms created on tables in the database. This catalog is a view of security alarm information held in the system iiprotect table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| alarm_name | char(32) | The name of the security alarm |
| object_name | char(256) | The name of the table to which the security alarm applies |
| object_owner | char(32) | The owner of the security alarm |
| object_type | char(1) | The type of object to which the security alarm applies  Always T |
| create_date | char(25) | The date the security alarm was created |
| subject_type | char(1) | U if the security_user is a user  G if a group  R if a role  P if a public identifier |
| security_user | char(32) | The user to which the security alarm applies |
| security_number | smallint | The security alarm number |
| dbevent_name | char(32) | Database event associated with the alarm |
| dbevent_owner | char(32) | Owner of the database event |
| dbevent_text | char(256) | Text of the database event |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text_segment | varchar(240) | The text of the security alarm statement definition |

### iisession_privileges Catalog

The iisession_privileges catalog contains information about subject privilege statuses for the current session.

| Column Name | Data Type | Description |
| --- | --- | --- |
| priv_name | char(32) | The name of privilege |
| priv_access | char(32) | Y if privilege held  N if privilege not held |

### iisequences Catalog

The iisequences catalog contains information about all sequences defined in the database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| seq_name | char(256) | The name of the sequence |
| seq_owner | char(32) | The owner of the sequence |
| create_date | ingresdate | The date on which the sequence was created |
| modify_date | ingresdate | The date on which the sequence was last altered |
| data_type | varchar(7) | The data type of the sequence  integer  bigint  decimal |
| seq_length | smallint | The size in bytes of the sequence value |
| seq_precision | integer | The precision in decimal digits of the sequence value |
| start_value | decimal(31) | The start value (or restart value) of the sequence |
| increment_value | decimal(31) | The increment value of the sequence |
| next_value | decimal(31) | The next sequence value to be assigned |
| min_value | decimal(31) | The minimum value of the sequence |
| max_value | decimal(31) | The maximum value of the sequence |
| cache_size | integer | The number of cached sequence values |
| start_flag | char(1) | Y if start value was defined  N if start value was not defined |
| incr_flag | char(1) | Y if increment value was defined  N if increment value was not defined |
| min_flag | char(1) | Y if minimum value was defined  N if minimum value was not defined |
| max_flag | char(1) | Y if maximum value was defined  N if maximum value was not defined |
| restart_flag | char(1) | Y if restart value was defined  N if restart value was not defined |
| cache_flag | char(1) | Y if cache value was defined  N if cache value was not defined |
| cycle_flag | char(1) | Y if cycle was defined  N if cycle was not defined |
| order_flag | char(1) | Y if order was defined  N if order was not defined |
| seql_flag | char(1) | Y if sequential (not unordered) sequence  N if not sequential sequence |
| unordered_flag | char(1) | Y if unordered sequence  N if not unordered sequence |
| ident_flag | char(1) | Y if sequence associated with an identity column  N if not |

### iistats Catalog

Th iistats catalog contains entries for columns that have statistics.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table |
| table_owner | char(32) | The owner of the table |
| column_name | char(256) | The column name to which the statistics apply |
| create_date | char(25) | The date on which statistics were gathered |
| num_unique | float4 | The number of unique values in the column |
| rept_factor | float4 | The repetition factor |
| has_unique | char(1) | Y if the column has unique values  N if the column is not unique |
| pct_nulls | float4 | The percentage (fraction of 1.0) of the table that contains NULL for the column |
| num_cells | smallint | The number of cells in the histogram |
| column_domain | smallint | A user-specified number signifying the domain from which the column draws its values; default is 0 |
| is_complete | char(1) | Y if the column contains all possible values in the domain  N if the column does not contain all possible values in the domain |
| stat_version | char(8) | The version of the statistics for this column, for example, II9.0 |
| hist_data_length | smallint | The length of the histogram boundary values:  Either the specified length  Or length computed by optimizedb |

### iisynonyms Catalog

The iisynonyms catalog contains information about the synonyms.

| Column Name | Data Type | Description |
| --- | --- | --- |
| synonym_name | char(256) | The name of the synonym |
| synonym_owner | char(32) | The owner of the synonym |
| table_name | char(256) | The name of the table, view or index for which the synonym was created |
| table_owner | char(32) | The owner of the table, view, or index for which the synonym was created |

### iitables Catalog

The iitables catalog contains an entry for each table, view, or index in the database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the table |
| table_owner | char(32) | The owner of the table |
| create_date | char(25) | The creation date of the object  Blank if unknown |
| alter_date | char(25) | The last time this table was altered.  Updated when the structure of the table changes through changes to the columns in the table or to the primary key.  Physical changes to the table, such as changes to data or physical keys, do not change this date.  Blank if unknown. |
| table_type | char(1) | Type of the query object:T if table  V if view  I if index  P if physical partition of a partitioned tableFurther information about views can be found in iiviews. |
| table_subtype | char(1) | Specifies the type of table or view.N if native for standard Actian Data Platform databases  L if links for Star  Blank if unknown |
| table_version | varchar(11) | Version of the object; enables the Actian Data Platform tools to determine where additional information about this particular object is stored. This reflects the database type, as well as the version of an object in a given database. For Actian Data Platform tables, the value for this field is II9.0. |
| system_use | char(1) | S if the object is a system object  U if user object  G if generated by the system for the user  Blank if unknown |
| tups_per_page | integer | Maximum tuples per data page |
| keys_per_page | integer | Maximum keys per index page for ISAM and BTREE tables |
| keys_per_leaf | integer | Maximum keys per leaf for BTREE tables |

The following columns have values only if the table_type is T, I, or P.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_stats | char(1) | Y if the iistats table has entries  N if the iistats table does not have entries  Blank if query iistats to determine if statistics exist. |
| table_indexes | char(1) | Y if this object has entries in iiindexes that see this as a base table  N if this object does not have entries  Blank if query iiindexes on the base_table column |
| is_readonly | char(1) | N if updates are allowed  Y if no updates are allowed  Blank if unknownUsed for tables defined to Enterprise Access for retrieval only (such as tables in a hierarchical database).  If Y updates cannot occur, irrespective of the permissions set  If N updates are allowed depending on the permissions setting |
| concurrent_access | char(1) | Y if concurrent access is allowed |
| num_rows | integer | The estimated number of rows in the table  -1 if unknown  If value is for a partitioned table, this is the total for all partitions |
| storage_structure | char(16) | The storage structure of the table:  HEAP  X100  X100_ROW |
| is_compressed | char(1) | Y if the table is compressed  N if the table is uncompressed  Blank if unknown |
| key_is_compressed | char(1) | Y if the table uses key compression  N if no key compression  Blank if unknown |
| duplicate_rows | char(1) | D if the table allows duplicate rows  U if the table does not allow duplicate rows  Blank if unknown  The table storage structure (unique vs. non-unique keys) can override this setting. |
| unique_rule | char(1) | D if duplicate keys are allowed. (A unique alternate key exists in iialt_columns and any storage structure keys are listed in iicolumns.)U if the object is an Actian Data Platform object, indicates that the object has unique storage structure keys.If the object is not an Actian Data Platform object, it indicates that the object has a unique key, described in either iicolumns or iialt_columns.Blank if uniqueness is unknown or does not apply. |
| number_pages | integer | The estimated number of used pages in the table  -1 if unknown  If the value is for a partitioned table, this is the total for all partitions. |
| overflow_pages | integer | The estimated number of overflow pages in the table  -1 if unknown |
| partition_dimensions | smalliint | For a partitioned table, this is the number of dimensions (partitioning levels) in the table's partitioning scheme.  In all other cases, this is zero. |
| phys_partitions | smallint | For a partitioned table, this is the number of physical partitions.  For a physical partition, this is the partition number  In all other cases, this is zero. |
| row_width | integer | The size in bytes of the uncompressed binary value for a row of this query object. For encrypted tables, the width of the encrypted row. |

The following columns are used by Actian Data Platform, except for those preceded by an asterisk (*). Columns preceded by an asterisk (*) have values only if table_type is T or I.

| Column Name | Data Type | Description |
| --- | --- | --- |
| expire_date | integer | Expiration date of table |
| modify_date | char(25) | The date when the table was last modified  Blank if unknown or inapplicable |
| location_name | char(32) | The first location of the table.  If there are additional locations for a table, they are shown in the iimulti_locations table and multi_locations are set to Y. |
| table_integrities | char(1) | Y if this object has Actian Data Platform style integrities  Blank if query the iiintegrities table to determine if integrities exist |
| table_permits | char(1) | Y if this object has Actian Data Platform style permissions |
| all_to_all | char(1) | Y if this object has Actian Data Platform permit all to all  N if not |
| ret_to_all | char(1) | Y if this object has Actian Data Platform permit retrieve to all  N if not |
| is_journalled | char(1) | Y if journaling is enabled on this object  N if journaling is disabled on this object  C if journaling is enabled/disabled after the next online checkpoint |
| view_base | char(1) | Deprecated. Value set to N. |
| multi_locations | char(1) | Y if the table is in multiple locations  N if the table is single location |
| table_ifillpct | smallint | Fill factor, expressed as a percentage, for the index pages  Specified in modify command nonleaffill clause |
| table_dfillpct | smallint | Fill factor, expressed as a percentage, for the data pages  Specified in modify command fillfactor clause |
| table_lfillpct | smallint | Fill factor, expressed as a percentage, for the leaf pages  Specified in modify command leaffill clause |
| table_minpages | integer | Minpages parameter from the last execution of the modify command.  Used for hash structures only. |
| table_maxpages | integer | Maxpages parameter from the last execution of the modify command.  Used for hash structures only. |
| table_relstamp1 | integer | High part of last create or modify timestamp for the table |
| table_relstamp2 | integer | Low part of last create or modify timestamp for the table |
| table_reltid | integer | Reltid from iirelation |
| table_reltidx | integer | Reltidx from iirelation |
| * unique_scope | char(1) | R if this object is row-level  S if statement-level  Blank if not applicable |
| * allocation_size | integer | The allocation size, in pages. Set to -1 if unknown. |
| * extend_size | integer | The extend size, in pages  -1 if unknown |
| * allocated_pages | integer | The total number of pages allocated to the table |
| row_security_audit | char(1) | Y if row-level security auditing is enabled  N if not |
| table_pagesize | integer | Page size of a table |
| table_relversion | smallint | Version of table |
| table_reltotwid | integer | Width of the table, including all deleted columns. For encrypted tables, the width of the encrypted row. |
| table_reltcpri | smallint | Table's priority in the buffer cache  Values can be between 0 - 8:  Zero is the default.  1–8 can be specified in the priority clause of a create table or modify table statement. |
| label_granularity | char(1) | Empty stringThis column is deprecated. |
| security_label | char(8) | Empty stringThis column is deprecated. |
| table_reldatawid | integer | The size in bytes of the uncompressed binary value for a row of this query object (for encrypted tables, the width of the decrypted row) |
| table_reltotdatawid | integer | Width of the table, including all deleted columns (for encrypted tables, the width of the decrypted row) |
| encrypted_columns | char(1) | Y if the table contains encrypted columns  N if not |
| encryption_version | smallint | Internal version number of column encryption for the table (0 if there is no encryption) |
| encryption_type | varchar | Column encryption type (NONE, AES128, AES192, or AES256) |
| minmax_samples | char(1) | Y if the min-max index for the table is sampled.  N if not |

### iiviews Catalog

The iiviews catalog contains one or more rows for each view in the database.

| Column Name | Data Type | Description |
| --- | --- | --- |
| table_name | char(256) | The name of the view |
| table_owner | char(32) | The owner of the view |
| view_dml | char(1) | The language in which the view was created:  S if SQL  Q if QUEL |
| check_option | char(1) | Y if the check option was specified  N if not  Blank if unknown |
| text_sequence | integer8 | The sequence number from 1 for the text_segment |
| text_segment | varchar(240) | The text of the view definition |
