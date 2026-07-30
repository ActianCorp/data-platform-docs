---
title: "Permissions on Database Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Permissions_on_Database_Procedures.htm"
canonical_id: "actian-data-platform-permissions-on-database-procedures"
---

## Permissions on Database Procedures

A procedure is owned by the user who creates it or by the group or role specified in the CREATE PROCEDURE statement. A procedure can be executed by the owner and by any user, group, or role to whom the owner has granted execute permissions. Users, groups, and roles to which the owner has granted execute permission WITH GRANT OPTION can grant execute permission to other users.

Although a user can create a private procedure that accesses tables owned by other users, the user must have all required permissions on those tables to be able to execute the procedure. Those permissions must be granted to the specific user and not to groups or roles the user may be a member of.
