---
title: "Retrieve Results Using Cursors"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Retrieve_Results_Using_Cursors.htm"
canonical_id: "actian-data-platform-retrieve-results-using-cursors"
---

## Retrieve Results Using Cursors

To give your program the ability to access the database or issue other database statements while processing rows retrieved as the result of the select, a cursor must be used to retrieve those rows.

To use cursors, after the SQLDA has been analyzed and result variables have been allocated and pointed at, the program must declare and open a cursor to fetch the result rows.

The syntax of the cursor declaration for a dynamically defined SELECT statement is:

```
EXEC SQL DECLARE cursor_name CURSOR FOR statement_name;
```

This statement associates the SELECT statement represented by statement_name with the specified cursor. Statement_name is the name assigned to the statement when the statement was prepared. As with non-dynamic cursor declarations, the SELECT statement is not evaluated until the cursor is opened. After opening the cursor, the program retrieves the result rows using the FETCH statement with the SQLDA instead of the list of output variables.

The syntax for a cursor FETCH statement is:

```
EXEC SQL FETCH cursor_name USING DESCRIPTOR descriptor_name;
```

Before the FETCH statement, the program has filled the result descriptor with the addresses of the result storage areas. When executing the FETCH statement, the result columns are copied into the result areas referenced by the descriptor.

The following example elaborates on an earlier example in this section. The program reads a statement from the terminal. If the statement is “quit” the program ends; otherwise, the program prepares the statement. If the statement is not a select, it is executed. If the statement is a FETCH statement, it is described, a cursor is opened, and the result rows are fetched. Error handling is not shown.

```
exec sql include sqlca;
```

```
exec sql include sqlda;
```

```

```

```
allocate an sqlda with 300 sqlvar elements;
```

```
sqlda.sqln = 300;
```

```

```

```
read statement_buffer from terminal;
```

```

```

```
loop while (statement_buffer <> 'quit')
```

```

```

```
     exec sql prepare s1 from :statement_buffer;
```

```
     exec sql describe s1 into sqlda;
```

```

```

```
     if (sqlda.sqld = 0) then
```

```
                         /* This is not a select */
```

```

```

```
          exec sql execute s1;
```

```
     else                /* This is a select */
```

```

```

```
          exec sql declare c1 cursor for s1;
```

```
          exec sql open c1;
```

```

```

```
          print column headers from the sqlname
```

```
          fields; analyze the SQLDA, inspecting
```

```
          types and lengths; allocate result
```

```
          variables for a cursor result row;
```

```
          set sqlvar fields sqldata and sqlind;
```

```

```

```
          loop while (sqlca.sqlcode = 0)
```

```
               exec sql fetch c1 using descriptor sqlda;
```

```
               if (sqlca.sqlcode = 0) then
```

```
                    print the row using the results
```

```
                    (sqldata and sqlind)
```

```
                    pointed at by the sqlvar array;
```

```
               end if;
```

```

```

```
          end loop;
```

```

```

```
          free result variables from the sqlvar elements;
```

```

```

```
          exec sql close c1;
```

```

```

```
     end if;
```

```

```

```
     process the sqlca and print the status;
```

```

```

```
     read statement_buffer from the terminal;
```

```

```

```
end loop;
```
