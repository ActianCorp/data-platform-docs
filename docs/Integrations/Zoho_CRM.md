---
title: "Zoho CRM"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Zoho_CRM.htm"
canonical_id: "actian-data-platform-zoho-crm"
---

## Zoho CRM

The Zoho CRM connector retrieves the data of various Zoho CRM modules.

Zoho CRM provides standard modules such as Leads, Accounts, Contacts, Deals, Forecasts, Activities, and more.

- [Prerequisites](../Integrations/Zoho_CRM.md)
- [Connection Details](../Integrations/Zoho_CRM.md)

- [Additional Information](../Integrations/Zoho_CRM.md)

Prerequisites

You must have a Zoho CRM account and create an app which specifies the default Redirect URI provided from the Actian Data Platform. This generates the Client ID and Client Secret to enable you to use OAuth 2.0 authentication.

Connection Details

The Zoho CRM connector authenticates with Zoho using OAuth 2.0 protocols.

For creating connections to Zoho CRM, the Client ID, Client Secret must be obtained from the Zoho CRM app.

To set up credentials, please refer to [https://www.zoho.com/crm/developer/docs/api/v6/oauth-overview.html](https://www.zoho.com/crm/developer/docs/api/v6/oauth-overview.html).

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | A unique string that identifies your application when using OAuth 2.0. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| API version | Specify an API version, for example: v6. |
| API Domain URL | Domain name of the Zoho CRM app. For example:`https://zohoapis.com` |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.**Note:**Currently, we are not regenerating access tokens using this option. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the Zoho API documentation for more info on the API requests and responses. API docs can be found at [https://www.zoho.com/crm/developer/docs/api/](https://www.zoho.com/crm/developer/docs/api/).

The 'Fetch Records for Modules' operation fetches all of the data for a specific module such as Leads, Contacts, etc. The field parameter is mandatory, and it accepts comma-separated values of the field names for which data is to be retrieved. For more details on what values should be specified for this particular endpoint, please refer to this documentation in [https://www.zoho.com/crm/developer/docs/api/v6/get-records.html](https://www.zoho.com/crm/developer/docs/api/v6/get-records.html).
