---
title: "Creating a Connection"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Creating_a_Connection.htm"
canonical_id: "actian-data-platform-creating-a-connection"
---

## Creating a Connection

!!! note "Note"

    Before reading this topic, ensure that you have read [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).

You can use a saved connection or create a new connection while on the source page of the profile editor. Once a connection has been created, it can be referenced or reused within any new profile. A saved connection helps to speed up development, and eliminates redundant manual entry of credentials when creating profiles.

Connections can be created using Data Profiler or Integrations. Each tool supports a different set of connections. You can create connections:

- When defining source for a new profile.
- From Integrations, Connections, Create Connection.

Creating a connection consists of the following high level design steps:

1. Describe – Name your connection.
2. Define Properties – Specify connection properties.

Navigation between pages of the guided workflow is possible by using the Back and Continue buttons at the bottom of the page. Navigating between pages will not clear data that has been entered by the user. When navigation to other pages is not possible, the button will fade in color and will not be active. You can exit the process anytime without saving any information by clicking Cancel.

To create a new connection

1. Click Create Connection.

    The Create New **Connection**page is displayed. It is a guided workflow that lets you create a connection by specifying the connection properties for the selected Data Source.

**IMPORTANT!**Creating an Actian Warehouse connection is not supported, but you can use them as a source and target connector and configure the connection information, when creating a profile. See [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).

2. Provide a name for the connection in the Name field, then click Continue. The Description field is optional.

!!! note "Note"

    A connection name must be unique. The size of the name should be <= 255 chars.

3. Depending on the Data Source selection, you will be required to specify some connection properties. Refer to the Source Detailssection for the connector of interest in [Source and Target Connections](../DataQuality/Source_and_Target_Connections.md).
4. After specifying connection properties, click Test to test your connection.

5. After a successful test, click Save.

    A success message is displayed and the new connection information is added to the Connections page.

6. Enter your connection name, in the search box on the Connections page, and ensure that the connection that you just created is displayed here.

    You can use this connection information, when creating a profile. See [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).
