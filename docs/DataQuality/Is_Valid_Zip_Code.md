---
title: "Is Valid Zip Code"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Is_Valid_Zip_Code.htm"
canonical_id: "actian-data-platform-is-valid-zip-code"
---

## Is Valid Zip Code

| Rule | IsValidZipCode |
| --- | --- |
| Default Rule Name | <fieldname>_IsValidZipCode |
| Description | Checks whether a string field is a valid zip code. This metric will provide options to choose from. Default would be selected based on the locale. For example if locale is United States, then US zip code pattern would be selected.Valid zip codes are written to the Pass Target. Invalid zip codes are written to the Fail Target. |
| Rule Parameters | Zip Code Format: Select from a list of countries. You can select from:<br>• Canada<br>• Germany<br>• India<br>• United Kingdom<br>• United StatesFor a description of Zip Code Format options, see Remarks. |
| Supported Data Types | String |
| Remarks | Listed below are the regular Java expressions for valid zip code:<br>• Canada: ^([A-Za-z]\\d[A-Za-z][\\s-]?\\d[A-Za-z]\\d)<br>• Germany: ^[0-9]{5}$<br>• India: ^[0-9]{6}$<br>• United Kingdom: ^([Gg][Ii][Rr] 0[Aa]{2})\|((([A-Za-z][0-9]{1,2})\|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})\|(([A-Za-z][0-9][A-Za-z])\|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$<br>• United States: ^[0-9]{5}(-[0-9]{4})?$ |
