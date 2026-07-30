---
title: "Encryption Functions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Encryption_Functions.htm"
canonical_id: "actian-data-platform-encryption-functions"
---

## Encryption Functions

Encryption functions encrypt data stored in Actian Data Platform tables. The encryption functions include:

- AES_ENCRYPT_IV
- AES_DECRYPT_IV

For more information, see the Security Guide.

**AES_ENCRYPT_IV**

```
AES_ENCRYPT_IV(column_name,'encryption_passphrase'[,128|192|256])
```

:   Operand type: VARCHAR. Compatible types are automatically converted to VARCHAR.

:   Result type: VARCHAR

:   Encrypts the values to be inserted or updated in a table. The data is encrypted using a random initialization vector (IV) with cipher block chaining (CBC) mode.

:   The data can be read only by using the AES_DECRYPT_IV function, supplying the encryption passphrase. The key size, if not specified, defaults to 128.

:   The resulting string is a 7-bit ASCII string.

:   Examples:

```
SELECT * FROM mytable WHERE column = AES_ENCRYPT_IV('secret_value', 'passphrase')
```

```
INSERT INTO socsec2 SELECT
```

```
        fname, lname,
```

```
        AES_ENCRYPT_IV(socsec,'user function encryption')
```

```
        FROM socsec1
```

    The following will fail because the encrypted result cannot be converted to an integer because it contains non-numeric characters:

```
CREATE TABLE table1 (a INT);
```

```
INSERT INTO table1 VALUES (AES_ENCRYPT_IV(2, '278435'))
```

    The following, however, will work:

```
CREATE TABLE table2 (a VARCHAR(100));
```

```
INSERT INTO table2 VALUES (AES_ENCRYPT_IV(2, '278435'))
```

**Caution!**Do not truncate the result when storing because decryption will fail. For information on error handling for string truncation, see [String Truncation](../SQLLanguage/SQL_Operations.md).

**AES_DECRYPT_IV**

```
AES_DECRYPT_IV(column_name,'encryption_passphrase'[,128|192|256])
```

:   Operand type: VARCHAR

:   Result type: VARCHAR

:   Decrypts data (allows encrypted data to be read in plain text) that has been encrypted with the AES_DECRYPT_IV function by supplying the encryption passphrase. The key size, if not specified, defaults to 128.

:   Example:

```
SELECT columnname, columnname,        AES_DECRYPT_IV(columnname,'encryption_passphrase') AS columnname        FROM table2
```

!!! note "Note"

    You may need to explicitly cast the VARCHAR result back to the original encrypted input data type.
