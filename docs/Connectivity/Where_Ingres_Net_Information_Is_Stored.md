---
title: "Where Ingres Net Information Is Stored"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Where_Ingres_Net_Information_Is_Stored.htm"
canonical_id: "actian-data-platform-where-ingres-net-information-is-stored"
---

## Where Ingres Net Information Is Stored

Ingres Net configuration values are stored in eitherof these places:

**config.dat file**

:   Stores Ingres Net configuration parameters.

**Name Server database**

:   Stores remote access information.

## config.dat--Store Net Configuration Values

The following Ingres Net configuration parameters are stored in config.dat. The default values are assigned during installation.

!!! note "Note"

    The Net Server is the Communications Server.

| Parameter | Default |
| --- | --- |
| inbound_limitoutbound_limit | 64 inbound sessions64 outbound sessions |
| log_level | Level 4 |
| Protocol | Any protocol present at installation is indicated as active |
| Listen Address | A GCC listen address is assigned for any protocol present at installation. (The format depends on the protocol.) |
| default_server_class | INGRES |
| remote_vnode | No default value |
| local_vnode | Name of host machine |

## Name Server Database--Store Remote Access Information

The Name Server database is an internal database used by the Name Server (iigcn). The Name Server database contains the information required for remote access, such as remote node names, listen addresses, login accounts and passwords, and virtual node names. This information can be entered in the Name Server database.

In a client/server configuration, this database contains one file called iiname.all and one or more "nodename" files for each client node and for the local node. For example:

```
iiname.all
```

```
IIINGRES_nodename1
```

```
IICOMSVR_nodename1
```

```
IISTAR_nodename1
```

```
IINODE_nodename1
```

```
IILOGIN_nodename1
```

```
IIIUSVR_nodename1
```

```
IIDB2UDB_nodename1
```

```
IIORACLE_nodename1
```

```
IIRDB_nodename1
```

```
IIRMS_nodename1
```

```
IILTICKET_nodename1
```

```
IIRTICKET_nodename1
```

```
IIINGRES_nodename2
```

```
IICOMSVR_nodename2
```

```
IISTAR_nodename2
```

```
IINODE_nodename2
```

```
IILOGIN_nodename2
```

```
IIIUSVR_nodename2
```

```
IIDB2UDB_nodename2
```

```
IIORACLE_nodename2
```

```
IIRDB_nodename2
```

```
IIRMS_nodename2
```

```
IILTICKET_nodename2
```

```
IIRTICKET_nodename2
```

A unique set of files is created for each node registered as an Ingres Net client.

In the cluster environment, the Name Server database has only one file of each type. For example:

```
iiname.all
```

```
INGRES
```

```
COMSVR
```

```
STAR
```

```
NODE
```

```
LOGIN
```

```
IUSVR
```

```
DB2 UDB
```

```
ORACLE
```

```
RDB
```

```
RMS
```

```
LTICKET
```

```
RTICKET
```

All the nodes in an Ingres Cluster Solution instance share the same files.

The files in the Name Server Database are:

**iiname.all**

:   Contains a list of the files required on all instances other than those for specific servers.

**svrclass.nam**

:   Contains a list of all of the types of servers that the instance is expected to manage. The possibilities are warehouses, Communications servers, and Star servers.

**IIINGRES_nodename**

:   Contains the GCA listen addresses of all the warehouses registered with the Name Server (iigcn) on the specified node.

:   The file is written when the warehouse starts and is cached when the node's (identified bynodename) Name Server starts.

**IICOMSVR_nodename**

:   Contains the GCA listen address of the Communications Server (iigcc) on the specified node (identified by nodename). The file is written when the local Communications Server starts and is cached when the local Name Server starts.

**IIDASVR_nodename**

:   Contains the GCA listen address of the Data Access Server (iigcd) on the specified node (identified by nodename). The file is written when the local Data Access Server starts and is cached when the local Name Server starts.

**IISTAR_nodename**

:   Contains the GCA listen address of the Star Server on the specified node (identified bynodename). The file is written when the Star Server starts and is cached when the nodename’s Name Server starts.

**IINODE_nodename**

:   Contains the connection data entries established for the specified node. The file is written whenever you select the “create” option to add a connection data entry for an existing vnode. The file is cached when the nodename’s Name Server starts.

**IILOGIN_nodename**

:   Contains the remote user authorizations set up at the specified node. The file is written whenever you add a remote user authorization. It is cached when the nodename’s Name Server starts.

**IIATTR_nodename**

:   Contains the connection attributes set up at the specified node. The file is written whenever you add a connection attribute. It is cached when the nodename’s Name Server starts.
