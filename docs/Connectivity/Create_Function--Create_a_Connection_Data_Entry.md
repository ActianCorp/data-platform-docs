---
title: "Create Function--Create a Connection Data Entry"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Create_Function--Create_a_Connection_Data_Entry.htm"
canonical_id: "actian-data-platform-create-function-create-a-connection-data-entry"
---

## Create Function--Create a Connection Data Entry

In netutil non-interactive mode, you can use the create function to create a connection data entry.

This function has the following format:

```
create type connection vnode network_address protocol listen_address
```

**type**

:   Specifies the type of entry. Valid values are:

global

:   Indicates that the object is available to all users on the local node.

private

:   Indicates that the object is available to a single user.

**vnode**

:   Identifies the virtual node name associated with this connection entry.

**network_address**

:   Identifies the address or name of the remote node. Your network administrator specifies this address or name when the network software is installed. Normally, the node name as defined at the remote node is sufficient for this field.

:   The format of a net address depends on the type of network software that the node is using.

**protocol**

:   Specifies the keyword for the protocol used to connect to the remote instance. For a list of protocols and their associated keywords, see [Network Protocol Keywords](../Connectivity/Connection_Data_Table_in_Netutil.md).

**listen_address**

:   Is the unique identifier used by the remote Communications Server for interprocess communication. The format of a listen address depends on the network protocol.

Example: Create a Connection Data Entry

The following command creates a global connection data entry on vnode “payroll,” where:

Network address = payroll

Protocol = TCP/IP

Listen address = fe0

```
C G C payroll payroll tcp_ip fe0 # payroll comsvr 1
```

!!! note "Note"

    The virtual node name and the network address are different objects, although it is common for them to have the same value.

If a connection entry already exists that matches the specified one in all respects, the operation has no effect and no error is reported.

!!! note "Note"

    Private connection data entries are created for the currently logged-in user or for the user identified by the -u flag. Only a user with the GCA privilege NET_ADMIN can create a global connection data entry.
