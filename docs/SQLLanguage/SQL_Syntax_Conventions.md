---
title: "SQL Syntax Conventions"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQL_Syntax_Conventions.htm"
canonical_id: "actian-data-platform-sql-syntax-conventions"
---

## SQL Syntax Conventions

When representing syntax, the following conventions are used in this guide:

| Convention | Usage |
| --- | --- |
| UPPERCASE | Indicates reserved keywords such as SELECT and WHERE |
| `Monospace` | Indicates keywords, symbols, or punctuation that you must enter as shown |
| Italic< > (angle brackets) | Indicates a variable name for which you must supply an actual value—this convention is used in explanatory text and syntax |
| [ ] (square brackets) | Indicates an optional item |
| { } (curly braces) | Indicates an optional item that you can repeat as many times as appropriate |
| \| (vertical bar) | Indicates a list of mutually exclusive items (that is, you can select only one item from the list) |

The following example illustrates the syntax conventions:

```
[EXEC SQL] ALTER GROUP group_id {, group_id}
```

```
ADD USERS (user_id{, user_id}) | DROP USERS (user_id{, user_id}) | DROP ALL
```

Explanation:

- [EXEC SQL] is optional and does not need to be included
- ALTER GROUP are reserved keywords (for more information, see [Keywords](../SQLLanguage/Keywords.md))

- group_id is a variable name for which you must substitute an actual group ID number
- {, group_id} is an optional item that can be repeated (multiple values must be separated by a comma)

- ADD USERS | DROP USERS | DROP ALL are mutually exclusive items—pick and use only one

SQL statement syntax is followed by a term list explaining the keywords, variables, and other values provided in the syntax representation.
