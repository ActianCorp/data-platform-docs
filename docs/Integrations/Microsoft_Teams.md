---
title: "Microsoft Teams"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Microsoft_Teams.htm"
canonical_id: "actian-data-platform-microsoft-teams"
---

## Microsoft Teams

Microsoft Teams connector allows you get the details of messages, Teams, Groups, and Channels.

- [Prerequisites](../Integrations/Microsoft_Teams.md)
- [Connection Details](../Integrations/Microsoft_Teams.md)

- [Additional Information](../Integrations/Microsoft_Teams.md)

Prerequisites

You must have an active Microsoft 365 subscription that includes Microsoft Teams.

Microsoft Teams relies on Azure AD for authentication and user management.

You need a Microsoft Developer account to register your application and obtain the necessary credentials.

You should configure proper API permissions by accessing the Azure portal, registering your application, and then adding your API permissions.

Connection Details

The Microsoft Teams connector authenticates with your Microsoft account using OAuth2.0.

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | The Client ID is the public identifier for your Microsoft Teams app. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| Tenant ID | A unique identifier assigned to your application when you register it to Azure AD. |
| Base URL | The base URL where the Microsoft API is hosted. For example:`https://graph.microsoft.com` |
| Access Token URL | The URL to generate the access token:`https://www.linkedin.com/oauth/v2/accessToken.` |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token. |
| Authorize button | Click to generate the access token. |

Additional Information

For more information, please refer to the Microsoft documentation at:
[https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow ).
[https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview).
