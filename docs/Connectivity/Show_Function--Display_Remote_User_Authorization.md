---
title: "Show Function--Display Remote User Authorizations"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Show_Function--Display_Remote_User_Authorization.htm"
canonical_id: "actian-data-platform-show-function-display-remote-user-authorization"
---

## Show Function--Display Remote User Authorizations

In netutil non-interactive mode, you can use the show function to display remote user authorizations. The login information for the specified vnodes is displayed on the terminal or written to standard output. The password is not displayed.

The information is displayed in a format similar to that of control file input lines for ease of use in programs that edit and re-use the information.

The show function has following format for displaying remote user authorizations:

```
show type login vnode
```

**type**

:   Specifies the type of entry. Valid values are:

global

:   Indicates that the object is available to all users on the local node.

private

:   Indicates that the object is available to a single user.

**vnode**

:   Identifies the virtual node name associated with this authorization. An asterisk (*) can be used as a wildcard in the vnode, field.

Example: Display Remote User Authorizations

The following command displays the global login of vnode “accounting:”

```
S GL login accounting
```

The following line is displayed:

```
global login accounting ingres
```
