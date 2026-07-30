---
title: "Update Users"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Update_Users.htm"
canonical_id: "actian-data-platform-update-users"
---

## Update Users

Only users in the useradmin group have the privilege to maintain other users.

To update a user, connect as the userdamin privileged user to User Management database (iidbdb) where the users are maintained, and execute an ALTER USER query.

!!! note "Note"

    The following example assumes connection to the User Management database (iidbdb). See examples of connections in [Overview of User Management](../DBaaS_User/Overview_of_User_Management.md).

Example

```
alter user testuser2 with profile=useradmin, group=dbadmingrp;
```

This example updates testuser2 (from [Add Native Users](../DBaaS_User/Add_Native_Users.md), Example 2) to have privileges to maintain users by assigning a useradmin profile and adding testuser2 to dbadmingrp, allowing the user to read and write access to the sample data.

More information:

[ALTER USER](../SQLLanguage/ALTER_USER.md)
