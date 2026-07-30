---
title: "Connection Data Table in Netutil"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Connection_Data_Table_in_Netutil.htm"
canonical_id: "actian-data-platform-connection-data-table-in-netutil"
---

## Connection Data Table in Netutil

The Connection data table on the netutil startup screen specifies the network address of the remote node, the listen address of the remote instance’s Communications Server, and the network protocol that is used to make the connection.

The Connection data table has the following columns:

**Type**

:   Specifies type of connection, either global or private.

**Net Address**

:   Identifies the network address or name of the remote node.

:   Your network administrator specifies this address or name when the network software is installed. Normally, the node name as defined at the remote node is sufficient for the node address.

:   The format of the net address depends on the type of network software used by the node. For protocol-specific information, see the “TCP/IP Protocol” appendix in this guide.

**Protocol**

:   Specifies the Actian X keyword for the protocol used by the local node to connect to the remote node. In Linux and Windows environments, use the keyword **tcp_ip**.

:   Protocol availability varies by platform. For a list of protocols and their associated keywords, see [Network Protocol Keywords](../Connectivity/Connection_Data_Table_in_Netutil.md).

**Listen Address**

:   Identifies the unique identifier used by the remote Communications Server for interprocess communication.

:   Just as the vnode name identifies an instance on the network, the listen address identifies a process (the Communications Server) in the remote instance.

:   The format of a remote node listen address depends on the type of network software that the node is using.

### Network Protocol Keywords

When entering connection data for a remote instance, you are prompted for the name of the network protocol that is used to make the connection. You must respond with one of the following keywords:

**tcp_ip**

:   TCP/IP Internet protocol for Linux and Windows (using WinSock 2.2 API). This is the default TCP/IP protocol and supersedes wintcp.

**decnet**

:   DECnet protocol for VMS

**tcp_dec**

:   TCP/IP Services for OpenVMS and Multinet TCP/IP when running in TCP/IP Services emulation

**tcp_ibm**

:   IBM TCP/IP for MVS
