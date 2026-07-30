---
title: "Mapping"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Mapping.htm"
canonical_id: "actian-data-platform-mapping"
---

## Mapping

On the Mapping step, by default, the source and target fields are auto-mapped by matching field names (if creating new output tables, field mapping is 1-1). If you want to map a specific field, drag and drop it from the source grid to the target grid. You can drop the field in any position as long as your output mode is set to Replace. Information on how to manually add or delete fields is also provided [here](../Integrations/Mapping.md).

The source information is displayed on the left side and the target information is displayed on the right. The specified table names are displayed in parentheses next to the source and target connectors.

You can perform the following actions:

| Actions | Description |
| --- | --- |
| >><< | Click these icons to expand and hide the source and target view.When expanded, the source view displays the Type and Size columns. The Target view displays the Field, Expression, Type, and Size columns by default. |
| Add a new field | Click ![](images/DesignWorkspace_10.png)to add a new field row to the target view. Specify the following information for the new field:•Field – Provide a name for the field.•Expression – Add any valid expression. For string literals, use double quotes. Do not use quotes for numbers.•Type – Data type of the field.•Size – Length of the field.You can drag or drop the new field to the desired position or simply edit the field number and change it to the desired position.You can change the data type and the size if required. Size is editable based on the data type. For example, you cannot change the size for INTEGER, BOOLEAN, and FLOAT data types. You can change the size for Text, VARCHAR, or CHAR data types. |
| Map a field | Drag and drop a field from the source view to the target view |
| Auto map fields | To automatically map fields by name or to copy all fields from source to target in case of an empty schema, click Actions, and then click Auto Map.If the target exists and the field names do not match, the fields are left unmatched. Then you need to manually map or set some expression for the field, or can choose to leave it blank. |
| Preview mapping results | Click this link to preview a sample set of data that will be written into the target.**IMPORTANT!**When using an Agent with Actian Warehouse as the target, make sure the IP address of the host machine where the Agent is installed is added to the Warehouse's allowed IP list. Without this, the integration will not run and the mapping results will not show. See[Update Allow List IP Addresses](../User/UpdateAllowListIPs.md). |
| Add an expression. | See [Expression Builder](../Integrations/Expression_Builder.md).**Note:**You cannot manually create or edit expressions by typing in the target expression cell. |
| Delete an expression | Click ![](images/DesignWorkspace_11.png) in the desired target expression cell to delete an expression. |
| Clear expressions | To clear the expressions for all the target fields, click Actions, and then click Clear Expressions.**Note:**You cannot undo this action. |
| ![](images/DesignWorkspace_12.png) | Click this icon and specify the value that you want to search. The values in each column will be evaluated during the search. Contents will be filtered based on the search string.Click ![](images/DesignWorkspace_13.png) to close the search box. |
| ![](images/DesignWorkspace_14.png) | Select one or more fields to delete and click this icon. A pop-up message appears asking for confirmation. Click OK. The fields are deleted. |
