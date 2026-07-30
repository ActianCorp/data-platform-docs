---
title: "CREATE SEQUENCE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_SEQUENCE.htm"
canonical_id: "actian-data-platform-create-sequence"
---

## CREATE SEQUENCE

!!! note "Note"

    Sequences work only in specific circumstances; we do not recommend the use of sequences except in consultation with Actian Support or Actian Services.

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL

The CREATE SEQUENCE statement creates a new sequence. A sequence is a defined database entity that is used to supply a set of integer values to an application in sequential order according to a set of definition parameters (sequence_options).

The CREATE SEQUENCE statement has the following format:

```
[EXEC SQL] CREATE SEQUENCE [schema.]sequence_name [sequence_options]
```

**sequence_name**

:   Defines the name of the sequence.

**sequence_options**

:   Control how the sequence supplies data when requested by an application. Sequence options can be specified in any order, and none are required.

:   Any of the following options can be specified in a blank-space separated list:

AS data type

:   Specifies the data type of the sequence as one of the following:

:   INTEGER

:   BIGINT

:   DECIMAL (with an optional precision, but 0 scale)

:   Default: INTEGER

!!! note "Note"

    Both bigint and integer sequences are managed internally as 64-bit integers.

START WITH number

:   Specifies the start of the sequence as an integer constant. The default value is 1 for positive sequences (positive increment) and -1 for negative sequences (negative increment). (This option is valid with the CREATE SEQUENCE statement only.)

RESTART WITH number

:   Specifies a new start value for the sequence. (This option is valid with the ALTER SEQUENCE statement only.)

INCREMENT BY number

:   Specifies the increment value (positive or negative) that produces successive values of the sequence.

:   Default: 1

MAXVALUE number

:   Specifies the maximum value allowed for the sequence.

:   Defaults:

:   For positive integer sequences: 2**31-1

:   For positive bigint sequences: 2**63-1

:   For positive decimal(n) sequences: 10**(n+1)-1

:   For negative sequences: -1

NO MAXVALUE / NOMAXVALUE

:   Specifies that sequences can generate values with an upper bound equivalent to that of the data type chosen to hold the sequence (for example, 2**31-1 for integers).

MINVALUE number

:   Specifies the minimum value allowed for the sequence.

:   Default:

:   For positive sequences: 1

:   For negative bigint sequences: -2**63

:   For negative integer sequences: -2**31

:   For negative decimal(n) sequences: -(10**(n+1)-1)

NO MINVALUE / NOMINVALUE

:   Specifies that sequences can generate values with a lower bound equivalent to that of the data type chosen to hold the sequence (for example, -2**31 for integers).

CACHE number

:   Specifies the number of sequence values held in server memory. When the supply of numbers is exhausted, Actian X requires a catalog access to acquire the next set.

:   Default: 20

NO CACHE / NOCACHE

:   Specifies that sequence values are not to be cached by the server. When this option is selected, a catalog access is required for each request for a sequence value. This can severely degrade application performance.

:   Default: CACHE 20 (when neither CACHE nor NOCACHE are specified), which ensures low catalog overhead.

CYCLE

:   Specifies that the sequence restarts at the beginning value once it reaches the minimum value (negative increment) or maximum value (positive increment).

:   Default: NO CYCLE

NO CYCLE / NOCYCLE

:   Specifies that the sequence is not cycled when the last valid value is generated. An error is issued to the requesting transaction.

ORDER

NO ORDER / NOORDER

:   These options are included solely for syntax compatibility with other DBMSes that implement sequences, and are not currently supported in Actian X.

:   Default: NOORDER

SEQUENTIAL / UNORDERED

:   Specifies whether values are returned sequentially or in unordered sequence. RANDOM is a synonym for UNORDERED. This option is ignored for decimal-based sequences.

:   Default: SEQUENTIAL

#### Permissions

You must have CREATE_SEQUENCE privilege.

You need NEXT privilege to retrieve values from a defined sequence. For information on the NEXT privilege, see [GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md).

#### Locking and Sequences

In applications, sequences use logical locks that allow multiple transactions to retrieve and update the sequence value while preventing changes to the underlying sequence definition. The logical lock is held until the end of the transaction.

#### Related Statements

[ALTER SEQUENCE](../SQLLanguage/ALTER_SEQUENCE.md)[](../SQLLanguage/ALTER_SEQUENCE.md)

[DROP SEQUENCE](../SQLLanguage/DROP_SEQUENCE.md)[](../SQLLanguage/DROP_SEQUENCE.md)
