---
title: "Common Terms"
product: "Actian Data Platform"
guide: "Data Quality Guide"
source_file: "Common_Terms.htm"
canonical_id: "actian-data-platform-common-terms"
---

## Common Terms

Automatically created when a profile is scheduled for execution, and specifies when and where to execute the profile. Configurations can be edited.

Used for profiling a dataset, a data profile is comprised of data quality rules, and definitions for the data source and target.

The act of identifying problems and anomalies in a dataset. To profile data you add a data profiling rule to a profile to identify those problems. The profiling rule allows you to identify Data Quality issues, and then take the appropriate action.

Data is evaluated based on the conformance to the conditions or values defined within the profile rules. The rules specify characteristics such as accuracy, completeness, consistency, timeliness, validity, uniqueness. Once data has been profiled, multiple views are provided which help identify data quality issues and trends.

Specifies the type of value a field can store, the range of possible values, and the operations that can be performed on those values. The data type of a field also determines which rules can be used against the field. For example, there is a set of rules for the string data type, and another set of rules for the boolean data type.

Refers to any profile that has been executed, is currently running, or scheduled to run in the future. Profile execution results (for example, the execution duration time and pass/fail results) are stored in jobs. Jobs cannot be edited.

Allows users to evaluate source fields against a condition or value. Data is classified as either valid or invalid during execution. Valid data is written to the Pass Target, and invalid data is written to the Fail Target.

A profile rule resides in a profile and is associated with a field of a connected source. For information, see [Creating a Data Profile](../DataQuality/Creating_a_Data_Profile.md).

When enabled, automatically executes a profile whenever a rule is added, edited, or removed. This option provides immediate data quality rule results, which enables you to validate, and revise them.

Specifies the number of source data records to display on the page. There are three options: 5,000 records, 10,000 records, or All records. When Sample Size is set to All, the Inspect & Recommend option is disabled. Latency issues with large sources can be avoided by disabling "Run profile after every rule update” before creating profile rules, and then manually executing the profile.

Data Profiler has two targets for storing profile execution results. Each time a profile executes, Data Profiler writes the valid data to the Pass target, and the invalid data to the Fail target.

    - PASS_TARGET: Valid records, as defined by the profiling rules, are written to this target.

    - FAIL_TARGET: Invalid records, as defined by the profiling rules, are written to this target.

For information, see [Define Targets](../DataQuality/Define_Targets.md).
