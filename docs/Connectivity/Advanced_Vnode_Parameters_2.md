---
title: "Advanced Vnode Parameters"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Advanced_Vnode_Parameters_2.htm"
canonical_id: "actian-data-platform-advanced-vnode-parameters-2"
---

## Advanced Vnode Parameters

You can maintain up to two login data definitions for each vnode. If the first definition has been defined as private, the other login must be global (and vice versa). A global entry is available to all users on the local instance. A private entry is available only to the user who creates it.

If one of the login data definitions is private and the other is global, the vnode is considered to be an advancedvnode. A vnode is also considered to be an advanced vnode if it has more than one connection data definition and/or has one or more vnode attribute definitions.

### Multiple Connection Data Entries

If a remote instance has more than one Communications Server or can be accessed by more than one network protocol, that information can be included in the vnode definition by adding another connection data entry. This allows you to distribute the load of communications processing and increase fault tolerance.

!!! note "Note"

    When more than one Communications Server listen address is defined for a given vnode, Ingres Net automatically tries each server in random order until it finds one that is available. Similarly, when a connection fails over one network protocol, Ingres Net automatically attempts the connection over any other protocol that has been defined.

End users can create private connection data for an existing vnode by adding an entry to the Connection Data table. For the user who creates it, a private connection data entry overrides a global connection data entry defined to the same vnode. In other words, Ingres Net uses the private connection data entry whenever the user who created the entry uses the vnode.

You need the following information before adding a connection data entry:

- The network address of the node on which the remote instance resides
- The listen address of the remote instance’s Communications Server.

- The keyword for the network protocol (see [Network Protocol Keywords](../Connectivity/Connection_Data_Table_in_Netutil.md)) used to make the connection.

To define an additional connection data entry using Network Utility

See the topics under Defining Connection Data in the Procedures section of the Network Utility online help.

### Additional Remote User Authorization

End users can create a private remote user authorization for an existing vnode.

For the user who creates it, a private authorization overrides a global authorization defined to the same vnode. Ingres Net uses the private authorization whenever that user uses the vnode.

To define and test a new remote user authorization using Network Utility

See the following topics in the Procedures section of the Network Utility online help:

- Adding a Login Database Definition
- Altering a Login Database Definition

- Dropping a Login Database Definition

### Vnode Attributes Configuration

In addition to login and connection data, you can configure additional vnode attributes.

For a description of each attribute and its associated values, see [Vnode Attribute Names and Values](../Connectivity/Establish_and_Test_a_Remote_Connection_Using_Net.md).
