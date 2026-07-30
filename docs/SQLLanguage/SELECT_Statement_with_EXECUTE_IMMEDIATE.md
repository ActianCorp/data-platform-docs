---
title: "SELECT Statement with EXECUTE IMMEDIATE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SELECT_Statement_with_EXECUTE_IMMEDIATE.htm"
canonical_id: "actian-data-platform-select-statement-with-execute-immediate"
---

## SELECT Statement with EXECUTE IMMEDIATE

A dynamic SELECT statement can be executed if the statement has been prepared and described with an EXECUTE IMMEDIATE statement that includes the USING clause. The USING clause tells the Actian Data Platform to place the values returned by the select into the variables pointed to by the elements of the SQLDA sqlvar array. If the select returns more than one row, a select loop can also be defined to process each row before another is returned.

The syntax of EXECUTE IMMEDIATE in this context is:

```
EXEC SQL EXECUTE IMMEDIATE select_statement               USING [DESCRIPTOR] descriptor_name;[EXEC SQL BEGIN;               host_codeEXECT SQL END;]
```

Within a select loop, no SQL statements other than an ENDSELECT can be issued. For non-looped selects, the Actian Data Platform expects the select to return a single row, and issues an error if more than one row is returned.

To illustrate this option, the following program example contains a dynamic select whose results are used to generate a report:

```
allocate an sqldaread the dynamic select from the terminal into      a stmt_bufferexec sql prepare s1 from :stmt_buffer;exec sql describe s1 into :sqlda;if (sqlca.sqlcode < 0) or (sqlda.sqld = 0) then     print an error message           ('Error or statement is not a select');     return;else if (sqlda.sqld > sqlda.sqln) then      allocate a new sqlda;     exec sql describe s1 into :sqlda;endif;analyze the results and allocate variablesexec sql execute immediate :stmt_buffer     using descriptor :sqlda;exec sql begin;     process results, generating report     if error occurs, then          exec sql endselect;     endif;...exec sql end;
```
