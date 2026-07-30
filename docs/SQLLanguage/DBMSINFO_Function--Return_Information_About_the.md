---
title: "DBMSINFO Function--Return Information About the Current Session"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DBMSINFO_Function--Return_Information_About_the.htm"
canonical_id: "actian-data-platform-dbmsinfo-function-return-information-about-the"
---

## DBMSINFO Function--Return Information About the Current Session

DBMSINFO is a SQL function that returns a string containing information about the current session. Use this function in the SQL CLI or in an embedded SQL application.

The DBMSINFO function is used in a SELECT statement as follows:

```
SELECT DBMSINFO('request_name')
```

where 'request_name' is one of those described in [Request Names for DBMSINFO Function](../SQLLanguage/MASK_COLUMN_Function.md).

### Dbmsinfo Examples

To see the version of Actian Data Platform runtime you are using, enter:

```
SELECT DBMSINFO('_VERSION');
```

The DBMSINFO function can be used in WHERE clauses in SELECT statements. For example:

```
EXEC SQL SELECT dept FROM employee      WHERE ename=DBMSINFO('USERNAME');
```
