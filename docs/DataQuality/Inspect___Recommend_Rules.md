---
title: "Inspect & Recommend Rules"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Inspect___Recommend_Rules.htm"
canonical_id: "actian-data-platform-inspect-recommend-rules"
---

## Inspect & Recommend Rules

!!! note "Note"

    Before reading this topic, ensure that you have read [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).

This option uses internal algorithms that inspect the source data and recommend rules based on knowledge of the source schema and various data pattern matching tests. This is the fastest way to create a profile by quickly reviewing the recommended rules and keeping the ones that look meaningful for your profile.

When editing an existing profile, the profile engine examines the existing rules against the schema of the source data set. If the schema has been altered and either the data type or field name from an existing profile rule cannot be resolved, an error will be displayed next to the rule. You will be prompted to either edit or remove the rule.

To add a rule using Inspect & Recommend Rules

1. On the Rules page, click Inspect & Recommend Rules.

    The Select fields to recommend rules dialog is displayed.

2. Select each field for which you want recommended rules, or click Select All.

!!! note "Note"

    You can locate a particular field by entering a string in the Search field.

3. Click Confirm to start the inspection process.

!!! note "Note"

    During the inspection process, you can click Cancel to exit the process.

    After inspection the Select fields to recommend rules dialog closes automatically. The identified rules and their details are organized by field name in the order they appear in the dataset in the Add from recommended rules page.

4. Click an identified rule to view its details. The following information is displayed:

| Options | Description |
| --- | --- |
| Name | The name of the rule as applied to the particular field in your dataset. |
| Field | The field or column on which the rule is applied. |
| Base Rule | The name of the Data Quality rule which was used to create the rule applied to the particular field. |
| Description | A brief description about the rule. |

    Some profile rules have associated parameters, allowing users to specify specific values or conditions. See [Rule and Parameter Reference](../DataQuality/Rule_and_Parameter_Reference.md).

    You can perform the following actions with the source dataset:

| Options | Description |
| --- | --- |
| ![](images/Design_25.png) | Click this icon to search for a particular value. Contents will be filtered based on the search string. Click ![](images/Design_26.png) to close the search box. |
| ![](images/Design_27.png) | Click this icon to select the fields you wish to see in the table. This feature is useful when working with data sets with a large number of fields. |

5. Select the most appropriate rules to apply by clicking the check box that is displayed against the rule, or Select All to apply all recommended rules.
6. Click Add Rules.

    The selected rules are added to your profile and focus is returned to the Rules page of the editor.

!!! note "Note"

    If the Source schema updated popup dialog opens, click Remove to delete the no longer valid rules and go to the Rules page (the Invalid rules removed popup confirms the number of rules removed). Or click Review to go to the Review and update invalid rules page. The NOT VALID message (![](images/Design_28.png)) appears next to each no longer valid rule. Click delete to remove a rule. Or select a rule, edit the Field, Rule Type, Parameters and Field Value as needed, click Update (the Rules updated popup confirms the number of rules updated), then click Continue.
