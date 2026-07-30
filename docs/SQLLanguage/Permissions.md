---
title: "Permissions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Permissions.htm"
canonical_id: "actian-data-platform-permissions"
---

## Permissions

To use [CREATE PROCEDURE](../SQLLanguage/CREATE_PROCEDURE.md), you must have permission to access the tables and views specified in queries issued by the procedure. If the procedure uses database events owned by other users, you must have the required permissions (RAISE and REGISTER) on the database events. If the procedure executes database procedures owned by other users, you must have EXECUTE permission for those procedures.

If permissions are changed after the procedure is created and the creator of the procedure no longer has permissions to access the tables and views, a runtime error results when the procedure is executed.

The GRANT statement can be used to assign the [NO]CREATE_PROCEDURE privilege to specific users, groups, and roles.
