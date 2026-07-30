---
title: "Creating Server Connection Definitions (Vnodes)"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Creating_Server_Connection_Definitions_(Vnodes).htm"
canonical_id: "actian-data-platform-creating-server-connection-definitions-vnodes"
---

# Creating Server Connection Definitions (Vnodes)

## Server Connection Definitions (Virtual Nodes)

To connect to a remote instance, you can specify all the required information dynamically in the connection string. This is the typical approach when connecting to an Actian database.

If you do not use the dynamic method, you must define a Server Connection Definition (also known as a virtual node, or vnode).

A vnode is a name defined on the local instance to identify a particular remote instance. The definition contains connection data and authorization data for a remote instance.

Using vnodes is generally simpler for users because they only have to enter a single, user-friendly vnode name when they run an application, rather than detailed network-specific connection information. Another advantage of vnodes is that network changes can be updated for a vnode without notifying the user or changing the application.
