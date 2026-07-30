---
title: "Prerequisites to Establish and Test a Remote Connection"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Prerequisites_to_Establish_and_Test_a_Remote_Con.htm"
canonical_id: "actian-data-platform-prerequisites-to-establish-and-test-a-remote-con"
---

## Prerequisites to Establish and Test a Remote Connection

To establish and test a remote connection, the following information is required:

- The network address or name of the node on which the remote instance resides.
- The listen address of the remote instance’s Communications Server.

- The keyword for the network protocol that is used to make the connection. For more information, see [Network Protocol Keywords](../Connectivity/Connection_Data_Table_in_Netutil.md).
- The user name that is used to access the remote instance.

    This information is not applicable when using an Installation Password to authorize access.

- The password, which can be one of the following:

    - –Installation Password of the remote instance

    - –Password of the user's remote login account

    - –The DBMS password for the user on the remote instance, assuming DBMS authentication is enabled for the remote server
