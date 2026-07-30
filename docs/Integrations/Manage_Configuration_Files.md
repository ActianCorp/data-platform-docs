---
title: "Manage Configuration Files"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Manage_Configuration_Files.htm"
canonical_id: "actian-data-platform-manage-configuration-files"
---

## Manage Configuration Files

You can upload files for use with your configuration. These can be public files or private files.

- Private Files – Private files can be created, edited, or deleted by the logged–in user. These files are visible to administrators.
- Public Files – Public files can be seen and accessed by any user. They may be created, edited, or deleted by an administrator.

### View Configuration Files

There is a repository where you can store files (publicly or privately) which can be referenced within a configuration.

To view files associated with a configuration

1. Click Integrations, Manage, Configurations.

    The Configurations page is displayed, listing all available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the desired configuration name.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click Files.

    The Configuration Files page is displayed, listing all files associated with the configuration.

The following details are displayed:

| Properties | Description |
| --- | --- |
| File Name | Name of the file. Click the File Name header to sort the file list in ascending or descending alphabetical order. Click the file name to download it. |
| File Type | The file type, based on the file extension. |
| Last Modified | Date the file was last modified. Click the Last Modified header to sort the file list in ascending or descending date/time order. |
| File Size | Size of the file in kilobytes. Click the File Size header to sort the file list in ascending or descending file size order. |

The Configuration Files page options and actions:

| Options and Actions | Description |
| --- | --- |
| ![](images/RuntimeWorkspace_49.png) | Click this icon and specify the value that you want to search. The values in each column will be evaluated during the search. Contents will be filtered based on the search string.Click ![](images/RuntimeWorkspace_50.png) to close the search box. |
| ![](images/RuntimeWorkspace_51.png) | Click the down arrow and select how many records to display on the page. The default page size is set to 25. |
| ![](images/RuntimeWorkspace_52.png) | Use these options to Navigate from one page to another. |
| ![](images/RuntimeWorkspace_53.png) | •Upload Files – See [Upload Files to a Configuration](../Integrations/Manage_Configuration_Files.md).•Link file in File Repository – See [Link a File to the File Repository](../Integrations/Manage_Template_Files.md). |
| Delete File Link | This button is displayed when you select a file by clicking the check-box that is displayed against the file name. Select a file and click Delete File Link to disassociate it from the current template. |

### Upload Files to a Configuration

To upload files to a configuration

1. Click Integrations, Manage, Configurations.

    The Configurations page is displayed, listing all available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the desired configuration name.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click Files.

    The Configuration Files page is displayed, listing all files associated with the configuration.

4. Click the ![](images/RuntimeWorkspace_54.png) button that is displayed beside Upload File.

    The Upload Files dialog appears.

5. Drag and drop the file or click BROWSE FILES to add the file.

    The file is added and listed on the Template Files page.

### Link a File in the File Repository

To link a file in file repository

1. Click Integrations, Manage, Configurations.

    The Configurations page is displayed, listing all available configurations. See [View Configurations](../Integrations/View_Configurations.md).

2. Click the desired configuration name.

    The Configuration Details page is displayed. See [Edit Configuration Details](../Integrations/Edit_Configuration_Details.md).

3. Click Files.

    The Configuration Files page is displayed.

4. From the Upload File drop-down menu, click Link file in Files Repository.

    The File Manager dialog appears.

    a. Select whether to link a public or private package:

    ![](images/RuntimeWorkspace_55.png)

    The files are listed.

    a. Select a package from the list:

    ![](images/RuntimeWorkspace_56.png)

    a. Click the Select Package button.

    The File Manager dialog closes, and the file is listed.

    Click ![](images/RuntimeWorkspace_57.png) to unlink the file.

!!! note "Note"

    Accepted file formats are: .djar, .rtc, .process, .ip.xml, .tf.xml, .jar, .dr, or .js

5. Select the file and click Link File.

    The linked file is listed on the Configuration Files page.
