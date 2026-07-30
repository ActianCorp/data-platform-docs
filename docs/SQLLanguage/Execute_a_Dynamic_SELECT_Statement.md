---
title: "Execute a Dynamic SELECT Statement"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Execute_a_Dynamic_SELECT_Statement.htm"
canonical_id: "actian-data-platform-execute-a-dynamic-select-statement"
---

## Execute a Dynamic SELECT Statement

To execute a dynamic SELECT statement, use one of the following methods:

- If your program knows the data types of the SELECT statement result columns, use the EXECUTE IMMEDIATE statement with the INTO clause to execute the select. EXECUTE IMMEDIATE defines a select loop to process the retrieved rows.
- If your program does not know the data types of the SELECT statement result columns, use the EXECUTE IMMEDIATE statement with the USING clause to execute the select.

- If your program does not know the data types of the SELECT statement result columns, declare a cursor for the prepared SELECT statement and use the cursor to retrieve the results.

The EXECUTE IMMEDIATE option allows you to define a select loop to process the results of the select. Select loops do not allow the program to issue any other SQL statements while the loop is open. If the program must access the database while processing rows, use the cursor option.

For more information on these options, see [Unknown Result Column Data Types](../SQLLanguage/Execute_a_Dynamic_SELECT_Statement.md) and [How Unknown Result Column Data Types are Handled](../SQLLanguage/Execute_a_Dynamic_SELECT_Statement.md).

To determine whether a statement is a select, use the PREPARE and DESCRIBE statements. A REPEATED SELECT statement can be prepared only if it is associated with a cursor.

The following code demonstrates the use of the PREPARE and DESCRIBE statements to execute random statements and print results. This example uses cursors to retrieve rows if the statement is a select.

```
statement_buffer = ' ';loop while reading statement_buffer from terminal     exec sql prepare s1 from :statement_buffer;     exec sql describe s1 into :rdescriptor;     if sqlda.sqld = 0 then          exec sql execute s1;     else          /* This is a SELECT */          exec sql declare c1 cursor for s1;          exec sql open c1;          allocate result variables using                result_descriptor;          loop while there are more rows in the cursor               exec sql fetch c1 using descriptor                     :rdescriptor;               if (sqlca.sqlcode not equal 100) then                    print the row using                    rdescriptor;               end if;          end loop;          free result variables from rdescriptor;          exec sql close c1;     end if;     process sqlca for status;end loop;
```

### Unknown Result Column Data Types

For some dynamic SELECT statements, the program knows the data types of the resulting columns and, consequently, the data types of the result variables used to store the column values. If the program has this information, the program can use the EXECUTE IMMEDIATE statement with the into clause to execute the SELECT statement.

In the following example, a database contains several password tables, each having one column and one row and containing a password value. An application connected to this database requires a user to successfully enter two passwords before continuing. The first password entered is the name of a password table and the second is the password value in that table.

The following code uses the EXECUTE IMMEDIATE statement to execute the dynamically-defined select built by the application to check these passwords:

```
...prompt for table_password and value_passwordselect_stmt = 'select column1 from ' +     table_password;exec sql execute immediate :select_stmt     into :result_password;if (sqlstate < 0) or (value_password <>     result_password) then     print      'Password authorization failure'endif...
```

Because the application developer knows the data type of the column in the password table (although not which password table is selected), the developer can execute the dynamic select with the EXECUTE IMMEDIATE statement and the INTO clause.

The syntax of EXECUTE IMMEDIATE in this context is:

```
exec sql execute immediate select_statement
```

```
into variable{,variable};
```

```
[exec sql begin;
```

```
     host_code
```

```
exec sql end;]
```

This syntax retrieves the results of the select into the specified host language variables. The begin and end statements define a select loop that processes each row returned by the SELECT statement and terminates when there are no more rows to process. If a select loop is used, your program cannot issue any other SQL statements for the duration of the loop.

If the select loop is not included in the statement, the Actian Data Platform assumes that the SELECT statement is a singleton select returning only one row and, if more than one row is returned, issues an error.

### How Unknown Result Column Data Types are Handled

In most instances, when a dynamically defined SELECT statement is executed, the program does not know in advance the number or types of result columns. To provide this information to the program, first prepare and describe the SELECT statement. The DESCRIBE statement returns to the program the type description of the result columns of a prepared SELECT statement. After the select is described, the program must allocate (or reference) dynamically the correct number of result storage areas of the correct size and type to receive the results of the select.

If the statement is not a SELECT statement, describe returns a zero to the sqld and no sqlvar elements are used.

After the statement has been prepared and described and the result variables allocated, the program has two choices regarding the execution of the SELECT statement:

- The program can associate the statement name with a cursor name, open the cursor, fetch the results into the allocated results storage area (one row at a time), and close the cursor.
- The program can use EXECUTE IMMEDIATE. EXECUTE IMMEDIATE defines a select loop to process the returned rows. If the select returns only one row, it is not necessary to use a select loop.

### Prepare and Describe SELECT Statements

If the program has no advance knowledge of the resulting columns, the first step in executing a dynamic SELECT statement is to prepare and describe the statement. Preparing the statement encodes and saves the statement and assigns it a name. For information about the syntax and use of PREPARE, see [PREPARE and EXECUTE Statements](../SQLLanguage/Dynamic_SQL_Statements.md).

The DESCRIBE statement returns descriptive information about a prepared statement into a program descriptor, that is, an SQLDA structure. This statement is primarily used to return information about the result columns of a SELECT statement to the program; however, it is also possible to describe other statements. (When a non-select statement is described, the only information returned to the program is that the statement was not a SELECT statement.)

The syntax of the DESCRIBE statement is:

```
EXEC SQL DESCRIBE statement_name INTO|USING descriptor_name;
```

When a SELECT statement is described, information about each result column is returned to an sqlvar element. (For information about sqlvar elements, see [Structure of the SQLDA](../SQLLanguage/SQLDA.md).) This is a one-to-one correspondence: the information in one sqlvar element corresponds to one result column. Therefore, before issuing the DESCRIBE statement, the program must allocate sufficient sqlvar elements and set the SQLDA sqln field to the number of allocated sqlvars. The program must set sqln before the DESCRIBE statement is issued.

After issuing the DESCRIBE statement, the program must check the value of sqld, which contains the number of sqlvar elements used to describe the statement. If sqld is zero, the prepared statement was not a SELECT statement. If sqld is greater than sqln, the SQLDA does not have enough sqlvar elements: more storage must be allocated and the statement must be re-described.

The following example shows a typical DESCRIBE statement and the surrounding host program code. The program assumes that 20 sqlvar elements are sufficient:

```
sqlda.sqln = 20;exec sql describe s1 into sqlda;if (sqlda.sqld = 0) then     statement is not a select statement;else if (sqlda.sqld > sqlda.sqln) then     save sqld;     free current sqlda;     allocate new sqlda using sqld as the size;     sqlda.sqln = sqld;     exec sql describe s1 into sqlda;end if;
```

### Sqlvar Elements

After describing a statement, the program must analyze the contents of the sqlvar array. Each element of the sqlvar array describes one result column of the SELECT statement. Together, all the sqlvar elements describe one complete row of the result table.

The DESCRIBE statement sets the data type, length, and name of the result column (sqltype, sqllen and sqlname), and the program must use that information to supply the address of the result variable and result indicator variable (sqldata and sqlind). Your program must also allocate the space for these variables.

For example, if you create the table object as follows:

```
exec sql create table object     (o_id            integer not null,      o_desc          char(100) not null,      o_price         money not null,      o_sold          date);
```

and describe the following dynamic query:

```
exec sql prepare s1 from 'select * from object';exec sql describe s1 into sqlda;
```

The SQLDA descriptor results are as follows:

| sqld | 4 (columns) |  |  |
| --- | --- | --- | --- |
| sqlvar(1) | sqltype | = | 30 (integer) |
|  | sqllen | = | 4 |
|  | sqlname | = | 'o_id' |
| sqlvar(2) | sqltype | = | 20 (char) |
|  | sqllen | = | 100 |
|  | sqlname | = | 'o_desc' |
| sqlvar(3) | sqltype | = | 5 (money) |
|  | sqllen | = | 0 |
|  | sqlname | = | 'o_price' |
| sqlvar(4) | sqltype | = | -3 (nullable date) |
|  | sqllen | = | 0 |
|  | sqlname | = | 'o_sold' |

The value that the DESCRIBE statement returns in sqllen depends on the data type of the column being described, as listed in the following table:

| Data Type | Contents of sqllen |
| --- | --- |
| char and varchar | Maximum length of the character string. |
| integer and float | Declared size of the numeric field. |
| ansidate | 0 (the program must use a 25-byte character string to retrieve or set date data). |
| money | 0 (the program must use an 8-byte floating point variable to retrieve or set money data). |
| decimal | High byte contains precision, low byte contains scale. |

After the statement is described, your program must analyze the values of sqltype and sqllen in each sqlvar element. If sqltype and sqllen do not correspond exactly with the types of variables used by the program to process the SELECT statement, modify sqltype and sqllen to be consistent with the program variables. After describing a SELECT statement, there is one sqlvar element for each expression in the select target list.

After processing the values of sqltype and sqllen, allocate storage for the variables that contain the values in the result columns of the SELECT statement by pointing sqldata at a host language variable that contain the result data. If the value of sqltype is negative, which indicates a nullable result column data type, allocate an indicator variable for the particular result column and set sqlind to point to the indicator variable. If sqltype is positive, indicating that the result column data type is not nullable, an indicator variable is not required. In this case, set sqlind to zero.

To omit the null indicator for a nullable result column (sqltype is negative if the column is nullable), set sqltype to its positive value and sqlind to zero. Conversely, if sqltype is positive and an indicator variable is allocated, set sqltype to its negative value, and set sqlind to point to the indicator variable.

In the preceding example, the program analyzes the results and modifies some of the types and lengths to correspond with the host language variables used by the program: the money data type is changed to float, and the date type to char. In addition, sqlind and sqldata are set to appropriate values. The values in the resulting sqlvar elements are:

| sqlvar(1) | sqltype | = | 30 (integer not nullable) |
| --- | --- | --- | --- |
|  | sqllen | = | 4 |
|  | sqldata | = | Address of 4-byte integer |
|  | sqlind | = | 0 |
|  | sqlname | = | 'o_id' |
| sqlvar(2) | sqltype | = | 20 (char not nullable) |
|  | sqllen | = | 100 |
|  | sqldata | = | Address of 100-byte character string |
|  | sqlind | = | 0 |
|  | sqlname | = | 'o_desc' |
| sqlvar(3) | sqltype | = | 31 (float not nullable, was money) |
|  | sqllen | = | 8 (was 0) |
|  | sqldata | = | Address of 8-byte floating point |
|  | sqlind | = | 0 |
|  | sqlname | = | 'o_price' |
| sqlvar(4) | sqltype | = | -20 (char nullable, was date) |
|  | sqllen | = | 25 (was 0) |
|  | sqldata | = | Address of 25-byte character string |
|  | sqlind | = | Address of 2-byte indicator variable |
|  | sqlname | = | 'o_sold' |
