---
title: "Update Allow List IP Addresses"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "UpdateAllowListIPs.htm"
canonical_id: "actian-data-platform-updateallowlistips"
---

# Update Allow List IP Addresses

After you have created a warehouse (see [Create a Warehouse](../User/Create_a_Warehouse.md)), you may add or remove IP addresses that can access the warehouse.

!!! note "Note"

    If you use Azure Private Link, you cannot use the private IP address in the Allow List. For more information, see Azure Private Link Limitations.

To update Allow List IP addresses

1. On the Actian Warehouses page, click the name of the warehouse whose IP addresses you want to change.

    The [Warehouse Details](../User/Warehouse_Details.md) page is displayed.

2. (Optional) In the IP Allow List IP field, click the Show IP Labels to toggle between text labels and address numbers:

![](images/IPAllowListToggle.png)

3. Click the ![](images/DownArrowBlue.png) button to display the complete list of IP addresses.
4. To add or remove IP addresses:

    a. Click the ![](images/PlusButtonBlue.png) button at the right end of the IP Allow List field.

    The IP Allow List dialog opens.

        - Sort the listed addresses by clicking the “IP Address” or “Label” column headers.

        - Search for labels or IP addresses by clicking in the search field and entering text.

        - Edit the text labels for any IP address by clicking in the label field and retyping the text.

    b. To delete an IP address, click the ![](images/TrashCanIcon.png) icon to the right of the address entry. Confirm the deletion.

    To delete multiple addresses, click the radio button to the left of each address and then select Delete IP Addresses from the Add Allowed IPs dropdown menu. Confirm the deletion.

    c. To add an IP address, click the Add Allowed IPs button. Enter one or more IP addresses, with or without [CIDR (Classless Inter-Domain Routing) blocks](https://searchnetworking.techtarget.com/definition/CIDR), separated by commas, and add an optional text label. Then click Add.

    CIDR blocks 24–30 are accepted. 31 is not accepted, and 32 is the same as the IP address itself. Enter in the form: XXX.XXX.XXX.XXX/##.

    The IP address list is updated for the warehouse within a minute.
