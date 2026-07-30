---
title: "Add a New Rule"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Add_a_New_Rule.htm"
canonical_id: "actian-data-platform-add-a-new-rule"
---

## Add a New Rule

!!! note "Note"

    Before reading this topic, ensure that you have read [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).

This option allows you to manually select and configure rules for a specific field. Before adding any rule, it’s a good idea to review the source data to understand which rules and associated parameters would be useful.

When editing an existing profile, the profile engine examines the existing rules against the schema of the source data set. If the schema has been altered and either the data type or field name from an existing profile rule cannot be resolved, an error will be displayed next to the rule. You will be prompted to either edit or remove the rule.

To add a new rule manually

1. On the Rules page, under Add your Rules here, click Add New Rule.

    The Add New Rules page is displayed. The top half of the page is used to select a field, profile rule, and profile parameters. The bottom half of the page displays the source data.

2. Click the Field dropdown and select the field name on which you would like to apply a rule.

    For example, if you want to create a rule to test for missing account numbers in the accnumber column, select the accnumber field name from the Fields dropdown.

3. Select a rule from the Rule Type dropdown. See [Rule and Parameter Reference](../DataQuality/Rule_and_Parameter_Reference.md).

!!! note "Note"

    Profile rules support specific data types. The rule type list is filtered to display appropriate rules based on the data type of the selected field.

    In the Rule Name field, a default rule name is provided. The rule name is a combination of the field name and the rule type. This value can be modified or overwritten. Rule names must contain only alphanumeric characters and underscore (_).

4. Based on the selected Rule Type, you may be required to specify Rule Parameters. See [Rule and Parameter Reference](../DataQuality/Rule_and_Parameter_Reference.md).

    You can perform the following actions with the source dataset:

| Options | Description |
| --- | --- |
| ![](images/Design_29.png) | Click this icon to search for a particular value. Contents will be filtered based on the search string. Click ![](images/Design_30.png) to close the search box. |
| ![](images/Design_31.png) | Click this icon to select the fields you wish to see in the table. This feature is useful when working with data sets with a large number of fields. |

5. Click Add Rules.

    The selected rules are added to your profile and focus is returned to the Rules page of the editor.

!!! note "Note"

    If the Source schema updated popup dialog opens, click Remove to delete the no longer valid rules and go to the Rules page (the Invalid rules removed popup confirms the number of rules removed). Or click Review to go to the Review and update invalid rules page. The NOT VALID message (![](images/Design_32.png)) appears next to each no longer valid rule. Click delete to remove a rule. Or select a rule, edit the Field, Rule Type, Parameters and Field Value as needed, click Update (the Rules updated popup confirms the number of rules updated), then click Continue.
