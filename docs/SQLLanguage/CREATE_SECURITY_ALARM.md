---
title: "CREATE SECURITY_ALARM"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "CREATE_SECURITY_ALARM.htm"
canonical_id: "actian-data-platform-create-security-alarm"
---

## CREATE SECURITY_ALARM

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL, ESQL

!!! note "Note"

    Security alarms can be enabled on request by contacting [Actian Support](https://supportservices.actian.com/support-services/support/#contacts).

The CREATE SECURITY_ALARM statement specifies, for tables, databases, or the current installation, the events to be written to the security log.

#### Syntax

The CREATE SECURITY_ALARM statement has the following format:

```
[EXEC SQL] CREATE SECURITY_ALARM [alarm_name] ON
```

```
             [TABLE | DATABASE] [schema.]object_name {, [schema.]object_name} |
```

```
                CURRENT INSTALLATION
```

```
             [IF SUCCESS | FAILURE | SUCCESS, FAILURE]
```

```
             [WHEN SELECT | DELETE | INSERT | UPDATE | CONNECT | DISCONNECT]
```

```
             [BY [USER | GROUP | ROLE] auth_id{, auth_id} | PUBLIC;]
```

```
             [RAISE DBEVENT [dbevent_owner.]dbevent_name [dbevent_text]]
```

**object_name**

:   Specifies the table or database for which security events are logged.

**IF SUCCESS | FAILURE | SUCCESS, FAILURE**

:   Specifies when logging occurs:

SUCCESS

:   Creates a log record when a user succeeds in performing the specified type of access.

FAILURE

:   Creates a log record when a user attempts to perform the specified type of access and fails (the query is terminated). Users can fail to gain access to a table because they lack the required permissions.

SUCCESS, FAILURE

:   Logs all attempts to access the tables.

**WHEN clause**

:   Specifies the types of access to be logged. Any combination of the access types shown in the syntax diagram can be specified, in a comma separated list.

**BY clause**

:   Specifies the user names of the users for whom logging is performed.

:   To log access attempts for all users, specify PUBLIC.

:   Default: PUBLIC

## Permissions

You must own the table.

## Related Statements

DISABLE SECURITY_AUDIT

ENABLE SECURITY_AUDIT

DROP SECURITY_ALARM

HELP SECURITY_ALARM

## CREATE SECURITY_ALARM Examples

1. Log all successful changes to the employee table.

```
CREATE SECURITY_ALARM ON TABLE employee    IF SUCCESS WHEN INSERT, UPDATE, DELETE BY PUBLIC;
```

2. Specify alarms for a specific user group or application role.

```
CREATE SECURITY_ALARM clerk_update ON TABLE secure_data IF FAILURE WHEN UPDATE BY GROUP clerk
```

    These alarms are fired when a session connects as the specified group or role.

3. Specify alarm on a particular database or the current installation to raise an alarm when user, spy, connects to any database.

```
CREATE SECURITY_ALARM secconnect ON CURRENT INSTALLATION WHEN CONNECT BY USER spy
```

4. Raise an optional database event, secconnect, as the result of an alarm firing when user, spy, connects to database sec1.

```
CREATE SECURITY_ALARM secconnect ON DATABASE sec1 WHEN CONNECT BY USER spy RAISE DBEVENT secconnect 'user spy connected to sec1 database';
```
