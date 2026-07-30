---
title: "Warehouse Authorization Identifiers"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Warehouse_Authorization_Identifiers.htm"
canonical_id: "actian-data-platform-warehouse-authorization-identifiers"
---

## Warehouse Authorization Identifiers

Access can be granted to the following authorization identifiers. Identifiers are listed from highest to lowest precedence, which determines the privilege enforced for a session if a particular privilege is defined for more than one authorization identifier associated with a session.

**Role**

:   Roles simplify access to the database by associating subject privileges and permissions with an application. Roles can be created with the option of an additional password. For more information, see [Groups and Roles](../Security/Groups_and_Roles.md).

**User**

:   For each valid Actian Data Platform user, a user object must be created in the Actian Data Platform User Management database (iidbdb). The user object specifies the user name, default group, default profile, subject privileges, and other attributes. For more information, see [Manage Users](../User/Manage_Users_2.md).

**Group**

:   Groups simplify managing permissions because individual users can be added or removed from groups as required. Being a member of a group does not automatically give the user the permissions granted to the group. The user must have the group specified as its default group or specify the group name in the session startup. For more information, see [Groups and Roles](../Security/Groups_and_Roles.md).

**Public**

:   Granting permissions on objects to PUBLIC allows any user, group, or role access to those objects. The use of grants to PUBLIC should be limited. For more information, see [Working with Grants](../Security/Object_Permissions_(Grants).md).
