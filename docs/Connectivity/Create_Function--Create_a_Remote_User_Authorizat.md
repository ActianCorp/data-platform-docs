---
title: "Create Function--Create a Remote User Authorization"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Create_Function--Create_a_Remote_User_Authorizat.htm"
canonical_id: "actian-data-platform-create-function-create-a-remote-user-authorizat"
---

## Create Function--Create a Remote User Authorization

In netutil non-interactive mode, you can use the create function to create a remote user authorization.

This function has the following format when used to create a remote user authorization:

```
create type login vnode login password
```

**type**

:   Specifies the type of entry. Valid values are:

global

:   Indicates that the object is available to all users on the local node.

private

:   Indicates that the object is available to a single user.

**vnode**

:   Identifies the virtual node name associated with this authorization.

**login**

:   Identifies the name of the account to be used on the remote instance's host machine.

:   If you are authorizing access to the remote instance using an Installation Password, an asterisk (*) must be entered into this field.

**password**

:   Identifies the remote instance's Installation Password, the password of the remote account, or the DBMS password, depending on the method of authorization.

Examples: Create a Remote User Authorization

This command creates a private authorization for vnode “payroll” for user Jane:

```
C P L Payroll jane jpassword
```

This command creates a global authorization for vnode “accounting” using an Installation Password:

```
cr gl login accounting * acctpassword
```

!!! note "Note"

    Any previously existing authorization of the specified type is replaced by the execution of this line.

!!! note "Note"

    Private authorizations are created for the currently logged-in user or for the user identified by the -u flag. Only a user with the GCA privilege NET_ADMIN can create a global authorization.
