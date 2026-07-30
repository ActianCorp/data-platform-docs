---
title: "Search Conditions in SQL Statements"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Search_Conditions_in_SQL_Statements.htm"
canonical_id: "actian-data-platform-search-conditions-in-sql-statements"
---

## Search Conditions in SQL Statements

Search conditions are used in WHERE and HAVING clauses to qualify the selection of data. Search conditions are composed of predicates of various kinds, optionally combined using parentheses and logical operators (AND, OR, and NOT). The following are examples of legal search conditions:

| Description | Example |
| --- | --- |
| Simple predicate | salary BETWEEN 10000 AND 20000 |
| Predicate with NOT operator | edept NOT LIKE 'eng_%' |
| Predicates combined using OR operator | edept LIKE 'eng_%' OR edept LIKE 'admin_%' |
| Predicates combined using AND operator | salary BETWEEN 10000 AND 20000 AND edept LIKE 'eng_%' |
| Predicates combined using parentheses to specify evaluation | (salary BETWEEN 10000 AND 20000 AND edept LIKE 'eng_%') OR edept LIKE 'admin_%' |

Predicates evaluate to true, false, or unknown. They evaluate to unknown if one or both operands are null (the IS NULL predicate is the exception). When predicates are combined using logical operators (that is, AND, OR, NOT) to form a search condition, the search condition evaluates to true, false, or unknown as shown in the following tables:

| AND | true | false | unknown |
| --- | --- | --- | --- |
| true | true | false | unknown |
| false | false | false | false |
| unknown | unknown | false | unknown |

| OR | true | false | unknown |
| --- | --- | --- | --- |
| true | true | true | true |
| false | true | false | unknown |
| unknown | true | unknown | unknown |

NOT(true) is false, NOT(false) is true, NOT(unknown) is unknown.

After all search conditions are evaluated, the value of the WHERE or HAVING clause is determined. The WHERE or HAVING clause can be true or false, not unknown. Unknown values are considered false.

More information:

Comparison Operators

[Logical Operators](../SQLLanguage/Elements_of_SQL_Statements.md)

[Predicates in SQL](../SQLLanguage/Predicates_in_SQL.md)
