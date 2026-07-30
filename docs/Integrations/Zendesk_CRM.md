---
title: "Zendesk CRM"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Zendesk_CRM.htm"
canonical_id: "actian-data-platform-zendesk-crm"
---

## Zendesk CRM

The Zendesk CRM (Zendesk Sell) connector lets you tap into Zendesk Sell and retrieve all object data present inside your Zendesk Sales app.

- [Prerequisites](../Integrations/Zendesk_CRM.md)
- [Connection Details](../Integrations/Zendesk_CRM.md)

- [Additional Information](../Integrations/Zendesk_CRM.md)

Prerequisites

You must have a Zendesk Sell account and create an app with the Default Redirect URI from the Actian Data Platform to generate credentials and start OAuth 2.0 authentication.

To set up the OAuth 2.0 authentication, please refer to [https://developer.zendesk.com/api-reference/sales-crm/authentication/introduction/](https://developer.zendesk.com/api-reference/sales-crm/authentication/introduction/).

For Registering an application, please refer to the URL regarding creating a Developer app in the OAuth2 Settings: [https://app.futuresimple.com/settings/oauth/apps](https://app.futuresimple.com/settings/oauth/apps.).

Connection Details

The Zendesk Sell connector authenticates using OAuth 2.0 protocols.

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | A unique string that identifies your application when using OAuth 2.0. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| API version | Specify an API version, for example: v2. |
| Base API URL | The base URL where the Zendesk Sell API is hosted. For example:`https://api.getbase.com` |
| Access Token URL | The URL to generate the access token. For example:`https://api.getbase.com/oauth2/token` |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.**Note:**Currently, we are not regenerating access tokens using this option. |
| Authorize button | Click to generate the access token. |

!!! note "Note"

    You need to authenticate the connection before running any integration.

Additional Information

Please refer to the Zendesk Sell API documentation for more info on the API requests and responses. This connector only supports CORE APIs, please refer to the CORE API section in the documentation to get information on the APIs. API docs can be found at [https://developer.zendesk.com/api-reference/sales-crm/introduction/](https://developer.zendesk.com/api-reference/sales-crm/introduction/).
