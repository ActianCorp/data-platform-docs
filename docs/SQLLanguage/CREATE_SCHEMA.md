---
title: "CREATE SCHEMA"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_SCHEMA.htm"
canonical_id: "actian-data-platform-create-schema"
---

## CREATE SCHEMA

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE SCHEMA statement creates a named collection of database objects.

The CREATE SCHEMA statement has the following format:

```
[EXEC SQL] CREATE SCHEMA AUTHORIZATION schema_name               [object_definition {object_definition}];
```

**schema_name**

:   Specifies the effective user for the session issuing the CREATE SCHEMA statement.

**object_definition**

:   Is a [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md), [CREATE VIEW](../SQLLanguage/CREATE_VIEW.md), or GRANT statement.

The CREATE SCHEMA statement creates a named collection of database objects (tables, views, and privileges). Each user has a maximum of one schema per database. If an error occurs within the CREATE SCHEMA statement, the entire statement is rolled back.

The statements within the CREATE SCHEMA statement must not be separated by semicolon delimiters; however, the CREATE SCHEMA statement must be terminated by placing a semicolon after the last object definition statement (CREATE TABLE, CREATE VIEW, or GRANT).

If object definitions are omitted, an empty schema is created.

To issue grant statements in a CREATE SCHEMA statement, you must have the required privileges. Specifically, to grant a privilege on an object you do not own, you must have been granted the privilege WITH GRANT OPTION (see [GRANT OPTION Clause](../SQLLanguage/GRANT_(privilege).md)).

If an invalid GRANT statement is issued within a CREATE SCHEMA statement, the outcome is determined as follows:

- If you have no privileges whatsoever on the object against which you issue the GRANT statement, the entire [CREATE SCHEMA](../SQLLanguage/CREATE_SCHEMA.md) statement is terminated.
- If you have any privilege whatsoever on the object, a warning is issued and the invalid portions of the grant do not succeed. The valid portions of the grant do succeed, and the CREATE SCHEMA statement is not terminated.

For example, if user andre has been granted SELECT WITH GRANT OPTION on table tony.mytable and issues the following GRANT statement within a CREATE SCHEMA statement:

```
grant select, insert on tony.mytable to fred
```

user fred is granted SELECT privilege but not INSERT privilege, and a warning is issued.

If a CREATE SCHEMA is issued specifying an existing schema (schema_name), Actian Data Platform issues an error. To add objects to an existing schema, issue the required CREATE statements outside of a CREATE SCHEMA statement.

If no schema exists for the effective user identifier, one is implicitly created when any database object is created. If a CREATE SCHEMA statement is subsequently issued for the user, Actian Data Platform returns an error.

If, within a CREATE SCHEMA statement, tables are created that have referential constraints, the order of CREATE TABLE statements is not significant. This differs from the requirements for creating tables with referential constraints outside of a CREATE SCHEMA statement, where the referenced table must exist before creating a constraint that references it. For more information about referential constraints, see [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md).

Other users can reference objects in your schema if you have granted them the required permissions. To access an object in a schema other than the schema for the effective user of the session, specify the object name as follows:

```
schema.object
```

For example, user harry can select data from the employees table of the accounting group (if accounting has granted harry select permission). Harry can issue the following SELECT statement:

```
select lname, fname from accounting.employees
```

#### Embedded Usage

You cannot use host language variables in an embedded CREATE SCHEMA statement.

#### Permissions

This statement is available to all users.

#### Locking

The CREATE SCHEMA statement takes an exclusive lock on a page in the iischema catalog. Locks are acquired by the individual CREATE statements within the CREATE SCHEMA statement, but released only when the CREATE SCHEMA statement itself is committed. If the CREATE SCHEMA statement contains CREATE statements that acquire locks in excess of the maximum configured for the Actian Data Platform, the CREATE SCHEMA statement is terminated.

#### Related Statements

[CREATE TABLE](../SQLLanguage/CREATE_TABLE.md)[](../SQLLanguage/CREATE_TABLE.md)

[CREATE VIEW](../SQLLanguage/CREATE_VIEW.md)[](../SQLLanguage/CREATE_VIEW.md)

[GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md)[](../SQLLanguage/GRANT_(privilege).md)
