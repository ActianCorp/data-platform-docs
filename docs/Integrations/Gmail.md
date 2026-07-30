---
title: "Gmail"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Gmail.htm"
canonical_id: "actian-data-platform-gmail"
---

## Gmail

The Gmail connector lets you view and manage Gmail mailbox data like threads, messages, and labels.

- [Prerequisites](../Integrations/Gmail.md)
- [Connection Details](../Integrations/Gmail.md)

- [Additional Information](../Integrations/Gmail.md)

Prerequisites

You must have a Google developer account.

You must create a project.

You must create a developer application to generate a client ID and client secret for API connectivity.

For more details, please refer to [https://developers.google.com/gmail/api/reference/rest](https://developers.google.com/gmail/api/reference/rest).

Connection Details

The connector authenticates with your Google Account using OAuth2.0.

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | The client ID for your application. You can find this value in the API Console Credentials page.. |
| Redirect URI | Determines how Google's authorization server sends a response to your app. |
| Scope | A space-delimited list of scopes that identify the resources that your application could access on the user's behalf. |
| Authorization URL | The Authorization URL uses the Client ID, Redirect URI, and scope to generate the authorization code. |
| Refresh Token | A token that you can use to obtain a new access token. Refresh tokens are valid until the user revokes access. Note that refresh tokens are always returned for installed applications. |
| Access Token | The token that your application sends to authorize a Google API request. |
| Base URL | The Base URL for accessing the APIs must be specified:https://www.googleapis.com/gmail |

Additional Information

Please refer to the Google Authorization Flow Reference in [https://developers.google.com/identity/protocols/oauth2/native-app](https://developers.google.com/identity/protocols/oauth2/native-app).
