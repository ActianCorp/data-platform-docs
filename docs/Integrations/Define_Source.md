---
title: "Define Source"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Define_Source.htm"
canonical_id: "actian-data-platform-define-source"
---

## Define Source

The Define Source page specifies which source file, table, or object to read from within the integration. On this page you can select from a number of different connectors, then configure and test the connection and view the data.

To define a source connection

1. Click Select Source to view and pick a source from your recent source selection list or click Browse Sources and select from the available source options.

    All available connections for the selected source are listed in the Choose Source Connections drop-down.

2. To connect via agent, enable Connect via Agent (connectors that support connections via agent are displayed).

    If not, disable Connect via Agent.

!!! note "Note"

    Connecting via agent is useful when the data source is located behind a firewall on premise.

3. Choose from the Choose Source Connections list or click Create Connection to create a new one. See [Create Connections](../Integrations/Create_Connections.md).

!!! note "Note"

    If you select an Actian Warehouse as the source, the Create Connection button is not displayed, as you do not need a connection to connect to Actian Warehouse. You can connect directly, but you must remember that the warehouse must be running in order to connect to it while designing or executing an integration.

4. Depending on the source selection, you will be required to specify some connection properties. See [Source and Target Connections](../Integrations/Source_and_Target_Connections.md).
5. Select the desired file, table or object.

    A representation of the schema for the selected dataset will appear on the Mapping page, displaying the field names, data types, and field sizes.

6. Click the Preview the first 20 records link.

    The data for the selected source table is displayed in the Source Data Preview pane. Review your data set. You can perform the following actions on the Source Data Preview pane:

| Options | Description |
| --- | --- |
| ![](images/DesignWorkspace_2.png) | Click the down arrow and select how many records to display on the page. |
| ![](images/DesignWorkspace_3.png) | Use these options to Navigate from one page to another. |
| ![](images/DesignWorkspace_4.png) | Click this icon to search for a particular value in the data set. Contents will be filtered based on the search string.Click ![](images/DesignWorkspace_5.png) to close the search box. |

7. Click Continue.

    The Define Target page is displayed. See [Define Target](../Integrations/Define_Target.md).
