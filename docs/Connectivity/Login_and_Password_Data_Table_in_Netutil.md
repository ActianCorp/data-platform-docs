---
title: "Login and Password Data Table in Netutil"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Login_and_Password_Data_Table_in_Netutil.htm"
canonical_id: "actian-data-platform-login-and-password-data-table-in-netutil"
---

## Login and Password Data Table in Netutil

The Login and password data table on the netutil startup screen is used for the following tasks:

- To record a remote user authorization using a login account and password on the remote instance’s host machine
- To record a remote user authorization using the Installation Password defined on the remote instance

- To define an Installation Password for the local instance

The information you enter into the fields in the Login/password data table depends on which of the above tasks you are performing. For more information, see [Task-Specific Values for the Login/Password Data Fields](../Connectivity/Login_and_Password_Data_Table_in_Netutil.md).

The Login/password data columns are as follows:

**Type**

:   Is the type of definition, either Global or Private. For details, see [Global and Private Definitions](../Connectivity/Login_and_Password_Data_Table_in_Netutil.md).

**Scope**

:   Is a read-only message, supplied automatically, that briefly describes the scope of the connection. The message depends on the value that you enter in the Type field.

:   If you enter Private, netutil displays the following message:

```
User user_id only
```

:   If you enter Global, netutil displays the following message:

```
Any user on node_name
```

**Login**

:   Specifies the name of the account to be used on the remote instance’s host machine.

!!! note "Note"

    If you are authorizing access to a remote instance using an Installation Password or defining an Installation Password for the local instance, enter an asterisk (*) into this field.

:   After you fill in this field, netutil prompts you for a password.

### Global and Private Definitions

Both connection data entries and remote user authorization entries can be defined for vnodes as either global or private. A global entry is available to all users on the local instance. A private entry is available only to the user who creates it.

Each user can create a private entry. Only a user with the GCA privilege NET_ADMIN (typically a system administrator) can create a global entry.

If both a private and a global entry exist for a given vnode, the private entry takes precedence when the user who created the private entry invokes the vnode.

The following figure shows how connections are made when both private and global entries are defined for a given vnode.

![](images/UsingUtilities.png)

On installation_c, the system administrator has created a vnode (“Chicago”) with a global connection data entry specifying installation_a and a global remote user authorization specifying a login account (“Guest”) on that instance. User A has not defined any private definitions for vnode “Chicago” that takes precedence over the global definitions.

When User A invokes vnode “Chicago,” a connection is made to installation_a through login account “Guest.” User B has added a private remote user authorization to vnode “Chicago,” specifying the login account “User B.” When User B invokes vnode “Chicago,” the private authorization takes precedence over the global authorization, and a connection is made to installation_a through the login account “User B.”

User C has added a private connection data entry to vnode “Chicago.” The private connection data entry contains the listen address, node name, and network protocol of installation_b.

User C has also added a private authorization to login account “User C” on installation_b. When User C invokes vnode “Chicago,” the private definitions take precedence over the global definitions, and a connection is made to installation_b through the login account “User C.”

### Task-Specific Values for the Login/Password Data Fields

The following table shows the required values for the Type, Login, and Password fields according to the kind of record you are entering:

|  |  | Type | Login | Password |
| --- | --- | --- | --- | --- |
| Remote User Authorization | Using login account password | Global or Private | Name of remote login account | Password of remote login account |
|  | Using Installation Password | Global or Private | * (asterisk) | Installation Password of remote instance |
| Local Installation Password |  | Global | * (asterisk) | Local Installation Password |

!!! note "Note"

    When creating a local installation password, the vnode name used must be identical to the name that has been configured as LOCAL_VNODE on the Configure Name Server screen of the Configuration-By-Forms (cbf) utility and is generally the same as the local machine name.
