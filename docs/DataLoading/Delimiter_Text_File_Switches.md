---
title: "Delimiter Text File Switches"
product: "Actian Data Platform"
guide: "Data Loading Guide"
source_file: "Delimiter_Text_File_Switches.htm"
canonical_id: "actian-data-platform-delimiter-text-file-switches"
---

## Delimiter Text File Switches

The following are supported delimiter text file switches.

| Switch | Default | Definition |
| --- | --- | --- |
| charToEscapeQuoteEscaping | escape or \0 | Sets a single character used for escaping the escape for the quote character. The default value is escape character when escape and quote characters are different, \0 otherwise. |
| columnNameOfCorruptRecord | the value specified in spark.sql.columnNameOfCorruptRecord | Allows renaming the new field having malformed string created by PERMISSIVE mode. This overrides spark.sql.columnNameOfCorruptRecord. |
| comment | empty string | Sets a single character used for skipping lines beginning with this character. By default, it is disabled. |
| dateFormat | yyyy-MM-dd | Sets the string that indicates a date format. Custom date formats follow the formats at java.text.SimpleDateFormat. This applies to date type. |
| emptyValue | empty string | Sets the string representation of an empty value |
| enforceSchema | true | If set to true, the specified or inferred schema will be forcibly applied to data source files, and headers in CSV files will be ignored. If set to false, the schema will be validated against all headers in CSV files in the case when the header option is set to true. Field names in the schema and column names in CSV headers are checked by their positions taking into account spark.sql.caseSensitive. Although the default value is true, we recommend that you disable the enforceSchema option to avoid incorrect results. |
| escape | \ | Sets a single character used for escaping quotes inside an already quoted value |
| header | false | Uses the first line as names of columns |
| ignoreLeadingWhiteSpace | false | A flag indicating whether leading white spaces from values being read should be skipped |
| ignoreTrailingWhiteSpace | false | A flag indicating whether trailing white spaces from values being read should be skipped. |
| inferSchema | false | Infers the input schema automatically from data. It requires one extra pass over the data. |
| mode | PERMISSIVE | Allows a mode for dealing with corrupt records during parsing. It supports the following case-insensitive modes:<br>• PERMISSIVE – When it meets a corrupted record, puts the malformed string into a field configured by columnNameOfCorruptRecord, and sets other fields to null. To keep corrupt records, a user can set a string type field named columnNameOfCorruptRecord in a user-defined schema. If a schema does not have the field, it drops corrupt records during parsing. A record with less or more tokens than the schema is not a corrupted record to CSV. When it meets a record having fewer tokens than the length of the schema, it sets null to the extra fields. When the record has more tokens than the length of the schema, it drops the extra tokens.<br>• DROPMALFORMED – Ignores the whole of corrupted records<br>• FAILFAST – Throws an exception when it meets corrupted records |
| multiLine | false | Parse one record, which may span multiple lines |
| nanValue | NaN | Sets the string representation of a non-number value |
| negativeInf | -Inf | Sets the string representation of a negative infinity value |
| nullvalue | empty string | Sets the string representation of a null value. Since 2.0.1, this applies to all supported types including the string type. |
| positiveInf | Inf | Sets the string representation of a positive infinity value |
| quote | " | Sets a single character used for escaping quoted values where the separator can be part of the value. To turn off quotations, you need to set not null but an empty string. This behavior is different from com.databricks.spark.csv. |
| samplingRatio | 1.0 | Defines fraction of rows used for schema inferring |
| sep | , | Sets a single character as a separator for each field and value |
| timestampFormat | yyyy-MM-dd'T'HH:mm:ss.SSSXXX | Sets the string that indicates a timestamp format. Custom date formats follow the formats at java.text.SimpleDateFormat. This applies to timestamp type. |
