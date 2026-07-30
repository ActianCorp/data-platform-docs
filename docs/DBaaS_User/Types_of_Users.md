---
title: "Types of Users"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Types_of_Users.htm"
canonical_id: "actian-data-platform-types-of-users"
---

## Types of Users

Three types of users can connect to Actian: native users, platform users, and single sign-on (SSO) users of systems such as Salesforce (for example, name@company.com) used to access the Actian. For more information, see [Single Sign-on Users, Native Users, and Platform Users](../DBaaS_User/Single_Sign-on_Users__Native_Users__and_Platform.md).

!!! note "Note"

    Currently SSO users can access only the warehouse database using [Query Editor](../DBaaS_User/Part_QueryEditor.md). SSO users are limited to short names (schema name) of 32 characters and long names of 160 characters, both including quotes; for more information, see [ALTER USER](../SQLLanguage/ALTER_USER.md), LONG_NAME parameter.

Adding SSO users at warehouse creation time to the dbadmingrp ensures that they have privileges to data granted to dbadmingrp. To ensure all dbadmingrp members have access to the data, grant all privileges on a table to the group dbadmingrp after the table is created by either an SSO or native warehouse user.

The warehouse owner (SSO user) and dbuser are part of dbadmingrp by default.

Related topics:

- [Add Native Users](../DBaaS_User/Add_Native_Users.md)
- [Add SSO Users](../DBaaS_User/Add_SSO_Users.md)

- [Actian Data Platform Identity and Access Management](../Security/Actian_Data_Platform_Identity_and_Access_Managem.md)
