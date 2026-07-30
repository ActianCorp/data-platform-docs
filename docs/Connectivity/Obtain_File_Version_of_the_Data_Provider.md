---
title: "Obtain File Version of the Data Provider"
product: "Actian Data Platform"
guide: "Connectivity Guide"
source_file: "Obtain_File_Version_of_the_Data_Provider.htm"
canonical_id: "actian-data-platform-obtain-file-version-of-the-data-provider"
---

## Obtain File Version of the Data Provider

Actian Support may ask what file version of the data provider is installed on the client.

The file version of the data provider's Ingres.Client.dll is incremented to mark changes to the data provider. You can obtain the change level of the data provider by displaying the file version of the DLL.

The Ingres.Client.dll is installed (by default) into the C:\Program Files\Ingres\Ingres .NET Data Provider\v2.1 directory and also into the Global Assembly Cache (GAC) that can be displayed at C:\WINDOWS\assembly.

To display the file version of the Ingres.Client.dll using the Windows file explorer

Right-click the Ingres.Client.dll in one of the directories mentioned previously and select Properties.

The Version tab of the Properties dialog displays the file version of the data provider.
