---
title: "Is Valid TimeStamp"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Is_Valid_TimeStamp.htm"
canonical_id: "actian-data-platform-is-valid-timestamp"
---

## Is Valid TimeStamp

| Rule | IsValidTimeStamp |
| --- | --- |
| Default Rule Name | <fieldname>_IsValidTimeStamp |
| Description | Compares the value from the source field with the selected time stamp format. This metric will provide a list of time stamp formats to choose from.Valid time stamps are written to the Pass Target. Invalid time stamps are written to the Fail Target. |
| Rule Parameters | **TimeStamp** **Format**: Select from one of the following time stamp formats:<br>• yyyy-MM-dd HH:mm:ss<br>• MM/dd/yyyy HH:mm<br>• MMM dd, yyyy HH:mm aa<br>• EEE, dd MMM yyyy HH:mm:ss Z<br>• MM-dd-yyyy hh:mm:ss a<br>• dd-MM-yyyy HH:mm:ss<br>• yyyy-MM-dd hh:mm:ss a |
| Supported Data Types | String |
| Remarks | None |
