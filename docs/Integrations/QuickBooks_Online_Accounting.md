---
title: "QuickBooks Online Accounting"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "QuickBooks_Online_Accounting.htm"
canonical_id: "actian-data-platform-quickbooks-online-accounting"
---

## QuickBooks Online Accounting

The QuickBooks Online Accounting connector reads the details related to accounting, bill payment, company info and reconciliation reports on expense management, budgeting, payment processing, and tax rate.

- [Prerequisites](../Integrations/QuickBooks_Online_Accounting.md)
- [Connection Details](../Integrations/QuickBooks_Online_Accounting.md)

- [Additional Information](../Integrations/QuickBooks_Online_Accounting.md)

Prerequisites

You must have a QuickBooks Online Accounting account.

You must create an app and specify the default Redirect URI provided from the Actian Data Platform to generate the Client ID and Client Secret, to use the OAuth 2.0 authentication.

Connection Details

The QuickBooks Online Accounting connector authenticates with QuickBooks Online Accounting app using OAuth 2.0. authentication.

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | A unique string that identifies your application when using OAuth 2.0. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| Base URL | The base URL where the QuickBooks API is hosted. For example:`https://quickbooks.api.intuit.com/` |
| Company ID | The ID that identifies a QuickBooks Online Accounting company. This can also be the realm ID. |
| Minor Version | Queries when to access a specific API version.**Note:**Refer to the documentation to reference Minor Version and Company ID, at https://quickbooks.intuit.com/learn-support/en-us/help-article/customer-company-settings/find-quickbooks-online-company-id/L7lp8O9yU_US_en_US. |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the QuickBooks Online Accounting API documentation for more info on the API requests and responses. API docs can be found at [https://developer.intuit.com/docs/api/accounting](https://developer.intuit.com/docs/api/accounting).
