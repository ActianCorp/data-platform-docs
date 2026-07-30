---
title: "Give Your Actian Warehouse Access to AWS Cloud Storage"
product: "Actian Data Platform"
guide: "Warehouse User Guide"
source_file: "Give_Your_Actian_Warehouse_Access_to_AWS_Cloud_S.htm"
canonical_id: "actian-data-platform-give-your-actian-warehouse-access-to-aws-cloud-s"
---

## Give Your Actian Warehouse Access to AWS Cloud Storage

The Actian Data Platform authenticates through AWS IAM access keys to read and ingest data from AWS S3 buckets. For more information, see [Set Up Amazon S3 Access](../User/Set_Up_Amazon_S3_Access.md).

!!! note "Note"

    This section applies only when loading data from external tables. It is not necessary when loading using [Loading Delimited Text Data Using COPY VWLOAD (SQL)](../DataLoading/Loading_Delimited_Text_Data_from_Cloud_Data_Stor.md).

To add the keys to your Actian warehouse

1. From the Actian warehouse list, click the name of the warehouse whose credentials you want to identify.

    The [Warehouse Details](../User/Warehouse_Details.md) page is displayed.

2. In the External Table Access row, click Set S3 Authentication.

    The External Table Access dialog appears.

3. Enter the AWS Access Key.

    This key and password are available from [Set Up Amazon S3 Access](../User/Set_Up_Amazon_S3_Access.md).

4. Enter the AWS Secret Key.
5. Click Save.

Your warehouse can now access S3 data in the cloud.

!!! note "Note"

    Depending on your loading method, setting S3 credentials may have no effect on an open connection, and you may need to disconnect and reconnect to the database to pick up the new credentials. Setting S3 credentials while loading is in progress may interrupt the loading operation.

After setting external table credentials, they should be applied to the warehouse within a minute.

Your warehouse can now access your AWS data in the cloud, and you may now run queries against the data source using the [Query Editor](../User/Part_QueryEditor.md).
