---
title: "Manage Configuration Macros"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Manage_Configuration_Macros.htm"
canonical_id: "actian-data-platform-manage-configuration-macros"
---

## Manage Configuration Macros

These are macros which are specific to a configuration.

### Edit Configuration Macros

To edit macros that are associated with a configuration

1. Click Integrations, Manage, Configurations.

    The Configurations page is displayed, listing all available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the desired configuration name.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click Macros.

    The Configuration Macros page is displayed, listing all macros associated with the configuration.

You can edit the following information:

| Properties | Editable | Description |
| --- | --- | --- |
| Macro | Yes | The macro name. Click the template name to edit it. A text box is displayed. Type a new name and then press enter. |
| Value | Yes | The macro value. Click the macro value to change it. A text box is displayed. Type a new value and then press enter. To encrypt any macro values, click the ![](images/RuntimeWorkspace_30.png) icon in the Value column, and then click SECURE MACRO. The ![](images/RuntimeWorkspace_31.png) icon changes to the ![](images/RuntimeWorkspace_32.png) icon which indicates that the macro value is encrypted. |
| Description | Yes | The macro description. Click the macro description to edit it. A text box is displayed. Type a new description and then press enter. |
| Origin | No | The origin of macro. For example Configuration, Public, Private. |

The Configuration Macros page options and actions:

| Options and Actions | Description |
| --- | --- |
| ![](images/RuntimeWorkspace_33.png) | Click this icon and specify the value that you want to search. The values in each column will be evaluated during the search. Contents will be filtered based on the search string.Click ![](images/RuntimeWorkspace_34.png) to close the search box. |
| ![](images/RuntimeWorkspace_35.png) | Click the down arrow and select how many records to display on the page. The default page size is set to 25. |
| ![](images/RuntimeWorkspace_36.png) | Use these options to Navigate from one page to another. |
| ![](images/RuntimeWorkspace_37.png) | • Add Macro - See [Add Macros to a Configuration](../Integrations/Manage_Configuration_Macros.md).<br>• Import Macro - See [Import Macros to a Configuration](../Integrations/Manage_Configuration_Macros.md). |
| Delete Macro | This button is displayed when you select a macro by clicking the check-box that is displayed against the macro name. Select a macro and click Delete Macro to delete it.**Caution!**The delete action cannot be undone. |
| ![](images/RuntimeWorkspace_38.png) | If any entry spans multiple lines, it is in a collapsed state by default.Click this icon to expand the collapsed lines. The icon changes to ![](images/RuntimeWorkspace_39.png) (click this to collapse the lines). |
| ![](images/RuntimeWorkspace_40.png)![](images/RuntimeWorkspace_41.png) | These are another set of icons that can be used to expand and collapse the lines which span multiple lines. |

### Add Macros to a Configuration

To add a macro to a configuration

1. Click Integrations, Manage, Configurations.

    The Configurations page is displayed, listing all available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the desired configuration name.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click Macros.

    The Configuration Macros page is displayed, listing all macros associated with the configuration.

4. Click the ![](images/RuntimeWorkspace_42.png) button that is displayed beside Add Macro.

    A blank record is added for the new macro with the default name “Macro 1”.

5. Click the blank space under Macro, Value, and Description fields and a text box appears. Type the required values and press enter.

![](images/RuntimeWorkspace_43.png)

![](images/RuntimeWorkspace_44.png)

![](images/RuntimeWorkspace_45.png)

### Import Macros to a Configuration

To import a macro to a template

1. Click Integrations, Manage, Configurations.

    The Configurations page is displayed, listing all available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the desired configuration name.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click Macros.

    The Configuration Macros page is displayed, listing all macros associated with the configuration.

4. From the Add Macro drop-down menu, click Import Macros.

    The Upload Macro File dialog appears.

5. Drag and drop the macros file or click BROWSE FILES to add the macro file.

    The macros are added and listed on the Configuration Macros page. For more information on macros, see DataConnect documentation on [https://docs.actian.com/](https://docs.actian.com/).

![](images/RuntimeWorkspace_46.png)

![](images/RuntimeWorkspace_47.png)

![](images/RuntimeWorkspace_48.png)
