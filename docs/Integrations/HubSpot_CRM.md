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
| Scope | •Specifies the required multiple values to call the endpoints. The default scopes given for the connector:•oauth crm.schemas.quotes.read•crm.objects.line_items.read•crm.schemas.deals.read•crm.objects.carts.read•crm.schemas.line_items.read•crm.pipelines.orders.read•crm.objects.subscriptions.read•crm.schemas.subscriptions.read•crm.schemas.orders.read•crm.schemas.commercepayments.read•crm.objects.owners.read•crm.objects.commercepayments.read•crm.objects.orders.read•crm.objects.invoices.read•crm.schemas.invoices.read•crm.objects.leads.read•crm.objects.users.read•crm.objects.marketing_events.read•crm.schemas.custom.read•crm.objects.custom.read•crm.objects.feedback_submissions.read•crm.objects.goals.read•crm.objects.companies.read•crm.lists.read crm.objects.deals.read•crm.schemas.contacts.read•crm.objects.contacts.read•crm.schemas.companies.read•crm.objects.quotes.read•crm.schemas.carts.read•e-commerce•tickets |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.This is an optional field. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the Hubspot CRM API documentation for more info on the API requests and responses. API docs can be found at [https://developers.hubspot.com/docs/api/overview](https://developers.hubspot.com/docs/api/overview).
