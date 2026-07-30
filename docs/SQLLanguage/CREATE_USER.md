---
title: "CREATE USER"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_USER.htm"
canonical_id: "actian-data-platform-create-user"
---

## CREATE USER

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE USER statement defines a new user.

This statement has the following format:

```
[EXEC SQL] CREATE USER user_name [WITH with_item {, with_item}]with_item = NOPRIVILEGES | PRIVILEGES = ( priv {,priv} )             | NOGROUP | GROUP = default_group             | NOEXPIRE_DATE | EXPIRE_DATE = 'expire_date'             | DEFAULT_PRIVILEGES = (priv {,priv})| ALL             | NODEFAULT_PRIVILEGES             | NOPROFILE | PROFILE = profile_name             | NOPASSWORD | PASSWORD = 'user_password'            | PASSWORD = X'encrypted_role_password'             | EXTERNAL_PASSWORD            | DBMS_AUTHENTICATION = 'REQUIRED' | 'OPTIONAL'            | LONG_NAME = 'long_name_string'
```

**user_name**

:   Specifies the user name to be created. Must be a valid object name.

**priv**

:   Specifies one of the following subject privileges, which apply to the user regardless of the database to which the user is connected.

TRACE

:   Allows the user to use tracing and debugging features.

OPERATOR

:   Allows the user to perform database backups and other database maintenance operations.

MAINTAIN_USERS

:   Allows the user to perform various user-related functions, such as creating or altering users, profiles, group and roles, and to grant or revoke database and installation resource controls.

CHANGE_PASSWORD

:   Allows the user to change his password.

**default_group**

:   Specifies the default group to which the user belongs. It must be an existing group. For more information about groups, see [CREATE GROUP](../SQLLanguage/CREATE_GROUP.md).

:   If the GROUP clause is omitted, the default is NOGROUP, which means the user is not assigned to a group.

**expire_date**

:   Specifies an optional expiration date associated with each user. Any valid date can be used. Once the expiration date is reached, the user is no longer able to log on. If the expire_date clause is omitted, the default is NOEXPIRE_DATE.

**DEFAULT_PRIVILEGES = ( priv {, priv} ) | ALL | NODEFAULT_PRIVILEGES**

:   Defines the privileges initially active when connecting to Actian Data Platform. These must be a subset of those privileges granted to the user.

ALL

:   All the privileges held by the profile are initially active.

NODEFAULT_PRIVILEGES

:   No privileges are initially active. Allows default privileges to be removed.

**profile_name**

:   Allows a profile to be specified for a particular user. If the profile clause is omitted, the default is NOPROFILE.

**user_password**

:   Allows users to change their own password. If the oldpassword clause is missing or invalid the password is unchanged. In addition, users with the maintain_users privilege can change or remove any password.

**EXTERNAL_PASSWORD**

:   Allows a user’s password to be authenticated externally to Actian Data Platform. The password is passed to an external authentication server for authentication.

**DBMS_AUTHENTICATION =**

:   Indicates whether DBMS authentication is required or optional.

'REQUIRED'

:   Allows only connection requests that specify the user name and password defined at Actian Data Platform level and to a dbms_authentication enabled warehouse to succeed; other connections fail. Users with the “security” privilege, including the installation owner, cannot be defined as DBMS_AUTHENTICATION='REQUIRED'.

'OPTIONAL'

:   Allows connection requests that specify a user name and password defined at the operating system level, an installation password, or a Kerberos principle to succeed. In particular, this allows a local connection to a dbms_authentication server to succeed through implicit OS login authentication, without requiring the DBMS password.

:   Default: 'OPTIONAL'

**LONG_NAME = 'long_name_string'**

:   Specifies a unique long name of up to 160 characters that defaults to user_name. This is useful, for example, for user names from single sign-on applications such as Salesforce, which consist of a name, or a name and an email address. LONG_NAME must not match a different user’s user_name.

:   The connection will be verified (and authenticated, if DBMS authentication is turned on), matching either the user_name or long_name_string. After connection is initiated and the incoming name is validated, the short user_name will be used to identify object ownership, identify the session, locate grants and privileges, and perform all operations that user_name can do.

:   The session may query the long_name_string through DBMSINFO, regardless of whether the connection was established with long_name_string or user_name.

## CREATE USER Examples

1. Create a user with several privileges, and a smaller set of default privileges.

```
CREATE USER bspring    WITH PRIVILEGES=(TRACE,        DEFAULT_PRIVILEGES = (TRACE);
```

2. Create a user that requires authentication through the DBMS, rather than through operating system authentication, installation passwords, or Kerberos authentication. Allow the user to change his password:

```
CREATE USER fred     WITH PASSWORD='secret', PRIVILEGES = (CHANGE_PASSWORD),        DBMS_AUTHENTICATION='REQUIRED';
```
