---
title: "Types of Error Codes"
product: "Actian Data Platform"
guide: "SQL Language Guide"
source_file: "Types_of_Error_Codes.htm"
canonical_id: "actian-data-platform-types-of-error-codes"
---

## Types of Error Codes

Three types of error codes are returned to applications:

**Local errors**

:   Local errors are error codes specific to the DBMS.

**Generic errors**

:   Generic errors are a set of error codes that are mapped to the warehouse. Generic errors allow portable applications to be written.

**ANSI/ISO error codes**

:   SQLSTATE and SQLCODE are ANSI/ISO-compliant error code variables. (SQLCODE is supported but designated by ANSI/ISO Entry SQL-92 as a deprecated feature. SQLSTATE is the ANSI/ISO Entry SQL-92-compliant method for returning errors.)

By default, the DBMS returns generic and local errors as follows:

**Generic errors**

:   Returned in sqlcode (an SQLCA variable) as a negative value. (Also in the SQLCODE standalone variable.)

:   Returned when your application issues the INQUIRE_SQL(ERRORNO) statement.

**Local errors**

:   Returned in sqlerrd(1), the first element of the SQLCA sqlerrd array.

:   Returned when your application issues the INQUIRE_SQL(DBMSERROR) statement.

To reverse this arrangement (so that local error numbers are returned to errorno and sqlcode and generic errors to dbmserror and sqlerrd(1)), use the SET_SQL(ERRORTYPE) statement.

To obtain the text of error messages, use the INQUIRE_SQL(ERRORTEXT) statement or check the SQLCA variable sqlerrm.
