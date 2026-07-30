---
title: "SSO Authentication Troubleshooting"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "SSO_Authentication_Troubleshooting.htm"
canonical_id: "actian-data-platform-sso-authentication-troubleshooting"
---

## SSO Authentication Troubleshooting

SSO user cannot connect to a warehouse receives a message about a GCA protocol service failure.

When SSO users fail to connect to a warehouse, they receive the following message:

```
E_LC0001 GCA protocol service (GCA_REQUEST) failure. Internal service status E_GC013b -- An unknown attribute was specified in the connection string or as part of a vnode.
```

It is likely the Actian Data Platform Client version does not support SSO authentication. To correct this problem, you must download the latest [Actian Client Runtime Package](../User/Actian_Client_Runtime_Package.md) and install on your system.

!!! note "Note"

    The Actian Client release must be at a minimum 1.1.0 level to support SSO authentication. The naming convention on the client download zip file (actian-client-1.1.x-xxx.zip) can help determine the version.
