---
title: "SQLCODE and SQLSTATE"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "SQLCODE_and_SQLSTATE.htm"
canonical_id: "actian-data-platform-sqlcode-and-sqlstate"
---

## SQLCODE and SQLSTATE

SQLCODE and SQLSTATE are variables in which the DBMS returns ANSI/ISO Entry-92-compliant status codes indicating the results of the last SQL statement that was executed.

### SQLCODE Variable

SQLCODE is an integer variable in which the DBMS returns the status of the last SQL statement executed.

!!! note "Note"

    The ANSI Entry SQL-92 specification describes SQLCODE as a deprecated feature and recommends using the SQLSTATE variable.

#### Values Returned by SQLCODE

The values returned in the standalone SQLCODE variable are the same as those returned in the sqlcode member of the SQLCA structure. The value of SQLCODE is meaningful only in the context of a session.

The values returned in SQLCODE are listed in the following table:

| Value | Description |
| --- | --- |
| 0 | Successful completion. |
| +100 | No rows were processed by a DELETE, FETCH, INSERT, SELECT, UPDATE, MODIFY, COPY, CREATE INDEX, or CREATE TABLE AS SELECT statement. This value (+100) sets the not found condition of the WHENEVER statement. |
| +700 | A message statement in a database procedure has just executed, setting the sqlmessage condition of the WHENEVER statement. |
| +710 | A database event was raised. |
| Negative Value | An error occurred. The value of SQLCODE is the negative value of the error number returned to errorno. For information on errorno, see [Error Checking Using Inquire Statements](../SQLLanguage/Error_Handling_in_Embedded_Applications.md). A negative value sets the sqlerror condition of the WHENEVER statement. |

### SQLSTATE Variable

The SQLSTATE variable is a 5-character string in which the Actian Data Platform returns the status of the last SQL statement executed. The values returned in SQLSTATE are specified in the ANSI/ISO Entry SQL-92 standard.

!!! note "Note"

    If queries are executed while connected to a DBMS server that does not support SQLSTATE, SQLSTATE is set to 5000K (meaning SQLSTATE not available). This result does not necessarily mean that an error occurred. To check the results of the query, use one of the other error-checking methods.

SQLSTATE is not available within database procedures; however, a routine that directly executes a database procedure can check SQLSTATE to determine the result of the procedure call.

The following example illustrates the use of SQLSTATE in an embedded program:

```
exec sql begin declare section;     character SQLSTATE(5)exec sql end declare section;\exec sql connect mydatabase;if SQLSTATE <> "00000" print 'Error on connection!'
```
