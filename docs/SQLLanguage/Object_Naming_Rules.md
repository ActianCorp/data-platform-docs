---
title: "Object Naming Rules"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Object_Naming_Rules.htm"
canonical_id: "actian-data-platform-object-naming-rules"
---

## Object Naming Rules

The rules for naming database objects (such as tables, columns, and views) are as follows:

- Names can contain only alphanumeric characters and must begin with an alphabetic character or an underscore (_). Database names must begin with an alphabetic character and cannot begin with an underscore.
- Case significance (upper or lower) is determined by the settings for the database in which the object is created (ANSI/ISO Entry SQL-92-compliant) and differs for regular and delimited identifiers.

- Names can contain (but cannot begin with) the following special characters: 0 through 9, #, @, and $. Names specified as delimited identifiers (in double quotes) can contain additional special characters. Database objects cannot begin with the letters, ii. This prefix is reserved for use by the Actian Data Platform.

    For more information on valid user names, see [User Names](../SQLLanguage/Object_Naming_Rules.md).

    For more information about delimited identifiers, see [Regular and Delimited Identifiers](../SQLLanguage/Regular_and_Delimited_Identifiers.md).

- The maximum length of names for the following objects is 256 bytes:

    - –Column

    - –Constraint

    - –Index

    - –Synonym

    - –Table

    Actian Data Platform always installs with the UTF8 character set, so the maximum length of a name may be less than 256 characters if some glyphs use multiple bytes.

- The maximum length of names for the following objects is 32 bytes:

    - –Database

    - –Location

    - –Node

    - –Group

    - –Owner

    - –Profile

    - –Role

    - –Schema

    - –User

- Database names must be unique to 24 bytes.
- Avoid assigning reserved words as object names. A list of reserved words can be found in the in [Keywords](../SQLLanguage/Keywords.md).

- For ANSI/ISO Entry SQL-92 compliant databases, the maximum length of an object name is 18 bytes.

## User Names

User names used to administer Actian Data Platform may contain the following ASCII characters only: alphanumeric, at (@), pound (#), dollar ($), underscore (_), hyphen (-), period (.). Administrative user names cannot contain a blank character.

Non-administrative user names can contain any characters specific to the installation character set. User names that contain characters outside this range must be delimited. For more information, see [Restrictions on Identifiers](../SQLLanguage/Regular_and_Delimited_Identifiers.md).
