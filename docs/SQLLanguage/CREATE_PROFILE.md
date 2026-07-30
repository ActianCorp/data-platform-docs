---
title: "CREATE PROFILE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_PROFILE.htm"
canonical_id: "actian-data-platform-create-profile"
---

## CREATE PROFILE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE PROFILE statement creates a new user profile.

A user profile is a set of subject privileges and other attributes that can be applied to a user or set of users. Each user can be given a profile, which provides the default attributes for that user.

A profile includes:

- Subject privileges
- Default subject privileges

- Default user groups
- Security auditing attributes

- Expire date

A default profile, which can be changed by the system administrator, is created during installation. It determines the default user attributes when no profile is specified. The initial default profile is:

- NOPRIVILEGES
- NODEFAULT_PRIVILEGES

- NOEXPIRE_DATE
- NOGROUP

#### Syntax

The CREATE PROFILE statement has the following format:

```
[EXEC SQL] CREATE PROFILE profile_name [WITH with_item {,with_item}]with_item = NOPRIVILEGES | PRIVILEGES = ( priv {, priv} )              | NOGROUP | GROUP = default_group               | SECURITY_AUDIT= ( audit_opt {,audit_opt})              | NOEXPIRE_DATE | EXPIRE_DATE = 'expire_date'               | DEFAULT_PRIVILEGES = (priv {,priv})| ALL              | NODEFAULT_PRIVILEGES
```

**profile_name**

:   Defines the name of the profile that is being created. Must be a valid object name that is unique in the installation.

**priv**

:   Specifies a subject privilege, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

:   Default: NOPRIVILEGES if the privileges clause is omitted.

**default_group**

:   Specifies the default group for users with this profile. Must be an existing group. For more information about groups, see [CREATE GROUP](../SQLLanguage/CREATE_GROUP.md). To specify that the user is not assigned to a group, use the NOGROUP option. If the GROUP clause is omitted, the default is NOGROUP.

**audit_opt**

:   Defines security audit options, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

**expire_date**

:   Specifies an optional expiration date associated with each user using this profile. Any valid date can be used. When the expiration date is reached, the user is no longer able to log on. If NOEXPIRE_DATE is specified, this profile has no expiration limit.

**DEFAULT_PRIVILEGES = ( priv {, priv} ) | ALL | NODEFAULT_PRIVILEGES**

:   Defines the privileges initially active. These must be a subset of those privileges granted to the user.

ALL

:   All the privileges held by the profile are initially active.

NODEFAULT_PRIVILEGES

:   No privileges are initially active.

## CREATE PROFILE Examples

1. Specify a profile for a particular user.

```
CREATE PROFILE dbop;    CREATE USER bspring WITH PROFILE = dbop;
```

2. Create a dbop profile with the appropriate privileges to maintain a database.

```
CREATE PROFILE dbop WITH PRIVILEGES = (OPERATOR, TRACE),GROUP = dbopgroup;
```
