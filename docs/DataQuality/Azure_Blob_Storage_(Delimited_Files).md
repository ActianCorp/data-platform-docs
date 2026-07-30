---
title: "Azure Blob Storage (Delimited Files)"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Azure_Blob_Storage_(Delimited_Files).htm"
canonical_id: "actian-data-platform-azure-blob-storage-delimited-files"
---

## Azure Blob Storage (Delimited Files)

This topic describes Azure Blob Storage connector properties and connection details for reading blobs in the block storage managed by the Azure Blob Storage cloud service. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for Azure Blob Storage](../DataQuality/Azure_Blob_Storage_(Delimited_Files).md) to [Define Source](../DataQuality/Define_Source.md).

!!! note "Note"

    CSV is the ONLY supported data format.

Prerequisites

You must have an Azure account and credentials.

Source Details for Azure Blob Storage

This topic provides properties and details needed to create a new connection and specify the source using the Azure Blob Storage connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to Azure Blob Storage will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Advanced Properties | Enable this property to access additional properties (for example, Endpoint Suffix). |
| Account Name | Specifies a storage account name on Azure Blob Storage. This property is mandatory. |
| Access Key | Specifies the access key to connect to the Azure Blob Storage account. This property is mandatory. |
| Endpoints Protocol | (Optional) Specifies a protocol that is used to make a connection. It has two possible values: HTTPs (default) and HTTP. |
| Endpoint Suffix | (Optional) Specifies the endpoint suffix to use for establishing the connection. The default value is core.windows.net. This property is applicable when Advanced Properties is enabled. |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Container Name | Specifies the name of the container to access. This property is mandatory. |
| Folder | (Optional) Specifies the folder containing the object. Clicking on the refresh button lists folders within the current folder. Hierarchies of the folders are navigated by repeatedly clicking on the refresh button. |
| Object | Specifies the Object on which to perform operation. This property is mandatory. |
| Header | (Optional) Specifies whether a comma separated lists of values (CSV data) contains a header row. Enable to include a header row. Disable to exclude one. This property is disabled by default. |
| Quote | (Optional) Specifies the quote character. Default value is ". |
| Delimiter | (Optional) Specifies the field delimiter character. Default value is ,. |
| Escape | (Optional) Specifies the escape character. This property is empty by default. |
| Separator | (Optional) Specifies the row separator characters. Default value is \r\n. |
| Character Set | (Optional) Specifies the character set of the data. Default value is UTF-8. |
| Limit | (Optional) Specifies the maximum number of records to return. This property is empty by default. |
| Sample Size | (Optional) Specifies the number of records to analyze when determining the data structure. Default value is 5000. |
| Read Chunk Size (Bytes) | (Optional) Specifies the size of chunks, in bytes, in which to retrieve data from the source object. When the property is not specified, or is set to a non-positive value, the entire object data is retrieved in a single chunk. Default value is 5000000. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_56.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

None
