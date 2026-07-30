---
title: "Manage Template Files"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Manage_Template_Files.htm"
canonical_id: "actian-data-platform-manage-template-files"
---

## Manage Template Files

You can upload files for use with your templates. These can be public files or private files.

- Private Files – Private files can be created, edited, or deleted by the logged-in user. These files are visible to administrators.
- Public Files – Public files can be seen and accessed by any user. They may be created, edited, or deleted by an administrator.

### View Template Files

To view files associated with a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the desired template name.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. Click Files.

    The Template Files page is displayed, listing all files associated with the template.

The following details are displayed:

| Properties | Description |
| --- | --- |
| File Name | Name of the file. Click the File Name header to sort the file list in ascending or descending alphabetical order. Click the file name to download it. |
| Last Modified | Date the file was last modified. Click the Last Modified header to sort the file list in ascending or descending date/time order. |
| File Size | Size of the file in kilobytes. Click the File Size header to sort the file list in ascending or descending file size order. |
| File Type | The file type, based on the file extension. |

The Template Details page options and actions:

| Options and Actions | Description |
| --- | --- |
| ![](images/RuntimeWorkspace_97.png) | Click this icon and specify the value that you want to search. The values in each column will be evaluated during the search. Contents will be filtered based on the search string.Click ![](images/RuntimeWorkspace_98.png) to close the search box. |
| ![](images/RuntimeWorkspace_99.png) | Click the down arrow and select how many records to display on the page. The default page size is set to 25. |
| ![](images/RuntimeWorkspace_100.png) | Use these options to Navigate from one page to another. |
| ![](images/RuntimeWorkspace_101.png) | •Upload Files – See [Upload Files to a Template](../Integrations/Manage_Template_Files.md).•Link file in File Repository – See [Link a File to the File Repository](../Integrations/Manage_Template_Files.md). |
| Delete File Link | This button is displayed when you select a file by clicking the check-box that is displayed against the file name. Select a file and click Delete File Link to disassociate it from the current template. |

### Upload Files to a Template

To upload files to a template

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the template name you want to add a macro to.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. Click Files.

    The Template Files page is displayed, listing all files associated with the template.

4. Click the ![](images/RuntimeWorkspace_102.png) button that is displayed beside Upload File.

    The Upload Files dialog appears.

5. Drag and drop the file or click BROWSE FILES to add the file.

    The file is added and listed on the Template Files page.

### Link a File to the File Repository

To link file in the file repository

1. Click Integrations, Manage, Templates.

    The Templates page is displayed, listing all available templates. See [View Templates](../Integrations/View_Templates.md).

2. Click the template name you want to add a macro to.

    The Template Details page is displayed. See [Edit Template Details](../Integrations/Edit_Template_Details.md).

3. Click Files.

    The Template Files page is displayed, listing all files associated with the template.

4. From the Upload File drop-down menu, click Link file in Files Repository.

    The File Manager dialog appears.

    a. Select whether to link a public or private package:

![](images/RuntimeWorkspace_103.png)

    The files are listed.

    b. Select a package from the list:

![](images/RuntimeWorkspace_104.png)

    c. Click the Select Package button.

    The File Manager dialog closes, and the file is listed.

    Click ![](images/RuntimeWorkspace_105.png) to unlink the file.

!!! note "Note"

    Accepted file formats are: .djar, .rtc, .process, .ip.xml, .tf.xml, .jar, .dr, or .js

5. Select the file and click Link File.

    The linked file is listed on the Template Files page.
