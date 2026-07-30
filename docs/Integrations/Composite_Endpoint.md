---
title: "Composite Endpoint"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Composite_Endpoint.htm"
canonical_id: "actian-data-platform-composite-endpoint"
---

## Composite Endpoint

Composite endpoints define a number of endpoints that are called in sequence. Outputs from one endpoint can be passed as inputs to subsequent endpoints. This is accomplished by defining output parameters in one endpoint, and input parameters with the same name in a subsequent endpoint.

Example use cases for composite endpoints include:

- Call a logon API to get an authorization token and use that token in a subsequent call
- Call an API to look up the identifier of a particular record, and then perform some operation on that record

### Create a Composite Endpoint

To create a composite endpoint

1. On the Integrations Console, select Design.
2. Select Services (REST/SOAP).

3. On the Services page, click a service against which you want to create a composite endpoint.
An Endpoints list page opens.

4. Click Create Composite Endpoint ![](images/CreateComposite.png).
5. Enter the required General Information in the fields as follows:

    a. Name
The name of the composite endpoint.

    b. Description
A description of the endpoint.

    c. Category
A tag to group together related endpoints.

    d. Connection Test Endpoint
If toggle is enabled, Endpoint will be called to test the connection to the server when the service is deployed as a connector.

6. Click Continue to complete the Endpoint List fields.
7. Select the required endpoints to create a composite endpoint from the Endpoint List fields.

    Up to 4 endpoints can be chained in sequence. Select between 2 and 4 endpoints from the service.

8. Click Validate to ensures that for any input parameter of an endpoint, there is an output parameter from an earlier API call with the same name.
9. Click Save.

    A confirmation message displays: “Endpoint created successfully”.
You are redirected to the Endpoints list page.

### Edit a Composite Endpoint

To edit a composite endpoint

1. On the Integrations Console, select Design.
2. Select Services (REST/SOAP).

3. On the Services page, click a service against which you want to edit a composite endpoint.
An Endpoints List page opens.

4. Select the composite endpoint check box that you want to edit.

    A toolbar opens with an Edit ![](images/EditIcon.png).

5. Click Edit ![](images/EditIcon.png) to modify the composite endpoint.
6. (Optional) Click Information ![](images/Information%20Icon.png) and then click Edit ![](images/Edit.png) to modify the composite endpoint.

7. Click Save.

    A confirmation message displays: “Endpoint updated successfully”.
You are redirected to the Endpoints list page.
