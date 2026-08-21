---
title: "Actian Data Profiling Release Notes"
product: "Actian Data Platform"
guide: "Welcome"
source_file: "Actian_Data_Profiling_Release_Notes.htm"
canonical_id: "actian-data-platform-actian-data-profiling-release-notes"
---

## Actian Data Profiling Release Notes

These Release Notes are for releases of Actian Data Quality on the Actian Data Platform.

| Actian Data Profiling Release Features | Release Date |
| --- | --- |
| • [Rule Sets](../DataQuality/Rule_Sets.md)<br>• Select All option for [Inspect & Recommend Rules](../DataQuality/Inspect___Recommend_Rules.md)<br>• Execute Profiles in background when you [Define Targets](../DataQuality/Define_Targets.md)<br>• Adjust sample size for data loading for [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md)<br>• Evaluate rules with new source details for [Inspect & Recommend Rules](../DataQuality/Inspect___Recommend_Rules.md) | October, 2024 |
| • [Define Source](../DataQuality/Define_Source.md)<br>• [Source and Target Connections](../DataQuality/Source_and_Target_Connections.md)<br>• [Define Rules and Analyze Results](../DataQuality/Define_Rules_and_Analyze_Results.md)<br>• [Run History for all Profiles](../DataQuality/Run_History_for_all_Profiles.md)<br>• [Managing Configurations](../DataQuality/Managing_Configurations.md)<br>• [Run History for all Configurations](../DataQuality/Run_History_for_all_Configurations.md) | May 11, 2024 |

Users can use rule sets, which is a method that allows managing data profiling rules by saving and reusing them. This feature includes the process of importing rules into a profile from a rule set and creating rule sets within a profile due to existing discrepancies and inconsistencies.

There is a Select All option for rule selection to enable users to select all rules at once during the process of creating a profile, when users define targets.

To improve data loading times, users can cancel and adjust the sample size of data.

The platform can evaluate rules with new source details and then notify users that rules are affected when a user changes the source.

To create a data profile you need to define a data source, define a connection to the data source, create data quality rules, and define a target. The data quality rules are set to enforce specific conditions or values. When a rule applies to a specific field in a profile, the data in that field is evaluated against the condition or value within the rule. After processing is complete, each value from the source field is either valid or invalid. Valid data is written to the Pass target, while invalid data is written to the Fail target.

You can also test and adjust rules using a subset of your source data. This can be helpful when your source dataset is large and you want to shorten processing time.

Each time a profile executes, the Data Profiler creates a job. Profile execution results, such as Pass/Fail count and execution duration time, are in each job. Aggregated job results for profiles are shown in the Run History for all Profiles page. Job results for a single profile are shown in the Profile Details page.

You can also schedule a profile to execute at regular intervals. When a profile is scheduled to execute a configuration is automatically created for the profile. The configuration specifies when and where the profile executes. You then manage and edit the configuration associated with the profile, and monitor execution results in the Manage environment. You can also interact with trend graphs which trace job results over a selected period.
