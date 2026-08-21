---
title: "Is Valid Phone Number"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Is_Valid_Phone_Number.htm"
canonical_id: "actian-data-platform-is-valid-phone-number"
---

## Is Valid Phone Number

| Rule | IsValidPhoneNumber |
| --- | --- |
| Default Rule Name | <fieldname>_IsValidPhoneNumber |
| Description | Checks whether a string field is a valid phone number. This metric will provide options to choose from. Default would be selected based on the locale. For example if locale is United States, then US phone number pattern would be selected.Valid phone numbers are written to the Pass Target. Invalid phone numbers are written to the Fail Target. |
| Rule Parameters | Phone Number Format: Select from a list of countries. You can select from:<br>• Canada<br>• Germany<br>• India<br>• United Kingdom<br>• United States |
| Supported Data Types | String |
| Remarks | Listed below are the regular Java expressions for valid phone numbers of specified countries:<br>• Canada: ^\\+?[01]?[- .]?\\(?[2-9]\\d{2}\\)?[- .]?\\d{3}[- .]?\\d{4}$<br>• Germany: ^(?:(\\+49\|0049\|\\+\\(49\\)\|\\(\\+49\\))?[ ()\\/-]*(?(1)\|0)1(?:5[12579]\|6[023489]\|7[0-9])\|(\\+43\|0043\|\\+\\(43\\)\|\\(\\+43\\))?[ ()\\/-]*(?(2)\|0)6(?:64\|(?:50\|6[0457]\|7[0678]\|8[0168]\|9[09])))[ ()\\/-]*\\d(?:[ \\/-]*\\d){6,7}\\s*$<br>• India: ^((0\|91\|\\+91)\\s*-?\\s*)?^[6-9][0-9]{9}$<br>• United Kingdom: ^((0\|44\|\\+44\|\\+44\\s*\\(0\\)\|\\+44\\s*0)\\s*)?7(\\s*[0-9]){9}$<br>• United States: ^[01]?[- .]?\\(?[2-9]\\d{2}\\)?[- .]?\\d{3}[- .]?\\d{4}$ |
