---
title: "Constants"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Constants.htm"
canonical_id: "actian-data-platform-constants"
---

## Constants

A constant is a symbol that represents a specific data value.

SQL constants can be used in queries and expressions. They can be used any number of times in a query, but the value is only materialized once per query execution. So a constant such as CURRENT_DATE can be referenced in an INSERT statement that inserts many rows, or an UPDATE statement that alters many rows, and the same date value will be used for each.

Examples:

```
SELECT CURRENT_DATE;
```

```
SELECT CURRENT_DATE + 7; sales_order (item_number INT, clerk VARCHAR(32), billing_date ANSIDATE);INSERT INTO sales_order (item_number, clerk, billing_date) VALUES ('123', USER, CURRENT_DATE+DATE('7 days'));
```

The following constants can be used in queries:

| Constant | Meaning |
| --- | --- |
| NULL | Indicates a missing or unknown value in a table. |
| CURRENT_DATE | Current date (as ANSI date type) |
| CURRENT_TIME | Current time with time zone |
| CURRENT_TIMESTAMP | Current date and time with time zone |
| CURRENT_USER | Same as user |
| INITIAL_USER | Actian user identifier in effect at the start of the session |
| LOCAL_TIME | Current time without time zone |
| LOCAL_TIMESTAMP | Current timestamp without time zone.Returns a timestamp without a timezone but is a TIMESTAMP WITH LOCAL TIMEZONE data type. |
| SESSION_USER | Same as user |
| SYSTEM_USER | Operating system user identifier of the user who started the session |
| USER | Effective user of the session (the Actian user identifier, not the operating system user identifier) |
