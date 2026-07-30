---
title: "Is Valid Ip4"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Is_Valid_Ip4.htm"
canonical_id: "actian-data-platform-is-valid-ip4"
---

## Is Valid Ip4

| Rule | IsValidIp4 |
| --- | --- |
| Default Rule Name | <fieldname>_IsValidIp4 |
| Description | Checks whether a string field value is a valid IPv4 address. Valid Ip4 addresses are written to the Pass Target. Invalid Ip4 addresses are written to the Fail Target. |
| Rule Parameters | None |
| Supported Data Types | String |
| Remarks | A valid Ip4 address must match the following regular java expression:^(?:(25[0-5]\|2[0-4][0-9]\|1[0-9][0-9]\|[1-9][0-9]\|[0-9])(\\.(?!$)\|$)){4}$ |
