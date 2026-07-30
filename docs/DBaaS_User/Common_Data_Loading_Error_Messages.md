---
title: "Common Data Loading Error Messages"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Common_Data_Loading_Error_Messages.htm"
canonical_id: "actian-data-platform-common-data-loading-error-messages"
---

## Common Data Loading Error Messages

Loading data into Actian Actian involves the following steps:

1. Creating the external table that references data on your data store.
2. Creating the native Actian table.

3. Inserting data from the external table reference to the native Actian table.
4. Creating stats on the Actian table to increase performance.

Getting everything correct in these steps can be challenging, since the schema and data need to match exactly. Creating the external table sometimes results in issues during the loading step. The following examples list some of the error messages you may encounter.

SQL Error [2014] [42000]

SQL Error [2014] [42000]: CREATE or ALTER TABLE: invalid column format 'integerr' on column 'c_custkey'.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGERR,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Invalid data type. Datatype “INTEGERR” is misspelled. Correct the datatype to “INTEGER”.

SQL Error [3809] [42000]

SQL Error [3809] [42000]: Line 3, syntax error on 'c_name'. The correct syntax is:
CREATE EXTERNAL TABLE table_name
( column_name col_type
{, ... }
)
USING [schema.]provider_name
WITH REFERENCE = 'reference-value'
[,FORMAT = 'format-value']
[,EXTERNAL_ROLE = 'external-role']
[,OPTIONS = ('key'= 'value' {,'key'= 'value'})]
[,ROWS = integer_value ]

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Invalid format (without comma). Insert comma after “INTEGER” on line 2.

SQL Error [1315347] [5000A] – Example 1

SQL Error [1315347] [5000A]: External table provider reported an error 'java.io.FileNotFoundException: Bucket some-junk-path does not exist'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 56, transaction id 668.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Invalid bucket location (last 2 lines). Enter a valid path to the S3 bucket.

SQL Error [1315347] [5000A] – Example 2

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: Path does not exist: s3a://<bucket_name>/customers.tbl*;'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 74, transaction id 676.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customers.tbl*',format='csv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Invalid reference path. Correct the path.

SQL Error [1315347] [5000A] – Example 3

SQL Error [1315347] [5000A]: External table provider reported an error 'java.lang.ClassNotFoundException: Failed to find data source: csvv. Please find packages at http://spark.apache.org/third-party-projects.html, caused by: java.lang.ClassNotFoundException: csvv.DefaultSource'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 116, transaction id 698.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csvv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Invalid format. Correct ‘csvv’ to ‘csv’ on the last line.

SQL Error [1315347] [5000A] – Example 4

SQL Error [1315347] [5000A]: External table provider reported an error 'java.lang.Exception: header flag can be true or false'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 134, transaction id 706.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='truee','delimiter'='|');
```

Reason and correction:

Invalid header flag. Correct ‘truee’ to ‘true’ on the last line.

SQL Error [1315347] [5000A] – Example 5

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`c_custkey`' given input columns: [src_5._c4, src_5._c0, src_5._c5, src_5._c6, src_5._c2, src_5._c3, src_5._c1, src_5._c7]; line 1 pos 41;
'InsertIntoTable 'UnresolvedRelation `customer_s3_6`, false, false
+- 'Project ['c_custkey, 'c_name, 'c_address, 'c_nationkey, 'c_phone, 'c_acctbal, 'c_mktsegment, 'c_comment]
+- SubqueryAlias src_5
+- Relation[_c0#166,_c1#167,_c2#168,_c3#169,_c4#170,_c5#171,_c6#172,_c7#173] csv'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 150, transaction id 713.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('heade'='true','delimiter'='|');
```

Reason and correction:

Invalid header field. Correct ‘heade’ to ‘header’ on last line.

SQL Error [1315347] [5000A] – Example 6

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`c_custkey`' given input columns: [src_7.c_custkey|c_name|c_address|c_nationkey|c_phone|c_acctbal|c_mktsegment|c_comment]; line 1 pos 41;
'InsertIntoTable 'UnresolvedRelation `customer_s3_8`, false, false
+- 'Project ['c_custkey, 'c_name, 'c_address, 'c_nationkey, 'c_phone, 'c_acctbal, 'c_mktsegment, 'c_comment]
+- SubqueryAlias src_7
+- Relation[c_custkey|c_name|c_address|c_nationkey|c_phone|c_acctbal|c_mktsegment|c_comment#208] csv'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 166, transaction id 720.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='true','delimiter'='!');
```

Reason and correction:

Invalid delimiter. Enter a valid delimiter character on the last line.

SQL Error [1315347] [5000A] – Example 7

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`c_custkey`' given input columns: [src_9.c_custkey|c_name|c_address|c_nationkey|c_phone|c_acctbal|c_mktsegment|c_comment]; line 1 pos 42;
'InsertIntoTable 'UnresolvedRelation `customer_s3_10`, false, false
+- 'Project ['c_custkey, 'c_name, 'c_address, 'c_nationkey, 'c_phone, 'c_acctbal, 'c_mktsegment, 'c_comment]
+- SubqueryAlias src_9
+- Relation[c_custkey|c_name|c_address|c_nationkey|c_phone|c_acctbal|c_mktsegment|c_comment#236] csv'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 184, transaction id 728.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='true','delimite'='|');
```

Reason and correction:

Invalid delimiter field name. Correct ‘delimite’ to ‘delimiter’ on last line.

SQL Error [1315347] [5000A] – Example 8

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`c_custkeyy`' given input columns: [src_11.c_name, src_11.c_comment, src_11.c_address, src_11.c_custkey, src_11.c_nationkey, src_11.c_mktsegment, src_11.c_phone, src_11.c_acctbal]; line 1 pos 42;
'InsertIntoTable 'UnresolvedRelation `customer_s3_12`, false, false
+- 'Project ['c_custkeyy, c_name#265, c_address#266, c_nationkey#267, c_phone#268, c_acctbal#269, c_mktsegment#270, c_comment#271]
+- SubqueryAlias src_11
+- Relation[c_custkey#264,c_name#265,c_address#266,c_nationkey#267,c_phone#268,c_acctbal#269,c_mktsegment#270,c_comment#271] csv'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 208, transaction id 739.

Code:

```
create external table customer_s3 (
```

```
c_custkeyy INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Spark schema mapping not correctly. Ensure declared column name (c_custkey) matches schema.

SQL Error [1315347] [5000A] – Example 9

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`c_custkey`' given input columns: [src_15._c0, src_15._c1, src_15._c3, src_15._c6, src_15._c5, src_15._c7, src_15._c4, src_15._c2]; line 1 pos 42;
'InsertIntoTable 'UnresolvedRelation `customer_s3_16`, false, false
+- 'Project ['c_custkey, 'c_name, 'c_address, 'c_nationkey, 'c_phone, 'c_acctbal, 'c_mktsegment, 'c_comment]
+- SubqueryAlias src_15
+- Relation[_c0#348,_c1#349,_c2#350,_c3#351,_c4#352,_c5#353,_c6#354,_c7#355] csv'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 244, transaction id 755.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='false','delimiter'='|');
```

Reason and correction:

Data has a header but ‘false’ was provided in the query. Change to ‘true’.

SQL Error [1315347] [5000A] – Example 10

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.hadoop.fs.s3a.AWSS3IOException: getFileStatus on s3a://<bucket_name>/customer.tbl.1.csv: com.amazonaws.services.s3.model.AmazonS3Exception: Moved Permanently (Service: Amazon S3; Status Code: 301; Error Code: 301 Moved Permanently; Request ID: 440D084ADDE1572A), S3 Extended Request ID: EcLrXaYP1ndNXFuc/GWkfSqR+ZYXARPvJEh4ipOWxRvyI2Rr9RVG8XKt4cS9qVp4KTGQxU53ZcY=: Moved Permanently (Service: Amazon S3; Status Code: 301; Error Code: 301 Moved Permanently; Request ID: 440D084ADDE1572A), caused by: com.amazonaws.services.s3.model.AmazonS3Exception: Moved Permanently (Service: Amazon S3; Status Code: 301; Error Code: 301 Moved Permanently; Request ID: 440D084ADDE1572A), S3 Extended Request ID: EcLrXaYP1ndNXFuc/GWkfSqR+ZYXARPvJEh4ipOWxRvyI2Rr9RVG8XKt4cS9qVp4KTGQxU53ZcY='. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 28, transaction id 650.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl.1.csv',format='csv',options=('header'='false','delimiter'='|');
```

Reason and correction:

S3 permissions are not set for the warehouse. Set S3 permissions. See Set Up Access Credentials for Cloud Storage Accounts.

SQL Error [1315347] [5000A] – Example 11

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.hadoop.fs.s3a.AWSS3IOException: getFileStatus on s3a://<bucket_name>/customer.tbl.1.csv: com.amazonaws.services.s3.model.AmazonS3Exception: Moved Permanently (Service: Amazon S3; Status Code: 301; Error Code: 301 Moved Permanently; Request ID: A041E8FB17D5E97A), S3 Extended Request ID: VR/YlHG0Yqmc+HeeZgTVWFaadmeGfcTrGxtAU1N4RdFjp/XNGhjkb3SFY09530VNf5ryUPEf+hM=: Moved Permanently (Service: Amazon S3; Status Code: 301; Error Code: 301 Moved Permanently; Request ID: A041E8FB17D5E97A), caused by: com.amazonaws.services.s3.model.AmazonS3Exception: Moved Permanently (Service: Amazon S3; Status Code: 301; Error Code: 301 Moved Permanently; Request ID: A041E8FB17D5E97A), S3 Extended Request ID: VR/YlHG0Yqmc+HeeZgTVWFaadmeGfcTrGxtAU1N4RdFjp/XNGhjkb3SFY09530VNf5ryUPEf+hM='. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 70, transaction id 667

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl.1.csv',format='csv',options=('header'='false','delimiter'='|');
```

Reason and correction:

The warehouse is in N.Virginia but data is being loaded from Ohio region

SQL Error [1315347] [5000A] – Example 12

SQL Error [1315347] [5000A]: External table provider reported an error 'java.nio.file.AccessDeniedException: : getFileStatus on : com.amazonaws.services.s3.model.AmazonS3Exception: Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: 87559381F3F15DA7), S3 Extended Request ID: hSfwo/ABeykNkjcpB+Rz0DcXiHDN5qI5z4ELP94hSNEnqUVHbAx9xdvKP+STq5R4IqTvskwr6KM=, caused by: com.amazonaws.services.s3.model.AmazonS3Exception: Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: 87559381F3F15DA7), S3 Extended Request ID: hSfwo/ABeykNkjcpB+Rz0DcXiHDN5qI5z4ELP94hSNEnqUVHbAx9xdvKP+STq5R4IqTvskwr6KM='. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 310, transaction id 785.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl*',format='csv',options=('header'='false','delimiter'='|');
```

Reason and correction:

S3 is set with a different environment’s credentials. Use the correct credentials.

SQL Error [1315347] [5000A] – Example 13

SQL Error [1315347] [5000A]: External table provider reported an error 'org.apache.spark.sql.AnalysisException: cannot resolve '`c_custkey`' given input columns: [src_1.1 Customer#000000001 j5JsirBM9PsCy0O1m 15 25-989-741-2988 711.56 BUILDING "regular, regular platelets are fluffily according to the even attainments. blithely iron"]; line 1 pos 41;
'InsertIntoTable 'UnresolvedRelation `customer_s3_2`, false, false
+- 'Project ['c_custkey, 'c_name, 'c_address, 'c_nationkey, 'c_phone, 'c_acctbal, 'c_mktsegment, 'c_comment]
+- SubqueryAlias src_1
+- Relation[1 Customer#000000001 j5JsirBM9PsCy0O1m 15 25-989-741-2988 711.56 BUILDING "regular, regular platelets are fluffily according to the even attainments. blithely iron"#10] csv'. For more information: check ${II_SYSTEM}/ingres/files/spark_provider.log, query id 346, transaction id 801.

Code:

```
create external table customer_s3 (
```

```
c_custkey INTEGER,
```

```
c_name VARCHAR(25),
```

```
c_address VARCHAR(40),
```

```
c_nationkey INTEGER,
```

```
c_phone CHAR(15),
```

```
c_acctbal DECIMAL(18,2),
```

```
c_mktsegment CHAR(10),
```

```
c_comment VARCHAR(117)
```

```
) using spark with reference='s3a://<bucket_name>/customer.tbl.1',format='csv',options=('header'='true','delimiter'='|');
```

Reason and correction:

Header is set to “true” when data has no header. Set header to ‘false’.
