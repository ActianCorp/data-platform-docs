---
title: "PipeDrive CRM"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "PipeDrive_CRM.htm"
canonical_id: "actian-data-platform-pipedrive-crm"
---

## PipeDrive CRM

The PipeDrive CRM connector allows you to retrieve various data from your PipeDrive Sandbox to the Actian warehouse. PipeDrive is a sales CRM with an intuitive RESTful API. You can use the API to create public or private apps using OAuth 2.0 and integrations via an API token. Public apps and integrations work directly with PipeDrive and are available in PipeDrive’s Marketplace.

- [Prerequisites](../Integrations/PipeDrive_CRM.md)
- [Connection Details](../Integrations/PipeDrive_CRM.md)

- [Additional Information](../Integrations/PipeDrive_CRM.md)

Prerequisites

You must have a Pipedrive account.

PipeDrive CRM uses an API key type authentication, where you need to authenticate the APIs using the API key provided during your account creation. You can get your API token manually from PipeDrive web app. For more information, please visit [https://pipedrive.readme.io/docs/how-to-find-the-api-token](https://pipedrive.readme.io/docs/how-to-find-the-api-token).

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Base URL | The base URL where the PipeDrive sandbox account is hosted. For example:`https://<sandbox.pipedrive.com>/v1` |
| API Token | You can retrieve this token from the PipeDrive Web app. |

Additional Information

Please refer to the PipeDrive API documentation for more info on the API requests and responses. API docs can be found at [https://developers.pipedrive.com/docs/api/v1](https://developers.pipedrive.com/docs/api/v1).
