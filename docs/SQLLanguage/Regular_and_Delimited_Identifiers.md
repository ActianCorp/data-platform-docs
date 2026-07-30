---
title: "Regular and Delimited Identifiers"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Regular_and_Delimited_Identifiers.htm"
canonical_id: "actian-data-platform-regular-and-delimited-identifiers"
---

## Regular and Delimited Identifiers

Identifiers in SQL statements specify names for the following objects:

- Authorization identifier (user, group, or role)
- Column

- Constraint
- Correlation name

- Index
- Location

- Schema
- Synonym

- Table
- View

The name for any of these objects can be specified using regular (unquoted) identifiers or delimited (double-quoted) identifiers. For example:

- Table name specified using a regular identifier in a SELECT SQL statement:

```
SELECT * FROM employees
```

- Table name specified using a delimited identifier in a SELECT SQL statement:

```
SELECT * FROM "my table"
```

Delimited identifiers let you use special characters in object names. The use of special characters in regular identifiers is restricted. For example, a view name that begins with or consists only of numeric characters must be delimited because a regular identifier cannot begin with the characters 0 through 9, #, @, and $.

!!! note "Note"

    User-defined function names cannot be delimited.

## Case Sensitivity of Identifiers

Case sensitivity for regular and delimited identifiers is defined by configuration parameters. At the time a database is created, the current settings of those parameters are stored with the database.

By default, regular identifiers are translated to and stored as lowercase, and delimited identifiers are kept in mixed case.

The Actian Data Platform treats database, user, group, role, cursor, location, and user-defined function names without regard to case. Mixed-case database or location names cannot be created.

To determine the settings for the database to which a session is connected

Use the DBMSINFO function, as follows:

```
SELECT DBMSINFO('DB_NAME_CASE')
```

and

```
SELECT DBMSINFO('DB_DELIMITED_CASE')
```

## Restrictions on Identifiers

The following table lists the restrictions for regular and delimited identifiers (the names assigned to database objects):

| Restrictions | Regular Identifiers | Delimited Identifiers |
| --- | --- | --- |
| Quotes | Specified without quotes | Specified in double quotes |
| Keywords | Cannot be a keyword | Can be a keyword |
| Valid special characters | “At” sign (@)  (not ANSI/ISO)Crosshatch (#)  (not ANSI/ISO)Dollar sign ($)  (not ANSI/ISO)Underscore (_) | Ampersand (&)Asterisk (*)“At” sign (@)Backslash (\)Braces ({ })Caret (^)Colon (:)Comma (,)Crosshatch (#)Dollar sign ($)Double quotes (")Equal sign (=)Exclamation point (!)Forward slash (/)Left and right caret (< >)Left and right parenthesesLeft quote (ASCII 96 or X'60')Hyphen (-)Percent sign (%)Period (.)Plus sign (+)Question mark (?)Semicolon (;)Single quote (')SpaceTilde (~)Underscore (_)Vertical bar (\|) |

The following characters cannot be embedded in object names using either regular or delimited identifiers:

```
DEL (ASCII 127 or X'7F')
```

To specify double quotes in a delimited identifier, repeat the quotes. For example:

```
"""Identifier""Name"""
```

is interpreted as:

```
"Identifier"Name"
```

Trailing spaces are deleted from object names specified using delimited identifiers.

For example:

```
 "space test " (scolumn INT);
```

creates a table named, space test, with no trailing blanks (leading blanks are retained).

If an object name composed entirely of spaces is specified, the object is assigned a name consisting of a single blank. For example, the following creates a table named “ ”.

```
 "     " (scolumn INT);
```

## Comment Delimiters

To indicate comments in interactive SQL, use the following delimiters:

- /* and */

    For example:

```
/* This is a comment */
```

    The /*...*/ delimiters allow a comment to continue over more than one line. For example:

```
/* Everything from here......to here is a comment */
```

- --

    The -- delimiter indicates that the rest of the line is a comment. The comment cannot be continued to another line.

    For example:

```
--This is a one-line comment.
```
