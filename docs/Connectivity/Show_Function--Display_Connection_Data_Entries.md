---
title: "Show Function--Display Connection Data Entries"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Show_Function--Display_Connection_Data_Entries.htm"
canonical_id: "actian-data-platform-show-function-display-connection-data-entries"
---

## Show Function--Display Connection Data Entries

In netutil non-interactive mode, you can use the show function to display connection data entries. The connection information for the specified vnode is displayed on the terminal or written to standard output. The information is displayed in a format similar to the format of control file input lines, for ease of use in programs that edit and re-use the information. The password is not displayed.

This function has the following format:

```
show type connection vnode network_address protocol listen_address
```

**type**

:   Specifies the type of entry. Valid values are:

global

:   Indicates that the object is available to all users on the local node.

private

:   Indicates that the object is available to a single user.

**vnode**

:   Identifies the virtual node name associated with this input line. An asterisk (*) can be used as a wildcard to select a range of records.

**network_address**

:   Identifies the address or name of the remote node. An asterisk (*) can be used as a wildcard to select a range of records.

**protocol**

:   Specifies the keyword for the protocol used to connect to the remote instance. For a list of protocols and their associated keywords, see [Network Protocol Keywords](../Connectivity/Connection_Data_Table_in_Netutil.md). An asterisk (*) can be used as a wildcard to select a range of records.

**listen_address**

:   Is the unique identifier used by the remote Communications Server for interprocess communication. An asterisk (*) can be used as a wildcard to select a range of records.

Example: Display Connection Data Entries

The following displays global connection data entries on vnode “payroll,” where:

Network address = payroll

Protocol = * (This field is not to be used in selecting records.)

Listen address = * (This field is not to be used in selecting records.)

```
S GL conn payroll payroll * *
```

The following line is displayed:

```
global connection payroll payroll tcp_ip fe2
```
