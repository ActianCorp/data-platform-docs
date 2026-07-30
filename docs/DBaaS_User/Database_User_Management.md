---
title: "Database User Management"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Database_User_Management.htm"
canonical_id: "actian-data-platform-database-user-management"
---

## Database User Management

The initial user credentials that are given for the Actian Data Platform are Single Sign-On (SSO) users that are configured to iidbdb, accessible from the Query Editor. The credentials enable you to connect to your database. You can add additional types of users, depending on your needs.

[Add Platform Users](../DBaaS_User/Add_Platform_Users.md): These users can login to the Actian Data Platform and perform tasks as set by permissions and policies. For example, a platform user might administrate all additional users to your Actian Data Platform installation.

!!! note "Note"

    Additional platform users do not automatically have access to databases.

[Add Native Users](../DBaaS_User/Add_Native_Users.md): These users are for database access only. You configure these users in iidbdb / accessdb with a simple password authentication. For users that own schemas/objects in the database, native users are easier to use from scripts and remote servers.

!!! note "Note"

    These users cannot access the platform.

[Add SSO Users](../DBaaS_User/Add_SSO_Users.md): Database users with Actian Data Platform SSO authentication are configured in iidbdb, but must also be added as Platform users separately.
