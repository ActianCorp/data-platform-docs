---
title: "DROP PROFILE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_PROFILE.htm"
canonical_id: "actian-data-platform-drop-profile"
---

## DROP PROFILE

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The DROP PROFILE statement drops a user profile that is no longer needed.

User profiles are a set of subject privileges and other attributes that can be applied to a user or set of users. Each user can be given a profile, which is used to provide the default attributes for that user. A default profile, changeable by the system administrator, is provided to determine the default user attributes when no profile is explicitly specified.

This statement is available in dynamic SQL. It is not available in database procedures. There are no dynamic parameters in embedded SQL.

#### Syntax

The DROP PROFILE statement has the following format:

```
[EXEC SQL] DROP PROFILE profile_name [RESTRICT | CASCADE]
```

**RESTRICT**

:   (Default) Specifies that if any users have this profile the statement is rejected.

**CASCADE**

:   Specifies that any users with this profile have their profile reset to the default profile.

## DROP PROFILE Example

Drop the myprofile profile:

```
DROP PROFILE myprofile CASCADE
```
