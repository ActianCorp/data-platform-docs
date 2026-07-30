---
title: "Google Cloud Storage (Delimited Files)"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Google_Cloud_Storage_(Delimited_Files).htm"
canonical_id: "actian-data-platform-google-cloud-storage-delimited-files"
---

## Google Cloud Storage (Delimited Files)

This topic describes Google Cloud Storage connector properties and connection details for reading data from Google Cloud Storage buckets and objects in the Google Cloud Platform. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for Google Cloud Storage](../DataQuality/Google_Cloud_Storage_(Delimited_Files).md) to [Define Source](../DataQuality/Define_Source.md).

!!! note "Note"

    CSV is the ONLY supported data format.

Prerequisites

You must have the Google Cloud account and credentials.

Source Details for Google Cloud Storage

This topic provides properties and details needed to create a new connection and specify the source table using the Google Cloud Storage connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to Google Cloud Storage will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Name | Enter a unique name for the connection and click Continue. |
| Authentication Method | Choose one of the following:•Credentials File: To upload a file containing credentials.•Credentials Content: To paste credentials.This property is mandatory. |
| Credentials | The JSON credentials of the service account used to access the Cloud Storage service. The credentials file can be downloaded from the Cloud Storage console.**Note:**To define a connection, the concerned GCP account must have the permission for storage.buckets.list. Your credentials are authenticated successfully only if you have the permissions. |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Bucket | Specifies the name of the cloud storage bucket to access. This property is mandatory. |
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
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_57.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

Limitations: The Google Cloud Storage connector only supports authentication for Google service accounts. Authentication for Google end-user accounts and API keys is not supported.
