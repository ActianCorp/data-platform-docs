---
title: "Set the dbuser Connection Password"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Set_the_dbuser_Connection_Password.htm"
canonical_id: "actian-data-platform-set-the-dbuser-connection-password"
---

## Set the dbuser Connection Password

!!! note "Note"

    This section applies only to Azure and AWS AV-1 warehouses.

The dbuser is the local database user with administrative privileges on the db database. It is able to manage other users (add, alter, remove; see [Manage Users](../User/Manage_Users_2.md)) and has all privileges for sample data (select, alter, delete, copy, reference, and so on). It is a member of the dbadmingrp (see [User Groups](../User/User_Groups.md)).

It is used for managing users; database administration; and for any JDBC, ODBC, and CLI connections when dbuser is specified as the connecting user.

The dbuser has identical privileges to the warehouse creator. The dbuser is a database user that has equivalent privilege levels and access to the warehouse creator, who is an SSO user (see [Types of Users](../User/Types_of_Users.md)). The dbuser and warehouse creator can create and assign privileges to other account users. The dbuser and warehouse creator are both database administrators.

After warehouse creation ([Create a Warehouse](../User/Create_a_Warehouse.md)), one of your first tasks should be to set a password for the dbuser to ensure it is available for use in other tools and applications.

!!! warning "Important"

    **IMPORTANT!**To perform this task, the warehouse must be in a Running state.

To set the dbuser database connection password

1. On the Warehouses page, click the name of the warehouse whose dbuser password you want to set.

    The [Warehouse Details](../User/Warehouse_Details.md) page is displayed.

2. In the Connection Password field, click the Set Connection Password link.

    The Database Connection Password dialog appears.

3. Enter the new password of at least 7 characters and confirm it.
4. Click Save.
