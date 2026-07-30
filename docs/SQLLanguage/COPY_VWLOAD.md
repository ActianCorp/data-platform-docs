---
title: "COPY VWLOAD"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "COPY_VWLOAD.htm"
canonical_id: "actian-data-platform-copy-vwload"
---

## COPY VWLOAD

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, Query Editor

The COPY...VWLOAD statement copies the contents of a file to a table using the VWLOAD operator. This operation is similar to using vwload -c on the command line, except that the load is done from within a multi-statement transaction instead of in a separate session.

For differences between COPY VWLOAD and INSERT INTO EXTERNAL CSV syntax, see [Required COPY VWLOAD Options to Load Data Written with INSERT INTO EXTERNAL CSV](../DataLoading/ExportingImportingData.md).

This statement has the following format:

```
COPY tablename() VWLOAD FROM 'datafile', ... WITH option{, option}
```

**tablename()**

:   Specifies the name of the table to be loaded. The column list is empty and not supported.

**'datafile'**

:   Specifies names of one or more files on supported systems (see below), using full or relative paths, that contain the data to be loaded. File names are specified as a comma-separated list from one to many. An entry can be a file name, a file name with an asterisk as a wildcard, or a directory. If you specify a directory, all files in the directory are loaded. Valid use of wildcards in file names are: *, abc*, *abc, abc*def, *abc*.

:   File systems supported: abfs, gs, s3a, public HTTPS. COPY VWLOAD does not work for local files located on a desktop or behind a firewall. For more information about loading data files from a local system, see [Data Load](../DataLoading/Data_Load.md).

**WITH option{, option}**

:   Specifies any WITH clause options:

ATTRIBUTES='col1, col2, col3,...'

:   Specifies a list of columns to load. An empty col name indicates an input field that is to be ignored.

:   Default: All columns are loaded if no attributes argument is specified.

AUTO_DETECT_COMPRESSION

:   Detects GZ and ZIP files. Compressed files are automatically detected by the file contents, not by the file suffix. If you are loading from a directory or using a file name wildcard, you can mix regular text files, GZ, and ZIP.

AWS_ACCESS_KEY='my_access_key'

:   Specifies the access key ID to access your S3 bucket on Amazon Web Services.

AWS_REGION='aws_region_name'

:   Specifies the region where the source data resides in your S3 bucket on Amazon Web Services.

!!! note "Note"

    If you do not specify the AWS region, your COPY VWLOAD will fail.

AWS_SECRET_KEY='my_secret_key'

:   Specifies the secret access key used to access to your S3 bucket on Amazon Web Services.

AZURE_CLIENT_ENDPOINT='https://login.microsoftonline.com/tenant_id/oauth2/token'

:   Specifies the Directory (tenant) ID used to access your Azure Storage account.

AZURE_CLIENT_ID = 'client_id'

:   Specifies the Application (client) ID used to access your Azure Storage account.

AZURE_CLIENT_SECRET = 'client_secret'

:   Specifies the Client Secret (password) used to access your Azure Storage account.

GCS_EMAIL='name@mail.com'

:   Specifies the email used for the service account used for Google Cloud Storage access.

GCS_PRIVATE_KEY_ID='xxxx'

:   Specifies the ID of the private key for the service account used for Google Cloud Storage access. For information about keeping your credentials safe, see the Security Guide.

GCS_PRIVATE_KEY='-----BEGIN PRIVATE KEY-----\n<long_key>\n-----END PRIVATE KEY-----\n'

:   Specifies the private key for the service account used for Google Cloud Storage access in PKCS#8 format. The key must include the starting and ending characters: -----BEGIN PRIVATE KEY----- and -----END PRIVATE KEY-----. For example:

```
-----BEGIN PRIVATE KEY-----MIIEvAIBADANBgkqhkiG9w0BgSiAgEAAoIBAQDHd1HNub/lfF41 ... jm+177ZXFg+QIyXFCqbMDTAnjYY3-----END PRIVATE KEY-----
```

:   For information about keeping your credentials safe, see the Security Guide.

**Note:**For details regarding service account key files, see[https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).

CHARSET='charset'

:   Specifies the input character set (see [VWLOAD Supported Character Sets](../SQLLanguage/COPY_VWLOAD.md)).

:   Default: no conversion

DATEFORMAT='col1=format1,col2=format2,...'

:   Sets date format for the column.

:   When no column is indicated, the format applies to all columns that are not otherwise set. That format must be defined last, without any assignment operation.

:   Valid values for format are described in [VWLOAD Date Format Settings](../SQLLanguage/COPY_VWLOAD.md).

:   Alternatively, a custom format string can be specified by starting the format with a '+' sign followed by the format string. The format string can consist of any of the format specifier characters used on the DATE_FORMAT function, described in this guide.

:   To be able to use any character in the format string (including for example, "," and "="), you must quote the format string in the same way that you would quote a delimited identifier on the command line (for example: 'ColX="+%M,%Y,%d",ColY=US'). For more information about delimited identifiers, see [Regular and Delimited Identifiers](../SQLLanguage/Regular_and_Delimited_Identifiers.md).

:   Default: US

:   Examples:

```
WITH DATEFORMAT='col1=+'%d-%b-%y' WITH DATEFORMAT='Col1=US,Col2=+%M %Y %d'
```

    Define US date format for columns a2_us, a4_us and GERMAN for all other columns (a1_multi, a3_de, a5_de):

```
WITH ATTRIBUTES='a1_multi,a2_us,a3_de,a4_us,a5_de', FDELIM=',', DATEFORMAT='a2_us=US,a4_us=US,GERMAN';
```

    or, which accomplishes the same:

```
WITH ATTRIBUTES='a1_multi,a2_us,a3_de,a4_us,a5_de', FDELIM=',', DATEFORMAT='a1_multi=GERMAN,a3_de=GERMAN,a5_de=GERMAN,US';
```

ERRCOUNT=n

:   Terminates after the first n errors in all input files. Default: 0 (do not terminate).

ESCAPE='escape_character'

:   Specifies the escape character to use. This allows escaping of single characters to allow a delimiter character to be part of a field (for example: \) or to allow a quote character to be part of a quoted string.

:   The argument must be a single ASCII character or an empty string. If the argument is an empty string, this functionality is disabled. To specify a control character, use an escape sequence (see [VWLOAD Escape Sequences](../SQLLanguage/COPY_VWLOAD.md)).

:   Default: none

ESCAPES

:   Interprets data escape sequences.

FDELIM='field_delimiter'

:   Specifies field delimiter to use. The delimiter must be a single character. To specify a control character, use an escape sequence (see [VWLOAD Escape Sequences](../SQLLanguage/COPY_VWLOAD.md)).

:   Default: "|"

HEADER

:   Skips header line in files.

IGNFIRST

:   Ignores the first field.

IGNLAST

:   Ignores the last field.

INSERTMODE=

:   Specifies the mode to use for inserts and merges. Valid modes are:

ROW

:   Inserts through the PDT (allows concurrent inserts)

BULK

:   Appends directly to disk (does not allow concurrent inserts)

LOG='dir'

:   Logs rejected rows and corresponding errors to the specified file. The file is created by the operation.

NONCHAR_LEADING_SPACES_NULL

:   When -nullvalue is used, data may contain spaces in front of the null identifiers. This option applies to non-character columns only. For example, if -nullvalue NADA is specified, -nonchar_leading_spaces_null will interpret a DATE column containing “NADA” or “ NADA” as NULL.

NOTNULL_EMPTY

:   Keeps empty strings. Does not consider the input value NULL if it is empty (that is, contains two consecutive field delimiters). For VARCHAR, the value becomes an empty string; for CHAR the value becomes blanks. This option applies only to CHAR, NCHAR, VARCHAR, and NVARCHAR columns that are NOT NULL.

NULLVALUE='null_value'

:   Defines the string that identifies NULL values.

:   Default: ' '

QUOTE='quote_character'

:   Specifies the quote character(s) to use. This allows the input to contain quoted fields (for example "Doe, John"), which may contain field or record delimiter characters. To include a quote character inside a quoted field, enter it twice in the input—for example: "The ""BIG"" Boss". When using distinct open and close quote characters, enter only the close quote character twice—for example: [The [BIG]] Boss].

:   The argument must be one or two ASCII characters or an empty string.

:   If the argument is an empty string, this functionality is disabled. If the argument is two characters, the first character is used as the opening quote character, and the second as the closing quote character. For example, specify "[]" to allow [quoted string].

:   To specify a control character, use an escape sequence (see [VWLOAD Escape Sequences](../SQLLanguage/COPY_VWLOAD.md)).

:   Default: none

RDELIM='record_delimiter'

:   Specifies record delimiter to use. The delimiter must be a single character. To specify a control character, use an escape sequence (see [VWLOAD Escape Sequences](../SQLLanguage/COPY_VWLOAD.md)).

:   Default: "\n"

ROLLBACK=

:   Turns “roll back on error” on or off.

ON

:   (Default) Rolls back on error.

OFF

:   Does not roll back the load transaction when errors were encountered, causing partial data to be loaded.

STRICTNULLS

:   Uses strict NULL value checking. This distinguishes between plain and quoted or escaped occurrences of a NULL representation. For example, NULL is a NULL value, whereas “NULL” is a 4-character string value. By default, VWLOAD does not make this distinction. This option allows proper loading of some data generated by MySQL and PostgreSQL.

SUBSTITUTE='substitute_character'

:   Substitutes the specified character for any invalid input character during character set conversion. When no substitute character is provided, an invalid input character is considered an error condition. Specifying a substitute character allows records that contain invalid characters to be loaded successfully.

:   The argument must be a single Unicode character or an empty string. If the argument is an empty string, the functionality is disabled.

:   To specify a control character or Unicode code point that cannot easily be typed on the keyboard, use an escape sequence (see [VWLOAD Escape Sequences](../SQLLanguage/COPY_VWLOAD.md)).

TEXTMODE

:   Opens input files in text mode and does not perform newline conversion. On Linux, this may gain a 5 to 10 percent performance improvement. On Windows, there is no known advantage to using this option. (By default, VWLOAD opens files in binary mode and performs automatic newline conversion, transparently handling text formats of various operating systems.)

**Note:**When using -T on Windows, any ^Z (ASCII SUB) character in the input is interpreted as End-Of-File by the Windows library, and causes VWLOAD not to see any data following the first such character.

## COPY VWLOAD Examples

1. Bulk load the data from multiple files into the mytable table. Columns in the data file are delimited with a vertical bar, records are delimited by a new line, and null values are identified as NULL:

```
COPY mytable() VWLOAD FROM 'abfs://loadtest@avalanchetest.dfs.core.windows.net/path/to/data/mytable_1.txt', 'abfs://loadtest@avalanchetest.dfs.core.windows.net/path/to/data/mytable_2.txt' WITH INSERTMODE=BULK, FDELIM='|', RDELIM='\n', NULLVALUE='NULL';
```

2. Load data from multiple files residing in Azure Data Lake Storage into the lineitem table.

```
COPY lineitem() VWLOAD FROM   'abfs://loadtest@avalanchetest.dfs.core.windows.net/firstfolder/lineitem10.tbl',   'abfs://loadtest@avalanchetest.dfs.core.windows.net/firstfolder/lineitem10_2.tbl',   'abfs://loadtest@avalanchetest.dfs.core.windows.net/firstfolder/lineitem10_3.tbl',   'abfs://loadtest@avalanchetest.dfs.core.windows.net/firstfolder/lineitem10_4.tbl',   'abfs://loadtest@avalanchetest.dfs.core.windows.net/firstfolder/lineitem10_5.tbl',   'abfs://loadtest@avalanchetest.dfs.core.windows.net/firstfolder/lineitem10_6.tbl'WITH    AZURE_CLIENT_ENDPOINT = 'https://login.microsoftonline.com/TENANT_ID/oauth2/token',   AZURE_CLIENT_ID = 'CLIENT_ID',   AZURE_CLIENT_SECRET = 'CLIENT_SECRET'
```

3. Load specific columns from a CSV file into the mytable table. Fields in the data file are delimited with a comma. Set the date format for columns a2_us and a4_us to US, and for all other columns to GERMAN.

```
COPY mytable() VWLOAD FROM 'abfs://loadtest@avalanchetest.dfs.core.windows.net/path/to/data/5255.csv' WITH ATTRIBUTES='a1_multi,a2_us,a3_de,a4_us,a5_de', FDELIM=',', DATEFORMAT='a2_us=US,a4_us=US,GERMAN';
```

4. Load data from files residing in Google Cloud Storage into the lineitem table:

```
COPY lineitem() VWLOAD FROM
```

```
   'gs://vector-gs-loadtest/data/lineitem*.tbl'
```

```
WITH
```

```
   GCS_EMAIL = 'jane.doe@acme.com',
```

```
   GCS_PRIVATE_KEY_ID = '1234',
```

```
   GCS_PRIVATE_KEY = '-----BEGIN PRIVATE KEY-----\n ... ==\n-----END PRIVATE KEY-----\n'
```

## VWLOAD Escape Sequences

To specify control characters in the VWLOAD command, you must use an escape sequence. An escape sequence is initiated by a '\' character. Valid escape sequences are:

| Escape Sequence | Description |
| --- | --- |
| \a | Bell (alert) |
| \b | Back space |
| \f | Form feed |
| \n | Newline |
| \r | Carriage return |
| \t | Tab |
| \v | Vertical tab |
| \nnn | The character with octal code value nnn |
| \uxxxx | The 2-byte Unicode code point with hexadecimal value xxxx |
| \\ | \ character |

!!! note "Note"

    Certain special characters, such as \, ", ', and |, must be protected from interpretation by the command shell by using the appropriate quoting and escaping mechanisms provided by the shell.

## VWLOAD Date Format Settings

The ‑‑dateformat format| attr=format option on the vwload command sets the date format for the attribute (column).

Valid settings for formatare:

| Setting | Valid Input Formats | Output Format |
| --- | --- | --- |
| US (default) | mm/dd/yy  mm-dd-yy  mmddyy  mm/dd/yyyy  mm-dd-yyyy  mmddyyyy  dd-mmm-yyyy  dd mmm yyyy  yyyy-mm-dd  yyyy.mm.dd  yyyy_mm_dd  mm-dd  mm/ddam and pm format in timestamp. Only hours between 1 and 12 are valid.  am and pm must be in lowercase. | dd-mmm-yyyy |
| MULTINATIONAL | yyyy-mm-dd  mm-dd-yy  mmddyy  mmddyyyy  dd/mm/yy  dd/mm/yyyy  dd mmm yyyyAll US formats except mm/dd/yyyy and mm/dd/yy | dd/mm/yy |
| MULTINATIONAL4 | yyyy-mm-dd  dd/mm/yy  dd/mm/yyyy  dd mmm yyyy  mm-dd-yy  mmddyy  mmddyyyyAll US formats except mm/dd/yyyy and mm/dd/yy | dd/mm/yyyy |
| ISO | yyyy-mm-dd  yyyymmdd  yymmdd  ymmdd  mmdd  mdd  dd mmm yyyyAll US input formats except mmddyy | yymmdd |
| ISO8601 | All ISO input formats | yyyy-dd-mmThh:mm:ssZwhere hh is in 24-hour format and Z indicates Zulu (UTC) timezone |
| ISO4 | yyyy-mm-dd  yyyymmdd  yymmdd  ymmdd  mmdd  mdd  dd mmm yyyyAll US input formats except mmddyy | yyyymmdd |
| ISO4T | All ISO4 input formats.If the prefix "T" is used then the absolute time component can use the input format hhmmss as well as the standard hh:mm:ss. For example:Acceptable: yyyymmddThhmmss, yyyymmddThh:mm:ss, and yyyymmdd hh:mm:ssNot acceptable:yyyymmdd hhmmssAcceptable:'Thhmmss', 'Thh:mm:ss' and 'hh:mm:ss'Not acceptable:'hhmmss'This is the only case where an absolute time can be entered in format hhmmss instead of hh:mm:ss. To avoid ambiguity, a time field entered in hhmmss format must be 6 characters long. | yyyymmddISO4 output format, unless the date includes a time, in which case the format is: yyyymmddThhmmss |
| ISO4TC | See description under ISO4T. | ISO4 output format, unless the date includes a time, in which case the format is:yyyymmddThh:mm:ss |
| SWEDEN or FINLAND | yyyy-mm-dd  yy-mm-dd  mmddyy  dd mmm yyyyAll US input formats  exceptmm-dd-yyyy | yyyy-mm-dd |
| GERMAN | yyyy-mm-dd  dd.mm.yyyy  ddmmyy  dmmyy  dmmyyyy  ddmmyyyy  dd mmm yyyy  mm-dd-yyAll US input formats exceptyyyy.mm.dd and mmddyy | dd.mm.yyyy |
| YMD | mm/dd  mm-dd  mmdd  yymdd  yymmdd  yy-mm-dd  yyyymdd  yyyy-mmm-dd  yyyy/mm/dd  yyyy.mm.dd  yyyy-mm-dd  yyyy_mm_dd  yyyymmdd  yyyy mmm dd | yyyy-mmm-dd |
| DMY | yyyy-mm-dd  yyyy_mm_dd  dd/mm  dd-mm  ddmm  ddmyy  dd-mm-yy  ddmmyy  ddmyyyy  ddmmyyyy  dd/mm/yyyy  dd-mm-yyyy  dd.mm.yyyy  dd-mmm-yyyy  dd mmm yyyy | dd-mmm-yyyy |
| MDY | yyyy-mm-dd  yyyy_mm_dd  mm/dd  mm-dd  mmdd  mmddyy  mddyy  mddyyyy  mm-dd-yy  mm-dd-yyyy  mm/dd/yyyy  mm.dd.yyyy  mmddyyyy  mmm-dd-yyyy | mmm-dd-yyyy |

For a date that is missing the century on input, yearis determined by the setting on the II_DATE_CENTURY_BOUNDARY environment variable.

In three-character month formats, for example, dd-mmm-yy, specify three-letter abbreviations for the month (for example, mar, apr, may).

To specify the current system date and time, use the constant, NOW.

## VWLOAD Supported Character Sets

Character sets supported on the vwload --charset option are:

| Character Set | Description | Format |
| --- | --- | --- |
| ALT | Support of Cyrillic on DOS | Single byte |
| ARABIC | Arabic-449-Plus | Single byte |
| CHINESES | Simplified Chinese – PRC | Double byte |
| CHTBIG5 | Traditional Chinese – Taiwan, BIG5 | Double byte |
| CHTEUC | Traditional Chinese – Taiwan, EUC | Double byte |
| CHTHP | Traditional Chinese – Taiwan, HP ROC15 | Double byte |
| CSGB2312 | Simplified Chinese – GB2312 | Double byte |
| CSGBK | Simplified Chinese – GBK | Double byte |
| CW | Cyrillic on Windows 3.1 | Single byte |
| DECMULTI | DEC Multinational (superset of ASCII) and default for VMS | Single byte |
| DOSASMO | IBM DOS ASMO Arabic (cp708) | Single byte |
| ELOT437 | Greek for PC/RS6000/SCO-UNIX | Single byte |
| GREEK | DEC Greek Elot | Single byte |
| HEBREW | DEC Hebrew | Single byte |
| HPROMAN8 | HP Roman8 (superset of ASCII) | Single byte |
| IBMPC437 | IBM PC Code Page 437 (US and English) | Single byte |
| IBMPC850 | IBM PC Code Page 850 (Multilingual), includes accented characters | Single byte |
| IBMPC866 | IBM PC 866 (Cyrillic for DOS) | Single byte |
| IS885915 | ISO 8859/2 (Latin and some Greek). Identical to ISO 8859/1 Latin, except for eight characters, including the Euro currency symbol (€, Unicode U+20AC) | Single byte |
| ISO88591 | ISO 8859/1 Latin and default for UNIX (superset of ASCII) | Single byte |
| ISO88592 | 8859/5 (Latin and Cyrillic) | Single byte |
| ISO88595 | 8859/9 (Latin and some Turkish) CP 920 | Single byte |
| ISO88597 | ISO 8859/7 (Greek) | Single byte |
| ISO88599 | ISO 8859/15 (Latin and Euro sign) | Single byte |
| KANJIEUC | Japanese, EUC | Double byte |
| KOI18 | KOI 8-bit (ISO 6937/8), Russia | Single byte |
| KOREAN | Korean | Double byte |
| PC737 | IBM PC Code page 737 - Greek | Single byte |
| PC857 | IBM PC Code page 857 - Turkish | Single byte |
| PCHEBREW | IBM PC / MSDOS Hebrew | Single byte |
| SHIFTJIS | Shift-JIS Japanese | Double byte |
| SLAV852 | IBM PC Code Page 852 (Slavic) | Single byte |
| THAI | DEC Thai Tis | Single byte |
| UTF8 | Unicode encoding form UTF-8 | Multi-byte |
| WARABIC | Arabic | Single byte |
| WHEBREW | Microsoft Windows Hebrew | Single byte |
| WIN1250 | Eastern Europe: Windows page 1250 | Single byte |
| WIN1252 | Windows code page 1252 - Latin 1 (Western Europe) and default for Windows | Single byte |
| WIN1253 | Modern Greek | Single byte |
| WTHAI | IBM/Windows Thai (cp874) | Single byte |
