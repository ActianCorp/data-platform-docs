---
title: "Environment Variables"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Environment_Variables.htm"
canonical_id: "actian-data-platform-environment-variables"
---

# Environment Variables

The environment variables described in this section are useful for ODBC, the SQL CLI, and Embedded SQL. They cannot be set or used with JDBC or .NET applications.

Valid in: SQL, ESQL, ODBC

These variables control the output and/or the input format:

**II_DATE_CENTURY_BOUNDARY**

:   Determines the inferred century for a date that is missing the century on input. It can be set to an integer value in the range of 0 < n < =100. If this environment variable is not explicitly set in the user’s environment or if it is set to 0 or 100, the current century is used.

:   The century is determined by the following calculation:

```
if (current_year < II_DATE_CENTURY_BOUNDARY)
```

```
    if (input_year < II_DATE_CENTURY_BOUNDARY)
```

```
       output_year = input_year + current_century
```

```
    else
```

```
       output_year = input_year + previous_century
```

```
else
```

```
    if (input_year < II_DATE_CENTURY_BOUNDARY)
```

```
       output_year = input_year + next_century
```

```
    else
```

```
       output_year = input_year + current_century
```

:   For example, if II_DATE_CENTURY_BOUNDARY is 50 and the current year is 1999, an input date of 3/17/51 is treated as March 17, 1951, but a date of 03/17/49 is treated as March 17, 2049.

:   If the user enters the full four digits for the year into a four-digit year field in the application, the year is accepted as entered, regardless of the II_DATE_CENTURY_BOUNDARY setting.

**II_DATE_FORMAT**

:   Defines the format for date values. If set, it replaces the default format (the US setting) with an alternative format.

:   The following are valid II_DATE_FORMAT settings and their output formats:

| Setting | Output Format |
| --- | --- |
| US (default) | dd-mm-yyyy |
| MULTINATIONAL | dd/mm/yy |
| MULTINATIONAL4 | dd/mm/yyyy |
| ISO | yymmdd |
| ISO8601 | yyyy-dd-mmThh:mm:ssZ, where hh is in 24-hour format and Z indicates Zulu (UTC) timezone |
| ISO4 | yyyymmdd |
| ISO4T | yyyymmdd unless the date includes a time, in which case the format is: yyyymmddThhmmss |
| ISO4TC | yyyymmdd unless the date includes a time, in which case the format is: yyyymmddThh:mm:ss |
| SWEDEN or FINLAND | yyyy-mm-dd |
| GERMAN | dd.mm.yy |
| YMD | yyyy-mmm-dd |
| DMY | dd-mmm-yyyy |
| MDY | mmm-dd-yyyy |

:   For example, if the II_DATE_FORMAT setting is ISO, the dates are output as yymmdd. If you enter a date using a similar, six-character format, such as mmddyy, the date is interpreted on output asyymmdd. For example, if you enter the date March 9, 1912, as 030912 (mmddyy) and II_DATE_FORMAT is set to ISO, this date is interpreted as Sept. 12, 1903 (030912 as yymmdd). If the date you entered cannot be interpreted as a valid date in the output format, you will receive an error message.

!!! note "Note"

    When using the _date4() function (MULTINATIONAL4), the output format for the year value always returns “yyyy”.

**II_DECIMAL**

:   Specifies the character used to separate fractional and non-fractional parts of a number. Valid characters are the period (.) (as in 12.34) or the comma (,) (as in 12,34).

:   Default: period

!!! note "Note"

    If II_DECIMAL is set to comma, ensure that when SQL syntax requires a comma (such as a list of table columns or SQL functions with several parameters), that the comma is followed by a space. For example:

```
select col1, ifnull(col2, 0), left(col4, 22) from t1:
```

**II_MONEY_FORMAT**

:   Defines the format of monetary output.

:   II_MONEY_FORMAT is set to a string with two symbols separated by a colon (:). The symbol to the left of the colon indicates the location of the currency symbol—L for a leading currency symbol or T for a trailing currency symbol. The symbol to the right of the colon is the currency symbol you want displayed. Currency symbols can contain up to four physical characters.

:   If no currency symbol is required, set the value to NONE.

:   For example:

| Logical Definition | Result |
| --- | --- |
| `L:$` | `$100` |
| `T:DM` | `100DM` |
| `T:F` | `100F` |

**II_MONEY_PREC**

:   Specifies the number of decimal places to be displayed for money values. Valid values are 0, 1, and 2.

:   Default: 2 (for decimal currency)

:   II_MONEY_PREC is applied when a money value is converted to a character string (for printing, for example). Extra decimal places are rounded. For example, if II_MONEY_PREC is set to 0, 9.50 is rounded to 10.

**II_TIMEZONE_NAME**

:   Specifies the world time zone that determines the warehouse’s location for timing purposes. It is defined during installation with the equivalent of the UTC timezone name.

Valid in: SQL, ESQL, ODBC

The following variables enable you to inject initial SQL statements. The injected statements are executed when connecting. Only statements starting with “SET...” are allowed.

**ING_SET**

:   Specifies a quoted string or startup file of set commands to be executed whenever a user connects to the warehouse through an application or the SQL CLI.

**ING_SET_dbname**

:   Specifies a quoted string or startup file of set commands to be executed whenever a user connects to the database specified by dbname. Affects any user who connects to the specified database through an application or the SQL CLI. For more information, see [Syntax Rules for Startup Files and Environment Variables](../SQLLanguage/Syntax_Rules_for_Startup_Files_and_Environment_V.md).

**ING_SYSTEM_SET**

:   Specifies a quoted string or startup file of set commands to be executed whenever a user connects to the warehouse through an application or the SQL CLI. For more information, see [Syntax Rules for Startup Files and Environment Variables](../SQLLanguage/Syntax_Rules_for_Startup_Files_and_Environment_V.md).

Valid in: SQL

The following variables have a meaning for the [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md) only.

**II_NULL_STRING**

:   Specifies the string used by the SQL CLI to represent the null value. The string consists of one to three characters. The default value is three blanks.

**II_SQL_INIT**

:   Can be set to the full path name of a file containing SQL commands. Typically, it is defined by individual users. When a user with II_SQL_INIT set connects to the SQL CLI, the commands in the named file are processed.

**II_TM_EXIT_ON_ERROR**

:   Directs the SQL CLI to perform a rollback instead of a commit before exiting due to an error.

:   This variable works only when the \nocontinue switch is set (either as an SQL CLI command in the script or on the II_TM_ON_ERROR variable), which instructs the SQL CLI to exit whenever an SQL statement fails.

**II_TM_ON_ERROR**

:   Defines the action taken when an error occurs in the SQL CLI. The valid settings are continue (on error) or terminate (on error). If this environment variable is not set, the default action for the SQL CLI is to continue; the default for interactive terminal monitors is to terminate.
