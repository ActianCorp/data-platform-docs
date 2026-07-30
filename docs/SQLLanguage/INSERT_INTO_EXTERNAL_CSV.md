---
title: "INSERT INTO EXTERNAL CSV"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "INSERT_INTO_EXTERNAL_CSV.htm"
canonical_id: "actian-data-platform-insert-into-external-csv"
---

## INSERT INTO EXTERNAL CSV

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The INSERT INTO EXTERNAL CSV statement writes a table to a POD, ABFS, S3A, or GS file system. The result is either a single CSV file or a collection of CSV files, depending on whether the query is run in parallel. The number of files produced cannot be specified, but can be indirectly influenced by setting [engine] max_parallelism_level.

For differences between INSERT INTO EXTERNAL CSV and COPY VWLOAD syntax, see [Required COPY VWLOAD Options to Load Data Written with INSERT INTO EXTERNAL CSV](../DataLoading/ExportingImportingData.md).

This statement has the following format:

```
INSERT INTO EXTERNAL CSV 'filename' SELECT ... [WITH options]
```

**filename**

:   Specifies the output location, which can be either a POD, ABFS, S3A, or GS file system path URL. If multiple files are created, they use the filename with suffixes in the form '.nnn' where nnn is the file number.

:   You must have permissions to write to the specified location.

:   For security reasons, existing files cannot be overwritten. The query will end with an error if any of the output files already exist.

**SELECT**

:   Specifies a SELECT statement that selects the table data to be written.

**WITH options**

:   (Optional) Specifies WITH clause options separated by a comma. Valid optionsare:

AWS_ACCESS_KEY='my_access_key'

:   Specifies the access key ID to access your S3 bucket on Amazon Web Services.

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

NULL_MARKER='null_value'

:   Specifies the text to use for the NULL valued attributes. When a parameter contains commas or spaces, double quotation marks must be used. Default: 'null'

FIELD_SEPARATOR='field_separator'

:   Specifies the character to use to separate fields. The delimiter must be a single character. Default: , (comma)

FLOAT_FORMAT='xwidth.prec'

:   Specifies the format to export floating point numbers. The format has the following

:   parameters:

:   x=format specifier:

        - f (demical representation), e.g. 503.42003

        - e (scientific notation), e.g. 5.0342003c+03

        - g (default): individually choose the best representation between f and e (i.e. scientific format if there are significant digits after prec zeros in the fraction, otherwise decimal).

:   Uppercase format letters are also possible, they generate an uppercase exponent letter (e.g. 5.0342003E+03)

:   width = total string width

:   “.” = decimal point: any other specifier is possible (e.g. “,” for 503,42003)

:   prec = number of decimal places

:   Default: ‘g79.38’

!!! note "Note"

    Very large and very small (absolute value) numbers might cause rounding errors. This can occur if the exponent is larger than 78 or if the number of decimal places is larger than 14. Use smaller formats, e.g. ‘g11.3’ to avoid such rounding errors.

RECORD_SEPARATOR='record_separator'

:   Specifies the character to use to separate records. The delimiter must be a single character. To specify a control character, use an escape sequence. Default: \n

WORK_DIR='file_directory'

:   Specifies the directory in which the files are created if the filename is relative.

## INSERT INTO EXTERNAL CSV Examples

Azure:

```
INSERT INTO EXTERNAL CSV 'abfs://vwexport@vectorjenkinstest.dfs.core.windows.net/test4.csv'
```

```
SELECT * FROM test3 WITH
```

```
azure_client_endpoint='https://login.microsoftonline.com/20067ce9-1326-4771-8b04-e7824ef632de/oauth2/token',
```

```
AZURE_CLIENT_ID='931f4f78-e87b-4fag-9141-2e82a7d61e26',
```

```
AZURE_CLIENT_SECRET = 'this is a secret :)',
```

```
NULL_MARKER='"this is null"'
```

AWS:

```
INSERT INTO EXTERNAL CSV 's3a://vector-sumatra-test/vwexport/test3.csv'
```

```
SELECT * FROM test3 WITH
```

```
AWS_ACCESS_KEY='AKIAT7HATMLVMCELSH6L',
```

```
AWS_SECRET_KEY='THIS IS A SECRET :)'
```

Google Cloud:

```
INSERT INTO EXTERNAL CSV 'gs://drivi01-test/test3.csv'
```

```
SELECT * FROM test3 WITH
```

```
GCS_EMAIL='company-test-admin@avalanche.iam.gserviceaccount.com',
```

```
GCS_PRIVATE_KEY_ID='099aebe9ccbcd92fd6543a0806aedbafbb1fc16e',
```

```
GCS_PRIVATE_KEY = '-----BEGIN PRIVATE KEY-----my very long secret key-----END PRIVATE KEY-----\n',
```

```
NULL_MARKER='"this is null"'
```
