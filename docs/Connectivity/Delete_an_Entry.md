---
title: "Delete an Entry"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Delete_an_Entry.htm"
canonical_id: "actian-data-platform-delete-an-entry"
---

## Delete an Entry

To delete a virtual node entry or one of its connection data entries, remote user authorizations or attributes, place the cursor on the desired record and choose Destroy from the menu.

### Delete All Vnode Information

To delete all information for a specific vnode

1. Highlight the desired entry in the Virtual Node Name table and choose Destroy from the menu.

    A pop-up window appears with the following prompt:

```
Really destroy all data for vnode [vnode name]?No – Do not destroy all data for vnodeYes – Destroy all data for vnode
```

2. Use the arrow keys to highlight No or Yes (No is the default); then choose Select from the menu.

    Netutil removes the vnode from the Virtual Node Name table and all associated information from the Login/password data and Connection data tables.

#### Delete a Connection Entry for a Vnode

To delete one of the connection data entries associated with a particular vnode

1. Highlight the desired entry in the Connection Data table and choose Destroy from the menu.

    A pop-up window appears with the following prompt:

```
Really destroy connection entry?No – Do not destroy connection entryYes – Destroy connection entry
```

2. Use the arrow keys to highlight No or Yes (No is the default), and then choose Select from the menu.

    Netutil removes the entry from the Connection Data table.

#### Delete a Remote User Authorization for a Vnode

To delete one of the remote user authorizations associated with a particular vnode

1. Highlight the desired entry in the Login/password data table and choose Destroy from the menu.

    A pop-up window appears with the following prompt:

```
Really destroy [private/global] login/password entry ‘[Login name]’?No – Do not destroy [private/global] login/password entryYes – Destroy [private/global] login/password entry
```

2. Use the arrow keys to highlight No or Yes (No is the default); then choose Select from the menu.

    Netutil removes the entry from the Login/password data table.

#### Delete an Attribute Associated with a Vnode

To delete an attribute associated with a particular vnode

1. From the netutil startup screen, select the Attributes menu option.

    The “Other attribute data” table is displayed.

2. Select the desired vnode from the Virtual Node Name table. Tab to the Other attribute data for vnode table, highlight the attribute that you want to delete, and choose Destroy from the menu.

    A pop-up window appears with the following prompt:

```
Really destroy attribute entry?No – Do not destroy attribute entryYes – Destroy attribute entry
```

3. Use the arrow keys to highlight No or Yes (No is the default); then choose Select from the menu.

    Netutil removes the attribute from the Other attribute data for vnode table.
