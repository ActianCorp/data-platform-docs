---
title: "Using Utilities"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Using_Utilities.htm"
canonical_id: "actian-data-platform-using-utilities"
---

# Using Utilities

## Netutil (Net Management Utility)

The forms-based Net Management Utility, netutil, is used to define the connection and authorization data used by the Communications Server to access remote instances.

Warehouse administrators (or any user with the appropriate Actian Data Platform privileges) can use netutil to perform the following tasks:

- Add, change, or delete global remote user authorizations or connection data entries.

    These tasks require the GCA privilege NET_ADMIN.

- Add, change, or delete any user’s private remote user authorizations or connection data entries using the **-u**command flag.

    These tasks require the NET_ADMIN privilege. For more information about the -**u** flag, which allows a user to perform operations on behalf of other users, see [Command Line Flags in Netutil Non-interactive Mode](../Connectivity/Command_Line_Flags_in_Netutil_Non-interactive_Mo.md).

- Stop the Communications Server.

    This task requires the GCA privilege SERVER_CONTROL.

End users can use netutil to:

- Add, change, or delete their private connection data entries.
- Add, change, or delete their private remote user authorizations.
