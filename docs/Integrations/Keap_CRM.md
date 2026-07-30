---
title: "Keap CRM"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Keap_CRM.htm"
canonical_id: "actian-data-platform-keap-crm"
---

## Keap CRM

The Keap CRM connector is a Rest API connnector which retrieves the data of each of the objects and creates specific tables in the ActianWarehouse.

- [Prerequisites](../Integrations/Keap_CRM.md)
- [Connection Details](../Integrations/Keap_CRM.md)

- [Additional Information](../Integrations/Keap_CRM.md)

Prerequisites

You must have a Keap CRM account and create an app in Keap CRM using the Actian Redirect URI.

Connection Details

The Keap CRM connector authenticates using OAUTH 2.0. Please refer to documentation for Keap CRM authentication:[https://developer.infusionsoft.com/getting-started-oauth-keys/](https://developer.infusionsoft.com/getting-started-oauth-keys/).

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | The Client ID is the public identifier for your Keap CRM app. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.**Note:**Currently, we are not regenerating access tokens using this option. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the Keap CRM API documentation for more info on the API requests and responses. API docs can be found at [https://developer.infusionsoft.com/docs/rest/](https://developer.infusionsoft.com/docs/rest/).
