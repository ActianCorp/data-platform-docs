---
title: "Edit Integration"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Edit_Integration.htm"
canonical_id: "actian-data-platform-edit-integration"
---

## Edit Integration

To edit an integration

1. Click the Integrations link at the top of the page.

    The Integration Designs page displays the available integrations.

2. Select the check box that is displayed for the integration that you want to edit, then click ![](images/DesignWorkspace_36.png).

    The Edit Integration page is displayed. By default the focus is on the Mapping page. Navigation between pages is possible by using the Back and Continue buttons at the bottom of the page. When navigation to other pages is not possible, the button will fade in color and will not be active.

3. **Navigate to the desired page to view the current integration information and edit it. You can edit the following pages:**

    - Mapping – See [Mapping](../Integrations/Mapping.md).

    - Define Source – See [Define Source](../Integrations/Define_Source.md).

    - Define Target – See [Define Target](../Integrations/Define_Target.md).

**Note:**If the table selected on the Target side already exists, and the Output mode selected is Append or Truncate and Append, then you will not be allowed to Add, Delete, and Update fields in the mapping step. You also cannot use drag and drop to create a new field. You will only be able to update field expressions and drag and drop on field expressions. However, if the Output mode selected is Replace then you can Add, Update, and Delete fields in the mapping step.

4. Once editing is complete, navigate back to the mapping step and perform one of the following actions:

| Actions | Description |
| --- | --- |
| Save & Close | Save your integration and close the Edit Integration page. Focus is directed back to the Integration Designs page from where you can search and list you newly created integration. See [View Integration Details](../Integrations/View_Integration_Details.md). |
| Save & Schedule | Save your integration and navigate to the Scheduling page. |
| Save & Run | Save your integration and execute it.**IMPORTANT!**When using an Agent to run an integration with Actian Warehouse as the target, make sure the IP address of the host machine where the Agent is installed is added to the Warehouse's allowed IP list. Without this, the integration will not run. See[Update Allow List IP Addresses](../User/UpdateAllowListIPs.md). |
