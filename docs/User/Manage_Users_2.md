---
title: "Manage Users"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Manage_Users_2.htm"
canonical_id: "actian-data-platform-manage-users-2"
---

# Manage Users

## Overview of User Management

The Actian Data Platform grants user administrators the privilege to maintain users who have access to the database. A user with this privilege can create, delete, and update users, assign privileges and access levels to the sample data.

The privilege to maintain other users in the database is determined by the user’s assigned profile. The access rights to the sample data are controlled by the assigned group. When a new user is created, it should be assigned to a profile and a group, if applicable. The default dbuser user has a useradmin profile assignment and is part of the dbadmingrp.

For more information about Actian Data Platform accounts, see [Actian Data Platform Identity and Access Management](../Security/Actian_Data_Platform_Identity_and_Access_Managem.md). For more information about managing users through the console Administration interface, see [Manage Users](../User/Manage_Users.md).

!!! note "Note"

    To maintain users, useradmin (dbuser) must connect to the User Management database (iidbdb), not db.

The connection syntaxes to the User Management database (iidbdb) for native users are defined as follows:

**ODBC**

    - DRIVER={Actian};SERVER=@<warehouse_ ID>.avprod.actiandatacloud.com,tcp_ip,27832;DATABASE=iidbdb;

    - UID=dbuser;PWD=<password>;<additional_parameters>

    You can find and copy the warehouse ID for your warehouse from the Warehouse ID field on the warehouse’s [Warehouse Details](../User/Warehouse_Details.md) page.

    For more information about ODBC connection, see [Connection Tools](../User/Connection_Tools.md).

**JDBC**

:   For JDBC driver older than 4.3.7:

    - jdbc:ingres://<warehouse_ID>.avprod.actiandatacloud.com:27839/iidbdb;encryption=on;

    - UID=dbuser;PWD=<password>;<additional_parameters>

:   For JDBC driver 4.3.7 or newer:

    - jdbc:actian://<warehouse_ID>.avprod.actiandatacloud.com:27839/iidbdb;encryption=on;

    - UID=dbuser;PWD=<password>;<additional_parameters>

    You can find and copy the warehouse ID for your warehouse from the Warehouse ID field on the warehouse’s [Warehouse Details](../User/Warehouse_Details.md) page.

    For more information about JDBC connection, see [Connection Tools](../User/Connection_Tools.md).

**Actian SQL Command Line Interface (Actian SQL CLI)**

    - sql +user=dbuser @<warehouse_ID>.avprod.actiandatacloud.com,tcp_ip,27832::iidbdb

**Query Editor**

    - <warehouse_name> – User Management (iidbdb) connection

![](images/QueryEditor_database_dropdown.png)

More information:

For more information about user administration and implementing security, see the Security Guide.
