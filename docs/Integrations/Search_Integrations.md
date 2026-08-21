---
title: "Search Integrations"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Search_Integrations.htm"
canonical_id: "actian-data-platform-search-integrations"
---

## Search Integrations

To search integrations

1. Click the Integrations link at the top of the page.

    The Integration Designs page displays the available integrations.

2. Enter an integration name in the Search box and click ![](images/DesignWorkspace_15.png) to search it.

    You can also perform the following actions:

| Options | Description |
| --- | --- |
| ![](images/DesignWorkspace_16.png) | Click this icon to search for specific text within the integrations listing. Contents will be filtered based on the search string.Click ![](images/DesignWorkspace_17.png) to clear the search box. |
| ![](images/DesignWorkspace_18.png) | Click this icon and select a connector to filter the list of integrations by connector. |
| ![](images/DesignWorkspace_19.png) | Click this icon and select Nameor Date to sort the list of integrations by one of those fields. |

3. Click the check box to select the desired integration. A toolbar is displayed on the top right of the page. You can perform the following actions from the toolbar:

| Actions | Description |
| --- | --- |
| ![](images/DesignWorkspace_20.png) | Run the selected integration. See also [Run an Integration Manually](../Integrations/Run_an_Integration_Manually.md). |
| ![](images/DesignWorkspace_21.png) | Edit the selected integration. See [Edit Integration](../Integrations/Edit_Integration.md). |
| ![](images/DesignWorkspace_22.png) | Make a copy of the selected integration, usually for editing. See [Duplicate Integration](../Integrations/Duplicate_Integration.md). |
| ![](images/DesignWorkspace_23.png) | Delete the selected integration. See [Delete Integration](../Integrations/Delete_Integration.md). |

    Integration page options and actions:

| Options | Description |
| --- | --- |
| ![](images/DesignWorkspace_24.png) | Click the ![](images/DesignWorkspace_25.png) icon that is displayed for an integration. A set of execution options is displayed. You can choose from the following actions:<br>• View Details - Opens the Integration Details page. See [Edit Integration](../Integrations/Edit_Integration.md).<br>• Run - Executes the current integration.<br>• Edit - Takes you to the Edit Integration page. See [Edit Integration](../Integrations/Edit_Integration.md).<br>• Duplicate - Creates a copy of the current integration. See [Duplicate Integration](../Integrations/Duplicate_Integration.md).<br>• Delete - Deletes the current integration. See [Delete Integration](../Integrations/Delete_Integration.md). |
| ![](images/DesignWorkspace_26.png) | Create an Integration. See [Creating Integrations](../Integrations/Creating_Integrations.md). |
| ![](images/DesignWorkspace_27.png) | • Integration Designs - Displays the Integration Designs page.<br>• Connections - Displays the Connections page. See [View Connection](../Integrations/View_Connection.md).<br>• Services (REST/SOAP) - Displays the Services (REST/SOAP) page. See [Services (REST/SOAP)](../Integrations/Services_(REST_2fSOAP).md).<br>• Run History - Displays the Run History page. See [View Integration Run History](../Integrations/View_Integration_Run_History.md). |

!!! warning "Important"

    **IMPORTANT!**When using an Agent to run an integration with Actian Warehouse as the target, make sure the IP address of the host machine where the Agent is installed is added to the Warehouse's allowed IP list. Without this, the integration will not run. See [Update Allow List IP Addresses](../User/UpdateAllowListIPs.md).
