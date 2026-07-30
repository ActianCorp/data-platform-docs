---
title: "Default Remote Nodes"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Default_Remote_Nodes.htm"
canonical_id: "actian-data-platform-default-remote-nodes"
---

## Default Remote Nodes

A system administrator can define a default remote node for the local node. When this parameter is set, users are automatically connected to the default node whenever they request a connection without specifying a vnode name. If users want to access a database on their local node, they must specify the name configured as local_vnode.

To illustrate, assume that the system administrator has set up the node “eugenie” as the default remote node for users at the node “josephine.” The node “eugenie” has the database “advertisers” and “josephine” has the database “employees.” Whenever users on “josephine” issue database connection requests that do not specify a vnode name, they are automatically connected to “eugenie” because “eugenie” is the default remote node for “josephine.” For example, look at the following statement:

```
isql advertisers
```

If users on “josephine” issue this statement, Ingres Net automatically connects them to the “advertisers” database on “eugenie.” If the users on “josephine” want to query a local database, they must specify josephine’s local_vnode name. For example, if the local_vnode name for “josephine” is “royal,” users on “josephine” issue the following statement to query the local database “employees”:

```
isql royal::employees
```

!!! note "Note"

    Do not set the default remote node name to point to a vnode that is in fact a loopback to the local instance. If you do so, your local connections loop through Ingres Net until all resources are exhausted and the connection fails.

## How You Set Default Remote Nodes

To define a default remote node for the local node, set the configuration parameter remote_vnode.
