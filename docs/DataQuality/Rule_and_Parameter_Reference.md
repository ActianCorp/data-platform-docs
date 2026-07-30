---
title: "Rule and Parameter Reference"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Rule_and_Parameter_Reference.htm"
canonical_id: "actian-data-platform-rule-and-parameter-reference"
---

## Rule and Parameter Reference

You can create profiling Rules of different types to identify data quality issues within a data set. Each profile rule contains one or more conditions, allowing you to evaluate data against those conditions. The records that adhere to the profiling rules are written to the “Pass Target” and the records that do not adhere to the profiling rules are written to the “Fail Target”. Since data is written into two separate files, each target can be consumed or processed in separate workflows once the profile has been run. For example, the data in the Pass Target, is considered “clean” and can be consumed immediately, the data in the Fail Target is considered “dirty” and can be routed separately for remediation.

!!! note "Note"

    If your data contains whitespaces, the rules may not work correctly as rules consider whitespace as a part of the data. Hence if a rule is not working as expected, check for whitespaces in the source data. You can workaround the problem with some of the rules by adding spaces to the values in the rule parameters.

Listed below are the different Rule Types:

- [Compare to Constant](../DataQuality/Compare_to_Constant.md)
- [Compare to Field](../DataQuality/Compare_to_Field.md)

- [Is Not Blank](../DataQuality/Is_Not_Blank.md)
- [Is Not Duplicate](../DataQuality/Is_Not_Duplicate.md)

- [Is Not Null](../DataQuality/Is_Not_Null.md)
- [Is Numeric](../DataQuality/Is_Numeric.md)

- [Is Valid Date](../DataQuality/Is_Valid_Date.md)
- [Is Valid Email](../DataQuality/Is_Valid_Email.md)

- [Is Valid Ip4](../DataQuality/Is_Valid_Ip4.md)
- [Is Valid Phone Number](../DataQuality/Is_Valid_Phone_Number.md)

- [Is Valid Social ID](../DataQuality/Is_Valid_Social_ID.md)
- [Is Valid Time](../DataQuality/Is_Valid_Time.md)

- [Is Valid TimeStamp](../DataQuality/Is_Valid_TimeStamp.md)
- [Is Valid Zip Code](../DataQuality/Is_Valid_Zip_Code.md)

- [Is Within Range](../DataQuality/Is_Within_Range.md)
- [Matches Pattern](../DataQuality/Matches_Pattern.md)
