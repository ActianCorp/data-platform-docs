---
title: "Assigning Privileges and Granting Permissions"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Assigning_Privileges_and_Granting_Permissions.htm"
canonical_id: "actian-data-platform-assigning-privileges-and-granting-permissions"
---

# Assigning Privileges and Granting Permissions

## Subject Privileges

A subject privilege defines the type of operations permissible in a user session. Subject privileges are assigned to a user (subject).

Subject privileges are typically assigned when a user object is created or modified. Subject privileges can also be assigned to roles, as discussed in [Groups and Roles](../Security/Groups_and_Roles.md).

To set or change subject privileges for a user, you must have the MAINTAIN_USERS privilege (see [ALTER USER](../SQLLanguage/ALTER_USER.md)).

!!! warning "Important"

    **IMPORTANT!**Subject privileges allow many trusted operations to be performed. Therefore, assign privileges with care, especially the Security privilege.

The subject privileges are as follows:

**CHANGE_PASSWORD**

:   Enables the user to change his password.

**IMA_SEC_READ**

:   Enables warehouse administrators to access IMA tables. Access to IMA tables enables users to view various real-time monitoring information.

**MAINTAIN_USERS**

:   Enables the user to perform various user-related functions, such as creating users and roles

**UNMASK**

:   Allows the user to see masked columns without masking, to use the MASK_COLUMN() function in views, and to use COPY INTO when a table contains columns marked as MASKED

## CHANGE_PASSWORD Privilege

The CHANGE_PASSWORD privilege lets users change their password (but not those of others).

## IMA_SEC_READ Privilege

The IMA_SEC_READ privilege enables warehouse administrators to access IMA tables. Access to IMA tables enables users to view various real-time monitoring information. For more information, see [Working with Monitoring (imadb) Tables](../User/Working_with_Monitoring_(imadb)_Tables.md).

## MAINTAIN_USERS Privilege

The MAINTAIN_USERS privilege allows a user to perform various user-related functions.

A user with this privilege can:

- Maintain profiles using CREATE/ALTER/DROP PROFILE statements
- Maintain users using CREATE/ALTER/DROP USER statements

- Maintain groups using CREATE/ALTER/DROP GROUP statements
- Maintain roles using CREATE/ALTER/DROP ROLE statements

## UNMASK Privilege

The UNMASK privilege allows users to:

- View data that is masked
- Use the MASK_COLUMN() function in views to control access to and the presentation of masked data

- Use COPY INTO when a table contains columns marked as MASKED

## Sets of Privileges Associated with a Session

In addition to assigning subject privileges to a user, Actian Data Platform lets you define a default set of subject privileges that will be available at session startup.

In addition, any privilege assigned to the user can be added or dropped during the life of the session; this capability effectively applies the principle of least privilege.

The principle of least privilege asserts that a subject must have the minimum privileges required to perform an operation, and that these privileges must be active for the minimum amount of time necessary to perform that operation.

Thus, a session has three sets of privileges associated with it:

- The default privilege set contains those privileges that become active when a connection to Actian Data Platform is initiated.
- The working privilege set contains those privileges that are active at any particular time (at session startup, the working privilege set is equivalent to the default privilege set).

- The maximum privilege set contains all privileges that a particular user is allowed to have.

The working privilege set is determined during the life of the session, when privileges can be made active as necessary to allow a privileged operation to be performed and made inactive on completion of the task.

The working privilege set is specified using the SET SESSION statement. Using SET SESSION, you can:

- Add allowed privileges to the working privilege set
- Drop privileges from the working privilege set

- Replace the working privilege set with specified allowed privileges
- Set the working privilege set to all allowed privileges

- Reset the working privilege set to the default privilege set
- Remove all privileges from the working privilege set
