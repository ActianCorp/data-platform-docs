---
title: "Create an Endpoint"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Create_an_Endpoint.htm"
canonical_id: "actian-data-platform-create-an-endpoint"
---

## Create an Endpoint

To create an endpoint

1. On the Integrations Console, select Design.
2. Select Services (REST/SOAP).

3. On the Services page, click a service against which you want to create an endpoint.
An Endpoints list page opens.

4. Click Create Endpoint ![](images/CreateEndpoint.png).
5. Enter the required General Information in the fields as follows:

    a. Name

    b. Description

    c. Category
A tag to group together related endpoints.

    d. Connection Test Endpoint toggle
If this is enabled, the endpoint will be called to test the connection to the server when a connection is configured using this connection.

6. Click Continue to complete the Authentication.
7. Define the authentication type as one of the following:

    a. Use Service Definition
Use the authentication mechanism defined in the service.

    b. None
The endpoint does not require any authentication.

    c. Basic
The endpoint requires username and password for authentication.

    d. Bearer Token
For Bearer type authentication, enter the bearer token. You will get the bearer token from your service provider.

!!! note "Note"

    The authentication definition for an endpoint is typically defined at the service level, but for a specific endpoint can be overridden to use a different authentication mechanism.

8. Click Continue to fill the Request step details which includes the fields as follows:
Go to [Request](../Integrations/Create_an_Endpoint.md), for more details.

    a. Service URL

    b. Relative URL

    c. Method

    d. Query parameters

    e. Headers

    f. Parameters

    g. Pagination Type

9. Click Call API to invoke the API using the details specified on the request page or click Continue to move to Success Response.
10. The Success Response page is populated if the API call was successful. The page shows the following information:

    Go to [Success and Error Response](../Integrations/Create_an_Endpoint.md), for more details.

    a. Status

    b. Content Type

    c. Response Body

    d. Output Parameters

11. Click Continue and the Error Response page is populated if the API call was unsuccessful. The page shows the following information.

    a. Status

    a. Content Type

    a. Response Body

    a. Output Parameters

12. Click Save.

    A confirmation message displays: "Endpoint created successfully".
You are redirected to the Endpoints list page.

### Request

Defines an endpoint of the API call.

The request definition contains the following:

- Service URL
A URL defined in the service to which the Relative URL is appended.

- Relative URL
The value specified for the relative URL is appended to the URL defined in the parent service. Alternatively, an absolute path (beginning with http: or https:) can also be specified in which case the service's URL will be ignored.

- Method
This is an HTTP verb. Select one of the methods from below:

    - –GET

    - –POST

    - –PUT

    - –DELETE

    - –PATCH

    - –HEAD

    - –OPTIONS

- Query Parameters
URL parameters to pass the API. The value can either be set to a literal value or to a request parameter value, specified as "{$param-name}".

    Click Add a row ![](images/DesignWorkspace_120.png) to add a Parameter and its Value.

- Headers
The HTTP headers to set in the request. The value can either be set to a literal value or to a request parameter value, specified as "{$param-name}".

    Click Add a row ![](images/AddARow.png) to add a Header and its Value.

- Parameters
The parameters can be used in the URL, headers, or query parameters, specifying the parameter name as "{$param-name}".

    Click Add a row ![](images/DesignWorkspace_121.png) to add the fields as follows:

    - –Name

    - –Description

    - –Value

    - –Label

    - –Type: String/Integer/Boolean/Datetime/Masked

    - –Required toggle

- Pagination Type
This specifies a type of pagination. Select one of the pagination types as follows:

    - –None
Pagination is not enabled.

    - –Offset
For the properties, refer to the following table:

| Property | Description |
| --- | --- |
| Records per Call | The number of records to fetch per call. |
| Limit | The total number of records to return across all calls. |
| First Offset | The offset value to provide in the first call. |
| End of Data Indicator | This property specifies how the REST service reports that the page is the final page. This property has the following possible values:<br>• Number of Records - A field in the response, or in a header value, provides the total number of records being returned.<br>• Is Last - A boolean field in the response, or in a header value, specifies that the current page is the last page.<br>• Has More - A boolean field in the response, or in a header value, specifies that the current page is not the last page.<br>• No Indicator - Nothing in the data indicates that a page is the last page. Instead, an empty or missing array implies there is no more data. |
| End of Data Location | Location in response as where to find the total number of records. Select end of data location from below:<br>• Header<br>• Body |
| Number of Records Path | Header name or the path for which the total number of records are found. This property is applicable only when the Pagination Type is set to Offset and End of Data Indicator is set to Number of Records.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Is Last Path | Header name or the path where the is last indicator is found. This is a boolean field or header that has the value of true to indicate that the last page has been reachedSee [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Has More Path | Header name or the path where the has more indicator is found. This is a boolean field or header that has the value of true to indicate that there are more pages to be fetched.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Records Path | This property provides the path where the array of records is found in the data. If the path does not exist, or contains an empty array, this signals that there is no more data.This property is applicable when the End of Data Indicator is set to No Indicator.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |

    - –Page
For the properties, refer to the below table:

| Property | Description |
| --- | --- |
| Records per Call | The number of records to fetch per call. |
| First Page | The page value to provide in the first call. |
| Number of Pages Location | Location where to find total number of pages. Select number of pages location from below:<br>• Header<br>• Body |
| End of Data Indicator | This property specifies how the REST service reports that the page is the final page. This property has the following possible values:<br>• Number of Pages - A field in the response, or in a header value, provides the total number of pages being returned.<br>• Is Last - A boolean field in the response, or in a header value, specifies that the current page is the last page.<br>• Has More - A boolean field in the response, or in a header value, specifies that the current page is not the last page.<br>• No Indicator - Nothing in the data indicates that a page is the last page. Instead, an empty or missing array implies there is no more data. |
| Number of Pages Path | Header name or the path for which the URL for the next page is found. This property is applicable only when the Pagination Type is set to Page and End of Data Indicator is set to Number of Pages.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Is Last Path | Header name or the path where the is last indicator is found. This is a boolean field or header that has the value of true to indicate that the last page has been reached.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Has More Path | Header name or the path where the has more indicator is found. This is a boolean field or header that has the value of true to indicate that there are more pages to be fetched.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Records Path | This property provides the path where the array of records is found in the data. If the path does not exist, or contains an empty array, this signals that there is no more data.This property is applicable when the End of Data Indicator is set to No Indicator.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |

    - –Next Page Link
For the properties, refer to the below table:

| Property | Description |
| --- | --- |
| Next Page Link Location | The name of the header or the path in the body for the field containing the URL for the next page. Select the next page link location from below:<br>• Header<br>• Body |
| Next Page Link Path | Header name or the path for which the URL for the next page is found.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |

    - –Next Page Token
For the properties, refer to the below table:

| Property | Description |
| --- | --- |
| Next Token Location | The name of the header or the path in the body for the field containing the token for the next page. Select the next token location from below:<br>• Header<br>• Body |
| Next Token Path | Header name or the path for which the token for the next page is found.See [JSON Paths](../Integrations/Create_an_Endpoint.md) to specify path. |
| Pagination Token Location | Location where the pagination token for subsequent calls would be configured. Select the pagination token location from below:<br>• Parameter<br>• Header |
| Pagination Token name | Name of the pagination token to be passed in the next subsequent calls. |

JSON Paths

    Properties that use JSON paths are as follows:

    - Number of Records Path

    - Number of Pages Path

    - Is Last Path

    - Has More Path

    - Next Page Link Path

    - Next Page Token Path

    The syntax for specifying paths for fields in JSON responses follows the JSON Path specification. You can specify the path for the properties as follows:

```
/key1/key2
```

    For example, given this JSON response:

```
{
```

```
   "token1": "111",
```

```
   "object1": { "token2": "222" },
```

```
   "array1": [ { "token3": "222" } ]
```

```
}
```

    The paths for the three tokens are:

    - –Token1: /token1

    - –Token2: /object1/token2

    - –Token3: /array1/0/token3

!!! note "Note"

    Note: For arrays, the integral value for the index is specified, where the first element in the array has an index of 0. To access the last element of an array, specify the index with the special value -1.

Pagination Special Values

In paginated API calls, the pagination parameters are provided either as query parameters, or (less commonly) as request header values. Since these values change with each call to the API, a mechanism is provided to specify these varying parameters.

This is provided by special properties that have the syntax {{…}}. These special values are as follows:

| Value | Description |
| --- | --- |
| {{record_count}} | The value of the Records per Call property. |
| {{offset}} | The next offset value. On each call this will be incremented by the value of the Records per Call property. |
| {{page}} | The next page number. On each call this will be incremented. |
| {{pagination_token}} | The pagination token from the prior call. On the first call, the query parameter or header will not be set. On subsequent calls, it will be set to the value of the pagination token from the previous call. |

- Call API
When the API is called, its response then populates the response body field of either the success or error response, based on the HTTP status returned by the API call.

### Success and Error Response

Properties for success and error responses are as follows:

- Status
The HTTP status code of the response.

- Content type
The content type of the response data.

- Response body
A response body for a successful/error response.

- Output parameters
Output parameters are used in composite endpoints, to pass response values from one API to inputs of a subsequent API. The location allows for extracting parameters from response headers or from the response body. Paths are specified using dot notation, e.g. "address.city", "error.message"
Click Add a row ![](images/AddARow.png) to add the Name, Location, and Path.
