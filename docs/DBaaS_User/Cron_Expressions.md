---
title: "Cron Expressions"
product: "Actian Data Platform"
guide: "DBaaS User Guide"
source_file: "Cron_Expressions.htm"
canonical_id: "actian-data-platform-cron-expressions"
---

## Cron Expressions

Actian lets you set a schedule warehouse or database actions using a cron expression, which is a specially formatted text string.

The following example is a cron expression representing a schedule that will run at 1:25 p.m. on the first day of each month.

```
0 25 13 1 * ? *
```

### Building a Cron Expression

A cron expression is composed of six or seven values separated by spaces. Each of these values represents part of the schedule and can be either a number or a certain special character.

#### Expression Fields

| Field | Required | Values | Special Characters |
| --- | --- | --- | --- |
| Second | Yes | 0–59 | , - * / |
| Minute | Yes | 0–59 | , - * / |
| Hour | Yes | 0–23 | , - * / |
| Day of Month | Yes | 1–31 | , - * / L W ? |
| Month | Yes | 1–12 or JAN–DEC | , - * / |
| Day of Week | Yes | 1–7 or SUN–SAT | , - * / # ? |
| Year | No | 1970–2099 | , - * / |

#### Special Characters

Special characters let you specify wildcards, ranges, and other conditions for each field.

| Character | Description | Examples |
| --- | --- | --- |
| * | All values for the field are selected. | * in the Hour field means every hour. |
| ? | No specific value required. Only usable in the Day of Month and Day of Week fields. | To set a schedule that runs on Sundays regardless of the day of the month, use a ? in the Day of Month field and a 1 in the Day of Week field. |
| - | Specify a range (inclusive) between 2 values. | 1–3 in the Hour field (along with a 0 in the Minute and Second fields) is triggered at 1:00 a.m., 2:00 a.m., and 3:00 a.m. |
| , | Separate multiple values. | 1,3 in the Hour field means 1:00 a.m. and 3:00 a.m. |
| / | Incremental trigger. Enter in the format X/Y, where X is the starting value and Y is the increment. | 0/15 in the Minute field means the schedule begins at minute 00 and then runs every 15 minutes thereafter. |
| L | Last day of the month or week.Can be combined with other values in each field as illustrated below.<br>• Day of Month: L–X, where X is a number of days to offset from the last calendar day of the month.<br>• Day of Week: XL, where X is a day value (1–7). | L in the Day of Month field means the last calendar day of the month.L–2 in the Day of Month field means the second-to-last calendar day of the month.L in the Day of Week field simply means 7 (Saturday).7L in the Day of Week field means the last Saturday of the month. |
| W | Weekday (Monday–Friday) nearest the given day. Enter in the format XW, where X is the day of the month. | 12W in the Day of Month field is triggered on the 12th day of the month if that day falls on a weekday. If the 12th falls on a Saturday or Sunday, the schedule runs on the following Monday.LW in the Day of Month field is triggered on the last weekday of the month. |
| # | Exact monthly instance of the specified day of the week. Enter in the format X#Y, where X is the day of the week and Y is the instance.**Note:**A value using X#5 will not be triggered for the month if there are not 5 of day X within the month. | 2#3 in the Day of Week field means the 3rd Monday each month. |

### Examples

Following are several examples of simple and complex cron expressions.

#### Simple Daily

Run the schedule at 9:00 a.m. every day.

```
0 0 9 * * ? *
```

| Seconds | Minutes | Hours | Day of Month | Month | Day of Week | Year |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 9 | * | * | ? | * |

#### Complex Daily

Run the schedule every 5 seconds for 1 minute beginning at 9:00 a.m. every day.

```
0/5 0 9 * * ? *
```

| Seconds | Minutes | Hours | Day of Month | Month | Day of Week | Year |
| --- | --- | --- | --- | --- | --- | --- |
| 0/5 | 0 | 9 | * | * | ? | * |

#### Simple Weekly

Run the schedule at 9:25 a.m. every Friday.

```
0 25 9 * * 6 *
```

| Seconds | Minutes | Hours | Day of Month | Month | Day of Week | Year |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 25 | 9 | * | * | 6 | * |

#### Complex Weekly

Run the schedule at 9:00 a.m. every Friday, but only in January or February of 2019.

```
0 0 9 * 1,2 6 2019
```

| Seconds | Minutes | Hours | Day of Month | Month | Day of Week | Year |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 9 | * | 1,2 | 6 | 2019 |

#### Monthly

Run the schedule at 9:00 a.m., 9:22 a.m., and 9:44 a.m. on the last Thursday of each month.

```
0 0,22,44 9 ? * L5 *
```

| Seconds | Minutes | Hours | Day of Month | Month | Day of Week | Year |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0,22,44 | 9 | ? | * | L5 | * |

#### Yearly

Run the schedule at 2:27 p.m., 3:27 p.m., and 4:27 p.m. on the weekday nearest the 12th day of the month every October.

```
0 27 14-16 12W 10 ? *
```

| Seconds | Minutes | Hours | Day of Month | Month | Day of Week | Year |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 27 | 14-16 | 12W | 10 | ? | * |
