---
title: "Define Source"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Define_Source.htm"
canonical_id: "actian-data-platform-define-source"
---

## Define Source

!!! note "Note"

    Before reading this topic, ensure that you have read [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).

On the Source page, specify the source connection type, the connection, and the file or table you intend to profile. You can establish a new connection, or utilize an existing one. After selecting the source file or table you can preview the data to verify that you selected the correct data source.

Depending on the source connection type you select, you may be required to specify some connection properties. These instructions guide you to the information needed.

To define a source connection

1. Click Select Source and choose a connection type from your recent source selection list, or click Browse Sources to select from the Data Source Catalog.
2. If you selected Actian Warehouse as the connection type refer to [Source Details for Actian Warehouse](../DataQuality/Actian_Warehouse.md). Otherwise, proceed to next Step.

3. All available connections for the selected connection type are listed in the Connection drop-down. Do one of the following:

    - Choose a connection from the Connection drop-down list, then proceed to the next Step.

    If the drop-down list is empty, click the reload icon (on the right).

    - Choose Create Connection to create a new connection, enter a name for the connection and click Continue. Locate the connection type you’re configuring in [Source and Target Connections](../DataQuality/Source_and_Target_Connections.md) and refer to the Source Details section to establish the connection.

4. Click Test Credentials to verify your connection.

    A “Connection successful” message is returned or an appropriate error message is displayed if the connection attempt fails.

5. Select the desired table or file from the Table Name field. If no tables are listed click the reload icon (on the right).
6. Click the Preview the first 20 records link.

    The data for the selected source table is displayed in the source data preview pane. Use this to verify that you’re connected to the correct table. Click outside of the pane to close it.

7. Click Continue.

    The Rules page is displayed (See [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md)). A representation of the selected dataset appears on this page, displaying the field names and first few records based on the configured sample size.
