---
title: "Grant Overhead"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Grant_Overhead.htm"
canonical_id: "actian-data-platform-grant-overhead"
---

## Grant Overhead

Grants can affect query processing time. Queries for a table or view have overhead if:

- Permissions have been granted on the table or view
- Column-specific permissions are granted

- Many permissions are granted in general in the database

For the following, however, there is no overhead:

- For the table owner
- On certain public grants:

    - –In****SELECT operations

    - –Any operation for which all allowed permissions are specified for PUBLIC

- If no permissions qualify (the query is simply terminated)

There is additional overhead during session initialization to evaluate database privileges for the authorization identifiers associated with the session. Because session initialization must read the catalogs in which groups, roles, and database privileges are stored, certain operations issued by the DBA or system administrator that write to these catalogs can be committed or rolled back as soon as possible. These operations include:

- Granting or revoking database privileges
- Creating, altering, or dropping a group

- Creating, altering, or dropping a role

## Multiple Permission Checks

Multiple permissions can apply to the same query, because the system catalog is scanned for all possible permissions that apply. Generally, this means the broadest grant applies. The hierarchy of evaluation is described in more detail below, but the hierarchy is generally not something the DBA needs to formally consider.

For example, assume that grants have been created to allow all permissions on the employee table to PUBLIC, and that a grant has been created to allow a particular user, Susan, the SELECT privilege on the employee table. Susan, as part of the public, can perform all operations on the employee table, even though her individual grant was only for SELECT permission.

!!! note "Note"

    If you want more restrictive grants to apply, the solution is to drop the inclusive grants to PUBLIC and define specific grants for specified groups or users.

## How Privileges for a Session Are Determined

In any session, the privileges in effect for that session are derived from the privileges granted to the authorization identifiers (role, user, group, and public) associated with the session, and any applicable defaults. If a particular privilege is defined for more than one authorization identifier associated with a session, then a hierarchy is used to determine which defined privilege is enforced for that session.

The authorization hierarchy, in order of highest to lowest precedence, is:

1. role
2. user

3. group
4. public

For each accessed object in a session, there is a search for a defined privilege that specifies that object and the desired access characteristics (for example, SELECT, INSERT, EXECUTE, and so on).

### Access to Tables, Views, or Procedures and the Authorization Hierarchy

If the specified object attempting to be accessed is a table, view, or database procedure, then one of the authorization identifiers in effect for the session must have the required privilege for that object for the session to access that object. In the case of these grantedprivileges that are otherwise restricted, the authorization identifiers are searched for one that gives the required authorization.

For example, to insert into a specified table, one of the authorization identifiers associated with the session must have the INSERT permission defined for the specified table. If none of the authorization identifiers associated with the session has this permission and the user does not own the table, then the internal default is used. In this case, because the internal default for the INSERT permission is not to allow inserts, inserts are not allowed into the specified table.

### Access to Databases and the Authorization Hierarchy

When the specified object attempting to be accessed is the database, the authorization hierarchy is also important because the privileges defined on the database can be defined with different values for different authorization identifiers. When a database privilege is defined at differing levels, the hierarchy is used to determine which privilege to enforce.

For example, assume that query row limits have been defined differently for each authorization level as follows:

| Authorization Identifier | Query Row Limit |
| --- | --- |
| The role identifier | 1700 |
| The user | 1500 |
| The group identifier | 2000 |
| The public | 1000 |

If a user starts a session and specifies both group and role identifiers, the limit defined for the role is enforced because it has the highest order of precedence in the hierarchy, giving the session a query row limit of 1700.

Several other possible scenarios include:

- If NOQUERY_ROW_LIMIT was defined for role, then the query row limit defined for that user is enforced, which is 1500 rows. This is also the case if the user had not specified a role identifier.
- If NOQUERY_ROW_LIMIT was defined for that user, then the query row limit defined for the group (2000 rows) is enforced.

- If NOQUERY_ROW_LIMIT was defined for group, or if the user had not specified a group identifier, then the query row limit defined for public (1000 rows) is enforced.
- If none of the identifiers had QUERY_ROW_LIMIT defined, the internal default is enforced, which in this case is an unlimited numbers of rows.

!!! note "Note"

    In cases where multiple authorizations apply, the resource limit associated with the highest order of precedence applies, not necessarily the one that grants the most resources.

## How Database Privileges for a Session Are Determined

The authorization hierarchy (see [How Privileges for a Session Are Determined](../Security/Grant_Overhead.md)) is used to determine the session’s database privileges. The hierarchy includes the privileges granted to the authorization identifiers in effect for the session, and the internal defaults.

When a user begins a session:

- If the user has a default group identifier defined for the user ID (that is, dbmadmingrp), the default group identifier is automatically applied to the session. A default group identifier can be specified for a user when a user is created or modified. For more information, see Example 3 in [Add Native Users](../User/Add_Native_Users.md).
- For users who do not have assigned default group identifier defined for the user ID, the privileges in effect for the session are derived from the privileges defined for the user identifier and for public. For example, while you might have the privilege to select all the tables in the database, you might only have the update permission on a limited number of those tables. To ensure the user has access to privileges in effect for the session, in the [Actian SQL CLI](../SQLLanguage/Actian_SQL_CLI.md) the user needs to include the -G or -R flag, or both, when beginning the session, then the privileges for the specified group or role identifier are also in effect for the session. For JDBC and ODBC connections, see the groupName and roleName data source properties in the Connectivity Guide.

## DBMSINFO--View Permissions for Current Session

You can use the DBMSINFO function to obtain the current value of any database privilege in effect for the current session.

To issue a DBMSINFO request, use the following syntax:

```
SELECT DBMSINFO('request_name');
```

The request_name can be any of the following parameters:

**CONNECT_TIME_LIMIT**

:   The session’s value for the connect time limit, or ‑1 if none

**CREATE_PROCEDURE**

:   “Y” if the session has create procedure privileges or “N” if not

**CREATE_TABLE**

:   “Y” if the session has create table privileges or “N” if not

**DB_ADMIN**

:   “Y” if the session has DB admin privileges or “N” if not

**IDLE_TIME_LIMIT**

:   The session’s value for the idle time limit or -1 if none

**LOCKMODE**

:   “Y” if the session can issue the SET LOCKMODE statement or “N” if not

**QUERY_COST_LIMIT**

:   The session’s value for the query cost limit or -1 if none

**QUERY_CPU_LIMIT**

:   The session’s value for the CPU limit or -1 if none

**QUERY_IO_LIMIT**

:   The session’s value for the query I/O limit or -1 if none

**QUERY_PAGE_LIMIT**

:   The session’s value for the query page limit or -1 if none

**QUERY_ROW_LIMIT**

:   The session’s value for the query row limit or -1 if none

**SESSION_PRIORITY**

:   The session’s current priority or -1 if none

**SELECT_SYSCAT**

:   “Y” if the session has the SELECT_SYSCAT privilege or “N” if not

**UPDATE_SYSCAT**

:   “Y” if the session has the UPDATE_SYSCAT privilege or “N” if not

### Example: Return the Value of Query Row Limit for Current Session

Assuming the QUERY_ROW_LIMIT permission for the current session is 50, the following query returns the value “50”:

```
SELECT DBMSINFO('QUERY_ROW_LIMIT');
```

!!! note "Note"

    The DBMSINFO function allows other request_namevalues relating to other aspects of the current session. For more information, see the DBMSINFO Function in the SQL Language Guide.
