---
title: "ALTER GROUP"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "ALTER_GROUP.htm"
canonical_id: "actian-data-platform-alter-group"
---

## ALTER GROUP

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The ALTER GROUP statement modifies the list of users associated with a group identifier. Individual users can be added or dropped or the entire list can be dropped.

An add and a drop operation cannot be performed in the same ALTER GROUP statement.

#### Syntax

The ALTER GROUP statement has the following format:

```
[EXEC SQL] ALTER GROUP group_id{, group_id}
```

```
ADD USERS (user_id{, user_id}) | DROP USERS (user_id{, user_id}) | DROP ALL
```

**ALTER GROUP group_id{, group_id}**

:   Modifies the list of users associated with a group identifier (group_id).

:   The group_id must be an existing group identifier. If a non-existent group_id is specified, a warning is issued and processing continues with the next valid group_id in the list.

**ADD USERS (user_id{, user_id})**

:   Adds the specified user_ids to the specified the group_ids.

:   The user_ids must exist to be added to a group. If a specified user_id does not exist, an error is issued and processing continues with the remaining user_ids.

:   If a specific user_idoccurs more than once in the user list, additional occurrences of the specified user_idare ignored. No errors are issued.

**DROP USERS (user_id {, user_id})**

:   Removes the specified user_ids to the specified the group_ids.

:   If a specified user_id is not in the group user list, an error is issued and processing continues with the remaining user_ids.

:   A user cannot be dropped from a group if that group is the default group of the user. Use the ALTER USER statement to change a user's default group.

:   If a user is dropped from a group in a session that is associated with that group, the user retains the privileges of the group until the session terminates.

**DROP ALL**

:   Removes all users from the specified group_ids.

:   If any member of the specified group has that group as its default group, DROP ALL results in an error. Use the ALTER USER statement to change the user's default group.

:   If a user is dropped from a group in a session that is associated with that group, the user retains the privileges of the group until the session terminates.

## ALTER GROUP Examples

Add and drop user identifiers from the user list associated with a group identifier:

1. Add users to the group, sales_clerks.

```
EXEC SQL ALTER GROUP sales_clerks     ADD USERS (dannyh, helent);
```

2. Drop three users from the group, tel_sales.

```
EXEC SQL ALTER GROUP tel_sales     DROP USERS (harryk, joanb, elainet);
```

3. In an application, drop all users from the group, researchers.

```
EXEC SQL ALTER GROUP researchers DROP ALL;
```
