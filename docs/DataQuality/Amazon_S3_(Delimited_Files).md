---
title: "Amazon S3 (Delimited Files)"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Amazon_S3_(Delimited_Files).htm"
canonical_id: "actian-data-platform-amazon-s3-delimited-files"
---

## Amazon S3 (Delimited Files)

This topic describes Amazon S3 (Amazon Simple Storage Service) connector properties and connection details for reading data from Amazon S3 buckets. If you’re [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md) or [Creating a Connection](../DataQuality/Creating_a_Connection.md), see [Source Details for Amazon S3](../DataQuality/Amazon_S3_(Delimited_Files).md) to [Define Source](../DataQuality/Define_Source.md).

- [Prerequisites](../DataQuality/Amazon_S3_(Delimited_Files).md)
- [Source Details for Amazon S3](../DataQuality/Amazon_S3_(Delimited_Files).md)

- [Additional Information](../DataQuality/Amazon_S3_(Delimited_Files).md)

!!! note "Note"

    - CSV is the ONLY supported data format.
    - To create an Amazon S3 connection for use with Actian Data Profiler, specify the Region property to define the connection rather than the Endpoint property.

Prerequisites

You must have the AWS account access and credentials and an IAM user created in AWS account.

Source Details for Amazon S3

This topic provides properties and details needed to create a new connection and specify the source table using the Amazon S3 connector, as well as other options that are presented when you [Define Source](../DataQuality/Define_Source.md).

When finished entering this information your connection to Amazon S3 will be established. You will then be guided to the next Step in [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md): [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).

Specify the following details to define a new connection:

| Option | Description |
| --- | --- |
| Name | Enter a unique name for the connection and click Continue. |
| Access key | Specifies the AWS access key for the IAM user for the connection. This access key is used to sign programmatic requests to AWS API calls through the connector. This property is mandatory. |
| Secret key | Specifies the AWS secret key for the IAM user for the connection. This property is mandatory. |
| Region | Select an AWS region for the IAM user account. For example, US_EAST_1. This property is mandatory.**Note:**The AWS denotes every geographic region by a region-code. |
| Test | Click to verify your connection, then click Save. |

Specify the following details to define the source on the new connection:

| Option | Description |
| --- | --- |
| Test Credentials | Click to verify your connection. A “Connection successful” message is returned when the connection is successful. An error message is returned when the connection attempt fails. |
| Bucket name | Specifies the bucket name. This property is mandatory. |
| Folder name | (Optional) Specifies the folder name under the specified bucket. |
| Key | Specifies the key identifier (object name) of the object to retrieve. This property is mandatory. |
| Header | (Optional) Specifies whether a comma separated lists of values (CSV data) contains a header row. Enable to include a header row. Disable to exclude one. This property is disabled by default. |
| Quote | (Optional) Specifies the quote character. Default value is ". |
| Delimiter | (Optional) Specifies the field delimiter character. Default value is ,. |
| Escape | (Optional) Specifies the escape character. This property is empty by default. |
| Separator | (Optional) Specifies the row separator characters. Default value is \r\n. |
| Character Set | (Optional) Specifies the character set of the data. Default value is UTF-8. |
| Limit | (Optional) Specifies the maximum number of records to return. This property is empty by default. |
| Sample Size | (Optional) Specifies the number of records to analyze when determining the data structure. Default value is 5000. |
| Read Chunk Size (Bytes) | (Optional) Specifies the size of chunks, in bytes, in which to retrieve data from the source object. When the property is not specified, or is set to a non-positive value, the entire object data is retrieved in a single chunk. Default value is 5000000. |
| Preview the first 20 records | Click to preview the first 20 records. Use this to verify that you’re connected to the correct table.Data for the selected source table is displayed in the source data preview pane.Click ![](images/Design_55.png) and enter a string to search for a particular record. |
| Continue | Click when you have finished entering source definitions. The Rules page opens.If you are in the process of creating a Data Profile, proceed to [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md).If you are in the process of creating connection, return to [Creating a Connection](../DataQuality/Creating_a_Connection.md). |

Additional Information

None
