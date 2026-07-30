---
title: "Access to a Remote Instance"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Access_to_a_Remote_Instance.htm"
canonical_id: "actian-data-platform-access-to-a-remote-instance"
---

## Access to a Remote Instance

You can connect to an Actian warehouse using either a vnode or dynamic vnode. Actian Data Platform users typically use dynamic vnodes, which contain all required information in the connection string.

## vnode Connection

A vnode is the traditional method of connecting to a remote instance. Before configuring an ODBC data source, a vnode must be defined.

## Dynamic Vnode (Vnode-less)

A dynamic vnode definition eliminates the need to define a vnode separately.

The ODBC Administrator accepts dynamic syntax automatically (on the Simple tab). The Detailed tab, lets you define the dynamic vnode entry.

A dynamic vnode has the following syntax:

```
@hostName,protocol,listenAddress[uid,pwd]
```

## Serverless Client

If the ODBC data source uses dynamic vnode syntax, no local Name Server or Communications Server is required. The ODBC application itself makes the connection to the remote data source.
