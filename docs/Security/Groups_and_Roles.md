---
title: "Groups and Roles"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Groups_and_Roles.htm"
canonical_id: "actian-data-platform-groups-and-roles"
---

## Groups and Roles

Groups and roles can simplify control of database access. Groups are used to apply permissions to a list of users, while roles are used to associate subject privileges and permissions with an application.

## Groups

A groupis an identifier that can be used to apply permissions to a list of users associated with the identifier.

A group allows multiple users to be referenced by a single name.

For example, a company has an accounting group to identify the accounting department employees as a whole, and a payroll group to identify the payroll department employees as a whole. To define these groups, the DBA creates the groups and adds all the users in the associated departments to their respective groups. The groups can be easily maintained by adding and dropping users as they join or leave the departments.

!!! note "Note"

    A user can be a member of more than one group.

### Working with Group Objects

You can perform the following basic operations on group objects:

- Create and alter group objects
- View existing group objects, including the detailed properties of each individual object

- Drop group objects

In SQL, you can accomplish these tasks with the [CREATE GROUP](../SQLLanguage/CREATE_GROUP.md), [ALTER GROUP](../SQLLanguage/ALTER_GROUP.md), and [DROP GROUP](../SQLLanguage/DROP_GROUP.md) statements when working in a session connected to the User Management database (iidbdb).

### Examples: Creating, Altering, and Dropping a Group using SQL Statements

To create a new group, specify a user-defined group ID in a [CREATE GROUP](../SQLLanguage/CREATE_GROUP.md) statement, and then list the users in the group on the WITH USERS clause. The group can be amended later by ADD USERS or DROP USERS clauses on the [ALTER GROUP](../SQLLanguage/ALTER_GROUP.md) statement. The group can be deleted with the [DROP GROUP](../SQLLanguage/DROP_GROUP.md) statement.

Here are examples of using the [CREATE GROUP](../SQLLanguage/CREATE_GROUP.md), [ALTER GROUP](../SQLLanguage/ALTER_GROUP.md), and [DROP GROUP](../SQLLanguage/DROP_GROUP.md) statements:

1. Create a group identifier for a company’s telephone sales force and put the salespersons’ user IDs in the group user list:

```
CREATE GROUP tel_sales   WITH USERS = (harryk, videls, jerryw, arlenep);
```

2. Create the group identifier and_muchmuchmore and reserve it for later use. This is done by omitting the WITH USERS clause:

```
CREATE GROUP and_muchmuchmore;
```

3. Add two users to the group tel_sales and drop three users.

    The adding and dropping must be done in separate ALTER statements:

```
ALTER GROUP tel_sales   ADD USERS (dannyh, helent);
```

```
ALTER GROUP tel_sales   DROP USERS (harryk, videls, arlenep);
```

4. Drop all users from the group researchers. Then drop the group. The DROP ALL option should be run prior to dropping a group, since a group cannot be dropped if its user list has any members.

```
ALTER GROUP researchers DROP ALL;DROP GROUP researchers;
```

    If a user is dropped from a group but is currently active in a session, that session continues to have the group’s permissions until it terminates. “Currently active” means that the user is currently connected to a database. If a group is dropped, all the permissions assigned to the group are dropped.

### Groups and Permissions

After a group is created, you can associate permissions with it. When you grant permission to a group, you are, in effect, granting that same permission to each user in the group.

Groups are a convenient way to give the same permissions to many users at once.

Groups also make managing the permissions easy by allowing you to add users to (and remove users from) the group. For example, grant the payroll group insert, delete, and select permissions on the payroll tables, which gives all the users in the group those permissions. If an employee leaves the payroll department, or if a new employee joins, you simply have to drop or add a user from the group, without modifying the permissions. Similarly, if you find that the group needs fewer or more permissions, revoke or grant the permissions once, for the entire group, rather than individually for each member of the group.

Being a member of a group, however, does not automatically give a user the permissions granted to the group. Users must specifically identify themselves as part of a group to be allowed the associated permissions.

A user can be identified as part of a group in the following ways:

- Specifying a group ID at session startup
- Specifying a default group for the user. A default group is specified for a user using the SQL statements [CREATE USER](../SQLLanguage/CREATE_USER.md) or [ALTER USER](../SQLLanguage/ALTER_USER.md).

## Roles

A roleis an identifier that can be used to associate permissions with applications.

A role is typically associated with one or more applications to grant permissions to those applications.

For example, a company uses a restricted application that performs certain checks before updating the payroll tables to ensure that these tables are updated correctly. The DBA defines a role, for example update_payroll, and later assigns appropriate permissions for the necessary tables. The application developer associates the role with the application.

!!! note "Note"

    When defining a role, the DBA typically works with the application developer, so that they can agree on what role identifier and password to use for specific applications.

For further security, a role password can be specified. The role password is optional.

### Working with Role Objects

You can perform the following basic operations on roles:

- Create and alter role objects

!!! note "Note"

    Passwords can be associated with role objects as well as with user objects. The section [User Password](../Security/Authorizing_User_Access_for_a_Warehouse.md) contains more information about passwords.

- View existing role objects, including the detailed properties of each object
- Drop role objects

In SQL, you implement roles with the [CREATE ROLE](../SQLLanguage/CREATE_ROLE.md), [ALTER ROLE](../SQLLanguage/ALTER_ROLE.md), and [DROP ROLE](../SQLLanguage/DROP_ROLE.md) statements when working in a session connected to the User Management database (iidbdb).

### Examples: Creating, Altering, and Dropping a Role Using SQL Statements

Here are examples of using the [CREATE ROLE](../SQLLanguage/CREATE_ROLE.md), [ALTER ROLE](../SQLLanguage/ALTER_ROLE.md), and [DROP ROLE](../SQLLanguage/DROP_ROLE.md) statements:

1. Create a role identifier and password for an inventory application for a bookstore:

```
CREATE ROLE bks_onhandWITH PASSWORD = ’hgwells’;
```

!!! note "Note"

    Enclose any special characters or blanks in the roll password in single quotes. Blanks are not significant in passwords—for example, 'a b c' is equivalent to 'abc'. The password can be up to 24 characters in length. (You should choose long passwords that cannot be easily guessed.) If no password is assigned, then all users that have been granted access to that role have access to the role identifier and its associated permissions. (See the [GRANT (role)](../SQLLanguage/GRANT_(role).md) statement.) If a password is assigned, then the user or application must additionally use the password to access the role.

2. Create a role identifier with no password for the daily sales application for a bookstore:

```
CREATE ROLE dly_sales WITH NOPASSWORD;
```

3. Create dual role IDs (these function as synonyms) and password for a recommended list application for a bookstore:

```
CREATE ROLE sclemens, mtwainWITH PASSWORD = ’goodluck’;
```

4. Change the password for the existing role identifier new_accounts to eggbasket:

```
ALTER ROLE new_accountsWITH PASSWORD = eggbasket;
```

5. Drop the existing role identifier sales_report:

```
DROP ROLE sales_report;
```

### Roles and Permissions

After a role is created, you can then associate permissions with it and create grants to it for individual users. For example, for the associated application to execute properly, grant update permission to all payroll tables for the update_payroll role. For more information, see [Object Permissions (Grants)](../Security/Object_Permissions_(Grants).md).

When you grant an object permission or a subject privilege to a role, you are, in effect, granting that same permission or privilege to any session that is started using that role.
