---
title: "What is a Vnode (Virtual Node)?"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "What_is_a_Vnode_(Virtual_Node)_3f.htm"
canonical_id: "actian-data-platform-what-is-a-vnode-virtual-node-3f"
---

## What is a Vnode (Virtual Node)?

A vnode is a name for an entry in a client-side registry of server connection information. This additional redirection enables you to make changes to the connection information without requiring changes to any client that only uses the vnode name to connect to a database server.

A dynamic vnode bypasses that client-side registry. To distinguish a vnode from a dynamic vnode, the dynamic vnode starts with “@.” To connect to a remote instance, all required information is contained in the connection string (as described in [Dynamic Vnode Specification--Connect to Remote Database](../Connectivity/Using_Net.md)).

!!! note "Note"

    The Actian Data Platform users use dynamic vnodes where all the information is contained within the connection string. The Actian Data Platform console lists these connection strings for respective warehouse instance under the Connections tab for various tools and APIs. See [Warehouse Details](../User/Warehouse_Details.md).

Examples for dynamic vnodes as they are typically used with the Actian Data Platform when using the Actian SQL CLI, which is part of the Actian Data Platform Client Runtime Package:

```
sql +user=dbuser @av-5iiffz03avmg.actiandatacloud.com,tcp_ip,27832::db
```

```
sql @av-5iiffz03avmg.actiandatacloud.com,tcp_ip,27832[dbuser,<password>]::db
```

Actian Data Platform users cannot create vnodes unless they have access to other Actian product packages, which contain the respective tools. Many subsequent sections of this guide are shared with the documentation of different Actian product; therefore, the vnode occurrences in those subsequent chapters remain.

If you do not use the dynamic method, you must define a Server Connection Definition (also known as a vnode), as described in [Creating Server Connection Definitions (Vnodes)](../Connectivity/Creating_Server_Connection_Definitions_(Vnodes).md). The Name Server must be running to define and use virtual nodes.

A vnode is a name defined on the local instance to identify a particular remote instance. The definition contains connection data and authorization data for a remote instance.

Using vnodes is generally simpler for users because they only have to enter a single, user-friendly vnode name when they run an application, rather than detailed network-specific connection information. Another advantage of vnodes is that network changes can be updated for a vnode without notifying the user or changing the application.
