---
title: "How You Diagnose Connectivity Problems"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "How_You_Diagnose_Connectivity_Problems.htm"
canonical_id: "actian-data-platform-how-you-diagnose-connectivity-problems"
---

## How You Diagnose Connectivity Problems

Often, the most difficult task in problem solving is determining the origin of the problem. Sometimes the circumstances of the problem point to a particular cause. For example, if only one user on a node is experiencing an Ingres Net connection problem, that user’s vnode entries are probably incorrect. Some problems, however, leave more ambiguous clues.

To determine the origin of a problem

1. Examine the Client Runtime logs.

    Often the error message provides sufficient information to determine the origin of the problem.

2. Examine any of the optional logs or tracing facilities, if set up in your installation.
3. Perform the [General Net Installation Check](../Connectivity/How_You_Diagnose_Connectivity_Problems.md) if examining the error messages does not pinpoint the origin of the problem.

## General Net Installation Check

The Ingres Net installation check is a diagnostic procedure that checks your installation to determine the following:

- Whether the problem is Ingres Net-related
- Whether the iigcn and iigcc processes are running

- Whether the network protocol software is working

### How You Check Net Installation on Windows

If you are experiencing a problem and cannot determine its source, use this diagnostic procedure as a starting point:

1. Verify that your network protocol is functioning.

    a. Use the ping command to connect between machines to verify that basic TCP/IP networking is working.

    b. On both the client and the server, verify that TCP/IP is properly installed and configured. Do this by attempting to connect to the default localhost (or loopback) listen address from each machine. Type one of the following commands to loop back to your own machine using the network:

        - ping localhost

        - ping 127.0.0.1

        - ping ::1 (if TCP/IP version 6 enabled)

    If either “a” or “b” fails, the problem is with the underlying network. Contact your network administrator.

2. If the remote node is a Linux machine, verify that you can connect to the target database on the remote node when you are logged in directly to the remote node.

    a. Use telnet to log in to the remote node from your local node.

    b. Enter a command that connects you to the database. For example:

```
sql database_name
```

    If you cannot connect to the database even when logged in directly to the remote node, the problem is something other than Ingres Net.

    If you can connect this way, but cannot connect when you are Using Net to log in to the remote node and connect (through the syntax sql vnode_name::database_name), it is an Ingres Net problem. Proceed with Step 3.

3. Check that the iigcc process is registered with the Name Server:

    a. Enter **iinamu** at the operating system prompt.

    b. Type **show comsvr**.

    If you receive no output from the show comsvr command, this means that no Communications Server is registered with the Name Server.

4. Check that configuration parameters such as local_vnode and the Communications Server listen address are correctly set.
5. Check the II_GCNxx_PORT environment variable where xx is the instance ID. It must be visible only when using the ingprenv utility. It must never be visible when using the Linux commands env or printenv. II_GCNxx_PORT must not be part of your local operating system environment. If it is set in the local environment, it overrides their proper settings in the Actian Data Platform symbol table.

You must be the installation owner to take corrective action.

### How You Check Net Installation on Linux

If you are experiencing a problem and cannot determine its source, use this diagnostic procedure as a starting point:

1. Verify that your network protocol is functioning.

    a. Use the rlogin and/or telnet commands to connect between machines to verify that basic TCP/IP networking is working.

    b. On both the client and the server, verify that TCP/IP is properly installed and configured. Do this by attempting to connect to the default localhost (or loopback) listen address from each machine. Type one of the following commands to loop back to your own machine using the network:

        - telnet localhost

        - telnet 127.0.0.1

        - ping ::1 (if TCP/IP version 6 enabled)

    The login messages that follow the command reveal whether you are connected to your own machine (the name of the machine can be embedded in the messages). If they do not, you can log in and issue the hostname command to display the name of the machine to which you are connected.

    If either “a” or “b” fails, the problem is with the underlying network. Contact your network administrator.

2. Verify that you can connect to the target database on the remote node when you are logged in directly to the remote node.

    a. Use telnet, rlogin, or your site’s network server bridge software to log in to the remote node from your local node.

    b. Enter a command that connects you to the database. For example:

```
$ sql database_name
```

    If you cannot connect to the database even when logged in directly to the remote node, the problem is something other than Ingres Net.

    If you can connect this way, but cannot connect when you are Using Net to log in to the remote node and connect (through the syntax sql vnode_name::database_name), it is an Ingres Net problem. Proceed with Step 3.

3. To verify that the Communications Server (iigcc) and Name Server (iigcn) processes are running on your local node, use the ps command. This command shows the status of all currently running processes. Also check the processes on the remote node.
4. Check that the iigcc process is registered with the Name Server:

    a. Enter **iinamu** at the operating system prompt.

    b. Type **show comsvr**.

    If you receive no output from the show comsvr command, this means that no Communications Server is registered with the Name Server.

5. Check that configuration parameters such as local_vnode and the Communications Server listen address are correctly set.
6. Check the II_GCNxx_PORT environment variable where xx is the instance ID. It must only be visible using the ingprenv utility. It must never be visible using the Linux commands env or printenv. II_GCNxx_PORT must not be part of your local Linux shell environment. If it is set in the local environment, it overrides their proper settings in the Actian Data Platform symbol table.

    You must be the installation owner (who by default has Actian Data Platform user privileges) to take corrective action.

## Connection Errors

Connection errors can occur for a variety of reasons. For example, a failure in any of the internal connections described in [How Connection Between the Application and Warehouse Is Established](../Connectivity/Troubleshooting_Connectivity.md) results in a connection error.

How connection errors are reported depends on where the failure occurs. If failure occurs:

- At the local instance, errors are reported directly to the user interface program or the application.
- Between the local and remote instances, for example, when attempting to connect from the local Communications Server to the remote Communications Server, errors go to the local errlog.log file as well as to the application.

- At the server installation, errors are reported to both the local and remote errlog.log file and to the application.

### Local Connection Errors

Each Communications Server has a GCA and GCC listen address. The GCA listen address is the server’s connection to local processes and is known only to the local Name Server (iigcn). The GCC listen address is the server’s connection to the network and is known to all nodes in the network. These listen addresses are stored separately.

The GCA address is stored at runtime in an IICOMSVR file in the Name Server database. You can obtain this address using the iinamu utility. Do not attempt to view these files directly.

The GCC address is stored in the config.dat file when the installation is configured.

When the Communications Server starts up, it must be able to obtain the use of the network (GCC) listen address. If the Communications Server cannot use this listen address because the operating system has allocated the address to another process, the Communications Server cannot listen on that protocol. This problem can occasionally arise if the installation is not started from the machine boot file.

### How You Resolve Remote Connection Errors

When you cannot establish a remote connection, use this procedure to diagnose the problem:

1. Check the errlog.log for error messages.
2. If that does not identify the problem, follow the procedure for your protocol in the General Net Installation Check section of this section. This procedure tells you if your network and protocol are working properly and if the Name Server (iigcn) and Communications Server (iigcc) processes are working properly.

## How You Resolve Net Registration Problems

To resolve net registration problems

1. Use the General Net Installation Check to verify that your installation is properly installed and working.
2. Check that your connection data entries and remote user authorizations are correct.

    The utilities used to set up connection data and remote user authorizations can test a connection, but you must explicitly choose the Test operation from a menu. If you did not test the connection after entering, adding, or editing connection data or remote user authorizations, the information can be incorrect.

3. Check that the required connection data and remote user authorizations for the target installation exist. If they are present, check the following:

    - That all vnode names and user (account) names are spelled correctly

    - That the proper network protocol has been specified

    - That listen addresses and network addresses are correct

!!! note "Note"

    End users check their private entries.

    Any user can check global entries, however if corrections are required, they must be made by a user with the GCA privilege NET_ADMIN (typically the system administrator).
