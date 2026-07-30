---
title: "Azure Blob Storage"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Azure_Blob_Storage.htm"
canonical_id: "actian-data-platform-azure-blob-storage"
---

## Azure Blob Storage

The Azure Blob Storage connector provides support to perform read and write operations on the blobs in the block storage managed by the Azure Blob Storage cloud service.

- [Prerequisites](../Integrations/Azure_Blob_Storage.md)
- [Connection Details](../Integrations/Azure_Blob_Storage.md)

- [Source Details](../Integrations/Azure_Blob_Storage.md)
- [Additional Information](../Integrations/Azure_Blob_Storage.md)

Prerequisites

You must have an Azure account and credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Account Name | Specifies a storage account name on Azure Blob Storage. This is a mandatory property. |
| Access Key | Specifies the access key to connect to the Azure Blob Storage account. This is a mandatory property. |
| Endpoints Protocol | (Optional) Specifies a protocol that is used to make a connection. It has two possible values: HTTPs (default) and HTTP. |
| Endpoint Suffix | (Optional) Specifies the endpoint suffix to use for establishing the connection. The default value is core.windows.net. This property is applicable when Advanced Properties toggle is enabled. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Container Name | Specifies the name of the container to access. This is a mandatory property. |
| Folder | (Optional) Specifies the folder containing the object. Clicking on the refresh button lists folders within the current folder. Hierarchies of the folders are navigated by repeatedly clicking on the refresh button. |
| Object | Specifies the Object on which to perform operation. This is a mandatory property. |
| Read Chunk Size (Bytes) | (Optional) Specifies the size of chunks, in bytes, in which to retrieve data from the source object. When the property is not specified, or is set to a non-positive value, the entire object data is retrieved in a single chunk. |
| Data Format | Specifies the data format. This is a mandatory property. Select one of the following as per the data format type:•CSV:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Quote: Specifies the quote character. Default value is ".–Delimiter: Specifies the field delimiter character. Default value is ,.–Escape: Specifies the escape character.–Separator: Specifies the row separator characters. Default value is \r\n.–Character Set: Specifies the character set of the data. Default value is UTF-8.–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.•Excel:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Worksheet Index: Specifies the index of the worksheet. The index of the first worksheet is 1(default).–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.•Avro:The following properties must be configured:–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the AVRO data you wish to map to tables in the target.•Parquet•JSON:The following properties must be configured:–Find Array: If enabled, specifies that the output will iterate on the first array found in the JSON document.–Array Path: Specifies the path of the JSON array within the document. Omit if the document is an array. For example,"/resources".–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the JSON data you wish to map to tables in the target. |
| Limit | (Optional) Specifies the maximum number of records to return. |
| Batch Size | (Optional) Specifies the number of records to return per batch. |

Additional Information

None
