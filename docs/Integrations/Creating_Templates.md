---
title: "Creating Templates"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Creating_Templates.htm"
canonical_id: "actian-data-platform-creating-templates"
---

## Creating Templates

Templates contain integration settings that can be reused by linked configurations (see [Managing Configurations](../Integrations/Managing_Configurations.md)). Templates include a package, macros, and a location to execute the job.

You can create a configuration from a template by specifying a source and then run the configuration (see [Create a Configuration from Template](../Integrations/Manage_Template_Macros.md)). The data from the source will then be loaded into your Actian Warehouse.

To create a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed. See [View Templates](../Integrations/View_Templates.md).

2. Click Create Template.

    The Data Integration Template Setup page is displayed.

3. Name your template and click one of the following buttons:

    - Integration Files – Choose an Integration from the Integrations File repository.

    The File Manager dialog appears.

    a. Select whether to link a public or private package:

![](images/RuntimeWorkspace_62.png)

    The file(s) are listed.

    b. Select a package from the list:

![](images/RuntimeWorkspace_63.png)

    c. Click the Select Package button.

    The File Manager dialog closes, and the file is listed.

    Click ![](images/RuntimeWorkspace_64.png) to unlink the file.

    - Local System – Choose an existing Integration from your local system.

    The file(s) are listed.

    Click ![](images/RuntimeWorkspace_65.png) to unlink a file.

!!! note "Note"

    Accepted file formats are: .djar, .rtc, .process, .ip.xml, .tf.xml, .jar, .dr, or .js

4. Click **Create**.

    The template is created and you are navigated to the Template Details page. See [View Templates](../Integrations/View_Templates.md).
