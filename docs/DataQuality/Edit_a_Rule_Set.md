---
title: "Edit a Rule Set"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Edit_a_Rule_Set.htm"
canonical_id: "actian-data-platform-edit-a-rule-set"
---

## Edit a Rule Set

There are two ways you can edit a rule set:

- From the Rule Sets page.
- From the Rule Set Details page.

To edit a rule set

1. Click the Data Quality link at the top of the page and then click Rule Sets.

    The Rule Sets page displays the available rule sets.

2. Do one of the following:

    - Select the desired rule set by clicking the check box in the tile, then click ![](images/Design_96.png) in the menu that appears.

    - Click the tile of the desired rule set. The Rule Set Details page is displayed. Click Edit Rule Set.

    The Edit Rule Set page is displayed. By default the focus is on the Rules step. Navigation between pages is possible by using the Back and Continue buttons at the bottom of the page. When navigation to other pages is not possible, the button will fade in color and will not be active.

3. Click Back to go to the description step. If required you can edit the rule set description:

    - Name - The rule set name.

    - Locale - The language (country) preference. Locale will help in validating and applying rules like [Is Valid Phone Number](../DataQuality/Is_Valid_Phone_Number.md), [Is Valid Social ID](../DataQuality/Is_Valid_Social_ID.md), and [Is Valid Zip Code](../DataQuality/Is_Valid_Zip_Code.md). If English (United States) locale is selected then United States phone number, social ID, zip code format will be used for validating. Default is English (United States). The available values are:

        - –English (Canada)

        - –English (Germany)

        - –English (India)

        - –English (United Kingdom)

        - –English (United States)

    - Description - (Optional) The description text for the rule set.

4. Click Continue.

    The rule collection entry is displayed on the Create Rule Set page, which you can edit.

5. Select a rule set collection to edit it or click Add to add a new rule set collection. You can add or edit the following information:

    - Data Type: You can choose from Bigint, Binary, Boolean, Date, Decimal, Double, Float, Integer, Smallint, String, Table, Time, Time Stamp,andTinyint. Based on the data type you select, a set of rules to choose from will appear. The data type also determines which fields the rule collection can be applied to.

    - Field Name Pattern: The field name pattern represents the specified value used to identify similarly named fields in the source dataset. To enable field name pattern matching, add an asterisk (*) as a wildcard before or after the field name pattern value. This allows for matching similar field names.

!!! note "Note"

    A Rule Collection name is automatically generated based on the specified Data Type and Field Name Pattern. The format is <DataType>_<FieldNamePattern>.

    - Rules: Depending on the selected Data Type, a set of rules is available for you to choose from. Select the check box that is displayed against the rule name to add the rule to Rule Collections. Un-check the check box to remove it. You may have to specify additional parameters for some of the rules. Click the rule name below to see the rule details.

        - –Bigint - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Boolean - [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Date - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Decimal - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Double - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Float - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Integer - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Smallint - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –String - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Blank](../DataQuality/Is_Not_Blank.md), [Is Not Duplicate](../DataQuality/Is_Not_Duplicate.md), [Is Not Null](../DataQuality/Is_Not_Null.md), [Is Numeric](../DataQuality/Is_Numeric.md), [Is Valid Date](../DataQuality/Is_Valid_Date.md), [Is Valid Email](../DataQuality/Is_Valid_Email.md), [Is Valid Ip4](../DataQuality/Is_Valid_Ip4.md), [Is Valid Phone Number](../DataQuality/Is_Valid_Phone_Number.md), [Is Valid Social ID](../DataQuality/Is_Valid_Social_ID.md), [Is Valid Time](../DataQuality/Is_Valid_Time.md), [Is Valid TimeStamp](../DataQuality/Is_Valid_TimeStamp.md), [Is Valid Zip Code](../DataQuality/Is_Valid_Zip_Code.md), [Matches Pattern](../DataQuality/Matches_Pattern.md).

        - –Time - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Time Stamp - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

        - –Tinyint - [Compare to Constant](../DataQuality/Compare_to_Constant.md), [Is Not Null](../DataQuality/Is_Not_Null.md), Value in Range.

    You can also perform the following actions:

| Icon | Description |
| --- | --- |
| ![](images/Design_97.png) | This icon is displayed next to each rule collection. Click this to Delete the corresponding rule collection from rule set. |
| ![](images/Design_98.png) | Click this icon to view the selected list of rules for the selected rule collection. |

6. Click Save to save the changes.

!!! warning "Important"

    **IMPORTANT!**The Cancel Editing the Rule Set dialog appears when attempting to navigate away from the Edit Rule Set page. From this dialog, you have two options: save the changes to the rule set and close the editor by clicking Save and Close, or return to the editor by clicking Continue Editing or the “X” button.
