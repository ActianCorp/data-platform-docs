---
title: "Google Cloud Storage"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Google_Cloud_Storage.htm"
canonical_id: "actian-data-platform-google-cloud-storage"
---

## Google Cloud Storage

The Google Cloud Storage connector provides access to Google Cloud Storage buckets and objects in the Google Cloud Platform.

- [Prerequisites](../Integrations/Google_Cloud_Storage.md)
- [Connection Details](../Integrations/Google_Cloud_Storage.md)

- [Source Details](../Integrations/Google_Cloud_Storage.md)
- [Additional Information](../Integrations/Google_Cloud_Storage.md)

Prerequisites

You must have the Google Cloud account and credentials.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Credentials | (Optional) The JSON credentials of the service account used to access the Cloud Storage service. This is the content of the credentials file that can be downloaded from the Cloud Storage console.**Note:**To define a connection, the concerned GCP account must have the permission for storage.buckets.list. Your credentials are authenticated successfully only if you have the permissions. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Bucket | Specifies the name of the cloud storage bucket to access. This is a mandatory property. |
| Folder | (Optional) Specifies the folder containing the object. Clicking on the refresh button lists folders within the current folder. Hierarchies of the folders are navigated by repeatedly clicking on the refresh button. |
| Object | Specifies the name of the object to access. This is a mandatory property. |
| Read Chunk Size (Bytes) | (Optional) Specifies the size of chunks, in bytes, in which to retrieve data from the source object. When the property is not specified, or is set to a non-positive value, the entire object data is retrieved in a single chunk. |
| Data Format | Specifies the data format. This is a mandatory property. Select one of the following as per the data format type:<br>• CSV:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Quote: Specifies the quote character. Default value is ".–Delimiter: Specifies the field delimiter character. Default value is ,.–Escape: Specifies the escape character.–Separator: Specifies the row separator characters. Default value is \r\n.–Character Set: Specifies the character set of the data. Default value is UTF-8.–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.<br>• Excel:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Worksheet Index: Specifies the index of the worksheet. The index of the first worksheet is 1(default).–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.<br>• Avro:The following properties must be configured:–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the AVRO data you wish to map to tables in the target.<br>• Parquet<br>• JSON:The following properties must be configured:–Find Array: If enabled, specifies that the output will iterate on the first array found in the JSON document.–Array Path: Specifies the path of the JSON array within the document. Omit if the document is an array. For example,"/resources".–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the JSON data you wish to map to tables in the target. |
| Limit | (Optional) Specifies the maximum number of records to return. |
| Batch Size | (Optional) Specifies the number of records to return per batch. |

Additional Information

Limitations: The Google Cloud Storage connector only supports authentication for Google service accounts. Authentication for Google end-user accounts and API keys is not supported.
