---
title: "Effects of Errors in Database Procedures"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Effects_of_Errors_in_Database_Procedures.htm"
canonical_id: "actian-data-platform-effects-of-errors-in-database-procedures"
---

## Effects of Errors in Database Procedures

When an error occurs in a database procedure, it has the following effects:

- All statements in the procedure up to the point of the error are rolled back.
- The procedure continues execution with the statement following the statement that caused the error.

- Parameters passed by reference are not updated.

The error is returned to the application in SQLSTATE, SQLCODE, and ERRORNO. An error number is also returned to iierrornumber, a built-in variable available only in database procedures for error handling.

!!! note "Note"

    A fatal error, such as dividing by zero, cannot be trapped in a database procedure and will cause the procedure to fail. For example, executing the following database procedure, in which the divisor variable is 0, will result in program failure:

```
...
```

```
update a_test set an_integer=int4(an_integer/:divisor);
```

```
select iierrornumber, iirowcount into :enumber, :rowcount;
```

```
if enumber=0 then
```

```
if rowcount=0 then
```

```
...
```

### iierrornumber and iirowcount Variables

The iierrornumber and iirowcount variables, in conjunction with the RAISE ERROR statement, handle errors in database procedures.

The iirowcount variable contains the number of rows affected by the last executed SQL statement. The iierrornumber variable contains the error number (if any) associated with the execution of a database procedure statement.

Because both iierrornumber and iirowcount reflect the results of the preceding query, beware of inadvertently resetting the value of one when checking the other.

The following example from a database procedure illustrates this error:

```
...update emp set .../* The following statement resets iierrornumber, which will reflect the results of the second statement and not the first, as desired. *//* wrong way to check iirowcount */rcount = iirowcount;/* The error number reflects the results of the preceding assignment, not the update statement */enumber = iierrornumber;
```

The following example illustrates the correct way to check iierrornumber and iirowcount: select both values into variables, and then check the contents of the variables (because iierrornumber and iirowcount is reset to reflect the results of the SELECT statement).

```
...update emp set .../* right way to check iirowcount (using select) */select iirowcount, iierrornumber into rcount, enumber;
```

```

```

The following table lists the values of iirowcount and iierrornumber after the successful or unsuccessful execution of an SQL statement:

| Statement | Success | Success | Error | Error |
| --- | --- | --- | --- | --- |
|  | iirowcount | iierrornumber | iirowcount | iierrornumber |
| INSERT | number of rows | 0 | 0 | error number |
| UPDATE | number of rows | 0 | 0 | error number |
| DELETE | number of rows | 0 | 0 | error number |
| SELECT | 0 or 1 | 0 | 0 | error number |
| ASSIGNMENT | 1 | 0 | 0 | error number |
| COMMIT | -1 | 0 | -1 | error number |
| ROLLBACK | -1 | 0 | -1 | error number |
| MESSAGE | -1 | 0 | -1 | error number |
| RETURN | -1 | 0 | -1 | error number |
| IF | no change | no change | no change | error number |
| ELSEIF | no change | no change | no change | error number |
| WHILE | no change | no change | no change | error number |
| CONTINUE | no change | no change | no change | no change |
| ELSE | no change | no change | no change | no change |
| ENDIF | no change | no change | no change | no change |
| ENDLOOP | no change | no change | no change | no change |
| ENDWHILE | no change | no change | no change | no change |

The execution of each database procedure statement sets the value of iierrornumber either to zero (no errors) or an error number. To check the execution status of any particular statement, iierrornumber must be examined immediately after the execution of the statement.

Errors occurring in IF, WHILE, MESSAGE, and RETURN statements do not set iierrornumber. However, any errors that occur during the evaluation of the condition of an IF or WHILE statement terminate the procedure and return control to the calling application.

### Raise Error Statement

The RAISE ERROR statement generates an error. The Actian Data Platform responds to this error exactly as it does to any other error. If the RAISE ERROR statement is issued by a database procedure that is directly executed, the error is handled using the default error handling behavior or the user-supplied error handling mechanism.

The error number that is specified as an argument to raise error is returned to sqlerrd(1), and can be accessed using INQUIRE_SQL(DBMSERROR).
