---
title: "View Macros"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "View_Macros.htm"
canonical_id: "actian-data-platform-view-macros"
---

## View Macros

To view macros

Click Integrations, Manage, Macros.

All macros that are available to the logged in user are listed.

To switch between Public Macros and Private Macros, click the macros control:

![](images/PublicPrivateSlider.png)

The Macros page displays the available macros.

- Private Macros – Private macros can be created, edited, or deleted by the logged–in user. These macros are visible to administrators.
- Public Macros – They may be created, edited, or deleted by an administrator. Public macros are visible to any user.

The following values for macros are displayed.

| Column Name | Description |
| --- | --- |
| Macro | Name of the macro. Click the macro name to edit it. A text box is displayed. Type a new name and then press enter.Clicking the Macro header sorts the files list in ascending or descending alphabetical order. |
| Value | Macro value and whether the value is encrypted:![](images/RuntimeWorkspace_111.png) – Unencrypted (blue)![](images/RuntimeWorkspace_112.png) – Encrypted (gray)Click the macro value to change it. A text box is displayed. Type a new value and then press enter.To encrypt any macro values, click the ![](images/RuntimeWorkspace_113.png) icon in the Value column, and then click SECURE MACRO. The ![](images/RuntimeWorkspace_114.png) icon changes to the ![](images/RuntimeWorkspace_115.png) (gray) icon which indicates that the macro value is encrypted.**Note:**Secured macros cannot be unsecured, and their values cannot be edited. If you need to change the value of a secured macro, you must delete and readd it.Clicking the Value header sorts the files list in ascending or descending date/time order. |
| Description | Provides additional details about the use, actions or requirements of the macro.Click the macro description to edit it. A text box is displayed. Type a new description and then press enter. |

You can also view and manage macros per configuration or template.

- To view macros associated with a particular configuration, see [Manage Configuration Macros](../Integrations/Manage_Configuration_Macros.md).
- To view macros associated with a particular template, see [Manage Template Macros](../Integrations/Manage_Template_Macros.md).
