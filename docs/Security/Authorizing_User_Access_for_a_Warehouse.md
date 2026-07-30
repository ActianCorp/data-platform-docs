---
title: "Authorizing User Access for a Warehouse"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Authorizing_User_Access_for_a_Warehouse.htm"
canonical_id: "actian-data-platform-authorizing-user-access-for-a-warehouse"
---

# Authorizing User Access for a Warehouse

Users are defined using user objects and, optionally, profile objects.

A user object is a definition that specifies the user’s name, default group, default profile, subject privileges, and several other attributes.

A profile is a template that defines a set of subject privileges and other attributes that can be applied to one or more users. You can streamline the user authorization process by using profiles.

## Working with User Objects

You can perform the following basic operations on user objects:

- Create and alter user objects
- View existing user objects, including the detailed properties of each object

- Drop user objects

In SQL, you can use the [CREATE USER](../SQLLanguage/CREATE_USER.md), [ALTER USER](../SQLLanguage/ALTER_USER.md), and [DROP USER](../SQLLanguage/DROP_USER.md) statements when working in a session connected to the User Management database (iidbdb).

!!! note "Note"

    Many of the features associated with a user object, such as subject privileges, password, expiration date are security-related features described later in this guide.

### User Expiration Date

The user expiration date is an optional part of the user definition. It determines the date after which the user can no longer access Actian Data Platform.

An expiration date can be specified as any valid Actian Data Platform date or as a date or time interval. For example, you might specify an interval of “1 month” or “1 year,” or an absolute date, such as “5‑jan‑2020.”

The user expiration date is checked each time the user connects to the warehouse. If the expiration date has passed, then access is denied.

To enable an expired user to connect, the associated user (or profile) object must be modified to reset the expiration date.

### User Password

A password can be specified as part of the user definition. A password is only required for native warehouse users and not for single sign-on users since they are authenticated by their credentials from the configured identity provider.

A user with the [CHANGE_PASSWORD Privilege](../Security/Assigning_Privileges_and_Granting_Permissions.md) is permitted to change his own password; to do so, however, he must supply his old password. A user with the [MAINTAIN_USERS Privilege](../Security/Assigning_Privileges_and_Granting_Permissions.md) can change the password of another user, in addition to changing the method of password validation or removing the password altogether.

!!! note "Note"

    Passwords also apply to roles.

## Working with Profile Objects

You can perform the following basic operations on profile objects:

- Create and alter profile objects
- View existing profile objects, including the detailed properties of each object

- Drop profile objects

In SQL, you can use the [CREATE PROFILE](../SQLLanguage/CREATE_PROFILE.md), [ALTER PROFILE](../SQLLanguage/ALTER_PROFILE.md), and [DROP PROFILE](../SQLLanguage/DROP_PROFILE.md) statements when working in a session connected to the User Management database (iidbdb).

### Example of Using a Profile

After a profile is created, it can be associated with a new or existing user object as the default profile for that user. By doing so, the attributes defined in the profile are associated with the user, and the user’s attributes are updated whenever the profile is modified.

Attributes can also be set directly at the user level to override settings at the profile level.

### Default Profile

A default profile is the profile initially assigned to a user if one is not explicitly assigned.

The default profile specifies the following:

- No default group
- No subject privileges or default privileges

- No expiration date

**Notes:**

- You can alter the default profile but you cannot drop it.
- Altering the default profile will alter privilege attributes of all users that have not been given a specific profile.

You change the default profile using the [ALTER DEFAULT PROFILE](../SQLLanguage/ALTER_PROFILE.md) statement.
