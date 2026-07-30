---
title: "Manage Users"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Manage_Users.htm"
canonical_id: "actian-data-platform-manage-users"
---

## Manage Users

!!! note "Note"

    This section is for users with Account Administrator access to an Actian account. Account Administrators may:

- Enable or disable administrative privileges for users
- Activate or deactivate account users

- Assign or change roles for account users
- Add platform users

To accomplish any of these tasks, perform the appropriate procedure below.

To search for a user

1. Open the Administration interface (see [Access the Administration Interface](../DBaaS_User/Database_Administration.md)).
2. In the pane on the left, click User Management.

    The User Management page is displayed on the right.

3. Click the Search icon at the right of the header bar to open the Search field.
4. Enter your search text, for example, all or part of the username you want to find.

    Matching usernames are displayed.

5. Click the X on the Search field to clear the entry and redisplay all usernames.

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

Deactivated users will still be able to log in to Actian but be unable to view any warehouses.

To assign or modify a user’s role

!!! note "Note"

    The Role dropdown is available only for non-administrative users.

1. Click the username of the user you want to modify.

    The User Details dialog opens.

2. Select the role for the user from the Role dropdown.
3. Click Save.

To add a platform user

A platform user is one who has access to Google Cloud data sources and Integrations.

1. Click the Add Platform User button.

    The Create a New Platform User dialog opens.

2. Enter the user’s email address as their username.
3. Provide and confirm an API password (provides direct API access for applications that do not support OAuth flows).

4. (Optional) Enter a first and last name for the user.
5. Choose whether the user should be an Account Administrator.

6. Choose whether the user should be active.
7. Select the user’s role from the dropdown.

8. Click the Create a New Platform User button.

    The user is added to the list.
