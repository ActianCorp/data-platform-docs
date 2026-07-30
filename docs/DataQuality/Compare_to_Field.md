---
title: "Compare to Field"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Compare_to_Field.htm"
canonical_id: "actian-data-platform-compare-to-field"
---

## Compare to Field

| Rule | CompareToField |
| --- | --- |
| Default Rule Name | <fieldname>_CompareToField |
| Description | Compares a field value with another field value. After comparing the field value to another field value, the values that are equal to the field value are written to the Pass Target. Values that are not equal to the field value are written to the Fail Target. |
| Rule Parameters | •Operator: Select from one of the following comparison operators:–Is Equal To–Is Not Equal To–Greater Than–Greater Than Or Equal To–Lesser Than–Lesser Than or Equal To•**Compare Field****:** Select the required field to compare from the Compare Field drop-drown list. |
| Supported Data Types | String, Date, Timestamp, Boolean, Numeric, Double, Float, Long, Integer |
| Remarks | •The two fields must be of the same data type.•The Is Equal To operator is not recommended for use on double or float field comparisons. |
