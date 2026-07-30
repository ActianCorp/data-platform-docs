---
title: "Delete Users and Their Schemas"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Delete_Users_and_Their_Schemas.htm"
canonical_id: "actian-data-platform-delete-users-and-their-schemas"
---

## Delete Users and Their Schemas

Only users in the useradmin group have the privilege to maintain other users.

!!! note "Note"

    The following example assumes connection to the User Management database (iidbdb). See examples of connections in [Overview of User Management](../DBaaS_User/Overview_of_User_Management.md).

To delete a user’s database schema and the data it contains

1. Connect to the User Management database (iidbdb) as a useradmin user (for example, dbuser) and connect to the iidbdb database.
2. Change the password of the user whose schema you want to delete. For example:

```
alter user testuser1     with password='mypassword'
```

3. Connect to the Actian database as the user you want to delete (testuser1) using the password supplied in step 2.
4. Drop the schema of the user. For example:

```
drop schema testuser1 cascade
```

To delete a user

Connect to the User Management database (iidbdb) as a useradmin user (for example, dbuser) and execute the drop user statement:

```
drop user testuser1;
```

More information:

- [ALTER USER](../SQLLanguage/ALTER_USER.md)
- [DROP SCHEMA](../SQLLanguage/DROP_SCHEMA.md)

- [DROP USER](../SQLLanguage/DROP_USER.md)
