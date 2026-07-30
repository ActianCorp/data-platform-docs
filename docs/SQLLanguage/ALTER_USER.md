---
title: "ALTER USER"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_USER.htm"
canonical_id: "actian-data-platform-alter-user"
---

## ALTER USER

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The ALTER USER statement changes the characteristics of an existing user.

!!! note "Note"

    You cannot use either ADD PRIVILEGES or DROP PRIVILEGES if a with_item is specified in the WITH clause.

This statement has the following format:

```
ALTER USER user_name [ADD PRIVILEGES (priv {, priv}) | DROP PRIVILEGES (priv {, priv})][WITH with_item {, with_item}]with_item = NOPRIVILEGES | PRIVILEGES = ( priv {, priv} )                | NOGROUP | GROUP = default_group                | NOEXPIRE_DATE | EXPIRE_DATE = 'expire_date'                | DEFAULT_PRIVILEGES = (priv {,priv})| ALL                | NODEFAULT_PRIVILEGES                | NOPROFILE | PROFILE= profile_name                | NOPASSWORD | PASSWORD = 'user_password'               | PASSWORD = X'encrypted_role_password'                | EXTERNAL_PASSWORD               | OLDPASSWORD = 'oldpassword'               | DBMS_AUTHENTICATION = 'REQUIRED' | 'OPTIONAL'               | LONG_NAME='long_name_string'
```

**user_name**

:   Specifies the user name. The user must be an existing Actian Data Platform user. If the user name contains non-alphanumeric characters, it must be enclosed in quotation marks (")—see example 10 in [ALTER USER Examples](../SQLLanguage/ALTER_USER.md).

**priv**

:   Specifies a subject privilege, as described in [CREATE USER](../SQLLanguage/CREATE_USER.md).

**default group**

:   Specifies the default group to which the user belongs. Must be an existing group. To specify that the user is not assigned to a group, use the NOGROUP option.

:   Default: NOGROUP if the group clause is omitted.

**expire_date**

:   Specifies an optional expiration date associated with the user. Any valid date can be used. Once the expiration date is reached, the user is no longer able to log on.

:   Default: NOEXPIRE_DATE if the EXPIRE_DATE clause is omitted

**DEFAULT_PRIVILEGES =**

:   Defines the privileges initially active when connecting to Actian Data Platform. These must be a subset of those privileges granted to the user.

:   When specified with ADD PRIVILEGE, the default privileges are added to the existing default privileges for the user; otherwise, the specified default privileges will replace the existing default privileges for the user.

**NODEFAULT_PRIVILEGES**

:   Specifies that the session is started with no privileges active. Allows default privileges to be removed.

**profile_name**

:   Allows a profile to be specified for a particular user.

:   Default: NOPROFILE if the profile clause is omitted.

**user_password**

:   Allows users to change their own password. If the OLDPASSWORD clause is missing or invalid, the password is unchanged. In addition, users with the maintain_users privilege can change or remove any password.

**EXTERNAL_PASSWORD =**

:   Allows a user’s password to be authenticated externally to Actian Data Platform. The password is passed to an external authentication server for authentication.

**oldpassword**

:   Specifies the user’s old password.

**DBMS_AUTHENTICATION =**

:   Indicates whether DBMS authentication is required or optional.

'REQUIRED'

:   Allows only connection requests that specify the user name and password defined at the Actian Data Platform level and to a dbms_authentication enabled warehouse to succeed; other connections fail. Users with the “security” privilege, including the installation owner, cannot be defined as DBMS_AUTHENTICATION='REQUIRED'.

'OPTIONAL'

:   Allows connection requests that specify a user name and password defined at the operating system level, an installation password, or a Kerberos principle to succeed. In particular, this allows a local connection to a dbms_authentication server to succeed through implicit OS login authentication, without requiring the DBMS password.

:   Default: 'OPTIONAL'

**LONG_NAME='long_name_string'**

:   Specifies a unique long name of up to 160 characters that defaults to user_name. This is useful, for example, for user names from single sign-on applications such as Salesforce, which consist of a name, or a name and an email address. LONG_NAME must not match a different user’s user_name.

:   The connection will be verified (and authenticated, if DBMS authentication is turned on), matching either the user_name or long_name_string. After connection is initiated and the incoming name is validated, the short user_name will be used to identify object ownership, identify the session, locate grants and privileges, and perform all operations that user_name can do.

:   The session may query the long_name_string through DBMSINFO, regardless of whether the connection was established with long_name_string or user_name.

## ALTER USER Examples

The following examples change the characteristics of an existing user:

1. Change an existing user, specifying privileges and group.

```
ALTER USER bspring WITH    GROUP = engineering,   NOPRIVILEGES;
```

2. Change an existing user, specifying group.

```
ALTER USER barney WITH    GROUP = marketing;
```

3. Specify no expiration date for a predefined user.

```
ALTER USER bspring WITH NOEXPIRE_DATE
```

4. Allow a user with maintain_users privilege to change or remove any password.

```
ALTER USER username   WITH PASSWORD='theirpassword'
```

5. Specify a profile for a particular user.

```
ALTER USER bspring WITH PROFILE = dbop
```

    where “dbop” is an existing profile.

6. Specify that a user has an externally verified password.

```
ALTER USER bspring WITH EXTERNAL_PASSWORD
```

7. Specify that user roy has the privilege to change his password.

```
ALTER USER roy WITH PRIVILEGES = (CHANGE_PASSWORD)
```

8. Roy changes his own password.

```
ALTER USER roy WITH    OLDPASSWORD='myoldpassword',   PASSWORD='mypassword';
```

9. Juanita changes her own password.

```
ALTER USER "juanita.ramirez" WITH    OLDPASSWORD='myoldpassword',   PASSWORD='mypassword';
```
