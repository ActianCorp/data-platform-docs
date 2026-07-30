---
title: "Single Sign-on Users, Native Users, and Platform Users"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Single_Sign-on_Users__Native_Users__and_Platform.htm"
canonical_id: "actian-data-platform-single-sign-on-users-native-users-and-platform"
---

## Single Sign-on Users, Native Users, and Platform Users

Single sign-on (SSO) users are users added and authenticated by an identity provider, which could be Actian or a customer-internal identity provider.

Query Editor uses login information from the console, which is always an SSO user added to Salesforce (at this time) and the customer’s identity provider in the future. The same username is used to authenticate the user in the background to use Query Editor.

Native users exist only in the scope of an Actian warehouse. These users cannot be used to log in to the Actian Data Platform web console and can be used only directly with the warehouse. Using SSO users within Query Editor creates a more natural environment and flow when creating warehouses and then attempting to run queries against them.

More information:

- [Actian Data Platform Identity and Access Management](../Security/Actian_Data_Platform_Identity_and_Access_Managem.md)
- [Types of Users](../User/Types_of_Users.md)

- [Add Native Users](../User/Add_Native_Users.md)
- [Add SSO Users](../User/Add_SSO_Users.md)

- [Add Platform Users](../User/Add_Platform_Users.md)
