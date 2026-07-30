---
title: "Rule Sets"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Rule_Sets.htm"
canonical_id: "actian-data-platform-rule-sets"
---

## Rule Sets

The rule set editor allows users to create, save, and reuse data profile rules. Rules contained within a rule set are stored in collections which are organized based on the data type and the field name pattern.

The saved rules within a rule set can be quickly added to a profile and conversely, existing rules within a profile can be saved to a rule set. When you add rules from a rule set to a profile, a copy of the rule is created and added to the profile. This enables you to modify the rules within the profile without affecting the original rule in the rule set.

When adding a rule within a rule set, the user must specify both a data type and a corresponding field name pattern. There is a structured association between data types and profile rules. Each data type is supported by a distinct subset of profile rules, ensuring that the application of rules remains contextually appropriate. For instance, a rule designed for date data types is restricted from being applied to numeric fields. This behavior ensures that each rule is applied only to the data types for which it was specifically designed, enhancing the accuracy and reliability of rule set rules.

Some key concepts related to rule sets are:

- A rule set consists of one or more collection of rules.
- Each rule collection contains a group of rules relevant to a specific Data Type and Field Name Pattern. Thus a rule collection can be applied to fields of a specified data type with names that match a specified named pattern.

- The Field Name Pattern represents the specified value used to identify similarly named fields in the source dataset. Field name patterns allow for wildcard matching using the asterisk (*) character. This feature is particularly useful when reusing profile rules through a rule set, as it allows a single rule to match multiple similar fields (for example, *name will match first name, middle name, last name) when applying the rule set rules to a profile. The field name patterns are case insensitive.

Note that rules that are added in a rule set operate differently from rules that are added in a profile. When you add a rule within a profile the rule resides in that profile, and is associated with a particular field of a connected data source. Whereas when you add a rule in a rule set, the rule is not part of any profile, nor is it associated with any particular field of a connected data source. Instead, the rule set rules are associated with a Data Type and Field Name Pattern that you specify.

Topics:

- [Create a Rule Set](../DataQuality/Create_a_Rule_Set.md)
- [Search a Rule Set](../DataQuality/Search_a_Rule_Set.md)

- [View Rule Set Details](../DataQuality/View_Rule_Set_Details.md)
- [Edit a Rule Set](../DataQuality/Edit_a_Rule_Set.md)

- [Delete a Rule Set](../DataQuality/Delete_a_Rule_Set.md)

See Also:

- [Add Rule from Rule Set](../DataQuality/Add_Rule_from_Rule_Set.md)
- [Save Profile Rules as Rule Set](../DataQuality/Save_Profile_Rules_as_Rule_Set.md)
