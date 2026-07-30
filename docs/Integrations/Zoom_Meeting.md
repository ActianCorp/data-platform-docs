---
title: "Zoom Meeting"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Zoom_Meeting.htm"
canonical_id: "actian-data-platform-zoom-meeting"
---

## Zoom Meeting

The Zoom Meeting connector accesses past and present meeting and webinar details, device details, recordings and reconciliation reports on meetings, and webinars.

- [Prerequisites](../Integrations/Zoom_Meeting.md)
- [Connection Details](../Integrations/Zoom_Meeting.md)

- [Additional Information](../Integrations/Zoom_Meeting.md)

Prerequisites

You must have a Zoom User or Admin account.

Create a user level app or admin level app with the default Redirect URI provide from Actian to generate the Client ID and Client Secret, to avail the OAuth 2.0 Auth Code Authentication in zoom marketplace

Connection Details

The connector authenticates with the Zoom Meeting app using OAuth2.0.

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Client ID | A unique string that identifies your application when using OAuth 2.0. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| Scope | Scope allows an app to view the meeting information for all the users in the Zoom account. This includes meeting reports, participants, polls, and registrants. |
| Meeting ID | An up to 10-digit long format integer (not integer), for example: 1234567890 |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.**Note:**Currently, we are not regenerating access tokens using this option. |
| Authorize button | Click to generate the access token. |

Additional Information

Please refer to the Zoom Meeting API documentation for more info on the API requests and responses. API docs can be found at [https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#overview](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#overview).
