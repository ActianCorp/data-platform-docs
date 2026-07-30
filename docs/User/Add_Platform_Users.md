---
title: "Add Platform Users"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Add_Platform_Users.htm"
canonical_id: "actian-data-platform-add-platform-users"
---

## Add Platform Users

!!! note "Note"

    This section is for users with Account Administrator access to an Actian Data Platform account. For more information, see [User Roles](../User/User_Roles.md).

!!! warning "Important"

    **IMPORTANT!**Beginning with the January 2022 release, user access to the Actian Data Platform has changed. If you were not previously an Account Administrator, you can still log in but will have no access to warehouses or other features. (Your user status defaults to No Role.)

    If you receive the following message, contact your Account Administrator to assign you the role of Warehouse User or Warehouse Administrator (see [User Roles](../User/User_Roles.md)):

     Service Unavailable 403 Insufficient privilege to perform requested operation.
    After your Account Administrator assigns a role to you, you must log out of the console and log back in to enable your new role assignment (see [Log Out](../User/Log_Out.md) and [Log In](../User/Log_In.md)).

Account Administrators may:

- Enable or disable administrative privileges for users
- Activate or deactivate account users

- Assign or change roles for account users

To open the Administration interface and display User Management

1. In the upper right corner of the Actian Data Platform console window, click the user menu and select Administration:

    ![](images/AdministrationMenuItem_2.png)

    The Administration interface opens in a new browser tab.

2. In the pane on the left, click User Management.

    The User Management page is displayed on the right.

For more information about monitoring account AU usage, see [Monitor AU Usage](../User/Monitor_AU_Usage.md).

Add Platform Users

1. Click the Add Platform User button at the right of the User Management page.
2. Complete the new user information to create a Warehouse User or Warehouse Administrator.

    - Username

    - API Password/Confirm - the API password enables direct access for applications that cannot support OAuth flows.

    - First/Last Name

    - Account Administrator - manages user access and administers account warehouses.

    - Active

    - Role - select Warehouse User or Warehouse Administrator

3. Click Create a New Platform User button to create the user.

To search for a user

1. Click the Search icon at the right of the header bar to open the Search field.
2. Enter your search text, for example, all or part of the username you want to find.

    Matching usernames are displayed.

3. Click the X on the Search field to clear the entry and redisplay all usernames.

To enable or disable Admin privileges for a user

1. Click the username of the user you want to modify.

    The User Details dialog opens.

2. Click the desired option next to Account Administrator.
3. Click Save.

To activate or deactivate a user

1. Click the username of the user you want to modify.

    The User Details dialog opens.

2. Click the Yes or No option next to Active.
3. Click Save.

Deactivated users will still be able to log in to the Actian Data Platform but be unable to view any warehouses.

To assign or modify a user’s role

!!! note "Note"

    The Role dropdown is available only for non-administrative users.

1. Click the username of the user you want to modify.

    The User Details dialog opens.

2. Select the role for the user from the Role dropdown.
3. Click Save.
