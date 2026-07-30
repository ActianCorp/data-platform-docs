---
title: "Amazon S3"
product: "Actian Data Platform"
guide: "Integrations Guide"
source_file: "Amazon_S3.htm"
canonical_id: "actian-data-platform-amazon-s3"
---

## Amazon S3

With the Amazon S3 or Amazon Simple Storage Service connector, a user can access S3 buckets to read the stored data.

- [Prerequisites](../Integrations/Amazon_S3.md)
- [Connection Details](../Integrations/Amazon_S3.md)

- [Source Details](../Integrations/Amazon_S3.md)
- [Additional Information](../Integrations/Amazon_S3.md)

Prerequisites

You must have the AWS account access and credentials and an IAM user created in AWS account.

Connection Details

Specify the following details to define a connection:

| Property | Description |
| --- | --- |
| Access key | Specifies the AWS access key for the IAM user for the connection. This access key is used to sign programmatic requests to AWS API calls through the connector. This is a mandatory property. |
| Secret key | Specifies the AWS secret key for the IAM user for the connection. This is a mandatory property. |
| Endpoint | (Optional) Specifies the endpoint name of a storage services to connect and access the S3 or S3 compatible buckets by the Amazon S3 connector. If not specified, the Amazon S3 connector connects to the Amazon S3 Service endpoint based on the region specified.**Note:**To access an S3 compatible bucket hosted by an object storage service other than the default Amazon S3 service, Endpoint option must be specified. Region option is optional.**Note:**If you are creating an Amazon S3 connection for use with Actian Data Profiler, specify the Region property to define the connection rather than the Endpoint property. |
| Region | Specifies the name to connect to an AWS region for the IAM user account. For example, US_EAST_1. This is a mandatory property.**Note:**The AWS denotes every geographic region by a region-code. |

Source Details

Specify the following source details:

| Property | Description |
| --- | --- |
| Bucket name | Specifies the bucket name. This is a mandatory property. |
| Folder name | (Optional) Specifies the folder name under the specified bucket. |
| Key | Specifies the key identifier (object name) of the object to retrieve. This is a mandatory property. |
| Read Chunk Size (Bytes) | (Optional) Specifies the size of chunks, in bytes, in which to retrieve data from the source object. When the property is not specified, or is set to a non-positive value, the entire object data is retrieved in a single chunk. |
| Data Format | Specifies the data format. This is a mandatory property. Select one of the following as per the data format type:•CSV:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Quote: Specifies the quote character. Default value is ".–Delimiter: Specifies the field delimiter character. Default value is ,.–Escape: Specifies the escape character.–Separator: Specifies the row separator characters. Default value is \r\n.–Character Set: Specifies the character set of the data. Default value is UTF-8.–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.•Excel:The following properties must be configured:–Header: If enabled, specifies whether the CSV data contains a header row.–Worksheet Index: Specifies the index of the worksheet. The index of the first worksheet is 1(default).–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.•Avro:The following properties must be configured:–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the AVRO data you wish to map to tables in the target.•Parquet•JSON:The following properties must be configured:–Find Array: If enabled, specifies that the output will iterate on the first array found in the JSON document.–Array Path: Specifies the path of the JSON array within the document. Omit if the document is an array. For example,"/resources".–Sample Size: Specifies the number of records to analyze when determining the data structure. Default value is 100.–Select Source Tables: Select which arrays of objects in the JSON data you wish to map to tables in the target. |
| Limit | (Optional) Specifies the maximum number of records to return. |
| Batch Size | (Optional) Specifies the number of records to return per batch. |

Additional Information

None
