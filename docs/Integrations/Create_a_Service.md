---
title: "Create a Service"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Create_a_Service.htm"
canonical_id: "actian-data-platform-create-a-service"
---

## Create a Service

To create a new service

1. On the Integrations Console, select Design.
2. Select Services (REST/SOAP).

3. Click Create Service to define a new service.
The Create Service page is opened.

4. Enter the required Service Information in the fields as follows:

    a. Service Name

    b. Description

    c. Base URL

    d. Proxy URL

    e. ![](images/AddIcon.png)
You can upload .svg file to the service. This icon is displayed in the Connections page when connections to this service are created.

5. Click Continue to complete the Authentication.
6. Define the authentication type as one of the following:
Go to [Authentication](../Integrations/Create_a_Service.md), for more details.

    a. None

    b. Basic

    c. Bearer Token

    d. OAuth 2.0

    e. Call Authentication Endpoint

7. Click Continue to configure the Retry Strategy.
8. Enter the specific information for the Retry Strategy properties as follows:
Go to [Retry Strategy](../Integrations/Create_a_Service.md), for more details.

    a. Number of Retries

    b. Initial Delay (ms)

    c. Delay Multiplier.

9. Click Continue to define the parameters.
Parameters can be specified in any field, such as the Base URL. Parameters should be specified in the form "{$parameter-name}". If a parameter reference is entered into any field in this form, it will automatically be added to the parameters table.

10. Click Add a row ![](images/AddARow.png) to add the fields as follows:

    a. Name

    b. Description

    c. Value

    d. Label

    e. Type

    f. Required

11. Click Save.
A confirmation message displays: "Service created successfully".
You are redirected to the Services list page.

### Authentication

There are five options to authenticate a service.

- None
The endpoint does not require any authentication.

- Basic
The endpoint requires username and password for authentication.

- Bearer Token
For Bearer type authentication, enter the bearer token. You will get the bearer token from your service provider.

- OAuth 2.0
The endpoint requires an access token to access the services securely by using OAuth 2.0 Authentication.

- Call Authentication Endpoint
Select the endpoint to call to authenticate the user.

#### OAuth 2. 0 authentication properties

Access Token Action: Whether to generate a new token or use an existing one.

Select a relevant option from below fields:

- Use Existing Access Token: This action allows you to use the existing token. Refer to the below table:

| Options | Description |
| --- | --- |
| Access Token Expiry Action | Action to be taken if the access token is expired. The available options are:<br>• Do not refresh<br>• Refresh with client credentials<br>• Refresh with password credentials |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Access Token URL | The endpoint which is called to generate an access token in exchange of the authentication code. |
| Client ID | This is sometimes referred to as the consumer key. |
| Client Secret | This is sometimes referred to as the consumer secret. |
| Client Authentication | Specifies whether the client credentials are passed to the authorization API in the body or as a basic authentication header. |
| Username | User name for authentication. |
| Password | Password for authentication. |
| Security Token | This token is provided by the Service provider. If not provided, it is already appended to the password. This is an optional field. |

- Generate Access Token Now: This action allows you to generate the new token. Refer to the below table:

| Options | Description |
| --- | --- |
| Grant Type | Refers to the way an application gets an access token. The available options are:<br>• Authentication Code<br>• Authentication Code with PKCE<br>• Client Credentials<br>• Password Credentials |
| Access Token URL | The endpoint which is called to generate an access token in exchange of the authentication code. |
| Client ID | This is sometimes referred to as the consumer key. |
| Client Secret | This is sometimes referred to as the consumer secret. |
| Client Authentication | Specifies whether the client credentials are passed to the authorization API in the body or as a basic authentication header. |
| Redirect URL | Configure the application to include the given redirected URL:{server}/v1/integ/services/oauth2/actions/generate-tokens |
| Authentication URL | This endpoint is called to generate the authentication code. |
| Scope | Specifies the multiple values with the spaces between them. |
| Resource | A URL that indicates resource/target services where the token is intended to be used. |
| Audience | A URL that indicates target audiences/services where the token is intended to be used. |
| Code Challenge Method | This is an algorithm used for code challenge. |
| Authorize button | Click to generate the access token. |
| Get Tokens button | Calls the server which in return calls the Access Token URL to get the access token and may request a token. |
| Username | User name for authentication. |
| Password | Password for authentication. |
| Access Token | Specifies security token which grants access to the given REST endpoint in OAuth 2.0 |
| Refresh Token | This is used to get new access token. This is an optional field. |

- Generate Access Token at Runtime: This action allows you to generate the new token at runtime. Refer to the below table:

| Options | Description |
| --- | --- |
| Grant Type | Refers to the way an application gets an access token. The available options are:<br>• Client Credentials<br>• Password Credentials |
| Access Token URL | The endpoint which is called to generate an access token in exchange of the authentication code. |
| Client ID | This is sometimes referred to as the consumer key. |
| Client Secret | This is sometimes referred to as the consumer secret. |
| Client Authentication | Specifies whether the client credentials are passed to the authorization API in the body or as a basic authentication header. |
| Scope | Specifies the multiple values with the spaces between them. |
| Audience | A URL that indicates target audiences/services where the token is intended to be used. |
| Resource | A URL that indicates resource/target services where the token is intended to be used. |
| Username | User name for authentication. |
| Password | Password for authentication. |

### Retry Strategy

The primary purpose of defining retry parameters is when an API is rate-limited, whereby the API only permits a certain number of calls to be made in a given time period.

Retry is controlled by these parameters:

- Number of retries
The maximum number of times that an API is called if it returns a failure status.

- Initial delay
The initial time interval that the process waits before retrying the API call.

- Delay multiplier
A decimal value that is multiplied by the delay value to extend the delay after each failing call. By default, this is set to 1.0, which means that the delay between each call is the same.
