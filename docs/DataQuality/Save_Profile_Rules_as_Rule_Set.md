---
title: "Save Profile Rules as Rule Set"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Save_Profile_Rules_as_Rule_Set.htm"
canonical_id: "actian-data-platform-save-profile-rules-as-rule-set"
---

## Save Profile Rules as Rule Set

Rule sets can be created while designing or editing a profile, from the Save as Rule Set page. When saving rules from a profile, the rule set is organized based on data type and field name. If multiple saved rules were configured against the same field in the profile, they will be saved as a collection, or group, within the rule set and will be given a default name of <DataType_FieldName> (example: string_AccountNumber). If desired, the parameters for each profile rule can be edited within the Save as Rule Set page. This process creates a copy of the rules from the profile which means they can be modified within the rule set editor without impacting the original rules or profile.

The rule set created from the Save as Rule Set page is displayed on the Data Quality, Design, Rule Sets page. Rule set rules are different from the profile rules in the way that when you add a rule within a profile the rule resides in that profile, and is associated with a particular field of a connected data source. Whereas when you save a rule as a rule set, the rule is not a part of any profile, nor is it associated with any particular field of a connected data source. Instead, the rule set rules are associated with a Data Type and Field Name Pattern.

The Field Name Pattern represents the specified value used to identify similarly named fields in the source dataset. Field name patterns allow for wildcard matching using the asterisk (*) character. This feature is particularly useful when reusing profile rules through a rule set, as it allows a single rule to match multiple similar fields (for example, *name will match first name, middle name, last name) when applying the rule set rules to a profile.

See also:

- [Rule Sets](../DataQuality/Rule_Sets.md)
- [Add Rule from Rule Set](../DataQuality/Add_Rule_from_Rule_Set.md)

To save profile rules as a rule set

1. When creating (see [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md)) or editing (see [Edit a Profile](../DataQuality/Edit_a_Profile.md)) a data profile, on the Rules page, click the check box that is displayed next to the rules to select the rules that you want to include in your rule set.
2. Click ![](images/Design_80.png) in the menu that appears.

    The system automatically assigns a rule set name, description, data type, and field name pattern.

    Rules are grouped by data type and field name. The rule collection name is automatically assigned and cannot be edited, following the format <DataType>_<FieldNamePattern>. The data type of the rule collection also determines which fields it can be applied to.

    The rule set name and field name pattern can be edited. Additionally, each rule must be selected using checkbox and the parameters can be edited if desired (see [Rule and Parameter Reference](../DataQuality/Rule_and_Parameter_Reference.md)). By default the parameters contain the same values as the profile rules.

3. You can select each DataType_FieldName collection to display the associated rules. You can edit the following rule collection information:

    - Rule Set Name and Description.

    - Field Name Pattern - The field name pattern represents the specified value used to identify similarly named fields in the source dataset. Field name patterns allow for wildcard matching using the asterisk (*) character. This feature is particularly useful when reusing profile rules through a rule set, as it allows a single rule to match multiple similar fields (for example, *name will match first name, middle name, last name) when applying the rule set rules to a profile. The field name patterns are case insensitive.

4. For each rule collection, select the rules that you want to add to your rule collection. Depending on the data type, a set of rules is available for you to choose from. You may have to specify additional parameters for some of the rules. Click the rule name below to see the rule details.

    - Bigint - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Boolean - [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Date - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Decimal - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Double - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Float - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Integer - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Smallint - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - String - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Blank](../DataQuality/Is_Not_Blank.md), [Is Not Duplicate](../DataQuality/Is_Not_Duplicate.md), [Is Not Null](../DataQuality/Is_Not_Null.md), [Is Numeric](../DataQuality/Is_Numeric.md), [Is Valid Date](../DataQuality/Is_Valid_Date.md), [Is Valid Email](../DataQuality/Is_Valid_Email.md), [Is Valid Ip4](../DataQuality/Is_Valid_Ip4.md), [Is Valid Phone Number](../DataQuality/Is_Valid_Phone_Number.md), [Is Valid Social ID](../DataQuality/Is_Valid_Social_ID.md), [Is Valid Time](../DataQuality/Is_Valid_Time.md), [Is Valid TimeStamp](../DataQuality/Is_Valid_TimeStamp.md), [Is Valid Zip Code](../DataQuality/Is_Valid_Zip_Code.md), [Matches Pattern](../DataQuality/Matches_Pattern.md).

    - Time - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Time Stamp - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    - Tinyint - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

5. After editing the required information and configuring the rules, click Save as Rule Set.

    The new Rule Set is saved. You can view and edit the rule set later from the Edit Rule Set page. See [Edit a Rule Set](../DataQuality/Edit_a_Rule_Set.md).
