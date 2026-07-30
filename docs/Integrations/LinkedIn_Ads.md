---
title: "LinkedIn Ads"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "LinkedIn_Ads.htm"
canonical_id: "actian-data-platform-linkedin-ads"
---

## LinkedIn Ads

The LinkedIn Ads connector is a Rest-based connector for Linkedin Ads which allows user to fetch all info from the Linkedin Ads account. You can retrieve data of DMP Segments/Audiences, Campaigns information along with other various entities of their Linkedin Ads account.

- [Prerequisites](../Integrations/LinkedIn_Ads.md)
- [Connection Details](../Integrations/LinkedIn_Ads.md)

- [Additional Information](../Integrations/LinkedIn_Ads.md)

Prerequisites

You must have a LinkedIn Ads account.

The connector authenticates with Linkedin Ads using OAuth2.0. For more information, please visit [Authorization documentation](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?toc=%2Flinkedin%2Fmarketing%2Ftoc.json&bc=%2Flinkedin%2Fbreadcrumb%2Ftoc.json&view=li-lms-2024-06&tabs=HTTPS1).

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Base URL | The LinkedIn API base URL:`https://api.linkedin.com/rest` |
| LinkedIn API version | Latest API version, for example: 202402.**Note:**To reference API versioning, please see  [https://learn.microsoft.com/en-us/linkedin/marketing/versioning?view=li-lms-2024-06](https://learn.microsoft.com/en-us/linkedin/marketing/versioning?view=li-lms-2024-06) |
| Client ID | The Client ID is the public identifier for your LinkedIn Ads app. |
| Client Secret | The Client Secret is the secret known only to the application and the authorization server. |
| Access Token URL | The URL to generate the access token:`https://www.linkedin.com/oauth/v2/accessToken.` |
| Redirect URL | Configure the application to include the Redirected URL. The Redirect URL can be found on the screen while creating the connection. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get a new access token.**Note:**Currently, we are not regenerating access tokens using this option. |
| Authorize button | Click to generate the access token. |

Additional Information

When using the search operation in Linkedin Ads. a proper search query is required. To specify a proper search query, please refer to the Linkedin API documentation:

[https://learn.microsoft.com/en-us/linkedin/marketing/overview?view=li-lms-2024-06](https://learn.microsoft.com/en-us/linkedin/marketing/overview?view=li-lms-2024-06 )

!!! note "Note"

    Change the date in the view query to the latest month and year to go to the latest version of the document.
