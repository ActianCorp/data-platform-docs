---
title: "Typeform"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Typeform.htm"
canonical_id: "actian-data-platform-typeform"
---

## Typeform

The Typeform connector allows you to retrieve data from your Typeform Application. This includes workspaces, forms, insights and form responses.

- [Prerequisites](../Integrations/Typeform.md)
- [Connection Details](../Integrations/Typeform.md)

- [Additional Information](../Integrations/Typeform.md)

Prerequisites

You must have a Typeform account.

Connection Details

The connector authenticates with Typeform using OAuth2.0.

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | A unique string that identifies your application when using OAuth 2.0. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| Base URL | The base URL where the Typeform API is hosted. For example:`https://api.typeform.com` |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.**Note:**Currently, we are not regenerating access tokens using this option. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the Typeform API documentation for more info on the API requests and responses. API docs can be found at [https://www.typeform.com/developers/get-started/](https://www.typeform.com/developers/get-started/).
