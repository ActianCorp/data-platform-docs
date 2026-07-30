---
title: "Data at Rest Encryption"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Data_at_Rest_Encryption.htm"
canonical_id: "actian-data-platform-data-at-rest-encryption"
---

## Data at Rest Encryption

Data at rest refers to data on physical media recorded in a persistent form in an Actian Data Platform database table, transaction log, journal, and checkpoint files.

Data at rest encryption allows all columns in all tables in the database to be encrypted.

Encrypted columns are stored in the database files using 256-bit Advanced Encryption Standard (AES) encryption. The encryption is transparent to the applications accessing the data.

Data at rest encryption does not protect data outside of the database, which includes:

- Data passed back and forth to applications
- Transactions that implement data replication at a logical (as opposed to the binary, journal application) level

!!! note "Note"

    If the security of data transmitted over a network is important, you may implement protection using other mechanisms such as AES. Flat files containing sensitive information that is encrypted in the database should be stored in encrypted files or on encrypted media.
