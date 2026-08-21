---
title: "View Configurations"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "View_Configurations.htm"
canonical_id: "actian-data-platform-view-configurations"
---

## View Configurations

To view configurations

1. Click Integrations, Manage, Configurations.

    The Configurations page displays the available configurations.

2. Click one of the following tabs to reorganize the configuration list:

    - All – Displays all configurations.

    - Recent – Displays recently executed, edited, or created configurations.

    - Favorites – Displays configurations that were set as favorites. See [Set a Configuration as a Favorite](../Integrations/Set_a_Configuration_as_a_Favorite.md).

**Note:**The configurations are sorted in alphabetical order in each view.

    The following information is displayed:

| Column Name | Description |
| --- | --- |
| Configuration | Displays the name of the configuration. Clicking the Configuration header sorts the list alphabetically in ascending or descending order.Clicking a configuration name displays the Configuration Details page which provides various properties related to the Configuration. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md). |
| Template Used | Displays the template that the configuration is based on. If the configuration is not based on a template, Not Set is displayed. Clicking the Template Used header sorts the list alphabetically in ascending or descending order.Clicking the template name displays the Template Details page which provides various properties related to the Template. See [Edit Template Details](../Integrations/Edit_Template_Details.md). |
| Next Job | The next job column provides some insight in terms of when a configuration will run. For example “On Demand” will be displayed for a configuration that must be run manually and “Every 6 hours” will be displayed for a configuration that is scheduled to run after every six hours.See [Run a Configuration Manually](../Integrations/Run_a_Configuration_Manually.md) and [Edit Configuration Schedule](../Integrations/Edit_Configuration_Schedule.md). |
| Owner | Displays the first two characters of the configuration owner (creator) name. Clicking on the owner icon displays the username of the owner. |
| Active | Whether the configuration is active (set to run on demand or by schedule) or inactive (set not to run on demand or by schedule) |

    Configuration page options and actions:

| Options and Actions | Description |
| --- | --- |
| ![](images/RuntimeWorkspace_9.png) | Click this icon to search for specific text within the configuration listing. Contents will be filtered based on the search string.Click ![](images/RuntimeWorkspace_10.png) to clear the search box. |
| ![](images/RuntimeWorkspace_11.png) | Click this icon and then select one or more of the following options to list configurations by the selected one or more filters:<br>• TemplateNotSet - Lists configuration for which template is not set.<br>• OnDemand - Lists unscheduled configurations.<br>• Active - Lists active configurations.<br>• Inactive - Lists inactive configurations. |
| ![](images/RuntimeWorkspace_12.png) | Click the down arrow and select how many records to display on the page. |
| ![](images/RuntimeWorkspace_13.png) | Use these options to Navigate from one page to another. |
| ![](images/RuntimeWorkspace_14.png) | Select one or more configurations by clicking the check box that is displayed before the configuration name to perform the following actions from the toolbar which displays on the top right of the page:<br>• Run – Click this option to execute the selected configurations. Running a configuration takes you to the Run History page. See [View Configuration Jobs](../Integrations/View_Configuration_Jobs.md) and [Run a Configuration Manually](../Integrations/Run_a_Configuration_Manually.md).<br>• Active – Click this option to set the selected configurations to Active. See [Set a Configuration to Active or Inactive](../Integrations/Set_a_Configuration_to_Active_or_Inactive.md).<br>• Inactive – Click this option to set the selected configurations to Inactive. See [Set a Configuration to Active or Inactive](../Integrations/Set_a_Configuration_to_Active_or_Inactive.md).<br>• Favorite – Click this option to set the associated configuration to Favorite. See [Set a Configuration as a Favorite](../Integrations/Set_a_Configuration_as_a_Favorite.md).<br>• Delete – Click this option to delete the selected configurations. See [Delete a Configuration](../Integrations/Delete_a_Configuration.md). |
| ![](images/RuntimeWorkspace_15.png) | Each configuration has its own corresponding context menu (refer second image) displayed within the table view.Click ![](images/RuntimeWorkspace_16.png) next to the configuration record will expose a set of execution options for the selected configurations. You can choose from the following actions:<br>• Run – Click this option to execute the selected configuration. Running a configuration takes you to the Run History page. See [View Configuration Jobs](../Integrations/View_Configuration_Jobs.md) and [Run a Configuration Manually](../Integrations/Run_a_Configuration_Manually.md).<br>• Run with Message – Click this option to run the associated configuration after entering a message. See [Run Configuration with a Message](../Integrations/Run_Configuration_with_a_Message.md).<br>• Run with File – Click this option to run the associated configuration after uploading a file. See [Run Configuration with a File](../Integrations/Run_Configuration_with_a_File.md).<br>• Duplicate – Click this option to duplicate the associated configuration, usually for editing. See [Duplicate a Configuration](../Integrations/Duplicate_a_Configuration.md).<br>• Set as Active – Click this option to set the selected configurations to Active. See [Set a Configuration to Active or Inactive](../Integrations/Set_a_Configuration_to_Active_or_Inactive.md).<br>• Set as Inactive – Click this option to set the selected configurations to Inactive. See [Set a Configuration to Active or Inactive](../Integrations/Set_a_Configuration_to_Active_or_Inactive.md).<br>• Favorite – Click this option to set the associated configuration to Favorite. See [Set a Configuration as a Favorite](../Integrations/Set_a_Configuration_as_a_Favorite.md).<br>• Delete – Click this option to delete the selected configurations. See [Delete a Configuration](../Integrations/Delete_a_Configuration.md). |
| Import Integration | Click this to import an integration. See [Import Integration](../Integrations/Import_Integration.md). |
