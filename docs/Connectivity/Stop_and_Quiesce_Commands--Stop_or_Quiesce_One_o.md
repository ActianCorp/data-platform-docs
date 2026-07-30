---
title: "Stop and Quiesce Commands--Stop or Quiesce One or More Communications Servers"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Stop_and_Quiesce_Commands--Stop_or_Quiesce_One_o.htm"
canonical_id: "actian-data-platform-stop-and-quiesce-commands-stop-or-quiesce-one-o"
---

## Stop and Quiesce Commands--Stop or Quiesce One or More Communications Servers

In netutil non-interactive mode, to stop all Communications Servers on the instance, enter the following commands at the system prompt:

```
netutil -file-
```

```
stop
```

To stop a single Communications Server, enter the following commands at the system prompt:

```
netutil -file-
```

```
stop server_id
```

**server_id**

:   Is a unique string that identifies a particular Communications Server on the instance. To find the server_id, use the iinamu utility.

Examples: Quiesce One or More Communications Servers

The following commands entered at the system prompt quiesce all Communications Servers on the instance (that is, stops the Communications Servers after all current sessions have terminated):

```
netutil -file-
```

```
quiesce
```

The following commands entered at the system prompt quiesce Communications Server 2937 (that is, stop the server after all current sessions have terminated):

```
netutil -file-
```

```
quiesce 2937
```

!!! note "Note"

    Only a user with the GCA privilege SERVER_CONTROL can stop a Communications Server.
