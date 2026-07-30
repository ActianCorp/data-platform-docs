---
title: "REVOKE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "REVOKE.htm"
canonical_id: "actian-data-platform-revoke"
---

## REVOKE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The REVOKE statement revokes privileges. It removes database privileges or role access granted to the specified users, groups, roles, or PUBLIC. (To confer privileges, use the GRANT statement.)You cannot revoke privileges granted by other users.

#### Syntax

The REVOKE statement has the following format:

```
[EXEC SQL] REVOKE [GRANT OPTION FOR]              ALL [PRIVILEGES] | privilege {, privilege} | role {, role}              [ON [object_type] [schema.]objectname {, [schema.]object_name} |                             CURRENT INSTALLATION]              FROM PUBLIC | [auth_type] auth_id {, auth_id}              [CASCADE | RESTRICT];
```

**privilege**

:   Specifies the privileges to revoke. To revoke all privileges, use ALL. The privileges must agree with the object_type as follows:

| Object Type | Valid Privileges |
| --- | --- |
| Table (omit object_type) | COPY_INTOCOPY_FROMDELETEEXCLUDINGINSERTREFERENCESSELECTUPDATE |
| DATABASE (or CURRENT INSTALLATION) | [NO]ACCESS[NO]CONNECT_TIME_LIMIT[NO] CREATE PROCEDURE[NO]CREATE_TABLE[NO]DB_ADMIN[NO]IDLE_TIME_LIMIT[NO]QUERY_COST_LIMIT[NO]QUERY_CPU_LIMIT[NO]QUERY_PAGE_LIMIT[ACTUAL] [NO]QUERY_ROW_LIMIT[NO]QUERY_ROW_STEP_LIMIT[NO]READONLY[NO]SELECT_SYSCAT[NO]SESSION_PRIORITY[NO]TIMEOUT_ABORT[NO]UPDATE_SYSCAT |
| PROCEDURE | EXECUTE |
| DBEVENT | REGISTERRAISE |
| SEQUENCE | NEXT |
| Role | Omit this clause |

**object_type**

:   Specifies the type of object on which the privileges were granted. To revoke permission on a table, omit the object_type parameter. Valid object_types are:

DATABASE

PROCEDURE

DBEVENT

SEQUENCE

**object_name**

:   Specifies the name of the table, database procedure, database event, or role on which the privileges were granted.

**auth_type**

:   Specifies the type of authorization identifier to which privileges were granted. Auth_type must be USER, GROUP, or ROLE. The default is USER. More than one auth_type cannot be specified.

**auth_id**

:   Specifies the users, groups, or roles from which privileges are being revoked. The auth_ids must agree with the type specified by the auth_type.

    For example, if you specify GROUP as auth_type, the auth_id list must be a list of group identifiers. If you specify PUBLIC for the auth_id, you must omitauth_type. You can revoke from users and PUBLIC in the same REVOKE statement.

Revoking a database privilege makes that privilege on the specified database undefined for the specified grantee (auth_id). If an attempt is made to revoke a privilege that was not granted to a specified auth_id, no changes are made to the privileges of that auth_id.

Privileges granted on specific databases are not affected by REVOKE...ON CURRENT INSTALLATION, and privileges granted on current installation are not affected by REVOKE...ON DATABASE. Revoking privileges from PUBLIC does not affect privileges granted to a specific user.

If a privilege was granted using its “no” form (for example, NOCREATE_TABLE), the same form must be used when revoking the privilege. For example, the following grant prevents a user from creating tables:

```
GRANT NOCREATE_TABLE ON DATABASE employee         TO USER karenk;
```

To remove this restriction:

```
REVOKE NOCREATE_TABLE ON DATABASE employee         FROM USER karenk;
```

For more information about privileges, see [GRANT (privilege)](../SQLLanguage/GRANT_(privilege).md).

!!! note "Note"

    In some cases granting a database privilege imposes a restriction, and revoking the privilege removes the restriction. For example, GRANT NOCREATE_TABLE prevents the user from creating tables.

## Revoking Grant Option

The GRANT statement GRANT OPTION enables users other than the owner of an object to grant privileges on that object. For example, the following statement enables mike to grant the select privilege (with or without grant option) to other users:

```
GRANT SELECT ON employee_roster TO mike WITH GRANT OPTION;
```

The GRANT OPTION can be revoked without revoking the privilege with which it was granted. For example, the following statement:

```
REVOKE GRANT OPTION FOR SELECT ON employees FROM mike...
```

means that mike can still select data from the employees table, but cannot grant the select privilege to other users. (The grant option cannot be specified for database privileges.)

## Restrict versus Cascade

The RESTRICT and CASCADE options specify how Actian Data Platformhandles dependent privileges. The CASCADE option directs Actian Data Platform to revoke the specified privileges plus all privileges and objects that depend on the privileges being revoked. The RESTRICT option directs Actian Data Platform not to revoke the specified privilege if there are any dependent privileges or objects.

The owner of an object can grant privileges on that object to any user, group, or role. Privileges granted by users who do not own the object are dependent on the privileges granted WITH GRANT OPTION by the owner.

For example, if user jerry owns the employees table, he can grant tom the ability to select data from the table and to enable other users to select data from the table:

```
GRANT SELECT ON employees TO tom WITH GRANT OPTION;
```

User tom can now enable another user to select data from the employees table:

```
GRANT SELECT ON employees TO sylvester WITH GRANT OPTION;
```

The grant tom conferred on sylvester is dependent on the grant the table's owner jerry conferred on tom. In addition, sylvester can enable other users to select data from the employees table.

If sylvester creates a view on the employees table, that view depends on the SELECT privilege that tom granted to sylvester. For example:

```
CREATE VIEW njemps AS SELECT * FROM employees WHERE state='New Jersey'
```

To remove his grant to tom, all grants tom can have issued, and any dependent objects, jerry must specify REVOKE...CASCADE:

```
REVOKE SELECT ON employees FROM tom CASCADE;
```

As a result of this statement, the SELECT privilege granted by tom to sylvester is revoked, as are any SELECT grants issued by sylvester to other users conferring SELECT privilege for the employees table. The njemps view is destroyed.

To prevent dependent privileges from being revoked, jerry must specify REVOKE...RESTRICT:

```
REVOKE SELECT ON employees FROM tom RESTRICT;
```

Because there are dependent privileges (tom has granted SELECT privilege on the employees table to sylvester), this REVOKE statement fails, and no privileges are revoked. The njemps view is not destroyed.

!!! note "Note"

    If privileges are revoked from specific authorization IDs (users, groups, and roles) that were also granted to PUBLIC, privileges and objects that depend on the grants persist (until the privileges are revoked from PUBLIC).

The RESTRICT and CASCADE parameters have the same effect whether revoking a specific privilege or the GRANT OPTION for a specific privilege. In either case, RESTRICT prevents the operation from occurring if there are dependent privileges, and CASCADE causes dependent privileges to be deleted. When revoking a GRANT OPTION with CASCADE, all dependent privileges are revoked, not only the GRANT OPTION portion of the dependent privileges.

RESTRICT or CASCADE must be specified when revoking privileges on tables, database procedures, or database events. When revoking database privileges, CASCADE, RESTRICT or GRANT OPTION cannot be specified (because database privileges cannot be granted with GRANT OPTION).

## REVOKE Examples

The following are REVOKE statement examples:

1. Prevent any user from granting any form of access to the payroll table (assuming no privileges were granted to specific users, groups, or roles). Delete all dependent grants.

```
REVOKE GRANT OPTION FOR ALL ON payroll         FROM PUBLIC CASCADE;
```

2. Prevent user harry from selecting rows from the employees table (assuming the same privilege was not granted to public).

```
REVOKE SELECT ON employees         FROM harry CASCADE;
```

3. Prevent user roger from using role manager.

```
REVOKE manager FROM roger
```
