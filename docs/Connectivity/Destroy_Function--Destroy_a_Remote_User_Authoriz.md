---
title: "Destroy Function--Destroy a Remote User Authorization"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Destroy_Function--Destroy_a_Remote_User_Authoriz.htm"
canonical_id: "actian-data-platform-destroy-function-destroy-a-remote-user-authoriz"
---

## Destroy Function--Destroy a Remote User Authorization

In netutil non-interactive mode, you can use the destroy function to destroy a remote user authorization.

This function has the following syntax when destroying a remote user authorization:

```
destroy type login vnode
```

**type**

:   Specifies the type of entry. Valid values are:

global

:   Indicates that the object is available to all users on the local node.

private

:   Indicates that the object is available to a single user.

**vnode**

:   Identifies the virtual node name associated with this authorization.

Examples: Destroy a Remote User Authorization

This command destroys a private login on vnode “payroll.” The entry to be destroyed is uniquely identified by its type and the vnode name. No additional fields are necessary.

```
DE PR L payroll # Current user now uses global login
```

This command destroys a private login on all vnodes where it occurs. Using a wildcard in the vnode field lets you destroy all instances of a particular login with a single input line:

```
DE PR L *
```

!!! note "Note"

    Private authorizations are destroyed for the currently logged-in user or for the user identified by the -u flag. Only a user with the GCA privilege NET_ADMIN can destroy a global authorization.
