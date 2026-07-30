---
title: "Facebook Ads"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Facebook_Ads.htm"
canonical_id: "actian-data-platform-facebook-ads"
---

## Facebook Ads

The Facebook Ads connector is a Rest API connector you can use with the Facebook Ads Application. You can retrieve the data of each of the objects and create specific tables in an Actian warehouse.

- [Prerequisites](../Integrations/Facebook_Ads.md)
- [Connection Details](../Integrations/Facebook_Ads.md)

- [Additional Information](../Integrations/Facebook_Ads.md)

Prerequisites

You must have a Facebook Ads account.

Create an app in Facebook Ads account with the default Redirect URI provided from Actian to generate the Client ID and Client Secret for authentication.

Specify these permissions for the App: ads_management, business_management, and public_profile

Connection Details

The Facebook Ads connector authenticates using OAUTH 2.0. For more information, please see [https://developers.facebook.com/docs/marketing-apis/overview/authentication](https://developers.facebook.com/docs/marketing-apis/overview/authentication).

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Business ID | Your business ID is the unique number that corresponds to your business portfolio. |
| Client ID | The Client ID is the public identifier for your Facebook Ads app. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| API Version | Specify the version in this format: v19.0 |

Additional Information

Please refer to the Facebook Ads API documentation for more info on the API request and response: [https://developers.facebook.com/docs/marketing-api/reference/](https://developers.facebook.com/docs/marketing-api/reference/).
