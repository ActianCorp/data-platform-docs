---
title: "Netutil Non-Interactive Mode"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Netutil_Non-Interactive_Mode.htm"
canonical_id: "actian-data-platform-netutil-non-interactive-mode"
---

## Netutil Non-Interactive Mode

Netutil supports a non-interactive mode of operation controlled by command line flags and an input control file. You can use this mode if you want to write your own system administration utility programs or authorize large numbers of users using a batch file.

The following functions are available through this interface:

**Create**

:   Creates a new connection data entry or remote user authorization.

**Destroy**

:   Destroys a connection data entry or remote user authorization.

**Show**

:   Displays information to the terminal. This function does not correspond to a menu item in the forms-based interface.

**Stop**

:   Stops all Communications Servers.

:   For example, this command stops a specific Communications Server:

```
stop 2937
```

**Quiesce**

:   Stops all Communications Servers after the sessions currently in progress on those servers have terminated.

:   For example, this command quiesces a specific Communications Server:

```
quiesce 2116
```

!!! note "Note"

    The Edit and Test functions found in the forms-based netutil interface are not supported in non-interactive mode.
