---
title: "HubSpot CRM"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "HubSpot_CRM.htm"
canonical_id: "actian-data-platform-hubspot-crm"
---

## HubSpot CRM

The Hubspot CRM Connector is a Rest API connector which can retrieve the data of each of the objects and create specific tables in Actian warehouse.

- [Prerequisites](../Integrations/HubSpot_CRM.md)
- [Connection Details](../Integrations/HubSpot_CRM.md)

- [Additional Information](../Integrations/HubSpot_CRM.md)

Prerequisites

You must have a Hubspot CRM account.

You must create a public app in your Hubspot CRM account with the default Redirect URI provided from Actian to generate the Client ID and Client Secret, to use OAuth 2.0.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | The Client ID is the public identifier for your Hubspot CRM app. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| API version | API version for your request.Format: v3 |
| Scope | • Specifies the required multiple values to call the endpoints. The default scopes given for the connector:<br>• oauth crm.schemas.quotes.read<br>• crm.objects.line_items.read<br>• crm.schemas.deals.read<br>• crm.objects.carts.read<br>• crm.schemas.line_items.read<br>• crm.pipelines.orders.read<br>• crm.objects.subscriptions.read<br>• crm.schemas.subscriptions.read<br>• crm.schemas.orders.read<br>• crm.schemas.commercepayments.read<br>• crm.objects.owners.read<br>• crm.objects.commercepayments.read<br>• crm.objects.orders.read<br>• crm.objects.invoices.read<br>• crm.schemas.invoices.read<br>• crm.objects.leads.read<br>• crm.objects.users.read<br>• crm.objects.marketing_events.read<br>• crm.schemas.custom.read<br>• crm.objects.custom.read<br>• crm.objects.feedback_submissions.read<br>• crm.objects.goals.read<br>• crm.objects.companies.read<br>• crm.lists.read crm.objects.deals.read<br>• crm.schemas.contacts.read<br>• crm.objects.contacts.read<br>• crm.schemas.companies.read<br>• crm.objects.quotes.read<br>• crm.schemas.carts.read<br>• e-commerce<br>• tickets |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.This is an optional field. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the Hubspot CRM API documentation for more info on the API requests and responses. API docs can be found at [https://developers.hubspot.com/docs/api/overview](https://developers.hubspot.com/docs/api/overview).
