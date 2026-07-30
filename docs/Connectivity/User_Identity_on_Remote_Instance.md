---
title: "User Identity on Remote Instance"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "User_Identity_on_Remote_Instance.htm"
canonical_id: "actian-data-platform-user-identity-on-remote-instance"
---

## User Identity on Remote Instance

A user’s identity when working on a remote instance depends upon the type of access authorized. When access is authorized through a user name and password (whether an operating system account or DBMS authentication) on the remote instance’s host machine, users take on the identity of this account when working on the remote instance.

In either case, the user’s privileges and permissions on the remote instance can differ from those on the local instance. For example, a user can have system administrator privileges on the local instance but only very general, low-level privileges and permissions on the remote instance. It is important to make sure that the privileges and permissions assigned to you on the remote instance are adequate for the work that you intend to perform.

User privileges and permissions are set up individually for each instance using the [CREATE USER](../SQLLanguage/CREATE_USER.md) statement. They apply only to the instance on which they are set up. For more information about this procedure, see the Security Guide.

## Verify Your Identity

When impersonating a user using the -u command flag, you may need to verify your identity.

To verify your identity

Use the following command:

```
dbmsinfo('username')
```

The user ID that you are working under is displayed.
