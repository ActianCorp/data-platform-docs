---
title: "Manage Template Macros"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Manage_Template_Macros.htm"
canonical_id: "actian-data-platform-manage-template-macros"
---

## Manage Template Macros

These are macros which are specific to a template.

### Edit Template Macros

To edit macros that are associated with a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the desired template name.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. Click Macros.

    The Template Macros page is displayed, listing all macros associated with the template.

You can edit the following information:

| Properties | Editable | Description |
| --- | --- | --- |
| Macro | Yes | The macro name. Click the template name to edit it. A text box is displayed. Type a new name and then press enter. |
| Value | Yes | The macro value. Click the macro value to change it. A text box is displayed. Type a new value and then press enter. To encrypt any macro values, click the ![](images/RuntimeWorkspace_78.png) icon in the Value column, and then click SECURE MACRO. The ![](images/RuntimeWorkspace_79.png) icon changes to the ![](images/RuntimeWorkspace_80.png) icon which indicates that the macro value is encrypted. |
| Description | Yes | The macro description. Click the macro description to edit it. A text box is displayed. Type a new description and then press enter. |
| Origin | No | The origin of the macro is “Template” and this information cannot be changed. |

The Template Macros page options and actions:

| Options and Actions | Description |
| --- | --- |
| ![](images/RuntimeWorkspace_81.png) | Click this iconand specify the value that you want to search. The values in each column will be evaluated during the search. Contents will be filtered based on the search string.Click ![](images/RuntimeWorkspace_82.png) to close the search box. |
| ![](images/RuntimeWorkspace_83.png) | Click the down arrow and select how many records to display on the page. The default page size is set to 25. |
| ![](images/RuntimeWorkspace_84.png) | Use these options to Navigate from one page to another. |
| ![](images/RuntimeWorkspace_85.png) | • Add Macro – See [Add Macros to Template](../Integrations/Manage_Template_Macros.md).<br>• Import Macro – See [Import Macros to a Template](../Integrations/Manage_Template_Macros.md). |
| Delete Macro | This button is displayed when you select a macro by clicking the check-box that is displayed against the macro name. Select a macro and click Delete Macro to delete it.**Caution!**The delete action cannot be undone. |
| ![](images/RuntimeWorkspace_86.png) | If any entry spans multiple lines, it is in a collapsed state by default.Click this icon to expand the collapsed lines. The icon changes to ![](images/RuntimeWorkspace_87.png) (click this to collapse the lines). |
| ![](images/RuntimeWorkspace_88.png)![](images/RuntimeWorkspace_89.png) | These are another set of icons that can be used to expand and collapse the lines which span multiple lines. |

### Add Macros to Template

To add a macro to a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the desired template name.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. Click Macros.

    The Template Macros page is displayed, listing all macros associated with the template.

4. Click the ![](images/RuntimeWorkspace_90.png) button that is displayed beside Add Macro.

    A blank record is added for the new macro with the default name “Macro 1”.

5. Click the blank space under Macro, Value, and Description fields and a text box appears. Type the required values and press enter.

![](images/RuntimeWorkspace_91.png)

![](images/RuntimeWorkspace_92.png)

![](images/RuntimeWorkspace_93.png)

### Import Macros to a Template

To import a macro to a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the desired template name.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. Click Macros.

    The Template Macros page is displayed, listing all macros associated with the template.

4. From the Add Macro drop-down menu, click Import Macros.

    The Upload Macro File dialog appears.

5. Drag and drop the macros file or click BROWSE FILES to add the macro file.

    The macros are added and listed on the Template Macros page.

![](images/RuntimeWorkspace_94.png)

![](images/RuntimeWorkspace_95.png)

![](images/RuntimeWorkspace_96.png)

### Create a Configuration from Template

To create a configuration from a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the desired template name.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. On the Template Details page, click Create Configuration.

    The Data Integration Setup page is displayed. The default source that is associated with the template appears preselected.

4. Name your configuration.
5. (Optional) change the source and template.

**IMPORTANT!**Care is required if you are changing the source and template.

6. Click Create.

    A configuration is created based on the specified information. The Configuration Details page is displayed for the new configuration. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).
