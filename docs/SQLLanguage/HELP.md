---
title: "HELP"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "HELP.htm"
canonical_id: "actian-data-platform-help"
---

## HELP

[Valid in](../SQLLanguage/Statement_Contexts_(Valid_in).md): SQL. Not valid in Query Editor.

The HELP statement displays information about database objects and SQL statements, including object name, owner, and type for all tables, views, and indexes to which the user has access, and all synonyms owned by the user. System tables and temporary tables are not listed. Information is displayed in a one-line-per-object format.

In general, to display high-level information, specify HELP objectname (for example, HELP mytable). To display detailed information, specify HELP object_type object_name (for example, HELP TABLE mytable).

The asterisk wildcard character can be used in object name specifications to display information about a selected set of objects.

The HELP statement has the following format:

```
HELP [[schema.]objectname {, [schema.]objectname}]HELP COMMENT COLUMN [schema.]table column_name {, column_name}HELP COMMENT TABLE [schema.]table {, [schema.]table }HELP CONSTRAINT [schema.]table_name                {, [schema.]constraint_name}HELP DEFAULT [schema.]table_name HELP HELPHELP INDEX [schema.]indexname {, [schema.]indexname}HELP PERMIT ON TABLE | VIEW               [schema.]object_name {, [schema.]object_name}HELP REGISTER [schema.]objectname HELP SECURITY_ALARM [ON TABLE] table_nameHELP SECURITY_ALARM ON DATABASE database_nameHELP SECURITY_ALARM ON CURRENT INSTALLATIONHELP SEQUENCE [schema.]objectname HELP SQL [sql_statement]HELP SYNONYM [schema.]synonym {, [schema.]synonym}HELP TABLE [schema.]table_name {, [schema.]table_name}HELP TABLE|INDEX nameHELP VIEW [schema.]view_name {, [schema.]view_name}
```

**objectname**

:   Specifies the name of a table, view, or index. Display format is block-style.

**COMMENT COLUMN**

:   Displays any comments defined for the specified columns.

**COMMENT TABLE**

:   Displays any comments defined for the specified tables.

**CONSTRAINT**

:   Displays any constraints defined on columns of the specified table or on the entire table.

**DEFAULT**

:   Displays any user-defined defaults defined on columns of the specified table.

**HELP**

:   Displays valid HELP statements.

**INDEX**

:   Displays detailed information about the specified indexes.

**PERMIT ON TABLE | VIEW**

:   For tables, displays the permit text. For other objects, displays the values required by the corresponding DROP PERMIT statement.

**REGISTER**

:   Displays information about registered objects.

**SECURITY_ALARM [ON TABLE]**

:   Displays all security alarms defined for the specified table. The information includes an index number that can be used on the DROP SECURITY_ALARM statement.

**SECURITY_ALARM ON DATABASE**

:   Displays all security alarms defined for the specified database. The information includes an index number that can be used on the DROP SECURITY_ALARM statement.

**SECURITY_ALARM ON CURRENT INSTALLATION**

:   Displays all security alarms defined for the current installation. The information includes an index number that can be used on the DROP SECURITY_ALARM statement.

**SEQUENCE**

:   Displays detailed information about the specified sequence.

**SQL**

:   Displays information about the specified SQL statement. If the sql_statement parameter is omitted, displays a list of SQL statements for which help information is available.

**SYNONYM**

:   Displays information about the specified synonyms. To display all the synonyms you own, specify HELP SYNONYM *. To display all the synonyms you own plus all the synonyms to which you have access, specify HELP SYNONYM *.*.

**TABLE**

:   Displays detailed information about the specified tables.

**TABLE | INDEX**

:   Displays the cache priority.

**VIEW**

:   Displays detailed information about the specified views.

The asterisk (*) wildcard can be used to specify all or part of the owner or object name parameters in a HELP statement. The HELP statement displays only objects to which the user has access, which are:

- Objects owned by the user
- Objects owned by other users that have granted permissions to the user

- Objects owned by the DBA to which you have access

If wildcards are specified for both the owner and object name (*.*), HELP displays all objects to which you have access. To display help information about objects you do not own, specify the owner name (using the schema.objectname syntax). If the owner name wildcard is omitted (that is, * is specified instead of *.*), HELP displays the objects that can be accessed without the owner prefix.

The following examples illustrate the effects of the wildcard character:

| Wildcard | Description |
| --- | --- |
| HELP * | Display objects owned by the effective user of the session. |
| HELP davey.* | Display all objects owned by davey. |
| HELP *.mytable | Display all objects named, mytable, regardless of owner. |
| HELP d*.* | Display all objects owned by users beginning with d. |
| HELP *.d* | Display all objects beginning with d regardless of owner. |
| HELP *.* | Display all objects regardless of owner. |

## HELP Examples

The following are HELP statement examples:

1. Display a list of all tables, views, and indexes to which the user has access.

```
HELP;
```

2. Display help about all tables starting with “e” to which the user has access.

```
HELP *.e*;
```

3. Display help about the employee and dept tables.

```
HELP employee, dept;
```

4. Display the definition of the view, highpay.

```
HELP view highpay;
```

5. Display all permits issued on the job and employee tables.

```
HELP PERMIT ON TABLE job, employee;
```

6. Display information on the SELECT statement.

```
HELP SQL select;
```
