---
title: "Compare to Constant"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Compare_to_Constant.htm"
canonical_id: "actian-data-platform-compare-to-constant"
---

## Compare to Constant

| Rule | CompareToConstant |
| --- | --- |
| Default Rule Name | <fieldname>_CompareToConstant |
| Description | Compares a field against a constant value. After comparing the field values to the constant value, the values that are equal to the constant value are written to the Pass Target. Values that are not equal to the constant value are written to the Fail Target. |
| Rule Parameters | • Operator: Select from one of the following comparison operators:–Is Equal To–Is Not Equal To–Greater Than–Greater Than Or Equal To–Lesser Than–Lesser Than or Equal To<br>• **Field Value****:** In this text box, type the constant value to compare. For equal or not equal you can list one or more constants separated by a “\|” character. |
| Supported Data Types | String, Date, Timestamp, Boolean, Numeric, Double, Float, Long, Integer |
| Remarks | • The Is Equal To operator is not recommended to use on double or float field comparisons.<br>• Do not use quotation marks with string data.<br>• In case of date, datetime, and time field, the constant value should be in ISO 8601 format.<br>• If source has GMT timestamp data, the constant value should end with 'Z'. |
