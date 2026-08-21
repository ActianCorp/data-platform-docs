---
title: "Is Valid Social ID"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Is_Valid_Social_ID.htm"
canonical_id: "actian-data-platform-is-valid-social-id"
---

## Is Valid Social ID

| Rule | IsValidSocialID |
| --- | --- |
| Default Rule Name | <fieldname>_IsValidSocialID |
| Description | Checks whether a string field is a valid social ID. This metric will provide options to choose from. Default would be selected based on the locale. For example if locale is United States, then US social ID pattern would be selected.Valid social ID’s are written to the Pass Target. Invalid social ID’s are written to the Fail Target. |
| Rule Parameters | Country: Select from a list of countries. You can select from:<br>• Canada<br>• Germany<br>• India<br>• United Kingdom<br>• United StatesFor a description of social IDregular Java expressions options, see Remarks. |
| Supported Data Types | String |
| Remarks | Listed below are the regular Java expressions for valid social IDs:<br>• Canada: ^(\\d{3}-\\d{3}-\\d{3})\|(\\d{9})$<br>• Germany: ^[0-9]{2}[0-9]{2}[0,1][0-9][0-9]{2}[A-Z][0-9]{2}[0-9]$<br>• India: ^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$<br>• United Kingdom - ^([ACEHJLMOPRSW-Yacehjlmoprsw-y][A-CEGHJ-NPRSTW-Za-ceghj-nprstw-z]\|[Bb][A-CEHJ-NPRSTW-Za-cehj-nprstw-z]\|[Gg][ACEGHJ-NPRSTW-Zaceghj-nprstw-z]\|[Kk][A-CEGHJ-MPRSTW-Za-ceghj-mprstw-z]\|[Nn][A-CEGHJLMNPRSW-Za-ceghjlmnprsw-z]\|[Tt][A-CEGHJ-MPRSTW-Za-ceghj-mprstw-z]\|[Zz][A-CEGHJ-NPRSTW-Ya-ceghj-nprstw-y])[0-9]{6}[A-Da-d ]?$<br>• United States: ^[0-9]{3}-?[0-9]{2}-?[0-9]{4}$ |
