---
title: "ALTER PROFILE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_PROFILE.htm"
canonical_id: "actian-data-platform-alter-profile"
---

## ALTER PROFILE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The ALTER PROFILE statement alters a user profile.

A profile provides default attributes for a user.

#### Syntax

The ALTER PROFILE statement has the following format:

```
[EXEC SQL] ALTER [DEFAULT PROFILE | PROFILE profile_name][ADD PRIVILEGES( priv {,priv}) | DROP PRIVILEGES( priv {,priv})] [WITH with_item {, with_item}]with_item =     NOPRIVILEGES | PRIVILEGES = ( priv{, priv} )     | NOGROUP | GROUP = default_group     | NOSECURITY_AUDIT | SECURITY_AUDIT = ( audit_opt{,audit_opt})    | NOEXPIRE_DATE | EXPIRE_DATE = 'expire_date'     | NODEFAULT_PRIVILEGES | DEFAULT_PRIVILEGES = ( priv{, priv} ) | ALL
```

**ALTER DEFAULT PROFILE**

:   Modifies the settings of a default profile.

**ALTER PROFILE profile_name**

:   Modifies the settings of the specified profile. The profile_name can be a delimited identifier. It must be an existing profile.

:   DEFAULT and a profile_name cannot be specified in the same statement.

**ADD PRIVILEGES | DROP PRIVILEGES**

:   Adds or drops privileges to or from the user profile.

:   Only one of the following can be specified in a single ALTER PROFILE statement:

:   ADD PRIVILEGES ( priv{, priv})

:   DROP PRIVILEGES ( priv{, priv})

:   NOPRIVILEGES

:   PRIVILEGES = ( priv{, priv} )

**priv**

:   Specifies a subject privilege, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

!!! note "Note"

    These are requestable privileges. They must be activated using the SET SESSION ADD PRIVILEGES statement.

**GROUP = default_group**

:   Specifies the default group for users with this profile. The group must exist.

:   Use the NOGROUP option to specify that the user is not assigned to a group.

:   Default: NOGROUP if the GROUP clause is omitted.

**audit_opt**

:   Defines security audit options, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

**EXPIRE_DATE = expire_date**

:   Specifies an optional expiration date associated with each user using this profile.Any valid date can be used.When the expiration date is reached, the user is no longer able to log on.

:   If NOEXPIRE_DATE is specified, this profile has no expiration date.

**DEFAULT_PRIVILEGES = ( priv{, priv} ) | ALL**

:   Defines the privileges initially active.

priv

:   A subset of those privileges granted to the user.

ALL

:   All the privileges held by the profile are initially active.

**NODEFAULT_PRIVILEGES**

:   No privileges are initially active.

More information:

[CREATE PROFILE](../SQLLanguage/CREATE_PROFILE.md)

## ALTER PROFILE Examples

The following examples alter a user profile:

1. Update a default profile by using the alter default profile variant of the ALTER PROFILE statement.

```
ALTER DEFAULT PROFILEWITH EXPIRE_DATE = '30 days';
```

2. Alter the trusted profile to make the default group trusted_group:

```
ALTER PROFILE trusted ADD PRIVILEGES WITH GROUP = trusted_group
```

    All users currently using this profile have the appropriate changes made to their security privilege and group.
