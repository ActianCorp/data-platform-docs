---
title: "Indicator Variables"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Indicator_Variables.htm"
canonical_id: "actian-data-platform-indicator-variables"
---

## Indicator Variables

An indicator variable is a 2-byte integer variable associated with a host language variable in an embedded SQL statement. Indicator variables enable an application to:

- Detect when a null value is retrieved
- Assign a null value to a table column, form field, or table field column

- Detect character string truncation

### Indicator Variable Declaration

Like other host language variables, an indicator variable must be declared to embedded SQL in a declare section.

In an embedded SQL statement, the indicator variable is specified immediately after the host language variable, with a colon separating the two:

```
host_variable:indicator_variable
```

Or you can use the optional keyword indicator in the syntax:

```
host_variable indicator :indicator_variable
```

When used to detect or assign a null, indicator variables are commonly termed null indicator variables.

Specify indicator variables in association with host language variables that contain the following data:

- Database column value
- Constant database expression

- Form field value
- Table field column value

For example, the following example associates null indicators with variables representing column values:

```
exec sql select ename, esal     into :name:name_null, :salary:sal_null     from employee;
```

### Null Indicators and Data Retrieval

When a null value is retrieved into a host language variable that has an associated indicator variable, the indicator variable is set to -1 and the value of the host language variable is not changed. If the value retrieved is not a null, the indicator variable is set to 0 and the value is assigned to the host language variable. If the value retrieved is null and the program does not supply a null indicator, an error results.

Null indicator variables can be associated with the following:

- SELECT INTO and FETCH INTO result variable lists
- Database procedure parameters passed by reference

The following example illustrates the use of a null indicator when retrieving data. This example issues a FETCH statement and writes a roster to a file while checking for null phone numbers indicated by the variable, phone_null.

```
exec sql fetch emp_cursor into :name,     :phone:phone_null, :id;if (phone_null = -1) then     format_and_write_roster(name, 'N/A', id);else     format_and_write_roster(name, phone, id);end if;
```

### Using Null Indicators to Assign Nulls

Use an indicator variable with a host language variable to specify the assignment of a null to a database column. (An indicator variable can also be used to assign a null to a form field or a table field column.) When the Actian Data Platform assigns the value from a host language variable to one of these objects, it checks the value of the host language variable’s associated indicator variable.

If the indicator variable value is -1, a null is assigned to the object and ignores the value in the host language variable. If the indicator variable is any value other than -1, the value of the host language variable is assigned to the object.

If the indicator value is -1 and the object type is not nullable (such as a column created with the NOT NULL clause), an error results.

The following example demonstrates the use of an indicator variable and the null constant with the INSERT statement. For a description of the null constant, see [Nulls](../SQLLanguage/Nulls.md).

```
read name, phone number, and id from terminal;if (phone = ' ') then     phone_null = -1;else     phone_null = 0;end if;exec sql insert into newemp (name, phone, id,     comment)     values (:name, :phone:phone_null, :id, null);
```

Use null indicators to assign nulls in:

- The VALUES clause of the INSERT statement
- The SET clause of the UPDATE statement

- EXECUTE PROCEDURE statement parameters

All constant expressions in the above clauses can include the keyword NULL. Wherever an indicator variable can be used to assign a null, you can use the keyword NULL.

### Indicator Variables and Character Data Retrieval

When a character string is retrieved into a host language variable too small to hold the string, the data is truncated to fit. (If the data was retrieved from the database, the sqlwarn1 field of the SQLCA is set to 'W'.)

If the host language variable has an associated indicator variable, the indicator is set to the original length of the data. For example, the following statement sets the variable, char_ind, to 6 because it is attempting to retrieve a 6-character string into a 3-byte host language variable, char_3.

```
exec sql select 'abcdef' into :char_3:char_ind;
```

!!! note "Note"

    If a long varchar or long byte column is truncated into a host language variable, the indicator variable is set to 0. The maximum size of a long varchar or long byte column (two gigabytes) is too large a value to fit in an indicator variable.
