---
title: "Destroy Function--Destroy a Connection Data Entry"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Destroy_Function--Destroy_a_Connection_Data_Entr.htm"
canonical_id: "actian-data-platform-destroy-function-destroy-a-connection-data-entr"
---

## Destroy Function--Destroy a Connection Data Entry

In netutil non-interactive mode, you can use the destroy function to destroy a connection data entry. To obtain the network address, protocol, and listen address of the connection data entry you want to destroy, use the show command.

This function has the following format:

```
destroy type connection vnode network_address protocol listen_address
```

**type**

:   Specifies the type of entry. Valid values are:

global

:   Indicates that the object is available to all users on the local node.

private

:   Indicates that the object is available to a single user.

**vnode**

:   Identifies the virtual node name associated with this input line. An asterisk (*) can be used as a wildcard to select a range of records.

**network_address**

:   Identifies the address or name of the remote node. An asterisk (*) can be used as a wildcard to select a range of records.

**protocol**

:   Specifies the keyword for the protocol used to connect to the remote instance. For a list of protocols and their associated keywords, see [Network Protocol Keywords](../Connectivity/Connection_Data_Table_in_Netutil.md). An asterisk (*) can be used as a wildcard to select a range of records.

**listen_address**

:   Is the unique identifier used by the remote Communications Server for interprocess communication. An asterisk (*) can be used as a wildcard to select a range of records.

**Examples: Destroy a Connection Data Entry**

The following command destroys a private connection data entry on vnode “payroll”, where:

Network address = payroll
Protocol = TCP/IP
Listen address = fe2

```
D p c payroll payroll tcp_ip fe2 # No comm server on fe2
```

The following command destroys all global connection data entries for vnode “accounting” that include the TCP/IP protocol:

```
d gl c accounting * tcp_ip *
```

!!! note "Note"

    Private connection data entries are destroyed for the currently logged-in user or for the user identified by the -u flag. Only a user with the GCA privilege NET_ADMIN can destroy a global connection data entry.
