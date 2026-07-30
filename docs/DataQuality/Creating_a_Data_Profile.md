---
title: "Creating a Data Profile"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Creating_a_Data_Profile.htm"
canonical_id: "actian-data-platform-creating-a-data-profile"
---

## Creating a Data Profile

Data profiling is an essential component of any data processing workflow. It provides the insight needed to significantly mitigate the negative effects of low-quality data on an organization's decisions, revenue, and actions. This process boosts the efficacy of various data-related activities, including integration, cataloging, procurement, analytics, and artificial intelligence, by defining, enforcing, and validating data accuracy and consistency.

During the profiling process, data is evaluated based on its adherence to the conditions and values provided within the profile rules. These rules help define data quality and enforce the recognized dimensions of data quality: accuracy, completeness, consistency, timeliness, validity, and uniqueness. Once complete, the results of the profile can offer insight into the type, and volume, of data quality issues found within a given dataset. During execution, Data Profiler writes data to two separate targets: Pass and Fail. Data that meets the criteria within the profile rules is written to the Pass target and data that does not meet that criteria is written to the Fail target. This bifurcation allows the immediate processing of the data in the Pass target, while the Fail target data can be routed for remediation.

A new data profile can be created by following the steps in our data profile editor. The steps include:

1. Description – Name your data profile.
2. Source – Provide the source connection details.

3. Rules – Define rules and analyze results for your profile.
4. Targets - Provide the target connection details.

5. Results – View the results.

Navigation between pages of the guided workflow is possible by using the Back and Continue buttons at the bottom of the page. Navigating between pages will not clear data that has been entered by the user. When navigation to other pages is not possible, the button will fade in color and will not be active. You can exit the process anytime without saving any information by clicking Cancel.

To create a new data profile

1. Click Data Quality, Data Profiles, Create Data Profile.

    The Create **Data Profile**page is displayed. It is a guided workflow that lets you create a new data profile by specifying the source and target connection details and defining the rules.

2. Provide a description for the data profile (see [Describe Data Profile](../DataQuality/Describe_Data_Profile.md)) and click Continue.

    The Source page is displayed.

3. Define the Source connection (see [Define Source](../DataQuality/Define_Source.md)) and click Continue.

    The Rules page is displayed.

4. Add and apply Rules. For more information see one of the following topics:

    - [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md)

    - [Inspect & Recommend Rules](../DataQuality/Inspect___Recommend_Rules.md)

    - [Add a New Rule](../DataQuality/Add_a_New_Rule.md)

    - [Add Rule from Rule Set](../DataQuality/Add_Rule_from_Rule_Set.md)

5. Click Continue.

    The Targets page is displayed.

!!! note "Note"

    The Continue button will not be enabled until you add and apply Rules.

6. Define Pass and Fail Target connections (see [Define Targets](../DataQuality/Define_Targets.md)).
7. Click Continue & Run (see [Results](../DataQuality/Results.md)).

    The profile is executed, the Pass/Fail data is written to the Targets, and the Results page is displayed. Drilldown reporting provides multiple different views of the Pass/Fail target data.

!!! note "Note"

    Inaccurate source field lengths are common with delimited files. In such cases, the creation of profile jobs may fail with a The string supplied is too long to fit into the resulting string type error. To prevent this, adjust the sample size on the source page to a higher number so that more records are considered to calculate the target field size.

8. You can now perform one of the following actions:

| Actions | Description |
| --- | --- |
| Save & Schedule | Click this save the data profile and open the [Edit Profile Schedule](../DataQuality/Edit_Profile_Schedule.md) page. From this page you can create a schedule for profile execution.**Note:**Once the profile is scheduled an associated configuration will be created. Changes made to the profile after that are not updated in the configuration. To update the configuration, recreate and schedule the profile. |
| Save & Close | Click this to save and close the data profile. Focus is directed back to the Data Profiles page. Use this option if you have incomplete work and want to resume working later. You can search, view, and edit the profile from the Data Profiles page and edit it later. See [Search Data Profiles](../DataQuality/Search_Data_Profiles.md). |

!!! warning "Important"

    **IMPORTANT!**The Cancel the Data Profile Creation dialog appears when attempting to navigate away from any profile creation page. From this dialog, you have three options: discard the profile being created by clicking Discard, save it as a draft by clicking Save as Draft, or return to the editor by clicking the “X” button. Save as Draft is useful if you have incomplete work and want to resume working later. You can edit the profile later from the Edit Data Profile page. See [Edit a Profile](../DataQuality/Edit_a_Profile.md).
