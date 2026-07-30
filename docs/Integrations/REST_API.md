---
title: "REST API"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "REST_API.htm"
canonical_id: "actian-data-platform-rest-api"
---

## REST API

The Representational State Transfer (REST) connector enables you to access REST APIs or HTTP requests on remote web services.

- [Prerequisites](../Integrations/REST_API.md)
- [Source Details](../Integrations/REST_API.md)

- [Additional Information](../Integrations/REST_API.md)

Prerequisites

None

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| URL | Specifies the REST URL endpoint. This is a mandatory property. |
| Proxy URL | (Optional) Specify the URL to connect to a proxy server. |
| Method | Specifies the HTTP method. This is a mandatory property. Options available in Method are as follows:•GET•HEAD•PUT•POST•PATCH•DELETE |
| Authentication | (Optional) Specifies the options to authenticate a connection. There are the following options:•None: This option does not require any authentication.•Basic: This option requires username and password for authentication.•OAuth 2.0: This option requires an access token to access the REST APIs securely by using OAuth 2.0 Authentication. |
| Username | Specifies the username for the REST connection authentication. This is a mandatory property. This property is enabled when Authentication Type is selected to Basic authentication method. |
| Password | Specifies the password for the REST connection authentication. This is a mandatory property. This property is enabled when Authentication Type is selected to Basic authentication method. |
| Access Token Action | Specifies the security token with grants access to given REST endpoint. This is a mandatory property. This property is enabled when Authentication Type is selected to OAuth 2.0 authentication method. There are two supported values:•Use Existing Access Token (default)•Generate Access Token Runtime: The following properties must be configured:–Grant Type: Specifies the grant type for an application to gets an access token. This is a mandatory property. There are two supported values:•Client Credentials (default): The following properties must be configured:–Scope: Specifies the scope of the request and multiple values with spaces between them.–Resource: Specifies an URI that indicates resource/target services where the token is intended to be used.–Audience: Specifies an URI that indicates resource/target services where the token is intended to be used.–Access Token URL: Specifies the endpoint URL for authentication server. This is a mandatory property.–Consumer Key: Specifies the consumer key to identify the consumer to the service provider. This is a mandatory property.–Consumer Secret: Specifies the consumer secret which is used to establish the ownership of the consumer key. This is a mandatory property. |
|  | •Password Credentials: The following properties must be configured:–Scope: Specifies the scope of the request and multiple values with spaces between them.–Audience: Specifies an URI that indicates resource/target services where the token is intended to be used.–Access Token URL: Specifies the endpoint URL for authentication server. This is a mandatory property.–Username: Specifies the username for the REST connection authentication. This is a mandatory property.–Password: Specifies the password for the REST connection authentication. This is a mandatory property.–Consumer Key: Specifies the consumer key to identify the consumer to the service provider. This is a mandatory property.–Consumer Secret: Specifies the consumer secret which is used to establish the ownership of the consumer key. This is a mandatory property. |
| Access Token Expiry Action | Specifies the action to be taken if the access token is expired. This is a mandatory property. This property is enabled when Authentication Type is selected to OAuth 2.0 authentication method. There are three supported values which are enabled when Access Token Action property field is selected to Use Existing Access Token(default):•Do Not Refresh(default)•Refresh With Password Credentials: The following properties must be configured:–Access Token URL: Specifies the endpoint URL for authentication server. This is a mandatory property.–Username: Specifies the username for the REST connection authentication. This is a mandatory property.–Password: Specifies the password for the REST connection authentication. This is a mandatory property.–Consumer Key: Specifies the consumer key to identify the consumer to the service provider. This is a mandatory property.–Consumer Secret: Specifies the consumer secret which is used to establish the ownership of the consumer key. This is a mandatory property.–Security Token: (Optional) Specifies the security token that is provided to you when you register. If not provided, it is assumed to be already appended to password.•Refresh With Client Credentials: The following properties must be configured:–Access Token URL: Specifies the endpoint URL for authentication server. This is a mandatory property.–Consumer Key: Specifies the consumer key to identify the consumer to the service provider. This is a mandatory property.–Consumer Secret: Specifies the consumer secret which is used to establish the ownership of the consumer key. This is a mandatory property. |
| Access Token | Specifies the security token with grants access to given REST endpoint. This is a mandatory property. This property is enabled when Authentication Type is selected to OAuth 2.0 authentication method. |
| Headers | (Optional) Specifies the header. List of HTTP request headers in the format:key=value key=value ... key=value |
| Select Source Tables | (Optional) Select which arrays of objects in the JSON data you wish to map to tables in the target. |

Additional Information

None
