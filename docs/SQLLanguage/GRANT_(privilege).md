---
title: "GRANT (privilege)"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "GRANT_(privilege).htm"
canonical_id: "actian-data-platform-grant-privilege"
---

## GRANT (privilege)

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The GRANT (privilege) statement grants privileges on the database as a whole or on individual tables, views, sequences, or procedures. It controls access to database objects, roles, and DBMS resources.Details about using the GRANT statement with role objects is described in [GRANT (role)](../SQLLanguage/GRANT_(role).md).

To remove privileges, use the REVOKE statement. To determine the privileges in effect for a session, use the DBMSINFO function. In some cases granting a privilege imposes a restriction, and revoking the privilege removes the restriction. For example, GRANT NOCREATE_TABLE prevents the user from creating tables.

!!! note "Note"

    The GRANT statement is the ISO/ANSI-compliant method for controlling access to database objects and resources.

To display granted database privileges, select data from the iidbprivileges system catalog.

#### Syntax

The GRANT (privilege) statement has the following format:

```
[EXEC SQL] GRANT ALL [PRIVILEGES] | privilege {, privilege}              [ON [object_type] [schema.]object_name {, [schema.]object_name}]              TO PUBLIC | [auth_type] auth_id {, auth_id} [WITH GRANT OPTION];
```

**privilege**

:   Specifies the privilege, which must be valid for the object_type.

:   Valid privileges are described under the section [Object Privileges](../SQLLanguage/GRANT_(privilege).md).

**object_type**

:   Specifies the type of object on which you are granting privileges. Object_type must be one of the following:

TABLE

:   (Default) Controls access to individual tables or views.

DATABASE

:   Controls access to database resources.

PROCEDURE

:   Controls who can execute individual database procedures.

DBEVENT

:   Controls who can register for and raise specific database events.

SEQUENCE

:   Controls who can retrieve values from individual database sequences.

CURRENT INSTALLATION

:   Grants the specified privilege on the current installation.

:   The object_type must agree with the privilege being granted (for example, EXECUTE privilege cannot be granted on a table).

:   Privileges cannot be defined for more than one type of object in a single GRANT statement. Ifobject_type is CURRENT INSTALLATION, object_namemust be omitted.

**object_name**

:   Specifies the name of the table, view, procedure, database event, sequence, or database for which the privilege is being defined. The object must correspond to the object_type. For example, if object_type is TABLE, object_name must be the name of an existing table or view.

**auth_type**

:   Specifies the type of authorization to which you are granting privileges. A GRANT statement cannot contain more than one auth_type. Valid auth_types are:

    - USER

    - GROUP

    - ROLE

    The auth_ids specified in the statement must agree with the specified auth_type. For example, if you specify auth_type as GROUP, all auth_ids listed in the statement must be group identifiers.

    Default: USER

**PUBLIC**

:   Grants a privilege to all users. The auth_type parameter can be omitted.

**auth_id**

:   Specifies the name of the users, groups, or roles to which you are granting privileges, or PUBLIC. Both PUBLIC and a list of auth_ids can be specified in the same GRANT statement. If the privilege is subsequently revoked from PUBLIC, the individual privileges still exist.

## Object Privileges

The privilege granted depends on the type of object it affects: TABLE, DATABASE, PROCEDURE, DBEVENT, or SEQUENCE.

### TABLE Privileges

Table privileges control access to tables and views. By default, only the owner of the table has privileges for the table. To enable others to access the table, the owner must grant privileges to specific authorization IDs or to public. Table privileges must be granted explicitly.

Valid table privileges are:

**SELECT**

:   Allows grantee to select rows from the table.

**INSERT**

:   Allows grantee to add rows to the table.

**UPDATE**

:   Allows grantee to change existing rows. To limit the columns that the grantee can change, specify a list of columns to allow or a list of columns to exclude.

:   To grant the privilege for specific columns, use the following syntax after the UPDATE keyword in the GRANT statement:

```
(column_name {, column_name)
```

:   To grant the privilege for all columns except those specified, use the following syntax after the UPDATE keyword in the GRANT statement:

```
EXCLUDING (column_name {, column_name})
```

:   If the column list is omitted, update privilege is granted to all columns of the table or, for views, all updatable columns.

**DELETE**

:   Allows grantee to delete rows from the table.

**REFERENCES**

:   Allows grantee to create referential constraints that reference the specified tables and columns. For more information about referential constraints, see [CREATE TABLE](../SQLLanguage/CREATE_TABLE.md). A list of columns to allow or to exclude can optionally be specified.

:   To grant the privilege for specific columns except those specified, use the following syntax after the REFERENCES keyword in the GRANT statement:

```
(column_name {, column_name})
```

:   To grant the privilege for all columns except those specified, use the following syntax after the REFERENCES keyword in the GRANT statement:

```
EXCLUDING (column_name {, column_name})
```

:   If the column list is omitted, references privilege is granted to all columns of the table. The references privilege cannot be granted on a view.

**COPY_INTO**

:   Allows the grantee to issue the COPY...INTO statement on a table. This privilege can be granted on tables only.

**COPY_FROM**

:   Allows the grantee to issue the COPY...FROM statement on a table. This privilege can be granted on tables only.

**ALL [PRIVILEGES]**

:   Grants the subset of select, insert, update, delete, and references privileges for which the grantor has GRANT OPTION. For more information, see [GRANT ALL PRIVILEGES Option](../SQLLanguage/GRANT_(privilege).md).

When privileges are granted against a table, the date and timestamp of the specified table is updated, and Actian Data Platform recreates query plans for repeat queries and database procedures that see the specified table.

### TABLE Privileges for Views

The privileges required to enable the owner of a view to grant privileges on the view are as follows:

**SELECT**

:   View owner must own all tables and views used in the view definition, or view owner or public must have GRANT OPTION for SELECT for the tables and views used in the view definition.

**INSERT**

:   View owner must own all tables and views used in the view definition, or view owner or public must have GRANT OPTION for INSERT for the tables and views used in the view definition.

**UPDATE**

:   View owner must own all tables and updatable columns in views used in the view definition, or view owner or public must have GRANT OPTION for UPDATE for the tables and updatable columns in views used in the view definition.

**DELETE**

:   View owner must own all tables and views used in the view definition, or view owner or public must have GRANT OPTION for DELETE for the tables and views used in the view definition.

To grant privileges for views the grantor does not own, the grantor must have been granted the specified privilege WITH GRANT OPTION.

### DATABASE Privileges

Database privileges control the consumption of computing resources.

Database privileges can only be assigned when connected to the iidbdb database.

To override the default for a database privilege, grant a specific value to PUBLIC. For example, by default, everyone (PUBLIC) has the privilege to create tables. To override the default, grant NOCREATE_TABLE to PUBLIC, and grant the CREATE_TABLE privilege to any user, group, or role that you want to have this privilege. (Users, groups, and roles are referred to collectively as authorization IDs.)

Database privileges do not apply to DBAs in their own databases, nor to security administrators.

The database privileges in effect for a session are determined by the values that were granted to the authorization IDs in effect for the session, according to the following hierarchy:

1. Role
2. User

3. Group
4. Public

For example, if different values for CREATE_TABLE are granted to PUBLIC, and to the user, group, and role that are in effect for a session, the value for the role of the session prevails.

Valid database privileges are as follows:

**[NO]ACCESS**

:   Allows the specified authorization IDs to connect to the specified database.

:   NOACCESS prevents the specified authorization IDs from connecting.

!!! note "Note"

    The access bitmask of the iidatabase_info catalog is set only if database utilities are used to change the access rights to the database. Using a GRANT [NO]ACCESS ON DATABASE dbnameTO PUBLIC statement does not change the access from global to private or vice versa in iidatabase_info.

**[NO]CONNECT_TIME_LIMIT**

:   Limits the total connect time that a session can consume. The connect time is checked periodically by Actian Data Platform and if the limit has been exceeded for a session, it is disconnected, rolling back any open database transactions.

:   The units are seconds. The maximum connection time limit is 2147483647 seconds, approximately 68 years. The minimum connection time limit is 1 second.

:   Default: No limit, that is, a session can remain connected indefinitely.

**[NO]CREATE_PROCEDURE**

:   Allows the specified authorization IDs to create database procedures in the specified database.

:   NOCREATE_PROCEDURE prevents the specified users, groups, or roles from creating database procedures.

:   Default: All authorization IDs can create database procedures.

**[NO]CREATE_TABLE**

:   Allows the specified authorization IDs to create tables in the specified database.

:   NOCREATE_TABLE prevents the specified authorization IDs from creating tables.

:   Default: All authorization IDs can create tables.

**[NO]DB_ADMIN**

:   Confers unlimited database privileges for the specified database and the ability to specify effective user (using the -u flag). A session that has the DB_ADMIN privilege does not have all the rights that a DBA has; some utilities can be run only by a DBA. Warehouse owners have the DB_ADMIN privilege by default. For all other users, the default is NODB_ADMIN.

**[NO]IDLE_TIME_LIMIT**

:   Specifies the time that a session can take between issuing statements. The idle time for each session is checked periodically by Actian Data Platform, and if a session exceeds its idle time limit it is disconnected, rolling back any open database transactions.

:   The units are seconds. The maximum idle time limit is 2147483647 seconds, approximately 68 years. The minimum idle time limit is 1 second. IDLE_TIME_LIMIT can be granted to user, group, role or public, and can only be issued when connected to the iidbdb database.

:   Default: No limit, that is, a session can remain idle indefinitely without being disconnected.

**[NO]QUERY_COST_LIMIT**

:   Specifies the maximum cost per query on the database, in terms of disk I/O and CPU usage.

:   Default: Authorization identifiers are allowed an unlimited cost per query.

**[NO]QUERY_CPU_LIMIT**

:   Specifies the maximum CPU usage per query on the database.

:   Default: Authorization identifiers are allowed unlimited CPU usage per query.

**[NO]QUERY_IO_LIMIT**

:   Specifies the maximum estimated number of I/O requests allowed for a single query for the specified authorization IDs when connected to the specified database. Integer must be a non-negative integer (or 0 to specify that no I/O is performed).

:   NOQUERY_IO_LIMIT grants an unlimited number of I/O requests per query.

:   Default: NOQUERY_IO_LIMIT

**[NO]QUERY_PAGE_LIMIT**

:   Specifies the maximum number of pages per query on the database.

:   Default: Authorization identifiers are allowed an unlimited number of pages per query.

**[ACTUAL | ESTIMATED] [NO]QUERY_ROW_LIMIT**

:   Specifies the maximum ACTUAL or ESTIMATED number of rows returned by a single query for the specified authorization IDs when connected to the specified database. Integer must be a positive number (or 0 to specify that no rows are returned). ESTIMATED is the default and does not need to be specified. ACTUAL and ESTIMATED are mutually exclusive.

:   Default: NOQUERY_ROW_LIMIT (query can return an unlimited number of rows)

**[NO]QUERY_ROW_STEP_LIMIT n**

:   Specifies the number of rows that an individual query step cannot exceed before the query is canceled.

:   Default: NOQUERY_ROW_STEP_LIMIT (no limit)

**[NO]UPDATE_SYSCAT**

:   Allows the specified authorization IDs to update system catalogs when working in a session connected to the iidbdb database.

**[NO]READONLY**

:   Controls the access mode for the database. READONLY disallows insert, update, delete, truncate, copy, and DDL operations and returns an SQLSTATE of 25000 (invalid session state). Temporary tables are the exception and are always writable. When a READONLY session is begun, it registers itself with the logging system and is allowed to proceed. Use it for applications that can be read only most of the time.

**[NO]SELECT_SYSCAT**

:   Allows a session to query system catalogs to determine schema information. When connected to the master database (iidbdb), this includes the master database catalogs such as iiuser and iidatabase. SELECT_SYSCAT can be granted to user, group, role or public, and can only be issued when connected to the iidbdb database.

:   This privilege restricts user queries against the Actian Data Platform catalogs containing schema information, such as iirelation and iiattribute. Standard system catalogs such as iitables can still be queried.

**[NO]SESSION_PRIORITY**

!!! note "Note"

    Whether this privilege has an effect depends on the operating system.

:   Determines whether a session is allowed to change its priority, and if so, its initial and highest priority.

:   If NOSESSION_PRIORITY (the default) is specified, users can not alter their session priority.

:   If SESSION_PRIORITY is specified, users can alter their session priority, up to the limit determined by the privilege.

**[NO]TIMEOUT_ABORT**

:   Allows the specified authorization IDs to issue the SET JOINOP TIMEOUTABORT statement.

:   NOTIMEOUT_ABORT prevents the specified users, groups, or roles from issuing the SET JOINOP TIMEOUTABORT statement.

:   Default: Everyone can issue the SET JOINOP TIMEOUTABORT statement.

!!! note "Note"

    The restrictions set by QUERY_COST_LIMIT, QUERY_CPU_LIMIT, QUERY_IO_LIMIT, QUERY_PAGE_LIMIT, and QUERY_ROW_LIMIT are enforced based on estimates from the Actian Data Platform query optimizer. If the optimizer predicts that a query consumes more I/Os than allowed by the session, the query is terminated prior to execution. The accuracy of the optimizer’s estimates can be impeded by out-of-date or insufficient statistics about the contents of tables. For QUERY_ROW_LIMIT, actuals rather than estimates can be used.

### PROCEDURE Privileges

The EXECUTE privilege allows the grantee to execute the specified database procedures. To grant the EXECUTE privilege on database procedures, the owner of the procedure must have GRANT OPTION for all the privileges required to execute the procedure. To grant the EXECUTE privilege on database procedures that the grantor does not own, the grantor must have EXECUTE privilege WITH GRANT OPTION for the database procedure.

### DBEVENT Privileges

Database event privileges are as follows:

**RAISE**

:   Allows the specified authorization IDs to raise the database event (using the RAISE DBEVENT statement)

**REGISTER**

:   Allows the specified authorization IDs to register to receive a specified database event (using the REGISTER DBEVENT statement)

### SEQUENCE Privileges

The sequence privilege is as follows:

**NEXT**

:   Allows the grantee to execute the NEXT VALUE and CURRENT VALUE functions on the specified sequences. To grant the NEXT privilege on sequences, the grantor must either own the sequence or have NEXT privilege WITH GRANT OPTION for the sequence.

## Privilege Defaults

Privilege defaults are as follows:

| Privilege | Default |
| --- | --- |
| SELECT  INSERT  DELETE  UPDATE | Only the owner can perform select, insert, delete, or update operations on objects it owns. |
| REFERENCES | Only the table owner can create referential constraints that see its tables. |
| EXECUTE | Only the owner of a database procedure can execute the procedure. |
| RAISE | Only the owner of a database event can raise the event. |
| REGISTER | Only the owner of a database event can register to receive the event. |
| NEXT | Only the owner of a database sequence can execute the next value and current value operators on the sequence. |

Database privilege defaults are as follows:

| Privilege | Description |
| --- | --- |
| CREATE_TABLE | Any user can create tables (create_table). |
| DB_ADMIN | For a specified database, the DBA of the database and users that have the security privilege have the db_admin privilege. All other users of the database have nodb_admin privilege. |

## GRANT ALL PRIVILEGES Option

The following sections describe the results of the GRANT ALL PRIVILEGES option.

### Installation and Database Privileges

If GRANT ALL PRIVILEGES ON DATABASE or GRANT ALL PRIVILEGES ON CURRENT INSTALLATION is specified, the grantees receive the following database privileges:

- CREATE_TABLE
- RAISE DBEVENT

- REGISTER DBEVENT

Privileges granted on a specific database override privileges granted on current installation.

### Other Privileges

The requirements for granting all privileges on tables, views, database procedures, and database events depend on the type of object and the owner. To grant a privilege on an object owned by another user, the grantor or public must have been granted the privilege WITH GRANT OPTION. Only the privileges for which the grantor or public has GRANT OPTION are granted.

The following example illustrates the results of the GRANT ALL PRIVILEGES option. The accounting_mgr user creates the following employee table:

```
CREATE TABLE employee (name CHAR(25), department CHAR(5),	 salary MONEY)...
```

and, using the following GRANT statement, grants the accounting_supervisor user the ability to select all columns but only allows accounting_supervisor to update the department column (to prevent unauthorized changes of the salary column):

```
GRANT SELECT, UPDATE (department) ON TABLE employees TO accounting_supervisor WITH GRANT OPTION;
```

If the accounting_supervisor user issues the following GRANT statement:

```
GRANT ALL PRIVILEGES ON TABLE employees TO accounting_clerk;
```

the accounting_clerk user receives SELECT and UPDATE(department) privileges.

### Granting All Privileges on Views

The results of granting all privileges on a view you do not own are determined as follows:

| Privilege | Results |
| --- | --- |
| SELECT | Granted if the grantor can grant SELECT privilege on all tables and views in the view definition. |
| UPDATE | Granted for all columns for which the grantor can grant UPDATE privilege. If the grantor was granted UPDATE...WITH GRANT OPTION on a subset of the columns of a table, UPDATE is granted only for those columns. |
| INSERT | Granted if the grantor can grant INSERT privilege on all tables and views in the view definition. |
| DELETE | Granted if the grantor can grant DELETE privilege on all tables and views in the view definition. |
| REFERENCES | The REFERENCES privilege is not valid for views. |

## GRANT OPTION Clause

To enable an authorization ID to grant a privilege to another authorization ID, specify the WITH GRANT OPTION clause. The owner of an object can grant any privilege to any authorization ID (or to public). The authorization ID to whom the privilege is granted WITH GRANT OPTION can grant only the specified privilege. Any authorization ID can grant privileges that were granted to PUBLIC WITH GRANT OPTION to any other authorization ID.

The GRANT OPTION cannot be specified for database privileges.

For example, if user, tony, creates a table called mytable and issues the following statement:

```
GRANT SELECT ON tony.mytable TO laura        WITH GRANT OPTION;
```

User, laura, can select data from tony.mytable and can authorize user evan to select data from tony.mytable by issuing the following statement:

```
GRANT SELECT ON tony.mytable TO evan;
```

Because user laura did not specify the WITH GRANT OPTION clause, user evan cannot authorize another user to select data from tony.mytable. User laura can grant SELECT privilege, but cannot grant, for example, INSERT privilege. If user tony revokes SELECT permission from user laura (using the REVOKE statement), user tony must specify how Actian Data Platform must handle any dependent privileges that user laura has issued.

The choices are:

**REVOKE...CASCADE**

:   Revokes all dependent privileges. In the preceding example, SELECT permission is revoked from user evan.

**REVOKE...RESTRICT**

:   Does not revoke specified privileges if there are dependent privileges. In the preceding example, SELECT privileges are not revoked from user laura because her grant to user evan depends on the privileges she received fromuser tony.

## GRANT (PRIVILEGE) Examples

The following are GRANT (privilege) statement examples:

1. Grant select and update privileges on the salary table to the group, acct_clerk.

```
GRANT SELECT, UPDATE ON TABLE salary     TO GROUP acct_clerk;
```

2. Grant update privilege on the columns, empname and empaddress, in the employee table to the users, joank and gerryr.

```
GRANT UPDATE(empname, empaddress)     ON TABLE employee     TO joank, gerryr;
```

3. Enable any employee in accounting to change columns containing salary information.

```
GRANT UPDATE ON employee.salary, employee.socsec    TO GROUP accounting;
```

4. Enable the accounting manager, rickr, complete access to salary information and to grant permissions to other user.

```
GRANT ALL ON employee TO rickr WITH GRANT OPTION;
```

5. Enable any user to create a table constraint that references the employee roster.

```
GRANT REFERENCES ON emp_roster TO PUBLIC;
```
