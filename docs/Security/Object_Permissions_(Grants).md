---
title: "Object Permissions (Grants)"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Object_Permissions_(Grants).htm"
canonical_id: "actian-data-platform-object-permissions-grants"
---

## Object Permissions (Grants)

Anobject permission defines a capability related to a specific object, such as a database or a table. Object permissions are assigned to selected groups, roles, or users. Object permissions are also called grants, permits, or object privileges.

The owner of the object can grant and revoke object permissions and can grant other users the privilege to grant permission on the object. The granting of permissions is typically the DBA’s responsibility.

Using permissions, data access can be restricted in several ways. Grants on objects can range from general to specific.

Permissions are classified according to the type of objects they affect. Object types include:

- Database
- Table

- View
- Procedure

- Database event
- Role

- Current installation

## Working with Grants

You can perform the following basic operations on grants (object permissions):

- Grant any permission allowed for a particular object type to any group, role, or user (including public, which encompasses all current and future users)
- View all types of object permissions granted to a particular group, role, or user, or view the permissions granted for a particular object type

- Revoke a previously granted permission

In SQL, you can grant and revoke permissions using the GRANT and REVOKE statements. To display granted privileges, select data from the iidbprivileges system catalog. For more information, see [iidbprivileges Catalog](../SQLLanguage/Standard_Catalogs_for_iidbdb.md).

### Object Ownership and Granting Object Permissions

When you create an object, you become the owner of that object.

As the owner, you are automatically entitled to grant and revoke permissions for the object (with views, you must also own the base tables). When you grant permissions for an object (other than a database) to another user, you can also grant permission for that user to grant permissions for the object to other users, and you can likewise revoke that permission if necessary.

### The GRANT Statement

The GRANT statement is used to grant permissions. This statement has the general form:

```
GRANT privilege ON object TO whom
```

The full syntax of a GRANT statement is:

```
GRANT ALL [PRIVILEGES] | privilege {, privilege}   [ON [object_type] [schema.]object_name {, [schema.]object_name}]   TO PUBLIC | [authorization_type] auth_id {, auth_id} [WITH GRANT OPTION];
```

The default object type is TABLE, which is used for any table or view. The default authorization type is USER.

Authorization identifiers specify who is receiving the permissions. Authorizations can be specified for:

- Individual users

    Permissions defined by a particular GRANT statement can be issued to one or more end users, specifying the login user identifier.

- The key word PUBLIC, which includes all users. The authorization type PUBLIC is not followed by any auth_ids.

    For example: Grant all query permissions for the games table to all sessions:

```
GRANT ALL ON games TO PUBLIC;
```

- A defined group
- A defined role

Authorizations for the individual user and PUBLIC are always in effect but can be adjusted by group and role permissions.

For complete information on the GRANT statement, see the SQL Language Guide.

## Database Grants

Database permissionsare defined on the database as a whole. They set a number of limits that affect the authorization identifiers(that is, groups, roles, users, or public) specified when the grant is defined.

Notes:

- Most of the database permissions are prohibitingpermissions—if not specified, the default is no restrictions. Prohibiting permissions, even if defined, are not enforced for the owner of the database or for any user with the SECURITY privilege, such as the system administrator.
- To override the default for database permission, create a grant for the permission that specifies the grantee as public.

The valid database permissions are as follows:

**[NO]CONNECT_TIME_LIMIT**

:   Specifies the maximum time (in seconds) that a session can consume.

:   Default: No connect time limit

**[NO]CREATE_PROCEDURE**

:   Enables grantees to create database procedures in the database.

:   Default: All authorization identifiers can create database procedures.

**[NO]CREATE_TABLE**

:   Enables grantees to create tables in the database.

:   Default: All authorization identifiers can create tables.

**[NO]DB_ADMIN**

:   Gives grantees unlimited database privileges for the database and the ability to impersonate another user (using the -u flag in the [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md)).

:   Default: Granted to the owner of the database and to any user with the security privilege, such as the system administrator. For all other users, the default is not to allow unlimited database privileges.

**[NO]IDLE_TIME_LIMIT**

:   Specifies the maximum time that a session can take between issuing statements.

:   Default: No idle time limit

**[NO]LOCKMODE**

:   Enables grantees to issue the SET LOCKMODE statement.

:   Default: All authorization identifiers can issue the SET LOCKMODE statement.

**[NO]QUERY_COST_LIMIT**

:   Specifies the maximum cost per query on the database, in terms of disk I/O and CPU usage.

:   Default: All authorization identifiers are allowed an unlimited cost per query.

**[NO]QUERY_CPU_LIMIT**

:   Specifies the maximum CPU usage per query on the database.

:   Default: All authorization identifiers are allowed unlimited CPU usage per query.

**[NO]QUERY_IO_LIMIT**

:   Specifies the maximum number of I/O requests per query on the database.

:   Default: All authorization identifiers are allowed an unlimited number of I/O requests.

**[NO]QUERY_PAGE_LIMIT**

:   Specifies the maximum number pages per query on the database.

:   Default: All authorization identifiers are allowed an unlimited number of pages per query.

**[ACTUAL | ESTIMATED] [NO]QUERY_ROW_LIMIT**

:   Specifies the maximum ESTIMATED or ACTUAL number of rows returned per query on the database. ESTIMATED is the default behavior and does not need to be specified.

:   Default: All authorization identifiers are allowed an unlimited number of rows per query.

**[NO]SELECT_SYSCAT**

:   Allows a session to query system catalogs to determine schema information.

:   Default: Sessions are allowed to query the system catalogs.

**[NO]SESSION_PRIORITY**

!!! note "Note"

    Whether this privilege has an effect depends on the operating system.

:   Determines whether a session is allowed to change its priority, and if so what its initial and highest priority can be.

:   Default: A session cannot change its priority.

**[NO]UPDATE_SYSCAT**

:   Allows grantees to update system catalogs.

:   Default: No authorization identifier can update system catalogs.

:   For more information about system catalogs, see [System Catalogs](../SQLLanguage/System_Catalogs.md).

For complete information on these and more permissions, see [DATABASE Privileges](../SQLLanguage/GRANT_(privilege).md).

!!! note "Note"

    The restrictions set by QUERY_COST_LIMIT, QUERY_CPU_LIMIT, QUERY_IO_LIMIT, QUERY_PAGE_LIMIT, and QUERY_ROW_LIMIT are enforced based on estimates from the DBMS query optimizer. If the optimizer predicts that a query can require more I/O operations or return more rows than are allowed for the session, the query is terminated prior to execution. This prevents resource consumption by queries that are not likely to succeed. The accuracy of the optimizer’s estimates can be impeded by out-of-date or insufficient statistics about the contents of tables. For QUERY_ROW_LIMIT, you can specify that actuals rather than estimates be used.

**Preventing Permissions**—Each permission has a corresponding preventing permissionto specifically disallow the permission. For example, to prevent access to the database, specify the NOACCESS permission.

### How Database Permissions for a Session are Determined

The database permissions for a session are calculated when the session connects to the database and remain in effect for the duration of the session. If, after a session connects to a database, the database permissions for one of that session’s authorization identifiers are changed, the active session is not affected. Any new sessions that are established with the same authorization identifiers are subject to the revised database permissions.

### Database Grant Examples

Here are examples of granting permissions on a database:

1. Define a query row limit of 100 rows on the new_accts database for user ralph:

```
GRANT QUERY_ROW_LIMIT 100ON DATABASE new_accts TO ralph;
```

2. Prohibit group prodramsfrom creating tables and database procedures in the new_accts database:

```
GRANT NOCREATE_TABLE, NOCREATE_PROCEDURE ON DATABASE new_accts TO prodrams;
```

3. A database privilege can be superseded by issuing a subsequent GRANT statement for the user authorization. For example, assume that user karenk has been granted a query row limit of 1000 rows on the customers database:

```
GRANT QUERY_ROW_LIMIT 1000ON DATABASE customers TO karenk;
```

    Her job changes and she does not need to access so much of the database, so the DBA issues a new GRANT statement giving her a query row limit of 250:

```
GRANT QUERY_ROW_LIMIT 250ON DATABASE customers TO karenk;
```

    This new privilege replaces the old 1000-row privilege. If the DBA subsequently revokes the new limit:

```
GRANT NOQUERY_ROW_LIMIT ON DATABASE customers TO karenk;
```

    karenk’s QUERY_ROW_LIMIT privilege for the database becomes undefined (the old limit of 1000 is not re-established). At this point if no value for QUERY_ROW_LIMIT has been defined for any of the other authorization identifiers associated with karenk’s session, then the number of rows that her session’s queries can return is unrestricted.

## Table and View Grants

The Actian Data Platform allows data sharing and updating if users have been issued grant permissions on the tables or views used in the query.

Table and view permissions are enablingpermissions—if no permission is granted, the default is to prohibit access. Table and view permissions are not enforced for the owner of the table or view.

#### Permissions on Tables and Views

The following query permissions can be granted on both tables and views:

**SELECT**

:   Enables grantees to select rows from the table or view, for example using a SELECT statement or a WHERE clause.

**INSERT**

:   Enables grantees to add rows to the table or view, for example using an INSERT statement.

**DELETE**

:   Enables grantees to delete rows from the table or view, for example using a DELETE statement.

**UPDATE**

:   Enables grantees to change existing rows in the table or view, for example using an UPDATE statement. An update grant can apply to all columns in the table or view, or only to specific columns.

#### Permissions on Tables

The following query permissions can be granted on tables only:

**COPY_INTO**

:   Enables grantees to copy the contents of the table to a data file, for example using the INTO clause of the COPY statement.

**COPY_FROM**

:   Enables grantees to copy the contents of a file to the table, for example using the FROM clause of the COPY statement.

**REFERENCES**

:   Enables grantees to create tables that reference the table. A references grant can apply to all columns in the table, or only to specific columns.

    If a user is not the owner and does not have the references permission on a table, that user cannot create a referential constraint that references the table.

## Table Grant Examples

Here are examples of granting permissions on tables:

1. Grant select permission on the employee table to user freddy:

```
GRANT SELECT ON employee TO freddy;
```

2. Grant select permission on the employee and department_table tables to individual users sally and ralph:

```
GRANT SELECT ON employee, department_tableTO sally, ralph;
```

3. Grant both select and update permissions on the employee table to user rollin. Note that you must be able to select values to update them:

```
GRANT SELECT, UPDATE ON employee TO rollin;
```

4. Grant select and update permissions on the columns empname and empaddress in the employee table to users vidals and gerryr:

```
GRANT SELECT, UPDATE (empname, empaddress)ON employee TO vidals, gerryr;
```

5. Grant references permission on the address table to user joe:

```
GRANT REFERENCES ON address TO joe;
```

6. Grant references permission on selected columns of the finder table to user joe:

```
GRANT REFERENCES ON finder (lname, finit, state)TO joe;
```

    User joe can then create a referential constraint on table address or the specified columns of table finder. Note that he does not need the select permission to create the referential constraint.

7. Grant all query permissions (SELECT, INSERT, UPDATE, DELETE, and REFERENCES) on the phonelist table to all users:

```
GRANT ALL ON phonelist TO PUBLIC;
```

## Procedure Grants

For database procedures, the only valid permission is the EXECUTE permission, which allows the grantees to execute the procedure.

Granting permission to execute a procedure makes database queries contained in the procedure code available to grantees. Granting execute permission to a database procedure also allows grantees to create rules that trigger the procedure.

The EXECUTE permission is an enablingpermission. By default, execution is prohibited unless the permission is specifically granted. This permission is not enforced for the owner of the procedure.

Permission to create procedures in the database is described in [Database Grants](../Security/Object_Permissions_(Grants).md).

## Database Event Grants

The valid database event permissions are summarized below:

**RAISE**

:   Allows grantees to raise the database event (using the [RAISE DBEVENT](../SQLLanguage/RAISE_DBEVENT.md) statement).

**REGISTER**

:   Allows grantees to register to receive the database event (using the [REGISTER DBEVENT](../SQLLanguage/REGISTER_DBEVENT.md) statement).

These are enablingpermissions—by default, execution is prohibited unless the permission is specifically granted. Database event permissions are not enforced for the owner of the event.

## Role Grants

When a role is created, an implicit grant is issued on the role to the user creating the role.

Role access must be granted to other users (or public) before they can use the role. Role access is an enablingpermission—by default, access to the role is prohibited unless the permission is specifically granted.

## How Grants Restrict Data Access

Grants allow for data access to be restricted in the following ways:

- Operational restrictions (for example, SELECT, INSERT, UPDATE, and DELETE permissions applied to some or all of the columns of a table)
- Data value restrictions (data restrictions), which are implemented through views

- Resource restrictions, which are permissions defined for the database as a whole, rather than individual tables or columns

In a session where permissions are in effect, when you issue a query (for example, from an application), the query is passed to the warehouse. The Actian Data Platform then evaluates the grants on the tables involved in the query. If an operation does not pass an operational restriction, an error message is returned.

If an operation does not pass a data restriction, it means that views are being used and grants have been placed on the views, but the user authorization does not pass the grants on the data. In this case no error is returned, but the number of rows returned is affected. For example, if Anupama is accessing a view that returns rows only from the Shoe department, if she asks for information from the Toy department, no rows are returned.
