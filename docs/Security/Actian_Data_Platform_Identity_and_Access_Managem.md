---
title: "Actian Data Platform Identity and Access Management"
product: "Actian Data Platform"
guide: "Security Guide"
source_file: "Actian_Data_Platform_Identity_and_Access_Managem.htm"
canonical_id: "actian-data-platform-actian-data-platform-identity-and-access-managem"
---

## Actian Data Platform Identity and Access Management

A user represents a person or service that the Actian Data Platform supports. There are three types of users that can access and use the Actian Data Platform: SSO users, Platform users, and native users.

An SSO user is a single sign-on user that is created in a supported external IdP. The default IdP for Actian Data Platform is Salesforce Identity.

!!! note "Note"

    If you have SSO users that are having issues connecting to a warehouse, make sure your installation has the latest version of the Actian Data Platform Client. For more information, see [Actian Client Runtime Package](../User/Actian_Client_Runtime_Package.md).

A Platform user is set up on Actian Data Platform by an Actian administrator, and is not an SSO user. The Platform user can be set up to use APIs.

!!! note "Note"

    A Platform user does not automatically have access to the Actian Community, which provides access to Actian Academy training. For Platform users to get access to the Community, [register as a Community user at](https://communities.actian.com)[https://communities.actian.com.](https://communities.actian.com)

A native user is created within the warehouse itself. The following table explains these supported users, how they are different, and in which situations should they be used.

| User Type | Authenticating Server | Scope (Platform or Warehouse) | Supported Clients of Applications | Notes |
| --- | --- | --- | --- | --- |
| SSO | Supported OAuth2-compliant IdP | Platform and Warehouse | Web UI, Query Editor, OAuth supported clients (Tableau, DBeaver, etc...)Ideal for interactive users. | Will not work with clients that do not support connection through OAuth2 tokens and require a username/secret to be passed through the API.The SSO provider can be configured to support a user’s customer IdP, such as Okta. |
| SSO with device flow | Supported OAuth2-compliant IdP | Platform and Warehouse | SSH Clients, command line clients applications (any non-interactive clients with no web UI to perform OAuth 2 authentication).Ideal for situations where authentication needs to happen on a machine other than the client. | Will not work with clients that do not support connections through OAuth2 tokens and require a username/secret to be passed through the API.Will not work from within applications that use a UI and have no ability to standard output (Tableau, DBeaver, etc...).The SSO provider can be configured to support a user’s customer IdP, such as, Okta. |
| Native | Warehouse User Management DB (iidbdb) server | Warehouse | JDBC or ODBC applications that need a username/secret to connect and are unable to work with OAuth2 protocol.Ideal for applications that need to connect to the warehouse or for users using clients where a username/secret is required. | Example: Looker |
| Platform | Warehouse User Management DB (iidbdb) server | Platform and Warehouse | Web UI, Query Editor, OAuth supported clients (Tableau, DBeaver, etc...)Ideal for additional interactive users who are not available through SSO. | Platform users are managed by the platform. |
| API keys | Actian Data Platform authentication | Platform and Warehouse | Applications that need to use the Actian Data Platform REST API to perform platform operations or need to connect to the warehouse. | API keys are managed by the platform. |

More information:

- [Types of Users](../User/Types_of_Users.md)
- [Add Native Users](../User/Add_Native_Users.md)

- [Add SSO Users](../User/Add_SSO_Users.md)
- [Add Platform Users](../User/Add_Platform_Users.md)

- [API access with Platform User Accounts](../User/API_access_with_Platform_User_Accounts.md)
