---
title: "Advanced Vnode Parameters"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Advanced_Vnode_Parameters.htm"
canonical_id: "actian-data-platform-advanced-vnode-parameters"
---

## Advanced Vnode Parameters

You can maintain up to two login data definitions for each vnode. If the first definition has been defined as private, the other login must be global (and vice versa). A global entry is available to all users on the local instance. A private entry is available only to the user who creates it.

If one of the login data definitions is private and the other is global, the vnode is considered to be an advancedvnode. A vnode is also considered to be an advanced vnode if it has more than one connection data definition and/or has one or more vnode attribute definitions.

## Multiple Connection Data Entries

If a remote instance has more than one Communications Server or can be accessed by more than one network protocol, that information can be included in the vnode definition by adding another connection data entry. This allows you to distribute the load of communications processing and increase fault tolerance.

End users can create private connection data for an existing vnode by adding an entry to the Connection Data table. For the user who creates it, a private connection data entry overrides a global connection data entry defined to the same vnode. In other words, Ingres Net uses the private connection data entry whenever the user who created the entry uses the vnode.

You need the following information before adding a connection data entry:

- The network address of the node on which the remote instance resides
- The listen address of the remote instance’s Communications Server. (For the correct listen address format for your network protocol, see the appropriate appendix.)

- The keyword for the network protocol that is used to make the connection.

## Additional Remote User Authorization

End users can create a private remote user authorization for an existing vnode.

For the user who creates it, a private authorization overrides a global authorization defined to the same vnode. Ingres Net uses the private authorization whenever that user uses the vnode.

## Vnode Attributes Configuration

In addition to login and connection data, you can configure additional vnode attributes.

For a description of each attribute and its associated values, see [Vnode Attribute Names and Values](../Connectivity/Advanced_Vnode_Parameters.md).

### Vnode Attribute Names and Values

Valid vnode attribute names and values are:

**connection_type**

:   Abbreviation: conntype

:   Indicates how the connection is to be established. Valid values are:

default

:   Establishes a standard connection. In general, this means the connection is established between the client application process and the remote instance using the Net protocol.

comsvr

:   Establishes the connection using the Communications Server in the local instance, where it is then routed across the network.

**compression_type**

:   Abbreviation: compress

:   Specifies the compression type to be used on the connection. Only a single compression type is supported, so current values simply allow compression to be enabled or disabled. Valid values are:

none or off

:   Disables compression

default or on

:   Enables compression using the default compression type

**character_set**

:   Abbreviation: charset

:   Specifies the character set used on the remote instance. This attribute is necessary when connecting a UTF8 configured client instance with an older version remote instance that is not configured as UTF8 and the connection cannot be established because a common communication character set cannot be negotiated. Valid values are any character set names that can be used in the II_CHARSET environment variable.
