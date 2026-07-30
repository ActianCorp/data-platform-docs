---
title: "Create Connections"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Create_Connections.htm"
canonical_id: "actian-data-platform-create-connections"
---

## Create Connections

When creating a connection, users must select a connector then provide the details needed to connect (credentials, tokens, URLs, and so on).

Once a connection has been created, it can be referenced or reused within any new Integration. A saved connection helps to speed up development, and eliminates redundant manual entry of credentials when creating Integrations.

You can create connections from the following two places:

- When defining source for a new integration. See [Creating Integrations](../Integrations/Creating_Integrations.md).
- From Integrations, Connections, Create Connection.

Creating a connection consists of the following high level design steps:

1. Describe – Name your connection.
2. Choose Connection Type – Choose connection type.

3. Define Properties – Specify connection properties.

Navigation between pages of the guided workflow is possible by using the Back and Continue buttons at the bottom of the page. Navigating between pages will not clear data that has been entered by the user. When navigation to other pages is not possible, the button will fade in color and will not be active. You can exit the process anytime without saving any information by clicking Cancel.

To create a new connection

1. Click Integrations, Connections, and then click Create Connection.

    The Create **Connection**page is displayed. It is a guided workflow that lets you create a connection by specifying the connection details which you can use as source and target connections when creating an integration.

**IMPORTANT!**Creating an Actian Warehouse connection is not supported. However, you can use Actian Warehouse as a source and target connector when creating an integration and configure the connection information. See [Creating Integrations](../Integrations/Creating_Integrations.md).

2. Provide a name for the connection in the Name field, then click Continue. The Description field is optional.

!!! note "Note"

    A connection name must be unique. The size of the name should be <= 255 chars.

3. To connect via agent, enable Connect via Agent (the Connection Types list displays connectors that support connections via agent).

    If not, disable Connect via Agent.

!!! note "Note"

    Connecting via agent is useful when the data source is located behind a firewall on premise.

4. Choose a connection type and click Continue. See [Source and Target Connections](../Integrations/Source_and_Target_Connections.md).

!!! note "Note"

    Services which are user-defined connection types may also be listed as connection types. See [Services (REST/SOAP)](../Integrations/Services_(REST_2fSOAP).md).

5. Depending on the connection type selection, you will be required to specify some connection properties. See [Source and Target Connections](../Integrations/Source_and_Target_Connections.md).
6. After specifying connection properties, click Test to test your connection.

7. After a successful test, click Save.

    A success message is displayed and the new connection information is added to the Connections page.

8. Enter your connection name, in the search box on the Connections page, and ensure that the connection that you just created is listed here.

    You can use this connection information, when creating an integration. See [Creating Integrations](../Integrations/Creating_Integrations.md).
