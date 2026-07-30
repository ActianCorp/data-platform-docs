---
title: "Create a Rule Set"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Create_a_Rule_Set.htm"
canonical_id: "actian-data-platform-create-a-rule-set"
---

## Create a Rule Set

There are two ways you can add a rule set:

- From the Create **Rule Set**page which is described in this section.
- From the Rules page, when creating a data profile. See [Save Profile Rules as Rule Set](../DataQuality/Save_Profile_Rules_as_Rule_Set.md).

To create a new rule set

1. Click Data Quality, Rule Sets, Create Rule Set.

    The Create **Rule Set**page is displayed. It is a guided workflow that lets you create a new rule set by specifying the rule set details and defining the rules.

2. Provide a description for the rule set:

    - Name - Specify a unique name for your rule set.

    - Locale - Select a language (country) preference. Locale will help in validating and applying rules like [Is Valid Phone Number](../DataQuality/Is_Valid_Phone_Number.md), [Is Valid Social ID](../DataQuality/Is_Valid_Social_ID.md), and [Is Valid Zip Code](../DataQuality/Is_Valid_Zip_Code.md). If English (United States) locale is selected then United States phone number, social ID, zip code format will be used for validating. Default is English (United States). The available values are:

        - –English (Canada)

        - –English (Germany)

        - –English (India)

        - –English (United Kingdom)

        - –English (United States)

    - Description - (Optional) Add a description text for the rule set.

3. Click Continue.

    The Create Rule Set page is displayed. A blank new rule collection entry is displayed on this page, which you can edit to create a new rule collection.

4. Select a Data Type.

    You can choose from Bigint, Binary, Boolean, Date, Decimal, Double, Float, Integer, Smallint, String, Table, Time, Time Stamp,andTinyint. Based on the data type you select, a set of rules to choose from will appear. The data type also determines which fields the rule collection can be applied to.

5. Specify a Field Name Pattern.

    The field name pattern represents the specified value used to identify similarly named fields in the source dataset. To enable field name pattern matching, add an asterisk (*) as a wildcard before or after the field name pattern value. This allows for matching similar field names.

!!! note "Note"

    - A Rule Collection name is automatically generated based on the specified Data Type and Field Name Pattern. The format is <DataType>_<FieldNamePattern>.
    - The Field Name Patterns are case insensitive.

6. Select the Rules that you want to add to your Rule Collections.

    Depending on the selected Data Type, a set of rules is available for you to choose from. You may have to specify additional parameters for some of the rules. Click the rule name below to see the rule details.

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

7. Click Add.

    The new rule collection is added with the specified details.

!!! note "Note"

    A new blank rule collection is created using which you can add another collection of rules.

    You can also perform the following actions:

| Icon | Description |
| --- | --- |
| ![](images/Design_82.png) | This icon is displayed next to each rule collection. Click this to Delete the corresponding rule collection from rule set. |
| ![](images/Design_83.png) | Click this icon to view the selected list of rules for the selected rule collection. |

8. Click Save.

    The new Rule Set is added. You can edit the rule set later from the Edit Rule Set page. See [Edit a Rule Set](../DataQuality/Edit_a_Rule_Set.md).
