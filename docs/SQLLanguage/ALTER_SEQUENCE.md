---
title: "ALTER SEQUENCE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_SEQUENCE.htm"
canonical_id: "actian-data-platform-alter-sequence"
---

## ALTER SEQUENCE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The ALTER SEQUENCE statement changes sequence settings that were specified when the sequence was created.

The ALTER SEQUENCE syntax has the following format:

```
[EXEC SQL] ALTER SEQUENCE [schema.]sequence_name [sequence_options]
```

**sequence_options**

:   See [GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md) for more information.

#### Permissions

You must have CREATE_SEQUENCE privilege.

You need NEXT privilege to retrieve values from a defined sequence. For more information on the NEXT privilege, see [GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md).

#### Locking and Sequences

In applications, sequences use logical locks that allow multiple transactions to retrieve and update the sequence value while preventing changes to the underlying sequence definition. The logical lock is held until the end of the transaction.

#### Related Statements

[CREATE SEQUENCE](../SQLLanguage/CREATE_SEQUENCE.md)[](../SQLLanguage/CREATE_SEQUENCE.md)

[DROP SEQUENCE](../SQLLanguage/DROP_SEQUENCE.md)[](../SQLLanguage/DROP_SEQUENCE.md)
