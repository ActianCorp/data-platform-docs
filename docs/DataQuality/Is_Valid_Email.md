---
title: "Is Valid Email"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Is_Valid_Email.htm"
canonical_id: "actian-data-platform-is-valid-email"
---

## Is Valid Email

| Rule | IsValidEmail |
| --- | --- |
| Default Rule Name | <fieldname>_IsValidEmail |
| Description | Checks whether a string field is a valid email address. Valid email addresses are written to the Pass Target. Invalid email addresses are written to the Fail Target. |
| Rule Parameters | None |
| Supported Data Types | String |
| Remarks | A valid email address must match the following regular java expression:^(([A-Za-z0-9]+_+)\|([A-Za-z0-9]+\\-+)\|([A-Za-z0-9]+\\.+)\|([A-Za-z0-9]+\\++))*[A-Za-z0-9]+@((\\w+\\-+)\|(\\w+\\.))*\\w{1,63}\\.[a-zA-Z]{2,6}$ |
