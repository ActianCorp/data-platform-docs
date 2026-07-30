---
title: "eBay Sell"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "eBay_Sell.htm"
canonical_id: "actian-data-platform-ebay-sell"
---

## eBay Sell

The eBay Sell connector uses the eBay Sell API to manage user and customer data in your eBay application

- [Prerequisites](../Integrations/eBay_Sell.md)
- [Connection Details](../Integrations/eBay_Sell.md)

- [Additional Information](../Integrations/eBay_Sell.md)

Prerequisites

You must have an eBay developer account. You must generate the application key sets.

Connection Details

The connector authenticates with Ebay using OAuth2.0. To set up the credentials, see [https://developer.ebay.com/api-docs/static/authorization_guide_landing.html](https://developer.ebay.com/api-docs/static/authorization_guide_landing.html).

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID/Secret | Part of your OAuth credentials provided by eBay under Application Keys. |
| Base URL | The eBay API URL environment endpoint URL. For example:Sandbox: https://api.sandbox.ebay.comProduction: https://api.ebay.com |
| Scope | The request you use to generate the new token must include a scope that allows access to all the methods you plan to call with the token. |
| Access Token URL | The Access Token URL is taken from the refresh token request section. This URL generates the access token using the refresh token.The Access Token URL:Sandbox: https://api.sandbox.ebay.com/identity/v1/oauth2/token Production: https://api.ebay.com/identity/v1/oauth2/token |
| Authorization URL | The Authorization URL can be taken from your eBay Sign-in Settings:Sandbox: https://api.sandbox.ebay.com/identity/v1/oauth2/token Production: https://api.ebay.com/identity/v1/oauth2/token |

Additional Information

Please refer to the Ebay Sell API documentation for more information on the API requests and responses. API docs can be found at [https://edp.ebay.com/develop/selling-apps](https://edp.ebay.com/develop/selling-apps).
