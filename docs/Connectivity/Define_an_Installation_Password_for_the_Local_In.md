---
title: "Define an Installation Password for the Local Instance"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Define_an_Installation_Password_for_the_Local_In.htm"
canonical_id: "actian-data-platform-define-an-installation-password-for-the-local-in"
---

## Define an Installation Password for the Local Instance

To define an Installation Password for the local instance

1. Enter the following command at the operating system prompt:

```
netutil
```

    The netutil startup screen appears.

2. Make sure that the cursor is in the Virtual Node Name table, and then choose Create from the menu.

    A pop-up window appears, displaying the following prompt:

```
Enter new virtual node name:
```

3. Enter the virtual node name for the local instance and choose OK from the menu.

!!! note "Note"

    The virtual node name must be identical to the name that has been configured as LOCAL_VNODE on the Configure Name Server screen of the Configuration-By-Forms (cbf) utility and is typically the same as the local machine name.

    A pop-up window appears, displaying the following prompt:

```
Choose type of login to be createdGlobal – Any user on [local node]Private – User [user name] only
```

4. Highlight Global by using the arrow keys, and then choose Select from the menu.

    The Enter new login/password pop-up window appears. It displays prompts for the global login, the password, and verification of the password.

5. Enter an asterisk in the Global Login field, enter an Installation Password in the Password field, and finally re-enter the password as prompted. (Notice that for security purposes neither the password nor the verification appears on screen.) When you have entered this information, choose Save from the menu.

    The Enter new connection pop-up window appears. It displays prompts for the connection type (private or global), the network address, the network protocol to be used, and the Listen address of the instance.

6. Choose Cancel from the menu. (It is not necessary to enter connection data for the local instance.)

    Netutil returns to the startup screen. The data you entered in the previous steps is displayed in the vnode and Login/password data tables.
