---
title: "Connection Data"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Connection_Data.htm"
canonical_id: "actian-data-platform-connection-data"
---

## Connection Data

The Connection data specifies the network address of the remote node, the listen address of the remote instance’s Communications Server, and the network protocol that is used to make the connection.

The Connection data has these items:

**Type**

:   Specifies type of connection, either global or private.

**Net Address**

:   Identifies the host specified in the Actian Data Platform Warehouse Details page, Connections tab.

:   For the format of the net address, see[Network Address Format](../Connectivity/Connection_Data.md).

**Protocol**

:   Specifies the keyword for the protocol used by the local node to connect to the remote node. Use the keyword tcp_ip.

**Listen Address**

:   Identifies the unique identifier used by the remote Communications Server for interprocess communication.

:   Just as the vnode name identifies an instance on the network, the listen address identifies a process (the Communications Server) in the remote instance.

## Network Address Format

The network address in a TCP/IP environment has this format:

host_name | ip_address

where:

**host_name**

:   Is the name of the remote node in character form

**ip_address**

:   Is the internet address of the remote node in the following format:

:   For IPv4: d.d.d.d (For example: 123.45.67.89) dotted decimal
