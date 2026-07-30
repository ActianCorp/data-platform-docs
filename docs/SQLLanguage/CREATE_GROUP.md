---
title: "CREATE GROUP"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_GROUP.htm"
canonical_id: "actian-data-platform-create-group"
---

## CREATE GROUP

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

The CREATE GROUP statement establishes a group identifier and associates it with the specified list of users. Group identifiers enable the database administrator (or user that has the security privilege) to grant identical privileges to a group of users.

After creating a group identifier and specifying its members, the system administrator can grant privileges to the group identifier. When a member of the group begins a session, the group identifier can be specified in the SQL or CONNECT statement (or on the operating system command line, using the -G flag) to obtain the privileges associated with the group.

#### Syntax

The CREATE GROUP statement has the following format:

```
[EXEC SQL] CREATE GROUP group_id {, group_id}               [WITH USERS = (user_id {, user_id})]
```

**group id**

:   Is the group identifier. It must be a valid object name that is unique among all user, group, and role identifiers in the installation. If an invalid identifier is specified in the list of group identifiers, Actian Data Platform returns an error but processes all valid group identifiers. Group identifier names are stored in the iiusergroup catalog in the****iidbdb****database.

**user id**

:   Must be a valid user name. If an invalid user identifier is specified, Actian Data Platform issues an error but processes all valid user identifiers. A group can contain any number of users. A group identifier can be created without specifying a user list. To add users to an existing group identifier, use the ALTER GROUP statement.

## CREATE GROUP Examples

1. Create a group identifier for the telephone sales force of a company and put the user IDs of the salespeople in the user list of the group.

```
CREATE GROUP tel_sales WITH USERS = (harryk,    joanb, jerryw, arlenep);
```

2. In an application, create a group identifier for the inventory clerks of a store and place their user IDs in the user list of the group.

```
EXEC SQL CREATE GROUP inv_clerk WITH USERS =    (jeanies, louisem, joep);
```
