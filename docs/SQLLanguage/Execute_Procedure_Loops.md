---
title: "Execute Procedure Loops"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Execute_Procedure_Loops.htm"
canonical_id: "actian-data-platform-execute-procedure-loops"
---

## Execute Procedure Loops

Use an execute procedure loop to retrieve and process rows returned by a row-producing procedure using the RESULT ROW clause. The RESULT ROW clause identifies the host variables into which the values produced by the procedure return row statement are loaded. The entries in the RESULT ROW clause must match in both number and type the corresponding entries in the RESULT ROW declaration of the procedure.

The begin-end statements delimit the statements in the execute procedure loop. The code is executed once for each row as it is returned from the row-producing procedure. Statements cannot be placed between the EXECUTE PROCEDURE statement and the BEGIN statement.

During the execution of the execute procedure loop, no other statements that access the database can be issued; this causes a runtime error. However, if your program is connected to multiple database sessions, you can issue queries from within the execute procedure loop by switching to another session. To return to the outer execute procedure loop, switch back to the session in which the EXECUTE PROCEDURE statement was issued. To avoid preprocessor errors, the nested queries cannot be within the syntactic scope of the loop but must be referenced by a subroutine call or some form of a GOTO statement.

There are two ways to terminate an execute procedure loop: run it to completion or issue the ENDEXECUTE statement. A host language GOTO statement cannot be used to exit or return to the execute procedure loop.

To terminate an execute procedure loop before all rows are retrieved the application must issue the ENDEXECUTE statement. This statement must be syntactically within the begin-end block that delimits the ENDEXECUTE procedure loop.

The following example retrieves a set of rows from a row-producing procedure:

```
exec sql execute procedure deptsal_proc (deptid = :deptno) result row (:deptname, :avgsal, :empcount);exec sql begin; browse data;if error condition thenexec sql endexecute; end if;exec sql end;”
```
