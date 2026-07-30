---
title: "Define Target"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Define_Target.htm"
canonical_id: "actian-data-platform-define-target"
---

## Define Target

You can define the target connection details from the Define Target page. The Target options are any Actian Warehouse that you can access. Target can be to either existing or newly created tables.

To define a target connection

1. Select the Actian Warehouse that you want to connect to.

    If the selected warehouse is not running, click the Click here to start this Warehouse link. This link is displayed only after you select the warehouse. After you click this link, it will take some time for the warehouse to start running. The status will be displayed as Starting, Initializing, and then Running.

2. Specify the User name and Password for the selected warehouse.

    You can either connect as the current user or uncheck Connect to Actian Warehouse as current user to manually specify user credentials.

3. Click Test Credentials to verify the connection.

    A “Connection successful” message is returned or an appropriate error message is displayed if the connection attempt fails.

4. In Target Table, select or specify the table where data will be written to. You can choose from the following options:

    - **Existing Table** – Select this option to select an existing Actian Warehouse table as your target:

    a. The Existing Table Name drop-down appears. You can either scroll through the list of tables manually to select an existing table, or type in a text to filter table names that match the specified string.

    b. If your existing table contains data, the data inside the table can be visually inspected by clicking the Preview the first 20 records link.

    You can perform the following actions on the Target Data Preview pane:

| Options | Description |
| --- | --- |
| ![](images/DesignWorkspace_6.png) | Click the down arrow and select how many records to display on the page. |
| ![](images/DesignWorkspace_7.png) | Use these options to Navigate from one page to another. |
| ![](images/DesignWorkspace_8.png) | Click this icon to search for a particular value in the data set. Contents will be filtered based on the search string.Click ![](images/DesignWorkspace_9.png) to close the search box. |

    c. Select the Output Mode as Append, Replace, or Truncate and Append. See [Target Output Modes](../Integrations/Target_Output_Modes.md).

**Note:**If the table selected on the Target side already exists, and the Output mode selected is Append or Truncate and Append, then adding, deleting, or editing existing fields will not be allowed in the mapping step. You also cannot use drag and drop to create a new field. You will only be able to update field expressions and drag and drop on field expressions. However, if the Output mode selected is Replace then you can Add, Update, and Delete fields in the mapping step.

    d. Optionally, set the Array Size, which specifies the number of rows to be sent to the target at a time. The default value is 20000. Larger values will buffer multiple rows and send them all at once. While this improves the speed, it affects error reporting (a server error will not be detected or reported until the next batch of records is sent to the server).

    The maximum value allowed for this property is 100000. While a high value can be set, many drivers have lower limits. The connector will log a message indicating if the driver is forcing a lower value for the array size. In addition, the connector does not support arrays when there is a LOB-type field in the table, or when the (maximum) length of a character-type field is longer than 32767 characters. In these cases, a message will be logged indicating the array size has been reduced to 1.

    - New Table– Select this option to create a new Actian Warehouse table as your target:

    a. Type a New Table Name, where the data will be written to.

**Note:**Table names can contain only alphanumeric characters and must begin with an alphabetic character or an underscore (_). Names can contain (but cannot begin with) the following special characters: 0 through 9, #, @, and $.

**Caution!**Care is required when selecting either Append or Delete and Append as Output Mode for an existing table. Though the system automatically tries to check if the given target table already exists, but it may fail in cases where username is NOT of the pattern "john.doe" where the SSO email id is "john.doe@email.com". If there is a failure to detect an existing table and user tries to Add or Delete fields, this may result in data loss.

    b. **Optionally, set the Array Size, which specifies the number of rows to be sent to the target at a time. The default value is****20000****. Larger values will buffer multiple rows and send them all at once. While this improves the speed, it affects error reporting (a server error will not be detected or reported until the next batch of records is sent to the server).**

    **The maximum value allowed for this property is****100000****. While a high value can be set, many drivers have lower limits. The connector will log a message indicating if the driver is forcing a lower value for the array size. In addition, the connector does not support arrays when there is a LOB-type field in the table, or when the (maximum) length of a character-type field is longer than 32767 characters. In these cases, a message will be logged indicating the array size has been reduced to****1****.**

5. **Select the****Provide table access in Actian Query Editor** option for granting table access to the dbadmingrp group.
6. Click Continue.

    The Source & Target Mapping page is displayed. See [Mapping](../Integrations/Mapping.md).
