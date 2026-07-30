---
title: "Netutil Operations"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Netutil_Operations.htm"
canonical_id: "actian-data-platform-netutil-operations"
---

## Netutil Operations

The following operations are available from the netutil startup screen:

**Create**

:   Creates a new record in the highlighted table.

:   In the vnode table, this operation allows you to create a new vnode name and define its user authorization and connection data.

:   In the Connection data table or Login/password data table, this operation allows you to create an additional entry for an existing vnode.

**Destroy**

:   Deletes the highlighted record.

!!! note "Note"

    Deleting a record in the Virtual Node Name (vnode) table automatically deletes the Login/password and Connection data table records associated with that vnode.

**Attributes/Login**

:   Toggles the display to show attribute or login information for the highlighted node. The initial display shows login information, and the Attributes menu option appears on the menu. Choosing Attributes displays attribute information, and the Attributes menu option is replaced by the Login menu option. Choosing Login brings back the original display.

**Edit**

:   Modifies the highlighted record.

**Control**

:   Stops or quiesces the local Communications Server. This menu item takes you to the Network Server Control screen.

**Test**

:   Tests a vnode after all of the user authorization and connection data has been defined.

:   Netutil tests to see if a connection can be made to the remote instance using any of the connection data entries and remote user authorizations defined for the vnode. Note that individual connection data entries and remote user authorizations cannot be tested.

:   The Test operation has two options:

    - Connection – Tests connection data only.

    - Login – Tests both the connection and login data.

:   For more information, see [Establish and Test a Remote Connection Using Netutil](../Connectivity/Establish_and_Test_a_Remote_Connection_Using_Net.md).

**Help**

:   Displays help screens.

**End**

:   Exits netutil.
