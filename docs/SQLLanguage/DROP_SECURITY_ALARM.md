---
title: "DROP SECURITY_ALARM"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "DROP_SECURITY_ALARM.htm"
canonical_id: "actian-data-platform-drop-security-alarm"
---

## DROP SECURITY_ALARM

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL, OpenAPI, ODBC, JDBC, .NET

!!! note "Note"

    Security alarms can be enabled on request by contacting [Actian Support](https://supportservices.actian.com/support-services/support/#contacts).

The DROP SECURITY_ALARM statement deletes security alarms for a table, database, or current installation.

#### Syntax

The DROP SECURITY_ALARM statement has the following format:

```
[EXEC SQL] DROP SECURITY_ALARM ON [TABLE] table_name |             DATABASE dbname | CURRENT INSTALLATION | ALL |                integer {, integer} | alarm_name {, alarm_name}
```

**ALL**

:   Deletes all security alarms for the specified table, database, or current installation.

**integer (, integer)**

:   Deletes the security alarms identified by the specified numeric ID. To see the numeric ID, use the HELP SECURITY_ALARM statement (valid in interactive SQL but not in the Query Editor).

**alarm_name (, alarm_name)**

:   Deletes the security alarms identified by the specified alarm name.

#### Permissions

You must be the owner of the tables.

To drop database or installation security alarms, you must have security privilege and be connected to the iidbdb.

#### Related Statements

[CREATE SECURITY_ALARM](../SQLLanguage/CREATE_SECURITY_ALARM.md)

[HELP](../SQLLanguage/HELP.md) SECURITY_ALARM

ENABLE SECURITY_AUDIT

DISABLE SECURITY_AUDIT

## DROP SECURITY_ALARM Examples

1. Delete a security alarm for the employee table.

```
DROP SECURITY_ALARM ON employee 1;
```

2. Drop a table security alarm and an installation alarm.

```
DROP SECURITY_ALARM ON emp 2;DROP SECURITY_ALARM ON CURRENT INSTALLATION bad_update ;
```
